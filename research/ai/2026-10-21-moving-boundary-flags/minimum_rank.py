"""Exact repeated-minor certificates: a nonzero obstruction has rank >=4."""
import argparse
from collections import defaultdict
import importlib.util
import json
from math import gcd
from pathlib import Path

import sympy as sp

SPEC = importlib.util.spec_from_file_location('rank_four_normal', Path(__file__).with_name('normal_directions.py'))
normal = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(normal)


def primitive_form(row):
    """Return an integer linear form up to nonzero rational scaling."""
    row = {j: value for j, value in row.items() if value}
    if not row:
        return ()
    denominator = sp.ilcm(*(value.q for value in row.values())) if len(row) > 1 else next(iter(row.values())).q
    values = {j: int(value*denominator) for j, value in row.items()}
    divisor = gcd(*values.values())
    if values[min(values)] < 0:
        divisor = -divisor
    return tuple(sorted((j, value//divisor) for j, value in values.items()))


def form_table(matrix):
    rows = defaultdict(dict)
    for (i, j), value in matrix.todok().items():
        rows[i][j] = value
    forms, positions, table = [], defaultdict(list), [[0]*16 for _ in range(200)]
    indices = {}
    for i in range(200):
        for j in range(16):
            form = primitive_form(rows[200*j+i])
            if not form:
                continue
            if form not in indices:
                indices[form] = len(forms)+1
                forms.append(form)
            index = indices[form]
            positions[index].append((i, j))
            table[i][j] = index
    return forms, positions, table


def triangular_witness(table, positions, size=4):
    def search(chosen, candidates):
        if len(chosen) == size:
            return chosen
        if len(candidates) < size-len(chosen):
            return None
        for i, j in candidates:
            if any(table[r][j] or r == i or c == j for r, c in chosen):
                continue
            remaining = [(r, c) for r, c in candidates
                         if r != i and c != j and table[i][c] == 0]
            result = search(chosen+[(i, j)], remaining)
            if result is not None:
                return result
        return None
    return search([], positions)


def verify_minor(matrix, positions, form):
    """Verify the exact triangular identity, independently of the search."""
    if len(positions) != 4 or len({i for i, _ in positions}) != 4 or len({j for _, j in positions}) != 4:
        raise ArithmeticError('Not a four-by-four minor')
    for k, (i, j) in enumerate(positions):
        row = {c: matrix[200*j+i, c] for c in range(matrix.cols) if matrix[200*j+i, c]}
        if primitive_form(row) != tuple(tuple(pair) for pair in form):
            raise ArithmeticError('Diagonal forms do not agree')
        for _, col in positions[k+1:]:
            if any(matrix.row(200*col+i)):
                raise ArithmeticError('Claimed triangular zero is nonzero')


def chain(matrix):
    records = []
    while any(matrix):
        forms, positions, table = form_table(matrix)
        chosen, witnesses = [], []
        for index, form in enumerate(forms, 1):
            witness = triangular_witness(table, positions[index])
            if witness is not None:
                verify_minor(matrix, witness, form)
                chosen.append(form)
                witnesses.append({'positions': witness, 'form': form})
        if not chosen:
            raise ArithmeticError('Repeated four-by-four minors did not close the rank test')
        constraints = sp.MutableSparseMatrix(len(chosen), matrix.cols,
                                              {(i, j): value for i, row in enumerate(chosen)
                                               for j, value in row})
        kernel, _ = normal.sparse_nullspace(constraints)
        records.append({'parameter_dimension': matrix.cols,
                        'entry_linear_forms': len(forms),
                        'forced_linear_rank': matrix.cols-kernel.cols,
                        'minors': witnesses})
        matrix = matrix*kernel
    return {'rounds': records, 'final_parameter_dimension': matrix.cols,
            'final_obstruction_identically_zero': True}


def report():
    data = normal.data()
    records = {side: chain(data[key]) for side, key in (
        ('B', 'left_obstruction'), ('C', 'right_obstruction'))}
    for record in records.values():
        assert [r['forced_linear_rank'] for r in record['rounds']] == [82, 42, 16]
        assert record['final_parameter_dimension'] == 88
    # This is sharp for the auxiliary matrix space, not a target construction.
    left = sp.Matrix(200, 16, lambda i, j: data['left_obstruction'][200*j+i, 90])
    right = sp.Matrix(200, 16, lambda i, j: data['right_obstruction'][200*j+i, 90])
    assert normal.extension.rational_rank(left) == 4
    assert right == sp.zeros(200, 16)
    return {'field': 'Q, with the rank implication over C',
            'matrix_shape': [200, 16], 'initial_parameter_dimension': 228,
            'minimum_nonzero_obstruction_rank': 4, 'chains': records,
            'sharp_auxiliary_control': {'parameter_index': 90, 'B_rank': 4, 'C_rank': 0},
            'excluded_first_quotient_ranks': {'B_at_least': 13, 'C_at_least': 13},
            'scope': 'Necessary source-jet obstruction; neither a matrix target nor an exponent improvement.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(report(), indent=2)+'\n')
