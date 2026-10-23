"""Exact rational contraction certificate for C(5,10) degenerating to T4.

This verifier uses Python integers and fractions exclusively. It does not
import NumPy, SciPy, or the numerical discovery code. Decimal values are
produced only for display after all exact rational inequalities pass.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path
import argparse
import json
import time


def equations():
    nodes = [(a, p-a) for p in range(4) for a in range(p+1)]
    yw, zw = [-1, -1, 0, 1], [-1, 0, 1, 1]
    rows = []
    for x, y, z in product(range(4), range(10), range(10)):
        ya, yb = nodes[y]
        za, zb = nodes[z]
        exponent = yw[ya+yb]+zw[za+zb]
        target = int(ya+yb+za+zb == 3 and x == ya+za)
        assert not target or exponent == 0
        if exponent <= 0:
            terms = [(5*x+i, 20+10*y+j, 120+14*z+i+j)
                     for i in range(5) for j in range(10)]
            rows.append((x, y, z, exponent, target, terms))
    assert len(rows) == 172
    return rows


def evaluate_and_jacobian_numerators(center, denominator, rows):
    values, jacobian = [], []
    for _, _, _, _, target, terms in rows:
        values.append(sum(center[a]*center[b]*center[c] for a, b, c in terms)
                      -target*denominator**3)
        row = [0]*260
        for a, b, c in terms:
            row[a] += center[b]*center[c]
            row[b] += center[a]*center[c]
            row[c] += center[a]*center[b]
        jacobian.append(row)
    return values, jacobian


def multiply(left, right):
    columns = list(zip(*right))
    return [[sum(a*b for a, b in zip(row, column)) for column in columns]
            for row in left]


def rational_string(value):
    return str(value.numerator)+'/'+str(value.denominator)


def verify(certificate):
    start = time.monotonic()
    assert certificate['source'] == 'C(5,10)'
    assert certificate['target'] == 'canonical T4'
    assert certificate['variable_order'] == 'A[4,5],Y[10,10],Z[10,14]; row major'
    assert certificate['y_degree_weights'] == [-1, -1, 0, 1]
    assert certificate['z_degree_weights'] == [-1, 0, 1, 1]
    center = certificate['center_numerators']
    denominator = certificate['center_denominator']
    inverse = certificate['inverse_numerators']
    inverse_denominator = certificate['inverse_denominator']
    free = certificate['free_coordinate_indices']
    radius = Fraction(certificate['radius_numerator'], certificate['radius_denominator'])
    assert len(center) == 260 and all(type(v) is int for v in center)
    assert len(free) == len(set(free)) == 172 and all(0 <= v < 260 for v in free)
    assert len(inverse) == 172 and all(len(row) == 172 for row in inverse)
    assert all(type(v) is int for row in inverse for v in row)
    assert type(denominator) is int and denominator > 0
    assert type(inverse_denominator) is int and inverse_denominator > 0
    assert radius > 0
    rows = equations()
    f_numerators, full_jacobian = evaluate_and_jacobian_numerators(center, denominator, rows)
    jacobian = [[row[c] for c in free] for row in full_jacobian]
    rj_numerators = multiply(inverse, jacobian)
    common = inverse_denominator*denominator**2
    delta = Fraction(max(sum(abs((common if i == j else 0)-value)
                             for j, value in enumerate(row))
                         for i, row in enumerate(rj_numerators)), common)
    eta = Fraction(max(abs(sum(a*b for a, b in zip(row, f_numerators)))
                       for row in inverse), inverse_denominator*denominator**3)
    inverse_norm = Fraction(max(sum(map(abs, row)) for row in inverse), inverse_denominator)
    center_bound = Fraction(max(map(abs, center)), denominator)
    # Each equation has 50 distinct trilinear source monomials. Each has at
    # most six ordered second partial derivatives, bounded by M+radius.
    jacobian_lipschitz_bound = 300*(center_bound+radius)
    contraction = delta+inverse_norm*jacobian_lipschitz_bound*radius
    image_radius = eta+contraction*radius
    assert delta < 1, 'The rational approximate inverse is not certified invertible.'
    assert contraction < 1, 'The rational Newton map is not certified contractive.'
    assert image_radius < radius, 'The rational Newton map is not certified to preserve its ball.'
    # Confirm that the ordinary degree grading's entire coefficient set is
    # included, so the same exact zero also works with X=-3, Y=p, Z=q.
    included = {(x, y, z) for x, y, z, *_ in rows}
    nodes = [(a, p-a) for p in range(4) for a in range(p+1)]
    natural_count = 0
    for x, y, z in product(range(4), range(10), range(10)):
        if sum(nodes[y])+sum(nodes[z]) <= 3:
            assert (x, y, z) in included
            natural_count += 1
    assert natural_count == 140
    fractions = dict(radius=radius, center_max_abs=center_bound,
                     inverse_infinity_norm=inverse_norm,
                     initial_correction_bound=eta,
                     inverse_defect_bound=delta,
                     jacobian_lipschitz_bound=jacobian_lipschitz_bound,
                     contraction_factor_bound=contraction,
                     image_radius_bound=image_radius,
                     strict_ball_margin=radius-image_radius)
    return dict(
        status='exact rational contraction certificate passed',
        mathematical_conclusion='There exist exact real constant maps giving C(5,10) >=_deg T4.',
        all_172_equations_have_a_common_exact_real_zero=True,
        coefficient_equations=172,
        negative_weight_equations=sum(row[3] < 0 for row in rows),
        zero_weight_equations=sum(row[3] == 0 for row in rows),
        natural_grading_equations_also_certified=natural_count,
        parameters=260, free_parameters=172, fixed_rational_parameters=88,
        exact_bounds={key: rational_string(value) for key, value in fractions.items()},
        decimal_display_only={key: float(value) for key, value in fractions.items()},
        verifier_uses_only_integer_and_fraction_arithmetic=True,
        numerical_array_is_not_claimed_to_be_an_exact_solution=True,
        new_exponent_established=False,
        seconds=time.monotonic()-start,
    )



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate', type=Path)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    certificate = json.loads(args.certificate.read_text())
    result = verify(certificate)
    encoded = json.dumps(result, indent=2)+'\n'
    if args.report:
        args.report.write_text(encoded)
    print(encoded, flush=True)
