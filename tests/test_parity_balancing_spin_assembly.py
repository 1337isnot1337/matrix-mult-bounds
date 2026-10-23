import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'research/ai/2026-10-20-anisotropic-constructions/parity_balancing_spin_assembly.py'
SPEC = importlib.util.spec_from_file_location('spin_assembly_exact_controls', SCRIPT)
CORE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CORE)


class SpinAssemblyTests(unittest.TestCase):
    def test_full_coefficient_preimage_and_bases(self):
        report = CORE.verify()
        self.assertEqual(report['first_response_exact_rank'], 192)
        self.assertEqual(report['first_response_kernel_dimension'], 768)
        self.assertEqual(report['first_preimage_dimension_of_nine_target_matrices'], 777)
        self.assertTrue(report['all_28_single_coordinate_deletions_keep_rank_192'])
        self.assertEqual(report['added_Y_rows_with_saved_X_Z']['exact_kernel_dimension'], 727)
        self.assertEqual(report['added_Z_rows_with_saved_X_Y']['exact_kernel_dimension'], 747)
        self.assertFalse(report['full_square_assembly_constructed'])

    def test_nonzero_kernel_tamper_is_rejected(self):
        certificate = json.loads(CORE.CERTIFICATE.read_text())
        certificate['new_Y_against_saved_X_Z']['integer_kernel_vectors'][0][0][1] *= 2
        with self.assertRaisesRegex(ArithmeticError, 'kernel vector has a nonzero exact coefficient'):
            CORE.verify(certificate=certificate)

    def test_actual_map_tamper_is_rejected(self):
        exported = json.loads(CORE.FULL_MAPS.read_text())
        exported['restrictions'][1]['maps']['X']['entries'][0][2] *= 2
        with self.assertRaisesRegex(ArithmeticError, 'complete source contraction failed'):
            CORE.verify(full_export=exported)


if __name__ == '__main__':
    unittest.main()
