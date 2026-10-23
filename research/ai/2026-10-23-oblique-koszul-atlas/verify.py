#!/usr/bin/env python3
"""Exact full-space Koszul ranks of three fixed oblique residuals.

Only integer unit row operations are accepted. The resulting ranks hold
over every field, rather than just over Q or a sampled finite field.
"""

import argparse
import hashlib
import importlib.util
from itertools import combinations
import json
from math import comb
from pathlib import Path


PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]
PARENT = ROOT / "research/ai/2026-10-23-oblique-border-equalizer"
SPEC = importlib.util.spec_from_file_location("oblique_atlas_source", PARENT / "verify.py")
SOURCE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SOURCE)


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                    separators=(",", ":")).encode()).hexdigest()


def koszul_rows(shape, tensor, leg, degree):
    """Contract the first remaining leg; wedge on the selected leg.

    All labels use increasing exterior basis order. Zero matrix rows are
    omitted, but the full domain and codomain dimensions are returned.
    """
    if leg not in (0, 1, 2) or not 0 <= degree < shape[leg]:
        raise ValueError("Require a tensor leg and a degree below its dimension")
    first, last = [i for i in range(3) if i != leg]
    d = shape[leg]
    inputs = list(combinations(range(d), degree))
    outputs = {w: i for i, w in enumerate(combinations(range(d), degree + 1))}
    rows = {}
    for key, coefficient in sorted(tensor.items()):
        x, b, c = key[leg], key[first], key[last]
        for column_wedge, wedge in enumerate(inputs):
            if x in wedge:
                continue
            target = tuple(sorted((*wedge, x)))
            sign = (-1) ** sum(y < x for y in wedge)
            row_label = outputs[target] * shape[last] + c
            column = column_wedge * shape[first] + b
            row = rows.setdefault(row_label, {})
            row[column] = row.get(column, 0) + sign * coefficient
    rows = {label: {c: v for c, v in row.items() if v}
            for label, row in rows.items() if any(row.values())}
    return rows, [shape[last] * comb(d, degree + 1),
                  shape[first] * comb(d, degree)]


def unit_rank(rows):
    """Reduce the entire matrix using unimodular row operations.

    Distinct pivot columns give a triangular unit minor. Every other row
    reduces to zero, proving the matching upper bound over every field.
    A nonunit pivot fails closed and is never treated as invertible.
    """
    pivots = {}
    witness = []
    for label, source in sorted(rows.items()):
        row = dict(source)
        while row:
            column = min(row)
            value = row[column]
            if column not in pivots:
                require(value in (-1, 1), "Nonunit pivot: no all-field rank decision")
                pivots[column] = {c: v * value for c, v in row.items()}
                witness.append([label, column, value])
                break
            for c, v in pivots[column].items():
                new = row.get(c, 0) - value * v
                if new:
                    row[c] = new
                else:
                    row.pop(c, None)
    return {"rank": len(pivots), "unit_pivot_sha256": digest(witness),
            "nonzero_rows_reduced": len(rows), "nonunit_pivots": 0}


def source_pins(record=None):
    record = record or json.loads((PACKAGE / "sources.json").read_text())
    for item in record["local_sources"]:
        require(hashlib.sha256((ROOT / item["path"]).read_bytes()).hexdigest()
                == item["sha256"], "Changed source bytes: " + item["path"])
    return {"count": len(record["local_sources"]), "all_match": True}


def build_certificate():
    pins = source_pins()
    controls = []
    for b in (2, 3, 4):
        shape, tensor = SOURCE.canonical_residual(b)
        atlas = []
        for leg in range(3):
            for degree in range(shape[leg]):
                rows, matrix_shape = koszul_rows(shape, tensor, leg, degree)
                decision = unit_rank(rows)
                divisor = comb(shape[leg] - 1, degree)
                atlas.append({"leg": leg, "degree": degree,
                              "matrix_shape": matrix_shape, **decision,
                              "rank_one_divisor": divisor,
                              "border_rank_lower_bound":
                              (decision["rank"] + divisor - 1) // divisor})
        controls.append({"b": b, "n": b + 2, "concise_shape": shape,
                         "tensor_sha256": digest(SOURCE.records(tensor)),
                         "all_degrees_and_legs": atlas,
                         "strongest_full_space_koszul_bound":
                         max(row["border_rank_lower_bound"] for row in atlas),
                         "inherited_equalizer_lower_bound": 2 * b + 4})
    return {"claim": "EXP-OBLIQUE-KOSZUL-ATLAS-001",
            "field_scope": "Every field, by complete integer unit elimination",
            "source_pin_verification": pins,
            "native_n6_control": SOURCE.replay_native(ROOT),
            "controls": controls,
            "matrices_reduced": sum(len(c["all_degrees_and_legs"]) for c in controls),
            "projected_koszul_optimality_claimed": False,
            "border_rank_optimality_claimed": False,
            "independent_mathematical_review": False,
            "improves_omega": False}


def verify_saved(path):
    report = build_certificate()
    require(json.loads(Path(path).read_text()) == report, "Saved atlas differs from replay")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.output:
        report = build_certificate()
        args.output.write_text(json.dumps(report, indent=2) + "\n")
    else:
        report = verify_saved(PACKAGE / "certificate.json")
    print(json.dumps({"matrices_reduced": report["matrices_reduced"],
                      "strongest_bounds": [c["strongest_full_space_koszul_bound"]
                                           for c in report["controls"]],
                      "native_source_replayed": True, "status": "passed"}))


if __name__ == "__main__":
    main()
