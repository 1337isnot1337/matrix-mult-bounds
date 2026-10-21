"""Exact replay of the two coupled quantum families."""
from collections import Counter
import importlib.util
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


faces=load('paired_quantum_faces',Path('research/ai/2026-10-21-paired-quantum/coupled_faces.py'))
matrix_ranks=load('paired_matrix_ranks',Path('research/ai/2026-10-20-paired-sources/all_ranks.py'))


class CoupledQuantumTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result=faces.report()

    def test_every_laurent_coefficient(self):
        data=self.result['source_valuation_data']
        self.assertEqual(len(data['records']),288)
        self.assertEqual(Counter(r['valuation'] for r in data['records']),{0:182,1:93,2:13})
        self.assertEqual(self.result['families'][0]['tensor_exponent_histogram'],{0:241,2:47})
        self.assertEqual(self.result['families'][1]['tensor_exponent_histogram'],{0:108,8:97,16:77,24:6})

    def test_exact_sparse_tensors_and_slices(self):
        for family,count in zip(self.result['families'],[241,108]):
            self.assertEqual(len(family['tensor_coefficients']),count)
            self.assertEqual(family['flattening_ranks'],[9,15,15])
            self.assertEqual(family['invertible_slice_index'],6)
            self.assertEqual(family['invertible_slice_determinant'],'1/31701690482688')
        blocked=self.result['families'][1]
        self.assertTrue(blocked['all_further_target_degenerations_excluded_by_rank2_slice'])
        self.assertEqual(blocked['rank2_slice_index'],2)
        self.assertEqual(blocked['basis_slice_ranks'][2],2)

    def test_all_koszul_powers_and_independent_target(self):
        expected=[[15,128,468,960,1210,960,468,128,15],
                  [15,124,438,874,1085,861,427,121,15]]
        target=[sum(matrix_ranks.padded_matrix_rank(shape,9,p)
                    for shape in [(1,3,3),(3,3,2)]) for p in range(9)]
        self.assertEqual(target,self.result['target_first_leg_koszul'])
        for family,ranks in zip(self.result['families'],expected):
            self.assertEqual([k['rank'] for k in family['first_leg_koszul']],ranks)
            self.assertTrue(family['passes_target_first_leg_koszul'])

    def test_a_negative_weight_is_rejected(self):
        family=faces.FAMILIES[0]
        bad=list(family['W']);bad[0]-=20
        with self.assertRaisesRegex(ArithmeticError,'Laurent pole'):
            faces.leading_indices(self.result['source_valuation_data'],family['D'],bad)


if __name__=='__main__':
    unittest.main()
