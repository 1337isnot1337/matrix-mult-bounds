"""Exact permanent-component, weighted-cover, and trace-invariant controls."""
from collections import Counter
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import unittest


PACKAGE = Path(__file__).resolve().parents[1] / 'research/ai/2026-10-23-fixed-flip-components'
SPEC = importlib.util.spec_from_file_location('fixed_flip_components', PACKAGE / 'verify.py')
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)
TRACE_SPEC = importlib.util.spec_from_file_location('fixed_flip_trace', PACKAGE / 'trace_invariant.py')
T = importlib.util.module_from_spec(TRACE_SPEC)
TRACE_SPEC.loader.exec_module(T)


def shared_first_shear(factors, i, j):
    """An exact nontrivial elementary flip with equal first factors."""
    if factors[0][i] != factors[0][j]:
        raise ValueError('This control expects equal first factors.')
    changed = copy.deepcopy(factors)
    changed[1][i] = [a + b for a, b in zip(factors[1][i], factors[1][j])]
    changed[2][j] = [b - a for a, b in zip(factors[2][i], factors[2][j])]
    return changed


def pair_coefficients(factors, i, j):
    return [sum(factors[0][t][a] * factors[1][t][b] * factors[2][t][c] for t in (i, j))
            for a in range(20) for b in range(25) for c in range(20)]


class FixedFlipComponentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.factors = {name: V.seed(name) for name in V.SCENARIOS}
        cls.geometry = {name: V.analyze_components(factors) for name, factors in cls.factors.items()}
        cls.reports = {name: json.loads((PACKAGE / (name + '_enumeration.json')).read_text())
                       for name in V.SCENARIOS}
        cls.trace_certificate = json.loads((PACKAGE / 'trace_certificate.json').read_text())

    def test_components_and_flattening_certificates(self):
        for name, expected_checks in (('four', 4293), ('five', 4134)):
            with self.subTest(seed=name):
                components, bases, fixed, vectors, checks = self.geometry[name]
                self.assertEqual(dict(Counter(map(len, components))), V.SCENARIOS[name]['component_sizes'])
                self.assertEqual(sorted(i for group in components for i in group), list(range(76)))
                self.assertEqual(checks, expected_checks)
                self.assertEqual(len(fixed), 50)
                self.assertEqual(len(set(vectors)), 50)
                self.assertEqual(V.W.rank(vectors, 101), 20)
                # Each fixed direction really comes from a one-dimensional W span.
                self.assertEqual(sum(len(basis) == 1 for basis in bases[2]), 50)

    def test_disjointness_rejects_an_intersection(self):
        separated = [[[[1, 0]], [[0, 1]]]]
        self.assertEqual(V.certify_disjoint_spans(separated), 1)
        with self.assertRaises(ArithmeticError):
            V.certify_disjoint_spans([[[[1, 0]], [[2, 0]]]])
        # Rank over a residue field is a lower bound, not an upper bound.
        self.assertEqual(V.W.rank([[101, 0], [0, 1]]), 2)
        self.assertEqual(V.W.rank([[101, 0], [0, 1]], 101), 1)

    def test_nontrivial_flip_preserves_tensor_and_fixed_directions(self):
        for name, pair in (('four', (8, 17)), ('five', (26, 32))):
            with self.subTest(seed=name):
                original = self.factors[name]
                changed = shared_first_shear(original, *pair)
                self.assertNotEqual(changed, original)
                self.assertEqual(pair_coefficients(changed, *pair), pair_coefficients(original, *pair))
                components, _, fixed, vectors, checks = V.analyze_components(changed)
                initial_components, _, initial_fixed, initial_vectors, initial_checks = self.geometry[name]
                self.assertEqual(components, initial_components)
                self.assertEqual(fixed, initial_fixed)
                self.assertEqual(vectors, initial_vectors)
                self.assertEqual(checks, initial_checks)
                if name == 'five':
                    for group in components:
                        self.assertEqual(T.pairing(changed, group), T.pairing(original, group))

    def test_weight_report_corruption_is_rejected(self):
        for name, scenario in V.SCENARIOS.items():
            vectors = self.geometry[name][3]
            V.check_flat_report(self.reports[name], vectors, scenario)
            for key, changed_value in (
                    ('maximum_flat_weight', scenario['cap'] + 1),
                    ('four_subsets', 230299),
                    ('weighted_witness_members', [])):
                with self.subTest(seed=name, field=key):
                    changed = copy.deepcopy(self.reports[name])
                    changed[key] = changed_value
                    with self.assertRaises(ArithmeticError):
                        V.check_flat_report(changed, vectors, scenario)
            changed = copy.deepcopy(self.reports[name])
            changed['flat_weight_histogram'][str(scenario['cap'] + 1)] = 1
            with self.assertRaises(ArithmeticError):
                V.check_flat_report(changed, vectors, scenario)

    def test_quick_scope_and_retained_structural_certificate(self):
        result = V.verify()
        retained = json.loads((PACKAGE / 'certificate.json').read_text())
        self.assertEqual(result['claim_id'], 'AI-EXTERNAL-FIXED-FLIP-GRID-004')
        for name, total, cap in (('four', 148, 16), ('five', 74, 8)):
            data = result['scenarios'][name]
            self.assertEqual(data['fixed_W_total_weight'], total)
            self.assertEqual(data['rank_four_flat_weight_cap'], cap)
            self.assertEqual(data['minimum_rank_four_groups_by_weight'], 10)
            self.assertTrue(data['all_finite_standard_flips_termwise_grid_excluded'])
            self.assertFalse(data['exhaustive_enumeration_rerun_by_this_command'])
            self.assertTrue(retained['scenarios'][name]['exhaustive_enumeration_rerun_by_this_command'])
            retained['scenarios'][name]['exhaustive_enumeration_rerun_by_this_command'] = False
        self.assertEqual(result, retained)
        self.assertIn('25-dimensional target leg', result['scope']['grid_alignment'])
        self.assertIn('full generic family', result['scope']['application'])
        self.assertFalse(result['general_Q64_maps_excluded'])
        self.assertFalse(result['arbitrary_algorithms_excluded'])
        self.assertFalse(result['further_stabilizer_degenerations_excluded'])
        self.assertFalse(result['improves_omega'])

    def test_positive_trace_and_exact_retained_pairings(self):
        result = T.verify()
        self.assertEqual(T.build_certificate(), self.trace_certificate)
        self.assertEqual(result['isolated_components'], 53)
        self.assertEqual(result['individual_trace_values'], {'1': 52, '2': 24})
        self.assertEqual(result['total_surviving_trace'], 100)
        self.assertEqual(result['original_discarded_error_trace'], 0)
        self.assertTrue(result['five_split_finite_flip_subset_deletion_excluded'])
        self.assertFalse(result['four_split_subset_deletion_excluded'])
        self.assertFalse(result['general_border_rank_reduction_excluded'])
        self.assertFalse(result['improves_omega'])

    def test_trace_corruption_is_rejected(self):
        changed = copy.deepcopy(self.trace_certificate)
        group = next(record for record in changed['groups'] if len(record['indices']) == 5)
        group['pairing'][0][1] = 1
        with self.assertRaises(ValueError):
            T.verify(changed)
        changed = copy.deepcopy(self.trace_certificate)
        changed['original_discarded_term_traces'][0] = 1
        with self.assertRaises(ValueError):
            T.verify(changed)
        changed = copy.deepcopy(self.trace_certificate)
        changed['groups'].pop()
        with self.assertRaises(ValueError):
            T.verify(changed)

    @unittest.skipUnless(shutil.which('cc') or shutil.which('gcc') or shutil.which('clang'),
                         'A C99 compiler is required for the full enumeration.')
    def test_complete_fixed_direction_enumeration(self):
        for name, scenario in V.SCENARIOS.items():
            with self.subTest(seed=name):
                vectors = self.geometry[name][3]
                actual = V.W.enumerate_flats(vectors, scenario['weights'])
                V.check_flat_report(actual, vectors, scenario)
                self.assertEqual(actual, self.reports[name])


if __name__ == '__main__':
    unittest.main()
