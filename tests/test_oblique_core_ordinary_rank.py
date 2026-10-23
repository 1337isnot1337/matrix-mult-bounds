"""Check the explicit inputs to the isolated core's ordinary-rank proof."""

import copy
import importlib.util
import itertools
import json
from pathlib import Path
import tempfile
import unittest


PACKAGE = (Path(__file__).resolve().parents[1]
           / "research/ai/2026-10-23-oblique-border-repair")
SPEC = importlib.util.spec_from_file_location("oblique_core_ordinary_rank",
                                            PACKAGE / "ordinary_rank.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ObliqueCoreOrdinaryRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = MODULE.check()

    def test_complete_saved_certificate(self):
        self.assertEqual(MODULE.verify_saved(PACKAGE / "ordinary-rank-certificate.json"),
                         self.report)
        self.assertEqual(self.report["ordinary_rank_upper_bound"], 7)
        self.assertEqual(self.report["ordinary_rank_lower_bound_from_written_proof"], 7)
        self.assertEqual(self.report["tensor_coordinates_compared"], 75)
        self.assertFalse(self.report["whole_residual_rank_lower_bound_claimed"])
        self.assertFalse(self.report["independent_mathematical_review"])

    def test_same_core_as_the_saved_border_degeneration(self):
        witness = json.loads((PACKAGE / "witness.json").read_text())
        leading = {}
        for term in witness["core"]["terms"]:
            for aa, bb, cc in itertools.product(term["a"], term["b"], term["c"]):
                if aa[1] + bb[1] + cc[1] == 2:
                    key = aa[0], bb[0], cc[0]
                    leading[key] = leading.get(key, 0) + aa[2] * bb[2] * cc[2]
        self.assertEqual({key: value for key, value in leading.items() if value},
                         MODULE.canonical_core())
        ordinary = MODULE.add(*(MODULE.rank_one(*term)
                                for term in MODULE.ordinary_terms()))
        self.assertEqual(ordinary, MODULE.canonical_core())

    def test_polynomial_kernels_and_concision(self):
        self.assertTrue(self.report["right_kernel_identity"])
        self.assertTrue(self.report["left_kernel_identity"])
        self.assertEqual(self.report["generic_slice_minor"], "u^2*v^2")
        identity = [[int(i == j) for j in range(5)] for i in range(5)]
        self.assertEqual(self.report["second_leg_concision_minor"], identity)
        self.assertEqual(self.report["third_leg_concision_minor"], identity)

    def test_both_support_pattern_contradictions(self):
        self.assertEqual(self.report["graph_map_basis_functional_values"], [0] * 12)
        self.assertEqual(self.report["actual_mixed_block_functional_value"], 1)
        self.assertEqual(self.report["shared_w_residual_minor"],
                         [[int(i == j) for j in range(3)] for i in range(3)])

    def test_changed_ordinary_product_or_core_is_rejected(self):
        terms = MODULE.ordinary_terms()
        terms[-1][0][2] = -1
        with self.assertRaises(ArithmeticError):
            MODULE.check(terms=terms)
        core = MODULE.canonical_core()
        core[(2, 0, 2)] = 2
        with self.assertRaises(ArithmeticError):
            MODULE.check(core=core)

    def test_false_saved_minor_is_rejected(self):
        report = copy.deepcopy(self.report)
        report["shared_w_residual_minor"][2][2] = 0
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "false-certificate.json"
            path.write_text(json.dumps(report))
            with self.assertRaises(ArithmeticError):
                MODULE.verify_saved(path)


if __name__ == "__main__":
    unittest.main()
