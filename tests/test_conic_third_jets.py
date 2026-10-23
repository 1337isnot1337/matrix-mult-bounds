"""Independent original-source replay and corruption controls for a rational jet."""
import copy
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-23-conic-third-jets'
RESULTS = ROOT/'results/conic-third-jets-2026-10-23'
spec = importlib.util.spec_from_file_location('conic_third_replay',PACKAGE/'verify.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class ConicThirdJetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.witness = json.loads((RESULTS/'third-jet-pilot.json').read_text())

    def test_original_source_replay(self):
        report = v.verify(self.witness)
        self.assertEqual(report,json.loads((RESULTS/'verification.json').read_text()))
        self.assertEqual(report['jet_order'],3)
        self.assertEqual(report['first_nonboundary_entries'],128)

    def test_literal_source_matches_predecessor_convention(self):
        path = ROOT/'research/ai/2026-10-21-quantum-extension-spaces/extensions.py'
        spec = importlib.util.spec_from_file_location('third_jet_source_control',path)
        source = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(source)
        self.assertEqual(len(v.source_terms()),4096)
        self.assertEqual(set(v.source_terms()),set(source.TERMS))

    def test_constant_and_first_coefficients_are_the_credited_specialization(self):
        path = ROOT/'research/ai/2026-10-21-conic-second-jets/verify.py'
        spec = importlib.util.spec_from_file_location('third_jet_first_control',path)
        prior = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(prior)
        old = prior.read('witnesses')['cubic_component_two_jet']
        new = self.witness['reconstructed_third_jet']
        parameters = {prior.m.A:1,prior.m.B:2,prior.m.D:1}
        for key in ('B','C'):
            for k in (0,1):
                expected = prior.m.decode(old[key][k]).subs(parameters)
                self.assertEqual(v.decode(new[key][k],(14,112)),{
                    index:Fraction(str(value)) for index,value in expected.todok().items()})

    def test_changed_third_map_and_kernel_correction_are_rejected(self):
        for key in ('B','source_row_corrections'):
            bad = copy.deepcopy(self.witness)
            entry = bad['reconstructed_third_jet'][key][-1]['entries'][0]
            entry[2] = str(Fraction(entry[2])+1)
            with self.assertRaisesRegex(ValueError,'order 3'):
                v.verify(bad)

    def test_rank_and_parameter_corruption_are_rejected(self):
        bad = copy.deepcopy(self.witness)
        bad['reconstructed_third_jet']['B'][0]['entries'] = []
        with self.assertRaisesRegex(ValueError,'leading ranks'):
            v.verify(bad)
        bad = copy.deepcopy(self.witness)
        bad['parameters']['d'] = '2'
        with self.assertRaisesRegex(ValueError,'rational point'):
            v.verify(bad)


if __name__ == '__main__':
    unittest.main()
