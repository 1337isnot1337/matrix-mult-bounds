"""Exact coefficient acceptance for the varying recoupling family."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-20-quantum-recoupling'
RESULTS=ROOT/'results/quantum-recoupling-2026-10-20'
spec=importlib.util.spec_from_file_location('quantum_recoupling',PACKAGE/'quantum.py')
quantum=importlib.util.module_from_spec(spec);spec.loader.exec_module(quantum)


def check_basis(m,n,columns=None):
    columns=quantum.cg(m,n) if columns is None else columns
    inverse=quantum.inverse_cg(m,n)
    for (i,j),coordinates in inverse.items():
        for r in range(max(0,i+j-n),min(m,i+j)+1):
            coefficient=sum((value*columns[label].get(r,quantum.K.zero)
                             for label,value in coordinates),quantum.K.zero)
            if coefficient!=int(r==i):raise ArithmeticError('complete basis reconstruction')


class QuantumRecouplingTests(unittest.TestCase):
    def test_saved_exact_controls_and_regular_initial_ranks(self):
        self.assertEqual(json.loads(json.dumps(quantum.report())),json.loads((RESULTS/'controls.json').read_text()))

    def test_projection_has_three_local_diagonal_factors(self):
        q=quantum.q
        for m in range(5):
            for n in range(5):
                for i in range(m+1):
                    A=q**(i*n+i*(i-1)//2)*quantum.qchoose(m,i)
                    for j in range(n+1):
                        s=i+j
                        B=q**(j*(j-1)//2)*quantum.qchoose(n,j)
                        C=q**(-s*(s-1)//2)/quantum.qchoose(m+n,s)
                        self.assertEqual(A*B*C,quantum.highest_projection(m,n,i,j))

    def test_complete_generic_basis_reconstruction(self):
        for m,n in [(1,1),(1,2),(2,2),(2,4),(3,3),(3,6)]:check_basis(m,n)

    def test_corrupted_basis_is_rejected(self):
        columns={label:dict(value) for label,value in quantum.cg(2,4).items()}
        columns[1,1][1]+=quantum.q
        with self.assertRaisesRegex(ArithmeticError,'basis reconstruction'):check_basis(2,4,columns)

    def test_generic_basis_is_nonsingular_at_classical_specialization(self):
        for m,n in [(1,1),(2,2),(3,3),(3,6)]:
            columns=quantum.cg(m,n)
            for s in range(m+n+1):
                rows=range(max(0,s-n),min(m,s)+1)
                labels=[(k,s-k) for k in range(min(m,n)+1) if 0<=s-k<=m+n-2*k]
                determinant=quantum.determinant([[columns[label].get(i,quantum.K.zero) for label in labels] for i in rows])
                self.assertNotEqual(determinant.numer.evaluate(quantum.q.numer,1),0)
                self.assertNotEqual(determinant.denom.evaluate(quantum.q.numer,1),0)


if __name__=='__main__':unittest.main()
