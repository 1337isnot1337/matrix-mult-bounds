"""Exact finite controls for a conditional superlinear correction budget."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import argparse
import json


def localization_threshold(alpha):
    alpha = Fraction(alpha)
    if not 1 <= alpha < Fraction(3, 2):
        raise ValueError('The stated quantitative theorem requires 1 <= alpha < 3/2.')
    return Fraction(9, 4) - (Fraction(3, 2) - alpha) ** 2


def correction_gaps(p, alpha):
    """Exponents of all seven auxiliary monomials, subtracted from 2S."""
    p = tuple(map(Fraction, p))
    alpha = Fraction(alpha)
    if len(p) != 3 or any(x < 0 or x > 1 for x in p):
        raise ValueError('Three dot-product parameters in [0,1] are required.')
    total = sum(p)
    return [total - x - alpha for x in p] + [
        total + x - 2 * alpha for x in p] + [2 * total - 3 * alpha]


def certificate():
    alphas = [Fraction(1), Fraction(4, 3), Fraction(137, 100),
              Fraction(7, 5), Fraction(149, 100)]
    root_upper = Fraction(30000, 13433)
    root_ok = 13433 ** 10000 * 24 ** 13433 < 960000 ** 10000
    if not root_ok:
        raise ArithmeticError('The existing exact root upper certificate failed.')
    expected = [Fraction(2), Fraction(20, 9), Fraction(22331, 10000),
                Fraction(56, 25), Fraction(22499, 10000)]
    rows = []
    for alpha, threshold in zip(alphas, expected):
        if localization_threshold(alpha) != threshold:
            raise ArithmeticError('An exact localization threshold is incorrect.')
        rows.append({'alpha': str(alpha), 'localization_threshold': str(threshold),
                     'retains_strict_30000_over_13433': threshold < root_upper,
                     'parameter_controls': 0, 'minimum_observed_gap': None})
    grid_denominator = 40
    angular_points = 0
    minimum_gaps = [None] * len(alphas)
    for raw in product(range(grid_denominator + 1), repeat=3):
        # For S>2, the angular condition is equivalent to
        # 4*(1-p0)*(1-p1)*(1-p2) >= (S-2)^2.
        total_raw = sum(raw)
        if not 2 * grid_denominator < total_raw <= 9 * grid_denominator // 4:
            continue
        qprod = 1
        for value in raw:
            qprod *= grid_denominator - value
        if 4 * qprod < grid_denominator * (total_raw - 2 * grid_denominator) ** 2:
            continue
        angular_points += 1
        p = [Fraction(x, grid_denominator) for x in raw]
        total = sum(p)
        for k, alpha in enumerate(alphas):
            if total <= expected[k]:
                continue
            gaps = correction_gaps(p, alpha)
            if min(gaps) <= 0:
                raise ArithmeticError('A predicted lower-order term has a nonpositive gap.')
            # Independently compare the exponents of each expanded monomial.
            a_exponents = [total - x for x in p]
            for mask in range(1, 8):
                exponent = sum(alpha if mask & (1 << i) else a_exponents[i]
                               for i in range(3))
                if not exponent < 2 * total:
                    raise ArithmeticError('Direct product expansion failed its exponent bound.')
            rows[k]['parameter_controls'] += 1
            minimum_gaps[k] = min(gaps) if minimum_gaps[k] is None else min(minimum_gaps[k], *gaps)
    for row, gap in zip(rows, minimum_gaps):
        row['minimum_observed_gap'] = None if gap is None else str(gap)
    # The endpoint p=(3/4,3/4,3/4), alpha=3/2 makes every gap zero.
    # This rejects extending the quantitative big-O argument through equality.
    boundary = correction_gaps([Fraction(3, 4)] * 3, Fraction(3, 2))
    if boundary != [0] * 7:
        raise ArithmeticError('The strict-boundary negative control failed.')
    return {
        'claim_id': 'COND-PAIRED-SUPERLINEAR-CORRECTION-015',
        'construction_supplied': False, 'improves_omega': False,
        'conditional_bound': 'max(3/d_b, 9/4-(3/2-alpha)^2)',
        'd_b_equation': 'd_b*(6*b)^d_b=12*b^(3/2)',
        'exact_root_comparison_passed': root_ok,
        'root_upper': str(root_upper), 'grid_denominator': grid_denominator,
        'algebraic_angular_points': angular_points, 'examples': rows,
        'endpoint_big_O_gaps': [str(x) for x in boundary],
        'qualitative_endpoint_premise': 'auxiliary border rank o(n^(3/2))',
        'scope': 'Finite controls for a written conditional argument. No maps or unbounded construction are supplied.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = certificate()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
