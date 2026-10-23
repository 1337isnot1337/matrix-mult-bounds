"""Replay all missing projective strata and every saved polynomial source map.

The curve constructor is not imported.  Curves are checked against all 4096
literal source terms.  Complete tangent and curvature operators are rebuilt
from the byte-pinned preceding source model in the new unit row frames.
"""
import argparse
import ast
from functools import lru_cache
import gzip
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import time

import sympy as s

PACKAGE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('projective_acceptance_model', PACKAGE/'model.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
ROOT = m.ROOT
RESULTS = ROOT/'results/conic-projective-criterion-2026-10-23'
a, b, c, d = m.a, m.b, m.c, m.d
FIRST = [m.index(i, j, z) for i, j, z in product((1, 2), (1, 2), (0, 3, 6))]
OUTSIDE = [i for i in range(112) if i not in FIRST]
CRITERION = '(a1*r-a0*s)*(b1*r+b0*s)*(s*lambda**3+r*mu**3)=0'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def expression(text):
    """A polynomial-only bounded parser; no evaluation of certificate strings."""
    require(isinstance(text, str) and len(text) < 20000, 'Polynomial expression text')
    tree = ast.parse(text, mode='eval')
    require(sum(1 for _ in ast.walk(tree)) < 4000, 'Polynomial expression size')
    def walk(node):
        if isinstance(node, ast.Constant) and type(node.value) is int:
            require(abs(node.value) < 10**12, 'Polynomial integer bound')
            return s.Integer(node.value)
        if isinstance(node, ast.Name) and node.id in ('a', 'b', 'c', 'd'):
            return m.SYMBOLS[node.id]
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            z = walk(node.operand)
            return z if isinstance(node.op, ast.UAdd) else -z
        if isinstance(node, ast.BinOp):
            left, right = walk(node.left), walk(node.right)
            if isinstance(node.op, ast.Add):
                return left+right
            if isinstance(node.op, ast.Sub):
                return left-right
            if isinstance(node.op, ast.Mult):
                return left*right
            if isinstance(node.op, ast.Div):
                require(bool(right.is_Rational and right), 'Only nonzero rational denominators')
                return left/right
            if isinstance(node.op, ast.Pow):
                require(bool(right.is_Integer and 0 <= right <= 20), 'Polynomial exponent bound')
                return left**right
        raise ValueError('Unsupported polynomial expression')
    result = s.expand(walk(tree.body))
    s.Poly(result, a, b, c, d)
    return result


def decode(record):
    require(record.get('shape') == [14, 112], 'Complete fourteen-by-112 map required')
    entries = {}
    for row, col, text in record['entries']:
        require(type(row) is int and type(col) is int and 0 <= row < 14 and 0 <= col < 112,
                'Map coordinate bounds')
        require((row, col) not in entries, 'Repeated map coordinate')
        value = expression(text)
        require(value != 0, 'Explicit zero map entry')
        entries[row, col] = value
    return s.MutableSparseMatrix(14, 112, entries)


def read(name):
    return json.loads(gzip.decompress((RESULTS/(name+'.json.gz')).read_bytes()))


def write(name, record):
    payload = (json.dumps(record, sort_keys=True, separators=(',', ':'))+'\n').encode()
    (RESULTS/(name+'.json.gz')).write_bytes(gzip.compress(payload, mtime=0))


@lru_cache(None)
def source_terms():
    return tuple((m.index(i, z, 6-p-q), m.index(p, j, 6-r-z), m.index(r, q, 6-i-j))
                 for i, j, p, q, r, z in product(range(4), repeat=6))


def contract(B, C):
    """Separate literal loop, independent of the constructor and prior contraction."""
    by_b, by_c = {}, {}
    for (row, col), value in B.todok().items():
        by_b.setdefault(col, []).append((row, value))
    for (row, col), value in C.todok().items():
        by_c.setdefault(col, []).append((row, value))
    entries = {}
    for source, left, right in source_terms():
        for br, bv in by_b.get(left, ()):
            for cr, cv in by_c.get(right, ()):
                key = source, C.rows*br+cr
                entries[key] = entries.get(key, 0)+bv*cv
    return m.expand(s.MutableSparseMatrix(112, B.rows*C.rows, entries))


@lru_cache(None)
def output_columns():
    G = s.zeros(4, 112)
    for row, z in enumerate(m.LONG):
        G[row, m.index(0, 3, z)] = 1
        G[row, m.index(3, 0, z)] = -1
    pivots = contract(G, G)[FIRST, :].to_DM().rref()[1]
    require(len(pivots) == 12, 'Fixed G output rank')
    return [14*(j//4)+j % 4 for j in pivots]


def source_pins():
    records = json.loads((PACKAGE/'sources.json').read_text())
    count = 0
    for source in records['local']:
        for path, digest in source['sha256'].items():
            require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest,
                    'Credited source byte pin: '+path)
            count += 1
    return count


def compatibility(previous, data, curvature):
    op = previous.m
    matrices = {k: op.decode(curvature[k-1]['cohomology']) for k in (1, 2)}
    mixed = s.Matrix.vstack(*[
        op.expand(d*matrices[k][:, :68]+matrices[k][:, 68:136]).row_join(
            matrices[k][:, 136:137]*(1 if k == 2 else d*d)) for k in (2, 1)])
    rows, active, operations = op.unit_eliminate(mixed, 68, laurent=True)
    require(not any(j < 68 for i in active for j in rows[i]),
            'Complete mixed elimination must retain no velocity coefficient')
    target = data['delta']*(c+d**3)
    residuals = [s.expand(rows[i][68]) for i in active if rows[i].get(68, 0)]
    quotients = [s.cancel(z/target) for z in residuals]
    for quotient in quotients:
        numerator, denominator = quotient.as_numer_denom()
        s.Poly(numerator, a, b, c, d)
        coefficient, power = denominator.as_coeff_exponent(d)
        require(bool(coefficient.is_Rational and coefficient and power.is_Integer),
                'Mixed residual division must introduce only Laurent d units')
    units = [i for i, z in enumerate(quotients)
             if z.as_coeff_exponent(d)[0].is_Rational and z.as_coeff_exponent(d)[0]
             and z.as_coeff_exponent(d)[1].is_Integer]
    require(bool(units), 'Reverse ideal containment needs a Laurent unit')
    pure = {}
    for k in (1, 2):
        matrix = matrices[k]
        own = matrix[:, :68] if k == 1 else matrix[:, 68:136]
        require(not own.todok(), 'Pure class own boundary velocity block')
        generator = data['delta']*(1 if k == 1 else c)
        rhs = [z for z in matrix[:, 136] if z]
        quot = [s.cancel(z/generator) for z in rhs]
        require(all(z.is_polynomial(a, b, c) for z in quot), 'Pure residual containment')
        unit = next((i for i, z in enumerate(quot) if z.is_Rational and z), None)
        require(unit is not None, 'Pure residual reverse containment')
        pure[str(k)] = {'own_velocity_block_zero': True,
                        'residual_generator': str(s.expand(generator)),
                        'quotients': [str(z) for z in quot], 'reverse_unit_index': unit}
    return {'mixed_matrix': op.encode(mixed), 'mixed_guard': 'd != 0',
            'unit_operations': operations, 'unit_pivot_count': len(operations),
            'residual_generator': str(s.expand(target)),
            'residuals': [str(z) for z in residuals],
            'quotients': [str(z) for z in quotients], 'reverse_unit_index': units[0],
            'pure': pure}


def rebuild_certificates():
    records = []
    for stratum in m.STRATA[1:]:
        previous, data = m.complete_operator(stratum)
        tangents = [previous.tangent(k) for k in (0, 1, 2)]
        curvature = [previous.curvature(k) for k in (1, 2)]
        combined = compatibility(previous, data, curvature)
        records.append({'stratum': stratum, 'tangents': tangents,
                        'curvature': curvature, 'compatibility': combined})
        print('Rebuilt complete tangent and curvature:', stratum, flush=True)
    return {'schema': 'conic-projective-unit-certificates-v1', 'strata': records}


def check_affine_transition():
    previous = m.load('research/ai/2026-10-21-conic-second-jets/verify.py',
                      'projective_affine_credit')
    old = previous.m.base()
    old_normal = previous.normals()
    data = m.base('finite')
    determinants = []
    for side, index_side in (('B', 0), ('C', 1)):
        cols = data['raw_'+side][2:]
        change = m.expand(data[side][:, cols]*old[index_side][:, cols].inv())
        determinant = s.factor(change.det())
        require(determinant in (-1, 1), 'Affine basis transition must be a unit')
        require(not m.expand(change*old[index_side]-data[side]).todok(),
                'Exact affine leading frame transition')
        for k in (1, 2):
            require(not m.expand(change*old_normal[k][index_side]-m.normals(data, k)[index_side]).todok(),
                    'Exact affine normal transition')
        determinants.append(str(determinant))
    return {'row_change_determinants': determinants, 'normal_classes_identical': True}


def check_reversal():
    def reverse_coordinate(col):
        i, rem = divmod(col, 28)
        j, z = divmod(rem, 7)
        return m.index(3-i, 3-j, 6-z)
    require({tuple(reverse_coordinate(z) for z in term) for term in source_terms()}
            == set(source_terms()), 'Full literal source reversal')
    require({reverse_coordinate(z) for z in FIRST} == set(FIRST), 'Leading source chart reversal')
    records = []
    for stratum in m.STRATA:
        old = m.base(stratum)
        new = m.homogeneous_base(c, 1, old['a1'], old['a0'], old['b1'], old['b0'])
        require(s.expand(new['delta']+old['delta']) == 0, 'Homogeneous discriminant reversal')
        determinants = []
        for side, index_side in (('B', 0), ('C', 1)):
            reversed_base = m.reverse_map(old[side])
            cols = new['raw_'+side][2:]
            change = m.expand(new[side][:, cols]*reversed_base[:, cols].inv())
            determinant = s.factor(change.det())
            require(determinant in (-1, 1), 'Reversal row transition must be a constant unit')
            require(not m.expand(change*reversed_base-new[side]).todok(),
                    'Reversal complete leading map')
            for k in (1, 2):
                residual = change*m.reverse_map(m.normals(old, k)[index_side])+m.normals(new, 3-k)[index_side]
                require(not m.expand(residual).todok(), 'Reversal swaps both normal classes with one common sign')
            determinants.append(str(determinant))
        records.append({'stratum': stratum, 'row_change_determinants': determinants})
    return {'source_terms_permuted': 4096, 'projective_normal_transition': '[lambda:mu] -> [mu:lambda]',
            'strata': records}


def check_curve(record):
    stratum = record.get('stratum')
    require(stratum in m.STRATA, 'Curve projective stratum')
    kind = record.get('kind')
    require(kind in ('finite_mixed', 'conic_infinity'), 'Curve kind')
    data = m.base(stratum, 'finite' if kind == 'finite_mixed' else 'infinity')
    substitution = {c: -d**3} if kind == 'finite_mixed' else {}
    require(record.get('normal_class') == (['1', 'd'] if kind == 'finite_mixed' else ['0', '1']),
            'Prescribed projective normal class')
    bs, cs = [[decode(matrix) for matrix in record[side]] for side in ('B', 'C')]
    expected_c_count = 2 if kind == 'conic_infinity' and stratum != 'finite' else 3
    require(len(bs) == 2 and len(cs) == expected_c_count,
            'Complete polynomial degree bounds')
    require(bool(bs[-1].todok()) and bool(cs[-1].todok()), 'Last map coefficient is nonzero')
    for side, maps in (('B', bs), ('C', cs)):
        require(maps[0] == data[side].subs(substitution), 'Complete leading map')
    first_normal = [m.normals(data, 1)[k] if kind == 'conic_infinity' else
                    m.normals(data, 2)[k]+d*m.normals(data, 1)[k] for k in (0, 1)]
    for side, maps, normal in zip(('B', 'C'), (bs, cs), first_normal):
        residual = m.expand(maps[1]-normal.subs(substitution))
        require(all(col in data['raw_'+side] for row, col in residual.todok()),
                'First coefficient has the required normal class modulo boundary motion')
    determinants = [s.factor(bs[0][:, data['raw_B'][2:]].det()),
                    s.factor(cs[0][:, data['raw_C'][2:]].det())]
    require(all(z in (-1, 1) for z in determinants), 'Leading fourteen-row unit minors')
    degree = len(bs)+len(cs)-2
    counts = []
    leading = None
    for order in range(degree+1):
        coefficient = s.zeros(112, 196)
        for i in range(len(bs)):
            j = order-i
            if 0 <= j < len(cs):
                coefficient += contract(bs[i], cs[j])
        coefficient = m.expand(coefficient)
        require(not coefficient[OUTSIDE, :].todok(), 'Complete polynomial source product has a kernel residual')
        counts.append(len(coefficient.todok()))
        if order == 0:
            leading = coefficient
    flat_minor = s.factor(leading[FIRST, output_columns()].det())
    require(flat_minor in (-1, 1), 'Leading rank-twelve unit minor')
    return {'kind': kind, 'stratum': stratum, 'degrees': [len(bs)-1, len(cs)-1],
            'checked_product_orders': list(range(degree+1)),
            'allowed_output_entry_counts': counts,
            'leading_minor_determinants': [str(z) for z in determinants]+[str(flat_minor)],
            'normal_class': record['normal_class'], 'fixed_kernel': True}


def check_linear_components():
    """Both pure squares and their cross term vanish on every Delta=0 stratum."""
    branches = []
    for conic_chart in ('finite', 'infinity'):
        for stratum in m.STRATA:
            if conic_chart == 'infinity':
                substitutions = [] if stratum == 'finite' else [{}]
            else:
                substitutions = ({'finite': [{a: c}, {b: -c}],
                                  'a_infinity': [{b: -c}],
                                  'b_infinity': [{a: c}],
                                  'both_infinity': []}[stratum])
            data = m.base(stratum, conic_chart)
            for substitution in substitutions:
                require(s.expand(data['delta'].subs(substitution)) == 0, 'Linear component discriminant')
                B0, C0 = [data[key].subs(substitution) for key in ('B', 'C')]
                normal = {k: [matrix.subs(substitution) for matrix in m.normals(data, k)] for k in (1, 2)}
                require(not contract(B0, C0)[OUTSIDE, :].todok(), 'Linear component leading source')
                for k in (1, 2):
                    nb, nc = normal[k]
                    require(not m.expand(contract(nb, C0)+contract(B0, nc)).todok(),
                            'Linear component complete first source derivative')
                    require(not contract(nb, nc).todok(), 'Linear component pure quadratic product')
                require(not m.expand(contract(normal[1][0], normal[2][1])+
                                     contract(normal[2][0], normal[1][1])).todok(),
                        'Linear component mixed quadratic product')
                branches.append({'conic_chart': conic_chart, 'stratum': stratum,
                                 'substitution': {str(key): str(value) for key, value in substitution.items()},
                                 'all_normal_classes': True, 'full_product_constant': True})
    return branches


def certificate_headers(certificates):
    require(certificates.get('schema') == 'conic-projective-unit-certificates-v1', 'Unit certificate schema')
    require([record.get('stratum') for record in certificates['strata']] == list(m.STRATA[1:]),
            'Complete curvature stratum cover')
    for record in certificates['strata']:
        delta = m.base(record['stratum'])['delta']
        require(s.expand(expression(record['compatibility']['residual_generator'])-delta*(c+d**3)) == 0,
                'Projective curvature residual generator')
        for k in (1, 2):
            pure = record['compatibility']['pure'][str(k)]
            require(s.expand(expression(pure['residual_generator'])-delta*(1 if k == 1 else c)) == 0,
                    'Projective pure residual generator')


def verify(curves=None, certificates=None, rebuild=True):
    pins = source_pins()
    curves = read('curves') if curves is None else curves
    certificates = read('certificates') if certificates is None else certificates
    require(curves.get('schema') == 'conic-projective-criterion-v1', 'Curve schema')
    require(curves.get('criterion') == CRITERION, 'Homogeneous extension criterion')
    require(curves.get('scope') == 'existence for a nonzero normal class; boundary first velocity is free',
            'Normal-class existence scope')
    certificate_headers(certificates)
    expected = [(kind, stratum) for kind in ('finite_mixed', 'conic_infinity') for stratum in m.STRATA]
    require([(record.get('kind'), record.get('stratum')) for record in curves['families']] == expected,
            'Complete projective curve stratum cover')
    if rebuild:
        require(rebuild_certificates() == certificates, 'Exact complete unit certificate replay')
    summaries = []
    for record in certificates['strata']:
        require(record['stratum'] in m.STRATA[1:], 'Missing-stratum certificate name')
        summaries.append({'stratum': record['stratum'],
            'tangent_dimensions': [len(row['free_coordinates']) for row in record['tangents']],
            'tangent_basis_determinants': [row['basis_transform_determinant'] for row in record['tangents']],
            'mixed_unit_pivots': record['compatibility']['unit_pivot_count'],
            'mixed_residual_generator': record['compatibility']['residual_generator']})
    require([row['stratum'] for row in summaries] == list(m.STRATA[1:]), 'Complete curvature stratum cover')
    require(all(row['tangent_dimensions'] == [64, 3, 3] and row['mixed_unit_pivots'] == 49 for row in summaries),
            'Complete projective tangent and mixed curvature ranks')
    return {'verified': True, 'claim_id': curves['claim_id'], 'criterion': CRITERION,
            'source_byte_pins': pins, 'source_terms': len(source_terms()),
            'missing_strata': summaries, 'affine_transition': check_affine_transition(),
            'reversal': check_reversal(), 'curves': [check_curve(record) for record in curves['families']],
            'exact_linear_components': check_linear_components(),
            'all_projective_base_points': True, 'boundary_velocity_free': True,
            'prescribed_full_first_jet_claimed': False, 'target_tensor_constructed': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-certificates', action='store_true')
    parser.add_argument('--write-report', action='store_true')
    args = parser.parse_args()
    started = time.perf_counter()
    if args.write_certificates:
        source_pins()
        write('certificates', rebuild_certificates())
    report = verify(rebuild=not args.write_certificates)
    if args.write_report:
        (RESULTS/'verification.json').write_text(json.dumps(report, indent=2)+'\n')
    else:
        require(report == json.loads((RESULTS/'verification.json').read_text()), 'Saved verification report')
    print(json.dumps({'verified': True, 'all_projective_base_points': True,
                      'seconds': time.perf_counter()-started}, indent=2))


if __name__ == '__main__':
    main()
