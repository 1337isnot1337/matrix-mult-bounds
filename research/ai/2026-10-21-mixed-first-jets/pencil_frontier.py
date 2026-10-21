"""Verify the generic mixed-pencil normal space and twelve cubic minors."""
import argparse
from functools import lru_cache
import json
from pathlib import Path

import sympy as sp

import importlib.util

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('pencil_third_order', HERE / 'third_order.py')
third = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(third)
RESULTS = HERE.parents[2] / 'results/mixed-first-jets-2026-10-21'
minimum = third.load('pencil_primitive_forms', HERE.parent / '2026-10-21-moving-boundary-flags/minimum_rank.py')


def flatten(maps):
    return sp.MutableSparseMatrix(64*84, 16,
        {(84*i+j, k): value for i, a in enumerate(third.normal.KERNEL)
         for (j, k), value in maps[a].todok().items()})


def verify_cubic_minors(matrix, certificate):
    if len(certificate['rounds']) != 1:
        raise ArithmeticError('Expected the single retained cubic-minor stage')
    forms = []
    for record in certificate['rounds'][0]['minors']:
        positions = record['positions']
        form = tuple(tuple(pair) for pair in record['form'])
        if (len(positions) != 3 or len({i for i, j in positions}) != 3
                or len({j for i, j in positions}) != 3):
            raise ArithmeticError('Invalid cubic minor coordinates')
        for k, (i, j) in enumerate(positions):
            diagonal = {c: matrix[84*i+j, c] for c in range(matrix.cols)
                        if matrix[84*i+j, c]}
            if minimum.primitive_form(diagonal) != form:
                raise ArithmeticError('The three diagonal linear forms do not agree')
            for _, col in positions[k+1:]:
                if any(matrix.row(84*i+col)):
                    raise ArithmeticError('A cubic-minor triangular zero is nonzero')
        forms.append(form)
    constraints = sp.MutableSparseMatrix(len(forms), 16,
        {(i, j): value for i, form in enumerate(forms) for j, value in form})
    kernel, _ = third.normal.sparse_nullspace(constraints)
    if kernel.cols != 4 or matrix*kernel != sp.zeros(matrix.rows, 4):
        raise ArithmeticError('The cubic minors did not force the complete zero obstruction')
    return kernel, third.rank_certificate(constraints)


def check_orbit_identities():
    def weight(index):
        return index//28+(index//7) % 4+index % 7-6

    def flip(index):
        return third.verify.index(3-index//28, 3-(index//7) % 4, 6-index % 7)

    def transpose(index):
        return third.verify.index((index//7) % 4, index//28, index % 7)

    terms = third.verify.TERMS
    if any(sum(weight(i) for i in term) for term in terms):
        raise ArithmeticError('Diagonal source scaling does not preserve the tensor')
    if {tuple(flip(i) for i in term) for term in terms} != set(terms):
        raise ArithmeticError('Simultaneous short-index reversal fails')
    if {(transpose(a), transpose(c), transpose(b)) for a, b, c in terms} != set(terms):
        raise ArithmeticError('Output-leg exchange and short-index transposition fail')
    for z in (1, 2, 4, 5):
        if {weight(third.verify.index(i, j, z)) for i, j in ((0, 3), (3, 0))} != {z-3}:
            raise ArithmeticError('The diagonal action does not preserve the leading flag')
    # Both terms of each mixed row have the same weight; changing j from
    # one to two increases it by one, so the pencil parameter becomes t*lambda.
    for j in (1, 2):
        for z in (4, 5):
            if weight(third.verify.index(0, j, z)) != j+z-6:
                raise ArithmeticError('Incorrect mixed-pencil weight')
            if weight(third.verify.index(3, j, z-3)) != j+z-6:
                raise ArithmeticError('Mixed-row terms scale differently')
    return {'source_terms_checked': len(terms), 'parameter_action': 'lambda -> t*lambda',
            'nonzero_parameter_representative': 1,
            'endpoint_reversal': 'lambda=0 <-> lambda=infinity',
            'output_leg_exchange_with_short_index_transposition': True}


@lru_cache(None)
def report():
    certificate = json.loads((RESULTS / 'generic-pencil-twojet.json').read_text())
    family_report = third.verify.verify(certificate)
    data = third.normal.data()
    eb, ec = data['E_B_complement'], data['E_C_complement']
    expected = eb[:12]+[
        {j: eb[12+k].get(j, 0)+eb[14+k].get(j, 0) for j in range(112)
         if eb[12+k].get(j, 0)+eb[14+k].get(j, 0)} for k in (0, 1)]
    left = third.verify.rows(certificate['first_constant_B_new'])
    right = third.verify.rows(certificate['first_constant_C_new'])
    if left != expected or third.verify.covector_rank(ec[:12]+right) != 12:
        raise ArithmeticError('The family is not the specified generic mixed pencil')
    opposite = third.extension.contract(left[12:], ec[:12], third.extension.OUTSIDE)
    opposite = sp.MutableSparseMatrix(200, 12, lambda r, c: opposite[r//2, 12*(r % 2)+c])
    if third.matrix_rank(opposite) != 6:
        raise ArithmeticError('The opposite boundary annihilator is not exactly six-dimensional')
    directions = third.top_directions(certificate)
    normals = directions[third.normal.NORMAL, :]
    parameters = normals[data['free'], :]
    cross = third.first_constraints(certificate)
    if (data['first_kernel']*parameters != normals
            or third.matrix_rank(parameters) != 16
            or any(cross*parameters)):
        raise ArithmeticError('Invalid complete normal-space basis')
    cross_rank = third.rank_certificate(cross)
    if cross_rank['rational_rank'] != 212:
        raise ArithmeticError('Unexpected generic normal dimension')
    matrix = flatten(third.third_coefficients(certificate))
    minor_certificate = json.loads((RESULTS / 'generic-pencil-minors.json').read_text())
    kernel, minor_rank = verify_cubic_minors(matrix, minor_certificate)
    plane = sp.Matrix.hstack(*(sp.Matrix([row.get(j, 0) for row in rows for j in range(112)])
                              for rows in third.normal.plane_directions()))
    if third.matrix_rank((directions*kernel).row_join(plane)) != 4:
        raise ArithmeticError('Remaining normal directions are not exactly plane motion')
    return {'field': 'Q, with polynomial implications over C',
            'representative_parameter': 1,
            'twojet_family': family_report,
            'mixed_cross_rank_certificate': cross_rank,
            'compatible_normal_dimension': 16,
            'third_first_flattening_shape': [64, 84],
            'cubic_minor_count': len(minor_certificate['rounds'][0]['minors']),
            'forced_linear_rank_certificate': minor_rank,
            'minimum_nonzero_third_first_flattening_rank_at_least': 3,
            'zero_third_obstruction_normal_dimension': 4,
            'zero_space_equals_common_plane_tangents': True,
            'source_orbit_checks': check_orbit_identities(),
            'scope': 'Finite certificates for pencil_frontier.md; neither an improving matrix tensor nor an exponent bound.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(report(), indent=2)+'\n')
