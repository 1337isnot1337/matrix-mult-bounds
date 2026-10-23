"""Independent symbolic replay of the exact d=0 conic-fiber curve."""
import argparse
import ast
import gzip
import importlib.util
import json
from itertools import product
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
DEFAULT = ROOT/'results/conic-d0-cubic-2026-10-23/exact-curve.json'
a, b, c, d = s.symbols('a b c d')
SYMBOLS = {'a': a, 'b': b, 'c': c, 'd': d}
SOURCE_SPEC = importlib.util.spec_from_file_location(
    'conic_d0_literal_source',
    ROOT/'research/ai/2026-10-23-conic-third-jets/verify.py')
SOURCE = importlib.util.module_from_spec(SOURCE_SPEC)
SOURCE_SPEC.loader.exec_module(SOURCE)


def expression(text, names=('a', 'b', 'c', 'd')):
    """Parse only integer/rational polynomial arithmetic in named variables."""
    allowed = {name: SYMBOLS[name] for name in names}

    def read(node):
        if isinstance(node, ast.Constant) and type(node.value) is int:
            return s.Integer(node.value)
        if isinstance(node, ast.Name) and node.id in allowed:
            return allowed[node.id]
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            value = read(node.operand)
            return -value if isinstance(node.op, ast.USub) else value
        if isinstance(node, ast.BinOp):
            left, right = read(node.left), read(node.right)
            if isinstance(node.op, ast.Add): return left + right
            if isinstance(node.op, ast.Sub): return left - right
            if isinstance(node.op, ast.Mult): return left * right
            if isinstance(node.op, ast.Div): return left / right
            if isinstance(node.op, ast.Pow) and right.is_Integer and 0 <= right <= 12:
                return left ** int(right)
        raise ValueError('coefficient is outside the permitted arithmetic grammar')

    value = s.cancel(read(ast.parse(text, mode='eval').body))
    s.Poly(value, *(allowed[name] for name in names), domain=s.QQ)
    return value


def decode(record, shape, names=('a', 'b')):
    if record['shape'] != list(shape):
        raise ValueError('wrong matrix shape')
    result = {}
    for i, j, text in record['entries']:
        if (type(i) is not int or type(j) is not int or (i, j) in result
                or not 0 <= i < shape[0] or not 0 <= j < shape[1]):
            raise ValueError('wrong sparse matrix coordinate')
        value = expression(text, names)
        if not value:
            raise ValueError('stored zero matrix entry')
        result[i, j] = value
    return result


def add(*matrices):
    result = {}
    for matrix in matrices:
        for index, value in matrix.items():
            result[index] = result.get(index, 0) + value
    return {index: s.cancel(value) for index, value in result.items() if s.cancel(value)}


def rows(matrix, selected):
    position = {old: new for new, old in enumerate(selected)}
    return {(position[i], j): value for (i, j), value in matrix.items() if i in position}


def multiply(left, right):
    byrow = {}
    for (i, j), value in right.items():
        byrow.setdefault(i, []).append((j, value))
    result = {}
    for (i, k), value in left.items():
        for j, coefficient in byrow.get(k, ()):
            result[i, j] = result.get((i, j), 0) + value * coefficient
    return {index: s.cancel(value) for index, value in result.items() if s.cancel(value)}


def contract(left, right, terms):
    byleft, byright = {}, {}
    for (i, j), value in left.items():
        byleft.setdefault(j, []).append((i, value))
    for (i, j), value in right.items():
        byright.setdefault(j, []).append((i, value))
    result = {}
    for first, second, third in terms:
        for i, x in byleft.get(second, ()):
            for j, y in byright.get(third, ()):
                key = first, 14 * i + j
                result[key] = result.get(key, 0) + x * y
    return {index: s.cancel(value) for index, value in result.items() if s.cancel(value)}


def minor(matrix, rows_, columns):
    block = s.Matrix(len(rows_), len(columns),
                     lambda i, j: matrix.get((rows_[i], columns[j]), 0))
    return s.factor(block.det(method='domain-ge'))


def verify(record):
    if (record.get('base') != 'c=-d^3, specialize d=0'
            or record.get('status') != 'explicit-candidate'):
        raise ValueError('unexpected discovery record')
    if len(record.get('second_field_weights', ())) != 70 or any(
            expression(z) != 0 for z in record['second_field_weights']):
        raise ValueError('the proposed exact curve does not retain the fixed second coefficient')
    bs, cs = [[decode(matrix, (14, 112)) for matrix in record[key]]
              for key in ('B', 'C')]
    if len(bs) != 4 or len(cs) != 4 or bs[3] or cs[2] or cs[3]:
        raise ValueError('the proposed maps are not the stated quadratic/linear pair')
    if any(bs[3].values()) or any(cs[2].values()) or any(cs[3].values()):
        raise ValueError('unexpected higher map coefficient')
    if len(record['source_row_corrections']) != 3 or any(
            decode(item, (100, 12)) for item in record['source_row_corrections']):
        raise ValueError('the exact curve should need no source-row correction')

    # Preserve the credited PR101 constant and first maps on c=d=0.
    old = json.loads(gzip.decompress((ROOT/'results/conic-second-jets-2026-10-21/'
                                     'witnesses.json.gz').read_bytes()))['cubic_component_two_jet']
    for key, maps in (('B', bs), ('C', cs)):
        for order in (0, 1, 2):
            credited = decode(old[key][order], (14, 112), names=('a', 'b', 'c', 'd'))
            credited = {index: s.cancel(value.subs({c: 0, d: 0}))
                        for index, value in credited.items()}
            credited = {index: value for index, value in credited.items() if value}
            if add(maps[order], {(i, j): -value for (i, j), value in credited.items()}):
                raise ValueError(f'changed credited {key}{order} coefficient')

    terms = SOURCE.source_terms()
    if len(terms) != 4096:
        raise ValueError('wrong literal source term count')
    first = [28 * i + 7 * j + z for i, j, z in product((1, 2), (1, 2), (0, 3, 6))]
    outside = [i for i in range(112) if i not in first]
    fs = [add(*(contract(bs[i], cs[k-i], terms)
                for i in range(3) if 0 <= k-i < 2)) for k in range(4)]
    if rows(fs[0], outside):
        raise ValueError('constant source coefficient is nonzero on the kernel')
    for order in range(1, 4):
        if rows(fs[order], outside):
            raise ValueError(f'nonzero source-kernel coefficient at order {order}')

    rb = [28 * p + 7 * j + z for p, j, z in product((0, 3), (0, 3), (1, 2, 4, 5))]
    rc = [28 * j + 7 * p + z for p, j, z in product((0, 3), (0, 3), (1, 2, 4, 5))]
    pivots = record['output_pivot_columns']
    if len(pivots) != 12 or len(set(pivots)) != 12 or any(
            type(j) is not int or not 0 <= j < 196 for j in pivots):
        raise ValueError('wrong first-source minor coordinates')
    determinants = [minor(bs[0], range(14), rb[2:]),
                    minor(cs[0], range(14), rc[2:]),
                    minor(rows(fs[0], first), range(12), pivots)]
    if any(not z.is_Rational or not z for z in determinants):
        raise ValueError('leading rank minor is not a nonzero rational unit')
    if [str(z) for z in determinants] != ['1', '1', '-1']:
        raise ValueError('unexpected leading-minor values')
    nonboundary = (sum(j // 28 in (1, 2) for _, j in bs[1])
                   + sum(j // 7 % 4 in (1, 2) for _, j in cs[1]))
    if not nonboundary:
        raise ValueError('the first motion does not leave the boundary planes')
    return {
        'field': 'Q(a,b)',
        'parameter_scope': 'all complex a,b at c=0,d=0',
        'source_terms': len(terms),
        'kernel_coefficients_checked': 4 * 100 * 196,
        'map_degrees': [2, 1],
        'positive_curve_coefficients_checked': 3,
        'leading_minor_determinants': list(map(str, determinants)),
        'first_nonboundary_entries': nonboundary,
        'source_row_correction': 'identically zero',
        'identity': 'T(B0+t*B1+t^2*B2, C0+t*C1) has zero 100-row kernel block for all t',
        'matrix_target_constructed': False,
        'all_order_source_curve': True,
        'exponent_improvement': False,
        'independent_mathematical_review': False,
        'lean_formalized': False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('witness', nargs='?', type=Path, default=DEFAULT)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = verify(json.loads(args.witness.read_text()))
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
