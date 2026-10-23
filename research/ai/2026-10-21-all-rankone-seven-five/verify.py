"""Exact endpoint closure and projective rank-one seven-by-five coverage."""
import argparse
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('all_rankone_affine', HERE.parent / '2026-10-21-affine-partner-chart/verify.py')
affine = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(affine)
common = affine.common
frames, normal, point = common.frames, common.normal, common.point


@lru_cache(None)
def certificate():
    return json.loads((HERE / 'certificate.json').read_text())


class EndpointProof(affine.line.zero_module.ZeroProof):
    @lru_cache(None)
    def data(self):
        left, right = frames.endpoint_frames()
        if left[12:, 6] != sp.Matrix([0, 0, -1, 0]) or right[12:, 6] != sp.Matrix([0, 1, 0, 0]):
            raise ArithmeticError('Incorrect exceptional mixed partners')
        if any(len(matrix.to_DM().rref()[1]) != 7 for matrix in (left, right)):
            raise ArithmeticError('An endpoint maximal frame loses rank')
        parameters, free = normal.sparse_nullspace(frames.constraints(left, sp.zeros(16, 0)))
        if parameters.cols != 88:
            raise ArithmeticError('Incorrect complete endpoint normal dimension')
        virtual = point.build_virtual(left, right, parameters)
        plane = frames.plane_parameters()[free, :]
        if (len(plane.to_DM().rref()[1]) != 4 or (virtual['psi']*plane).todok()
                or (virtual['third']*plane).todok()):
            raise ArithmeticError('Incorrect endpoint common-plane kernel')
        _, columns = plane.row_join(sp.eye(88)).to_DM().rref()
        quotient = sp.SparseMatrix.eye(88)[:, [j-4 for j in columns[4:]]]
        basis, _ = point.row_basis(point.joint(virtual['psi']*quotient, 200))
        if basis.rows != 42 or quotient.cols != 84:
            raise ArithmeticError('Incorrect full endpoint obstruction rowspace')
        return {'obstruction': point.flat(basis, 84), 'source_rows': basis.rows,
                'third': virtual['third']*quotient, 'normal_dimension': parameters.cols}

    def source_rows(self, parameters, selected):
        n = parameters.cols
        full = self.data()['third']*parameters
        joint = sp.SparseMatrix(448, 7*n,
            {(i//7, n*(i % 7)+j): value for (i, j), value in full.todok().items()})
        known = sp.SparseMatrix.vstack(
            point.joint(self.data()['obstruction']*parameters, self.data()['source_rows']),
            *[joint[7*i:7*(i+1), :] for i in sorted(selected)])
        basis, pivots = point.row_basis(known)
        return basis, pivots, joint

    @lru_cache(None)
    def report(self):
        remaining, selected, dimensions = self.replay(sp.SparseMatrix.eye(84), set(), self.cert['records'])
        if remaining.cols or sorted(selected) != self.cert['selected_sources']:
            raise ArithmeticError('A nonplane endpoint normal survives')
        return {'partners': {'u': [0, 0, -1, 0], 'v': [0, 1, 0, 0]},
                'complete_normal_dimension': self.data()['normal_dimension'],
                'initial_source_coefficient_rows': self.data()['source_rows'],
                'quotient_dimensions': dimensions, 'added_coordinate_sources': len(selected),
                'final_nonplane_dimension': 0, 'plane_dimension': 4,
                'all_mixed_graphs_covered': True, 'arbitrary_boundary_four_space': True}


proof = EndpointProof(common, certificate())


def reverse(index):
    return normal.extension.index(3-index//28, 3-(index//7) % 4, 6-index % 7)


def reversal_report(transform=reverse):
    extension = normal.extension
    images = [transform(i) for i in range(112)]
    if sorted(images) != list(range(112)) or any(transform(transform(i)) != i for i in range(112)):
        raise ArithmeticError('The reversal is not an involutive coordinate permutation')
    terms = set(extension.TERMS)
    if any(tuple(transform(i) for i in term) not in terms for term in terms):
        raise ArithmeticError('The reversal does not preserve the original source tensor')
    def normalized(row):
        scalar = row[min(row)]
        return frozenset((i, sp.Rational(value, scalar)) for i, value in row.items())
    leading = {normalized(row) for row in extension.G}
    if any(normalized({transform(i): value for i, value in row.items()}) not in leading for row in extension.G):
        raise ArithmeticError('The reversal does not preserve the leading flags')
    checked = 0
    for key in ('E_B_complement', 'E_C_complement'):
        basis = normal.data()[key]
        for k, row in enumerate(basis[12:]):
            if {transform(i): value for i, value in row.items()} != basis[15-k]:
                raise ArithmeticError('The source action does not reverse the mixed coordinates')
            checked += 1
    return {'source_terms_checked': len(terms), 'source_coordinate_permutation': 112,
            'leading_rows_preserved': len(extension.G), 'mixed_rows_checked': checked,
            'mixed_action': '(v0,v1,v2,v3) -> (v3,v2,v1,v0)',
            'exchanges_projective_endpoints': True}


@lru_cache(None)
def report():
    endpoint = proof.report()
    reversal = reversal_report()
    return {'claim': 'AI-ALL-RANKONE-SEVEN-FIVE-101', 'endpoint': endpoint,
            'reversal': reversal, 'adopted_affine_claim': 'AI-AFFINE-PARTNER-CHART-100',
            'affine_chart_verifier_replayed_here': False,
            'coverage': ['v3 nonzero: affine chart', 'v0 nonzero: source reversal',
                         'v0=v3=0: the two reversed coordinate endpoints'],
            'all_projective_rankone_partners_excluded_under_adopted_claims': True,
            'first_space_dimensions': [7, 5], 'canonical_leading_flags_required': True,
            'arbitrary_later_regular_maps': True, 'delayed_unequal_orders': True,
            'laurent_first_leg': True, 'smaller_first_spaces_classified': False,
            'independent_review': False, 'improves_omega': False}


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
