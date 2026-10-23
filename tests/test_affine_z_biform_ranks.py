"""Regression for the exact affine-in-z biform rank family."""
import importlib.util
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
SCRIPT=ROOT/'research/ai/2026-10-23-affine-z-biform-ranks/verify.py'

class AffineZBiformRankTests(unittest.TestCase):
    def test_all_finite_controls(self):
        spec=importlib.util.spec_from_file_location('affine_z_rank_verify',SCRIPT)
        mod=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        report=mod.verify()
        self.assertEqual(report['status'],'pass')
        self.assertEqual(report['seed'],20261023)
        self.assertEqual(report['exhaustive'],3265)
        self.assertEqual(report['seeded'],2992)
        self.assertEqual(report['a_gt_b'],300)
        self.assertEqual(report['spectrum'],570)
        self.assertTrue(mod.check(3,7,[1],[0,0,1],101))
        self.assertTrue(mod.check(3,4,[1,1],[1,0,1],101))
        self.assertTrue(mod.check(5,2,[1],[0,0,0,0,1],101))

if __name__=='__main__':unittest.main()
