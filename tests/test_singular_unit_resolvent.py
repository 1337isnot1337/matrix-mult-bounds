"""Exact source and nonvanishing-minor evidence for the resolvent chart."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-21-singular-unit-resolvent'
spec=importlib.util.spec_from_file_location('singular_unit_resolvent_certificate',PACKAGE/'certify.py')
cert=importlib.util.module_from_spec(spec);spec.loader.exec_module(cert)


class SingularUnitResolventTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.witness=json.loads((ROOT/'results/singular-unit-resolvent-2026-10-21/certificate.json').read_text())

    def test_complete_exact_source_minor_and_invariant_replay(self):
        receipt=cert.verify(self.witness)
        self.assertEqual(receipt['minor_rank_mod_1009'],112)
        self.assertEqual(receipt['explicit_invariant_dimension'],16)
        self.assertTrue(receipt['all_finite_first_map_poles'])
        self.assertFalse(receipt['general_A4_excluded'])
        self.assertEqual(cert.build()[0],self.witness)

    def test_literal_sparse_source_agrees_with_full_maintained_source(self):
        labels=[(2,1,2,0),(3,2,2,1)]
        labels.extend((4,i,k,s) for i,k,s in cert.product(range(4),range(7),range(4)))
        for a,i,k,s in labels:
            n=a*a*(2*a-1);f=[0]*n;f[(i*(2*a-1)+k)*a+s]=1
            dense=cert.src.source_matrix(a,f)
            expected=[{j:x for j,x in enumerate(row) if x} for row in dense]
            self.assertEqual(cert.literal(a,i,k,s),expected)

    def test_corrupted_or_repeated_minor_indices_are_rejected(self):
        for field in ['minor_rows','minor_columns']:
            bad=copy.deepcopy(self.witness);bad[field][1]=bad[field][0]
            with self.assertRaises(ValueError):cert.verify(bad)
        bad=copy.deepcopy(self.witness);bad['rank']=111
        with self.assertRaises(ValueError):cert.verify(bad)

    def test_rank_hypothesis_and_ansatz_scope_cannot_be_removed(self):
        for key in ['requires_full_candidate_rank','requires_fixed_unit_resolvent_ansatz']:
            bad=copy.deepcopy(self.witness);bad.pop(key)
            with self.assertRaises(ValueError):cert.verify(bad)
        for key in ['all_singular_units_excluded','independent_review','lean_formalized','improves_omega']:
            bad=copy.deepcopy(self.witness);bad[key]=True
            with self.assertRaises(ValueError):cert.verify(bad)


if __name__=='__main__':unittest.main()
