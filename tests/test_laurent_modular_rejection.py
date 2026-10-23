"""Optional discovery checks; nonzero residues reject, zeros do not certify."""
import importlib.util
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / 'research/ai/2026-10-21-asymmetric-sl2-seed'
HAS_NUMPY = importlib.util.find_spec('numpy') is not None

@unittest.skipUnless(HAS_NUMPY, 'optional NumPy discovery dependency')
class LaurentModularTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.path.insert(0, str(FOLDER))
        spec = importlib.util.spec_from_file_location('laurent_modular_check', FOLDER / 'laurent_modular_check.py')
        cls.verify = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.verify)

    def test_exact_gauged_rectangular_positive_control(self):
        result = self.verify.control()
        self.assertFalse(result['exact_supplied_maps_rejected'])
        self.assertTrue(result['zero_result_would_not_certify_Q_i_identity'])

    def test_zero_maps_are_rejected(self):
        np = self.verify.np
        maps = [(np.zeros((5,45,n), dtype=np.int64), np.zeros((5,45,n), dtype=np.int64)) for n in (25,20,20)]
        result = self.verify.check(maps)
        self.assertTrue(result['exact_supplied_maps_rejected'])
        self.assertEqual(result['required_coefficient_mismatch_counts']['0'],100)
        self.assertTrue(all(v == 0 for k,v in result['required_coefficient_mismatch_counts'].items() if k != '0'))

    def test_dyadic_residue_is_exact(self):
        v = self.verify
        self.assertEqual(v.residue(0.125),pow(8,-1,v.P))
        self.assertEqual(v.residue(-0.5),(-pow(2,-1,v.P))%v.P)
        self.assertEqual(pow(v.P-1,(v.P-1)//2,v.P),v.P-1)

if __name__ == '__main__':
    unittest.main()
