from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "cyclic_equivariant", ROOT / "research/ai/2026-10-20-cyclic-equivariant/verify.py")
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class CyclicEquivariantTests(unittest.TestCase):
    def test_complete_exact_report(self):
        actual = json.loads(json.dumps(v.report()))
        self.assertEqual(actual, json.loads((v.RESULTS / "certificate.json").read_text()))
        self.assertEqual([r["vertex_representation_triples_checked"] for r in actual["representation_screens"]],
                         [8, 1200, 12312])

    def test_five_coefficient_identity_and_target_violation(self):
        for x0, xh, y0, yh, z0, zh in ((2, 3, 5, 7, 11, 13), (0, 3, 5, 0, 11, 13)):
            b = [x0*y0*z0, x0*yh*zh, xh*y0*zh, xh*yh*z0, xh*yh*zh]
            self.assertEqual(b[1]*b[2]*b[3]-b[0]*b[4]**2, 0)
        self.assertEqual(v.coefficients(2)["polynomial_defect"], str(Fraction(36, 5)))

    def test_both_central_parities_and_natural_positive_control(self):
        self.assertEqual(list(v.partitions(3, 0)), [])
        self.assertEqual(list(v.partitions(4, 0)), [(2, 2), (4,)])
        self.assertIn([[2], [2], [2]], v.representation_screen(2, (2, 2, 2))["survivors"])


if __name__ == "__main__":
    unittest.main()
