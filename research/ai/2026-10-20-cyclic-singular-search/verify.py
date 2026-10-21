"""Exact certificates for two fixed-map extension attempts, not all degenerations."""
from fractions import Fraction
import importlib.util
from itertools import product
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "results/cyclic-singular-search-2026-10-20"
spec = importlib.util.spec_from_file_location(
    "mixed_map", Path(__file__).resolve().parents[1] / "2026-10-20-cyclic-mixed-map/verify.py")
mixed = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mixed)


def old_maps(kind):
    if kind == "integer-derived":
        data = mixed.load_maps()
        shapes = (6, 12, 8)
    elif kind == "earlier-rational":
        path = ROOT / "results/cyclic-mixed-map-2026-10-20/discovery/earlier-m233-rational-witness.json"
        data = mixed.load_maps(path)
        shapes = (6, 9, 6)
    else:
        raise ValueError("Unknown fixed witness")
    maps = []
    for entries, rows in zip(data, shapes):
        matrix = sp.zeros(rows, 12)
        for row, col, value in entries:
            matrix[row, col] = sp.Rational(value)
        maps.append(matrix)
    if kind == "integer-derived":
        maps[1] = maps[1][[4*j+k for j, k in product(range(3), repeat=2)], :]
        maps[2] = maps[2][:6, :]
    return maps


def contraction_matrices(kind):
    a, b, c = old_maps(kind)
    vc, va = sp.zeros(54, 12), sp.zeros(54, 12)
    for x, y, z in mixed.source_terms(2):
        for i, j in product(range(6), range(9)):
            vc[9*i+j, z] += a[i, x]*b[j, y]
        for j, k in product(range(9), range(6)):
            va[6*j+k, x] += b[j, y]*c[k, z]
    return {"new-C": vc, "new-A": va}


def verify_certificate(certificate):
    records = []
    for kind in ("integer-derived", "earlier-rational"):
        matrices = contraction_matrices(kind)
        for leg, matrix in matrices.items():
            item = certificate[kind][leg]
            rows, cols = item["rows"], item["columns"]
            rank = len(rows)
            assert len(cols) == rank
            determinant = matrix.extract(rows, cols).det()
            assert determinant != 0 and determinant == sp.Rational(item["determinant"])
            vectors = item["kernel_basis"]
            kernel = sp.Matrix(12, len(vectors), lambda i, j: sp.Rational(vectors[j][i]))
            assert len(vectors)+rank == 12
            assert matrix*kernel == sp.zeros(54, len(vectors))
            assert kernel.rank() == len(vectors)
            records.append({"fixed_maps": kind, "new_leg": leg, "rank": rank,
                            "kernel_dimension": len(vectors), "minor_determinant": str(determinant)})
    return records


def mask_escape(r):
    """Exact M2 target-vertex gauge example: a negative and a positive error."""
    u, v, w = (0, 1), (0, 2), (0, 4)
    weights = ([u[i]+v[j] for i, j in product(range(2), repeat=2)],
               [-v[j]+w[k] for j, k in product(range(2), repeat=2)],
               [-w[k]-u[i] for k, i in product(range(2), repeat=2)])
    degree = lambda point: sum(weights[axis][point[axis]] for axis in range(3))
    assert all(degree(point) == 0 for point in mixed.target_terms(2, 2, 2))
    negative, positive = (0, 0, 1), (2, 0, 0)
    assert degree(negative) == -1 and degree(positive) == 1
    residual = Fraction(r)**degree(negative)
    omitted = Fraction(r)**degree(positive)
    return residual, omitted, residual**2+omitted**2


def report():
    certificate = json.loads((RESULTS / "fixed-extension-certificate.json").read_text())
    records = verify_certificate(certificate)
    assert [r["kernel_dimension"] for r in records] == [2, 0, 0, 0]
    assert all(mask_escape(r) == (Fraction(1, r), Fraction(r), Fraction(1, r*r)+r*r)
               for r in (2, 3, 10))
    return {"field": "C (rational certificate)", "fixed_map_records": records,
            "excluded_class": "Fixed old maps with one-sided new-vertex grading, in either direction",
            "general_degeneration_excluded": False, "new_exponent_established": False}


if __name__ == "__main__":
    print(json.dumps(report(), indent=2))
