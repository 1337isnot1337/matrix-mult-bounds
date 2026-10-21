"""Independent local reconstruction controls; no global exponent assertion."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    'sun_local_verifier', ROOT / 'research/ai/2026-10-21-sun-local-audit/verify.py')
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class SunLocalAuditTests(unittest.TestCase):
    def test_complete_local_replay(self):
        expected = json.loads((ROOT / 'results/sun-local-audit-2026-10-21/audit.json').read_text())
        actual = module.verify()
        # JSON represents integer degree keys by decimal strings.
        self.assertEqual(json.loads(json.dumps(actual)), expected)
        self.assertEqual(expected['literal_dense_scalars']['mismatch_count'], 128)
        self.assertEqual(expected['corrected_dense_scalars']['mismatch_count'], 0)
        for key in ['active_rank_four', 'active_source_resolved_lift',
                    'singular_C3', 'five_empty_C3']:
            self.assertEqual(expected[key]['negative_coefficients'], [])
            self.assertEqual(expected[key]['constant_mismatches'], [])
        self.assertTrue(expected['active_rank_four']['full_remainder_matches'])
        self.assertEqual(expected['five_empty_C3']['constant_coefficient_count'], 54)
        for record in expected['generic_exceptional_endpoints']:
            self.assertTrue(record['endpoint_pairing_identity'])
            self.assertEqual(record['cross_pairings_zero'], [True, True, True])
        self.assertEqual(expected['crossed_group_representation']['failures'], [])
        self.assertFalse(expected['full_M32_coefficient_witness_reconstructed'])
        self.assertFalse(expected['improves_omega'])


if __name__ == '__main__':
    unittest.main()
