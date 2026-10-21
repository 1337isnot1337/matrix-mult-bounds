"""Complete exact verification of the recovered Q54 -> M4 maps."""

import importlib.util
import json
from itertools import product
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-20-paired-construction"
SPEC = importlib.util.spec_from_file_location("outer_product_injection", PACKAGE / "outer_product_injection.py")
Q = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(Q)


class OuterProductInjectionTests(unittest.TestCase):
    def test_saved_integer_certificate(self):
        saved = json.loads((PACKAGE / "q54-exact.json").read_text())
        self.assertEqual(saved, Q.certificate(4))
        self.assertEqual(saved["source_terms_checked"], 400)
        self.assertEqual(saved["all_target_coefficient_positions_checked"], 4096)
        self.assertEqual(saved["target_nonzero_coefficients"], 64)
        self.assertEqual(saved["map_nonzero_counts"], [25, 20, 20])
        self.assertTrue(saved["restriction_constructed"])
        self.assertFalse(saved["improves_omega"])

    def test_full_saved_maps_independently(self):
        saved = json.loads((PACKAGE / "q54-exact.json").read_text())
        a, b, c = saved["maps_target_by_source"]
        tensor = [[[0]*16 for _ in range(16)] for _ in range(16)]
        # This uses only saved arrays, and independent direct source loops.
        for p, q, y, v in product(range(5), range(5), range(4), range(4)):
            aa, bb, cc = 5*p+q, 8*y+q+v, 4*(p+y)+v
            for ia in range(16):
                if not a[ia][aa]:
                    continue
                for ib in range(16):
                    if not b[ib][bb]:
                        continue
                    for ic in range(16):
                        tensor[ia][ib][ic] += a[ia][aa]*b[ib][bb]*c[ic][cc]
        for ia, ib, ic in product(range(16), repeat=3):
            i, h = divmod(ia, 4)
            ii, j = divmod(ib, 4)
            jj, hh = divmod(ic, 4)
            self.assertEqual(tensor[ia][ib][ic], int(i == ii and j == jj and h == hh))

    def test_all_bilinear_basis_inputs_and_integer_example(self):
        for left_entry, right_entry in product(range(16), repeat=2):
            left = [[int(4*i+j == left_entry) for j in range(4)] for i in range(4)]
            right = [[int(4*j+h == right_entry) for h in range(4)] for j in range(4)]
            expected = [[sum(left[i][j]*right[j][h] for j in range(4))
                         for h in range(4)] for i in range(4)]
            self.assertEqual(Q.multiply(left, right), expected)
        left = [[(7*i+3*j) % 11-5 for j in range(4)] for i in range(4)]
        right = [[(2*j+5*h) % 13-6 for h in range(4)] for j in range(4)]
        expected = [[sum(left[i][j]*right[j][h] for j in range(4))
                     for h in range(4)] for i in range(4)]
        self.assertEqual(Q.multiply(left, right), expected)

    def test_family_integer_identities(self):
        for k in range(2, 9):
            report = Q.certificate(k, include_maps=False)
            self.assertEqual(report["all_target_coefficient_positions_checked"], 16*k**4)
            self.assertEqual(report["target_nonzero_coefficients"], 4*k*k)
            self.assertEqual(report["map_nonzero_counts"], [(k+1)**2, 4*k+4, 4*k+4])


if __name__ == "__main__":
    unittest.main()
