"""Exact frontier replay, source pins and changed-certificate controls."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-23-oblique-longmap-frontier'
SPEC = importlib.util.spec_from_file_location('oblique_longmap_frontier', PACKAGE/'frontier.py')
FRONTIER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(FRONTIER)


class ObliqueLongmapFrontierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.saved = json.loads((PACKAGE/'certificate.json').read_text())

    def test_complete_saved_certificate_and_all_source_pins(self):
        rebuilt = FRONTIER.build_certificate()
        self.assertEqual(rebuilt, self.saved)
        replayed = FRONTIER.verify_certificate(self.saved)
        self.assertEqual(replayed['shift_candidates'], 384)
        self.assertEqual(replayed['nonsingular_mixed_corners'], 61)
        self.assertEqual(replayed['singular_modular_decoders'], 20)
        self.assertEqual(rebuilt['source_pin_verification'], {'checked': 5, 'all_match': True})

    def test_surjective_benchmark_and_all_field_minor(self):
        fixed = self.saved['fixed_good_rows']
        self.assertEqual(fixed['unit_minor_determinant'], 1)
        self.assertEqual(FRONTIER.determinant(fixed['one_factor_unit_minor']), 1)
        benchmark = fixed['benchmark']
        self.assertTrue(all(abs(x['determinant']) == 1 for x in benchmark['long_map_unit_minors']))
        self.assertEqual(benchmark['minimum_first_map_report']['minimum_first_residual_rank'], 9)
        native = benchmark['native_verification']
        self.assertEqual(native['source_terms_reconstructed'], 576)
        self.assertEqual(native['all_target_coefficient_positions_accounted_for'], 10000)
        self.assertEqual(native['exact_residual_flattening_ranks'], [9, 18, 18])
        self.assertFalse(fixed['arbitrary_filler_equality_claimed'])

    def test_changed_unit_minor_and_scope_are_rejected(self):
        changed = copy.deepcopy(self.saved['fixed_good_rows'])
        changed['unit_minor_columns'][-1] = changed['unit_minor_columns'][0]
        with self.assertRaises(ArithmeticError):
            FRONTIER.verify_fixed_good(changed)
        changed = copy.deepcopy(self.saved['fixed_good_rows'])
        changed['arbitrary_filler_equality_claimed'] = True
        with self.assertRaises(ArithmeticError):
            FRONTIER.verify_fixed_good(changed)

    def test_last_shift_minor_and_missing_grid_control_are_rejected(self):
        changed = copy.deepcopy(self.saved['shift_controls'][-1])
        changed['minor']['columns'][-1] = changed['minor']['columns'][0]
        with self.assertRaises(ArithmeticError):
            FRONTIER.check_shift_record(changed)
        changed = copy.deepcopy(self.saved)
        changed['shift_controls'].pop()
        with self.assertRaises(ArithmeticError):
            FRONTIER.verify_certificate(changed)

    def test_last_valid_corner_and_false_singular_status_are_rejected(self):
        valid = [x for x in self.saved['mixed_corner_controls'] if x['status'] == 'exact_corner_and_injective']
        changed = copy.deepcopy(valid[-1])
        changed['minor']['columns'][-1] = changed['minor']['columns'][0]
        with self.assertRaises(ArithmeticError):
            FRONTIER.check_corner_record(changed)
        changed = copy.deepcopy(valid[-1])
        changed['status'] = 'singular_decoder_mod_prime'
        with self.assertRaises(ArithmeticError):
            FRONTIER.check_corner_record(changed)
        changed = copy.deepcopy(self.saved)
        changed['mixed_corner_controls'].pop()
        with self.assertRaises(ArithmeticError):
            FRONTIER.verify_certificate(changed)

    def test_false_source_pin_is_rejected(self):
        manifest = json.loads((PACKAGE/'sources.json').read_text())
        manifest['local_sources'][-1]['sha256'] = '0'*64
        with self.assertRaises(ArithmeticError):
            FRONTIER.verify_sources(manifest=manifest)

    def test_sparse_native_contraction_and_full_first_map_controls(self):
        controls = [FRONTIER.shift_grid()[0], FRONTIER.shift_grid()[-1]]
        for parameters in controls:
            maps = FRONTIER.shifted_maps(parameters)
            sparse = FRONTIER.sparse_slices(maps[1], maps[2])
            dense = FRONTIER.EXACT.source_slices(6, 4, (5, 4, 5), maps[1], maps[2], FRONTIER.PRIME)
            self.assertEqual(sparse, [{i: x for i, x in enumerate(row) if x} for row in dense])
            source_rank = len(FRONTIER.rank_minor(sparse)['rows'])
            quotient_rank = len(FRONTIER.rank_minor(FRONTIER.quotient_by_target(sparse))['rows'])
            _, exact = FRONTIER.EXACT.minimum_first_residual(6, 4, (5, 4, 5), maps[1], maps[2])
            self.assertEqual(25-source_rank+quotient_rank, exact['minimum_first_residual_rank'])
            self.assertGreaterEqual(exact['minimum_first_residual_rank'], 9)
        corner = FRONTIER.mixed_corner_maps([1, 1, 0, 0], prime=None)
        image, _ = FRONTIER.EXACT.contract(6, 4, (4, 4, 4), corner)
        self.assertEqual(image, FRONTIER.EXACT.matrix_multiplication((4, 4, 4)))
        rows = FRONTIER.EXACT.source_slices(6, 4, (4, 4, 4), corner[1], corner[2])
        self.assertEqual(FRONTIER.EXACT.row_space(rows)[0], 36)
        with self.assertRaises(ValueError):
            FRONTIER.shifted_maps([0, 1, 1, 1, 1, 1, False])
        with self.assertRaises(ValueError):
            FRONTIER.mixed_corner_maps([0, 0, 0, 0.5])


if __name__ == '__main__':
    unittest.main()
