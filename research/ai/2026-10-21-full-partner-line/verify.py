"""Close the full b=1 partner line by explicit minors, phases and a=0."""
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


common = load('full_line_generic', HERE.parent / '2026-10-21-generic-partner-all-graphs/verify.py')
zero_module = load('full_line_zero', HERE / 'zero.py')
A = common.A
BAD = sp.Poly(A*(A**3-1), A, domain=sp.QQ)


@lru_cache(None)
def certificate(name):
    return json.loads((HERE / name).read_text())


zero_proof = zero_module.ZeroProof(common, certificate('zero-certificate.json'))


def allowed_polynomial(value):
    polynomial = sp.Poly(value, A, domain=sp.QQ)
    if polynomial.is_zero:
        return False
    while polynomial.degree() > 0:
        divisor = sp.gcd(polynomial, BAD)
        if divisor.degree() <= 0:
            return False
        polynomial = polynomial.exquo(divisor)
    return True


def check_minor(matrix, record):
    rank, rows, columns = record['rank'], record['rows'], record['columns']
    if (len(rows) != rank or len(set(rows)) != rank or not set(rows) <= set(range(matrix.rows))
            or len(columns) != rank or len(set(columns)) != rank or not set(columns) <= set(range(matrix.cols))):
        raise ArithmeticError('Invalid explicit rank minor')
    expected = sp.sympify(record['determinant'], locals={'a': A})
    numerator, denominator = sp.fraction(sp.cancel(expected))
    if not allowed_polynomial(numerator) or not allowed_polynomial(denominator):
        raise ArithmeticError('The rank minor has an unclassified zero or pole')
    if not rank:
        if expected != 1:
            raise ArithmeticError('Incorrect empty rank minor')
        return
    minor = matrix[rows, columns].copy()
    row_denominators = []
    for i in range(rank):
        scalar = sp.lcm([sp.denom(sp.cancel(value)) for value in minor[i, :].todok().values()])
        if not allowed_polynomial(scalar):
            raise ArithmeticError('A rank-minor row has an unclassified pole')
        row_denominators.append(scalar)
        if scalar != 1:
            minor[i, :] = minor[i, :].applyfunc(lambda value: sp.cancel(scalar*value))
    # Fraction-free polynomial determinants avoid repeated rational-function divisions.
    domain_matrix = minor.to_DM().convert_to(sp.QQ.poly_ring(A))
    determinant = domain_matrix.domain.to_sympy(domain_matrix.det())
    actual = sp.cancel(determinant/sp.prod(row_denominators))
    if sp.cancel(actual-expected) != 0:
        raise ArithmeticError('The explicit rank-minor determinant is incorrect')


def check_cover_labels(guards, records):
    labels = [r['label'] for r in records]
    expected = [r['label'] for r in guards]
    if (len(labels) != len(set(labels)) or len(expected) != len(set(expected))
            or len(labels) != len(expected) or set(labels) != set(expected)):
        raise ArithmeticError('The explicit minors do not cover every rational rank guard')


def phase_report(record):
    frames = common.frames
    extension = common.normal.extension
    weights = record['leg_coordinate_weights']
    frame_weights = [record['B_frame_weights'], record['C_frame_weights']]
    if (len(weights) != 3 or any(len(row) != 3 for row in weights)
            or any(len(row) != 7 for row in frame_weights)
            or any(type(value) is not int or not 0 <= value < 3 for row in weights+frame_weights for value in row)):
        raise ArithmeticError('Incorrect cube-root phase certificate')

    def physical_weight(leg, index):
        coordinates = (index//28, (index//7) % 4, index % 7)
        return sum(x*y for x, y in zip(weights[leg], coordinates)) % 3

    for term in extension.TERMS:
        if sum(physical_weight(leg, index) for leg, index in enumerate(term)) % 3:
            raise ArithmeticError('The phase does not preserve the original source tensor')
    for leg in (1, 2):
        for row in extension.G:
            if len({physical_weight(leg, index) for index in row}) != 1:
                raise ArithmeticError('The phase does not preserve a leading G row')
    bases = [common.normal.complement(extension.EB), common.normal.complement(extension.EC)]
    coefficients = 0
    for side, (coordinates, basis) in enumerate(zip(frames.chart_frames(), bases)):
        for j, covector in enumerate(frames.covectors(coordinates, basis)):
            for index, value in covector.items():
                for (degree_a, _), scalar in sp.Poly(value, frames.A, frames.B, domain=sp.QQ).terms():
                    if scalar and (physical_weight(side+1, index)-frame_weights[side][j]-degree_a) % 3:
                        raise ArithmeticError('The phase does not send a to zeta*a in the partner frames')
                    coefficients += 1
    return {'order': 3, 'source_terms_checked': len(extension.TERMS), 'leading_rows_checked': 8,
            'frame_coefficients_checked': coefficients, 'leg_coordinate_weights': weights,
            'parameter_action': 'a -> zeta*a, b unchanged, zeta**3=1',
            'source_automorphism_verified': True}


@lru_cache(None)
def report():
    records = certificate('rank-minor-cover.json')['minors']
    lookup = {r['label']: r for r in records}
    if len(lookup) != len(records):
        raise ArithmeticError('Duplicate rank-minor labels')
    seen = []
    original_guard = common.guard

    def explicit_guard(matrix, rank, label):
        numeric = original_guard(matrix, rank, label)
        if label not in lookup or lookup[label]['rank'] != rank:
            raise ArithmeticError('A rational rank guard has no matching explicit minor')
        check_minor(matrix, lookup[label])
        seen.append(label)
        return numeric

    common.guard = explicit_guard
    try:
        generic_report = common.report()
    finally:
        common.guard = original_guard
    check_cover_labels(generic_report['rank_guards'], records)
    if set(seen) != set(lookup) or len(seen) != len(records):
        raise ArithmeticError('Some explicit rank minors were not replayed')
    for denominator in generic_report['coefficient_denominators']:
        if not allowed_polynomial(sp.sympify(denominator, locals={'a': A})):
            raise ArithmeticError('A coefficient pole is outside the explicit candidate set')
    phase = phase_report(certificate('phase-certificate.json'))
    equal_partner = common.previous.report()
    if not equal_partner['all_graph_targets_excluded_at_partner']:
        raise ArithmeticError('The a=1 exclusion was not replayed')
    zero = zero_proof.report()
    return {'claim': 'AI-FULL-PARTNER-LINE-099', 'partner_line': 'b=1, every complex a',
            'generic_exception_polynomial': 'a*(a**3-1)', 'rank_minors_verified': len(records),
            'generic_rank_conditions_covered': True, 'phase': phase,
            'a_one_source_report_replayed': True, 'a_zero': zero,
            'all_complex_a_at_b_one_excluded': True, 'all_six_graph_parameters_covered': True,
            'arbitrary_boundary_four_space': True, 'extends_to_all_b_nonzero': True,
            'b_zero_boundary_classified': False, 'plane_dimension': 4,
            'final_nonplane_dimension': 0, 'independent_review': False, 'improves_omega': False}


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
