"""Regression and corruption controls for the quadratic-z middle family."""
import importlib.util
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-23-quadratic-z-middle'


def load(name,filename):
    spec=importlib.util.spec_from_file_location(name,PACKAGE/filename)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class QuadraticZMiddleRankTests(unittest.TestCase):
    def test_prime_fields_and_complete_kernel(self):
        mod=load('quadratic_z_verify','verify.py')
        report=mod.verify()
        self.assertEqual(report['status'],'pass')
        self.assertEqual(report['exhaustive'],580)
        self.assertEqual(report['seeded'],960)
        self.assertEqual(report['spectrum'],135)
        self.assertEqual(report['basis_vectors'],940)
        self.assertEqual(mod.prediction(5,3,[0,1]),20)
        self.assertEqual(mod.prediction(3,3,[0,0,1]),14)
        self.assertEqual(mod.prediction(5,9,[1,-2,3]),55)
        mod.check_case(5,3,2,[1,1],3,101)

    def test_independent_characteristic_zero(self):
        mod=load('quadratic_z_verify_q','verify_charzero.py')
        report=mod.verify()
        self.assertEqual(report['status'],'pass')
        self.assertEqual(report['independent_terms'],36)
        self.assertEqual(report['exact_rational_kernel_vectors'],105)

    def test_corrupt_matrix_rejected(self):
        mod=load('quadratic_z_verify_corrupt','verify.py')
        R=mod.source_matrix(3,3,1,[0,0,1],1,101)
        assert mod.rank_mod(R,101)==14
        damaged=[[0]*len(R[0]) for _ in R]
        self.assertNotEqual(mod.rank_mod(damaged,101),mod.prediction(3,3,[0,0,1]))


if __name__=='__main__':
    unittest.main()
