"""Replay biform identities, exact rank certificates and puncture controls."""
import importlib.util
import itertools
import json
from pathlib import Path
import unittest
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-21-biform-third-core'
RESULTS=ROOT/'results/biform-third-core-2026-10-21'
spec=importlib.util.spec_from_file_location('biform_third_verifier',PACKAGE/'verify.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)


def replay_chain(M,record):
    rows,columns=record['matrix_shape'];E=M
    def flat(i,j):return j*rows+i if record['vectorization']=='column' else i*columns+j
    for step in record['rounds']:
        assert E.cols==step['parameter_dimension']
        forms=[]
        for minor in step['minors']:
            positions=minor['positions'];assert len(positions)==record['minor_size']
            assert len({a for a,b in positions})==len(positions)==len({b for a,b in positions})
            form=sp.Matrix(1,E.cols,lambda _,j:dict(minor['linear_form']).get(j,0));forms.append(form)
            first=next(j for j in range(E.cols) if form[0,j]);scales=[]
            for k,(i,j) in enumerate(positions):
                entry=E[flat(i,j),:];scale=entry[0,first]/form[0,first]
                assert scale and entry==scale*form;scales.append(scale)
                for _,later in positions[k+1:]:assert not E[flat(i,later),:].todok()
            assert sp.prod(scales)==sp.Rational(minor['determinant_ratio'])
        R=sp.Matrix.vstack(*forms);K=v.decode(step['kernel'])
        assert len(R.to_DM().rref()[1])==step['forced_linear_rank']
        assert R*K==sp.zeros(R.rows,K.cols)
        assert len(K.to_DM().rref()[1])==K.cols==E.cols-step['forced_linear_rank']
        E=E*K
    assert not E.todok() and E.cols==record['final_parameter_dimension']


class BiformThirdCoreTests(unittest.TestCase):
    def test_complete_saved_reports_replay(self):
        for name,report in v.reports().items():
            self.assertEqual(report,json.loads((RESULTS/(name+'.json')).read_text()))
        self.assertEqual(v.reports()['core_minimum']['minimum_nonzero_first_rank'],2)

    def test_polynomial_product_from_integer_coefficient_convolution(self):
        report=json.loads((RESULTS/'structure.json').read_text())
        A=v.decode(report['U_basis_change']);B=v.decode(report['V_basis_change']);mu=v.decode(report['multiplication'])
        self.assertEqual(A.det(),1);self.assertEqual(B.det(),1)
        degreesA=[(0,0),(1,0),(0,1),(1,1),(0,2),(1,2)]
        degreesB=[(0,0),(1,0),(2,0),(0,1),(1,1),(2,1)]
        expected=sp.zeros(16,36)
        for i,j,a,b in itertools.product(range(6),repeat=4):
            p,q=degreesA[a];r,s=degreesB[b]
            expected[4*(p+r)+q+s,6*i+j]+=A[i,a]*B[j,b]
        self.assertEqual(mu,expected);self.assertEqual(len(mu.to_DM().rref()[1]),16)
        old=json.loads((ROOT/'results/boundary-hyperplanes-2026-10-21/matrix_space.json').read_text())
        self.assertEqual(mu*v.decode(old['reduced_space_basis']),sp.zeros(16,20))

    def test_tensor_factorization_and_sharp_specific_hyperplane_control(self):
        report=json.loads((RESULTS/'structure.json').read_text());core=v.decode(report['core'])
        old=json.loads((ROOT/'results/third-boundary-trap-2026-10-21/block.json').read_text());E=v.decode(old)
        keep=list(range(8))+list(range(12,16));reconstructed=sp.zeros(16*12*12,28)
        for i,s,k,b,c in itertools.product(range(2),range(2),range(4),range(6),range(6)):
            source=8*i+4*s+k;row=2*b+1-s;column=2*c+1-i
            reconstructed[(source*12+row)*12+column,:]=core[(k*6+b)*6+c,:]
        actual=E[[(a*16+keep[b])*16+keep[c] for a in range(16) for b in range(12) for c in range(12)],:]
        self.assertEqual(reconstructed,actual)
        mu=v.decode(report['multiplication']);K=v.decode(report['pair_syzygy_kernel'])
        operator=mu[:,[6*k for k in range(6)]].row_join(mu[:,list(range(6))])
        self.assertEqual(operator*K,sp.zeros(16,4));self.assertEqual(len(K.to_DM().rref()[1]),4)
        images=v.decode(report['pair_syzygy_matrix_images'])
        self.assertEqual(mu*images,sp.zeros(16,4));self.assertEqual(len(images.to_DM().rref()[1]),3)

    def test_all_saved_minor_chains_and_a_corruption_rejection(self):
        core=v.decode(json.loads((RESULTS/'structure.json').read_text())['core'])
        minimum=json.loads((RESULTS/'core_minimum.json').read_text());replay_chain(core,minimum)
        j=minimum['sharp_parameter'];self.assertEqual(len(sp.Matrix(4,36,lambda a,b:core[36*a+b,j]).to_DM().rref()[1]),2)
        old=v.previous_minors()
        data=old.normal.data();B=data['left_obstruction'][:2400,:];C=data['right_obstruction'][:2400,:]
        records=json.loads((RESULTS/'conditioned_obstructions.json').read_text())
        for side,full,remaining in [('C',B,C),('B',C,B)]:
            record=records[side];K=v.decode(record['other_side_full_boundary_kernel'])
            self.assertEqual(full*K,sp.zeros(2400,100));self.assertEqual(len(K.to_DM().rref()[1]),100)
            self.assertEqual(len(full.to_DM().rref()[1]),128)
            M=remaining*K;replay_chain(M,record['chain']);j=record['sharp_parameter']
            self.assertEqual(len(sp.Matrix(200,12,lambda a,b:M[200*b+a,j]).to_DM().rref()[1]),4)
        corrupt=sp.MutableSparseMatrix(core);minor=minimum['rounds'][0]['minors'][0]
        corrupt[36*minor['positions'][0][0]+minor['positions'][1][1],0]+=1
        with self.assertRaises(AssertionError):replay_chain(corrupt,minimum)

    def test_sharp_one_three_puncture_and_two_two_counterexample(self):
        report=json.loads((RESULTS/'puncture_control.json').read_text());matrices=[]
        for i in [1,2]:
            Z=sp.zeros(3);Z[0,i]=1;Z[i,0]=-1
            for a,b in itertools.product(range(2),repeat=2):
                unit=sp.zeros(2);unit[a,b]=1;matrices.append(sp.kronecker_product(Z,unit))
        images=[M.extract(range(1,6),[3,4,5]) for M in matrices]
        self.assertEqual([v.encode(M) for M in images],report['projected_matrices'])
        first=sp.Matrix.vstack(*(sp.Matrix(1,15,list(M)) for M in images))
        self.assertEqual(first.rank(),3)
        for M in matrices:self.assertEqual(M.extract(range(2,6),range(2,6)),sp.zeros(4))
        self.assertEqual(report['two_by_two_loss_counterexample_first_rank'],0)


if __name__=='__main__':unittest.main()
