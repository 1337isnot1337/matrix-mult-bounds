"""Acceptance and hypothesis controls for rectangular aggregation gates."""
import copy
import importlib.util
import json
from math import comb
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-aggregation-families/rectangular"
spec = importlib.util.spec_from_file_location("aggregation_rectangular", PACKAGE / "verify.py")
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)


class AggregationRectangularTests(unittest.TestCase):
    def test_complete_saved_shape_certificate(self):
        saved = json.loads((PACKAGE / "certificate.json").read_text())
        report = verify.verify_certificate(saved)
        self.assertTrue(report["accepted"])
        self.assertEqual(report["excluded_coordinate_counts"], list(range(1, 33)))
        # Independent coverage count: enumerate ordered triples and canonicalize.
        shapes = {(a, b, d-a-b) for d in range(1, 34)
                  for a in range(d+1) for b in range(d-a+1) if a <= b <= d-a-b}
        self.assertEqual({tuple(row["shape"]) for row in saved["shape_rows"]}, shapes)

    def test_balanced_specialization_and_boundary(self):
        for n in range(1, 12):
            c, d = comb(3*n, n), comb(2*n, n)
            row = verify.shape_row(n, n, n)
            self.assertEqual(row["product_cap"], 2*c*d // (3*d-1))
            self.assertEqual(row["excluded_by_complete_grid_budget"], n <= 10)
        self.assertEqual(verify.shape_row(10, 11, 11)["product_cap"], 64512240)
        self.assertFalse(verify.shape_row(11, 11, 11)["excluded_by_complete_grid_budget"])

    def test_individual_capacities_are_not_omitted(self):
        row = verify.shape_row(1, 2, 3)
        self.assertEqual(row["incidence_cap"], 7)
        self.assertEqual(row["product_cap"], 6)
        self.assertEqual(verify.shape_row(0, 1, 5)["product_cap"], 1)

    def test_incomplete_or_understated_certificate_rejected(self):
        saved = json.loads((PACKAGE / "certificate.json").read_text())
        missing = copy.deepcopy(saved)
        missing["shape_rows"].pop()
        with self.assertRaisesRegex(ValueError, "differs"):
            verify.verify_certificate(missing)
        wrong = copy.deepcopy(saved)
        wrong["shape_rows"][0]["product_cap"] = 0
        with self.assertRaisesRegex(ValueError, "differs"):
            verify.verify_certificate(wrong)

    def test_full_and_restricted_local_product_spaces(self):
        controls = verify.local_controls()
        self.assertEqual([row["pair_product_rank"] for row in controls["full_target_controls"]],
                         [1, 3, 4, 5, 6, 7, 8])
        self.assertEqual(controls["restricted_target_control"]["zero_projected_rows"], [2])


if __name__ == "__main__":
    unittest.main()
