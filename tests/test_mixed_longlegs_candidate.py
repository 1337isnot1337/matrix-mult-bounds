"""Exact controls for the frozen mixed-long-leg necessary-condition profile."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest


ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/"research/ai/2026-10-23-mixed-longlegs-candidate"
SPEC=importlib.util.spec_from_file_location("mixed_longlegs_candidate",PACKAGE/"verify.py")
VERIFY=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


class MixedLonglegsCandidateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report,cls.certificates=VERIFY.report()

    def test_saved_exact_report_and_frozen_input(self):
        saved=json.loads((ROOT/"results/mixed-longlegs-candidate-2026-10-23/verification.json").read_text())
        self.assertEqual(saved,self.report)
        self.assertEqual(self.report["candidate_sha256"],
            "c53abefde0cb5d5e2e816f96ae6c257ee843f59e6c28d13a6ae1994de9ab88f3")
        self.assertFalse(self.report["degeneration_constructed"])
        self.assertFalse(self.report["improved_exponent_established"])

    def test_forest_certificates_against_independent_rational_elimination(self):
        cases=[VERIFY.intrinsic_rows("S"),VERIFY.pair_rows("F2","M2"),
               VERIFY.pair_rows("O33","O42",True),VERIFY.intrinsic_rows("O33",True)]
        for n,rows in cases:
            self.assertEqual(VERIFY.graph_certificate(n,rows)["rank"],
                             VERIFY.rational_rank(rows))

    def test_incidence_acceptance_rejects_incorrect_signs(self):
        with self.assertRaises(ValueError):
            VERIFY.graph_certificate(2,[{0:1,1:1}])
        with self.assertRaises(ValueError):
            VERIFY.graph_certificate(2,[{0:2}])

    def test_all_shared_degrees_and_both_nonshared_orientations(self):
        shared=self.report["shared_A_B_star_wedge_convention"]
        self.assertEqual(shared["source"],[100,440,720,520,140])
        self.assertEqual(shared["target"],shared["source"])
        self.assertEqual(self.report["degree_one_literal_matrix_count"],44)
        for leg,source,target in (("B",12735,12587),("C",14000,13572)):
            actual=self.report["degree_one_nonshared_koszul"][leg]
            self.assertEqual((actual["source_rank"],actual["target_rank"]),(source,target))
            self.assertGreater(source,target)

    def test_exact_score_and_simultaneous_source_marginals(self):
        score=self.report["exact_score_comparison"]
        self.assertEqual(score["strict_cubed_gap"],"1050371253/4913")
        margins=self.report["source_simultaneous_uniform_marginals"]
        self.assertEqual((margins["literal_weights"],margins["marginal_coordinates"]),(500,245))
        self.assertEqual((margins["first_each"],margins["second_each"],margins["third_each"]),
                         ("28","7/5","1"))

    def test_source_tail_boundaries_and_copywise_limitation(self):
        tails=self.report["source_output_leg_maximal_windows"]
        self.assertEqual(tails["literal_matrix_count"],32)
        self.assertEqual(tails["candidate_automatic_C_degrees"],[[0,4],[40,139]])
        interior=[row for row in tails["controls"]
                  if (row["a"],row["b"],row["copies"],row["degree"])==(3,2,2,3)]
        self.assertEqual([(row["rows"],row["columns"],row["rank"]) for row in interior],
                         [(210,224,189)])
        allocation=self.report["copywise_dimension_control"]
        self.assertEqual(allocation["bounded_integer_tuples"],576)
        self.assertEqual(allocation["per_copy_solutions"],[[2,0,0,0,1]])
        self.assertFalse(allocation["arbitrary_mixing_excluded"])


if __name__=="__main__":
    unittest.main()

