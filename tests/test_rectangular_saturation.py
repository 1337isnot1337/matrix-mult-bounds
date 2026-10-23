import importlib.util
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'research/ai/2026-10-21-rectangular-direct-sums/saturation.py'
spec=importlib.util.spec_from_file_location('rectangular_saturation',P)
s=importlib.util.module_from_spec(spec);spec.loader.exec_module(s)

class SaturationTests(unittest.TestCase):
    def test_all_coordinate_witnesses(self):
        data=json.loads((ROOT/'results/rectangular-direct-sums-20261021/hankel-coordinate-certificates.json').read_text())
        self.assertEqual([s.verify(x)['coordinate_spaces_certified'] for x in data],[6435,6435])

    def test_corruption_rejected(self):
        data=json.loads((ROOT/'results/rectangular-direct-sums-20261021/hankel-coordinate-certificates.json').read_text())[0]
        data['certificates'][0][1]=0
        with self.assertRaises(AssertionError):s.verify(data)

    def test_first_candidates_closed(self):
        self.assertIsNotNone(s.exclusion(7,9,[(27,27,28),(6,6,2)],[765,768,768]))
        self.assertIsNotNone(s.exclusion(8,8,[(27,27,27),(7,7,7)],[778,778,778]))

    def test_constructed_controls_not_excluded(self):
        self.assertIsNone(s.exclusion(8,8,[(15,15,15)],[225,225,225]))
        self.assertIsNone(s.exclusion(7,9,[(6,6,6)],[36,36,36]))
        self.assertIsNone(s.exclusion(5,5,[(8,8,8),(3,3,3)],[73,73,73]))

    def test_all_recorded_survivors_closed(self):
        records=json.loads((ROOT/'results/rectangular-direct-sums-20261021/frontier.json').read_text())
        refined=s.refine(records)
        self.assertEqual([(r['a'],r['b'],len(r['excluded']),len(r['remaining'])) for r in refined],[(7,9,19,0),(8,8,552,0)])
        saved=json.loads((ROOT/'results/rectangular-direct-sums-20261021/saturation.json').read_text())
        self.assertEqual(refined,saved['target_refinement'])

    def test_bareiss_known_values(self):
        self.assertEqual(s.determinant([[0,2],[3,4]]),-6)
        self.assertEqual(s.determinant([[1,2,3],[4,5,6],[7,8,10]]),-3)
        self.assertEqual(s.determinant([[1,2],[2,4]]),0)

if __name__=='__main__':unittest.main()
