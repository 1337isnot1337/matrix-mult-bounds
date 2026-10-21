"""Reconstruct the selected cubic curve by exact correction solves."""
import argparse
from collections import defaultdict
import importlib.util
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('five_frame_quadratic', HERE.parent / '2026-10-21-invertible-line-lifts/quadratic.py')
quadratic = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(quadratic)
extension, normal = quadratic.extension, quadratic.normal
constructor = quadratic.normal_filter.constructor


def rows(vector):
    return [{j: vector[112*b+j] for j in range(112) if vector[112*b+j]} for b in range(8)]


def derivative(left, right, source):
    identity = [{i: 1} for i in range(112)]
    entries = defaultdict(int)
    for (x, column), value in extension.contract(identity, right, source).todok().items():
        u, c = divmod(column, 4)
        for b in range(4):
            entries[16*x+4*b+c, 112*b+u] += value
    for (x, column), value in extension.contract(left, identity, source).todok().items():
        b, u = divmod(column, 112)
        for c in range(4):
            entries[16*x+4*b+c, 448+112*c+u] += value
    return sp.MutableSparseMatrix(16*len(source), 896, dict(entries))


def construct():
    data = quadratic.data()
    first, cb, cc, _, top, annihilator = extension.matrices()
    recovery = sp.kronecker_product(sp.SparseMatrix.eye(100), normal.data()['recover'])
    projector = sp.kronecker_product(sp.SparseMatrix.eye(100), annihilator)
    operator = derivative(extension.G, extension.G, extension.OUTSIDE)
    source_operator = recovery*operator
    direction = data['directions'][:, 0]+data['directions'][:, 22]
    d = rows(direction)
    y1 = (source_operator*direction).reshape(100, 12)
    raw2 = extension.contract(d[:4], d[4:], extension.OUTSIDE)
    rhs = -data['forcing']*sp.Matrix(list(raw2))
    e2 = constructor.solver(data['system'])(rhs)
    freedom = normal.sparse_nullspace(data['system'])[0]
    cubic_operator = (derivative(d[:4], d[4:], extension.OUTSIDE)
                      - sp.kronecker_product(y1, sp.SparseMatrix.eye(16))
                      * derivative(extension.G, extension.G, extension.A0))
    offset = sp.Matrix(list(y1*extension.contract(d[:4], d[4:], extension.A0)))
    cokernel = normal.sparse_nullspace(top.T)[0].T
    obstruction_map = cokernel*projector*cubic_operator*freedom
    residual = cokernel*projector*(cubic_operator*e2-offset)
    if (freedom.cols != 264 or quadratic.third.matrix_rank(obstruction_map) != 13
            or not any(residual)):
        raise ArithmeticError('The selected cubic correction problem changed')
    e2 += freedom*constructor.solver(obstruction_map)(-residual)
    if data['system']*e2 != rhs:
        raise ArithmeticError('The cubic repair changed the earlier equations')
    second = rows(e2)
    y2 = (source_operator*e2+recovery*sp.Matrix(list(raw2))).reshape(100, 12)
    left, right = data['left'], data['right']
    cross_b = (extension.contract(left, second[4:], extension.OUTSIDE)
               - y2*extension.contract(left, extension.G, extension.A0))
    cross_c = (extension.contract(second[:4], right, extension.OUTSIDE)
               - y2*extension.contract(extension.G, right, extension.A0))
    b3 = constructor.solver(cb)(-sp.Matrix(list(cross_b)))
    c3 = constructor.solver(cc)(-sp.Matrix(list(cross_c)))
    raw3 = cubic_operator*e2-offset
    e3 = constructor.solver(top)(-projector*raw3)
    third = rows(e3)
    y3 = (source_operator*e3+recovery*raw3).reshape(100, 12)
    p = [extension.G+[{}], d[:4]+left, second[:4]+[{}],
         third[:4]+[{j: b3[j] for j in range(112) if b3[j]}]]
    q = [extension.G+[{}], d[4:]+right, second[4:]+[{}],
         third[4:]+[{j: c3[j] for j in range(112) if c3[j]}]]
    return {'P': [constructor.encode(x) for x in p], 'Q': [constructor.encode(x) for x in q],
            'source_corrections': [constructor.encode_correction(x) for x in (y1, y2, y3)],
            'order': 3, 'parameters': 1, 'first_direction_indices': [0, 22]}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(construct(), indent=2)+'\n')
