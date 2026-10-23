"""Exact positive and mutation controls for the six-split tensor-valuation seed."""
import copy
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest


PACKAGE = (Path(__file__).resolve().parents[1]
           / "research/ai/2026-10-23-gauged-splits")
SPEC = importlib.util.spec_from_file_location("gauged_split_seed", PACKAGE / "verify.py")
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)


class GaugedSplitSeedTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = json.loads((PACKAGE / "certificate.json").read_text())

    def test_complete_exact_identity_and_regeneration(self):
        result = V.verify(self.certificate)
        self.assertEqual(result["surviving_border_terms"], 76)
        self.assertEqual(result["distinct_U_directions"], 70)
        self.assertEqual(result["constant_positions_checked"], 10000)
        self.assertEqual(result["negative_coefficients"], 0)
        self.assertEqual(result["positive_nonzero_coefficients"], 73)
        self.assertFalse(result["Q64_maps_constructed"])
        self.assertFalse(result["rank_record_claimed"])
        self.assertEqual(V.build_certificate(), self.certificate)

    def test_tensor_valuation_is_strictly_weaker_than_factor_valuation(self):
        result = V.verify(self.certificate)
        self.assertFalse(result["all_ungauged_discarded_factors_positive"])
        self.assertEqual(result["discarded_tensor_valuations"], [3, 3, 6, 4, 1, 3])
        self.assertEqual(result["unscaled_mixed_cycle_trace"], 1)
        self.assertTrue(result["all_ramified_gauged_discarded_factors_positive"])
        changed = copy.deepcopy(self.certificate)
        changed["factor_gauge_exponents"][4][0] += 1
        with self.assertRaisesRegex(ValueError, "does not preserve"):
            V.verify(changed)

    def test_changed_coefficient_or_nonpositive_tensor_is_rejected(self):
        changed = copy.deepcopy(self.certificate)
        changed["surviving_factors"][0][0][0][1] = str(
            -Fraction(changed["surviving_factors"][0][0][0][1]))
        with self.assertRaises(ValueError):
            V.coefficient_replay(changed)
        changed = copy.deepcopy(self.certificate)
        # The fifth discarded tensor has valuation one. Lowering every
        # coefficient of one factor by one moves its leading term to zero.
        for entry in changed["discarded_factors"][4][0]:
            entry[2] -= 1
        with self.assertRaisesRegex(ValueError, "nonpositive valuation"):
            V.coefficient_replay(changed)

    def test_metadata_and_physical_basis_mutations_are_rejected(self):
        for key in ("schema", "scope", "base_certificate_sha256"):
            changed = copy.deepcopy(self.certificate)
            changed[key] = "invalid"
            with self.assertRaises(ValueError):
                V.verify(changed)
        changed = copy.deepcopy(self.certificate)
        changed["weights"][0][0] += 1
        with self.assertRaisesRegex(ValueError, "Physical bases or weights differ"):
            V.verify(changed)

    def test_independent_finite_parameter_eighty_two_term_identity(self):
        # Evaluate first, then contract a dense flat tensor. This finite
        # control is separate from formal degree collection in the verifier.
        parameter = Fraction(-2)
        actual = [Fraction(0)] * 10000
        surviving_only = None
        for group in ("surviving_factors", "discarded_factors"):
            for term in self.certificate[group]:
                vectors = []
                for entries, width in zip(term, (20, 25, 20)):
                    row = [Fraction(0)] * width
                    for coordinate, coefficient, exponent in entries:
                        row[coordinate] = Fraction(coefficient) * parameter ** exponent
                    vectors.append(row)
                for a, x in enumerate(vectors[0]):
                    if not x:
                        continue
                    for b, y in enumerate(vectors[1]):
                        if not y:
                            continue
                        for c, z in enumerate(vectors[2]):
                            actual[(a * 25 + b) * 20 + c] += x * y * z
            if group == "surviving_factors":
                surviving_only = actual[:]
        expected = [Fraction(0)] * 10000
        for i in range(4):
            for j in range(5):
                for k in range(5):
                    expected[((5*i+j)*25+(5*j+k))*20+(4*k+i)] = 1
        self.assertEqual(actual, expected)
        self.assertNotEqual(surviving_only, expected)


if __name__ == "__main__":
    unittest.main()
