"""Exact, dependency-free C(4,5) -> M2 Laurent coefficient certificate."""
from itertools import product
from pathlib import Path
import json
import argparse

U = [[1, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 0, 1]]
V = [[2, -1, 0, 0, 0, 0, 0, 0],
     [-8, 1, 0, 1, 1, -1, 0, 0],
     [-2, 0, -1, 1, 0, 0, 0, 0],
     [-1, 0, 0, 1, -1, 0, 0, 1]]
W = [[2, 1, 0, 4, 1], [1, 1, 1, 2, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 1]]
WEIGHTS = [[0, 4, 1, 5], [0, 2, -1, 1], [0, -4, -2, -6]]


def replay():
    constant, remainder = [], []
    checked = 0
    for x, y, z in product(range(4), repeat=3):
        coefficient = sum(U[x][a] * V[y][a + b] * W[z][b]
                          for a in range(4) for b in range(5))
        # Separate polynomial-convolution replay, followed by output projection.
        polynomial = [0] * 8
        for a, u in enumerate(U[x]):
            for b, w in enumerate(W[z]):
                polynomial[a + b] += u * w
        assert coefficient == sum(value * v for value, v in zip(polynomial, V[y]))
        degree = WEIGHTS[0][x] + WEIGHTS[1][y] + WEIGHTS[2][z]
        i, s = divmod(x, 2)
        ii, j = divmod(y, 2)
        jj, t = divmod(z, 2)
        target = int(i == ii and j == jj and s == t)
        assert degree == i - ii + 2 * (j - jj) + 4 * (s - t)
        if degree <= 0:
            assert coefficient == target
        if coefficient:
            assert degree >= 0
            (constant if degree == 0 else remainder).append([degree, x, y, z, coefficient])
        checked += 1
    assert len(constant) == 8 and len(remainder) == 22
    assert min(term[0] for term in remainder) == 1
    assert max(term[0] for term in remainder) == 7
    return {'source': 'C(4,5)', 'target': 'M2',
            'coefficient_field': 'integers; hence every field',
            'maps': {'U': U, 'V': V, 'W': W},
            'row_weights': dict(zip(('U', 'V', 'W'), WEIGHTS)),
            'all64_coefficients_checked': checked == 64,
            'constant_terms': constant, 'positive_remainder': remainder,
            'negative_coefficients_all_zero': True,
            'exact_Laurent_witness': True, 'improves_omega': False}


if __name__ == '__main__':
    report = replay()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.output:
        args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'all64_coefficients_checked': True,
                      'constant_term_count': len(report['constant_terms']),
                      'positive_remainder_count': len(report['positive_remainder']),
                      'maximum_remainder_degree': 7, 'improves_omega': False}))
