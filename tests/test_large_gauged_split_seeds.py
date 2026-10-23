import copy
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest


PACKAGE = Path(__file__).resolve().parents[1] / "research/ai/2026-10-23-large-gauged-batches"
SPEC = importlib.util.spec_from_file_location("large_gauged_split_verifier", PACKAGE / "verify.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class LargeGaugedSplitSeedTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixtures = {name: json.loads((PACKAGE / (name + "_certificate.json")).read_text())
                        for name in ("ten", "eleven")}

    def test_complete_exact_replay_and_regeneration(self):
        for name, count, directions, positives, weight in (
                ("ten", 10, 66, 283, 34), ("eleven", 11, 65, 414, 37)):
            with self.subTest(variant=name):
                certificate = self.fixtures[name]
                result = MODULE.verify(certificate)
                self.assertEqual(MODULE.build_certificate(name), certificate)
                self.assertEqual(result["discarded_terms"], count)
                self.assertEqual(result["intermediate_exact_terms"], 76 + count)
                self.assertEqual(result["surviving_border_terms"], 76)
                self.assertEqual(result["distinct_U_directions"], directions)
                self.assertEqual(result["all_constant_positions_checked"], 10000)
                self.assertEqual(result["constant_nonzero_coefficients"], 100)
                self.assertEqual(result["negative_coefficients"], 0)
                self.assertEqual(result["positive_nonzero_coefficients"], positives)
                self.assertEqual(result["deleted_original_U_weight"], weight)
                for field in ("rank_record_claimed", "search_optimum_claimed",
                              "actual_cross_component_flip_constructed", "Q64_maps_constructed",
                              "improves_omega"):
                    self.assertFalse(result[field])

    def test_poles_and_product_preserving_factor_gauges(self):
        for name, certificate in self.fixtures.items():
            with self.subTest(variant=name):
                minimums = certificate["minimum_factor_valuations"]
                self.assertTrue(any(min(row) < 0 for row in minimums))
                for row, gauge in zip(minimums, certificate["factor_gauge_exponents"]):
                    self.assertGreater(sum(row), 0)
                    self.assertEqual(sum(gauge), 0)
                    self.assertTrue(all(3*x + y > 0 for x, y in zip(row, gauge)))
                changed = copy.deepcopy(certificate)
                changed["factor_gauge_exponents"][0][0] += 1
                with self.assertRaisesRegex(ValueError, "does not preserve"):
                    MODULE.verify(changed)

    def test_coefficient_and_nonpositive_valuation_controls(self):
        for name, certificate in self.fixtures.items():
            with self.subTest(variant=name):
                changed = copy.deepcopy(certificate)
                item = changed["surviving_factors"][0][0][0]
                item[1] = str(Fraction(item[1]) + 7)
                with self.assertRaises(ValueError):
                    MODULE.coefficient_replay(changed)
                changed = copy.deepcopy(certificate)
                decrease = sum(changed["minimum_factor_valuations"][0])
                for item in changed["discarded_factors"][0][0]:
                    item[2] -= decrease
                with self.assertRaisesRegex(ValueError, "nonpositive valuation"):
                    MODULE.coefficient_replay(changed)

    def test_schema_source_scope_and_weight_controls(self):
        certificate = self.fixtures["eleven"]
        for key in ("schema", "scope", "seed_sha256", "basis_certificate_sha256", "variant"):
            with self.subTest(field=key):
                changed = copy.deepcopy(certificate)
                changed[key] = "changed"
                with self.assertRaises(ValueError):
                    MODULE.verify(changed)
        changed = copy.deepcopy(certificate)
        changed["weights"][0][0] = True
        with self.assertRaisesRegex(ValueError, "Invalid physical weights"):
            MODULE.verify(changed)
        changed = copy.deepcopy(certificate)
        changed["weights"][0][0] += 1
        with self.assertRaisesRegex(ValueError, "Surviving factors differ"):
            MODULE.verify(changed)

    def test_exact_ten_cross_span_contacts(self):
        certificate = self.fixtures["ten"]
        terms, _ = MODULE.V.split_seed(MODULE.V.load_seed(), certificate["replacements"])
        self.assertEqual(MODULE.check_ten_contacts(terms), 4)
        terms[19][0] = [[x for x in row] for row in terms[19][0]]
        terms[19][0][0][0] += 1
        with self.assertRaises(ValueError):
            MODULE.check_ten_contacts(terms)
        changed = copy.deepcopy(certificate)
        changed["cross_span_contacts"][0]["dimensions"] = [5, 1, 6]
        with self.assertRaisesRegex(ValueError, "Recorded cross-span contacts"):
            MODULE.verify(changed)

    def test_independent_dense_identity_at_signed_parameter(self):
        # Evaluate exported monomials directly, without parser or contraction
        # helpers.  Every expanded S+D family equals M at epsilon=-2.
        parameter = Fraction(-2)
        for name, certificate in self.fixtures.items():
            with self.subTest(variant=name):
                def evaluate(terms):
                    tensor = [Fraction(0)] * 10000
                    for term in terms:
                        factors = []
                        for entries, size in zip(term, (20, 25, 20)):
                            row = [Fraction(0)] * size
                            for coordinate, coefficient, exponent in entries:
                                row[coordinate] += Fraction(coefficient) * parameter**exponent
                            factors.append([(i, x) for i, x in enumerate(row) if x])
                        for a, x in factors[0]:
                            for b, y in factors[1]:
                                for c, z in factors[2]:
                                    tensor[(a * 25 + b) * 20 + c] += x*y*z
                    return tensor
                survivor = evaluate(certificate["surviving_factors"])
                error = evaluate(certificate["discarded_factors"])
                target = [Fraction(0)] * 10000
                for i in range(4):
                    for j in range(5):
                        for k in range(5):
                            target[((5*i+j)*25 + 5*j+k)*20 + 4*k+i] = 1
                self.assertEqual([x+y for x, y in zip(survivor, error)], target)
                self.assertNotEqual(survivor, target)


if __name__ == "__main__":
    unittest.main()
