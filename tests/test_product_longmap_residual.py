"""Exact fixed-long-map residual ranks, provenance, and corruption controls."""

from fractions import Fraction
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-product-longmap-residual"
SPEC = importlib.util.spec_from_file_location(
    "product_longmap_residual", PACKAGE / "verify.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
REFERENCE_ROOT = Path(os.environ.get("MATRIX_BOUNDS_REFERENCE_REPO", ROOT))


def old_reference():
    directory = REFERENCE_ROOT / "research/ai/2026-10-20-paired-direct-sums"
    spec = importlib.util.spec_from_file_location(
        "product_longmap_old_reference", directory / "q_product_projection.py"
    )
    result = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(directory))
    try:
        spec.loader.exec_module(result)
    finally:
        sys.path.pop(0)
    return result


class ProductLongmapResidualTests(unittest.TestCase):
    def test_certificate_exact_replay_and_scope(self):
        report = MODULE.verify()
        certificate = json.loads((PACKAGE / "certificate.json").read_text())
        self.assertEqual(report, certificate)
        cases = report["rational_direct_cases"]
        self.assertEqual([row["n"] for row in cases], list(range(5, 13)) + [16])
        self.assertEqual([row["minimum_first_residual_rank"] for row in cases],
                         [0, 16, 32, 48, 63, 80, 99, 120, 224])
        self.assertFalse(report["scope"]["excludes_arbitrary_long_maps"])
        self.assertFalse(report["scope"]["excludes_general_degenerations"])
        self.assertFalse(report["scope"]["improves_omega"])

    def test_pinned_sources_and_independent_dual_formula(self):
        sources = json.loads((PACKAGE / "sources.json").read_text())
        for source in sources["local_sources"]:
            data = (REFERENCE_ROOT / source["path"]).read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), source["sha256"])
        old = old_reference()
        for n in (5, 6, 7, 8, 12, 16, 32):
            dual = old.product_and_dual(n)[2]
            new = MODULE.dual_rows_twice(n)
            expected = [{j: 2 * value for j, value in enumerate(row) if value}
                        for row in dual]
            self.assertEqual(new, expected)

    def test_all_native_coefficients_match_the_old_maps(self):
        old = old_reference()
        for n in (5, 6):
            r = n - 1
            actual, target = old.contract(n, 4, r, old.maps(n))
            residual = MODULE.paired_spaces(n)[2]
            # Compare every coefficient, including every zero. The index
            # regrouping is separate from the code assembling paired rows.
            for i in range(r):
                for k in range(r):
                    row = residual[r * i + k]
                    for ib in range(r):
                        for jb in range(4):
                            y, a = divmod(jb, 2)
                            for jc in range(4):
                                b, v = divmod(jc, 2)
                                for kc in range(r):
                                    first = 4 * ib + 2 * a + v
                                    second = 4 * kc + 2 * b + y
                                    regrouped = first * (4 * r) + second
                                    native = ((r * i + k) * (4 * r)
                                              + 4 * ib + jb) * (4 * r)
                                    native += r * jc + kc
                                    self.assertEqual(row.get(regrouped, 0),
                                                     4 * (target[native]
                                                          - actual[native]))

    def test_quotient_rank_bound_can_be_attained(self):
        # Source S=<e0,e1>, target T=<e1,e2,e3>. The first target row
        # can be matched, while the other two remain independent modulo S.
        source = [{0: 1}, {1: 1}]
        target = [{1: 1}, {2: 1}, {3: 1}]
        minimum = MODULE.sparse_rank(source + target) - MODULE.sparse_rank(source)
        self.assertEqual(minimum, 2)
        optimum = [{}, {2: 1}, {3: 1}]
        self.assertEqual(MODULE.sparse_rank(optimum), minimum)
        # Several arbitrary replacements preserve the quotient lower bound.
        for a, b in ((0, 0), (1, -1), (Fraction(2, 3), Fraction(4, 5))):
            changed = [MODULE.add_rows(target[0], {0: a, 1: b}, -1),
                       MODULE.add_rows(target[1], {0: b}, -1),
                       MODULE.add_rows(target[2], {1: a}, -1)]
            self.assertGreaterEqual(MODULE.sparse_rank(changed), minimum)

    def test_characteristic_three_and_invalid_characteristics(self):
        # The older 3/4 diagonal minor vanishes in characteristic three.
        # The complete residual rank in the new theorem does not drop.
        self.assertEqual(MODULE.verify_case(12, direct=True, characteristic=3)
                         ["direct_old_map_residual_rank"], 120)
        with self.assertRaises(ValueError):
            MODULE.verify_case(8, characteristic=2)
        with self.assertRaises(ValueError):
            MODULE.verify_case(8, characteristic=9)
        with self.assertRaises(ValueError):
            MODULE.verify_case(4)

    def test_corruption_changes_the_exact_positive_control(self):
        source, target, residual = MODULE.paired_spaces(5)
        self.assertEqual(MODULE.sparse_rank(residual), 0)
        # Add one coefficient in a row previously identically zero.
        damaged = [dict(row) for row in residual]
        damaged[0][0] = 1
        self.assertEqual(MODULE.sparse_rank(damaged), 1)
        self.assertNotEqual(damaged, residual)
        # Removing the identity's final diagonal coefficient destroys a
        # genuine one-factor intersection vector at n=8.
        h, j, _ = MODULE.factor_spaces(8)
        self.assertEqual(MODULE.sparse_rank(h + [j[-1]]), len(h))
        bad = dict(j[-1])
        del bad[4 * 6 + 3]
        self.assertEqual(MODULE.sparse_rank(h + [bad]), len(h) + 1)


if __name__ == "__main__":
    unittest.main()
