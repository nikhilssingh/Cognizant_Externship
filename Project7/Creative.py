import argparse, json, random, time
from pathlib import Path

import torch
from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer,
    EarlyStoppingCallback,
    default_data_collator,
    set_seed,
)


def augment(example):
    sents = example["text"].split(".")
    if len(sents) > 1 and random.random() < 0.3:
        i = random.randint(0, len(sents) - 2)
        sents[i], sents[i + 1] = sents[i + 1], sents[i]
    example["text"] = ".".join(sents)
    return example


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model", default="distilbert-base-uncased")
    p.add_argument("--epochs", type=int, default=2)
    p.add_argument("--batch_size", type=int, default=16)
    p.add_argument("--lr", type=float, default=5e-5)
    p.add_argument("--output_dir", default="creative_out")
    p.add_argument("--seed", type=int, default=42)
    args = p.parse_args()

    set_seed(args.seed)
    ds = load_dataset("amazon_polarity", split="train[:10%]")  # small subset
    ds = ds.map(augment)

    tokenizer = AutoTokenizer.from_pretrained(args.model)
    def tok(b):
        return tokenizer(b["text"], truncation=True, padding="max_length")
    ds = ds.map(tok, batched=True, remove_columns=["text", "title"])
    ds = ds.rename_column("label", "labels").with_format("torch")
    ds = ds.train_test_split(test_size=0.1)

    model = AutoModelForSequenceClassification.from_pretrained(args.model, num_labels=2)

    targs = TrainingArguments(
        output_dir=args.output_dir,
        evaluation_strategy="epoch",
        learning_rate=args.lr,
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=args.batch_size*2,
        num_train_epochs=args.epochs,
        weight_decay=0.01,
        fp16=True,
        logging_steps=50,
        save_total_limit=2,
    )

    trainer = Trainer(
        model,
        targs,
        train_dataset=ds["train"],
        eval_dataset=ds["test"],
        tokenizer=tokenizer,
        data_collator=default_data_collator,
        callbacks=[EarlyStoppingCallback(early_stopping_patience=1)],
    )
    trainer.train()
    metrics = trainer.evaluate()
    Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    with open(Path(args.output_dir)/"creative_metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)
    print(metrics)


if __name__ == "__main__":
    main()
