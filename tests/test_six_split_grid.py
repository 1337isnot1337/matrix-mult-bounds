"""Exact positive fixed-direction cover and matching lower-bound controls."""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import unittest


PACKAGE = Path(__file__).resolve().parents[1] / 'research/ai/2026-10-23-six-split-grid'
SPEC = importlib.util.spec_from_file_location('six_split_grid', PACKAGE / 'verify.py')
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)


class SixSplitGridTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.geometry = V.geometry()
        cls.cover = json.loads((PACKAGE / 'cover.json').read_text())
        cls.report = json.loads((PACKAGE / 'enumeration.json').read_text())

    def test_exact_cover_and_component_geometry(self):
        components, bases, fixed, vectors, checks = self.geometry
        self.assertEqual(len(components), 52)
        self.assertEqual(checks, 3978)
        self.assertEqual(len(fixed), 47)
        self.assertEqual(V.C.W.rank(vectors, 101), 20)
        self.assertEqual(V.check_cover(self.cover, fixed, vectors), [4] * 9)
        self.assertEqual(sorted(len(basis) for basis in bases[2] if len(basis) > 1), [2, 2, 2, 2, 3])

    def test_cover_corruption_is_rejected(self):
        _, _, fixed, vectors, _ = self.geometry
        changed = copy.deepcopy(self.cover)
        changed['groups'].pop()
        with self.assertRaises(ArithmeticError):
            V.check_cover(changed, fixed, vectors)
        changed = copy.deepcopy(self.cover)
        group = changed['groups'][0]
        outside = next(i for i in range(47) if V.C.W.rank([vectors[j] for j in group + [i]]) == 5)
        group.append(outside)
        with self.assertRaises(ArithmeticError):
            V.check_cover(changed, fixed, vectors)
        changed = copy.deepcopy(self.cover)
        changed['fixed_W_representatives'][0] = 0
        with self.assertRaises(ArithmeticError):
            V.check_cover(changed, fixed, vectors)

    def test_weight_report_corruption_is_rejected(self):
        vectors = self.geometry[3]
        V.check_enumeration(self.report, vectors)
        for field, value in (('four_subsets', 178364), ('maximum_flat_weight', 17),
                             ('weighted_witness_members', [])):
            with self.subTest(field=field):
                changed = copy.deepcopy(self.report)
                changed[field] = value
                with self.assertRaises(ArithmeticError):
                    V.check_enumeration(changed, vectors)

    def test_exact_minimum_and_limited_scope(self):
        result = V.verify()
        self.assertEqual(result['claim_id'], 'AI-EXTERNAL-SIX-SPLIT-FIXED-COVER-007')
        self.assertEqual(result['fixed_W_total_weight'], 144)
        self.assertEqual(result['rank_four_flat_weight_cap'], 16)
        self.assertEqual(result['minimum_groups_from_weight'], 9)
        self.assertEqual(result['exact_minimum_rank_at_most_four_groups'], 9)
        self.assertTrue(result['all_47_fixed_directions_covered'])
        self.assertTrue(result['fixed_W_directions_permanent_under_finite_standard_flips'])
        self.assertFalse(result['full_factor_cover_constructed'])
        self.assertFalse(result['Q64_grid_constructed'])
        self.assertFalse(result['new_matrix_multiplication_algorithm'])
        self.assertFalse(result['improves_omega'])
        self.assertFalse(result['exhaustive_enumeration_rerun_by_this_command'])
        retained = json.loads((PACKAGE / 'certificate.json').read_text())
        self.assertTrue(retained['exhaustive_enumeration_rerun_by_this_command'])
        retained['exhaustive_enumeration_rerun_by_this_command'] = False
        self.assertEqual(retained, result)

    @unittest.skipUnless(shutil.which('cc') or shutil.which('gcc') or shutil.which('clang'),
                         'A C99 compiler is required for the full enumeration.')
    def test_complete_four_subset_replay(self):
        actual = V.C.W.enumerate_flats(self.geometry[3], V.WEIGHTS)
        V.check_enumeration(actual, self.geometry[3])
        self.assertEqual(actual, self.report)


if __name__ == '__main__':
    unittest.main()
