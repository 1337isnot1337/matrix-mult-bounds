"""Complete Laurent and specialized spin-extension checks, using stdlib only."""

import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = ROOT / "research/ai/2026-10-20-anisotropic-constructions"


def load(name):
    spec = importlib.util.spec_from_file_location(name, DIRECTORY / (name+".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CORE = load("parity_structure_spin_w34_laurent")
EXTENSION = load("parity_structure_spin_w34_laurent_extension")


class CoupledLaurentSpinTests(unittest.TestCase):
    def test_complete_laurent_source_and_response_minor(self):
        report = CORE.verify()
        self.assertEqual(report["source_terms_checked"], 262144)
        self.assertEqual(report["nonzero_constant_target_coefficients"], 243)
        self.assertTrue(report["negative_power_coefficients_zero"])
        self.assertTrue(report["positive_power_coefficients_zero"])
        self.assertTrue(report["endpoint_response_identically_zero"])
        self.assertEqual(report["polar_map_rank_exact"], 2)
        self.assertEqual(report["specialized_response_rank_exact"], 191)
        self.assertFalse(report["new_exponent_established"])

    def test_both_compositions_and_actual_ordinary_specialization(self):
        degeneration = json.loads(EXTENSION.DEGENERATION.read_text())
        two_channel = json.loads(EXTENSION.TWO_CHANNEL.read_text())
        ordinary = json.loads(EXTENSION.ORDINARY.read_text())
        first = EXTENSION.verify(degeneration)
        second = EXTENSION.verify(two_channel, ordinary)
        self.assertEqual(first["nonzero_constant_coefficients"], 267)
        self.assertEqual(first["positive_degree_one_coefficients"], 12)
        self.assertFalse(first["exact_for_every_nonzero_parameter"])
        self.assertEqual(second["nonzero_constant_coefficients"], 267)
        self.assertEqual(second["positive_degree_one_coefficients"], 0)
        self.assertTrue(second["exact_for_every_nonzero_parameter"])
        self.assertTrue(second["ordinary_t1_restriction_checked"])
        self.assertEqual(second["filled_middle_channels"], [0, 16])

    def test_parameter_preserving_pole_tamper_is_rejected(self):
        data = json.loads(CORE.MAPS.read_text())
        before, _ = CORE.parse(data)
        row, column, value = data["maps"]["Y"]["-1"]["entries"][0]
        data["maps"]["Y"]["-1"]["entries"][0][2] += value
        # Denominators are 56 and 672. This leaves the ordinary map
        # at t=1 unchanged, but changes its Laurent coefficients.
        correction = -12*value
        entries = data["maps"]["Y"]["0"]["entries"]
        for entry in entries:
            if entry[:2] == [row, column]:
                entry[2] += correction
                if not entry[2]:
                    entries.remove(entry)
                break
        else:
            entries.append([row, column, correction])
            entries.sort()
        after, _ = CORE.parse(data)
        self.assertEqual(CORE.specialize_one(before), CORE.specialize_one(after))
        with self.assertRaisesRegex(ArithmeticError, "complete Laurent coefficient identity"):
            CORE.verify(data, check_response=False)

    def test_nonzero_ordinary_map_tamper_is_rejected(self):
        data = json.loads(EXTENSION.TWO_CHANNEL.read_text())
        ordinary = json.loads(EXTENSION.ORDINARY.read_text())
        ordinary["maps"]["Y"]["entries"][0][2] *= 2
        with self.assertRaises(ArithmeticError):
            EXTENSION.verify(data, ordinary)


if __name__ == "__main__":
    unittest.main()
