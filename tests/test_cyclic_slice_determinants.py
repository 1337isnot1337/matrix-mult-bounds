"""Unimodular calibration, source frame, reducedness witnesses and corruption."""

import copy
import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-21-cyclic-slice-determinants'
spec=importlib.util.spec_from_file_location('cyclic_slice_determinant_certificate',PACKAGE/'certify.py')
certificate=importlib.util.module_from_spec(spec)
spec.loader.exec_module(certificate)


class CyclicSliceDeterminantTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=json.loads((ROOT/'results/cyclic-slice-determinants-2026-10-21/certificate.json').read_text())

    def test_unimodular_interval_controls(self):
        for a in range(1,11):
            blocks=certificate.interval_blocks(a)
            self.assertEqual(len(blocks),3*a-2)
            self.assertEqual(sum(b['dimension'] for b in blocks),a*(2*a-1))
            self.assertTrue(all(b['absolute_determinant']==1 for b in blocks))

    def test_source_frame_matches_existing_literal_source(self):
        path=ROOT/'research/ai/2026-10-20-koszul/cyclic_finite_target.py'
        spec=importlib.util.spec_from_file_location('cyclic_existing_literal_source',path)
        source=importlib.util.module_from_spec(spec);spec.loader.exec_module(source)
        from itertools import product
        for a in [2,3,4]:
            f=certificate.integer_slice(a)
            expected=[[source.slice_entry(f,a,row,column)
                       for column in product(range(2*a-1),range(a),range(a))]
                      for row in product(range(a),range(a),range(2*a-1))]
            self.assertEqual(certificate.source_matrix(a,f),expected)

    def test_all_exact_pencil_certificates_and_regeneration(self):
        self.assertEqual(len(certificate.verify_report(self.report)),3)
        for w in self.report['witnesses']:
            receipt=certificate.verify(w)
            self.assertEqual(receipt['krylov_rank'],w['dimension'])
            self.assertTrue(receipt['pencil_squarefree'])
            self.assertTrue(receipt['global_source_determinant_reduced'])
            self.assertEqual(receipt['normalized_commutator_rank'],w['dimension'])
            self.assertFalse(receipt['improves_omega'])
            self.assertEqual(certificate.generate(w['size']),w)

    def test_corrupted_cyclic_relation_bezout_and_scope_are_rejected(self):
        w=next(w for w in self.report['witnesses'] if w['size']==2)
        for field in ['characteristic_coefficients_low_first','bezout_polynomial']:
            bad=copy.deepcopy(w);bad[field][0]=(bad[field][0]+1)%1009
            with self.assertRaises(ValueError):certificate.verify(bad)
        bad=copy.deepcopy(w);bad['cyclic_vector']=[0]*bad['dimension']
        with self.assertRaises(ValueError):certificate.verify(bad)
        bad=copy.deepcopy(w);bad['scope']='All tensor degenerations excluded'
        with self.assertRaises(ValueError):certificate.verify(bad)
        bad=copy.deepcopy(w);bad['commutator_slice']=[0]*bad['dimension']
        with self.assertRaises(ValueError):certificate.verify(bad)
        bad=copy.deepcopy(self.report);bad['witnesses'].pop()
        with self.assertRaises(ValueError):certificate.verify_report(bad)
        bad=copy.deepcopy(self.report);bad['proof_status']='formalized'
        with self.assertRaises(ValueError):certificate.verify_report(bad)


if __name__=='__main__':unittest.main()
