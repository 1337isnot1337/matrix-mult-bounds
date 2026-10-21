"""Exact b=0 source closure, completing the finite affine partner chart."""
import argparse
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


line = load('affine_chart_line', HERE.parent / '2026-10-21-full-partner-line/verify.py')
common = line.common
generic, graph = common.generic, common.graph
normal, point, pure = common.normal, common.point, common.pure


@lru_cache(None)
def certificate():
    return json.loads((HERE / 'certificate.json').read_text())


class BoundaryProof(line.zero_module.ZeroProof):
    """Reuse rational source implications; reconstruct this fiber independently."""

    @lru_cache(None)
    def data(self):
        full = common.uniform.data()
        specialization = {common.A: 1, common.B: 0}
        psi = sp.SparseMatrix(full['virtual']['psi'].subs(specialization))
        tensor = sp.SparseMatrix(full['virtual']['third'].subs(specialization))
        sources = sp.SparseMatrix(full['sources'].subs(specialization))
        low = graph.source_action(tensor, sources)
        entries = {(312*(i//200)+i % 200, j): value for (i, j), value in psi.todok().items()}
        for source in range(16):
            for (i, j), value in low[49*source:49*(source+1), :].todok().items():
                brow, c = divmod(i, 7)
                entries[312*c+200+7*source+brow, j] = value
        base = sp.SparseMatrix(2184, 88, entries)
        plane = common.frames.plane_parameters()[full['normal_certificate']['free_coordinates'], :]
        if (len(plane.to_DM().rref()[1]) != 4 or (base*plane).todok()
                or (tensor*plane).todok()):
            raise ArithmeticError('Incorrect boundary common-plane kernel')
        _, columns = plane.row_join(sp.eye(88)).to_DM().rref()
        quotient = sp.SparseMatrix.eye(88)[:, [j-4 for j in columns[4:]]]
        # Use all 312 source rows here; do not specialize a generic row selection.
        basis, _ = point.row_basis(point.joint(base*quotient, 312))
        obstruction = point.flat(basis, 84)
        even = [168*j+k for j in range(3) for k in range(84)]
        odd = [168*j+84+k for j in range(3) for k in range(84)]
        projection = basis[:, odd]-basis[:, even]
        combinations, _ = normal.sparse_nullspace(projection.T)
        stable = combinations.T*basis
        stable_kernel, _ = normal.sparse_nullspace(pure.flat3(stable[:, even], 84))
        projected_rows, _ = point.row_basis(projection)
        projected = pure.flat3(projected_rows, 84)
        parameters, dimensions = sp.SparseMatrix.eye(84), [84]
        for record in self.cert['projection_square_rounds']:
            cuts = self.minor_cuts(projected*parameters, projected_rows.rows, record['witnesses'], 2)
            reduced, _ = normal.sparse_nullspace(cuts)
            if record['before'] != parameters.cols or record['after'] != reduced.cols:
                raise ArithmeticError('Incorrect boundary projection reduction')
            parameters = parameters*reduced
            dimensions.append(parameters.cols)
        if (basis.rows, stable.rows, stable_kernel.cols, dimensions) != (56, 10, 54, [84, 52, 48]):
            raise ArithmeticError('Incorrect complete boundary enclosure')
        change = sp.SparseMatrix.eye(64)
        for k, source in enumerate(normal.KERNEL):
            i, q, z = source//28, (source//7) % 4, source % 7
            if i == 2:
                change[normal.KERNEL.index(28+7*q+z), k] -= 1
        if any(i >= j for i, j in (change-sp.eye(64)).todok()):
            raise ArithmeticError('Boundary source change is not unitriangular')
        return {'quotient': quotient, 'obstruction': obstruction,
                'third': graph.source_action(tensor*quotient, change),
                'families': [stable_kernel, parameters], 'projection_dimensions': dimensions}

    def partition(self, parameters, basis, record):
        embedding = self.data()['quotient']*parameters
        groups = {i: k for k, group in enumerate(generic.certificate()['normal_components']) for i in group}
        column_groups = []
        for j in range(parameters.cols):
            supported = {groups[i] for i in range(88) if embedding[i, j]}
            if len(supported) != 1:
                raise ArithmeticError('A boundary parameter mixes source blocks')
            column_groups.append(supported.pop())
        columns = [j for j, group in enumerate(column_groups) if group == record['group']]
        rows = []
        for i in range(basis.rows):
            supported = {column_groups[j % parameters.cols] for (_, j), value in basis[i:i+1, :].todok().items()}
            if len(supported) != 1:
                raise ArithmeticError('A boundary source row mixes blocks')
            if supported == {record['group']}:
                rows.append(i)
        if columns != record['normal_parameters'] or rows != record['source_rows']:
            raise ArithmeticError('Incorrect boundary cubic block partition')
        return columns, rows

    def linear_cubes(self, parameters, selected, case):
        records = [r for r in self.cert['linear_cube_cases'] if r['case'] == case]
        if [r['group'] for r in records] != [0, 1]:
            raise ArithmeticError('Incomplete boundary cube-block coverage')
        basis, _, _ = self.source_rows(parameters, selected)
        cuts, covered, ranks = [], [], []
        for record in records:
            columns, rows = self.partition(parameters, basis, record)
            covered.extend(columns)
            minors = common.previous.cubic_coefficients(basis, columns, rows, record['witnesses'])
            forms = self.decode(record['forms'])
            variables = sp.symbols('x0:'+str(len(columns)))
            targets = common.previous.polynomial_rows([f**3 for f in forms*sp.Matrix(variables)], variables)
            self.span(minors, targets)
            expected = (7, 79, 84, 4) if case == 'stable' else (5, 31, 35, 3)
            rank = len(minors.to_DM().rref()[1])
            if (len(columns), rank, minors.cols, forms.rows) != expected:
                raise ArithmeticError('Incorrect boundary moment rank')
            ranks.append({'variables': len(columns), 'actual_cubic_rank': rank,
                          'cubic_monomials': minors.cols, 'linear_cubes': forms.rows})
            cuts.append(sp.SparseMatrix(forms.rows, parameters.cols,
                {(i, columns[j]): value for (i, j), value in forms.todok().items()}))
        if sorted(covered) != list(range(parameters.cols)):
            raise ArithmeticError('A boundary normal block was omitted')
        reduced, _ = normal.sparse_nullspace(sp.SparseMatrix.vstack(*cuts))
        return parameters*reduced, ranks

    @lru_cache(None)
    def report(self):
        names = ['stable', 'rank-one-projection']
        if ([r['case'] for r in self.cert['initial_source_cases']] != names
                or [r['case'] for r in self.cert['terminal_source_cases']] != names
                or [(r['case'], r['group']) for r in self.cert['linear_cube_cases']]
                != [(name, group) for name in names for group in range(2)]):
            raise ArithmeticError('Incomplete boundary case coverage')
        cases = []
        for family, initial, terminal in zip(self.data()['families'],
                self.cert['initial_source_cases'], self.cert['terminal_source_cases']):
            parameters, selected, dimensions = self.replay(family, set(), initial['records'])
            if sorted(selected) != initial['selected_sources']:
                raise ArithmeticError('Incorrect initial boundary source set')
            parameters, ranks = self.linear_cubes(parameters, selected, initial['case'])
            moment_dimension = parameters.cols
            remaining, selected, terminal_dimensions = self.replay(parameters, selected, terminal['records'])
            if remaining.cols or sorted(selected) != terminal['selected_sources']:
                raise ArithmeticError('A nonplane boundary normal survives')
            cases.append({'case': initial['case'], 'initial_source_dimensions': dimensions,
                          'moment_blocks': ranks, 'after_linear_cubes': moment_dimension,
                          'terminal_source_dimensions': terminal_dimensions,
                          'final_selected_sources': len(selected)})
        return {'partner': {'a': 1, 'b': 0},
                'projection_dimensions': self.data()['projection_dimensions'],
                'cases': cases, 'final_nonplane_dimension': 0, 'plane_dimension': 4,
                'all_mixed_graphs_covered': True, 'arbitrary_boundary_four_space': True}


proof = BoundaryProof(common, certificate())


def torus_report(boundary_weights):
    extension = normal.extension
    def weight(index):
        return index//28+(index//7) % 4+index % 7
    if any(sum(weight(index) for index in term) != 18 for term in extension.TERMS):
        raise ArithmeticError('The source is not homogeneous of total weight 18')
    if any(len({weight(index) for index in row}) != 1 for row in extension.G):
        raise ArithmeticError('The torus does not preserve the leading G flag')
    generic.check_torus(boundary_weights, 7)
    return {'source_terms': len(extension.TERMS), 'total_source_weight': 18,
            'partner_action': '(a,b) -> (a/lambda,b/lambda)',
            'normalizes_a_nonzero_b_zero_to': {'a': 1, 'b': 0}}


@lru_cache(None)
def report():
    point_report = proof.report()
    torus = torus_report(generic.certificate()['torus_boundary_weights'])
    # The corner's existing finite source verifier is replayed, not inferred by continuity.
    corner = common.uniform.point.report()
    if corner['partner'] != [0, 0, 0, 1] or corner['normal_dimensions'][-1] != 4:
        raise ArithmeticError('The corner source closure is incomplete')
    return {'claim': 'AI-AFFINE-PARTNER-CHART-100', 'boundary_point': point_report,
            'torus': torus, 'corner_claim_replayed': corner['claim'],
            'adopted_b_nonzero_claim': 'AI-FULL-PARTNER-LINE-099',
            'b_nonzero_verifier_replayed_here': False,
            'all_finite_a_b_excluded_under_adopted_claims': True,
            'partner_chart': {'u': ['a*b', '-a', '-b', '1'], 'v': ['a*b', 'b', 'a', '1']},
            'first_space_dimensions': [7, 5], 'canonical_leading_flags_required': True,
            'arbitrary_later_regular_maps': True, 'delayed_unequal_orders': True,
            'laurent_first_leg': True, 'projective_endpoints_classified': False,
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
