"""Exact algebra for the invertible-stratum bound; no family census."""
import hashlib
import importlib.util
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent


def require_zero(expression, label):
    if sp.cancel(expression) != 0:
        raise ArithmeticError(label)


def check_source_pins():
    sources = json.loads((PACKAGE / 'sources.json').read_text())
    for entry in sources['local_dependencies']:
        actual = hashlib.sha256((ROOT / entry['path']).read_bytes()).hexdigest()
        if actual != entry['sha256']:
            raise ArithmeticError('source pin: ' + entry['path'])
    return sources


def parent_tangent_checks():
    path = ROOT / 'research/ai/2026-10-24-quadratic-equality/verify.py'
    spec = importlib.util.spec_from_file_location('invertible_parent', path)
    parent = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(parent)
    # Replays the pinned full symbolic differential and quadratic identity,
    # including both block determinants; no new finite inputs are introduced.
    _, _, checked = parent.symbolic_checks()
    return {key: checked[key] for key in (
        'Schur_numerator_determinant', 'scaled_C_block_determinant')}


def scalar_checks():
    p, mu, rho, q, A, w, h = sp.symbols('p mu rho q A w h')
    norm = (1+rho)/(rho*mu)
    trace_Q, second_Q, det_Q = 2*mu, (1+rho)*mu**2, rho*mu**3
    alpha = 3*p/norm
    trace_C = p*trace_Q-3*alpha
    second_C = p*p*second_Q-2*alpha*p*trace_Q+3*alpha**2
    require_zero(trace_C-p*mu*(2-7*rho)/(1+rho), 'trace contradiction')
    require_zero(second_C.subs(rho, sp.Rational(2, 7))+p*p*mu*mu/21,
                 'second coefficient contradiction')
    require_zero((1/det_Q)/norm**3-rho**2/(1+rho)**3, 'norm ratio')
    if sp.Poly(2-7*rho, rho, modulus=7).as_expr() != 2:
        raise ArithmeticError('characteristic-seven trace')
    require_zero((A**3-4*q*A*p*p+8*p**4)/p**3
                 -((A/p)**3-4*q*(A/p)+8*p), 'monic integral relation')
    require_zero((w**3-4*q*w+8*p).subs(w, 2*h)-8*(h**3-q*h+p),
                 'integral linear form')
    return {
        'det_square_norm_cube_ratio': 'rho^2/(1+rho)^3',
        'trace_C': 'p*mu*(2-7*rho)/(1+rho)',
        'second_C_at_rho_2_over_7': '-p^2*mu^2/21',
        'characteristic_seven_trace_numerator': 2,
        'odd_characteristic_integral_linear_form': True,
    }


def determinant_coefficients(Q, p, q):
    """Literal determinant coefficients, independent of the invariant formula."""
    t = sp.Symbol('t')
    C = p*(Q-3/q*sp.eye(3))
    poly = sp.Poly((sp.eye(3)+t*C).det(), t)
    return poly.nth(1), poly.nth(2)


def matrix_checks():
    a, b, c, d, e, f, p, q = sp.symbols('a b c d e f p q')
    Q = sp.Matrix([[a, b, c], [b, d, e], [c, e, f]])
    actual_first, actual_second = determinant_coefficients(Q, p, q)
    second_Q = sp.trace(Q.adjugate())
    require_zero(actual_first-p*(sp.trace(Q)-9/q), 'literal first coefficient')
    require_zero(actual_second-p*p*(second_Q-6*sp.trace(Q)/q+27/q**2),
                 'literal second coefficient')
    values = sp.symbols('n0:9')
    N = sp.Matrix(3, 3, values)
    determinant = N.det()
    adj_transpose = N.adjugate().T
    for index, value in enumerate(values):
        require_zero(sp.diff(determinant, value)-adj_transpose[index],
                     'determinant gradient')
    return {'general_symmetric_Q_determinant_coefficients': True,
            'nine_symbolic_determinant_gradient_entries': True}


def modular_trace_only_control(prime):
    # These controls exercise the two misleading trace-only candidates.
    if prime not in (5, 151):
        raise ValueError('retained boundary primes are 5 and 151')
    rho = (2*pow(7, -1, prime)) % prime
    return {
        'prime': prime, 'rho': rho,
        'critical_ratio_polynomial': ((rho-1)*(rho*rho+3)) % prime,
        'trace_numerator': (2-7*rho) % prime,
        'second_coefficient_at_p_mu_one': -pow(21, -1, prime) % prime,
    }


def report():
    check_source_pins()
    controls = [modular_trace_only_control(prime) for prime in (5, 151)]
    if any(row['critical_ratio_polynomial'] or row['trace_numerator']
           or not row['second_coefficient_at_p_mu_one'] for row in controls):
        raise ArithmeticError('trace-only boundary control')
    return {
        'claim': 'AI-QUADRATIC-INVERTIBLE-STRATUM-001',
        'status': 'Exact corroboration of a written unreviewed proof',
        'proof_sha256': hashlib.sha256((PACKAGE / 'proof.md').read_bytes()).hexdigest(),
        'sources_sha256': hashlib.sha256((PACKAGE / 'sources.json').read_bytes()).hexdigest(),
        'parent_tangent_identities': parent_tangent_checks(),
        'scalar_identities': scalar_checks(),
        'matrix_identities': matrix_checks(),
        'trace_only_boundary_controls': controls,
        'dimension_upper_bound': 4,
        'excluded_characteristics': [2, 3],
        'sharpness_supplied': False,
        'independent_review': False,
        'improves_omega': False,
    }


if __name__ == '__main__':
    print(json.dumps(report(), indent=2))
