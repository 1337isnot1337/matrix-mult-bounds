"""Independent finite controls for the written formal channel argument."""
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "laurent_channel_barrier",
    ROOT / "research/ai/2026-10-23-laurent-channel-barrier/verify.py")
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class LaurentChannelBarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = verify.certificate()

    def test_exact_replay_matches_saved_report(self):
        saved = json.loads((ROOT / "results/laurent-channel-barrier-2026-10-23/verification.json").read_text())
        self.assertEqual(self.report, saved)

    def test_moving_kernel_and_actual_pole_cancellation(self):
        f = self.report["formal_controls"]
        self.assertEqual(f["moving_subspace_dimension"], 2)
        self.assertEqual(f["auxiliary_first_flattening_rank"], 2)
        self.assertTrue(f["genuine_poles_cancel_in_complete_total"])
        self.assertTrue(f["auxiliary_rank_one_truncation_breaks_channel_hypothesis"])
        self.assertEqual(f["primitive_vector"]["nonzero_constant"], [0, 1, 0])

    def test_raw_constant_and_generic_rank_are_distinguished(self):
        f = self.report["formal_controls"]
        self.assertEqual(f["raw_constant_rank_increase"],
                         {"generic_rank": 1, "constant_rank": 2})
        self.assertEqual(f["leading_rank_only_countercontrol"],
                         {"generic_rank": 2, "leading_rank": 1})

    def test_near_full_first_dimension_loss_is_counted(self):
        row = next(x for x in self.report["finite_cases"] if x["name"] == "moving_window_near_full")
        self.assertEqual(row["good_source_slices"], 25)
        self.assertEqual(row["kernel_dimension_lower_bound"], 49 - 64 + 25)
        self.assertEqual(row["exception_count_lower_bound"], 10)

    def test_full_coefficients_and_two_exact_fields(self):
        for row in self.report["finite_cases"]:
            self.assertGreater(row["exact_laurent_coefficient_checks"], 0)
            self.assertGreater(row["negative_power_coefficients_retained"], 0)
            self.assertLess(row["generic_channel_rank_cap"], row["h"])
            self.assertEqual({x["field_prime"] for x in row["finite_specializations"]}, {3, 101})
            for item in row["finite_specializations"]:
                self.assertGreaterEqual(item["complete_residual_flattening_rank"],
                                        row["kernel_dimension_lower_bound"])

    def test_boundary_cropping_is_not_treated_as_a_good_slice(self):
        case = verify.CASES[-1]
        ps, qs = verify.good_indices(case)
        self.assertNotIn(0, ps)
        self.assertNotIn(0, qs)
        self.assertNotEqual(verify.native_slice(case, 0, 0),
                            verify.factored_slice(case, 0, 0))

    def test_changed_pole_coefficient_fails_literal_identity(self):
        case = verify.CASES[1]
        ps, qs = verify.good_indices(case)
        direct = verify.native_slice(case, ps[0], qs[0])
        changed = verify.factored_slice(case, ps[0], qs[0])
        changed[0, 0] = verify.add(changed.get((0, 0), {}), verify.mono(t=-7))
        self.assertNotEqual(direct, changed)


if __name__ == "__main__":
    unittest.main()
