import copy
import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT=Path(__file__).resolve().parents[1]
DIRECTORY=ROOT/'research/ai/2026-10-20-anisotropic-constructions'
SPEC=importlib.util.spec_from_file_location('parity_balancing_stabilizer_verify',DIRECTORY/'parity_balancing_stabilizer_verify.py')
VERIFY=importlib.util.module_from_spec(SPEC)
sys.path.insert(0,str(DIRECTORY))
try:
    SPEC.loader.exec_module(VERIFY)
finally:
    sys.path.pop(0)
COORDINATES=ROOT/'results/anisotropic-constructions-2026-10-20/parity_balancing_stabilizer_a33_seed_coordinates.json'


class FixedSeedStabilizerTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads(COORDINATES.read_text())

    def test_full_exact_seed_and_positive_control(self):
        report=VERIFY.verify(self.data)
        self.assertEqual(report['N_trace_O_squared_minus_trace_O_squared'],[32521,59183])
        self.assertEqual(report['source_terms_replayed'],729)
        self.assertTrue(report['exact_M4_control']['all_4096_operator_entries_match_identity'])
        self.assertFalse(report['general_source_degeneration_excluded'])

    def test_changed_map_rejected_after_recomputing_its_hash(self):
        altered=copy.deepcopy(self.data)
        entry=altered['map_coordinates']['A'][0][0]
        entry[0]=(float.fromhex(entry[0])+1).hex()
        altered['coordinate_payload_sha256']=VERIFY.payload_hash(altered['map_coordinates'])
        with self.assertRaisesRegex(ArithmeticError,'replayed invariant'):
            VERIFY.verify(altered,with_control=False)

    def test_changed_exact_coordinate_hash_rejected(self):
        altered=copy.deepcopy(self.data)
        altered['coordinate_payload_sha256']='0'*64
        with self.assertRaisesRegex(ArithmeticError,'payload hash'):
            VERIFY.verify(altered,with_control=False)


if __name__=='__main__':
    unittest.main()
