"""Independent F4 coefficient, degeneration, tightness and entropy replay."""
import argparse
from collections import Counter
from itertools import permutations, product
import json
from math import prod
from pathlib import Path

N = 60


def scalar_product(a, b):
    polynomial = 0
    for i in range(2):
        for j in range(2):
            if (a >> i) & (b >> j) & 1:
                polynomial ^= 1 << (i+j)
    return polynomial ^ 7 if polynomial & 4 else polynomial


TABLE = [[scalar_product(a, b) for b in range(4)] for a in range(4)]
INVERSE = {1: 1, 2: 3, 3: 2}


def alternating_group():
    points = [p for p in permutations(range(5))
              if sum(p[i] > p[j] for i in range(5) for j in range(i+1, 5)) % 2 == 0]
    lookup = {p: i for i, p in enumerate(points)}
    multiplication = [[lookup[tuple(p[q[k]] for k in range(5))] for q in points] for p in points]
    return points, multiplication, [row.index(0) for row in multiplication]


def decode(text):
    value = int(text, 16)
    if value < 0 or value >> (2*N):
        raise ValueError('F4 vector is outside the stated group algebra')
    return [((value >> i) & 1) | (((value >> (N+i)) & 1) << 1) for i in range(N)]


def rank(vectors):
    basis = {}
    for vector in vectors:
        row = list(vector)
        while any(row):
            pivot = max(i for i, a in enumerate(row) if a)
            coefficient = row[pivot]
            if pivot not in basis:
                basis[pivot] = [TABLE[INVERSE[coefficient]][a] for a in row]
                break
            row = [a ^ TABLE[coefficient][b] for a, b in zip(row, basis[pivot])]
    return len(basis)


def convolution(left, right, multiplication):
    result = [0]*N
    for g, a in enumerate(left):
        if a:
            for h, b in enumerate(right):
                if b:
                    result[multiplication[g][h]] ^= TABLE[a][b]
    return result


def verify_cover(records, multiplication):
    matrices = [p for p in product(range(5), repeat=4) if (p[0]*p[3]-p[1]*p[2]) % 5 == 1]
    projection = {tuple(row['matrix']): row['image'] for row in records}
    if (len(records) != 120 or set(projection) != set(matrices)
            or any(type(v) is not int or not 0 <= v < N for v in projection.values())
            or Counter(projection.values()) != Counter({i: 2 for i in range(N)})):
        raise ValueError('wrong central-cover projection')

    def multiply(A, B):
        a, b, c, d = A
        e, f, g, h = B
        return ((a*e+b*g) % 5, (a*f+b*h) % 5, (c*e+d*g) % 5, (c*f+d*h) % 5)

    identity = (1, 0, 0, 1)
    kernel = [A for A in matrices if projection[A] == 0]
    if identity not in kernel:
        raise ValueError('cover map does not preserve identity')
    central = next(A for A in kernel if A != identity)
    if (multiply(central, central) != identity
            or any(multiply(central, A) != multiply(A, central) for A in matrices)):
        raise ValueError('kernel is not a central involution')
    for A in matrices:
        for B in matrices:
            if projection[multiply(A, B)] != multiplication[projection[A]][projection[B]]:
                raise ValueError('cover projection is not a homomorphism')
    return {'group': 'SL(2,5)', 'homomorphism_products_checked': 14400,
            'kernel': [list(A) for A in kernel]}


def verify(certificate):
    if certificate['coefficient_field'] != 'F2[w]/(w^2+w+1)':
        raise ValueError('wrong coefficient field')
    points, multiplication, inverse = alternating_group()
    if certificate['group_elements'] != [list(p) for p in points]:
        raise ValueError('wrong source group indexing')
    basis = [decode(v) for v in certificate['basis']]
    if len(basis) != N or rank(basis) != N:
        raise ValueError('proposed algebra basis is singular')
    weights = certificate['degeneration_weights']
    tight = certificate['tight_weights']
    for arrays in (weights, tight):
        if len(arrays) != 3 or any(len(row) != N or any(type(v) is not int for v in row)
                                   for row in arrays):
            raise ValueError('wrong integer weight format')
    if any(len(set(row)) != N for row in tight):
        raise ValueError('tightness weights are not injective')
    claimed = {tuple(row[:3]): row[3] for row in certificate['leading_tensor']}
    if len(claimed) != len(certificate['leading_tensor']):
        raise ValueError('duplicate leading tensor entry')
    inverted = [[v[inverse[g]] for g in range(N)] for v in basis]
    actual, nonzero = {}, 0
    for a in range(N):
        for b in range(N):
            value = convolution(basis[a], basis[b], multiplication)
            active = [(g, v) for g, v in enumerate(value) if v]
            if not active:
                continue
            for c in range(N):
                coefficient = 0
                for g, v in active:
                    coefficient ^= TABLE[v][inverted[c][g]]
                if coefficient:
                    nonzero += 1
                    exponent = weights[0][a]+weights[1][b]+weights[2][c]
                    if exponent < 0:
                        raise ValueError('the proposed source limit has a pole')
                    if exponent == 0:
                        actual[a, b, c] = coefficient
    if actual != claimed:
        raise ValueError('leading tensor does not match all source coefficients')
    for a, b, c in actual:
        if tight[0][a]+tight[1][b]+tight[2][c] != 0:
            raise ValueError('tightness identity failed')
    principal = [abc for abc in actual if all(i < 44 for i in abc)]
    matrix = [abc for abc in actual if all(i >= 44 for i in abc)]
    if len(principal) != 213 or len(matrix) != 64 or len(principal)+len(matrix) != len(actual):
        raise ValueError('wrong leading component support')
    expected_matrix = {(44+4*i+j, 44+4*j+k, 44+4*k+i)
                       for i, j, k in product(range(4), repeat=3)}
    if set(matrix) != expected_matrix or any(actual[abc] != 1 for abc in matrix):
        raise ValueError('the second component is not the stated M4 tensor')
    W = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    W_tight = ((0, 1), (0, 1), (-1, 0))
    combined = [[2*row[a]+W_tight[leg][d] for a in range(N) for d in range(2)]
                for leg, row in enumerate(tight)]
    if any(len(set(row)) != 120 for row in combined):
        raise ValueError('tensor-product tight weights are not injective')
    margins, denominator = [[0]*120 for _ in range(3)], 0
    for abc in actual:
        atom_weight = 128 if abc in principal else 213
        for digits in W:
            labels = [2*a+d for a, d in zip(abc, digits)]
            if sum(combined[leg][label] for leg, label in enumerate(labels)) != 0:
                raise ValueError('product tightness identity failed')
            denominator += atom_weight
            for leg, label in enumerate(labels):
                margins[leg][label] += atom_weight
    if (denominator != 122688 or denominator != certificate['probability_denominator']
            or any(row != margins[0] for row in margins)):
        raise ValueError('wrong rational distribution or unequal marginals')
    if margins != certificate['marginal_counts']:
        raise ValueError('saved entropy marginals are incorrect')
    # exp(H) > 517/5; no logarithm, root rounding or floating acceptance.
    lhs = pow(5*denominator, denominator)
    rhs = pow(517, denominator)*prod(pow(m, m) for m in margins[0] if m)
    if lhs <= rhs:
        raise ValueError('entropy lower bound is not above 517/5')
    if not (4*1889**3 < 27*1000**3 and 517*1889 > 195*5000
            and 2535**2 < 195**3):
        raise ValueError('additional central-factor comparison failed')
    cover = verify_cover(certificate['cover_projection'], multiplication)
    if certificate['exponent_improvement'] is not False:
        raise ValueError('the certificate cannot establish an exponent improvement')
    return {'source': 'F4[A5]', 'basis_rank': N, 'source_coefficients_checked': N**3,
            'source_nonzero_coefficients': nonzero, 'leading_terms': len(actual),
            'principal_terms': len(principal), 'matrix_terms': len(matrix),
            'tight_product_terms': len(actual)*3, 'probability_denominator': denominator,
            'entropy_lower_bound': '517/5', 'entropy_inequality_verified': True,
            'comparison_integer_bit_lengths': [lhs.bit_length(), rhs.bit_length()],
            'extra_C2_lower_bound': '976613/5000', 'central_cover': cover,
            'scope': 'Lower barrier for eventual global characteristic-two '
                     'source-power slice-rank costs. Finite-power or structured '
                     'restrictions and target constructions are not decided.',
            'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = verify(json.loads(args.certificate.read_text()))
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))
