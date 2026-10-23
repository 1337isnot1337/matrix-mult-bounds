"""Exact finite-field controls for simultaneous tensor-power contractions.

This finite control program records passed rank tests, not a construction.
The coefficient convention is the one supplied by research_frontier:
Full(a,b): x_i y_j z_(i+j); Mid(a,b): x_i y_(i+k) z_k;
SharedOutput(d,e): x_(j+k) y_j z_k.
"""

from functools import lru_cache
from itertools import combinations_with_replacement, product
from math import factorial, gcd
from pathlib import Path
import argparse
import json


ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "results/mixed-longlegs-candidate-2026-10-23"


TYPES = (
    ("Full", 5, 2, 7),
    ("Full", 5, 3, 10),
    ("SharedOutput", 3, 3, 4),
    ("SharedOutput", 4, 2, 2),
    ("Mid", 5, 2, 6),
)


def block(kind, first, second):
    if kind == "Full":
        a, b, c = first, second, first + second - 1
        terms = [(i, j, i + j) for i in range(a) for j in range(b)]
    elif kind == "Mid":
        a, b, c = first, first + second - 1, second
        terms = [(i, i + k, k) for i in range(a) for k in range(c)]
    elif kind == "SharedOutput":
        a, b, c = first + second - 1, first, second
        terms = [(j + k, j, k) for j in range(b) for k in range(c)]
    else:
        raise ValueError(kind)
    lookup = {(i, j): k for i, j, k in terms}
    assert len(lookup) == len(terms)
    return a, b, c, lookup


def rank_mod2(columns):
    pivots = {}
    for column in columns:
        while column:
            pivot = column.bit_length() - 1
            old = pivots.get(pivot)
            if old is None:
                pivots[pivot] = column
                break
            column ^= old
    return len(pivots)


def rank_rational(columns, nrows):
    """Primitive-integer elimination; no modular inference supplies this rank."""
    rows = [{} for _ in range(nrows)]
    for column_index, column in enumerate(columns):
        while column:
            bit = column & -column
            rows[bit.bit_length() - 1][column_index] = 1
            column ^= bit
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
                row = {j: sign * value // content for j, value in row.items()}
                pivots[pivot] = row
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
    return len(pivots)


def _encode(index, dimensions):
    out = 0
    for i, n in zip(index, dimensions):
        out = out * n + i
    return out


def tuple_control(kinds, rational=False):
    """Compute a single ordered block tuple; symmetry permits sorted inputs."""
    data = [block(*kind) for kind in kinds]
    assert len({value[0] for value in data}) == 1
    a = data[0][0]
    b_dims = [value[1] for value in data]
    c_dims = [value[2] for value in data]
    q = len(data)
    total_b = 1
    for b in b_dims:
        total_b *= b
    starts = []
    row_dims = []
    nrows = 0
    for k in range(q):
        starts.append(nrows)
        dims = [c_dims[k]] + b_dims[:k] + b_dims[k + 1:]
        row_dims.append(dims)
        nrows += c_dims[k] * (total_b // b_dims[k])

    def columns():
        for i in range(a):
            for indices in product(*(range(b) for b in b_dims)):
                column = 0
                for k in range(q):
                    z = data[k][3].get((i, indices[k]))
                    if z is None:
                        continue
                    output = (z,) + indices[:k] + indices[k + 1:]
                    row = starts[k] + _encode(output, row_dims[k])
                    column ^= 1 << row
                yield column

    rank = rank_mod2(columns())
    domain = a * total_b
    result = {
        "blocks": [list(kind) for kind in kinds],
        "domain": domain,
        "codomain": nrows,
        "rank_mod2": rank,
        "nullity_mod2": domain - rank,
    }
    if rational:
        rational_rank = rank_rational(columns(), nrows)
        result.update(rank_rational=rational_rank, nullity_rational=domain-rational_rank)
        if rational_rank != rank:
            raise AssertionError(("modular rank drop", result))
    return result


def target_control(q, rational=False):
    tuples = []
    rank = nullity = domain = 0
    for selection in combinations_with_replacement(range(len(TYPES)), q):
        control = tuple_control([TYPES[i][:3] for i in selection], rational=rational)
        weight = factorial(q)
        for i in range(len(TYPES)):
            multiplicity = selection.count(i)
            weight //= factorial(multiplicity)
        for i in selection:
            weight *= TYPES[i][3]
        control["ordered_tuple_weight"] = weight
        tuples.append(control)
        rank += weight * control["rank_mod2"]
        nullity += weight * control["nullity_mod2"]
        domain += weight * control["domain"]
    assert domain == 5 * 100**q
    source_rank = 5 * 100**q - max(5 - q, 0) * 90**q
    result = {
        "degree": q,
        "domain": domain,
        "target_rank_mod2": rank,
        "target_nullity_mod2": nullity,
        "source_rank_formula": source_rank,
        "target_minus_source": rank - source_rank,
        "exclusion_from_this_modular_lower_bound": rank > source_rank,
        "block_tuples": tuples,
    }
    if rational:
        result.update(target_rank_rational=rank, target_nullity_rational=nullity,
                      exclusion_over_complex_numbers=rank > source_rank)
    return result


def main():
    RESULTS.mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-degree", type=int, default=4)
    parser.add_argument("--rational", action="store_true")
    args = parser.parse_args()
    controls = []
    for q in range(1, args.max_degree + 1):
        item = target_control(q, rational=args.rational)
        controls.append(item)
        print(json.dumps({k: v for k, v in item.items() if k != "block_tuples"}), flush=True)
    source_controls = []
    for a, widths in [(2, [2, 3]), (3, [1, 2, 3]), (5, [2, 3, 1])]:
        q = len(widths)
        item = tuple_control([("Full", a, b) for b in widths])
        expected = max(a - q, 0)
        for b in widths:
            expected *= b - 1
        item["nullity_formula"] = expected
        assert item["nullity_mod2"] == expected
        source_controls.append(item)
    result = {
        "status": "exact rational and F2 ranks" if args.rational else "exact finite F2 controls, with characteristic-zero upper formula separately proved",
        "source_controls": source_controls,
        "target_controls": controls,
        "improves_omega": False,
    }
    (RESULTS / "shared_output_prolongation_controls.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )


if __name__ == "__main__":
    main()
