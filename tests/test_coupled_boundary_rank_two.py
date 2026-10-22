"""Replay the coupled universal cubic identities on actual source matrices."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-21-coupled-boundary-rank-two'
RESULTS = ROOT/'results/coupled-boundary-rank-two-2026-10-21'
spec = importlib.util.spec_from_file_location('coupled_rank_two',PACKAGE/'verify.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def replay(source,certificate):
    matrices = {'B':v.decode(source['B']),'C':v.decode(source['C'])}
    full = sp.eye(228)
    count = 0
    for step in certificate['rounds']:
        dimension = step['parameter_dimension']
        forms = []
        for minor in step['minors']:
            matrix = matrices[minor['side']]
            positions = minor['positions']
            assert matrix.cols==dimension and len(positions)==3
            assert len({i for i,j in positions})==len({j for i,j in positions})==3
            form = sp.Matrix(1,dimension,lambda _,j:dict(minor['form']).get(j,0))
            first = next(j for j,value in enumerate(form) if value)
            scales = []
            for k,(row,column) in enumerate(positions):
                entry = matrix[200*column+row,:]
                scale = entry[0,first]/form[0,first]
                assert scale and entry==scale*form
                scales.append(scale)
                for _,later in positions[k+1:]:
                    assert matrix[200*later+row,:]==sp.zeros(1,dimension)
            assert sp.prod(scales)==sp.Rational(minor['determinant_ratio'])
            forms.append(form)
            count += 1
        constraints = sp.Matrix.vstack(*forms)
        kernel = v.decode(step['kernel'])
        assert v.rank(constraints)==step['forced_linear_rank']
        assert kernel.rows==dimension
        assert v.rank(kernel)==kernel.cols==dimension-step['forced_linear_rank']
        assert constraints*kernel==sp.zeros(constraints.rows,kernel.cols)
        matrices = {side:matrix*kernel for side,matrix in matrices.items()}
        full = full*kernel
    assert count==certificate['cubic_identities']==232
    assert matrices['B']==matrices['C']==sp.zeros(2400,28)
    assert full==v.decode(certificate['original_parameter_map'])
    assert v.rank(full)==28


class CoupledBoundaryRankTwoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = json.loads((RESULTS/'source.json').read_text())
        cls.certificate = json.loads((RESULTS/'certificate.json').read_text())
        cls.pilot = json.loads((RESULTS/'coordinate_pilot.json').read_text())

    def test_rebuild_from_the_actual_source_and_verify_dependency_pins(self):
        self.assertEqual(v.reports(),{'coordinate_pilot':self.pilot,
                                     'source':self.source,'certificate':self.certificate})
        self.assertEqual(sum(n for a,b,n in self.pilot['rank_pair_histogram']),228)
        self.assertEqual(self.pilot['nonzero_pairs_with_both_ranks_at_most_two'],[])
        sources = json.loads((PACKAGE/'sources.json').read_text())
        for source in sources['local_dependencies']:
            self.assertEqual(hashlib.sha256((ROOT/source['path']).read_bytes()).hexdigest(),
                             source['sha256'])

    def test_every_cubic_identity_complete_kernel_and_corrupt_ratio(self):
        replay(self.source,self.certificate)
        corrupt = copy.deepcopy(self.certificate)
        corrupt['rounds'][0]['minors'][0]['determinant_ratio'] = '0'
        with self.assertRaises(AssertionError):
            replay(self.source,corrupt)

    def test_identification_with_the_prior_28_dimensional_biform_normal_family(self):
        first = v.decode(self.source['normal_first_kernel'])
        kernel = v.decode(self.certificate['original_parameter_map'])
        actual = v.decode(self.certificate['actual_normal_basis'])
        transform = v.decode(self.certificate['prior_basis_transform'])
        prior = json.loads((ROOT/'results/third-boundary-trap-2026-10-21/normal.json').read_text())
        basis = v.decode_old(prior['normal_basis'])
        self.assertEqual(first.shape,(448,228))
        self.assertEqual(v.rank(first),228)
        self.assertEqual(first*kernel,actual)
        self.assertEqual(basis*transform,actual)
        self.assertEqual(v.rank(transform),28)
        self.assertEqual(v.rank(actual),28)
        zero_system = v.decode(self.source['B']).col_join(v.decode(self.source['C']))
        self.assertEqual(v.rank(zero_system),200)
        self.assertEqual(zero_system*kernel,sp.zeros(4800,28))

    def test_individual_rank_two_does_not_imply_zero(self):
        b,c = v.decode(self.source['B']),v.decode(self.source['C'])
        for name,j in self.certificate['individual_rank_two_controls'].items():
            left = sp.Matrix(200,12,lambda row,column:b[200*column+row,j])
            right = sp.Matrix(200,12,lambda row,column:c[200*column+row,j])
            expected = (2,4) if name=='B_rank_two_C_rank_four' else (4,2)
            self.assertEqual((v.rank(left),v.rank(right)),expected)


if __name__=='__main__':
    unittest.main()
