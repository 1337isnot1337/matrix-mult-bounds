"""Exact acceptance of a complete polynomial curve on the cubic conic.

This verifier reconstructs the 4096 source terms directly. It imports no
discovery script, tangent operator, gauge formula or predecessor verifier.
All acceptance arithmetic is in QQ[a,b,d], with no parameter denominators.
"""
import argparse
import ast
from collections import defaultdict
import hashlib
from itertools import product
import json
from pathlib import Path

import sympy as s


ROOT = Path(__file__).resolve().parents[3]
PRIOR = ROOT / 'results/conic-third-jets-2026-10-23/mixed-family.json'
PRIOR_SHA256 = '0571cd47916d19c60a0f9493a6ddccaecb8053aea8a139137c05b3def9df1d5e'
A, B, D = s.symbols('a b d')
VARIABLES = (A, B, D)
ZERO = s.Poly(0, *VARIABLES, domain=s.QQ)
SYMBOLS = {str(z): s.Poly(z, *VARIABLES, domain=s.QQ) for z in VARIABLES}
FIRST = [28*i + 7*j + z for i, j, z in product((1, 2), (1, 2), (0, 3, 6))]
OUTSIDE = set(range(112)) - set(FIRST)
PIVOTS = [0, 1, 2, 3, 14, 15, 16, 17, 30, 31, 44, 45]


def expression(text):
    """Parse integer/rational polynomial arithmetic without executing input."""
    def read(node):
        if isinstance(node, ast.Constant) and type(node.value) is int:
            return s.Poly(node.value, *VARIABLES, domain=s.QQ)
        if isinstance(node, ast.Name) and node.id in SYMBOLS:
            return SYMBOLS[node.id]
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            value = read(node.operand)
            return -value if isinstance(node.op, ast.USub) else value
        if isinstance(node, ast.BinOp):
            left, right = read(node.left), read(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            if isinstance(node.op, ast.Mult):
                return left * right
            if isinstance(node.op, ast.Div) and right.total_degree() == 0 and right:
                return left.mul_ground(1 / right.as_expr())
            if isinstance(node.op, ast.Pow) and right.total_degree() == 0:
                exponent = right.as_expr()
                if exponent.is_Integer and exponent >= 0:
                    return left ** int(exponent)
        raise ValueError('coefficient is not polynomial arithmetic over Q[a,b,d]')
    try:
        if not isinstance(text, str):
            raise ValueError('coefficient must be a string')
        return read(ast.parse(text, mode='eval').body)
    except (SyntaxError, TypeError, ZeroDivisionError) as error:
        raise ValueError('invalid polynomial coefficient') from error


def decode(record):
    if record['shape'] != [14, 112]:
        raise ValueError('wrong map shape')
    matrix = {}
    for i, j, text in record['entries']:
        if (type(i) is not int or type(j) is not int or (i, j) in matrix
                or not 0 <= i < 14 or not 0 <= j < 112):
            raise ValueError('wrong map coordinate')
        value = expression(text)
        if not value:
            raise ValueError('stored zero map coefficient')
        matrix[i, j] = value
    return matrix


def add(*matrices):
    result = {}
    for matrix in matrices:
        for index, value in matrix.items():
            result[index] = result.get(index, ZERO) + value
    return {index: value for index, value in result.items() if value}


def source_terms():
    """Integer cyclic source, with index(u,v,z) = 28u + 7v + z."""
    return [(28*i + 7*r + 6-p-q,
             28*p + 7*j + 6-s-r,
             28*s + 7*q + 6-i-j)
            for i, j, p, q, s, r in product(range(4), repeat=6)]


def contract(left, right, terms):
    by_left, by_right = defaultdict(list), defaultdict(list)
    for (row, col), value in left.items():
        by_left[col].append((row, value))
    for (row, col), value in right.items():
        by_right[col].append((row, value))
    output = {}
    for first, second, third in terms:
        for i, x in by_left[second]:
            for j, y in by_right[third]:
                index = first, 14*i+j
                output[index] = output.get(index, ZERO) + x*y
    return {index: value for index, value in output.items() if value}


def determinant(matrix, rows, columns):
    return s.factor(s.Matrix(len(rows), len(columns),
        lambda i, j: matrix.get((rows[i], columns[j]), ZERO).as_expr()).det())


def nonboundary(matrix, side):
    def middle(column):
        return column // 28 if side == 'B' else column // 7 % 4
    return {index: value for index, value in matrix.items() if middle(index[1]) in (1, 2)}


def verify(record):
    if record.get('schema') != 'conic-polynomial-curve-v1' or record.get('base') != 'c=-d^3':
        raise ValueError('wrong curve schema or conic base')
    if len(record['B']) != 2 or len(record['C']) != 4:
        raise ValueError('wrong complete polynomial degrees')
    bs, cs = [[decode(matrix) for matrix in record[key]] for key in ('B', 'C')]
    if not bs[-1] or not cs[-1]:
        raise ValueError('missing highest polynomial coefficient')
    prior_bytes = PRIOR.read_bytes()
    if hashlib.sha256(prior_bytes).hexdigest() != PRIOR_SHA256:
        raise ValueError('credited predecessor bytes changed')
    prior = json.loads(prior_bytes)
    normal_counts = []
    boundary_difference_counts = []
    for key, maps in (('B', bs), ('C', cs)):
        if maps[0] != decode(prior[key][0]):
            raise ValueError('changed credited constant coefficient')
        previous_first = decode(prior[key][1])
        if nonboundary(maps[1], key) != nonboundary(previous_first, key):
            raise ValueError('changed credited first normal coefficient')
        normal_counts.append(len(nonboundary(maps[1], key)))
        difference = add(maps[1], {index: -value for index, value in previous_first.items()})
        boundary_difference_counts.append(len(difference))
    # This universal coefficient is one, so the first normal never vanishes,
    # including after d=0 or any other complex parameter specialization.
    if cs[1].get((0, 95), ZERO) != -SYMBOLS['d']:
        raise ValueError('missing middle-one normal anchor')
    if cs[1].get((0, 102), ZERO) != expression('-1'):
        raise ValueError('missing middle-two normal anchor')
    terms = source_terms()
    # Degrees 1 and 3 make these five coefficients the COMPLETE product.
    fs = [add(*(contract(bs[i], cs[k-i], terms)
                for i in range(2) if 0 <= k-i < 4)) for k in range(5)]
    for order, matrix in enumerate(fs):
        if any(row in OUTSIDE for row, col in matrix):
            raise ValueError(f'nonzero full-source kernel coefficient at order {order}')
    boundary_b = [28*p + 7*j + z for p, j, z in product((0, 3), (0, 3), (1, 2, 4, 5))]
    boundary_c = [28*j + 7*p + z for p, j, z in product((0, 3), (0, 3), (1, 2, 4, 5))]
    determinants = [determinant(bs[0], list(range(14)), boundary_b[2:]),
                    determinant(cs[0], list(range(14)), boundary_c[2:]),
                    determinant(fs[0], FIRST, PIVOTS)]
    if determinants != [1, 1, -1]:
        raise ValueError('wrong constant leading minors')
    return {
        'claim_id': 'AI-CONIC-POLYNOMIAL-CURVE-001',
        'coefficient_ring': 'Q[a,b,d]',
        'scope': 'Every complex a,b,d, with c=-d^3',
        'source_terms': len(terms),
        'map_degrees_in_t': [1, 3],
        'complete_product_orders_checked': list(range(5)),
        'source_kernel_coordinates_per_order': 100*196,
        'fixed_source_kernel_dimension': 100,
        'leading_minor_determinants': list(map(str, determinants)),
        'leading_map_ranks': [14, 14],
        'formal_first_source_rank': 12,
        'first_nonboundary_entry_counts': normal_counts,
        'first_boundary_difference_counts_from_pr107': boundary_difference_counts,
        'normal_class': '[1:d]',
        'first_normal_coefficients_equal_pr107': True,
        'full_first_jet_preserved': False,
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
        args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report))
