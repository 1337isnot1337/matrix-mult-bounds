"""A proved-impossible frame must not start an optional SAT search."""
import builtins
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-21-semisimple-koszul'
sys.path.insert(0,str(PACKAGE))
import sl2_f8_frames as frames
import subgroup_preflight as preflight
import subgroup_search as search


class F8SubgroupPreflightTests(unittest.TestCase):
    def test_default_frame_replays_exact_exclusion_without_solver_imports(self):
        original_import=builtins.__import__
        def no_solver(name,*args,**kwargs):
            if name.startswith('pysat'):
                raise AssertionError('the excluded frame tried to import its SAT solver')
            return original_import(name,*args,**kwargs)
        with tempfile.TemporaryDirectory() as directory:
            output=Path(directory)/'report.json'
            with patch('builtins.__import__',side_effect=no_solver), patch('builtins.print'):
                report=search.run(0,output)
            self.assertEqual(json.loads(output.read_text()),report)
        self.assertEqual(report['status'],'excluded-by-subgroup-ideal')
        self.assertEqual(report['models'],0)
        self.assertTrue(frames.verify_search(report)['analytic_exclusion_verified'])
        self.assertEqual(report['exclusion']['verification']['ideal_dimension_upper_bound'],244)
        self.assertEqual(report['exclusion']['verification']['other_pair_product'],450)
        self.assertFalse(report['unsat_proof_checked'])

    def test_positive_control_is_not_excluded_by_the_projection(self):
        self.assertIsNone(preflight.exclusion_for([18,1,1],frames.subgroup()))

    def test_bad_projection_rank_and_nonexcluding_shapes_are_rejected(self):
        H=frames.subgroup();proof=preflight.exclusion_for([18,18,25],H)
        bad=copy.deepcopy(proof);bad['central_projection']=['0']*9
        with self.assertRaises(ValueError):preflight.verify_exclusion(bad,[18,18,25],H)
        bad=copy.deepcopy(proof);bad['ideal_dimension_upper_bound']=243
        with self.assertRaises(ValueError):preflight.verify_exclusion(bad,[18,18,25],H)
        with self.assertRaises(ValueError):preflight.verify_exclusion(proof,[18,1,1],H)
        with self.assertRaises(ValueError):preflight.verify_exclusion(proof,[9,18,25],H)

    def test_unbacked_exclusion_status_is_rejected_and_history_still_replays(self):
        path=ROOT/'results/semisimple-koszul-2026-10-21/sl2-f8-subgroup-180s.json'
        historical=json.loads(path.read_text())
        self.assertFalse(frames.verify_search(historical).get('analytic_exclusion_verified',False))
        historical['status']='excluded-by-subgroup-ideal'
        with self.assertRaises(ValueError):frames.verify_search(historical)


if __name__=='__main__':unittest.main()
