"""Independent literal-kernel and rank-minor checks for four-space lines."""
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import unittest

import sympy as sp
from sympy.polys.matrices import DomainMatrix

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-23-hankel-fourspace-pencils'
RESULTS=ROOT/'results/hankel-fourspace-pencils-2026-10-23'
spec=importlib.util.spec_from_file_location('fourspace_pencils',PACKAGE/'verify.py')
verify=importlib.util.module_from_spec(spec);spec.loader.exec_module(verify)


def literal_matrix(values):
    h=[0]*19
    for i,value in zip([3,7,11,15],values):h[i]=value
    return sp.Matrix(10,10,lambda i,j:h[i+j])


def reconstructed_tangent(line):
    rows=[]
    # All pairings have homogeneous parameter degree four. Five finite
    # points recover their full common kernel; infinity is an extra control.
    for u,v in [(1,t) for t in range(5)]+[(0,1)]:
        H=literal_matrix([a*u+b*v for a,b in line])
        left=H.T.nullspace();right=H.nullspace()
        if len(left)!=2 or len(right)!=2:
            raise ArithmeticError('unexpected seed rank drop')
        for x in left:
            for y in right:
                row=[sp.Integer(0)]*19
                for i in range(10):
                    for j in range(10):row[i+j]+=x[i]*y[j]
                rows.append(row)
    return sp.Matrix(rows)


def rank(matrix):
    return DomainMatrix.from_Matrix(matrix).convert_to(sp.QQ).rank()


class HankelFourspacePencilTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=verify.report()

    def test_complete_symbolic_identity_and_saved_witness(self):
        self.assertEqual(self.report,json.loads((RESULTS/'controls.json').read_text()))
        self.assertEqual(self.report['chart_identity']['nonzero_residual_coefficients'],0)
        self.assertFalse(self.report['other_exceptional_extensions_classified'])
        self.assertFalse(self.report['arbitrary_quadratic_hankel_pencils_classified'])
        self.assertFalse(self.report['independent_review'])
        self.assertFalse(self.report['improves_omega'])

    def test_literal_kernels_reconstruct_all_declared_tangent_dimensions(self):
        dimensions=set()
        for row in self.report['lines']:
            line=[[sp.Rational(x) for x in pair] for pair in row['line']]
            operator=reconstructed_tangent(line)
            dimension=19-rank(operator);dimensions.add(dimension)
            self.assertEqual(dimension,row['common_tangent_dimension'])
            if dimension==4:
                self.assertEqual([i for i in range(19) if not any(operator[:,i])],[3,7,11,15])
        self.assertEqual(dimensions,{4,7})

    def test_eight_variable_identity_and_parameter_covariance(self):
        for coefficients in [(0,1,2,3,1,-1,2,0),(1,2,3,-1,2,1,-2,3),
                             (0,0,0,0,0,0,0,0),(1,0,0,1,1,0,0,1)]:
            line=[coefficients[i:i+2] for i in range(0,8,2)]
            M,N,delta=verify.matrices(line)
            self.assertEqual(N.det(),-4*delta*M.det()**3)
            for change in [sp.Matrix([[1,2],[0,1]]),sp.Matrix([[2,1],[1,1]])]:
                transformed=[list(sp.Matrix(1,2,pair)*change) for pair in line]
                P,Q,new_delta=verify.matrices(transformed)
                self.assertEqual(P.det(),M.det()*change.det()**3)
                self.assertEqual(Q.det(),N.det()*change.det()**10)
                self.assertEqual(new_delta,delta*change.det())

    def test_exceptional_tangent_equations_and_nonintegration(self):
        operator=reconstructed_tangent([(0,1),(0,0),(1,0),(0,1)])
        basis=operator.nullspace()
        self.assertEqual(len(basis),7)
        for vector in basis:
            for i in [0,1,2,8,9,10,12,13,14]:self.assertEqual(vector[i],0)
            for i in [4,5,6]:self.assertEqual(vector[i+12],-2*vector[i])
        h=[0]*19;h[5]=1;h[17]=-2
        extra=sp.Matrix(10,10,lambda i,j:h[i+j])
        endpoint=literal_matrix([1,0,0,1])
        self.assertEqual(rank(extra),8)
        self.assertEqual((extra+endpoint).det(),-1)
        self.assertEqual(rank(extra+endpoint),10)

    def test_higher_determinant_and_elimination_without_symbolic_pilot(self):
        for A,C,y in itertools.product([-1,0,1],repeat=3):
            h=[0]*19
            for i,value in {3:A,5:y,11:C,15:A,17:-2*y}.items():h[i]=value
            H=sp.Matrix(10,10,lambda i,j:h[i+j])
            self.assertEqual(H.det(),-A**4*y**6)
        # Reconstruct the ideal and check the two consequences used in the proof.
        A,B,D,x,y,z=sp.symbols('A B D x y z');E=A-D
        generators=[B*x+y*z,2*B*y+z*z,B*z,E*x,2*E*y+3*x*x,E*z+3*x*y]
        ideal=sp.groebner(generators,A,B,D,x,y,z)
        self.assertEqual(ideal.reduce(x**3)[1],0)
        self.assertEqual(ideal.reduce(z**3)[1],0)

    def test_paired_family_tangents_and_guard_from_literal_matrices(self):
        family=self.report['paired_exceptional_family']
        self.assertEqual(family['additional_parameter_guards'],[])
        self.assertEqual(family['seed_eight_minor_at_zero'],1)
        for beta in [-1,0,2,sp.Rational(1,2)]:
            operator=reconstructed_tangent([(0,1),(beta,0),(1,0),(0,1)])
            self.assertEqual(19-rank(operator),7)
            for vector in operator.nullspace():
                for shift in range(3):
                    value=vector[shift+4]
                    self.assertEqual(vector[shift],2*beta*value)
                    self.assertEqual(vector[shift+8],0)
                    self.assertEqual(vector[shift+12],-beta*value)
                    self.assertEqual(vector[shift+16],-2*value)
        M,_,_=verify.matrices([(0,1),(1,0),(1,0),(0,1)])
        self.assertEqual(M.det(),0)
        self.assertEqual(rank(literal_matrix([1,1,1,1])),4)

    def test_paired_family_determinant_from_complete_source(self):
        parameters=[(-1,1,2,3),(0,1,2,3),(2,1,2,1),
                    (sp.Rational(1,2),3,-1,2),(sp.I,2,1,1),
                    (2,0,1,1),(2,1,0,0)]
        for beta,A,C,y in parameters:
            with self.subTest(beta=beta,A=A,C=C,y=y):
                h=[0]*19
                for i,value in {1:-2*beta*y,3:A,5:-y,7:beta*C,
                                11:C,13:beta*y,15:A,17:2*y}.items():h[i]=value
                H=sp.Matrix(10,10,lambda i,j:h[i+j])
                expected=-(beta**3-1)**2*y**6*(A*A-beta*C*C-2*beta*y*y)**2
                self.assertEqual(sp.expand(H.det()-expected),0)

    def test_local_source_and_package_pins(self):
        sources=json.loads((PACKAGE/'sources.json').read_text())
        for path,digest in sources['local_source_sha256'].items():
            self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),digest,path)
        manifest=json.loads((PACKAGE/'manifest.json').read_text())
        for path,digest in manifest['sha256'].items():
            self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),digest,path)


if __name__=='__main__':
    unittest.main()
