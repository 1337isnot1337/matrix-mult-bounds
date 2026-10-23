"""Complete rational source replay at the exceptional partner a=0,b=1."""
from functools import lru_cache
from itertools import product

import sympy as sp


class ZeroProof:
    def __init__(self, common, certificate):
        self.common, self.cert = common, certificate
        self.previous = common.previous
        self.normal, self.point, self.pure = common.normal, common.point, common.pure

    @staticmethod
    def decode(record):
        return sp.SparseMatrix(*record['shape'], {(i, j): sp.Rational(value)
            for i, j, value in record['entries']})

    def minor_cuts(self, matrix, rows, witnesses, size):
        cuts = self.common.minor_cuts(matrix, rows, witnesses, size)
        if any(not value.is_Rational for value in cuts.todok().values()):
            raise ArithmeticError('The zero-partner minor is not rational')
        return cuts

    @lru_cache(None)
    def data(self):
        generic = self.common.generic
        base = generic.source_data()['base'].subs(self.common.A, 0)
        quotient = self.previous.data()['quotient']
        selected = generic.certificate()['selected_rows']
        obstruction = sp.SparseMatrix.vstack(*(base[[312*c+i for i in selected], :]*quotient for c in range(7)))
        basis, _ = self.point.row_basis(self.point.joint(obstruction, 56))
        even = [168*j+k for j in range(3) for k in range(84)]
        odd = [168*j+84+k for j in range(3) for k in range(84)]
        projection = basis[:, odd]
        combinations, _ = self.normal.sparse_nullspace(projection.T)
        stable = combinations.T*basis
        stable_kernel, _ = self.normal.sparse_nullspace(self.pure.flat3(stable[:, even], 84))
        projected_rows, _ = self.point.row_basis(projection)
        projected = self.pure.flat3(projected_rows, 84)
        parameters, dimensions = sp.SparseMatrix.eye(84), [84]
        for record in self.cert['projection_square_rounds']:
            cuts = self.minor_cuts(projected*parameters, projected_rows.rows, record['witnesses'], 2)
            reduced, _ = self.normal.sparse_nullspace(cuts)
            if record['before'] != parameters.cols or record['after'] != reduced.cols:
                raise ArithmeticError('Incorrect zero-partner square reduction')
            parameters = parameters*reduced
            dimensions.append(parameters.cols)
        if (basis.rows, stable.rows, stable_kernel.cols, dimensions) != (56, 10, 54, [84, 48, 44]):
            raise ArithmeticError('Incorrect complete zero-partner enclosure')
        return {'obstruction': obstruction, 'third': self.common.data()['third'].subs(self.common.A, 0),
                'families': [stable_kernel, parameters], 'projection_dimensions': dimensions}

    def source_rows(self, parameters, selected):
        n = parameters.cols
        full = self.data()['third']*parameters
        joint = sp.SparseMatrix(448, 7*n,
            {(i//7, n*(i % 7)+j): value for (i, j), value in full.todok().items()})
        known = sp.SparseMatrix.vstack(self.point.joint(self.data()['obstruction']*parameters, 56),
            *[joint[7*i:7*(i+1), :] for i in sorted(selected)])
        basis, pivots = self.point.row_basis(known)
        return basis, pivots, joint

    def replay(self, parameters, selected, records):
        selected, dimensions = set(selected), [parameters.cols]
        for record in records:
            n = parameters.cols
            basis, pivots, joint = self.source_rows(parameters, selected)
            if record['kind'] == 'mixed_only':
                combinations, _ = self.normal.sparse_nullspace(basis[:, :6*n].T)
                cuts = combinations.T*basis[:, 6*n:]
            elif record['kind'] == 'cubic_minors':
                cuts = self.minor_cuts(self.point.flat(basis, n), basis.rows, record['witnesses'], 3)
            elif record['kind'] == 'low_sources':
                if record['parameters'] != n:
                    raise ArithmeticError('Incorrect zero-partner source parameter count')
                residual = joint-joint[:, pivots]*basis
                for item in record['sources']:
                    source = item['source_position']
                    if (not 0 <= source < 64 or source in selected
                            or item['source_index'] != self.normal.KERNEL[source]):
                        raise ArithmeticError('Invalid zero-partner source identity')
                    block = residual[7*source:7*(source+1), :]
                    bound = item['bound']
                    if 'cover' in bound:
                        self.point.check_cover(block, n, bound['cover'])
                    elif (self.previous.graph.third.matrix_rank(block) != bound['joint_B_rank']
                          or bound['joint_B_rank'] > 2):
                        raise ArithmeticError('The zero-partner slice exceeds the target gap')
                    selected.add(source)
                continue
            else:
                raise ArithmeticError('Unknown zero-partner source reduction')
            reduced, _ = self.normal.sparse_nullspace(cuts)
            if record['before'] != n or record['after'] != reduced.cols or reduced.cols >= n:
                raise ArithmeticError('Incorrect zero-partner complete kernel')
            parameters = parameters*reduced
            dimensions.append(parameters.cols)
        return parameters, selected, dimensions

    def span(self, minors, targets):
        basis, pivots = self.point.row_basis(minors)
        if targets != targets[:, pivots]*basis:
            raise ArithmeticError('A zero-partner cubic span identity fails')

    def linear_cubes(self, parameters, selected):
        basis, _, _ = self.source_rows(parameters, selected)
        cuts, covered = [], []
        if [r['group'] for r in self.cert['linear_cube_cases']] != [0, 1]:
            raise ArithmeticError('Incomplete zero-partner cube coverage')
        for record in self.cert['linear_cube_cases']:
            columns, rows = self.previous.partition(parameters, basis, record)
            covered.extend(columns)
            minors = self.previous.cubic_coefficients(basis, columns, rows, record['witnesses'])
            forms = self.decode(record['forms'])
            variables = sp.symbols('x0:'+str(len(columns)))
            targets = self.previous.polynomial_rows([f**3 for f in forms*sp.Matrix(variables)], variables)
            self.span(minors, targets)
            cuts.append(sp.SparseMatrix(forms.rows, parameters.cols,
                {(i, columns[j]): value for (i, j), value in forms.todok().items()}))
        if sorted(covered) != list(range(parameters.cols)):
            raise ArithmeticError('A zero-partner cube block was omitted')
        reduced, _ = self.normal.sparse_nullspace(sp.SparseMatrix.vstack(*cuts))
        return parameters*reduced

    def branches(self, parameters, selected):
        if parameters.cols != 6 or [r['group'] for r in self.cert['stable_branch_certificates']] != [0, 1]:
            raise ArithmeticError('Incorrect zero-partner stable branch coverage')
        basis, _, _ = self.source_rows(parameters, selected)
        groups = []
        u, v, w = sp.symbols('u v w')
        for record in self.cert['stable_branch_certificates']:
            columns, rows = self.previous.partition(parameters, basis, record)
            plane, line = self.decode(record['plane']), self.decode(record['line'])
            if (len(columns) != 3 or plane != sp.Matrix([[0, 0, 1]])
                    or line != sp.Matrix([[-1, 1, 0], [1, 0, 1]])):
                raise ArithmeticError('Incorrect zero-partner branch equations')
            minors = self.previous.cubic_coefficients(basis, columns, rows, record['witnesses'])
            targets = self.previous.polynomial_rows([w*f**2 for f in line*sp.Matrix([u, v, w])], (u, v, w))
            self.span(minors, targets)
            groups.append(columns)
        output = []
        for modes in product(('A', 'B'), repeat=2):
            cuts = []
            for columns, mode in zip(groups, modes):
                matrix = sp.Matrix([[0, 0, 1]]) if mode == 'A' else sp.Matrix([[-1, 1, 0], [1, 0, 1]])
                cuts.append(sp.SparseMatrix(matrix.rows, 6,
                    {(i, columns[j]): value for (i, j), value in matrix.todok().items()}))
            reduced, _ = self.normal.sparse_nullspace(sp.SparseMatrix.vstack(*cuts))
            output.append(('stable-'+''.join(modes), parameters*reduced))
        return output

    @lru_cache(None)
    def report(self):
        if [r['case'] for r in self.cert['initial_source_cases']] != ['stable', 'rank-one-projection']:
            raise ArithmeticError('Both zero-partner initial families must be covered')
        stable, traces = None, []
        for family, record in zip(self.data()['families'], self.cert['initial_source_cases']):
            parameters, selected, dimensions = self.replay(family, set(), record['records'])
            if sorted(selected) != record['selected_sources']:
                raise ArithmeticError('Incorrect zero-partner selected source set')
            if record['case'] == 'stable':
                parameters = self.linear_cubes(parameters, selected)
                dimensions.append(parameters.cols)
                stable = (parameters, selected)
            elif parameters.cols:
                raise ArithmeticError('The zero-partner rank-one family remains')
            traces.append({'case': record['case'], 'dimensions': dimensions})
        branches, records = self.branches(*stable), self.cert['stable_terminal_branches']
        if [name for name, _ in branches] != [r['case'] for r in records]:
            raise ArithmeticError('A zero-partner terminal branch was omitted')
        terminal = []
        for (name, parameters), record in zip(branches, records):
            remaining, selected, dimensions = self.replay(parameters, stable[1], record['records'])
            if remaining.cols or sorted(selected) != record['selected_sources']:
                raise ArithmeticError('A zero-partner stable family remains')
            terminal.append({'case': name, 'dimensions': dimensions})
        return {'partner': {'a': 0, 'b': 1}, 'projection_reductions': self.data()['projection_dimensions'],
                'initial_source_traces': traces, 'stable_terminal_traces': terminal,
                'final_nonplane_dimension': 0, 'all_graphs_excluded': True}
