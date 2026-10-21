"""Construct the retained mixed two-jet family by rational linear solves."""
import argparse
import importlib.util
from itertools import combinations_with_replacement
import json
from pathlib import Path

import sympy as sp

PACKAGE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('mixed_extension_source', PACKAGE.parent / '2026-10-21-quantum-extension-spaces/extensions.py')
extension = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(extension)


def decode(encoded):
    return [{j: sp.Rational(numerator, denominator) for j, numerator, denominator in row}
            for row in encoded]


def encode(covectors):
    return [[[j, int(sp.Rational(value).p), int(sp.Rational(value).q)]
             for j, value in sorted(row.items())] for row in covectors]


def encode_correction(matrix):
    return [[extension.OUTSIDE[i], extension.A0[j], int(value.p), int(value.q)]
            for (i, j), value in sorted(matrix.todok().items())]


def solver(matrix):
    _, columns = matrix.to_DM().rref()
    _, rows = matrix[:, list(columns)].T.to_DM().rref()
    inverse = matrix[list(rows), list(columns)].inv(method='DM')

    def solve(rhs):
        answer = sp.zeros(matrix.cols, rhs.cols)
        coefficients = inverse*rhs[list(rows), :]
        for i, column in enumerate(columns):
            answer[column, :] = coefficients[i, :]
        if matrix*answer != rhs:
            raise ArithmeticError('Second coefficient equations are inconsistent')
        return answer
    return solve


def construct(seed):
    g = decode(seed['leading_rows'])
    if g != extension.G:
        raise ArithmeticError('Unexpected leading flag')
    new_b, new_c = decode(seed['first_constant_B_new']), decode(seed['first_constant_C_new'])
    directions = [decode(rows) for rows in seed['first_top_directions']]
    first, cb, cc, _, _, annihilator = extension.matrices()
    core = first[extension.A0, :]
    _, columns = core.to_DM().rref()
    inverse = core[:, list(columns)].inv()
    ys, cores, ps, qs = [], [], [], []
    for rows in directions:
        p, q = rows[:4], rows[4:]
        ps.append(p)
        qs.append(q)
        derivative = (extension.contract(p, g, extension.OUTSIDE)
                      + extension.contract(g, q, extension.OUTSIDE))
        y = derivative[:, list(columns)]*inverse
        if derivative != y*core:
            raise ArithmeticError('First coefficient cannot be corrected')
        ys.append(y)
        cores.append(extension.contract(p, g, extension.A0)+extension.contract(g, q, extension.A0))
    solve_b, solve_c = solver(cb), solver(cc)
    linear_b, linear_c = [], []
    for i in range(16):
        rb, rc = sp.zeros(400, 14), sp.zeros(400, 6)
        for j, b in enumerate(new_b):
            residual = (extension.contract([b], qs[i], extension.OUTSIDE)
                        - ys[i]*extension.contract([b], g, extension.A0))
            rb[:, j] = -sp.Matrix(list(residual))
        for j, c in enumerate(new_c):
            residual = (extension.contract(ps[i], [c], extension.OUTSIDE)
                        - ys[i]*extension.contract(g, [c], extension.A0))
            rc[:, j] = -sp.Matrix(list(residual))
        b, c = solve_b(rb), solve_c(rc)
        linear_b.append(encode([{j: b[j, k] for j in range(112) if b[j, k]} for k in range(14)]))
        linear_c.append(encode([{j: c[j, k] for j in range(112) if c[j, k]} for k in range(6)]))
    quadratic = []
    for i, j in combinations_with_replacement(range(16), 2):
        residual = extension.contract(ps[i], qs[j], extension.OUTSIDE)-ys[i]*cores[j]
        if i != j:
            residual += extension.contract(ps[j], qs[i], extension.OUTSIDE)-ys[j]*cores[i]
        if residual*annihilator.T != sp.zeros(100, 4):
            raise ArithmeticError('The retained seed needs a nonzero top second derivative')
        z = residual[:, list(columns)]*inverse
        if residual != z*core:
            raise ArithmeticError('Invalid quadratic source correction')
        quadratic.append({'monomial': [i, j], 'B_top': [[], [], [], []],
                          'C_top': [[], [], [], []], 'first_row_correction': encode_correction(z)})
    return {**seed, 'second_linear_B_new': linear_b, 'second_linear_C_new': linear_c,
            'first_row_corrections': [encode_correction(y) for y in ys],
            'second_quadratic': quadratic,
            'scope': 'Exact formal output jets and regular source row corrections through order two only; no matrix target, higher lift or exponent improvement.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed', type=Path, default=PACKAGE / 'seed.json')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(construct(json.loads(args.seed.read_text())), indent=2)+'\n')
