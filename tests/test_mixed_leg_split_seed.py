import copy
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import shutil
import unittest


PACKAGE = Path(__file__).resolve().parents[1] / "research/ai/2026-10-23-mixed-leg-splits"
SPEC = importlib.util.spec_from_file_location("mixed_leg_split_verifier", PACKAGE / "verify.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class MixedLegSplitSeedTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = json.loads((PACKAGE / "certificate.json").read_text())
        cls.obstruction = json.loads((PACKAGE / "w_obstruction.json").read_text())

    def test_complete_exact_replay_and_regeneration(self):
        result = MODULE.verify(self.certificate, self.obstruction)
        self.assertEqual(MODULE.build_certificate(), self.certificate)
        split = result["mixed_border_seed"]
        self.assertEqual(split["expanded_exact_terms"], 89)
        self.assertEqual(split["surviving_border_terms"], 76)
        self.assertEqual((split["U_replacements"], split["W_replacements"]), (11, 2))
        self.assertEqual(split["all_constant_positions_checked"], 10000)
        self.assertEqual(split["constant_nonzero_coefficients"], 100)
        self.assertEqual(split["nonzero_coefficients_at_negative_degrees"], 0)
        self.assertEqual(split["nonzero_coefficients_at_positive_degrees"], 506)
        screens = split["old_weight_screens"]
        self.assertEqual(screens["direction_counts_U_V_W"], [65, 76, 56])
        self.assertEqual(screens["deleted_original_weights"], {"U": 37, "W": 8})
        self.assertEqual(screens["retained_original_weights"], {"U": 214, "W": 141})
        self.assertTrue(screens["both_previous_weight_inequalities_pass"])
        flat = result["static_W_obstruction"]
        self.assertEqual((flat["total_weight"], flat["rank_at_most_four_weight_cap"]), (152, 16))
        self.assertTrue(flat["static_nine_group_cover_excluded"])
        self.assertFalse(flat["exhaustive_enumeration_rerun_by_this_command"])
        for field in ("arbitrary_subsequent_flips_excluded", "singular_limits_excluded",
                      "general_Q64_maps_excluded"):
            self.assertFalse(flat[field])
        for field in ("rank_record_claimed", "search_optimum_claimed", "Q64_maps_constructed",
                      "improves_omega"):
            self.assertFalse(result[field])

    def test_cross_leg_destinations_use_original_factors(self):
        original = MODULE.V.load_seed()
        saved = copy.deepcopy(original)
        surviving, discarded = MODULE.mixed_seed(original)
        self.assertEqual(original, saved)
        self.assertEqual(len(discarded), 13)
        for source, destination, leg in ((24, 12, 0), (26, 13, 0), (12, 8, 2), (13, 8, 2)):
            self.assertEqual(surviving[source][leg],
                             [[-x for x in row] for row in original[destination][leg]])
        self.assertEqual(surviving[12][0], original[12][0])
        self.assertEqual(surviving[13][0], original[13][0])
        with self.assertRaisesRegex(ValueError, "Repeated changed source"):
            MODULE.mixed_seed(original, [[0, 12, 8, -1], [2, 12, 8, -1]])
        with self.assertRaisesRegex(ValueError, "Invalid mixed replacement"):
            MODULE.mixed_seed(original, [[1, 12, 8, -1]])

    def test_product_preserving_gauges_replay_the_entire_error(self):
        discarded = MODULE.V.parse_factors(self.certificate["discarded_factors"], 13)
        original = MODULE.collect_coefficients(discarded)
        ramified = {(3*degree, a, b, c): value
                    for (degree, a, b, c), value in original.items()}
        gauged = []
        for term, gauge in zip(discarded, self.certificate["factor_gauge_exponents"]):
            self.assertEqual(sum(gauge), 0)
            factors = [[(coordinate, value, 3*exponent + shift)
                        for coordinate, value, exponent in factor]
                       for factor, shift in zip(term, gauge)]
            self.assertTrue(all(min(e for _, _, e in factor) > 0 for factor in factors))
            gauged.append(factors)
        self.assertEqual(MODULE.collect_coefficients(gauged), ramified)
        changed = copy.deepcopy(self.certificate)
        changed["factor_gauge_exponents"][0][0] += 1
        with self.assertRaisesRegex(ValueError, "does not preserve"):
            MODULE.verify_split(changed)

    def test_schema_source_scope_and_physical_weight_controls(self):
        for key in ("schema", "claim_id", "scope", "source_pins", "dimensions", "replacements"):
            with self.subTest(field=key):
                changed = copy.deepcopy(self.certificate)
                changed[key] = "changed"
                with self.assertRaises(ValueError):
                    MODULE.verify_split(changed)
        changed = copy.deepcopy(self.certificate)
        changed["weights"][0][0] = True
        with self.assertRaisesRegex(ValueError, "Invalid physical weights"):
            MODULE.verify_split(changed)
        changed = copy.deepcopy(self.certificate)
        changed["weights"][0][0] += 1
        with self.assertRaisesRegex(ValueError, "physical weights differ"):
            MODULE.verify_split(changed)

    def test_coefficient_and_nonpositive_valuation_controls(self):
        changed = copy.deepcopy(self.certificate)
        entry = changed["surviving_factors"][0][0][0]
        entry[1] = str(Fraction(entry[1]) + 7)
        with self.assertRaises(ValueError):
            MODULE.coefficient_replay(changed)
        changed = copy.deepcopy(self.certificate)
        decrease = sum(changed["minimum_factor_valuations"][0])
        for entry in changed["discarded_factors"][0][0]:
            entry[2] -= decrease
        with self.assertRaisesRegex(ValueError, "nonpositive valuation"):
            MODULE.coefficient_replay(changed)

    def test_static_W_certificate_mutations(self):
        for key in ("schema", "claim_id", "scope", "source_pins", "total_weight"):
            with self.subTest(field=key):
                changed = copy.deepcopy(self.obstruction)
                changed[key] = "changed"
                with self.assertRaises(ValueError):
                    MODULE.verify_w_obstruction(changed)
        for field in ("classes", "vectors"):
            with self.subTest(field=field):
                changed = copy.deepcopy(self.obstruction)
                changed[field][0][0] += 1
                with self.assertRaisesRegex(ValueError, "displayed mixed seed"):
                    MODULE.verify_w_obstruction(changed)
        changed = copy.deepcopy(self.obstruction)
        changed["weights"][0] -= 1
        with self.assertRaisesRegex(ValueError, "weights differ"):
            MODULE.verify_w_obstruction(changed)
        changed = copy.deepcopy(self.obstruction)
        changed["enumeration"]["four_subsets"] -= 1
        with self.assertRaisesRegex(ValueError, "complete coverage"):
            MODULE.verify_w_obstruction(changed)
        changed = copy.deepcopy(self.obstruction)
        changed["enumeration"]["flat_weight_histogram"]["16"] -= 1
        with self.assertRaisesRegex(ValueError, "histograms disagree"):
            MODULE.verify_w_obstruction(changed)

    @unittest.skipUnless(shutil.which("cc") or shutil.which("gcc") or shutil.which("clang"),
                         "A C99 compiler is needed for complete weighted enumeration")
    def test_complete_static_W_enumeration(self):
        result = MODULE.verify_w_obstruction(self.obstruction, full=True)
        self.assertTrue(result["exhaustive_enumeration_rerun_by_this_command"])
        self.assertEqual(result["stored_four_subsets"], 367290)
        self.assertEqual(result["stored_independent_four_subsets"], 366288)
        self.assertEqual(result["minimum_rank_at_most_four_groups_by_weight"], 10)

    def test_independent_dense_identity_at_nonzero_parameter(self):
        # Direct evaluation avoids the maintained parser/contraction backend.
        parameter = Fraction(-1, 2)
        def evaluate(terms):
            output = [Fraction(0)] * 10000
            for term in terms:
                factors = []
                for entries, size in zip(term, (20, 25, 20)):
                    row = [Fraction(0)] * size
                    for coordinate, coefficient, exponent in entries:
                        row[coordinate] += Fraction(coefficient) * parameter**exponent
                    factors.append([(i, value) for i, value in enumerate(row) if value])
                for a, x in factors[0]:
                    for b, y in factors[1]:
                        for c, z in factors[2]:
                            output[(a*25 + b)*20 + c] += x*y*z
            return output
        survivor = evaluate(self.certificate["surviving_factors"])
        error = evaluate(self.certificate["discarded_factors"])
        target = [Fraction(0)] * 10000
        for i in range(4):
            for j in range(5):
                for k in range(5):
                    target[((5*i+j)*25 + 5*j+k)*20 + 4*k+i] = 1
        self.assertEqual([x+y for x, y in zip(survivor, error)], target)
        self.assertNotEqual(survivor, target)


if __name__ == "__main__":
    unittest.main()
