import copy
import importlib.util
from pathlib import Path
import unittest


PATH = Path(__file__).resolve().parents[1]/'research/ai/2026-10-20-alternating-degree-packing/verify_packing.py'
SPEC = importlib.util.spec_from_file_location('alternating_degree_packing',PATH)
PACKING = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PACKING)


class AlternatingDegreePackingTests(unittest.TestCase):
    def test_both_parities_and_replication_replay_every_source_term(self):
        for m in (1,2,3,4,5,8,9):
            for k in (1,2,3):
                with self.subTest(m=m,k=k):
                    data = PACKING.witness(m,k)
                    result = PACKING.verify(data)
                    self.assertTrue(result['verified'])
                    self.assertEqual(result['B'],k*((3*m*m+3)//4)-(m-1)//2)
                    self.assertEqual(result['source_terms_enumerated'],m*data['B'])

    def test_m4_exact_witness_and_error_order(self):
        data = PACKING.witness(4)
        result = PACKING.verify(data)
        self.assertEqual(data['B'],11)
        self.assertEqual([(b['degree'],b['start']) for b in PACKING.blocks(4)],
                         [(0,0),(3,1),(1,5),(2,8)])
        self.assertEqual(set(result['coefficient_count_by_power']),{'0','1'})
        self.assertEqual(result['retained_terms'],20)

    def test_removing_weights_fails_full_coefficient_replay(self):
        data = copy.deepcopy(PACKING.witness(4))
        for row in data['y']+data['z']:
            row['weight'] = 0
        with self.assertRaisesRegex(AssertionError,'constant tensor differs'):
            PACKING.verify(data)


if __name__ == '__main__':
    unittest.main()
