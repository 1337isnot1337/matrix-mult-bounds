"""Complete the two ordered input roles in the historical finite search."""
import argparse
from fractions import Fraction
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path

from verify import check_report, coverage


ROOT = Path(__file__).resolve().parents[3]
SOURCES = json.loads(Path(__file__).with_name("sources.json").read_text())
SOURCE = SOURCES["local_sources"][0]
ARCHIVE_PATH = ROOT / SOURCE["path"]
if hashlib.sha256(ARCHIVE_PATH.read_bytes()).hexdigest() != SOURCE["sha256"]:
    raise ValueError("historical discovery source hash mismatch")
SPEC = importlib.util.spec_from_file_location("archived_monomial_discovery", ARCHIVE_PATH)
ARCHIVE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ARCHIVE)


def candidate(x, y, h):
    sectors, output_weights = ARCHIVE.components(x, y)
    sectors = sorted(tuple(sorted(sector)) for sector in sectors)
    blocks = [ARCHIVE.recognize(sector) for sector in sectors]
    for block in blocks:
        if "reversals" in block:
            block["reversals"] = list(block["reversals"])
    source = ARCHIVE.profile(len(x), len(y), h)
    target = sum((ARCHIVE.profile(b["a"], b["b"], h) for b in blocks), Fraction())
    return {
        "weights": [list(x), list(y)],
        "support": {
            "dimensions": [len(x), len(y), len(x) + len(y) - 1],
            "output_weights": output_weights,
            "terms": [list(term) for term in sorted(t for s in sectors for t in s)],
            "sectors": [[list(term) for term in s] for s in sectors],
        },
        "blocks": blocks,
        "score": {"source": str(source), "target": str(target), "ratio": str(target / source)},
    }


def key(record):
    return (-Fraction(record["score"]["ratio"]),
            tuple(record["support"]["dimensions"]),
            tuple(record["weights"][0]), tuple(record["weights"][1]))


def run(q, max_sum, top_k=5):
    if q < 2 or max_sum < 4 or top_k < 1:
        raise ValueError("need q >= 2, max_sum >= 4 and top_k >= 1")
    arrays = {n: [w for w in product(range(q), repeat=n) if min(w) == 0]
              for n in range(2, max_sum - 1)}
    h = ARCHIVE.slopes(max_sum)
    rows = {"historical": {}, "omitted": {}}
    leaders = {scope: [] for scope in rows}
    comparison = {"same": 0, "omitted_better": 0, "historical_better": 0, "witnesses": {}}

    def accept(record):
        a, b = record["support"]["dimensions"][:2]
        scope = "historical" if a <= b else "omitted"
        ratio = Fraction(record["score"]["ratio"])
        row = rows[scope].setdefault((a, b), {"cases": 0, "violations": 0, "best_ratio": Fraction()})
        row["cases"] += 1
        row["violations"] += ratio > 1
        row["best_ratio"] = max(row["best_ratio"], ratio)
        top = leaders[scope]
        if len(top) < top_k or key(record) < key(top[-1]):
            top.append(record)
            top.sort(key=key)
            del top[top_k:]
        return ratio

    for a in range(2, max_sum - 1):
        for b in range(a, max_sum - a + 1):
            for x in arrays[a]:
                for y in arrays[b]:
                    original = candidate(x, y, h)
                    left = accept(original)
                    if a != b:
                        reversed_record = candidate(y, x, h)
                        right = accept(reversed_record)
                        relation = "same" if left == right else "omitted_better" if right > left else "historical_better"
                        comparison[relation] += 1
                        if relation != "same" and relation not in comparison["witnesses"]:
                            comparison["witnesses"][relation] = [original, reversed_record]
            print(f"completed ordered dimensions {a},{b}", flush=True)

    summaries = {
        scope: [{"dimensions": list(dims), **row, "best_ratio": str(row["best_ratio"])}
                for dims, row in sorted(by_dim.items())]
        for scope, by_dim in rows.items()
    }
    counts = {scope: sum(row["cases"] for row in records) for scope, records in summaries.items()}
    counts["ordered"] = sum(counts.values())
    if counts != coverage(q, max_sum):
        raise ValueError("completed enumeration differs from independent count formula")
    report = {
        "schema_version": 1, "alphabet_size": q, "max_sum": max_sum, "top_k": top_k,
        "coverage": counts, "dimension_summaries": summaries, "leaders": leaders,
        "orientation_comparison": comparison,
        "scope": "All ordered lengths a,b >= 2 with a+b <= max_sum, normalized weights in range(q), first input shared. Finite score only; no exponent improvement.",
    }
    report["acceptance"] = check_report(report)
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--alphabet-size", type=int, required=True)
    parser.add_argument("--max-sum", type=int, required=True)
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = run(args.alphabet_size, args.max_sum, args.top_k)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"coverage": report["coverage"], "acceptance": report["acceptance"]}))
