"""Replay the hyperplane certificates without searching for new minors."""
import importlib.util
import json
from pathlib import Path
import unittest
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-21-boundary-hyperplanes'
RESULTS=ROOT/'results/boundary-hyperplanes-2026-10-21'
spec=importlib.util.spec_from_file_location('boundary_hyperplane_verifier',PACKAGE/'verify.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)


def check_minor(E,record):
    form=sp.Matrix(1,E.cols,lambda _,j:dict(record['linear_form']).get(j,0))
    scales=[];positions=record['positions']
    assert len(positions)==2 and len({p[0] for p in positions})==2 and len({p[1] for p in positions})==2
    chosen=next(j for j in range(E.cols) if form[0,j])
    for k,(row,column) in enumerate(positions):
        diagonal=E[200*column+row,:];scale=diagonal[0,chosen]/form[0,chosen]
        assert scale and diagonal==scale*form
        scales.append(scale)
        for _,future in positions[k+1:]:assert not E[200*future+row,:].todok()
    assert sp.prod(scales)==sp.Rational(record['determinant_ratio'])


class BoundaryHyperplaneTests(unittest.TestCase):
    def test_full_saved_reports_replay(self):
        for name,report in v.reports().items():
            self.assertEqual(report,json.loads((RESULTS/(name+'.json')).read_text()))
        self.assertEqual(v.reports()['matrix_space']['full_space_dimension'],80)
        self.assertEqual(v.reports()['matrix_space']['minimum_projected_first_rank_if_nonzero_normal'],3)

    def test_boundary_minors_and_full_kernels_without_search(self):
        old=v.load(ROOT/'research/ai/2026-10-21-moving-boundary-flags/minimum_rank.py','hyperplane_independent_old')
        data=old.normal.data();saved=json.loads((RESULTS/'boundary_obstruction.json').read_text())
        for side,key in [('B','left_obstruction'),('C','right_obstruction')]:
            M=data[key][:2400,:];E=M
            for record in saved[side]['rounds']:
                self.assertEqual(E.cols,record['parameter_dimension'])
                for minor in record['minors']:check_minor(E,minor)
                R=sp.MutableSparseMatrix(len(record['minors']),E.cols,
                    {(i,j):value for i,item in enumerate(record['minors']) for j,value in item['linear_form']})
                K=v.decode(record['kernel'])
                self.assertEqual(len(R.to_DM().rref()[1]),record['forced_rank'])
                self.assertEqual(R*K,sp.zeros(R.rows,K.cols))
                self.assertEqual(len(K.to_DM().rref()[1]),K.cols)
                self.assertEqual(K.cols,E.cols-record['forced_rank']);E=E*K
            self.assertFalse(E.todok())
            j=saved[side]['sharp_parameter'];control=sp.Matrix(200,12,lambda a,b:M[200*b+a,j])
            self.assertEqual(len(control.to_DM().rref()[1]),2)
        first=saved['B']['rounds'][0]['minors'][0];tampered=sp.MutableSparseMatrix(data['left_obstruction'][:2400,:])
        row=first['positions'][0][0];column=first['positions'][1][1]
        tampered[200*column+row,0]+=1
        with self.assertRaises(AssertionError):check_minor(tampered,first)

    def test_rank_one_peeling_by_independent_polynomial_evaluation(self):
        report=json.loads((RESULTS/'matrix_space.json').read_text())
        N=v.decode(report['annihilators']);B=v.decode(report['reduced_space_basis']);C=v.decode(report['full_space_basis'])
        self.assertEqual(N*B,sp.zeros(16,20))
        self.assertEqual(len(N.to_DM().rref()[1]),16)
        self.assertEqual(len(B.to_DM().rref()[1]),20)
        self.assertEqual(len(C.to_DM().rref()[1]),80)
        for a in range(2):
            for b in range(2):
                rows=[(2*i+a)*12+2*j+b for i in range(6) for j in range(6)]
                self.assertEqual(N*C[rows,:],sp.zeros(16,80))
        u=sp.symbols('u:6');w=sp.symbols('w:6')
        polynomials=[sum(N[r,6*i+j]*u[i]*w[j] for i in range(6) for j in range(6)) for r in range(16)]
        previous=[]
        for record in report['triangular_peeling']:
            self.assertEqual(record['previous_zero_coordinates'],previous)
            restricted=[p.subs({u[i]:0 for i in previous}) for p in polynomials]
            equations=[restricted[i]+(scale*restricted[j] if j is not None else 0)
                       for i,j,scale in record['equation_combinations']]
            M=sp.Matrix([[sp.expand(p).coeff(w[j]) for j in record['v_column_order']] for p in equations])
            coordinate=record['forced_u_coordinate']
            self.assertEqual(sp.expand(M.det()),sp.Rational(record['determinant_ratio'])*u[coordinate]**6)
            previous.append(coordinate)
        self.assertEqual(sorted(previous),list(range(6)))

    def test_general_compression_bound_has_a_sharp_control(self):
        report=v.compression_control()
        self.assertEqual(report['space_dimension'],60)
        self.assertEqual(report['projected_dimension'],55)
        self.assertEqual(report['compression_kernel_dimension'],5)
        # The written lemma uses a rank-one-free6-by6 space; skew matrices supply one.
        for i in range(1,6):
            M=sp.zeros(12);M[2*i,0]=1;M[0,2*i]=-1
            self.assertEqual(M.rank(),2)
            self.assertEqual(M.extract(range(1,12),range(1,12)),sp.zeros(11))


if __name__=='__main__':unittest.main()
