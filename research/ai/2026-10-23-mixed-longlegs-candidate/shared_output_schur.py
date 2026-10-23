"""Exact S_q-isotypic kernel ranks for q<=4 in the canonical candidate.

Companion to shared_output_prolongation.py. Kernel characters use
primitive-integer elimination followed by rational row reduction.
"""

from fractions import Fraction
from itertools import product
from math import gcd, factorial
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "results/mixed-longlegs-candidate-2026-10-23"

from shared_output_prolongation import TYPES, block, _encode


CLASSES = {
    2: [("11", 1, (0, 1)), ("2", 1, (1, 0))],
    3: [("111", 1, (0, 1, 2)), ("21", 3, (1, 0, 2)), ("3", 2, (1, 2, 0))],
    4: [("1111", 1, (0, 1, 2, 3)), ("211", 6, (1, 0, 2, 3)),
        ("22", 3, (1, 0, 3, 2)), ("31", 8, (1, 2, 0, 3)), ("4", 6, (1, 2, 3, 0))],
}
CHARACTERS = {
    2: {(2,): [1, 1], (1, 1): [1, -1]},
    3: {(3,): [1, 1, 1], (2, 1): [2, 0, -1], (1, 1, 1): [1, -1, 1]},
    4: {(4,): [1, 1, 1, 1, 1], (3, 1): [3, 1, -1, 0, -1],
        (2, 2): [2, 0, 2, -1, 0], (2, 1, 1): [3, -1, -1, 0, 1],
        (1, 1, 1, 1): [1, -1, 1, 1, -1]},
}


def cycles(permutation):
    remaining = set(range(len(permutation)))
    result = []
    while remaining:
        point = min(remaining)
        cycle = []
        while point not in cycle:
            cycle.append(point)
            remaining.remove(point)
            point = permutation[point]
        result.append(cycle)
    return result


def schur_dimension(partition, n):
    answer = Fraction(1)
    for i, width in enumerate(partition):
        for j in range(width):
            below = sum(other > j for other in partition[i + 1:])
            hook = width - j + below
            answer *= Fraction(n + j - i, hook)
    assert answer.denominator == 1
    return answer.numerator


def echelon(rows):
    rows.sort(key=len)
    pivots = {}
    for row in rows:
        while row:
            pivot = min(row)
            old = pivots.get(pivot)
            if old is None:
                content = 0
                for value in row.values():
                    content = gcd(content, value)
                sign = 1 if row[pivot] > 0 else -1
                pivots[pivot] = {j: sign * value // content for j, value in row.items()}
                break
            a, b = row[pivot], old[pivot]
            divisor = gcd(a, b)
            row = {j: value * (b // divisor) for j, value in row.items()}
            for j, value in old.items():
                new = row.get(j, 0) - (a // divisor) * value
                if new:
                    row[j] = new
                else:
                    row.pop(j, None)
            if row:
                content = 0
                for value in row.values():
                    content = gcd(content, value)
                if content > 1:
                    row = {j: value // content for j, value in row.items()}
    return pivots


def reduced(pivots):
    result = {}
    for pivot in sorted(pivots, reverse=True):
        old = pivots[pivot]
        row = {j: Fraction(value, old[pivot]) for j, value in old.items()}
        for j in sorted(tuple(row)):
            if j == pivot or j not in result:
                continue
            coefficient = row.get(j, 0)
            if not coefficient:
                continue
            for k, value in result[j].items():
                new = row.get(k, 0) - coefficient * value
                if new:
                    row[k] = new
                else:
                    row.pop(k, None)
        result[pivot] = row
    return result


def tuple_kernel_trace(kinds, permutation):
    data = [block(*kind) for kind in kinds]
    a = data[0][0]
    b_dims = [value[1] for value in data]
    c_dims = [value[2] for value in data]
    assert all(kinds[k] == kinds[permutation[k]] for k in range(len(kinds)))
    q = len(data)
    total_b = 1
    for b in b_dims:
        total_b *= b
    starts, output_dims = [], []
    nrows = 0
    for k in range(q):
        starts.append(nrows)
        output_dims.append([c_dims[k]] + b_dims[:k] + b_dims[k + 1:])
        nrows += c_dims[k] * (total_b // b_dims[k])
    rows = [{} for _ in range(nrows)]
    permuted = []
    for i in range(a):
        for indices in product(*(range(b) for b in b_dims)):
            col = i * total_b + _encode(indices, b_dims)
            moved = tuple(indices[permutation[k]] for k in range(q))
            permuted.append(i * total_b + _encode(moved, b_dims))
            for k in range(q):
                z = data[k][3].get((i, indices[k]))
                if z is not None:
                    output = (z,) + indices[:k] + indices[k + 1:]
                    row = starts[k] + _encode(output, output_dims[k])
                    rows[row][col] = 1
    pivots = reduced(echelon(rows))
    trace = Fraction(0)
    for free in range(a * total_b):
        if free in pivots:
            continue
        moved = permuted[free]
        if moved == free:
            trace += 1
        elif moved in pivots:
            trace -= pivots[moved].get(free, 0)
    assert trace.denominator == 1
    return {"kernel_dimension": a * total_b - len(pivots), "trace": trace.numerator}


def class_trace(permutation):
    cycle_list = cycles(permutation)
    total = 0
    records = []
    for labels in product(range(len(TYPES)), repeat=len(cycle_list)):
        kinds = [None] * len(permutation)
        weight = 1
        for cycle, label in zip(cycle_list, labels):
            weight *= TYPES[label][3]
            for position in cycle:
                kinds[position] = TYPES[label][:3]
        result = tuple_kernel_trace(kinds, permutation)
        total += weight * result["trace"]
        records.append({"cycle_types": list(labels), "weight": weight, **result})
    return total, records


def verify_character_table(q):
    data = list(CHARACTERS[q].values())
    sizes = [item[1] for item in CLASSES[q]]
    for i, chi in enumerate(data):
        for j, psi in enumerate(data):
            assert sum(s * c * p for s, c, p in zip(sizes, chi, psi)) == factorial(q) * (i == j)
    assert sum(chi[0]**2 for chi in data) == factorial(q)


def main():
    RESULTS.mkdir(parents=True, exist_ok=True)
    source_controls = []
    for q in (2, 3, 4):
        for _, _, permutation in CLASSES[q]:
            for width in (2, 3, 4):
                actual = tuple_kernel_trace([("Full", 5, width)] * q, permutation)
                expected = (5-q) * (width-1)**len(cycles(permutation))
                assert actual["trace"] == expected
                source_controls.append({"degree": q, "width": width,
                    "permutation": list(permutation), "trace": actual["trace"],
                    "formula": expected})
    original = json.loads((RESULTS / "shared_output_prolongation_controls.json").read_text())
    total_nullities = {item["degree"]: item["target_nullity_rational"] for item in original["target_controls"]}
    output = []
    for q in (2, 3, 4):
        verify_character_table(q)
        characters = [total_nullities[q]]
        class_records = []
        for name, size, permutation in CLASSES[q][1:]:
            value, records = class_trace(permutation)
            characters.append(value)
            class_records.append({"class": name, "character": value, "controls": records})
        pieces = []
        total_dimension = 0
        for partition, irreducible in CHARACTERS[q].items():
            numerator = sum(item[1] * chi * value for item, chi, value in zip(CLASSES[q], irreducible, characters))
            assert numerator % factorial(q) == 0
            kernel = numerator // factorial(q)
            assert kernel >= 0
            source_kernel = max(5-q, 0) * schur_dimension(partition, 90)
            domain = 5 * schur_dimension(partition, 100)
            source_rank, target_rank = domain-source_kernel, domain-kernel
            pieces.append({"partition": list(partition), "symmetric_group_dimension": irreducible[0],
                           "source_kernel": source_kernel, "target_kernel": kernel,
                           "source_rank": source_rank, "target_rank": target_rank,
                           "target_minus_source": target_rank-source_rank})
            total_dimension += irreducible[0] * kernel
        assert total_dimension == total_nullities[q]
        record = {"degree": q, "kernel_characters": characters, "pieces": pieces,
                  "class_records": class_records}
        output.append(record)
        print(json.dumps({k: v for k, v in record.items() if k != "class_records"}), flush=True)
    result = {"status": "scratch exact rational Schur-component screen; not a construction",
              "source_trace_controls": source_controls,
              "degrees": output, "improves_omega": False}
    (RESULTS / "shared_output_schur_controls.json").write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
