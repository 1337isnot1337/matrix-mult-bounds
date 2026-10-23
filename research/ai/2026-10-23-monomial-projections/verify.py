"""Optimize the archived score over projections on the two nonshared axes."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
import argparse
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PINS = json.loads(Path(__file__).with_name("sources.json").read_text())
SOURCE = ROOT / PINS["recognition"]["path"]
if hashlib.sha256(SOURCE.read_bytes()).hexdigest() != PINS["recognition"]["sha256"]:
    raise ValueError("recognition source does not match its byte pin")
SPEC = importlib.util.spec_from_file_location("projection_recognition", SOURCE)
BASE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BASE)


def components(terms):
    unseen = set(terms)
    groups = []
    while unseen:
        seed = min(unseen)
        unseen.remove(seed)
        group, ys, zs = {seed}, {seed[1]}, {seed[2]}
        while True:
            new = {t for t in unseen if t[1] in ys or t[2] in zs}
            if not new:
                break
            group.update(new)
            unseen.difference_update(new)
            ys.update(t[1] for t in new)
            zs.update(t[2] for t in new)
        groups.append(tuple(sorted(group)))
    return tuple(sorted(groups))


@lru_cache(None)
def profile(a, b):
    return BASE.ARCHIVE.profile(a, b, BASE.ARCHIVE.slopes(min(a, b)))


def block_score(terms):
    block = BASE.recognize(terms)
    if block is not None:
        return profile(block["a"], block["b"])
    return Fraction(max(max(Counter(t[k] for t in terms).values()) for k in range(3)))


def component_score(terms):
    return sum((block_score(g) for g in components(terms)), Fraction())


@lru_cache(None)
def optimize(terms):
    """Return (exact optimum, an induced support attaining it)."""
    if not terms:
        return Fraction(), ()
    groups = components(terms)
    if len(groups) > 1:
        results = [optimize(g) for g in groups]
        return sum((s for s, _ in results), Fraction()), tuple(sorted(
            t for _, kept in results for t in kept))
    best = (block_score(terms), terms)
    for axis in (1, 2):
        for value in sorted({t[axis] for t in terms}):
            candidate = optimize(tuple(t for t in terms if t[axis] != value))
            if (candidate[0], len(candidate[1]), candidate[1]) > (
                best[0], len(best[1]), best[1]
            ):
                best = candidate
    return best


def original_support(wx, wy):
    groups, _ = BASE.ARCHIVE.components(wx, wy)
    return tuple(sorted(t for g in groups for t in g))


def make_record(wx, wy):
    terms = original_support(wx, wy)
    value, kept = optimize(terms)
    return {"weights": [list(wx), list(wy)],
            "keep_y": sorted({t[1] for t in kept}),
            "keep_z": sorted({t[2] for t in kept}),
            "projected_terms": [list(t) for t in kept],
            "source_exact": str(profile(len(wx), len(wy))),
            "old_score_exact": str(component_score(terms)),
            "projected_score_exact": str(value),
            "ratio_exact": str(value / profile(len(wx), len(wy)))}


def replay_record(record):
    """Check an achieved projection score without using optimize()."""
    wx, wy = map(tuple, record["weights"])
    terms = original_support(wx, wy)
    ys, zs = set(record["keep_y"]), set(record["keep_z"])
    if record["keep_y"] != sorted(ys) or record["keep_z"] != sorted(zs):
        raise ValueError("coordinate masks must be sorted sets")
    if not ys <= {t[1] for t in terms} or not zs <= {t[2] for t in terms}:
        raise ValueError("projection mask contains an unknown coordinate")
    kept = tuple(t for t in terms if t[1] in ys and t[2] in zs)
    source, value = profile(len(wx), len(wy)), component_score(kept)
    if (record["projected_terms"] != [list(t) for t in kept]
            or record["source_exact"] != str(source)
            or record["old_score_exact"] != str(component_score(terms))
            or record["projected_score_exact"] != str(value)
            or record["ratio_exact"] != str(value/source)):
        raise ValueError("projection certificate does not replay")


def run(q, max_sum):
    count = improved = violations = 0
    best = first_improvement = None
    for a in range(2, max_sum-1):
        for b in range(2, max_sum-a+1):
            for wx in product(range(q), repeat=a):
                if min(wx) != 0:
                    continue
                for wy in product(range(q), repeat=b):
                    if min(wy) != 0:
                        continue
                    record = make_record(wx, wy)
                    count += 1
                    if Fraction(record["projected_score_exact"]) > Fraction(record["old_score_exact"]):
                        improved += 1
                        if first_improvement is None:
                            first_improvement = record
                    violations += Fraction(record["ratio_exact"]) > 1
                    if best is None or Fraction(record["ratio_exact"]) > Fraction(best["ratio_exact"]):
                        best = record
    if count != BASE.expected_count(q, max_sum):
        raise AssertionError("incomplete ordered census")
    witness = make_record((0, 0, 1), (0, 0, 0))
    for record in (best, first_improvement, witness):
        if record is not None:
            replay_record(record)
    return {"parameters": {"alphabet_size": q, "max_sum": max_sum},
            "cases_tested": count, "strict_score_improvements": improved,
            "exact_violation_count": violations, "best": best,
            "first_improvement": first_improvement, "worked_example": witness,
            "scope": "Exact optimum of the existing whole-convolution/slice-fallback "
                     "component score over y/z coordinate projections only, in the "
                     "specified ordered finite weight census. Scores on old supports; "
                     "no arbitrary-basis or exponent conclusion."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--alphabet-size", type=int, choices=(2, 3), default=2)
    parser.add_argument("--max-sum", type=int, default=8)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.max_sum < 4:
        parser.error("max-sum must be at least four")
    report = run(args.alphabet_size, args.max_sum)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: report[k] for k in ("cases_tested", "strict_score_improvements",
                                           "exact_violation_count")}))


if __name__ == "__main__":
    main()
