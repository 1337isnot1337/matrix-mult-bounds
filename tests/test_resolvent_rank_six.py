"""Low-rank locus identities, rejected corruptions, and compression sharpness."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-23-resolvent-rank-six'
spec = importlib.util.spec_from_file_location('rank_six',PACKAGE/'verify.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class ResolventRankSixTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.slices,cls.high,cls.inverse = v.source()
        cls.certificate = json.loads((PACKAGE/'certificate.json').read_text())
        cls.basis = v.replay(cls.certificate,cls.slices,cls.high)

    def test_complete_certificate_and_saved_report(self):
        expected = json.loads((ROOT/'results/resolvent-rank-six-2026-10-23/verification.json').read_text())
        self.assertEqual(v.verify(),expected)
        self.assertEqual(expected['elimination_stages'],26)
        self.assertEqual(expected['full_low_rank_dimension'],17)
        self.assertFalse(expected['rank_seven_exists'])
        self.assertFalse(expected['independent_review'])
        self.assertFalse(expected['improves_omega'])

    def test_independent_literal_source_reconstruction(self):
        predecessor = ROOT/'research/ai/2026-10-23-resolvent-minrank/verify.py'
        spec = importlib.util.spec_from_file_location('old_source',predecessor)
        old = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(old)
        slices,_,inverse,_,high = old.outer_source()
        self.assertEqual((self.slices,self.inverse,self.high),(slices,inverse,high))

    def test_missing_stage_and_bad_unit_are_rejected(self):
        bad = copy.deepcopy(self.certificate)
        bad['stages'].pop()
        with self.assertRaisesRegex(ValueError,'coverage'):
            v.replay(bad,self.slices,self.high)
        bad = copy.deepcopy(self.certificate)
        stage = bad['stages'][0]
        stage['form'][stage['pivot']] = 2
        with self.assertRaisesRegex(ValueError,'unit substitution'):
            v.replay(bad,self.slices,self.high)

    def test_bad_minor_and_corrupted_source_are_rejected(self):
        bad = copy.deepcopy(self.certificate)
        bad['stages'][0]['minor'][1][0] = bad['stages'][0]['minor'][0][0]
        with self.assertRaisesRegex(ValueError,'minor indices'):
            v.replay(bad,self.slices,self.high)
        bad = copy.deepcopy(self.certificate)
        stage = bad['stages'][0]
        index = next(i for i,x in enumerate(stage['form']) if not x)
        stage['form'][index] = 1
        with self.assertRaisesRegex(ValueError,'diagonal form'):
            v.replay(bad,self.slices,self.high)
        slices = copy.deepcopy(self.slices)
        # Put a new coefficient above a certified diagonal.
        row = stage['minor'][0][0]
        col = stage['minor'][1][1]
        slices[0][row][col] += 1
        with self.assertRaisesRegex(ValueError,'upper triangle'):
            v.replay(self.certificate,slices,self.high)

    def test_sharpness_and_rank_eight_boundary(self):
        for matrix in self.basis:
            self.assertEqual(sp.Matrix(matrix).rank(),6)
        self.assertEqual(sp.Matrix(v.combine(self.basis,[1,-2,3,-4,5])).rank(),6)
        self.assertEqual(sp.Matrix(self.high[1]).rank(),8)
        self.assertEqual(sp.Matrix.hstack(*(sp.Matrix(m) for m in self.basis)).rank(),6)

    def test_critical_compression_loses_exactly_one_low_rank_direction(self):
        # In coordinates E_full=F^6, construct U=X0^-1(L), with L the first
        # three coordinates. This realizes the proof's critical compression.
        blocks = []
        for block in range(4):
            for matrix in (self.basis if block == 0 else self.basis[:4]):
                m = sp.zeros(6,112)
                m[:,28*block:28*(block+1)] = sp.Matrix(matrix)[v.ROWS,:]
                blocks.append(m)
        self.assertEqual(len(blocks),17)
        self.assertEqual(sp.Matrix.hstack(*(m.reshape(672,1) for m in blocks)).rank(),17)
        quotient = blocks[0][3:,:]
        self.assertEqual(quotient.rank(),3)
        inclusion = sp.Matrix.hstack(*quotient.nullspace())
        self.assertEqual(inclusion.shape,(112,109))
        self.assertEqual(inclusion.rank(),109)
        compressed = [m[3:,:]*inclusion for m in blocks]
        self.assertEqual(compressed[0],sp.zeros(3,109))
        flat = sp.Matrix.hstack(*(m.reshape(327,1) for m in compressed))
        self.assertEqual(flat.rank(),16)
        self.assertEqual(len(flat.nullspace()),1)


if __name__ == '__main__':
    unittest.main()
