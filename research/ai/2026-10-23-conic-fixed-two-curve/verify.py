"""Exact full-source acceptance of the prescribed two-jet polynomial curve.

No constructor, gauge formula or prior contraction implementation is imported.
An arithmetic-only Laurent parser clears the permitted d poles. Sparse exact
polynomials then check every coefficient of the complete literal K contraction.
"""
import argparse
import ast
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
import hashlib
from itertools import product
import json
from pathlib import Path

import sympy as s
from sympy.polys.rings import ring


ROOT = Path(__file__).resolve().parents[3]
PRIOR = ROOT / 'results/conic-third-jets-2026-10-23/mixed-family.json'
PRIOR_SHA256 = '0571cd47916d19c60a0f9493a6ddccaecb8053aea8a139137c05b3def9df1d5e'
R, A, B, D = ring('a,b,d', s.QQ)
MONOMIALS = {'a': (1, 0, 0), 'b': (0, 1, 0), 'd': (0, 0, 1)}
ORIGIN = (0, 0, 0)
FIRST = [28*i+7*j+z for i, j, z in product((1, 2), (1, 2), (0, 3, 6))]
OUTSIDE = set(range(112))-set(FIRST)
PIVOTS = [0, 1, 2, 3, 14, 15, 16, 17, 30, 31, 44, 45]


def polynomial_add(left, right, sign=1):
    result = dict(left)
    for monomial, value in right.items():
        result[monomial] = result.get(monomial, Fraction(0))+sign*value
    return {monomial: value for monomial, value in result.items() if value}


def polynomial_multiply(left, right):
    result = {}
    for alpha, u in left.items():
        for beta, v in right.items():
            monomial = tuple(x+y for x, y in zip(alpha, beta))
            result[monomial] = result.get(monomial, Fraction(0))+u*v
    if len(result) > 50000:
        raise ValueError('coefficient expansion limit exceeded')
    return {monomial: value for monomial, value in result.items() if value}


@lru_cache(maxsize=4096)
def expression(text, pole):
    """Return d**pole times a permitted Laurent expression, as an exact polynomial."""
    def read(node):
        if isinstance(node, ast.Constant) and type(node.value) is int:
            return {ORIGIN: Fraction(node.value)} if node.value else {}
        if isinstance(node, ast.Name) and node.id in MONOMIALS:
            return {MONOMIALS[node.id]: Fraction(1)}
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            value = read(node.operand)
            return {m: -q for m, q in value.items()} if isinstance(node.op, ast.USub) else value
        if isinstance(node, ast.BinOp):
            left, right = read(node.left), read(node.right)
            if isinstance(node.op, ast.Add):
                return polynomial_add(left, right)
            if isinstance(node.op, ast.Sub):
                return polynomial_add(left, right, -1)
            if isinstance(node.op, ast.Mult):
                return polynomial_multiply(left, right)
            if isinstance(node.op, ast.Div) and len(right) == 1:
                (power, coefficient), = right.items()
                if power[:2] == (0, 0):
                    return {tuple(x-y for x, y in zip(m, power)): q/coefficient
                            for m, q in left.items()}
            if isinstance(node.op, ast.Pow) and set(right) <= {ORIGIN}:
                exponent = right.get(ORIGIN, Fraction(0))
                if exponent.denominator == 1 and abs(exponent) <= 128:
                    exponent = int(exponent)
                    if exponent < 0:
                        if len(left) != 1:
                            raise ValueError('unpermitted parameter denominator')
                        (power, coefficient), = left.items()
                        if power[:2] != (0, 0):
                            raise ValueError('unpermitted parameter denominator')
                        return {tuple(exponent*x for x in power): coefficient**exponent}
                    result = {ORIGIN: Fraction(1)}
                    while exponent:
                        if exponent & 1:
                            result = polynomial_multiply(result, left)
                        exponent //= 2
                        if exponent:
                            left = polynomial_multiply(left, left)
                    return result
        raise ValueError('coefficient is not permitted rational Laurent arithmetic')
    if not isinstance(text, str) or len(text) > 200000:
        raise ValueError('invalid coefficient text')
    try:
        tree = ast.parse(text, mode='eval')
        if sum(1 for _ in ast.walk(tree)) > 30000:
            raise ValueError('coefficient expression limit exceeded')
        values = read(tree.body)
    except (SyntaxError, ZeroDivisionError) as error:
        raise ValueError('invalid Laurent coefficient') from error
    if any(m[0] < 0 or m[1] < 0 or m[2] < -pole for m in values):
        raise ValueError('coefficient exceeds its permitted d pole')
    return R.from_dict({(i, j, k+pole): s.QQ.convert(q)
                        for (i, j, k), q in values.items()})


def decode(record, pole):
    if record['shape'] != [14, 112]:
        raise ValueError('wrong map shape')
    matrix = {}
    for i, j, text in record['entries']:
        if (type(i) is not int or type(j) is not int or (i, j) in matrix
                or not 0 <= i < 14 or not 0 <= j < 112):
            raise ValueError('wrong map coordinate')
        value = expression(text, pole)
        if not value:
            raise ValueError('stored zero map coefficient')
        matrix[i, j] = value
    return matrix


def source_terms():
    return [(28*i+7*r+6-p-q, 28*p+7*j+6-s-r, 28*s+7*q+6-i-j)
            for i, j, p, q, s, r in product(range(4), repeat=6)]


def contract(left, right, terms):
    by_left, by_right = defaultdict(list), defaultdict(list)
    for (row, column), value in left.items():
        by_left[column].append((row, value))
    for (row, column), value in right.items():
        by_right[column].append((row, value))
    output, products = {}, {}
    for first, second, third in terms:
        for i, x in by_left[second]:
            for j, y in by_right[third]:
                # The parser caches equal coefficient strings, so parity
                # repetitions use the same immutable input objects. Reusing
                # only these exact products changes no source contributions.
                key = id(x), id(y)
                if key not in products:
                    products[key] = x*y
                index = first, 14*i+j
                output[index] = output.get(index, R.zero)+products[key]
    return {index: value for index, value in output.items() if value}


def coefficient(bs, cs, order, terms):
    output = {}
    for i in range(len(bs)):
        if 0 <= order-i < len(cs):
            for index, value in contract(bs[i], cs[order-i], terms).items():
                output[index] = output.get(index, R.zero)+value
    return {index: value for index, value in output.items() if value}


def determinant(matrix, rows, columns):
    return s.factor(s.Matrix(len(rows), len(columns),
        lambda i, j: matrix.get((rows[i], columns[j]), R.zero).as_expr()).det())


def prepare(record):
    """Validate the complete maps and the prescribed maps/kernel data through two."""
    if (record.get('schema') != 'conic-fixed-two-curve-v1'
            or record.get('base') != 'c=-d^3' or record.get('chart') != 'd != 0'):
        raise ValueError('wrong curve schema or d chart')
    if len(record['B']) != 9 or len(record['C']) != 10:
        raise ValueError('wrong complete polynomial degrees')
    bs, cs = [[decode(matrix, pole) for matrix in record[key]]
              for key, pole in (('B', 5), ('C', 6))]
    if not bs[-1] or not cs[-1]:
        raise ValueError('missing highest polynomial coefficient')
    prior_bytes = PRIOR.read_bytes()
    if hashlib.sha256(prior_bytes).hexdigest() != PRIOR_SHA256:
        raise ValueError('credited predecessor bytes changed')
    prior = json.loads(prior_bytes)
    for side, maps, pole in (('B', bs, 5), ('C', cs, 6)):
        for order in range(3):
            if maps[order] != decode(prior[side][order], pole):
                raise ValueError(f'changed prescribed full coefficient {side}{order}')
    zero_corrections = [{'shape': [100, 12], 'entries': []} for _ in range(2)]
    if (prior['source_row_corrections'][:2] != zero_corrections
            or record.get('source_row_corrections_through_two') != zero_corrections):
        raise ValueError('changed prescribed kernel parametrization through two')
    return bs, cs


def verify(record):
    bs, cs = prepare(record)
    terms = source_terms()
    kernel_terms = [term for term in terms if term[0] in OUTSIDE]
    # This retains EVERY original contribution to every K entry. Other first
    # rows are unrestricted at positive order; no equation is dropped.
    for order in range(18):
        if coefficient(bs, cs, order, kernel_terms):
            raise ValueError(f'nonzero full-source kernel coefficient at order {order}')
    unscaled_b0, unscaled_c0 = [decode(record[key][0], 0) for key in ('B', 'C')]
    f0 = contract(unscaled_b0, unscaled_c0, terms)
    boundary_b = [28*p+7*j+z for p, j, z in product((0, 3), (0, 3), (1, 2, 4, 5))]
    boundary_c = [28*j+7*p+z for p, j, z in product((0, 3), (0, 3), (1, 2, 4, 5))]
    determinants = [determinant(unscaled_b0, list(range(14)), boundary_b[2:]),
                    determinant(unscaled_c0, list(range(14)), boundary_c[2:]),
                    determinant(f0, FIRST, PIVOTS)]
    if determinants != [1, 1, -1]:
        raise ValueError('wrong constant leading minors')
    pole_orders = [max(pole-min(power[2] for matrix in maps for value in matrix.values()
                                for power in value), 0)
                   for maps, pole in ((bs, 5), (cs, 6))]
    return {
        'claim_id': 'AI-CONIC-FIXED-TWO-CURVE-001',
        'coefficient_ring': 'Q[a,b,d,d^-1]',
        'scope': 'Every complex a,b,d with d nonzero, c=-d^3',
        'source_terms': len(terms),
        'map_degrees_in_t': [8, 9],
        'map_parameter_pole_orders': pole_orders,
        'complete_product_orders_checked': list(range(18)),
        'source_kernel_coordinates_per_order': 100*196,
        'source_kernel_coordinates_total': 18*100*196,
        'leading_minor_determinants': list(map(str, determinants)),
        'leading_map_ranks': [14, 14],
        'formal_first_source_rank': 12,
        'coefficient_entry_counts': {'B': list(map(len, bs)), 'C': list(map(len, cs))},
        'prescribed_map_orders_preserved': [0, 1, 2],
        'prescribed_kernel_corrections_preserved': ['Y1=0', 'Y2=0'],
        'fixed_source_kernel_at_all_orders': True,
        'normal_class': '[1:d]',
        'all_order_lift_established': True,
        'matrix_target_constructed': False,
        'exponent_improvement': False,
        'independent_mathematical_review': False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('witness', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = verify(json.loads(args.witness.read_text()))
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report))
