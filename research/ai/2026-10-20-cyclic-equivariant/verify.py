"""Exact coefficient controls and representation screens for a specified SL2 ansatz."""
from collections import Counter
from fractions import Fraction
import gzip
from itertools import product
import json
from math import comb
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "results/cyclic-equivariant-2026-10-20"


def singlet_sum(a):
    d = a-1
    total = Fraction()
    for i, j, p, s in product(range(a), repeat=4):
        q, r = i+s-p, j+p-s
        if not (0 <= q < a and 0 <= r < a):
            continue
        numerator = 1
        for v in (i, j, p, q, r, s):
            numerator *= comb(d, v)
        total += Fraction(numerator, comb(2*d, i+s)*comb(2*d, j+p)*comb(2*d, q+r))
    return total


def coefficients(a):
    d, n = a-1, 2*a-1
    b = comb(2*d, d)
    total = singlet_sum(a)
    source = [total/n**3, Fraction(1, n*b), Fraction(1, n*b),
              Fraction(1, n*b), Fraction((-1)**d)]
    target = [Fraction(1, n*n), Fraction(1, n), Fraction(1, n),
              Fraction(1, n), Fraction(1)]
    ratios = [t/s for t, s in zip(target, source)]
    defect = ratios[1]*ratios[2]*ratios[3]-ratios[0]*ratios[4]**2
    assert total >= 1 and b >= 2*d and b**3 > n and defect > 0
    return {"a": a, "source_coefficients": list(map(str, source)),
            "target_coefficients": list(map(str, target)),
            "normalized_target_coefficients": list(map(str, ratios)),
            "polynomial_defect": str(defect)}


def independent_coefficient_control(a):
    """Compare with retained full recoupling and a separate exact target basis inverse."""
    import sympy as sp
    sys.path.insert(0, str(ROOT / "research/ai/2026-10-20-clebsch-gordan"))
    from cg_blocks import equivariant_basis
    d, n, h = a-1, 2*a-1, 4*a-4
    degree_triples = ((0, 0, 0), (0, h, h), (h, 0, h), (h, h, 0), (h, h, h))
    indices = ((0, 0, 0), (0, 0, h), (0, 0, h), (0, h, 0), (0, 2*d, h))
    path = ROOT / f"results/cyclic-recoupling-2026-10-20/coefficients-a{a}.json.gz"
    with gzip.open(path, "rt") as stream:
        source = json.load(stream)
    actual_source = []
    for degrees, point in zip(degree_triples, indices):
        blocks = [b for b in source["blocks"]
                  if tuple(source["labels"][k]["degree"] for k in b["labels"]) == degrees]
        assert len(blocks) == 1
        actual_source.append(next(Fraction(c) for i, j, k, c in blocks[0]["terms"]
                                  if (i, j, k) == point))
    basis = list(equivariant_basis(2*d, 2*d))
    original = list(product(range(n), repeat=2))
    position = {v: i for i, v in enumerate(original)}
    inverse = sp.zeros(n*n)
    for weight in range(h+1):
        rows = [i for i, v in enumerate(original) if sum(v) == weight]
        cols = [i for i, b in enumerate(basis) if sum(b[:2]) == weight]
        matrix = sp.Matrix([[basis[col][2].get(original[row], 0) for col in cols] for row in rows])
        block = matrix.inv()
        assert block*matrix == sp.eye(len(rows))
        for i, col in enumerate(cols):
            for j, row in enumerate(rows):
                inverse[col, row] = block[i, j]
    actual_target = []
    for degrees, point in zip(degree_triples, indices):
        selected = [next(i for i, b in enumerate(basis) if h-2*b[0] == degree and b[1] == e)
                    for degree, e in zip(degrees, point)]
        value = 0
        for i, j, k in product(range(n), repeat=3):
            factor = (-1)**(i+j+k)*comb(2*d, i)*comb(2*d, j)*comb(2*d, k)
            old = (position[i, 2*d-j], position[j, 2*d-k], position[k, 2*d-i])
            value += factor*inverse[selected[0], old[0]]*inverse[selected[1], old[1]]*inverse[selected[2], old[2]]
        actual_target.append(Fraction(value))
    expected = coefficients(a)
    assert list(map(str, actual_source)) == expected["source_coefficients"]
    assert list(map(str, actual_target)) == expected["target_coefficients"]
    return {"a": a, "source_coefficients_checked": 5, "target_coefficients_checked": 5,
            "target_basis_dimension": n*n}


def partitions(n, parity, minimum=None):
    """Unordered irreducible dimensions, all odd (parity=1) or all even (0)."""
    minimum = (1 if parity else 2) if minimum is None else minimum
    if n == 0:
        yield ()
    for k in range(minimum, n+1, 2):
        for rest in partitions(n-k, parity, k):
            yield (k,)+rest


def tensor_character(left, right):
    result = Counter()
    for i, j in product(left, right):
        for dimension in range(abs(i-j)+1, i+j, 2):
            result[dimension] += 1
    return result


def source_character(a):
    return tensor_character(tuple(range(1, 2*a, 2)), (2*a-1,))


def representation_screen(a, shape):
    capacity = source_character(a)
    checked, survivors, violations = 0, [], Counter()
    for parity in (1, 0):
        choices = [list(partitions(n, parity)) for n in shape]
        for vertices in product(*choices):
            checked += 1
            obstruction = None
            for left, right in ((0, 1), (1, 2), (2, 0)):
                character = tensor_character(vertices[left], vertices[right])
                for dimension, multiplicity in sorted(character.items()):
                    if multiplicity > capacity.get(dimension, 0):
                        obstruction = (left, right, dimension, multiplicity, capacity.get(dimension, 0))
                        break
                if obstruction:
                    break
            if obstruction:
                violations[str(obstruction)] += 1
            else:
                survivors.append([list(v) for v in vertices])
    assert sum(violations.values())+len(survivors) == checked
    return {"a": a, "target": list(shape), "source_multiplicities_by_irrep_dimension": dict(sorted(capacity.items())),
            "vertex_representation_triples_checked": checked, "survivors": survivors,
            "first_violations_and_counts": dict(sorted(violations.items()))}


def report():
    screens = [representation_screen(a, shape) for a, shape in
               ((2, (3, 3, 3)), (4, (10, 10, 11)), (5, (13, 13, 17)))]
    assert screens[0]["survivors"] == [[[3], [3], [3]]]
    assert not screens[1]["survivors"] and not screens[2]["survivors"]
    for a in range(2, 9):
        natural = [[a], [a], [a]]
        assert natural in representation_screen(a, (a, a, a))["survivors"]
    return {"coefficient_formula_controls": [coefficients(a) for a in range(2, 13)],
            "independent_coefficient_controls": [independent_coefficient_control(a) for a in (2, 3, 4)],
            "representation_screens": screens, "natural_Ma_positive_controls": 7,
            "general_degeneration_excluded": False, "new_exponent_established": False}


if __name__ == "__main__":
    print(json.dumps(report(), indent=2))
