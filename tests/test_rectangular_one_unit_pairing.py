import importlib.util
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
FOLDER=ROOT/'research/ai/2026-10-21-rectangular-direct-sums'
SPEC=importlib.util.spec_from_file_location('one_unit_pairing_controls',FOLDER/'one_unit_pairing.py')
v=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(v)
class OneUnitPairingTests(unittest.TestCase):
 def test_complete_report(self):
  self.assertEqual(v.report(),json.loads((ROOT/'results/rectangular-direct-sums-20261021/one-unit-pairing.json').read_text()))
 def test_generic_pairing_cannot_pass_one_unit_gate(self):
  for a,b in [(2,4),(3,5),(4,6)]:
   self.assertEqual(v.pairing(a,b,1,{(0,0):1,(1,1):1})['source_rank_from_factor_formula'],a*a*b+a)
 def test_actual_hankel_one_unit_control(self):
  spec=importlib.util.spec_from_file_location('retained_one_step',FOLDER/'equality_one_step.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
  self.assertEqual(m.certificate(8,10)['rank_mod_2'],641)
if __name__=='__main__':unittest.main()
