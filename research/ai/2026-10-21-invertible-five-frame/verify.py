"""Exact annihilator certificates and a complete finite cubic control."""
import argparse
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RESULTS = ROOT / 'results/invertible-five-frame-2026-10-21'
SPEC = importlib.util.spec_from_file_location('five_frame_both', HERE.parent / '2026-10-21-both-mixed-first-spaces/verify.py')
both = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(both)
extension, source = both.extension, both.third.verify
SEED = ROOT / 'results/both-mixed-first-spaces-2026-10-21/invertible-lines-seed.json'


def seed_rows():
    seed = json.loads(SEED.read_text())
    return source.rows(seed['first_constant_B_new']), source.rows(seed['first_constant_C_new'])


def annihilator(side, frame):
    identity = [{i: 1} for i in range(112)]
    entries = {}
    if side == 'B':
        tensor = extension.contract(identity, frame, extension.OUTSIDE)
        for (x, column), value in tensor.todok().items():
            b, c = divmod(column, len(frame))
            entries[len(frame)*x+c, b] = value
    else:
        tensor = extension.contract(frame, identity, extension.OUTSIDE)
        for (x, column), value in tensor.todok().items():
            b, c = divmod(column, 112)
            entries[len(frame)*x+b, c] = value
    return sp.MutableSparseMatrix(100*len(frame), 112, entries)


def cubic_control(certificate, contract=source.contract):
    if (certificate['order'] != 3 or len(certificate['P']) != 4
            or len(certificate['Q']) != 4 or len(certificate['source_corrections']) != 3):
        raise ArithmeticError('Wrong cubic coefficient coverage')
    p = [source.rows(rows) for rows in certificate['P']]
    q = [source.rows(rows) for rows in certificate['Q']]
    if any(len(rows) != 5 for rows in p+q):
        raise ArithmeticError('Wrong active output dimensions')
    left, right = seed_rows()
    if p[0] != extension.G+[{}] or q[0] != extension.G+[{}] or p[1][4:] != left or q[1][4:] != right:
        raise ArithmeticError('The cubic control changes the retained first seed')
    coefficients = [source.add(*[(1, contract(p[i], q[k-i])) for i in range(k+1)])
                    for k in range(4)]
    for k in range(4):
        terms = [(1, coefficients[k])]
        terms += [(-1, source.correct(certificate['source_corrections'][j-1], coefficients[k-j]))
                  for j in range(1, k+1)]
        source.check_kernel(f'complete cubic coefficient {k}', source.add(*terms))
    linear = [[{j: rows0[i].get(j, 0)+rows1[i].get(j, 0) for j in range(112)
                if rows0[i].get(j, 0)+rows1[i].get(j, 0)} for i in range(5)]
              for rows0, rows1 in ((p[0], p[1]), (q[0], q[1]))]
    rank = both.third.matrix_rank(extension.contract(*linear, range(112)))
    if rank != 13:
        raise ArithmeticError('The uncorrected first-rank-thirteen control changed')
    return {'source_terms': 4096, 'field': 'Q', 'active_output_dimensions': [5, 5],
            'coefficients_checked': 4, 'kernel_rows_checked_per_coefficient': 100,
            'output_entries_per_source_row': 25, 'formal_order_verified': 3,
            'uncorrected_linear_first_rank_at_t_one': rank,
            'scope': 'One finite cubic curve with source corrections; no all-order lift or target.'}


@lru_cache(None)
def report():
    left, right = seed_rows()
    if any(extension.contract(left, right, extension.OUTSIDE)):
        raise ArithmeticError('The first new lines are incompatible')
    records = {}
    for side, frame, expected in (('B', extension.G+right, extension.G+left),
                                  ('C', extension.G+left, extension.G+right)):
        matrix = annihilator(side, frame)
        kernel = sp.Matrix(112, 5, lambda i, j: expected[j].get(i, 0))
        if any(matrix*kernel) or both.third.matrix_rank(kernel) != 5:
            raise ArithmeticError('The proposed five-frame kernel is invalid')
        certificate = both.third.rank_certificate(matrix)
        if certificate['rational_rank'] != 107:
            raise ArithmeticError('The annihilator is larger than the five-frame')
        records[side] = {'rank_certificate': certificate, 'kernel_dimension': 5,
                         'kernel_is_own_five_frame': True}
    return {'field': 'Q, with linear identities over C',
            'annihilators': records, 'minor_prime': extension.PRIME,
            'five_cross_maximum_matrix_rank': 10, 'target_minimum_nonzero_matrix_rank': 11,
            'cubic_control': cubic_control(json.loads((RESULTS / 'cubic-control.json').read_text())),
            'scope': 'Exact seed checks and finite cubic lift. The all-parameter and all-order conclusion uses the separate written proof and the adopted both-mixed classification.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(report(), indent=2)+'\n')
