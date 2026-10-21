"""Check the new parameterization without loading a discovery solver."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'research/ai/2026-10-20-group-potentials'))
from affine_fiber_certificate import check
from verify_stream_reports import verify_report


class AffineFiberTests(unittest.TestCase):
    def test_known_pair_model_has_all_343_normal_triples(self):
        report=json.loads((ROOT/'results/group-potentials-2026-10-20/octal-global-membership0.json').read_text())
        receipt=check(report['base_columns'],report['cuts'][0]['sets'])
        self.assertEqual(receipt['normal_fiber_triples_checked'],343)
        self.assertEqual(receipt['pair_map_sizes'],[361,361,361])
        self.assertEqual(receipt['varying_three_point_planes'],0)
        self.assertEqual(receipt['changed_short_directions'],0)

    def test_dependent_bases_and_bad_fibers_are_rejected(self):
        report=json.loads((ROOT/'results/group-potentials-2026-10-20/octal-global-membership0.json').read_text())
        sets=report['cuts'][0]['sets'];base=report['base_columns']
        wrong=base[:];wrong[1]=wrong[0]
        with self.assertRaises(ValueError):check(wrong,sets)
        wrong_sets=copy.deepcopy(sets);wrong_sets[0][0]=wrong_sets[0][1]
        with self.assertRaises(ValueError):check(base,wrong_sets)

    def test_native_solver_candidates_and_circuits_replay(self):
        report=json.loads((ROOT/'results/group-potentials-2026-10-20/octal-variable-planes0-native.json').read_text())
        verification=verify_report(report)
        self.assertEqual(verification['exact_cuts_replayed'],4)
        receipts=[check(report['base_columns'],cut['sets']) for cut in report['cuts']]
        self.assertTrue(all(r['normal_fiber_triples_checked']==343 for r in receipts))
        self.assertTrue(all(r['pair_map_sizes']==[361,361,361] for r in receipts))
        self.assertEqual(max(r['varying_three_point_planes'] for r in receipts),0)
        self.assertEqual(max(r['changed_short_directions'] for r in receipts),2)


if __name__=='__main__':unittest.main()
