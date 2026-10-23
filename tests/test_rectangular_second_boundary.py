import importlib.util
from pathlib import Path
import unittest
P=Path(__file__).resolve().parents[1]/'research/ai/2026-10-21-rectangular-direct-sums/second_boundary.py'
spec=importlib.util.spec_from_file_location('second_boundary',P)
s=importlib.util.module_from_spec(spec);spec.loader.exec_module(s)
class SecondBoundaryTests(unittest.TestCase):
    def test_exact_relations_and_nonreduced_jets(self):
        for r in range(3,9):
            row=s.verify_rank(r)
            self.assertEqual(row['full_jet_rank'],3*r-2)
            self.assertGreater(row['nonreduced_partitions_checked'],0)
    def test_symmetric_pencils(self):
        self.assertGreater(s.verify_pencils(),0)
    def test_candidate_and_scope(self):
        self.assertIsNotNone(s.exclusion(7,10,[(30,30,30),(4,4,5)],[916,920,920]))
        self.assertIsNone(s.exclusion(8,9,[(30,30,30),(3,3,3)],[909,909,909]))
        self.assertIsNone(s.exclusion(8,8,[(27,27,27),(7,7,7)],[778,778,778]))
if __name__=='__main__':unittest.main()
