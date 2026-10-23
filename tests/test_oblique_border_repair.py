"""Replay integer core and complete paired-source degeneration certificates."""

import copy
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest


PACKAGE=Path(__file__).resolve().parents[1]/'research/ai/2026-10-23-oblique-border-repair'
if not PACKAGE.is_dir():
    PACKAGE=Path(__file__).resolve().parent
sys.path.insert(0,str(PACKAGE))
SPEC=importlib.util.spec_from_file_location('oblique_border_six',PACKAGE/'border_six.py')
MODULE=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
from grid_karatsuba import certificate as scalar_certificate


class ObliqueBorderRepairTests(unittest.TestCase):
    def test_complete_core_polynomial_identity(self):
        terms,core,error=MODULE.canonical_core()
        report=MODULE.verify_identity(terms,core,error)
        self.assertEqual(report['rank_one_polynomial_terms'],6)
        self.assertEqual(report['first_nonzero_degree'],2)
        layers=MODULE.layers(MODULE.expand(terms))
        self.assertEqual(set(layers),{2,3,4})
        self.assertEqual(layers[2],core)
        for a in range(3):
            for b in range(5):
                for c in range(5):
                    key=a,b,c
                    self.assertEqual(layers[3].get(key,0),error.get(key,0)-core.get(key,0))
                    self.assertEqual(layers[4].get(key,0),-error.get(key,0))

    def test_koszul_unit_minor_and_false_record(self):
        report=MODULE.koszul_certificate()
        self.assertEqual(report['minor_determinant'],1)
        self.assertEqual(report['border_rank_lower_bound'],6)
        source=json.loads((PACKAGE/'core-koszul.json').read_text())
        source['koszul_matrix'][0][5]=0
        with tempfile.TemporaryDirectory() as temporary:
            path=Path(temporary)/'false-koszul.json'
            path.write_text(json.dumps(source))
            with self.assertRaises(ArithmeticError):
                MODULE.koszul_certificate(path)

    def test_complete_saved_certificate_and_pinned_sources(self):
        current_report=MODULE.build_certificate(PACKAGE.parents[2])
        saved_report=json.loads((PACKAGE/'witness.json').read_text())
        self.assertEqual(len(current_report['controls']),72)
        self.assertEqual(current_report['source_pin_verification'],
                         {'checked':4,'all_match':True})
        self.assertEqual(current_report,saved_report)
        current,saved=current_report['n6_witness'],saved_report['n6_witness']
        self.assertEqual(current['border_rank_upper_bound'],18)
        self.assertEqual(current['source_format'],[54,54,54])
        self.assertEqual(current['target_format'],[25,20,20])
        self.assertTrue(MODULE.replay_combined_record(saved))
        self.assertFalse(current['whole_residual_border_rank_optimality_claimed'])
        self.assertFalse(current['improves_omega'])

    def test_wrong_leading_map_coefficient_is_rejected(self):
        current=MODULE.combined_source_witness(6,4)
        current['polynomial_local_maps'][0].append([0,0,0,1])
        with self.assertRaises(ArithmeticError):
            MODULE.replay_combined_record(current)
        terms,core,error=MODULE.canonical_core()
        changed=copy.deepcopy(terms)
        changed[0][2][(1,2)]+=1
        with self.assertRaises(ArithmeticError):
            MODULE.verify_identity(changed,core,error)

    def test_disjoint_core_family_and_native_source_controls(self):
        for b in range(2,8):
            for d in range(7):
                n=b+1+d;r=n-1;m=min(d,b-1)
                report,_,_=MODULE.repair_family(n,b,raw=(b,d) in {(4,2),(4,3),(4,4),(2,3)})
                self.assertEqual(report['border_rank_upper_bound'],4*r*d-2*m*m)
                self.assertEqual(report['cores'],m*m)
                self.assertEqual(report['first_nonzero_degree'],2 if d else None)
        self.assertTrue(MODULE.replay_combined_record(MODULE.combined_source_witness(5,4)))

    def test_ordinary_and_border_counts_are_distinct(self):
        for n,ordinary,border in [(6,19,18),(7,44,40),(8,75,66),(9,119,110)]:
            report=scalar_certificate(n,4,raw=True)
            self.assertEqual(report['scalar_rank_upper_bound'],ordinary)
            report,_,_=MODULE.repair_family(n,4)
            self.assertEqual(report['border_rank_upper_bound'],border)

    def test_invalid_family_and_inexact_polynomial_inputs(self):
        for n,b in [(3,3),(4,1),(True,2),(6,2.0)]:
            with self.assertRaises(ValueError):
                MODULE.repair_family(n,b)
        for entries in [[(0,-1,1)],[(0,0,0.5)],[(0,False,1)]]:
            with self.assertRaises(ValueError):
                MODULE.vec(entries)


if __name__=='__main__':
    unittest.main()
