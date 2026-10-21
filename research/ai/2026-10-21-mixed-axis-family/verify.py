"""Laurent-unit certificates for the mixed row m+t*d0, b=1."""
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


graph = load('axis_graph', HERE.parent / '2026-10-21-mixed-five-space-graphs/verify.py')
linear = load('axis_laurent_linear', HERE / 'laurent_linear.py')
pure, uniform, point, frames, normal, third = graph.pure, graph.uniform, graph.point, graph.frames, graph.normal, graph.third
A, T = frames.A, sp.Symbol('t')
canonical, encode = linear.canonical, uniform.encode


def decode(record):
    return sp.SparseMatrix(*record['shape'],
        {(i, j): sp.sympify(value, locals={'a': A, 't': T}) for i, j, value in record['entries']})


@lru_cache(None)
def certificate():
    return json.loads((HERE / 'certificate.json').read_text())


@lru_cache(None)
def initial_data():
    full, cert = uniform.data(), certificate()
    psi = canonical(full['virtual']['psi'].subs({frames.B: 1}))
    tensor = canonical(full['virtual']['third'].subs({frames.B: 1}))
    shifted_psi, shifted_tensor = psi.copy(), tensor.copy()
    for (i, j), value in psi.todok().items():
        if i < 200:
            shifted_psi[1200+i, j] += T*value
    for (i, j), value in tensor.todok().items():
        if i % 7 == 0:
            shifted_tensor[7*(i//7)+6, j] += T*value
    psi, tensor = shifted_psi, shifted_tensor
    sources = full['sources']
    low = canonical(graph.source_action(tensor, sources))
    mixed = sp.MutableSparseMatrix.vstack(psi[1200:1400, :],
        low[[49*i+7*j+6 for i in range(16) for j in range(7)], :])
    kernel = decode(cert['normal_kernel'])
    if any(not linear.laurent(value, A, T) for value in kernel.todok().values()):
        raise ArithmeticError('Normal kernel has an unaccounted denominator')
    if kernel[cert['normal_free'], :] != sp.eye(32) or canonical(mixed*kernel).todok():
        raise ArithmeticError('Invalid complete normal kernel')
    minor = cert['normal_minor']
    determinant = mixed[minor['rows'], minor['columns']].to_DM().det().as_expr()
    if sp.expand(determinant-T**18) != 0 or minor['determinant'] != 't**18':
        raise ArithmeticError('Normal rank minor is not t**18')
    plane = frames.plane_parameters()[full['normal_certificate']['free_coordinates'], :]
    plane32 = plane[cert['normal_free'], :]
    if canonical(kernel*plane32-plane).todok() or canonical(psi*plane).todok() or canonical(tensor*plane).todok():
        raise ArithmeticError('Incorrect plane quotient')
    _, columns = sp.Matrix.hstack(plane32, sp.eye(32)).to_DM().rref()
    if list(columns[:4]) != list(range(4)) or len(columns) != 32:
        raise ArithmeticError('Plane complement is incomplete')
    quotient_columns = [j-4 for j in columns[4:]]
    quotient = kernel[:, quotient_columns]
    rows = 312
    entries = {(rows*(i//200)+i % 200, j): value for (i, j), value in psi.todok().items()}
    for source in range(16):
        for (i, j), value in low[49*source:49*(source+1), :].todok().items():
            b, c = divmod(i, 7)
            entries[rows*c+200+7*source+b, j] = value
    obstruction = canonical(sp.SparseMatrix(7*rows, 88, entries)*quotient)
    if obstruction[6*rows:, :].todok():
        raise ArithmeticError('The actual mixed row is not annihilated')
    joint = point.joint(obstruction, rows)
    selected = joint[cert['selected_rows'], :]
    if selected.rows != 56 or len(set(cert['selected_rows'])) != 56:
        raise ArithmeticError('Incorrect selected obstruction rows')
    return {'mixed': mixed, 'kernel': kernel, 'quotient': quotient, 'quotient_columns': quotient_columns,
            'joint': joint, 'selected': selected}



def check_square(matrix, rows, witness):
    positions = witness['positions']
    if len(positions) != 2 or positions[0][0] == positions[1][0] or positions[0][1] == positions[1][1]:
        raise ArithmeticError('Invalid square minor positions')
    form = sp.SparseMatrix(1, matrix.cols,
        {(0, j): sp.sympify(value, locals={'a': A, 't': T}) for j, value in witness['form']})
    scales = [sp.sympify(value, locals={'a': A, 't': T}) for value in witness['scales']]
    if any(not linear.laurent(value, A, T, True) for value in scales):
        raise ArithmeticError('Square minor scale is not a Laurent unit')
    for (row, column), scale in zip(positions, scales):
        if not (0 <= row < rows and 0 <= column < 3):
            raise ArithmeticError('Square minor position is outside the matrix')
        if canonical(matrix[rows*column+row, :]-scale*form).todok():
            raise ArithmeticError('Incorrect square minor diagonal')
    if matrix[rows*positions[1][1]+positions[0][0], :].todok():
        raise ArithmeticError('Square minor triangular zero is missing')
    product = sp.sympify(witness['scale'], locals={'a': A, 't': T})
    if sp.expand(scales[0]*scales[1]-product) != 0:
        raise ArithmeticError('Incorrect square minor product')
    return form


@lru_cache(None)
def split_data():
    data, cert = initial_data(), certificate()
    selected = data['selected']
    even = [56*j+k for j in range(3) for k in range(28)]
    odd = [56*j+28+k for j in range(3) for k in range(28)]
    projection = canonical(T**3*(selected[:, odd]-A**3*selected[:, even]))
    combinations = decode(cert['stable_combinations'])
    if canonical(combinations.T*projection).todok():
        raise ArithmeticError('Stable combinations do not annihilate the projection')
    stable = canonical(combinations.T*selected)
    if canonical(stable[:, odd]-A**3*stable[:, even]).todok() or stable[:, 168:].todok():
        raise ArithmeticError('Incorrect stable row support')
    stable_coefficients = pure.flat3(stable[:, even], 28)
    w_kernel = linear.replay(stable_coefficients, cert['stable_kernel_steps'], A, T)
    if w_kernel.cols != 10:
        raise ArithmeticError('Unexpected stable-kernel dimension')
    q = pure.flat3(projection, 28)
    parameters, checks = sp.SparseMatrix.eye(28), []
    for record in cert['square_rounds']:
        if parameters.cols != record['before']:
            raise ArithmeticError('Incorrect square-round starting dimension')
        matrix = canonical(q*parameters)
        cuts = sp.SparseMatrix.vstack(*(check_square(matrix, selected.rows, witness)
                                       for witness in record['witnesses']))
        kernel = linear.replay(cuts, record['kernel_steps'], A, T)
        if kernel.cols != record['after']:
            raise ArithmeticError('Incorrect square-round ending dimension')
        checks.extend((matrix, selected.rows, witness) for witness in record['witnesses'])
        parameters = canonical(parameters*kernel)
    if parameters.cols:
        raise ArithmeticError('The rank-one projection was not eliminated')
    return {'stable': stable, 'stable_coefficients': stable_coefficients,
            'w_kernel': w_kernel, 'projection': projection, 'square_checks': checks}



@lru_cache(None)
def report():
    initial, split = initial_data(), split_data()
    return {'claim': 'AI-MIXED-AXIS-REDUCTION-091', 'parameters': {'a': 'any complex number', 'b': 1, 't': 'any nonzero complex number'},
            'mixed_row': 'm+t*d0', 'normal_minor': 't**18', 'normal_dimension': 32, 'plane_dimension': 4,
            'quotient': encode(initial['quotient']), 'stable_kernel': encode(split['w_kernel']),
            'projection_dimensions': [[r['before'], r['after']] for r in certificate()['square_rounds']],
            'remaining_quotient_dimension': 10, 'target_excluded_on_this_axis': False,
            'all_graphs_classified': False, 'independent_review': False, 'improves_omega': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    value = json.dumps(report(), indent=2, default=int)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(value)
    else:
        print(value, end='')
