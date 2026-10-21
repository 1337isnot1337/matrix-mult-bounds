import copy
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'research/ai/2026-10-20-anisotropic-constructions/torus_affine_slices.py'
SPEC = importlib.util.spec_from_file_location('torus_affine_slices', PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class TorusAffineSliceTests(unittest.TestCase):
    def test_complete_affine_system_rebuilt_from_the_actual_seed(self):
        directory = ROOT / 'results/anisotropic-constructions-2026-10-20'
        seed_path = directory / 'parity_balancing_torus_anchor_seed.json'
        expected = json.loads((directory / 'torus-affine-slices-corrected.json').read_text())
        self.assertEqual(hashlib.sha256(seed_path.read_bytes()).hexdigest(), expected['seed_sha256'])
        actual = MODULE.report(json.loads(seed_path.read_text()))
        self.assertEqual(
            {key: value for key, value in actual.items() if key != 'elapsed_seconds'},
            {key: value for key, value in expected.items() if key not in ('elapsed_seconds', 'seed_sha256')},
        )

    def test_all_free_basis_conditions_and_fixed_boundary_contradiction(self):
        path = ROOT / 'results/anisotropic-constructions-2026-10-20/torus-affine-slices-direct-control.json'
        actual = MODULE.fixed_boundary_contradiction_control()
        self.assertEqual(actual, json.loads(path.read_text()))
        self.assertEqual(actual['source_free_columns_checked'], 722)
        self.assertEqual((actual['forced_coefficient'], actual['required_target_coefficient']), (1, 0))

    def test_exact_rational_feasible_point_and_inconsistent_combination(self):
        records = [{'row': {0: 2, 1: 1}, 'rhs': 2},
                   {'row': {1: 2}, 'rhs': 1},
                   {'row': {1: 2, 2: 2}, 'rhs': 3}]
        solved = MODULE.exact_eliminate(records, {3: -2})
        self.assertTrue(solved['feasible'])
        self.assertEqual(solved['solution'], {0: Fraction(3, 4), 1: Fraction(1, 2),
                                              2: Fraction(1), 3: Fraction(-2)})
        impossible = [{'row': {0: 1, 1: 1}, 'rhs': 3},
                      {'row': {0: 2, 1: 2}, 'rhs': 7}]
        result = MODULE.exact_eliminate(impossible)
        self.assertFalse(result['feasible'])
        self.assertNotEqual(MODULE.verify_contradiction(impossible, result['certificate']), 0)
        tampered = copy.deepcopy(impossible)
        tampered[1]['rhs'] = 6
        with self.assertRaisesRegex(ArithmeticError, 'contradiction is invalid'):
            MODULE.verify_contradiction(tampered, result['certificate'])

    def test_saved_source_coefficient_contradiction_and_tamper(self):
        path = ROOT / 'results/anisotropic-constructions-2026-10-20/torus-affine-slices-corrected.json'
        data = json.loads(path.read_text())
        records, combination = [], {}
        for i, record in enumerate(data['inconsistent_equation_combination']):
            row = {tuple(entry[:3]): entry[3] for entry in record['linear_coefficients']}
            records.append({'row': row, 'rhs': record['rhs']})
            combination[i] = Fraction(*record['multiplier'])
        self.assertEqual(MODULE.verify_contradiction(records, combination), -1)
        self.assertEqual(data['inconsistent_equation_combination'][0]['equation_key'], [0, 25, 726, 707])
        tampered = copy.deepcopy(records)
        tampered[0]['rhs'] = 0
        with self.assertRaisesRegex(ArithmeticError, 'contradiction is invalid'):
            MODULE.verify_contradiction(tampered, combination)


if __name__ == '__main__':
    unittest.main()
