"""Exact coordinate controls for the zero-grade minimum slice-rank lemma."""

from collections import defaultdict
from itertools import product
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def verify(a=8):
    slices = defaultdict(set)
    source_terms = 0
    for i, j, p, q, r, s in product(range(a), repeat=6):
        if i + s != p + q or j + p != r + s:
            continue
        if q + r != i + j:
            raise ArithmeticError('The third zero-grade equation did not follow')
        source_terms += 1
        # X=(i,s), Y=(p,j), Z=(r,q) are the common zero-grade indices.
        if (a + 1) * i + s - p + a * j - a * r - (a + 1) * q:
            raise ArithmeticError('The residual two-torus weight identity failed')
        slices[i, s].add((a * p + j, a * r + q))
    ranks = []
    for i, s in product(range(a), repeat=2):
        pairs = slices[i, s]
        if len({row for row, _ in pairs}) != len(pairs) or len({column for _, column in pairs}) != len(pairs):
            raise ArithmeticError('A coordinate slice is not a partial permutation matrix')
        formula = sum(a - abs(p - s) for p in range(a) if 0 <= i + s - p < a)
        if len(pairs) != formula or formula < a:
            raise ArithmeticError('A coordinate slice-rank formula failed')
        ranks.append(formula)
    if min(ranks) != a:
        raise ArithmeticError('The minimum coordinate rank is incorrect')
    return {'source': f'A({a},{a}) restricted to zero grades on all three legs',
            'zero_grade_leg_dimension': a * a,
            'full_source_terms_examined': a ** 6,
            'zero_grade_source_terms': source_terms,
            'coordinate_slice_ranks_lex_i_s': ranks,
            'coordinate_slices_are_partial_permutations': True,
            'residual_two_torus_identity_checked': True,
            'minimum_coordinate_slice_rank': a,
            'minimum_nonzero_slice_rank_by_torus_proof': a,
            'maximum_ordinary_graded_target_zero_dimension_with_scalar_slice':
                a * a - (a // 2),
            'standard_library_only': True,
            'general_degenerations_excluded': False,
            'new_exponent_established': False}


if __name__ == '__main__':
    report = verify()
    (HERE / 'parity_structure_zero_grade_rank.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
