"""Check the saved quotient-score certificate directly with integer powers."""

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class QuotientScoreCertificateTests(unittest.TestCase):
    def test_complete_integer_certificate(self):
        data = json.loads((ROOT/"results/anisotropic-constructions-2026-10-20/quotient-score-barrier.json").read_text())
        maximum = data["maximum_control"]
        n, d = maximum["rational_upper"]
        self.assertEqual(maximum["critical_root_left"], n**5*(d+2*n)**4)
        self.assertEqual(maximum["critical_root_right"], d**9)
        self.assertGreater(n**5*(d+2*n)**4, d**9)
        self.assertEqual(maximum["maximum_fourth_power_left"], n**5*(d+n)**13)
        self.assertEqual(maximum["maximum_fourth_power_right"], 16*d**18)
        self.assertLess(n**5*(d+n)**13, 16*d**18)
        large = data["large_long_dimension_control"]
        self.assertEqual(large["minimum_long_dimension"], 6)
        self.assertEqual(large["cleared_left"], 200**4*36**9)
        self.assertEqual(large["cleared_right"], (93*19**3)**4)
        self.assertLess(large["cleared_left"], large["cleared_right"])
        self.assertEqual([(x["a"], x["b"]) for x in data["small_source_controls"]], [(2, 2), (2, 3), (2, 4), (3, 3)])
        for row in data["small_source_controls"]:
            a, b = row["a"], row["b"]
            x, q = a+b-1, row["score_scale"]
            m, r = row["largest_quotient_dimension"], row["residual_matrix_size"]
            self.assertLessEqual(m*m, a*b*x)
            self.assertGreater((m+1)**2, a*b*x)
            self.assertEqual(r, a*b-m)
            upper, lower = row["positive_term_upper"], row["negative_term_lower"]
            self.assertGreaterEqual(upper**4, q**4*(6*m)**9)
            self.assertLessEqual(lower**4, q**4*(6*r)**9)
            self.assertEqual(row["critical_threshold"], (3*x+1)**3)
            self.assertLess(100*(upper-lower), 93*q*(3*x+1)**3)
        self.assertEqual(data["relative_score_ceiling"], [93, 100])
        self.assertFalse(data["new_exponent_established"])
        self.assertFalse(data["joint_inequality_method_excluded"])


if __name__ == "__main__":
    unittest.main()
