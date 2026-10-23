"""Exact witnesses for the standard-flip component of the external seed.

Only the Python standard library is needed.  The finite certificate supports
the written proof in component_proof.md; it is not a proof assistant output.
"""
import argparse
from collections import Counter, defaultdict
import hashlib
import itertools
import json
from pathlib import Path


PACKAGE = Path(__file__).resolve().parent
SEED = PACKAGE.parent / "2026-10-21-external-grid-seed/factors.json"
SEED_SHA256 = "bc4bc0eb93b6074ec57aa420322b506a39f7958bd88f2b9897995006c4bc00c3"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load_seed(path=SEED):
    data = Path(path).read_bytes()
    require(hashlib.sha256(data).hexdigest() == SEED_SHA256,
            "External seed byte pin does not match")
    factors = json.loads(data)
    require(factors["n"] == [4, 5, 5] and factors["m"] == 76,
            "Unexpected external seed dimensions")
    for leg, width in (("u", 20), ("v", 25), ("w", 20)):
        rows = factors[leg]
        require(len(rows) == 76 and all(len(row) == width for row in rows),
                "Incorrect factor array shape")
        require(all(type(value) is int and value in (-1, 0, 1)
                    for row in rows for value in row),
                "Expected the pinned integer coefficient alphabet")
        require(all(any(row) for row in rows), "A factor is zero")
    return factors


def unit_minor(rows):
    """Find columns of a full-row minor using only integer unit pivots."""
    work = [list(row) for row in rows]
    available = list(range(len(work[0])))
    columns = []
    for pivot in range(len(work)):
        entry = next(((i, j) for i in range(pivot, len(work))
                      for j in available if abs(work[i][j]) == 1), None)
        require(entry is not None, "No unit pivot found for a required minor")
        i, j = entry
        work[pivot], work[i] = work[i], work[pivot]
        sign = work[pivot][j]
        work[pivot] = [sign * value for value in work[pivot]]
        for i in range(pivot + 1, len(work)):
            multiple = work[i][j]
            work[i] = [value - multiple * anchor
                       for value, anchor in zip(work[i], work[pivot])]
        available.remove(j)
        columns.append(j)
    return columns


def determinant(matrix):
    """Leibniz formula, independent of the unit-pivot witness generator."""
    size = len(matrix)
    total = 0
    for permutation in itertools.permutations(range(size)):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(size) for j in range(i + 1, size))
        value = -1 if inversions % 2 else 1
        for i, j in enumerate(permutation):
            value *= matrix[i][j]
        total += value
    return total


def trace_product(u, v, w):
    return sum(u[5 * i + j] * v[5 * j + k] * w[4 * k + i]
               for i in range(4) for j in range(5) for k in range(5))


def normalized_classes(factors):
    """Normalize W; move its sign into U so each tensor term is unchanged."""
    groups = defaultdict(list)
    for index, row in enumerate(factors["w"]):
        sign = next(value for value in row if value)
        require(sign in (-1, 1), "W normalization requires a unit entry")
        groups[tuple(sign * value for value in row)].append([index, sign])
    classes = list(groups.values())
    require(sorted(map(len, classes)) == [1] * 40 + [2] * 18,
            "Unexpected W proportionality classes")
    return classes


def pairing_matrix(factors, group):
    first, sign = group[0]
    w = [sign * value for value in factors["w"][first]]
    return [[trace_product([s * x for x in factors["u"][i]],
                           factors["v"][j], w)
             for j, _ in group] for i, s in group]


def build_certificate(factors):
    classes = normalized_classes(factors)
    minors = []
    for leg in ("u", "v"):
        for left, right in itertools.combinations(range(len(classes)), 2):
            indices = [i for i, _ in classes[left] + classes[right]]
            rows = [factors[leg][i] for i in indices]
            columns = unit_minor(rows)
            value = determinant([[row[j] for j in columns] for row in rows])
            require(abs(value) == 1, "Generated minor is not a unit")
            minors.append([leg, left, right, columns, value])
    return {"seed_sha256": SEED_SHA256, "groups": classes,
            "unit_minors": minors}


def verify_certificate(factors, certificate):
    """Check all supplied minors, their coverage, and every trace pairing."""
    require(certificate["seed_sha256"] == SEED_SHA256,
            "Certificate has the wrong seed pin")
    classes = normalized_classes(factors)
    require(certificate["groups"] == classes, "Certificate groups differ")
    expected = {(leg, left, right) for leg in ("u", "v")
                for left, right in itertools.combinations(range(58), 2)}
    seen = set()
    for leg, left, right, columns, value in certificate["unit_minors"]:
        key = (leg, left, right)
        require(key in expected and key not in seen,
                "Unknown or duplicate class-pair witness")
        seen.add(key)
        rows = [factors[leg][i] for i, _ in classes[left] + classes[right]]
        require(len(columns) == len(rows) and len(set(columns)) == len(rows),
                "Minor has incorrect or repeated columns")
        require(all(type(j) is int and 0 <= j < len(rows[0]) for j in columns),
                "Minor column is out of range")
        actual = determinant([[row[j] for j in columns] for row in rows])
        require(abs(value) == 1 and actual == value,
                "Recorded unit minor fails direct determinant replay")
    require(seen == expected, "Missing class-pair unit minors")
    traces = []
    pairings = []
    for group in classes:
        pairing = pairing_matrix(factors, group)
        c = pairing[0][0]
        require(c in (1, 2), "Trace scalar is not a positive integer")
        require(pairing == [[c if i == j else 0 for j in range(len(group))]
                            for i in range(len(group))],
                "Trace pairing is not a scalar identity")
        traces.extend([c] * len(group))
        pairings.append(c)
    require(Counter(traces) == {1: 52, 2: 24}, "Unexpected trace counts")
    return {
        "seed_sha256": SEED_SHA256,
        "class_sizes": {"1": 40, "2": 18},
        "cross_class_unit_minors": len(seen),
        "class_pairing_scalars": pairings,
        "individual_trace_values": {"1": 52, "2": 24},
        "sum_trace": sum(traces),
        "field_for_flip_and_deletion_theorem": "C (also characteristic zero)",
        "scope": "Finite standard shared-factor flips and term gauges of the pinned seed; no rank-increasing moves.",
        "proof_status": "written-unreviewed",
        "improves_omega": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-certificate", type=Path)
    args = parser.parse_args()
    factors = load_seed()
    if args.write_certificate:
        certificate = build_certificate(factors)
        summary = verify_certificate(factors, certificate)
        args.write_certificate.write_text(json.dumps(certificate, indent=2) + "\n")
    else:
        certificate = json.loads((PACKAGE / "component_certificate.json").read_text())
        summary = verify_certificate(factors, certificate)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
