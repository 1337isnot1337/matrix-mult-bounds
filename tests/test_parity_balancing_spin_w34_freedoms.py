import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'research/ai/2026-10-20-anisotropic-constructions/parity_balancing_spin_w34_freedoms.py'
SPEC = importlib.util.spec_from_file_location('spin_w34_freedoms', PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class SpinW34FreedomsTests(unittest.TestCase):
    def test_exact_family_and_full_replay(self):
        report = MODULE.verify()
        self.assertEqual(report['added_row_kernels']['Y']['complete_kernel_dimension'], 736)
        self.assertEqual(report['added_row_kernels']['Z']['complete_kernel_dimension'], 747)
        self.assertEqual(report['explicit_core_preserving_joint_family_parameters'], 891)
        self.assertFalse(report['new_exponent_established'])

    def test_actual_map_change_is_rejected(self):
        maps = json.loads(MODULE.MAPS.read_text())
        maps['restrictions'][1]['maps']['Z']['entries'][0][2] += 1
        with self.assertRaises(ArithmeticError):
            MODULE.verify(exported=maps)

    def test_kernel_change_is_rejected(self):
        certificate = json.loads(MODULE.CERTIFICATE.read_text())
        certificate['common_low_Y_kernel']['integer_kernel_vectors'][0][0][1] += 1
        with self.assertRaises(ArithmeticError):
            MODULE.verify(certificate=certificate)


if __name__ == '__main__':
    unittest.main()
