"""Exact finite hypotheses of the two-family all-weight theorem."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import unittest


ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/'research/ai/2026-10-21-nearfull-quantum/verify.py'
SPEC=importlib.util.spec_from_file_location('test_nearfull_certificate',PATH)
CERT=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(CERT)


class NearFullQuantumTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with contextlib.redirect_stdout(io.StringIO()):
            cls.report,cls.data=CERT.report(True)

    def test_complete_regeneration(self):
        for data in self.data:
            saved=json.loads((ROOT/f"results/nearfull-quantum-2026-10-21/N{data['N']}-m{data['m']}-family.json").read_text())
            for key in ['maps','local_records','coefficients','tensor','flattening_ranks','coordinate_weights']:
                self.assertEqual(json.loads(json.dumps(data[key])),saved[key])
            self.assertEqual(data['flattening_ranks'],data['source_format'])

    def test_exact_balanced_support(self):
        for case,size in zip(self.report['cases'],[18,42]):
            self.assertEqual(case['balanced_distribution']['positive_support_size'],size)
            self.assertEqual(case['balanced_distribution']['total_probability'],'1')

    def test_exact_koszul_deficits(self):
        expected=[([54,52,52],[54,54,54]),([255,255,255],[256,256,256])]
        for case,(source,target) in zip(self.report['cases'],expected):
            self.assertEqual(case['source_initial_k1_ranks'],source)
            self.assertEqual(case['target_k1_ranks'],target)
            self.assertTrue(any(a<b for a,b in zip(source,target)))
            self.assertFalse(case['improves_omega'])

    def test_trace_zero_instability_witness(self):
        face=self.report['cases'][1]['explicit_unstable_face']
        self.assertEqual(face['face_size'],146)
        self.assertEqual(face['k1_ranks'],[256,256,256])
        self.assertEqual(set(face['supported_instability_weight_histogram']),{1,7})
        self.assertTrue(all(sum(row)==0 for row in face['trace_zero_instability_weights']))


if __name__=='__main__':
    unittest.main()
