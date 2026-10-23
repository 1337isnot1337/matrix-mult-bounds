"""Full integer control replay and honest terminal search-report semantics."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-23-sl2-f8-native-all-cuts'
spec=importlib.util.spec_from_file_location('native_f8_full_source',PACKAGE/'native_search.py')
native=importlib.util.module_from_spec(spec);spec.loader.exec_module(native)


class NativeF8AllCutTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.control=json.loads((ROOT/'results/sl2-f8-native-all-cuts-2026-10-23/control.json').read_text())

    def test_exact_positive_control_replays_every_supported_term(self):
        result=native.verify_report(self.control)
        self.assertTrue(result['exact_witness_replayed'])
        self.assertEqual(self.control['witness']['verification']['intended_terms'],18)
        self.assertEqual(self.control['witness']['verification']['extra_supported_terms'],0)
        self.assertEqual(self.control['minimal_subgroup_cuts_per_leg'],[0,0,0])
        self.assertFalse(result['all_coordinate_targets_excluded'])

    def test_repeated_points_and_false_receipts_are_rejected(self):
        bad=copy.deepcopy(self.control);bad['witness']['sets'][0][1]=bad['witness']['sets'][0][0]
        with self.assertRaises(ValueError):native.verify_report(bad)
        bad=copy.deepcopy(self.control);bad['witness']['verification']['intended_terms']=19
        with self.assertRaises(ValueError):native.verify_report(bad)
        bad=copy.deepcopy(self.control);bad['witness']['potentials'].pop()
        with self.assertRaises(ValueError):native.verify_report(bad)

    def test_timeout_and_solver_unsat_are_not_nonexistence_certificates(self):
        bad=copy.deepcopy(self.control);bad['models']=0;bad['witness']=None
        for status in ['time-limit','solver-reported UNSAT; no proof trace']:
            bad['status']=status;result=native.verify_report(bad)
            self.assertFalse(result['exact_witness_replayed'])
            self.assertFalse(result['unsat_proof_checked'])
            self.assertFalse(result['all_coordinate_targets_excluded'])
        bad['unsat_proof_checked']=True
        with self.assertRaises(ValueError):native.verify_report(bad)

    def test_incomplete_or_miscounted_terminal_reports_are_rejected(self):
        bad=copy.deepcopy(self.control);bad['witness']=None
        with self.assertRaises(ValueError):native.verify_report(bad)
        bad=copy.deepcopy(self.control);bad['status']='running'
        with self.assertRaises(ValueError):native.verify_report(bad)
        bad=copy.deepcopy(self.control);bad['models']=2
        with self.assertRaises(ValueError):native.verify_report(bad)
        bad=copy.deepcopy(self.control);bad['status']='model-limit';bad['witness']=None;bad['models']=0
        with self.assertRaises(ValueError):native.verify_report(bad)


if __name__=='__main__':unittest.main()
