"""Standard-library acceptance of a literal-source dual and exact branches.

No constructor, tangent solver, shared contraction, or symbolic package is
imported. Coefficients are sparse rational Laurent polynomials in a,b,d.
"""
import argparse
import ast
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
import hashlib
from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PRESCRIBED = 'results/conic-third-jets-2026-10-23/mixed-family.json'
PRESCRIBED_SHA256 = '0571cd47916d19c60a0f9493a6ddccaecb8053aea8a139137c05b3def9df1d5e'
ZERO = (0, 0, 0)
ONE = {ZERO: Fraction(1)}
A = {(1, 0, 0): Fraction(1)}
B = {(0, 1, 0): Fraction(1)}
D = {(0, 0, 1): Fraction(1)}
FIRST = [28*i+7*j+z for i, j, z in product((1, 2), (1, 2), (0, 3, 6))]
OUTSIDE = [i for i in range(112) if i not in FIRST]


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            value = result.get(exponent, 0)+coefficient
            if value:
                result[exponent] = value
            else:
                result.pop(exponent, None)
    return result


def scale(polynomial, coefficient):
    return {e: q*coefficient for e, q in polynomial.items() if q*coefficient}


def multiply(left, right):
    result = {}
    for e, q in left.items():
        for f, r in right.items():
            exponent = tuple(x+y for x, y in zip(e, f))
            value = result.get(exponent, 0)+q*r
            if value:
                result[exponent] = value
            else:
                result.pop(exponent, None)
    if len(result) > 20000:
        raise ValueError('coefficient expansion exceeds the acceptance bound')
    return result


def inverse_monomial(polynomial):
    if len(polynomial) != 1:
        raise ValueError('division must be by a rational constant times a power of d')
    (exponent, coefficient), = polynomial.items()
    if exponent[:2] != (0, 0):
        raise ValueError('parameter denominator outside the d chart')
    return {(0, 0, -exponent[2]): 1/coefficient}


def power(polynomial, exponent):
    if abs(exponent) > 128:
        raise ValueError('coefficient power exceeds the acceptance bound')
    if exponent < 0:
        return power(inverse_monomial(polynomial), -exponent)
    result = ONE
    while exponent:
        if exponent % 2:
            result = multiply(result, polynomial)
        exponent //= 2
        if exponent:
            polynomial = multiply(polynomial, polynomial)
    return result


@lru_cache(maxsize=4096)
def expression(text, pole=2):
    if not isinstance(text, str) or len(text) > 20000:
        raise ValueError('invalid coefficient expression')
    tree = ast.parse(text, mode='eval')
    if sum(1 for _ in ast.walk(tree)) > 4000:
        raise ValueError('coefficient syntax exceeds the acceptance bound')

    def read(node):
        if isinstance(node, ast.Constant) and type(node.value) is int:
            return {ZERO: Fraction(node.value)} if node.value else {}
        if isinstance(node, ast.Name) and node.id in ('a', 'b', 'd'):
            return {'a': A, 'b': B, 'd': D}[node.id]
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            return scale(read(node.operand), -1 if isinstance(node.op, ast.USub) else 1)
        if isinstance(node, ast.BinOp):
            left, right = read(node.left), read(node.right)
            if isinstance(node.op, ast.Add):
                return add(left, right)
            if isinstance(node.op, ast.Sub):
                return add(left, scale(right, -1))
            if isinstance(node.op, ast.Mult):
                return multiply(left, right)
            if isinstance(node.op, ast.Div):
                return multiply(left, inverse_monomial(right))
            if isinstance(node.op, ast.Pow):
                exponent = right.get(ZERO, Fraction(0))
                if set(right)-{ZERO} or exponent.denominator != 1:
                    raise ValueError('power must be an integer')
                return power(left, int(exponent))
        raise ValueError('only rational Laurent arithmetic is permitted')

    result = read(tree.body)
    if any(e[0] < 0 or e[1] < 0 or e[2] < -pole for e in result):
        raise ValueError('coefficient has an unpermitted parameter pole')
    return result


def decode(record, shape, pole=2):
    if record.get('shape') != list(shape):
        raise ValueError('wrong matrix shape')
    result = {}
    seen = set()
    for i, j, text in record['entries']:
        if (type(i) is not int or type(j) is not int or (i, j) in seen
                or not 0 <= i < shape[0] or not 0 <= j < shape[1]):
            raise ValueError('invalid or repeated matrix coordinate')
        seen.add((i, j))
        value = expression(text, pole)
        if value:
            result[i, j] = value
    return result


def source_terms():
    return [(28*i+7*v+6-p-q, 28*p+7*j+6-r-v, 28*r+7*q+6-i-j)
            for i, j, p, q, r, v in product(range(4), repeat=6)]


def matrix_add(*matrices):
    result = {}
    for matrix in matrices:
        for position, polynomial in matrix.items():
            value = add(result.get(position, {}), polynomial)
            if value:
                result[position] = value
            else:
                result.pop(position, None)
    return result


def matrix_negative(matrix):
    return {p: scale(q, -1) for p, q in matrix.items()}


def contract(left, right, terms):
    byleft, byright = defaultdict(list), defaultdict(list)
    for (row, column), value in left.items():
        byleft[column].append((row, value))
    for (row, column), value in right.items():
        byright[column].append((row, value))
    result, products = {}, {}
    for source, b, c in terms:
        for br, x in byleft[b]:
            for cr, y in byright[c]:
                key = (id(x), id(y))
                if key not in products:
                    products[key] = multiply(x, y)
                position = source, 14*br+cr
                value = add(result.get(position, {}), products[key])
                if value:
                    result[position] = value
                else:
                    result.pop(position, None)
    return result


def select_rows(matrix, rows):
    positions = {row: i for i, row in enumerate(rows)}
    return {(positions[i], j): value for (i, j), value in matrix.items() if i in positions}


def matrix_product(left, right):
    byrow = defaultdict(list)
    for (i, j), value in right.items():
        byrow[i].append((j, value))
    result = {}
    for (i, k), x in left.items():
        for j, y in byrow[k]:
            value = add(result.get((i, j), {}), multiply(x, y))
            if value:
                result[i, j] = value
            else:
                result.pop((i, j), None)
    return result


def unit_minor(matrix, columns):
    size = len(columns)
    entries = [[matrix.get((i, j), {}) for j in columns] for i in range(size)]
    determinant = Fraction(1)
    for k in range(size):
        pivot = next(((i, j) for i in range(k, size) for j in range(k, size)
                      if set(entries[i][j]) == {ZERO}), None)
        if pivot is None:
            raise ValueError('leading minor has no rational unit pivot')
        i, j = pivot
        if i != k:
            entries[i], entries[k] = entries[k], entries[i]
            determinant = -determinant
        if j != k:
            for row in entries:
                row[j], row[k] = row[k], row[j]
            determinant = -determinant
        value = entries[k][k][ZERO]
        determinant *= value
        for i in range(k+1, size):
            factor = scale(entries[i][k], 1/value)
            for j in range(k+1, size):
                entries[i][j] = add(entries[i][j], scale(multiply(factor, entries[k][j]), -1))
            entries[i][k] = {}
    return determinant


def specialize_component(polynomial, component):
    result = {}
    for (a, b, d), value in polynomial.items():
        if component == 'a=-d^3':
            exponent, coefficient = (0, b, d+3*a), value*(-1)**a
        elif component == 'b=d^3':
            exponent, coefficient = (a, 0, d+3*b), value
        else:
            raise ValueError('unknown exceptional component')
        result = add(result, {exponent: coefficient})
    return result


def specialize_matrix(matrix, component):
    result = {position: specialize_component(value, component) for position, value in matrix.items()}
    return {position: value for position, value in result.items() if value}


def functional(weights, matrix, source_positions=None):
    result = {}
    for (source, br, cr), coefficient in weights.items():
        row = source if source_positions is None else source_positions[source]
        result = add(result, multiply(coefficient, matrix.get((row, 14*br+cr), {})))
    return result


def check_adjoint(weights, b0, c0, w0, terms):
    bysource = defaultdict(list)
    for (source, br, cr), value in weights.items():
        bysource[source].append((br, cr, value))
    badjoint, cadjoint = {}, {}
    for source, b, c in terms:
        for br, cr, value in bysource[source]:
            badjoint[br, b] = add(badjoint.get((br, b), {}), multiply(value, c0.get((cr, c), {})))
            cadjoint[cr, c] = add(cadjoint.get((cr, c), {}), multiply(value, b0.get((br, b), {})))
    if any(badjoint.values()) or any(cadjoint.values()):
        raise ValueError('functional does not annihilate every fourth map coefficient')
    for source in OUTSIDE:
        for k in range(12):
            value = add(*(multiply(coefficient, w0.get((k, 14*br+cr), {}))
                          for br, cr, coefficient in bysource[source]))
            if value:
                raise ValueError('functional does not annihilate every fourth kernel coefficient')


def check_linear_branch(branch, bs, cs, ys, terms):
    component = branch['component']
    if branch.get('kernel') != 'fixed' or branch.get('complete_map_degrees') != [1, 1]:
        raise ValueError('wrong exact linear branch degrees or kernel')
    maps = [[decode(row, (14, 112)) for row in branch[side]] for side in ('B', 'C')]
    if any(len(side) != 2 for side in maps):
        raise ValueError('exact branch must contain both complete linear maps')
    for exported, original in zip(maps, (bs, cs)):
        for k in range(2):
            if exported[k] != specialize_matrix(original[k], component):
                raise ValueError('changed prescribed linear branch coefficient')
        for k in (2, 3):
            if specialize_matrix(original[k], component):
                raise ValueError('prescribed higher coefficient does not vanish on the branch')
    if any(specialize_matrix(y, component) for y in ys):
        raise ValueError('prescribed kernel correction does not vanish on the branch')
    bmap, cmap = maps
    for k in range(3):
        value = matrix_add(*(contract(bmap[i], cmap[k-i], terms)
                             for i in range(2) if 0 <= k-i < 2))
        if select_rows(value, OUTSIDE):
            raise ValueError('nonzero exact linear branch source coefficient')


def rational_control(bs, cs, ys, weights, terms):
    """Separate Fraction-only complete contraction at (a,b,d)=(1,2,1)."""
    def evaluate(polynomial):
        return sum((value*2**exponent[1] for exponent, value in polynomial.items()), Fraction(0))
    left = [{p: evaluate(q) for p, q in matrix.items()} for matrix in bs]
    right = [{p: evaluate(q) for p, q in matrix.items()} for matrix in cs]
    kernels = [{p: evaluate(q) for p, q in matrix.items()} for matrix in ys]
    rational_weights = {p: evaluate(q) for p, q in weights.items()}

    def full_contract(bmap, cmap):
        result = defaultdict(Fraction)
        for source, b, c in terms:
            for br in range(14):
                x = bmap.get((br, b), Fraction(0))
                if x:
                    for cr in range(14):
                        y = cmap.get((cr, c), Fraction(0))
                        if y:
                            result[source, 14*br+cr] += x*y
        return result

    w0 = full_contract(left[0], right[0])
    w1 = full_contract(left[0], right[1])
    for position, value in full_contract(left[1], right[0]).items():
        w1[position] += value
    left.append({(1, 61): Fraction(3), (5, 51): Fraction(-2)})
    right.append({(7, 19): Fraction(5), (3, 93): Fraction(7)})
    y4 = {(35, 0): Fraction(11), (38, 5): Fraction(-13)}
    known = defaultdict(Fraction)
    for i in (1, 2, 3):
        for position, value in full_contract(left[i], right[4-i]).items():
            known[position] += value
    for (source_row, k), value in kernels[2].items():
        for output in range(196):
            known[OUTSIDE[source_row], output] -= value*w1.get((FIRST[k], output), 0)
    before = sum(value*known[source, 14*br+cr]
                 for (source, br, cr), value in rational_weights.items())
    for i, j in ((0, 4), (4, 0)):
        for position, value in full_contract(left[i], right[j]).items():
            known[position] += value
    for (source_row, k), value in y4.items():
        for output in range(196):
            known[OUTSIDE[source_row], output] -= value*w0.get((FIRST[k], output), 0)
    after = sum(value*known[source, 14*br+cr]
                for (source, br, cr), value in rational_weights.items())
    if before != Fraction(-16, 3) or after != before:
        raise ValueError('rational literal-source obstruction control failed')
    return {'parameters': {'a': '1', 'b': '2', 'd': '1'},
            'zero_fourth_coefficients': str(before),
            'nonzero_fourth_coefficients': str(after),
            'source_terms_per_product': len(terms)}


def verify(record):
    if (record.get('schema') != 'conic-prescribed-third-obstruction-v1'
            or record.get('claim_id') != 'AI-CONIC-FIXED-THIRD-OBSTRUCTION-001'):
        raise ValueError('wrong obstruction schema')
    if record.get('chart') != 'd!=0; c=-d^3':
        raise ValueError('wrong prescribed d chart')
    if record.get('coefficient_ring') != 'Q[a,b,d,d^-1]':
        raise ValueError('wrong coefficient ring')
    if record.get('extension_criterion') != '(a+d^3)*(b-d^3)=0':
        raise ValueError('wrong claimed extension criterion')
    if (record.get('prescribed_source') != PRESCRIBED
            or record.get('prescribed_sha256') != PRESCRIBED_SHA256):
        raise ValueError('wrong prescribed source pin')
    payload = (ROOT / PRESCRIBED).read_bytes()
    if hashlib.sha256(payload).hexdigest() != PRESCRIBED_SHA256:
        raise ValueError('prescribed third-jet source bytes changed')
    prescribed = json.loads(payload)
    bs, cs = [[decode(row, (14, 112)) for row in prescribed[side]] for side in ('B', 'C')]
    ys = [decode(row, (100, 12)) for row in prescribed['source_row_corrections']]
    if len(bs) != 4 or len(cs) != 4 or len(ys) != 3 or ys[0] or ys[1]:
        raise ValueError('wrong complete prescribed third jet')
    weights = {}
    for source, br, cr, text in record['functional']:
        if (any(type(j) is not int for j in (source, br, cr))
                or source not in OUTSIDE or not 0 <= br < 14 or not 0 <= cr < 14
                or (source, br, cr) in weights):
            raise ValueError('invalid or repeated functional coordinate')
        value = expression(text, 0)
        if not value:
            raise ValueError('zero exported functional coefficient')
        weights[source, br, cr] = value
    expected = expression('-d*(a+d**3)**4*(b-d**3)**3/3', 0)
    if expression(record['fourth_residual'], 0) != expected:
        raise ValueError('changed claimed fourth obstruction polynomial')
    terms = source_terms()
    fs = [matrix_add(*(contract(bs[i], cs[k-i], terms) for i in range(k+1)))
          for k in range(4)]
    if select_rows(fs[0], OUTSIDE):
        raise ValueError('nonzero prescribed constant kernel coefficient')
    for k in range(1, 4):
        residual = matrix_add(select_rows(fs[k], OUTSIDE), matrix_negative(matrix_add(*(
            matrix_product(ys[i-1], select_rows(fs[k-i], FIRST)) for i in range(1, k+1)))))
        if residual:
            raise ValueError('prescribed third jet fails literal source incidence')
    w0 = select_rows(fs[0], FIRST)
    rb = [28*p+7*j+z for p, j, z in product((0, 3), (0, 3), (1, 2, 4, 5))]
    rc = [28*j+7*p+z for p, j, z in product((0, 3), (0, 3), (1, 2, 4, 5))]
    determinants = [unit_minor(bs[0], rb[2:]), unit_minor(cs[0], rc[2:]),
                    unit_minor(w0, prescribed['output_pivot_columns'])]
    if determinants != [1, 1, -1]:
        raise ValueError('changed prescribed unit minors')
    check_adjoint(weights, bs[0], cs[0], w0, terms)
    pieces = [functional(weights, contract(bs[i], cs[4-i], terms)) for i in (1, 2, 3)]
    moving = functional(weights, matrix_product(ys[2], select_rows(fs[1], FIRST)),
                        {source: i for i, source in enumerate(OUTSIDE)})
    if pieces != [{}, expected, {}] or moving:
        raise ValueError('wrong literal fourth-order obstruction evaluation')
    branches = record['linear_branches']
    if [branch['component'] for branch in branches] != ['a=-d^3', 'b=d^3']:
        raise ValueError('both exceptional components must be supplied')
    for branch in branches:
        check_linear_branch(branch, bs, cs, ys, terms)
    control = rational_control(bs, cs, ys, weights, terms)
    return {
        'claim_id': record['claim_id'], 'source_terms': len(terms),
        'scope': 'Every complex a,b,d with d!=0 and c=-d^3; the full prescribed PR107 third jet',
        'prescribed_map_orders_fixed': [0, 1, 2, 3],
        'prescribed_kernel_orders_fixed': [1, 2, 3],
        'prescribed_kernel_entry_counts': [len(y) for y in ys],
        'prescribed_source_kernel_orders_replayed': [0, 1, 2, 3],
        'functional_nonzero_entries': len(weights),
        'arbitrary_fourth_map_coefficients_annihilated': 3136,
        'arbitrary_fourth_kernel_coefficients_annihilated': 1200,
        'fourth_residual': '-d*(a+d^3)^4*(b-d^3)^3/3',
        'known_fourth_term_values': ['0', '-d*(a+d^3)^4*(b-d^3)^3/3', '0'],
        'moving_kernel_term_value': '0',
        'necessary_and_sufficient_extension_condition': '(a+d^3)*(b-d^3)=0',
        'exceptional_exact_linear_components': ['a=-d^3', 'b=d^3'],
        'complete_linear_source_orders_per_component': [0, 1, 2],
        'leading_minor_determinants': list(map(str, determinants)),
        'rational_literal_source_control': control,
        'formal_or_polynomial_extension_off_components': False,
        'independent_mathematical_review': False,
        'matrix_target_constructed': False, 'exponent_improvement': False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('witness', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = verify(json.loads(args.witness.read_text()))
    if args.output:
        args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
