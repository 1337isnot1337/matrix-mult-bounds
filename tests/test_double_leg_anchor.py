"""Two-stage mixed-leg exact contractions and anchored four-flat obstruction."""
import importlib.util
import json
from pathlib import Path
import shutil
import unittest

ROOT=Path(__file__).resolve().parents[1]
DIR=ROOT/"research/ai/2026-10-23-double-leg-anchor"
spec=importlib.util.spec_from_file_location("double_leg_anchor_verifier",DIR/"verify.py")
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class DoubleLegAnchorTest(unittest.TestCase):
    def test_certificate_and_source_scopes(self):
        d=json.loads((DIR/"certificate.json").read_text())
        self.assertEqual(d["claim_id"],module.CLAIM)
        self.assertEqual(d["source_sha256"],module.SOURCE_SHA)
        self.assertEqual(d["basis_sha256"],module.BASIS_SHA)
        self.assertEqual({k:[list(v) for v in values] for k,values in module.VARIANTS.items()},d["variants"])
        self.assertEqual(d["surviving_positive_coefficient_counts"],module.EXPECTED_POSITIVE)
        self.assertEqual(d["anchor_maximum_flat_weight_mod101"],15)
        self.assertFalse(d["improves_omega"])

    def test_complete_laurent_for_all_four_variants(self):
        data=module.verify(False)
        self.assertEqual(set(data["variants"]),set(module.VARIANTS))
        for entry in data["variants"].values():
            self.assertEqual(entry["surviving_terms"],76)
            self.assertEqual(entry["discarded_terms"],15)
            self.assertEqual(entry["direction_counts_UVW"],[65,76,54])
            self.assertEqual(entry["retained_mixed_W_weight"],144)
            self.assertEqual(entry["W35_anchor_index"],28)
            self.assertEqual(len(entry["minima"]),15)
            self.assertTrue(all(sum(row)>0 for row in entry["minima"]))

    @unittest.skipUnless(shutil.which("cc") or shutil.which("gcc") or shutil.which("clang"),
                         "C99 compiler unavailable")
    def test_exhaustive_anchor_census(self):
        data=module.verify(True)
        for entry in data["variants"].values():
            self.assertEqual(entry["W35_anchor_bound"]["triples_checked"],23426)
            self.assertEqual(entry["W35_anchor_bound"]["rank_four_triples"],23352)
            self.assertEqual(entry["W35_anchor_bound"]["maximum_weight_in_anchor_flat"],15)

if __name__=="__main__":
    unittest.main()
