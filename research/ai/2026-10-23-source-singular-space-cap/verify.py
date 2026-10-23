"""Exact unit packing, source action and sharp zero-row kernel certificates.

The all-subspace limit and Laurent application are written proofs, not
finite enumeration over complex subspaces.
"""
import argparse
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULT = ROOT / "results/source-singular-space-cap-2026-10-23/certificate.json"
N, PRIME = 112, 1009
ROWS = list(product(range(4), range(4), range(7)))
COLS = list(product(range(7), range(4), range(4)))
COEFFS = list(product(range(4), range(7), range(4)))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def index(i, k, z):
    return (i*7+k)*4+z


def source_matrix(coefficients):
    require(len(coefficients) == N, "Wrong source coefficient count")
    return [[coefficients[index(h-j, p+q, ell-r)]
             if 0 <= h-j < 4 and 0 <= ell-r < 4 else 0
             for h, q, r in COLS] for j, p, ell in ROWS]


def determinant_mod(matrix, prime):
    a = [[int(x) % prime for x in row] for row in matrix]
    n, determinant = len(a), 1
    require(all(len(row) == n for row in a), "Nonsquare source matrix")
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            determinant = -determinant
        value = a[j][j]
        determinant = determinant*value % prime
        inverse = pow(value, -1, prime)
        for i in range(j+1, n):
            multiplier = a[i][j]*inverse % prime
            if multiplier:
                for k in range(j+1, n):
                    a[i][k] = (a[i][k]-multiplier*a[j][k]) % prime
                a[i][j] = 0
    return determinant % prime


def check_sources(record=None):
    record = json.loads((PACKAGE / "sources.json").read_text()) if record is None else record
    expected = {"research/ai/2026-10-21-cyclic-slice-determinants/certify.py",
                "research/ai/2026-10-20-koszul/cyclic_finite_target.md",
                "research/ai/2026-10-23-partial-regular-frames/proof.md"}
    entries = record["local_dependencies"]
    require(len(entries) == 3 and {x["path"] for x in entries} == expected,
            "Changed dependency inventory")
    for entry in entries:
        require(hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest() == entry["sha256"],
                "Changed source: " + entry["path"])
    return len(entries)


def short_matrix(c):
    return s.Matrix([[int(0 <= h-j < 4 and 0 <= ell-r < 4
                           and (h-j+ell-r) % 4 == c)
                      for h, r in product(range(7), range(4))]
                     for j, ell in product(range(4), range(7))])


def build():
    check_sources()
    short = [short_matrix(c) for c in range(4)]
    short_determinants = [int(k.det(method="domain-ge")) for k in short]
    require(short_determinants == [-1, 1, -1, 1], "Short source unit determinants changed")
    weights = [i+4*k+28*z for i, k, z in COEFFS]
    require(sorted(weights) == list(range(N)), "Source weights are not distinct")
    allowed_entries = 0
    for j, p, ell in ROWS:
        for h, q, r in COLS:
            if 0 <= h-j < 4 and 0 <= ell-r < 4:
                weight = weights[index(h-j, p+q, ell-r)]
                require(weight == -j+4*p+28*ell+h+4*q-28*r,
                        "Source weight does not separate into row and column weights")
                allowed_entries += 1
    witnesses, covered = [], []
    row_permutation = [ROWS.index((j, p, ell))
                       for p, j, ell in product(range(4), range(4), range(7))]
    col_permutation = [COLS.index((h, q, r))
                       for q, h, r in product(range(4), range(7), range(4))]
    for c, d in product(range(4), repeat=2):
        support = [n for n, (i, k, z) in enumerate(COEFFS) if (i+z) % 4 == c and k % 4 == d]
        f = [int(n in support) for n in range(N)]
        matrix = source_matrix(f)
        determinant = determinant_mod(matrix, PRIME)
        require(determinant in (1, PRIME-1), "Source unit is not modularly unimodular")
        middle = s.Matrix(4, 4, lambda p, q: int((p+q) % 4 == d))
        require(abs(middle.det()) == 1, "Middle block is not a permutation unit")
        # A second integer engine, with all entries of the factorization checked.
        for i, ri in enumerate(row_permutation):
            for j, cj in enumerate(col_permutation):
                require(matrix[ri][cj] == middle[i//28, j//28]*short[c][i % 28, j % 28],
                        "Literal source/Kronecker factorization mismatch")
        witnesses.append({"c": c, "d": d, "coefficient_one_support": support,
                          "determinant_mod1009": determinant,
                          "absolute_integer_determinant": 1})
        covered.extend(support)
    require(sorted(covered) == list(range(N)), "Supports do not partition the source")
    # Literal source row(0,0,0) imposes these16 independent coordinates.
    kernel_constraints = [index(i, k, 0) for i, k in product(range(4), repeat=2)]
    row_contraction = s.zeros(N, N)
    for col, (h, q, r) in enumerate(COLS):
        if h < 4 and r == 0:
            row_contraction[col, index(h, q, 0)] = 1
    require(row_contraction.rank() == 16, "Sharp row contraction rank changed")
    free = [i for i in range(N) if i not in kernel_constraints]
    require(len(free) == 96 and row_contraction[:, free] == s.zeros(N, 96),
            "Sharp all-singular kernel failed")
    return {"source_dimension": N, "coefficient_field": "C",
            "proof_status": "proof-written-unreviewed", "improves_omega": False,
            "all_singular_subspace_dimension_cap": 96, "minimum_for_forced_unit": 97,
            "source_weights": weights, "allowed_source_entries_checked": allowed_entries,
            "short_integer_determinants": short_determinants,
            "unit_witnesses": witnesses, "literal_factorization_entries_checked": 16*N*N,
            "sharp_kernel_zero_row": [0, 0, 0],
            "sharp_kernel_constraints": kernel_constraints, "sharp_kernel_dimension": 96,
            "scope": "Finite exact units/action/kernel evidence; all-complex-subspace cap and Laurent consequence are written proofs."}


def verify(record):
    require(record == build(), "Changed units, weights, sharp cap or mathematical scope")
    return {"unit_witnesses": 16, "partitioned_source_coordinates": N,
            "literal_factorization_entries_checked": 16*N*N,
            "source_weight_entries_checked": record["allowed_source_entries_checked"],
            "sharp_kernel_dimension": 96, "improves_omega": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    if args.write:
        RESULT.parent.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(json.dumps(build(), indent=2, sort_keys=True) + "\n")
    print(json.dumps(verify(json.loads(RESULT.read_text())), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
