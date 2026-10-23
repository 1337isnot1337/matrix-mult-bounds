"""Exact, standard-library certificates for the second-leg Koszul obstruction.

The tensor coefficients, all matrices, and both endpoints are defined here.
Certificate discovery uses reduced row echelon form.  Acceptance uses a
separate Bareiss determinant and literal multiplication of kernel vectors.
No closed convolution rank formula or numerical rank test is imported.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
from itertools import combinations
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "results/shared-output-koszul-2026-10-23"
SOURCE = ["E4"] * 10
TARGET = ["E3"] * 10 + ["E2"] + ["O"] * 2
EXPECTED_INTRINSIC = {"E4": 21, "E3": 12, "E2": 5, "O": 8}
EXPECTED_CROSS = {
    "E4/E4": 53, "E3/E3": 33, "E3/E2": 24,
    "E3/O": 34, "E2/O": 27, "O/O": 16,
}


def block(name: str) -> tuple[int, int, list[tuple[int, int, int]]]:
    """Return B dimension, C dimension, literal (A,B,C) nonzero entries."""
    if name in ("E2", "E3", "E4"):
        b = int(name[1:])
        return b, b + 4, [(i, j, i + j) for i in range(5) for j in range(b)]
    if name == "O":
        return 4, 2, [(j + k, j, k) for j in range(4) for k in range(2)]
    raise ValueError("unknown block")


def intrinsic_matrix(name: str) -> list[list[int]]:
    """C_i^* tensor B_i -> A tensor wedge^2 B_i."""
    b, c, entries = block(name)
    wedges = list(combinations(range(b), 2))
    row = {(i, j, k): r for r, (i, (j, k)) in
           enumerate((i, pair) for i in range(5) for pair in wedges)}
    matrix = [[0] * (c * b) for _ in range(5 * len(wedges))]
    for i, j, k in entries:
        for ell in range(b):
            if j < ell:
                matrix[row[i, j, ell]][k * b + ell] += 1
            elif j > ell:
                matrix[row[i, ell, j]][k * b + ell] -= 1
    return matrix


def cross_matrix(left: str, right: str) -> list[list[int]]:
    """(C_i^* tensor B_j)+(C_j^* tensor B_i) -> A tensor B_i tensor B_j."""
    b, c, entries = block(left)
    d, e, other = block(right)
    matrix = [[0] * (c * d + e * b) for _ in range(5 * b * d)]
    for i, j, k in entries:
        for ell in range(d):
            matrix[(i * b + j) * d + ell][k * d + ell] += 1
    for i, ell, k in other:
        for j in range(b):
            matrix[(i * b + j) * d + ell][c * d + k * b + j] -= 1
    return matrix


def full_matrix(names: list[str]) -> list[list[int]]:
    """Build the unsplit literal Koszul matrix for small decomposition controls."""
    blocks = [block(name) for name in names]
    btotal = sum(b for b, _, _ in blocks)
    ctotal = sum(c for _, c, _ in blocks)
    wedges = list(combinations(range(btotal), 2))
    row = {(i, j, k): r for r, (i, (j, k)) in
           enumerate((i, pair) for i in range(5) for pair in wedges)}
    matrix = [[0] * (ctotal * btotal) for _ in range(5 * len(wedges))]
    boff = coff = 0
    for b, c, entries in blocks:
        for i, j, k in entries:
            j += boff
            k += coff
            for ell in range(btotal):
                if j < ell:
                    matrix[row[i, j, ell]][k * btotal + ell] += 1
                elif j > ell:
                    matrix[row[i, ell, j]][k * btotal + ell] -= 1
        boff += b
        coff += c
    return matrix


def rref(matrix: list[list[int]]) -> tuple[list[list[Fraction]], list[int]]:
    """Certificate discovery only."""
    a = [[Fraction(value) for value in row] for row in matrix]
    pivots = []
    for col in range(len(a[0])):
        pivot = next((row for row in range(len(pivots), len(a)) if a[row][col]), None)
        if pivot is None:
            continue
        row = len(pivots)
        a[row], a[pivot] = a[pivot], a[row]
        scale = a[row][col]
        a[row] = [value / scale for value in a[row]]
        for other in range(len(a)):
            if other != row and a[other][col]:
                scale = a[other][col]
                a[other] = [x - scale * y for x, y in zip(a[other], a[row])]
        pivots.append(col)
        if len(pivots) == len(a):
            break
    return a, pivots


def bareiss_determinant(matrix: list[list[int]]) -> int:
    """Exact determinant; independent from discovery's rational RREF."""
    n = len(matrix)
    if n == 0:
        return 1
    if any(len(row) != n for row in matrix):
        raise ValueError("determinant requires a square matrix")
    a = [row[:] for row in matrix]
    sign = 1
    divisor = 1
    for k in range(n - 1):
        pivot = next((r for r in range(k, n) if a[r][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        value = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * value - a[i][k] * a[k][j]
                quotient, remainder = divmod(numerator, divisor)
                if remainder:
                    raise ValueError("nonexact Bareiss division")
                a[i][j] = quotient
            a[i][k] = 0
        divisor = value
    return sign * a[-1][-1]


def matrix_digest(matrix: list[list[int]]) -> str:
    return hashlib.sha256(json.dumps(matrix, separators=(",", ":")).encode()).hexdigest()


def make_rank_certificate(matrix: list[list[int]]) -> dict:
    reduced, columns = rref(matrix)
    _, rows = rref([list(row) for row in zip(*matrix)])
    free = [j for j in range(len(matrix[0])) if j not in columns]
    kernel = []
    for j in free:
        vector = {str(j): "1"}
        for i, col in enumerate(columns):
            if reduced[i][j]:
                vector[str(col)] = str(-reduced[i][j])
        kernel.append({"free_column": j, "entries": vector})
    minor = [[matrix[i][j] for j in columns] for i in rows]
    return {"rows": len(matrix), "columns": len(matrix[0]),
            "matrix_sha256": matrix_digest(matrix), "rank": len(columns),
            "minor_rows": rows, "minor_columns": columns,
            "minor_determinant": str(bareiss_determinant(minor)),
            "kernel_vectors": kernel}


def verify_rank_certificate(matrix: list[list[int]], certificate: dict) -> int:
    """Check both inequalities directly without rediscovering the matrix rank."""
    m, n = len(matrix), len(matrix[0])
    if (certificate["rows"], certificate["columns"]) != (m, n):
        raise ValueError("matrix format mismatch")
    if certificate["matrix_sha256"] != matrix_digest(matrix):
        raise ValueError("literal matrix digest mismatch")
    rank = certificate["rank"]
    rows = certificate["minor_rows"]
    cols = certificate["minor_columns"]
    if not isinstance(rank, int) or not 0 <= rank <= min(m, n):
        raise ValueError("invalid rank")
    if len(rows) != rank or len(cols) != rank:
        raise ValueError("minor dimensions mismatch")
    if len(set(rows)) != rank or len(set(cols)) != rank:
        raise ValueError("repeated minor index")
    if any(not isinstance(i, int) or not 0 <= i < m for i in rows):
        raise ValueError("invalid minor row")
    if any(not isinstance(j, int) or not 0 <= j < n for j in cols):
        raise ValueError("invalid minor column")
    determinant = bareiss_determinant([[matrix[i][j] for j in cols] for i in rows])
    if determinant == 0 or str(determinant) != certificate["minor_determinant"]:
        raise ValueError("nonzero minor certificate failed")
    free = sorted(set(range(n)) - set(cols))
    kernel = certificate["kernel_vectors"]
    if [item["free_column"] for item in kernel] != free:
        raise ValueError("missing kernel basis vector")
    for item in kernel:
        vector = {int(j): Fraction(value) for j, value in item["entries"].items()}
        if any(not 0 <= j < n for j in vector):
            raise ValueError("invalid kernel coordinate")
        if any(vector.get(j, 0) != int(j == item["free_column"]) for j in free):
            raise ValueError("kernel independence certificate failed")
        if any(sum(row[j] * value for j, value in vector.items()) for row in matrix):
            raise ValueError("kernel equation failed")
    return rank


def named_matrices() -> dict[str, list[list[int]]]:
    answer = {"intrinsic/" + name: intrinsic_matrix(name) for name in EXPECTED_INTRINSIC}
    answer.update({"cross/" + pair: cross_matrix(*pair.split("/")) for pair in EXPECTED_CROSS})
    return answer


def endpoint_report(names: list[str], intrinsic: dict, cross: dict) -> dict:
    counts = Counter(names)
    pair_counts = Counter("/".join(pair) for pair in combinations(names, 2))
    internal = sum(count * intrinsic[name] for name, count in counts.items())
    between = sum(count * cross[pair] for pair, count in pair_counts.items())
    return {"blocks": dict(counts), "dimensions": [5, sum(block(n)[0] for n in names),
             sum(block(n)[1] for n in names)],
            "intrinsic_rank": internal, "pair_counts": dict(pair_counts),
            "cross_rank": between, "koszul_rank": internal + between}


def score_comparison() -> dict:
    """Certify the candidate's strict score increase using rational cubing."""
    root_five_lower = Fraction(17, 10)
    deficit = 5 - root_five_lower ** 3
    target_lower = 240 + 29 * root_five_lower
    gap = target_lower ** 3 - 130 ** 3 * 11
    if deficit <= 0 or gap <= 0:
        raise ValueError("formal score comparison failed")
    return {"source": "65*cuberoot(11/2)",
            "target": "60*cuberoot(4)+(29/2)*cuberoot(5/2)",
            "common_positive_scale": "2^(4/3)",
            "scaled_source": "130*cuberoot(11)",
            "scaled_target": "240+29*cuberoot(5)",
            "cuberoot_five_lower_bound": str(root_five_lower),
            "lower_bound_cube_deficit": str(deficit),
            "scaled_target_lower_bound": str(target_lower),
            "cubed_strict_comparison_gap": str(gap),
            "score_increases": True, "degeneration_constructed": False}


def verify(certificate: dict) -> dict:
    matrices = named_matrices()
    if set(certificate) != set(matrices):
        raise ValueError("certificate matrix coverage mismatch")
    ranks = {name: verify_rank_certificate(matrix, certificate[name])
             for name, matrix in matrices.items()}
    intrinsic = {name: ranks["intrinsic/" + name] for name in EXPECTED_INTRINSIC}
    cross = {pair: ranks["cross/" + pair] for pair in EXPECTED_CROSS}
    if intrinsic != EXPECTED_INTRINSIC or cross != EXPECTED_CROSS:
        raise ValueError("recorded rank conclusion mismatch")
    source = endpoint_report(SOURCE, intrinsic, cross)
    target = endpoint_report(TARGET, intrinsic, cross)
    gap = target["koszul_rank"] - source["koszul_rank"]
    if source["dimensions"] != target["dimensions"] or gap != 21:
        raise ValueError("endpoint obstruction mismatch")
    return {"status": "exact rational certificates passed",
            "claim_status": "proof-written-unreviewed",
            "field": "complex numbers (ranks certified over rational numbers)",
            "scope": "canonical source and canonical target coefficient bases",
            "source": source, "target": target, "rank_gap": gap,
            "literal_matrix_count": len(matrices), "intrinsic_ranks": intrinsic,
            "cross_ranks": cross, "degeneration_excluded": True,
            "formal_score_comparison": score_comparison(),
            "independent_target_first_identifications_excluded": False,
            "new_exponent_established": False}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-certificate", action="store_true")
    parser.add_argument("--certificate", type=Path, default=RESULTS / "certificate.json")
    parser.add_argument("--output", type=Path, default=RESULTS / "verification.json")
    args = parser.parse_args()
    if args.write_certificate:
        certificate = {name: make_rank_certificate(matrix)
                       for name, matrix in named_matrices().items()}
        args.certificate.parent.mkdir(parents=True, exist_ok=True)
        args.certificate.write_text(json.dumps(certificate, indent=2) + "\n")
    else:
        certificate = json.loads(args.certificate.read_text())
    report = verify(certificate)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
