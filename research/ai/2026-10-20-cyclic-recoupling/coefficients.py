"""Exact cyclic-product recoupling, reusing the maintained rational CG basis."""
from collections import defaultdict
from fractions import Fraction
import gzip
from itertools import product
import json
from math import comb, lcm
from pathlib import Path
import sys

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "2026-10-20-clebsch-gordan"))
from cg_blocks import equivariant_basis, convolution_isomorphism, dot_slice_bound
from cg_search import profile


def triple_basis(degree):
    first = {(i, e): p for i, e, p in equivariant_basis(degree, degree)}
    result = []
    for i in range(degree+1):
        for j, e, p in equivariant_basis(2*degree-2*i, 2*degree):
            poly = defaultdict(Fraction)
            for (f, k), coefficient in p.items():
                for (u, v), other in first[i, f].items():
                    poly[u, v, k] += coefficient*other
            result.append((i, j, e, 4*degree-2*i-2*j, dict(poly)))
    return result


def inverse_basis(a):
    degree = a-1
    original = list(product(range(a), range(a), range(2*a-1)))
    basis = triple_basis(degree)
    dimension = len(original)
    assert len(basis) == dimension
    inverse = [[0]*dimension for _ in range(dimension)]
    denominators = [1]*dimension
    for weight in range(4*degree+1):
        columns = [i for i, b in enumerate(basis) if sum(b[:3]) == weight]
        rows = [i for i, v in enumerate(original) if sum(v) == weight]
        matrix = sp.Matrix([[basis[col][4].get(original[row], 0)
                             for col in columns] for row in rows])
        block_inverse = matrix.inv()
        assert block_inverse*matrix == sp.eye(len(columns))
        for i, col in enumerate(columns):
            denominators[col] = lcm(*(int(block_inverse[i, j].q) for j in range(len(rows))))
            for j, row in enumerate(rows):
                inverse[col][row] = int(block_inverse[i, j]*denominators[col])
    return original, basis, inverse, denominators


def recouple(a):
    degree = a-1
    original, basis, inverse, denominators = inverse_basis(a)
    index = {v: i for i, v in enumerate(original)}
    tensor = {}
    for i, j, p, q, r, s in product(range(a), repeat=6):
        coefficient = (-1)**(i+j+p+q+r+s)
        for v in (i, j, p, q, r, s):
            coefficient *= comb(degree, v)
        point = (index[i, s, 2*degree-p-q], index[j, p, 2*degree-r-s],
                 index[q, r, 2*degree-i-j])
        tensor[point] = coefficient
    by_column = [[(i, row[j]) for i, row in enumerate(inverse) if row[j]]
                 for j in range(len(original))]
    for axis in range(3):
        transformed = defaultdict(int)
        for point, coefficient in tensor.items():
            for new, factor in by_column[point[axis]]:
                target = point[:axis]+(new,)+point[axis+1:]
                transformed[target] += factor*coefficient
        tensor = {p: c for p, c in transformed.items() if c}
    labels = sorted({b[:2] for b in basis})
    label_index = {v: i for i, v in enumerate(labels)}
    blocks = defaultdict(list)
    for point, value in sorted(tensor.items()):
        b = [basis[i] for i in point]
        assert 2*sum(v[2] for v in b) == sum(v[3] for v in b)
        coefficient = Fraction(value, denominators[point[0]]*denominators[point[1]]*denominators[point[2]])
        blocks[tuple(label_index[v[:2]] for v in b)].append([*[v[2] for v in b], str(coefficient)])
    return {"a": a, "source_leg_dimension": len(original),
            "labels": [{"label": list(v), "degree": 4*degree-2*sum(v),
                        "dimension": 4*degree-2*sum(v)+1} for v in labels],
            "blocks": [{"labels": list(k), "terms": v} for k, v in sorted(blocks.items())]}


def uniform_certificate(dims, terms):
    masses = [value*value/Fraction(comb(dims[0]-1, i)*comb(dims[1]-1, j)*comb(dims[2]-1, k))
              for i, j, k, value in terms]
    total = sum(masses)
    assert total > 0
    for axis, dimension in enumerate(dims):
        margin = [Fraction()]*dimension
        for term, mass in zip(terms, masses):
            margin[term[axis]] += mass
        assert margin == [total/dimension]*dimension
    assert len({i+j+k for i, j, k, _ in terms}) == 1
    return min(dims)


def group_multiplicities(data):
    labels = data["labels"]
    degrees = sorted({b["degree"] for b in labels})
    by_degree = {d: [i for i, b in enumerate(labels) if b["degree"] == d] for d in degrees}
    groups = defaultdict(list)
    coefficient_count = 0
    for block in data["blocks"]:
        dims = tuple(labels[i]["dimension"] for i in block["labels"])
        terms = [(i, j, k, Fraction(v)) for i, j, k, v in block["terms"]]
        uniform_certificate(dims, terms)
        coefficient_count += len(terms)
        groups[tuple(d-1 for d in dims)].append(block)
    result = []
    for deg, group in sorted(groups.items()):
        first = group[0]["terms"]
        scale = Fraction(first[0][3])
        cg = {(i, j, k): Fraction(v)/scale for i, j, k, v in first}
        multiplicity = []
        for block in group:
            scalar = Fraction(block["terms"][0][3])
            actual = {(i, j, k): Fraction(v)/scalar for i, j, k, v in block["terms"]}
            assert actual == cg
            multiplicity.append((*[by_degree[d].index(i) for d, i in zip(deg, block["labels"])], scalar))
        dims = tuple(len(by_degree[d]) for d in deg)
        tensor = {"dims": dims, "terms": multiplicity}
        rank = dot_slice_bound(tensor)
        iso = convolution_isomorphism(tensor)
        bound = max(Fraction(rank), profile(*iso["convolution_lengths"]) if iso else Fraction(1))
        cg_tensor = {"dims": tuple(d+1 for d in deg), "terms": [(*k, v) for k, v in cg.items()]}
        result.append({"labels": [degrees.index(d) for d in deg], "degrees": list(deg),
            "multiplicity_dimensions": list(dims),
            "multiplicity_terms": [[i, j, k, str(v)] for i, j, k, v in multiplicity],
            "multiplicity_dot_rank": rank, "multiplicity_convolution_isomorphism": iso,
            "multiplicity_matching_profile_lower": str(bound),
            "cg_terms": [[*k, str(v)] for k, v in cg.items()],
            "cg_convolution_isomorphism": convolution_isomorphism(cg_tensor)})
    return {"a": data["a"], "degrees": degrees,
        "multiplicities": {str(d): len(by_degree[d]) for d in degrees}, "blocks": result,
        "factorization_verified_for_all_original_blocks": True,
        "uniform_scalar_blocks_checked": len(data["blocks"]),
        "exact_nonzero_coefficients_checked": coefficient_count}


def read_json(path):
    opener = gzip.open if str(path).endswith(".gz") else open
    with opener(path, "rt") as stream:
        return json.load(stream)


def write_json(path, value):
    payload = (json.dumps(value, separators=(",", ":"))+"\n").encode()
    Path(path).write_bytes(gzip.compress(payload, mtime=0) if str(path).endswith(".gz") else payload)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--a", type=int, required=True)
    parser.add_argument("--output-directory", type=Path, required=True)
    args = parser.parse_args()
    args.output_directory.mkdir(parents=True, exist_ok=True)
    data = recouple(args.a)
    grouped = group_multiplicities(data)
    write_json(args.output_directory/f"coefficients-a{args.a}.json.gz", data)
    write_json(args.output_directory/f"grouped-a{args.a}.json.gz", grouped)
    print({k: v for k, v in grouped.items() if k not in ("blocks", "degrees", "multiplicities")})
