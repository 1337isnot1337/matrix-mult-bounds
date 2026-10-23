"""Exact coefficient-span and source-factorization evidence, with scope controls."""
import copy
import importlib.util
import itertools
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-23-resolvent-all-compressions'
spec=importlib.util.spec_from_file_location('all_compressions_certificate',PACKAGE/'certify.py')
cert=importlib.util.module_from_spec(spec);spec.loader.exec_module(cert)


class AllConstantResolventTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.witness=json.loads((ROOT/'results/resolvent-all-compressions-2026-10-23/certificate.json').read_text())

    def test_complete_polynomial_coefficient_span(self):
        result=cert.verify(self.witness)
        self.assertEqual(result['cubic_coefficient_rank_mod_2'],1330)
        self.assertEqual(result['nonzero_reduced_matrix_rank_at_least'],3)
        self.assertTrue(result['all_cubic_forms_over_Q_spanned'])
        self.assertFalse(result['general_A4_excluded'])

    def test_source_factorization_on_all_112_literal_slices(self):
        path=ROOT/'research/ai/2026-10-21-singular-unit-resolvent/certify.py'
        spec=importlib.util.spec_from_file_location('resolvent_source_factorization_control',path)
        old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
        unit,_,normalized=cert.outer_source()
        dense=old.src.source_matrix(4,old.src.integer_slice(4))
        source_unit=[{j:x for j,x in enumerate(row) if x} for row in dense]
        for i,k,s in itertools.product(range(4),range(7),range(4)):
            matrix=[{} for _ in range(112)];outer=normalized[4*i+s]
            for q in range(4):
                qp=q+3-k
                if not 0<=qp<4:continue
                for u,row in enumerate(outer):
                    H,r=divmod(u,4);index=H*16+qp*4+r
                    matrix[index].update({(v//4)*16+q*4+v%4:x for v,x in enumerate(row) if x})
            self.assertEqual(old.multiply(source_unit,matrix),old.literal(4,i,k,s))

    def test_missing_or_dependent_cubic_minors_are_rejected(self):
        bad=copy.deepcopy(self.witness);bad['minors'].pop()
        with self.assertRaises(ValueError):cert.verify(bad)
        bad=copy.deepcopy(self.witness);bad['minors'][1]=bad['minors'][0]
        with self.assertRaises(ValueError):cert.verify(bad)
        bad=copy.deepcopy(self.witness);bad['minors'][0][0]=[0,0,1]
        with self.assertRaises(ValueError):cert.verify(bad)

    def test_rank_gap_and_exclusion_scope_cannot_be_promoted(self):
        for key in ['all_constant_compression_pairs','general_A4_excluded',
                    'moving_compressions_excluded','independent_review',
                    'lean_formalized','improves_omega']:
            bad=copy.deepcopy(self.witness);bad[key]=not bad[key]
            with self.assertRaises(ValueError):cert.verify(bad)
        bad=copy.deepcopy(self.witness);bad['field']=1009
        with self.assertRaises(ValueError):cert.verify(bad)


if __name__=='__main__':unittest.main()
