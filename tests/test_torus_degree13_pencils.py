import copy
import importlib.util
from itertools import product
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'research/ai/2026-10-20-anisotropic-constructions/torus_degree13_pencils.py'
SPEC = importlib.util.spec_from_file_location('torus_degree13_pencils', PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class DegreeThirteenPencilTests(unittest.TestCase):
    def test_saved_exact_report_and_product_grid_tamper(self):
        expected = json.loads((ROOT / 'results/anisotropic-constructions-2026-10-20/torus-degree13-pencils.json').read_text())
        actual = MODULE.report()
        self.assertEqual(actual, expected)
        self.assertEqual(actual['product_grids']['product_grid_coefficients_checked'], 17280)
        tampered = [list(row) for row in copy.deepcopy(MODULE.NEGATIVE_GRID)]
        tampered[0][0] = (0, 7, 7)
        with self.assertRaisesRegex(ArithmeticError, 'product-grid coefficient'):
            MODULE.verify_product_grids(negative_grid=tampered)

    def test_all_boolean_assignments_give_only_stated_normal_forms(self):
        # Independent representation: twelve Boolean incidences, not four
        # location variables. This checks the cyclic indexing and all masks.
        survivors = []
        at_most_one = 0
        for bits in product((False, True), repeat=12):
            a, b, c, d = [bits[3 * k:3 * k + 3] for k in range(4)]
            if any(sum(row) > 1 for row in (a, b, c, d)):
                continue
            at_most_one += 1
            if any((a[i] and c[j]) or (b[i] and d[j])
                   for i in range(3) for j in range(3) if i != j):
                continue
            if any((b[i] or d[(i + 1) % 3]) and not (a[i] or c[(i + 1) % 3])
                   for i in range(3)):
                continue
            if any((c[i] or a[(i + 1) % 3]) and not (d[i] or b[(i + 1) % 3])
                   for i in range(3)):
                continue
            survivors.append(tuple(next((i for i, value in enumerate(row) if value), -1)
                                   for row in (a, b, c, d)))
        expected = {(-1, -1, -1, -1)}
        for i in range(3):
            expected.update(((i, i, -1, -1), (-1, -1, i, i), (i, i, i, i)))
        self.assertEqual(at_most_one, 256)
        self.assertEqual(set(survivors), expected)
        self.assertEqual(MODULE.pattern_report()['patterns_after_all_contradictions'], 0)

    def test_opposite_products_and_independent_diagonal_contradictions(self):
        self.assertEqual(MODULE.trace_form((0, 14, 1), (6, 0, 7)), {})
        self.assertEqual(MODULE.trace_form((6, 0, 7), (0, 14, 1)), {(7, 7, 0): 1})
        cases = MODULE.verify_cross_types()
        self.assertEqual(len(cases), 4)
        for case in cases:
            self.assertNotEqual(case['forced_target_diagonal'], case['required_independent_target_diagonal'])
        self.assertEqual(MODULE.verify_generic_identities()['formal_polynomial_identities_checked'], 10)
        self.assertFalse(MODULE.report()['generic_pair_identities']['extreme_scalar_values_normalized'])


if __name__ == '__main__':
    unittest.main()
