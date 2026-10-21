"""Polynomial low-source slices on the entire rank-one v3 chart."""
import argparse
from collections import defaultdict
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('uniform_five_point', HERE.parent / '2026-10-21-mixed-five-space-residues/verify.py')
point = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(point)
frames, normal, third, hyper = point.frames, point.normal, point.third, point.hyper
A, B = frames.A, frames.B
encode = point.encode


def expand(matrix):
    return sp.MutableSparseMatrix(matrix.applyfunc(sp.expand))


def polynomial_row_basis(matrix):
    """A constant nonzero minor certifies the row basis at every a,b."""
    base = matrix.subs({A: 0, B: 0})
    certificate = third.rank_certificate(base)
    rows, columns = certificate['minor_rows'], certificate['minor_columns']
    inverse = base[rows, columns].inv()
    nilpotent = expand(inverse*matrix[rows, columns]-sp.eye(len(rows)))
    order = frames.triangular_order(nilpotent)
    reduced = expand(inverse*matrix[rows, :])
    adjacency = defaultdict(list)
    for (i, j), value in nilpotent.todok().items():
        adjacency[i].append((j, value))
    for i in reversed(order):
        for j, value in adjacency[i]:
            reduced[i, :] -= value*reduced[j, :]
        reduced[i, :] = reduced[i, :].applyfunc(sp.expand)
    if not frames.zero(matrix-matrix[:, columns]*reduced) or reduced[:, columns] != sp.eye(len(rows)):
        raise ArithmeticError('Invalid polynomial rowspace certificate')
    return reduced, columns, {'base_minor': certificate,
        'normalized_minor_minus_identity': encode(nilpotent), 'triangular_order': order,
        'row_basis': encode(reduced)}


def reduce_rows(matrix):
    reduced, columns, _ = polynomial_row_basis(matrix)
    return reduced, columns


@lru_cache(None)
def data():
    left, right = frames.chart_frames()
    parameters, normal_certificate = hyper.uniform_kernel(frames.constraints(left, sp.zeros(16, 0)))
    virtual = point.build_virtual(left, right, parameters, reduce_rows, expand)
    reduced, pivots, row_certificate = polynomial_row_basis(point.joint(virtual['psi'], 200))
    j = virtual['third']
    j_joint = sp.MutableSparseMatrix(448, 7*88,
        {(i//7, 88*(i % 7)+k): value for (i, k), value in j.todok().items()})
    j_reduced = expand(j_joint-j_joint[:, pivots]*reduced)
    sources = sp.MutableSparseMatrix.zeros(64, 16)
    labels = []
    for s in range(4):
        for z in (1, 2, 4, 5):
            col = len(labels)
            sources[normal.KERNEL.index(56+7*s+z), col] = 1
            sources[normal.KERNEL.index(28+7*s+z), col] = -A
            labels.append([s, z])
    low = expand(sp.kronecker_product(sources.T, sp.SparseMatrix.eye(7))*j_reduced)
    if any(row % 7 != 6 for row, _ in low.todok()):
        raise ArithmeticError('An adapted source has nonzero boundary B rows')
    pivot_rows = [normal.KERNEL.index(56+7*s+z) for s, z in labels]
    if sources[pivot_rows, :] != sp.eye(16):
        raise ArithmeticError('Adapted sources are not uniformly independent')
    return {'virtual': virtual, 'normal_certificate': normal_certificate,
            'row_certificate': row_certificate, 'sources': sources,
            'low': low, 'labels': labels, 'pivots': pivot_rows}


@lru_cache(None)
def report():
    result = data()
    return {'claim': 'AI-MIXED-FIVE-SPACE-LOW-SLICES-088',
            'partner_chart': {'u': ['a*b', '-a', '-b', '1'], 'v': ['a*b', 'b', 'a', '1']},
            'normal_dimension': 88, 'adapted_source_dimension': 16,
            'source_formula': 'e_(2,s,z)-a*e_(1,s,z), s=0,1,2,3; z=1,2,4,5',
            'normal_certificate': result['normal_certificate'],
            'obstruction_rowspace_certificate': result['row_certificate'],
            'virtual_c_residual_factor': encode(result['virtual']['residual_factor']),
            'adapted_sources': encode(result['sources']), 'source_identity_rows': result['pivots'],
            'reduced_adapted_third_coefficients': encode(result['low']),
            'only_nonzero_B_row': 6, 'maximum_slice_rank': 1,
            'scope': 'Uniform necessary vanishing on these sixteen source combinations for a matrix-target lift with full B seven-frame. This is not a complete five-space normal closure or an exponent improvement.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    value = json.dumps(report(), indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(value)
    else:
        print(value, end='')
