"""Exact exhaustive subgroup/ideal replay and incomplete-catalog controls."""
import copy
import gzip
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-23-sl2-f8-subgroup-catalog'
spec=importlib.util.spec_from_file_location('checked_f8_subgroup_catalog',PACKAGE/'verify.py')
verify=importlib.util.module_from_spec(spec);spec.loader.exec_module(verify)


class SL2F8SubgroupCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with gzip.open(ROOT/'results/sl2-f8-subgroup-catalog-2026-10-23/certificate.json.gz','rt') as handle:
            cls.report=json.load(handle)
        cls.group=verify.helper.projection.group()

    def test_complete_exact_lattice_ideals_and_all_target_cuts(self):
        self.__class__.receipt=verify.verify(self.report)
        result=self.receipt
        self.assertEqual((result['subgroups'],result['conjugacy_classes']),(386,12))
        self.assertEqual(result['target_formats'],16)
        dimensions={r['subgroup_order']:r['ideal_dimension'] for r in result['class_dimensions']}
        self.assertEqual(dimensions[14],308)
        self.assertEqual(dimensions[6],455)
        self.assertTrue(result['dihedral14_structure']['dihedral_relation_verified'])
        self.assertEqual(result['formats'][0]['minimal_cosets_per_leg'],[3431,3431,2647])
        self.assertEqual(sum(7056+1296==n for row in result['formats'] for n in row['new_cosets_per_leg']),10)
        self.assertTrue(result['new_cut_control']['prior_8_9_18_coset_filters_pass'])
        self.assertFalse(result['all_coordinate_targets_excluded'])

    def test_missing_subgroup_extension_and_target_format_are_rejected(self):
        rows=copy.deepcopy(self.report['subgroups'])
        rows.remove(next(r for r in rows if len(r['members'])==2))
        with self.assertRaises(ValueError):verify.verify_lattice(self.group,rows)
        bad=copy.deepcopy(self.report);bad['formats'].pop()
        with self.assertRaises(ValueError):verify.verify(bad)
        bad=copy.deepcopy(self.report);bad['general_complex_maps_excluded']=True
        with self.assertRaises(ValueError):verify.verify(bad)

    def test_actual_lower_minor_and_integer_projection_must_both_hold(self):
        row=next(r for r in self.report['ideal_classes'] if len(r['subgroup'])==14)
        _,cosets=verify.helper.conjugates_and_cosets(self.group,row['subgroup'])
        bad=list(cosets);bad[row['lower_minor_cosets'][0]]=()
        with self.assertRaises(ValueError):
            verify.verify_minor(bad,row['lower_minor_cosets'],row['lower_minor_columns'],308)
        with self.assertRaises(ValueError):
            verify.helper.projection.verify_projection(row['subgroup'],['0']*9,308)
        with self.assertRaises(ValueError):
            verify.helper.projection.verify_projection(row['subgroup'],row['central_projection'],307)

    def test_minimality_coverage_and_new_cut_control(self):
        classes=[]
        for row in self.report['ideal_classes']:
            if len(row['subgroup']) not in [8,9,14,18]:continue
            conjugates,cosets=verify.helper.conjugates_and_cosets(self.group,row['subgroup'])
            classes.append({'subgroup':row['subgroup'],'order':len(row['subgroup']),
                            'dimension':row['ideal_dimension'],'conjugates':conjugates,'cosets':cosets})
        saved=self.report['formats'][0]['minimal_cuts']
        bad=copy.deepcopy(saved);bad[0]=[r for r in bad[0] if r['subgroup_order']!=14]
        with self.assertRaises(ValueError):verify.verify_minimal_summaries(classes,[18,18,25],bad)
        bad=copy.deepcopy(saved);bad[0].append({'subgroup_order':18,'ideal_dimension':244,
                                            'conjugate_subgroups':28,'cosets':784})
        with self.assertRaises(ValueError):verify.verify_minimal_summaries(classes,[18,18,25],bad)
        bad=copy.deepcopy(self.report['new_cut_control']);bad['leg']=1
        with self.assertRaises(ValueError):verify.verify_new_cut_control(classes,bad)


if __name__=='__main__':unittest.main()
