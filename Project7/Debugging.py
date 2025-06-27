import argparse, json, shutil, time
from pathlib import Path
from copy import deepcopy

from FineTuningBert import train_eval  


def run_case(case_args, tag):
    out_dir = Path("debug_runs") / tag
    case_args.output_dir = str(out_dir)
    train_eval(case_args)
    metrics = json.load(open(list(out_dir.glob("*/metrics.json"))[0]))
    json.dump(metrics, open(f"debug_{tag}.json", "w"), indent=2)
    return metrics


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", choices=["v1", "v2"], default="v2")
    args = ap.parse_args()

    # BAD settings
    bad = argparse.Namespace(
        version=args.version,
        model="bert-base-uncased",
        epochs=1,
        batch_size=12,
        lr=1e-4,
        seed=123,
        output_dir="bad",
        fp16=False,
    )
    good = deepcopy(bad)
    good.lr = 3e-5
    good.epochs = 2
    good.output_dir = "good"

    m_bad = run_case(bad, "before")
    m_good = run_case(good, "after")

    print("--- Debug result ---")
    print("Before: EM={:.2f} F1={:.2f}".format(m_bad.get("exact_match", 0), m_bad.get("f1", 0)))
    print("After : EM={:.2f} F1={:.2f}".format(m_good.get("exact_match", 0), m_good.get("f1", 0)))


if __name__ == "__main__":
    main()
