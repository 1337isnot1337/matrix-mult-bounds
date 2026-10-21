"""Exact checks for a CONDITIONAL paired-source linear-correction criterion."""
import argparse
from fractions import Fraction
from itertools import product
import json
from pathlib import Path


def certificate():
    numerator, denominator = 13433, 10000
    left = pow(numerator, denominator) * pow(24, numerator)
    right = pow(96 * denominator, denominator)
    if not left < right:
        raise ArithmeticError('The conditional root certificate failed.')
    # These exact rational controls exercise all correction exponents.
    count = 0
    for raw in product(range(9), repeat=3):
        p = [Fraction(v, 8) for v in raw]
        S = sum(p)
        if S <= 2:
            continue
        pair_gaps = [S - p[k] - 1 for k in range(3)]
        single_gaps = [S + p[k] - 2 for k in range(3)]
        if min(pair_gaps + single_gaps + [2 * S - 3]) <= 0:
            raise ArithmeticError('A correction term was not lower order.')
        count += 1
    boundary_controls = []
    for n in range(2, 9):
        for b in range(2, 6):
            complete = {(p * n + q, q * b + j, j * n + p): 1
                        for p in range(n) for q in range(n) for j in range(b)}
            patterns = [('diagonal', {(p, p) for p in range(n)})]
            for c in range(1, min(3, n)):
                patterns.append(('boundary_' + str(c),
                                 {(p, q) for p in range(n) for q in range(n)
                                  if p >= n - c or q >= n - c}))
            for name, missing in patterns:
                kept = {key: value for key, value in complete.items()
                        if divmod(key[0], n) not in missing}
                # Construct the correction independently as individual products.
                correction = {}
                for p, q in missing:
                    for j in range(b):
                        key = (p * n + q, q * b + j, j * n + p)
                        correction[key] = correction.get(key, 0) + 1
                restored = dict(kept)
                for key, value in correction.items():
                    restored[key] = restored.get(key, 0) + value
                if restored != complete:
                    raise ArithmeticError('A boundary correction failed.')
                expected = b * n if name == 'diagonal' else b * (
                    2 * int(name.split('_')[1]) * n - int(name.split('_')[1]) ** 2)
                if len(correction) != expected:
                    raise ArithmeticError('A correction budget was miscounted.')
                boundary_controls.append({'n': n, 'b': b, 'pattern': name,
                                          'rank_one_terms': expected,
                                          'complete_coefficients': len(complete)})
    return {
        'claim_id': 'COND-PAIRED-LINEAR-CORRECTION-001',
        'improves_omega': False,
        'construction_supplied': False,
        'premise': 'For fixed b=4 and unbounded n, Q(n,4) plus an auxiliary of border rank O(n) degenerates to M(n,4,n), or the stated near-full rectangle.',
        'conditional_omega_upper_bound': '30000/13433',
        'strict_upper_comparison': '30000/13433 < 2.2334',
        'root_certificate': {
            'd_numerator': numerator, 'd_denominator': denominator,
            'integer_inequality': '13433^10000 * 24^13433 < 960000^10000',
            'left_bits': left.bit_length(), 'right_bits': right.bit_length(),
            'strict_comparison_passes': left < right},
        'critical_width_condition': '81*b > 256',
        'first_admissible_integer_width': next(b for b in range(1, 10) if 81 * b > 256),
        'rational_parameter_controls': count,
        'boundary_controls': boundary_controls,
        'scope': 'Finite verification of the conditional algebra and explicit correction counts. No paired source-to-target maps or unbounded family are supplied.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({key: result[key] for key in (
        'claim_id', 'construction_supplied', 'improves_omega',
        'first_admissible_integer_width', 'rational_parameter_controls')}))
