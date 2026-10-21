"""Integer controls for the scoped corner/full-correction theorem."""

import argparse
from fractions import Fraction
import json
from pathlib import Path


def verify():
    comparisons = [
        ('a(4)<4/5', 30**3, 13**4),
        ('b(5)<5/8', 3**12 * 5**9, 2**40),
        ('c(4)<1/6', 864**3, 13**8),
        ('max z^(3/2)(1-z)<3/16', 108*256, 9*3125),
        ('max sqrt(z)(1-z)<2/5', 4*25, 4*27),
    ]
    if not all(left < right for _, left, right in comparisons):
        raise ArithmeticError('A rational comparison failed')
    bound = Fraction(4, 5) + Fraction(5, 8)*Fraction(3, 16) + Fraction(1, 6)*Fraction(2, 5)
    if bound != Fraction(1889, 1920) or bound >= 1:
        raise ArithmeticError('The uniform inequality is not strict')
    return {'scope': 'full independent M_r correction supplied through the two-interval corner split',
            'comparisons': [{'claim': claim, 'left': left, 'right': right, 'strict': True}
                            for claim, left, right in comparisons],
            'uniform_dimension_ratio_upper_bound': str(bound),
            'nine_fourths_gate_excluded_in_this_scope': True,
            'shared_variable_cancellation_excluded': False,
            'general_source_restrictions_excluded': False,
            'new_exponent_established': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = verify()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
