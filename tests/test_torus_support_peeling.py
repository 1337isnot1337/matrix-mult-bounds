import copy
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'research/ai/2026-10-20-anisotropic-constructions/torus_support_peeling.py'
SPEC = importlib.util.spec_from_file_location('torus_support_peeling', PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
CERTIFICATE = ROOT / 'results/anisotropic-constructions-2026-10-20/torus-support-peeling-a88-m27-m7.json'


class TorusSupportPeelingTests(unittest.TestCase):
    def test_exact_certificate_without_discovery_geometry(self):
        data = json.loads(CERTIFICATE.read_text())
        with patch.object(MODULE, 'convex_hull', side_effect=AssertionError('Discovery geometry used by verifier')):
            with patch.object(MODULE, 'inside_hull', side_effect=AssertionError('Hull membership used by verifier')):
                result = MODULE.verify_certificate(data)
        self.assertEqual([(r['input_dimension'], r['rank_limit'], r['output_dimension'])
                          for r in result['rounds']], [(960, 391, 922), (922, 315, 834), (834, 139, 468)])
        self.assertTrue(result['ordinary_graded_restriction_excluded'])
        self.assertEqual(result['source_pair_projections_checked'], [262144] * 3)

    def test_rejects_false_separator_and_wrong_rank_limit(self):
        data = json.loads(CERTIFICATE.read_text())
        changed = copy.deepcopy(data)
        changed['rounds'][0]['removed_coordinates'][0]['separating_line'] = [0, 0, 0]
        with self.assertRaisesRegex(ArithmeticError, 'does not exclude'):
            MODULE.verify_certificate(changed)
        changed = copy.deepcopy(data)
        changed['rounds'][1]['rank_limit'] += 1
        with self.assertRaisesRegex(ArithmeticError, 'rank limit'):
            MODULE.verify_certificate(changed)

    def test_actual_identity_and_small_matrix_rank_controls_survive(self):
        # A(2,2) itself has dimension 12 and a homogeneous coordinate basis
        # with slice ranks at most 8. Its identity map must not be excluded.
        identity = MODULE.discover(2, 2, 12, 8)
        self.assertFalse(MODULE.verify_certificate(identity)['ordinary_graded_restriction_excluded'])
        self.assertEqual(identity['remaining_dimension'], 12)
        # The known coordinate M2 restriction also fits the stated parameters.
        small = MODULE.discover(2, 2, 4, 2)
        self.assertFalse(MODULE.verify_certificate(small)['ordinary_graded_restriction_excluded'])

    def test_unequal_source_corner_matchings_and_full_torus(self):
        for a, b in ((2, 3), (3, 2), (3, 4), (4, 3), (8, 8)):
            result = MODULE.corner_and_torus_controls(a, b)
            self.assertEqual(result['source_torus_weight_identities_checked'], (a * b) ** 3)
            self.assertEqual(result['full_rank_of_each_corner_slice'], a * b * min(a, b))
        big = MODULE.corner_and_torus_controls()
        self.assertEqual(big['full_rank_of_each_corner_slice'], 512)


if __name__ == '__main__':
    unittest.main()
