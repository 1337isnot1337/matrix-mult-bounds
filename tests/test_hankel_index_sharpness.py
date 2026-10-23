"""Check polynomial kernel degrees independently of the exported annihilator."""
import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp
from sympy.polys.matrices import DomainMatrix

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-23-hankel-index-sharpness'
RESULTS=ROOT/'results/hankel-index-sharpness-2026-10-23'
spec=importlib.util.spec_from_file_location('hankel_sharpness',PACKAGE/'verify.py')
verify=importlib.util.module_from_spec(spec); spec.loader.exec_module(verify)


def coefficient_kernel_dimension(A,B,degree,domain):
    rows,columns=A.shape
    system=sp.zeros(rows*(degree+2),columns*(degree+1))
    for j in range(degree+1):
        system[j*rows:(j+1)*rows,j*columns:(j+1)*columns]=A
        system[(j+1)*rows:(j+2)*rows,j*columns:(j+1)*columns]=B
    rank=DomainMatrix.from_Matrix(system).convert_to(domain).rank()
    return system.cols-rank


def literal_pencil(epsilon,p,q):
    r=epsilon*(p+q); a=r+p; b=r+q
    A=sp.Matrix(a,b,lambda i,j:int(i+j==r-1))
    B=sp.Matrix(a,b,lambda i,j:int(i+j==r+p+q-1))
    return A,B,r


class HankelIndexSharpnessTests(unittest.TestCase):
    def test_homogeneous_identities_and_saved_report(self):
        report=verify.report()
        self.assertEqual(report,json.loads((RESULTS/'controls.json').read_text()))
        self.assertEqual(report['pencils_checked'],36)
        self.assertFalse(report['independent_review'])
        self.assertFalse(report['improves_omega'])
        boundary=report['a10_boundary']
        self.assertEqual(boundary['shape'],[10,10])
        self.assertEqual(boundary['rank'],8)
        self.assertEqual(boundary['left_minimal_indices'],[2,2])
        self.assertEqual(boundary['right_minimal_indices'],[2,2])

    def test_complete_kernel_dimensions_from_coefficient_equations(self):
        # These systems use only the two literal moment matrices, not P.
        for epsilon,p,q in [(1,1,1),(2,1,2),(2,2,2),(3,1,1)]:
            A,B,_=literal_pencil(epsilon,p,q)
            for domain in [sp.QQ,sp.GF(2),sp.GF(3)]:
                for C,D,nullity in [(A,B,q),(A.T,B.T,p)]:
                    for degree in range(epsilon+2):
                        with self.subTest(epsilon=epsilon,p=p,q=q,domain=domain,
                                          shape=C.shape,degree=degree):
                            expected=nullity*max(0,degree-epsilon+1)
                            self.assertEqual(coefficient_kernel_dimension(C,D,degree,domain),expected)

    def test_rank_at_all_small_field_points_including_infinity(self):
        for epsilon,p,q in [(1,1,2),(2,2,2),(3,2,1),(4,1,1)]:
            A,B,r=literal_pencil(epsilon,p,q)
            for prime in [2,3,5]:
                for member in [A+t*B for t in range(prime)]+[B]:
                    self.assertEqual(DomainMatrix.from_Matrix(member).convert_to(sp.GF(prime)).rank(),r)

    def test_minimal_degrees_after_change_of_pencil_coordinates(self):
        A,B,_=literal_pencil(2,2,2)
        C=A+B; D=A+2*B  # Determinant one, also over F2.
        for domain in [sp.QQ,sp.GF(2),sp.GF(3)]:
            self.assertEqual([coefficient_kernel_dimension(C,D,j,domain) for j in range(4)],[0,0,2,4])

    def test_prior_source_pins_and_package_manifest(self):
        import hashlib
        sources=json.loads((PACKAGE/'sources.json').read_text())
        for path,digest in sources['prior_source_sha256'].items():
            self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),digest,path)
        manifest=json.loads((PACKAGE/'manifest.json').read_text())
        for path,digest in manifest['sha256'].items():
            self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),digest,path)


if __name__=='__main__':
    unittest.main()
