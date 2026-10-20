"""Check the arithmetic and positive controls; do not assume the new premise."""
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research/ai/2026-10-20-koszul"))
import finite_amplitude as amplitude


class FiniteAmplitudeTests(unittest.TestCase):
    def test_exact_rational_implication(self):
        required = Fraction(5005, 486)
        self.assertEqual(required, Fraction(13,12)*amplitude.diagonal(4))
        self.assertGreater((6*required)**3, 22**4)
        self.assertGreater(5005**2249, 22**3000*81**2249)
        self.assertLess(3*Fraction(749,1000), Fraction(2249,1000))

    def test_dimension_screen_boundary(self):
        for a in (1,2,3):
            volume = a*a*(2*a-1)
            self.assertLessEqual(6**6*volume**3, (6*a-2)**8)
        self.assertGreater(6**6*112**3, 22**8)
        self.assertGreater(Fraction(112), Fraction(5005,486)**2)

    def test_concrete_matrix_target_certificate(self):
        self.assertEqual((4*4*7)**2, 12544)
        self.assertEqual(7**6, 117649)
        self.assertLess(106**2, 12544)
        self.assertLess((36*105)**3, 22**8)
        self.assertGreater((36*106)**3, 22**8)
        self.assertGreater(3816**2249, 22**6000)

    def test_abelian_embedding_and_coordinate_bound(self):
        for a in range(2, 9):
            modulus = 2*a-1
            for i in range(a):
                for j in range(a):
                    for k in range(modulus):
                        self.assertEqual((i+j-k)%modulus == 0, i+j == k)
        self.assertEqual(49**3, 7**6)
        self.assertGreater(106**3, 7**6)
        self.assertLess(6**9*4**8*7**5, 22**12)
        # This particular inequality does not close the next diagonal.
        self.assertGreater(6**9*5**8*9**5, 28**12)

    def test_matching_profile_does_not_supply_the_premise(self):
        for a in range(1, 65):
            self.assertLess((6*amplitude.diagonal(a))**3, (6*a-2)**4)
        self.assertLess(amplitude.diagonal(4), Fraction(5005,486))

    def test_replay_report(self):
        saved = json.loads((ROOT / "results/koszul-2026-10-20/finite_amplitude.json").read_text())
        self.assertEqual(amplitude.report(), saved)
        self.assertFalse(saved["new_exponent_established"])

    def test_existing_controls_in_new_discovery_direction(self):
        path = ROOT / "research/ai/2026-10-20-concavity-equivalence/graded_certificate.py"
        spec = importlib.util.spec_from_file_location("graded_exact_control", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for a in (2,3):
            p,q = module.small_control(a)
            result = module.verify(a, a*(a+1)//2, p,q,alpha=5,beta=2)
            self.assertTrue(result["exact"])


if __name__ == "__main__":
    unittest.main()
