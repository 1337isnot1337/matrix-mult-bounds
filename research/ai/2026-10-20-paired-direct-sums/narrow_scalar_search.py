"""Explicit scalar-extended narrow-source discovery.

Q_(n,b) direct_sum r scalar tensors -> M(n,b,n).  Added scalar coordinates
are part of the source and never silently removed from a claimed map.
The search reuses the full-coefficient unrestricted ALS implementation.
"""
import argparse
import importlib.util
from itertools import product
import json
from pathlib import Path


SPEC = importlib.util.spec_from_file_location("narrow_scalar_dependency",
                                             Path(__file__).with_name("narrow_source_search.py"))
NARROW = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(NARROW)
ORIGINAL_COORDINATES = NARROW.coordinates


def coordinates(n, b, scalars):
    if not isinstance(scalars, int) or scalars < 0:
        raise ValueError("the scalar count must be a nonnegative integer")
    source_shape, source, target_shape, target = ORIGINAL_COORDINATES(n, b)
    extended = tuple(size+scalars for size in source_shape)
    source = source+[tuple(size+i for size in source_shape) for i in range(scalars)]
    return extended, source, target_shape, target


def exact_control():
    source_shape, source, target_shape, target = coordinates(2, 2, 1)
    spec = importlib.util.spec_from_file_location("scalar_p2_control",
            NARROW.ROOT / "research/ai/2026-10-20-paired-construction/exact_p2.py")
    p2 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(p2)
    labels = [list(product(range(2), range(2))), list(product(range(2), range(3))),
              list(product(range(3), range(2)))]
    maps = []
    for k, substitution in enumerate(p2.maps()):
        matrix = [[0]*source_shape[k] for _ in range(target_shape[k])]
        for column, label in enumerate(labels[k]):
            coefficient, image = substitution[label]
            matrix[2*image[0]+image[1]][column] = coefficient
        maps.append(matrix)
    actual = NARROW.coefficient_contraction(source, maps)
    if actual != {term: 1 for term in target}:
        raise ArithmeticError("The scalar-extended full coefficient control failed")
    for axis in maps:
        axis[0][-1] = 1
    changed = NARROW.coefficient_contraction(source, maps)
    if changed.get((0, 0, 0), 0) != actual.get((0, 0, 0), 0)+1:
        raise ArithmeticError("The appended scalar source term was not accounted for")
    return {"source": "Q_(2,2) direct_sum one scalar", "source_shape": source_shape,
            "source_terms": len(source), "target_shape": target_shape,
            "exact_control_passed": True, "appended_scalar_term_checked": True,
            "scope": "Control only; the target uses the known P2 maps and sends the scalar to zero."}


def fit(n, b, scalars, seed, iterations, ridge, report_every, checkpoint):
    # This is a local adapter in the independently imported module. The
    # generator is restored immediately after fitting; no file is changed.
    NARROW.coordinates = lambda nn, bb: coordinates(nn, bb, scalars)
    try:
        report = NARROW.fit(n, b, seed, iterations, ridge, report_every, checkpoint)
    finally:
        NARROW.coordinates = ORIGINAL_COORDINATES
    report["source"] = f"Q_({n},{b}) direct_sum {scalars} scalar tensor(s)"
    report["scalar_summands"] = scalars
    report["scope"] = "Finite search on the explicitly enlarged source. No restriction of Q_(n,b) alone or exponent improvement follows."
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=3)
    parser.add_argument("--b", type=int, default=2)
    parser.add_argument("--scalars", type=int, default=1)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--iterations", type=int, default=1000)
    parser.add_argument("--ridge", type=float, default=1e-12)
    parser.add_argument("--report-every", type=int, default=200)
    parser.add_argument("--checkpoint", type=Path)
    parser.add_argument("--control", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = (exact_control() if args.control else fit(args.n, args.b, args.scalars, args.seed,
              args.iterations, args.ridge, args.report_every, args.checkpoint))
    args.output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({key: value for key, value in report.items() if key != "history"}, indent=2))
