"""Exact controls for the partial A88 endpoint construction; no NumPy."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT=Path(__file__).resolve().parents[1]
DIRECTORY=ROOT/'research/ai/2026-10-20-anisotropic-constructions'
SPEC=importlib.util.spec_from_file_location('parity_balancing_torus_anchors',
                                           DIRECTORY/'parity_balancing_torus_anchors.py')
ANCHORS=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ANCHORS)
SEED=ROOT/'results/anisotropic-constructions-2026-10-20/parity_balancing_torus_anchor_seed.json'


class TorusEndpointSeedTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads(SEED.read_text())

    def test_exact_six_slices_and_all_three_actual_map_ranks(self):
        report=ANCHORS.verify(self.data)
        self.assertEqual(report['source_terms_enumerated'],262144)
        self.assertEqual(len(report['exact_extreme_slice_checks']),6)
        self.assertTrue(all(item['nonzero_target_coefficients']==27
                            for item in report['exact_extreme_slice_checks']))
        self.assertEqual(len(report['actual_map_rank_checks']),87)
        for leg in range(3):
            blocks=[item for item in report['actual_map_rank_checks'] if item['leg']==leg]
            self.assertEqual(sum(item['rank_mod65521'] for item in blocks),778)
        self.assertTrue(report['free_columns_never_occur_beside_an_extreme_source_point'])
        self.assertEqual(report['exact_embedded_M4']['nonzero_target_coefficients'],64)
        self.assertEqual(report['exact_embedded_M4']['full_target_coefficients_checked'],4096)
        self.assertFalse(report['full_target_witness'])
        self.assertFalse(report['new_exponent_established'])

    def test_tampered_corner_is_rejected(self):
        altered=copy.deepcopy(self.data)
        altered.pop('common_map_numerators')
        anchor=altered['anchor_target_units'][0]
        entry=next(entry for entry in altered['maps'][0] if entry[0]==anchor)
        entry[2]*=2
        with self.assertRaisesRegex(ArithmeticError,'required source corner'):
            ANCHORS.verify(altered)

    def test_missing_free_row_is_rejected_despite_recorded_rank_metadata(self):
        altered=copy.deepcopy(self.data)
        altered.pop('common_map_numerators')
        free={ANCHORS.original_column(1,column)
              for column in altered['free_source_columns_common_order']}
        boundary_rows={row for row,column,_ in altered['maps'][1] if column not in free}
        free_row=next(row for row,column,_ in altered['maps'][1]
                      if column in free and row not in boundary_rows)
        altered['maps'][1]=[entry for entry in altered['maps'][1] if entry[0]!=free_row]
        # Leave both the original construction report and old verification
        # metadata untouched: neither is an acceptance certificate.
        with self.assertRaisesRegex(ArithmeticError,'not concise: leg 1'):
            ANCHORS.verify(altered)

    def test_all_zero_maps_are_rejected(self):
        altered=copy.deepcopy(self.data)
        altered['maps']=[[],[],[]]
        altered['common_map_numerators']=[]
        with self.assertRaisesRegex(ArithmeticError,'not concise'):
            ANCHORS.verify(altered)

    def test_a_free_coefficient_can_change_without_changing_any_anchor_slice(self):
        altered=copy.deepcopy(self.data)
        altered.pop('common_map_numerators')
        free=set(altered['free_source_columns_common_order'])
        core=set(altered['m4_target_vertices'])
        entry=next(entry for entry in altered['maps'][0]
                   if entry[1] in free and not (entry[0]<729 and
                       entry[0]//27 in core and entry[0]%27 in core))
        entry[2]*=2
        report=ANCHORS.verify(altered)
        self.assertTrue(report['three_actual_maps_concise_by_recomputed_modular_ranks'])
        self.assertEqual(len(report['exact_extreme_slice_checks']),6)

    def test_historical_hadamard_seed_remains_only_a_six_slice_control(self):
        historical=SEED.with_name('parity_balancing_torus_anchor_hadamard_seed.json')
        report=ANCHORS.verify(json.loads(historical.read_text()))
        self.assertTrue(report['three_actual_maps_concise_by_recomputed_modular_ranks'])
        self.assertNotIn('exact_embedded_M4',report)
        self.assertFalse(report['full_target_witness'])

    def test_bad_sparse_map_structure_is_rejected(self):
        changes=[('map count',lambda data:data['maps'].pop()),
                 ('zero denominator',lambda data:data.update(map_denominator=0)),
                 ('negative denominator',lambda data:data.update(map_denominator=-1)),
                 ('noninteger denominator',lambda data:data.update(map_denominator=64.0)),
                 ('duplicate entry',lambda data:data['maps'][0].append(data['maps'][0][0].copy())),
                 ('out of range row',lambda data:data['maps'][0][0].__setitem__(0,778)),
                 ('out of range column',lambda data:data['maps'][0][0].__setitem__(1,960))]
        for name,change in changes:
            with self.subTest(name=name):
                altered=copy.deepcopy(self.data)
                change(altered)
                with self.assertRaises((ValueError,ArithmeticError)):
                    ANCHORS.verify(altered)


if __name__=='__main__':
    unittest.main()
