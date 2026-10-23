"""Complete polynomial verification and corruption controls on the pure fiber."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-23-conic-pure-criterion'
RESULTS=ROOT/'results/conic-pure-criterion-2026-10-23'
spec=importlib.util.spec_from_file_location('pure_conic_replay',PACKAGE/'verify.py')
v=importlib.util.module_from_spec(spec); spec.loader.exec_module(v)


class PureConicCurveTests(unittest.TestCase):
    def test_entire_polynomial_curve_and_export_replay(self):
        report=v.verify()
        self.assertEqual(report,json.loads((RESULTS/'verification.json').read_text()))
        self.assertEqual(report,v.verify(json.loads((RESULTS/'curve.json').read_text())))
        self.assertTrue(report['exact_polynomial_incidence_curve'])

    def test_changed_quadratic_coefficient_is_rejected(self):
        bad=v.build()
        bad['B'][2]['entries'][0][2]+='+1'
        with self.assertRaisesRegex(ValueError,'polynomial coefficient'):
            v.verify(bad)

    def test_chart_and_first_jet_corruption_are_rejected(self):
        bad=v.build(); bad['B'][1]['entries'][0][2]='1'
        with self.assertRaisesRegex(ValueError,'credited'):
            v.verify(bad)
        bad=v.build(); bad['B'][2]['entries'][0][2]='a/d'
        with self.assertRaisesRegex(ValueError,'polynomials in a,b'):
            v.verify(bad)
        bad=v.build(); bad['C'][2]['entries']=[[0,0,'1']]
        with self.assertRaisesRegex(ValueError,'polynomial degrees'):
            v.verify(bad)


if __name__=='__main__':
    unittest.main()
