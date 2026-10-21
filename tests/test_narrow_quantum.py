"""Exact unequal source equivalence and fixed root-eight degenerations."""
from collections import Counter
import importlib.util
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


faces=load('narrow_quantum_faces',Path('research/ai/2026-10-21-narrow-quantum/faces.py'))
matrix_ranks=load('narrow_independent_matrix_ranks',Path('research/ai/2026-10-20-paired-sources/all_ranks.py'))


class NarrowQuantumTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result=faces.report()

    def test_generic_source_equivalence_and_regular_limits(self):
        self.assertEqual(self.result['generic_source_identity_checks'],841)
        self.assertEqual([row['regular_tensor_flattening_ranks'] for row in self.result['regular_calibrations']],
                         [[9,5,5],[6,5,5]])
        data=self.result['source_valuation_data']
        self.assertEqual(data['generic_nonzero_coefficients'],83)
        self.assertEqual(Counter(row['baseline_valuation'] for row in data['coefficients']),{0:50,1:33})

    def test_every_fixed_face_and_its_exact_exclusion(self):
        self.assertEqual(len(self.result['families']),23)
        self.assertTrue(self.result['all_fixed_faces_excluded'])
        self.assertEqual(Counter(row['exclusion']['type'] for row in self.result['families']),
                         {'ordinary flattening rank':9,'closed rank-one slice incidence':10,'Koszul rank':4})
        for row in self.result['families']:
            self.assertTrue(row['target_excluded'])
            self.assertEqual(sum(row['tensor_exponent_histogram'].values()),83)
            self.assertGreaterEqual(min(row['tensor_exponent_histogram']),0)
            if row['exclusion']['type']=='closed rank-one slice incidence':
                self.assertEqual(row['concise_format'][0],9)
                self.assertEqual(row['original_basis_slice_ranks'][row['exclusion']['original_slice_index']],1)

    def test_long_leg_obstructions_and_all_first_leg_passes(self):
        for name,axis in [('face0',2),('face1',1)]:
            row=next(r for r in self.result['families'] if r['name']==name)
            self.assertTrue(all(s>=t for s,t in zip(row['all_legs_koszul'][0]['source_ranks'],
                                                   row['all_legs_koszul'][0]['target_ranks'])))
            self.assertEqual(row['exclusion']['witnesses'],
                             [{'axis':axis,'power':1,'source_rank':62,'target_rank':63}])
        row=next(r for r in self.result['families'] if r['name']=='face3')
        self.assertEqual(row['all_legs_koszul'][0]['source_ranks'],[6,53,206,453,608,494,240,66,8])

    def test_target_ranks_against_independent_formula(self):
        first=[matrix_ranks.padded_matrix_rank((3,2,3),9,p) for p in range(9)]
        self.assertEqual(first,self.result['target_intrinsic_koszul_ranks'][0])
        for ambient in (6,7,8):
            expected=[matrix_ranks.padded_matrix_rank((3,3,2),ambient,p) for p in range(ambient)]
            for axis in (1,2):self.assertEqual(expected,faces.padded_target_ranks(axis,ambient))

    def test_negative_laurent_exponent_is_rejected(self):
        family=faces.FAMILIES[0];bad=list(family['W']);bad[0]-=20
        with self.assertRaisesRegex(ArithmeticError,'Laurent pole'):
            faces.leading_indices(self.result['source_valuation_data'],family['D'],bad)


if __name__=='__main__':
    unittest.main()
