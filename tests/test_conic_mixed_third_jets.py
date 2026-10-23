"""Universal rational identity replay with coefficient and chart corruption controls."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-23-conic-third-jets'
RESULTS=ROOT/'results/conic-third-jets-2026-10-23'
spec=importlib.util.spec_from_file_location('mixed_third_jet_replay',PACKAGE/'verify_symbolic.py')
v=importlib.util.module_from_spec(spec); spec.loader.exec_module(v)


class MixedConicThirdJetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.witness=json.loads((RESULTS/'mixed-family.json').read_text())

    def test_all_parameter_identity_and_constant_leading_minors(self):
        report=v.verify(self.witness)
        self.assertEqual(report,json.loads((RESULTS/'mixed-family-verification.json').read_text()))
        self.assertEqual(report['leading_minor_determinants'],['1','1','-1'])
        self.assertEqual(report['normal_class'],'[1:d]')

    def test_changed_third_coefficient_is_rejected(self):
        bad=copy.deepcopy(self.witness)
        entry=bad['C'][3]['entries'][0]
        entry[2]=f'({entry[2]})+1'
        with self.assertRaisesRegex(ValueError,'symbolic order 3'):
            v.verify(bad)

    def test_coefficient_ring_and_predecessor_controls(self):
        for text in ('1/(a+1)','1/d**3',"__import__('os')"):
            with self.assertRaises(ValueError): v.expression(text)
        bad=copy.deepcopy(self.witness)
        bad['B'][1]['entries'][0][2]='1'
        with self.assertRaisesRegex(ValueError,'credited'):
            v.verify(bad)
        bad=copy.deepcopy(self.witness)
        bad['output_pivot_columns'].pop()
        with self.assertRaisesRegex(ValueError,'minor coordinates'):
            v.verify(bad)


if __name__=='__main__':
    unittest.main()
