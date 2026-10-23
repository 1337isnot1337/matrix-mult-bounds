"""Source indexing, complete polynomial replay, and compression controls."""

import copy
from fractions import Fraction
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-23-conjugation-limit'
RESULTS = ROOT / 'results/conjugation-limit-2026-10-23'
spec = importlib.util.spec_from_file_location('conjugation_limit_verify', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)


def rational_rank(rows):
    """Independent small dense rational calculation for structural controls."""
    work = [[Fraction(value) for value in row] for row in rows]
    used = 0
    for column in range(len(work[0])):
        pivot = next((i for i in range(used, len(work)) if work[i][column]), None)
        if pivot is None:
            continue
        work[used], work[pivot] = work[pivot], work[used]
        scale = work[used][column]
        work[used] = [value / scale for value in work[used]]
        for row in range(used + 1, len(work)):
            scale = work[row][column]
            work[row] = [x - scale * y for x, y in zip(work[row], work[used])]
        used += 1
        if used == len(work):
            break
    return used


class ConjugationLimitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = json.loads((RESULTS / 'certificate.json').read_text())
        cls.leading, cls.limit_report = verify.verify_limit(cls.certificate)

    def test_complete_certificate_and_recorded_report(self):
        self.assertEqual(verify.verify(self.certificate),
                         json.loads((RESULTS / 'verification.json').read_text()))

    def test_literal_source_matches_six_index_expansion(self):
        slices = [{} for _ in range(112)]
        for i, j, p, q, r, s in product(range(4), repeat=6):
            first = 16 * (p + q) + 4 * i + s
            row = (4 * j + p) * 7 + r + s
            column = 28 * q + 4 * (i + j) + r
            position = 112 * row + column
            slices[first][position] = slices[first].get(position, 0) + 1
        for k, i, s in product(range(7), range(4), range(4)):
            self.assertEqual(slices[16 * k + 4 * i + s], verify.literal_slice(i, k, s))

    def test_wrong_leading_coefficient_and_late_term_are_rejected(self):
        bad = copy.deepcopy(self.certificate)
        bad['basis'][0]['leading'][0][1] += 1
        with self.assertRaisesRegex(ValueError, 'leading coefficient'):
            verify.verify_limit(bad)
        bad = copy.deepcopy(self.certificate)
        # The source coordinate has nonzero z^0 coefficient; a shifted copy
        # introduces terms beyond the retained degree, which must be checked.
        bad['basis'][0]['transform'].append([9, 0, 1])
        with self.assertRaisesRegex(ValueError, 'complete polynomial degree'):
            verify.verify_limit(bad)

    def test_false_scalar_action_and_incomplete_basis_are_rejected(self):
        altered = copy.deepcopy(self.leading)
        altered[0][100] = 1  # row0, column100: off the scalar diagonal
        with self.assertRaisesRegex(ValueError, 'scalar-action identity'):
            verify.verify_scalar_columns(altered, list(range(100, 112)))
        bad = copy.deepcopy(self.certificate)
        bad['basis'].pop()
        with self.assertRaisesRegex(ValueError, '112 certified rows'):
            verify.verify_limit(bad)

    def test_omitted_pair_and_wrong_modular_rank_are_rejected(self):
        bad = copy.deepcopy(self.certificate)
        bad['principal_compressions'].pop()
        with self.assertRaisesRegex(ValueError, 'incomplete coverage'):
            verify.verify_census(bad, self.leading)
        bad = copy.deepcopy(self.certificate)
        bad['principal_compressions'][0][2] -= 1
        with self.assertRaisesRegex(ValueError, 'wrong projected rank'):
            verify.verify_census(bad, self.leading)

    def test_projection_can_recover_a_lost_leading_direction(self):
        # L_t=span((1,0,0),(0,1,t)). Projection onto coordinates0,2
        # loses one leading direction, but saturation recovers (0,1).
        projected_leading = [[1, 0], [0, 0]]
        recovered_limit = [[1, 0], [0, 1]]
        self.assertEqual(rational_rank(projected_leading), 1)
        self.assertEqual(rational_rank(recovered_limit), 2)
        self.assertEqual(rational_rank(recovered_limit) - rational_rank(projected_leading), 1)

    def test_target_evaluation_rank_depends_on_vector_matrix_rank(self):
        # A tiny Mat3 tensor I2 control, evaluated at a rank1 and rank2 vector.
        for vector, expected in (([[1, 2], [0, 0], [0, 0]], 3),
                                 ([[1, 0], [0, 1], [0, 0]], 6)):
            images = []
            for i, j in product(range(3), repeat=2):
                image = [[0, 0] for _ in range(3)]
                image[i] = list(vector[j])
                images.append([value for row in image for value in row])
            self.assertEqual(rational_rank(images), expected)

    def test_source_pins(self):
        sources = json.loads((PACKAGE / 'sources.json').read_text())
        for source in sources['local_dependencies']:
            self.assertEqual(hashlib.sha256((ROOT / source['path']).read_bytes()).hexdigest(),
                             source['sha256'])


if __name__ == '__main__':
    unittest.main()
