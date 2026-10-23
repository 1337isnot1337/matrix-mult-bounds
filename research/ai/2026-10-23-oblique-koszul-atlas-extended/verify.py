"""Exact, characteristic-independent Koszul ranks of fixed oblique residuals.

Acceptance uses integer row operations with unit pivots, not numerical ranks.
The native n=6 maps are copied sparsely from the immutable credited source.
"""

import argparse
from hashlib import sha256
from itertools import combinations, product
import json
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent


def residual(r):
    """K plus the two outer arms, in the preceding proof's adapted bases."""
    if type(r) is not int or r < 3:
        raise ValueError("r must be an integer at least three")
    terms = [(0, 0, 0), (0, 1, 1), (1, 2, 2), (1, 3, 3),
             (2, 0, 1), (2, 1, 4), (2, 3, 2), (2, 4, 3), (2, 0, 2)]
    for j in range(r - 2):
        terms.extend([(3 + j, 0, 5 + 2*j), (3 + j, 1, 6 + 2*j),
                      (r + 1 + j, 5 + 2*j, 2),
                      (r + 1 + j, 6 + 2*j, 3)])
    return {term: 1 for term in terms}, (2*r - 1, 2*r + 1, 2*r + 1)


def koszul_rows(tensor, dimensions, leg, degree):
    """Rows of Lambda^p V tensor W* -> Lambda^(p+1) V tensor U."""
    if leg not in range(3) or not 0 <= degree < dimensions[leg]:
        raise ValueError("invalid leg or exterior degree")
    order = [leg] + [i for i in range(3) if i != leg]
    a, b, c = [dimensions[i] for i in order]
    output_wedges = list(combinations(range(a), degree + 1))
    row_index = {wedge: i for i, wedge in enumerate(output_wedges)}
    rows = [{} for _ in range(len(output_wedges)*c)]
    for column, wedge in enumerate(combinations(range(a), degree)):
        for indices, coefficient in tensor.items():
            i, j, k = [indices[z] for z in order]
            if i in wedge:
                continue
            target = tuple(sorted((*wedge, i)))
            sign = -1 if sum(z < i for z in wedge) % 2 else 1
            row, index = rows[row_index[target]*c + k], column*b + j
            row[index] = row.get(index, 0) + sign*coefficient
    return [{k: v for k, v in row.items() if v} for row in rows], comb(a, degree)*b


def unit_rank(rows):
    """Reduce over Z; a nonunit pivot is rejected, never divided away."""
    basis, pivots = {}, []
    for row_number, original in enumerate(rows):
        row = dict(original)
        while row:
            column = max(row)
            if column not in basis:
                if row[column] not in (-1, 1):
                    raise ArithmeticError("nonunit pivot: no all-field certificate")
                basis[column] = row
                pivots.append((row_number, column, row[column]))
                break
            previous = basis[column]
            scale = row[column]*previous[column]
            for index, value in previous.items():
                row[index] = row.get(index, 0) - scale*value
                if not row[index]:
                    del row[index]
    payload = json.dumps(pivots, separators=(",", ":")).encode()
    return len(basis), sha256(payload).hexdigest()


def rank_record(r, leg, degree):
    tensor, dimensions = residual(r)
    rows, columns = koszul_rows(tensor, dimensions, leg, degree)
    rank, pivot_hash = unit_rank(rows)
    cost = comb(dimensions[leg] - 1, degree)
    return {"r": r, "leg": leg, "degree": degree,
            "shape": [len(rows), columns], "rank_over_every_field": rank,
            "rank_one_cost": cost, "border_lower_bound": (rank + cost - 1)//cost,
            "unit_pivot_sha256": pivot_hash}


def native_residual(witness):
    """Contract every native Q(6,4) term and subtract it from M(5,4,5)."""
    n, b, r = 6, 4, 5
    if witness["source"] != [n, b] or witness["target"] != [r, 4, r]:
        raise ValueError("unexpected source or target")
    if len(witness["maps"]) != 3:
        raise ValueError("exactly three source maps are required")
    maps = []
    for entries, output_size in zip(witness["maps"], (25, 20, 20)):
        by_source = [[] for _ in range(36)]
        seen = set()
        for output, source, coefficient in entries:
            if (type(coefficient) is not int or not coefficient or
                    not 0 <= output < output_size or not 0 <= source < 36 or
                    (output, source) in seen):
                raise ValueError("invalid sparse source map")
            seen.add((output, source))
            by_source[source].append((output, coefficient))
        maps.append(by_source)
    result = {(r*i+j, 4*i+h, r*h+j): 1
              for i, h, j in product(range(r), range(4), range(r))}
    for p, q, y, v in product(range(n), range(n), range(b), range(b)):
        for (i, x), (j, z), (k, w) in product(
                maps[0][n*p+q], maps[1][9*y+q+v], maps[2][4*(p+y)+v]):
            key = (i, j, k)
            result[key] = result.get(key, 0) - x*z*w
    return {key: value for key, value in result.items() if value}


def embedded_residual(r):
    """The same tensor in native target coordinates; no decoder is imported."""
    s = r - 2
    outer = [i for i in range(r) if i not in (0, s)]
    first = [{r*s: 1}, {s: 1}, {r*s+s: 1}]
    first += [{r*s+j: 1} for j in outer] + [{r*i+s: 1} for i in outer]
    second = [{4*s: 1, 1: -1}, {4*s+2: 1, 3: -1},
              {0: 1}, {1: 1}, {4*s+1: 1}]
    third = [{0: 1}, {2*r: 1}, {s: 1, 2*r: -1},
             {r+s: 1, 3*r: -1}, {2*r+s: 1}]
    for i in outer:
        second += [{4*i: 1}, {4*i+1: 1}]
        third += [{i: 1}, {2*r+i: 1}]
    tensor, _ = residual(r)
    result = {}
    for (i, j, k), value in tensor.items():
        for (a, x), (b, y), (c, z) in product(
                first[i].items(), second[j].items(), third[k].items()):
            key = (a, b, c)
            result[key] = result.get(key, 0) + value*x*y*z
    return {key: value for key, value in result.items() if value}


def certificate():
    witness = json.loads((HERE / "native-witness.json").read_text())
    if native_residual(witness) != embedded_residual(5):
        raise ArithmeticError("adapted tensor does not match the actual native residual")
    records = [rank_record(r, leg, p) for r in range(3, 7) for leg in range(3)
               for p in range((2*r - 1, 2*r + 1, 2*r + 1)[leg])]
    return {"schema": 1, "scope": "full-space Koszul maps, r=3,4,5,6",
            "native_witness_sha256": sha256((HERE / "native-witness.json").read_bytes()).hexdigest(),
            "native_source_terms": 576, "native_target_coordinates": 10000,
            "native_residual_nonzero_coefficients": len(embedded_residual(5)),
            "matrices": records,
            "best_bounds": {str(r): max(row["border_lower_bound"] for row in records
                                        if row["r"] == r) for r in range(3, 7)},
            "independent_mathematical_review": False, "improves_omega": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", type=Path, help="write a regenerated certificate")
    args = parser.parse_args()
    result = certificate()
    if args.write:
        args.write.write_text(json.dumps(result, indent=2) + "\n")
    elif result != json.loads((HERE / "certificate.json").read_text()):
        raise ArithmeticError("saved certificate does not match the complete exact replay")
    print(json.dumps({"matrices": len(result["matrices"]),
                      "best_bounds": result["best_bounds"], "native_identity": True}))


if __name__ == "__main__":
    main()
