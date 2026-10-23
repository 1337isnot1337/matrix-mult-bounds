"""Independent literal checks of exterior-module kernel witnesses."""
from __future__ import annotations

from itertools import combinations
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-mixed-longlegs-candidate"
SPEC = importlib.util.spec_from_file_location("mixed_longlegs_shadow", PACKAGE / "verify_shadow.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


class MixedLonglegsShadowTests(unittest.TestCase):
    def test_saved_report_and_literal_global_relations(self):
        report = VERIFY.report()
        saved = json.loads((ROOT / "results/mixed-longlegs-candidate-2026-10-23/shadow_verification.json").read_text())
        self.assertEqual(report, saved)
        self.assertEqual(report["global_degree_one_kernel_generators"], 428)
        self.assertTrue(report["all_generators_checked_on_unsplit_literal_map"])
        self.assertEqual(report["target_C5_kernel_lower_bound"], 4930805426)
        self.assertEqual(report["degrees_not_decided_by_these_bounds_alone"], [7, 8, 9, 10])
        self.assertEqual(report["current_unresolved_C_degrees"], [])

    def test_small_exterior_products_are_independent_literal_kernel_vectors(self):
        for counts, p in (({"F2": 1}, 2), ({"O33": 1, "O42": 1}, 2),
                          ({"O33": 1, "O42": 1}, 3), ({"F2": 1, "M2": 1}, 2)):
            bdim, cdim, generators = VERIFY.degree_one_generators(counts)
            _, _, entries = VERIFY.global_entries(counts)
            products = VERIFY.shadow_products(bdim, cdim, generators, p)
            degrees = [len(values) for values in VERIFY.leading_variables(bdim, generators)]
            expected = VERIFY.shadow_bound(cdim, degrees, p)
            self.assertEqual(len(products), expected)
            for product in products:
                self.assertFalse(VERIFY.literal_koszul_image(product, entries))
            domain = list(combinations(range(cdim), p))
            positions = {w: i for i, w in enumerate(domain)}
            rows = [{j * len(domain) + positions[w]: value
                     for (j, w), value in product.items()} for product in products]
            self.assertEqual(VERIFY.base.rational_rank(rows), expected)

    def test_shifted_output_projection_is_literal_polynomial_multiplication(self):
        for a, b, copies in ((1, 2, 2), (3, 2, 2), (5, 10, 10)):
            projected = {(i, r * b + j, r * b + i + j)
                         for r in range(copies) for i in range(a) for j in range(b)}
            full = {(i, j, i + j) for i in range(a) for j in range(copies * b)}
            self.assertEqual(projected, full)
            self.assertEqual(max(k for _, _, k in projected) + 1, copies * b + a - 1)


if __name__ == "__main__":
    unittest.main()
