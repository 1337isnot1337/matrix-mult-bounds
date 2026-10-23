"""Exact full-space compression and corrupted sharpness controls."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-23-resolvent-loss-seven'
spec=importlib.util.spec_from_file_location('loss_seven',PACKAGE/'verify.py')
v=importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def binary_rank(matrices):
    """Independent F2 elimination on packed whole-matrix vectors."""
    pivots={}
    for matrix in matrices:
        word=sum(1 << (112*r+c) for (r,c),x in matrix.items() if x % 2)
        while word:
            pivot=word.bit_length()-1
            if pivot not in pivots:
                pivots[pivot]=word
                break
            word ^= pivots[pivot]
    return len(pivots)


class ResolventLossSevenTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prior=v.predecessor()
        cls.slices,cls.high,cls.inverse=cls.prior.source()

    def test_exact_replay_and_saved_report(self):
        report=v.verify()
        self.assertEqual(report,json.loads((ROOT/'results/resolvent-loss-seven-2026-10-23/verification.json').read_text()))
        self.assertEqual(report['sharpness']['total_rank_loss'],7)
        self.assertFalse(report['independent_review'])
        self.assertFalse(report['improves_omega'])

    def test_independent_full_source_binary_compression(self):
        basis=list(v.source_basis(self.slices,self.high))
        self.assertEqual(len({label for label,matrix in basis}),112)
        self.assertEqual(binary_rank(matrix for label,matrix in basis),112)
        compressed=[{(r,c):x for (r,c),x in matrix.items()
                     if r not in v.OMIT_ROWS and c not in v.OMIT_COLUMNS}
                    for label,matrix in basis]
        self.assertEqual(binary_rank(compressed),110)
        kernel_indices=[i for i,(label,matrix) in enumerate(basis)
                        if label in [('high',0,0),('high',0,4)]]
        self.assertEqual(len(kernel_indices),2)
        for i in kernel_indices:
            self.assertEqual(compressed[i],{})

    def test_corrupt_factors_fail_exact_support(self):
        with self.assertRaisesRegex(ValueError,'does not kill'):
            v.check_witness(self.high,omit_columns=[3,7,11,19])
        with self.assertRaisesRegex(ValueError,'does not kill'):
            v.check_witness(self.high,omit_rows=[105,106,108])

    def test_projected_pencil_has_full_row_rank_over_small_fields(self):
        # Exhaust the projective parameter line, including its infinity point.
        # This is a finite control; the all-field claim uses the written proof.
        for prime in (2,3,5,7):
            parameters=[(1,t) for t in range(prime)]+[(0,1)]
            for a,b in parameters:
                rows=[]
                for j in range(3):
                    rows.append({(0,j):a,(0,j+1):b})
                self.assertEqual(v.rank_mod(rows,prime),3)


if __name__ == '__main__':
    unittest.main()
