"""Complete exact checks for the free-source direct-sum construction."""

import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'research/ai/2026-10-20-anisotropic-constructions/parity_structure_free_interior.py'
SPEC = importlib.util.spec_from_file_location('parity_structure_free_interior', PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class FreeInteriorConstructionTests(unittest.TestCase):
    def test_saved_a88_complete_contraction_and_tamper(self):
        report = MODULE.verify()
        self.assertEqual(report['target_blocks'], [7, 7, 6])
        self.assertEqual(report['exact_target_terms'], 902)
        self.assertEqual(report['free_source_dimension'], 722)
        self.assertTrue(report['nonzero_to_nonzero_tamper_rejected'])

    def test_smallest_member_includes_the_central_scalar(self):
        report = MODULE.verify(MODULE.build(3), check_tamper=False)
        self.assertEqual(report['target_blocks'], [2, 2, 1])
        self.assertEqual(report['exact_target_terms'], 17)
        self.assertTrue(report['all_mixed_block_coefficients_zero'])


if __name__ == '__main__':
    unittest.main()
