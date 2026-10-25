"""Integer polynomial certificates for a sharp odd-characteristic four-space."""
import hashlib
import importlib.util
import json
from pathlib import Path

import sympy as sp

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]


def check_pins():
    sources = json.loads((PACKAGE / 'sources.json').read_text())
    for item in sources['local_dependencies']:
        if hashlib.sha256((ROOT / item['path']).read_bytes()).hexdigest() != item['sha256']:
            raise ArithmeticError('source pin: ' + item['path'])
    return sources


def require_zero(expression, label):
    if sp.expand(expression) != 0:
        raise ArithmeticError(label)


def family(t, b, c, f):
    return sp.Matrix([[8*t, b, c], [0, 4*t, f], [0, 0, t]])


def literal_source(M):
    return sp.Matrix([
        [M[H-j, L-r] if 0 <= H-j < 3 and 0 <= L-r < 3 else 0
         for H in range(5) for r in range(3)]
        for j in range(3) for L in range(5)])


def kernel_vector(t, b, c, f):
    return sp.Matrix([0, 0, 0, 0, 0, t**3, 0, -4*t**3, -f*t*t,
                      8*t**3, (-b+8*f)*t*t, -c*t*t+f*f*t,
                      (8*b-32*f)*t*t, 2*b*f*t+8*c*t*t-12*f*f*t,
                      2*c*f*t-f**3])


def report():
    check_pins()
    t, b, c, f = sp.symbols('t b c f')
    M = family(t, b, c, f)
    if [M[2, 2], M[0, 1], M[0, 2], M[1, 2]] != [t, b, c, f]:
        raise ArithmeticError('four independent coefficient directions')
    require_zero(M.det()-32*t**3, 'coefficient determinant')
    R = literal_source(M)
    v = kernel_vector(t, b, c, f)
    if v[5] != t**3:
        raise ArithmeticError('nonzero polynomial kernel')
    for value in R*v:
        require_zero(value, 'polynomial source kernel')
    minor = R.minor_submatrix(11, 5)
    determinant = sp.factor(minor.det(method='domain-ge'))
    require_zero(determinant+2**18*t**14, 'uniform literal minor')
    require_zero(R.det(method='domain-ge'), 'literal source determinant')
    base = {t: 1, b: 0, c: 0, f: 0}
    certificate = minor.subs(base)
    if certificate.det(method='bareiss') != -2**18:
        raise ArithmeticError('basepoint minor')
    path = ROOT / 'research/ai/2026-10-25-quadratic-universal-three-plane/verify.py'
    spec = importlib.util.spec_from_file_location('pinned_universal_invariants', path)
    parent = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(parent)
    D, A2, T4, P12 = parent.integer_invariants(M)
    for actual, expected in zip((D, A2, T4, P12), (32*t**3, 16*t*t, 64*t**4, 0)):
        require_zero(actual-expected, 'integer invariant cross-check')
    return {
        'claim': 'AI-ODD-QUADRATIC-SHARP-FOUR-001',
        'scope': 'every field of characteristic different from two, including zero',
        'dimension': 4, 'coefficient_matrix': [[str(x) for x in row] for row in M.tolist()],
        'coefficient_determinant': str(D), 'integer_A2': str(A2),
        'integer_T4': str(T4), 'integer_P12': str(P12),
        'literal_source_determinant': 0, 'polynomial_right_kernel': [str(x) for x in v],
        'generic_minor': str(determinant), 'deleted_row_pair': [2, 1],
        'deleted_column_pair': [1, 2], 'basepoint': [1, 0, 0, 0],
        'base_minor_matrix': [[int(x) for x in row] for row in certificate.tolist()],
        'base_minor_determinant': -2**18,
        'source_rank_at_every_invertible_coefficient_point': 14,
        'upper_bound_from_pinned_written_proofs': 4, 'sharpness_supplied': True,
        'maximum_in_characteristic_two_from_separate_proof': 3,
        'independent_review': False, 'lean_formalized': False, 'improves_omega': False,
    }


if __name__ == '__main__':
    print(json.dumps(report(), indent=2))
