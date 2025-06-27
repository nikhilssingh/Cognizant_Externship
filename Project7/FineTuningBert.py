import argparse, json, os, random, time
from pathlib import Path
from typing import Dict, List

import numpy as np
import torch
from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForQuestionAnswering,
    TrainingArguments,
    Trainer,
    default_data_collator,
    set_seed,
)

def prepare_train_features(examples, tokenizer, max_length, doc_stride):
    tokenized_examples = tokenizer(
        examples["question"],
        examples["context"],
        truncation="only_second",
        max_length=max_length,
        stride=doc_stride,
        return_overflowing_tokens=True,
        return_offsets_mapping=True,
        padding="max_length",
    )

    sample_mapping = tokenized_examples.pop("overflow_to_sample_mapping")
    offset_mapping = tokenized_examples.pop("offset_mapping")

    tokenized_examples["start_positions"] = []
    tokenized_examples["end_positions"] = []

    for i, offsets in enumerate(offset_mapping):
        input_ids = tokenized_examples["input_ids"][i]
        cls_index = input_ids.index(tokenizer.cls_token_id)

        sequence_ids = tokenized_examples.sequence_ids(i)
        sample_index = sample_mapping[i]
        answers = examples["answers"][sample_index]
        if len(answers["answer_start"]) == 0:
            tokenized_examples["start_positions"].append(cls_index)
            tokenized_examples["end_positions"].append(cls_index)
            continue

        start_char = answers["answer_start"][0]
        end_char = start_char + len(answers["text"][0])

        token_start_index = 0
        while sequence_ids[token_start_index] != 1:
            token_start_index += 1
        token_end_index = len(input_ids) - 1
        while sequence_ids[token_end_index] != 1:
            token_end_index -= 1

        if not (offsets[token_start_index][0] <= start_char and offsets[token_end_index][1] >= end_char):
            tokenized_examples["start_positions"].append(cls_index)
            tokenized_examples["end_positions"].append(cls_index)
        else:
            while token_start_index < len(offsets) and offsets[token_start_index][0] <= start_char:
                token_start_index += 1
            token_start_index -= 1
            while offsets[token_end_index][1] >= end_char:
                token_end_index -= 1
            token_end_index += 1
            tokenized_examples["start_positions"].append(token_start_index)
            tokenized_examples["end_positions"].append(token_end_index)
    return tokenized_examples


def prepare_validation_features(examples, tokenizer, max_length, doc_stride):
    tokenized_examples = tokenizer(
        examples["question"],
        examples["context"],
        truncation="only_second",
        max_length=max_length,
        stride=doc_stride,
        return_overflowing_tokens=True,
        return_offsets_mapping=True,
        padding="max_length",
    )
    sample_mapping = tokenized_examples.pop("overflow_to_sample_mapping")
    tokenized_examples["example_id"] = []
    for i in range(len(tokenized_examples["input_ids"])):
        sequence_ids = tokenized_examples.sequence_ids(i)
        context_index = 1
        sample_index = sample_mapping[i]
        tokenized_examples["example_id"].append(examples["id"][sample_index])
        tokenized_examples["offset_mapping"][i] = [
            (o if sequence_ids[k] == context_index else None)
            for k, o in enumerate(tokenized_examples["offset_mapping"][i])
        ]
    return tokenized_examples


def postprocess_qa_predictions(examples, features, raw_predictions, n_best_size=20, max_answer_length=30):
    from collections import OrderedDict

    all_start_logits, all_end_logits = raw_predictions
    example_id_to_index = {k: i for i, k in enumerate(examples["id"])}
    features_per_example = {}
    for i, feat in enumerate(features):
        example_id = feat["example_id"]
        if example_id not in features_per_example:
            features_per_example[example_id] = []
        features_per_example[example_id].append(i)

    predictions = OrderedDict()
    for example_id, feat_indices in features_per_example.items():
        context = examples[example_id]["context"]
        best_score = -1e6
        best_answer = ""
        for idx in feat_indices:
            start_logits = all_start_logits[idx]
            end_logits = all_end_logits[idx]
            offset_mapping = features[idx]["offset_mapping"]
            input_ids = features[idx]["input_ids"]
            cls_score = start_logits[0] + end_logits[0]

            start_indexes = np.argsort(start_logits)[-1:-n_best_size - 1:-1].tolist()
            end_indexes = np.argsort(end_logits)[-1:-n_best_size - 1:-1].tolist()
            for s in start_indexes:
                for e in end_indexes:
                    if e < s or e - s + 1 > max_answer_length:
                        continue
                    if offset_mapping[s] is None or offset_mapping[e] is None:
                        continue
                    start_char = offset_mapping[s][0]
                    end_char = offset_mapping[e][1]
                    answer = context[start_char:end_char]
                    score = start_logits[s] + end_logits[e]
                    if score > best_score:
                        best_score = score
                        best_answer = answer
        predictions[example_id] = best_answer
    return predictions



def train_eval(args):
    set_seed(args.seed)
    run_name = f"{args.model.replace('/', '-')}_{args.version}_{int(time.time())}"
    out_dir = Path(args.output_dir) / run_name
    out_dir.mkdir(parents=True, exist_ok=True)

    ds = load_dataset("squad_v2" if args.version == "v2" else "squad")
    tokenizer = AutoTokenizer.from_pretrained(args.model, use_fast=True)
    max_len = 384
    doc_stride = 128
    tokenized_train = ds["train"].map(
        lambda ex: prepare_train_features(ex, tokenizer, max_len, doc_stride),
        batched=True,
        remove_columns=ds["train"].column_names,
    )
    tokenized_val = ds["validation"].map(
        lambda ex: prepare_validation_features(ex, tokenizer, max_len, doc_stride),
        batched=True,
        remove_columns=ds["validation"].column_names,
    )

    model = AutoModelForQuestionAnswering.from_pretrained(args.model)

    targs = TrainingArguments(
        output_dir=str(out_dir),
        do_eval=True,      
        learning_rate=args.lr,
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=max(8, args.batch_size),
        num_train_epochs=args.epochs,
        weight_decay=0.01,
        fp16=args.fp16,
        seed=args.seed,
        logging_steps=100,
)


    trainer = Trainer(
        model,
        targs,
        train_dataset=tokenized_train,
        eval_dataset=tokenized_val,
        tokenizer=tokenizer,
        data_collator=default_data_collator,
    )
    trainer.train()

    # Evaluation
    import evaluate, numpy as np
    metric = evaluate.load("squad_v2" if args.version == "v2" else "squad")
    raw_preds = trainer.predict(tokenized_val)
    start_logits, end_logits = raw_preds.predictions

    final_preds = postprocess_qa_predictions(
        ds["validation"], tokenized_val, (start_logits, end_logits)
    )

    formatted_preds = [
        {"id": k, "prediction_text": v, "no_answer_probability": 0.0}
        for k, v in final_preds.items()
    ]
    refs = [
        {"id": ex["id"], "answers": ex["answers"]}
        for ex in ds["validation"]
    ]
    metrics = metric.compute(predictions=formatted_preds, references=refs)

    # Saving metrics
    with open(out_dir / "metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)
    print("Final EM/F1:", metrics)

    trainer.save_model(str(out_dir / "model"))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--version", choices=["v1", "v2"], default="v2")
    p.add_argument("--model", default="bert-base-uncased")
    p.add_argument("--epochs", type=int, default=2)
    p.add_argument("--batch_size", type=int, default=12)
    p.add_argument("--lr", type=float, default=3e-5)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--output_dir", default="outputs")
    p.add_argument("--fp16", action="store_true")
    args = p.parse_args()
    train_eval(args)
