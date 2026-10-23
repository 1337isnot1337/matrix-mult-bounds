"""Exact controls for the geometric Hankel bound in all characteristics."""
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-23-hankel-all-characteristics'
SPEC = importlib.util.spec_from_file_location('hankel_all_characteristics', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class HankelAllCharacteristicsTests(unittest.TestCase):
    def test_complete_finite_report(self):
        saved = json.loads((ROOT / 'results/hankel-all-characteristics-2026-10-23/controls.json').read_text())
        self.assertEqual(verify.report(), saved)
        self.assertEqual(sum(saved['nonzero_evaluation_fibers'].values()), 911)
        self.assertEqual(sum(saved['monomial_assignment_cases'].values()), 882)
        self.assertFalse(saved['independent_review'])
        self.assertFalse(saved['improves_omega'])

    def test_doubled_diagonal_drops_real_constraints_in_characteristic_two(self):
        self.assertEqual(verify.assignment_dimension(2, 4, [0, 2], 2), 1)
        self.assertEqual(verify.assignment_dimension(2, 4, [0, 2], 2, True), 7)
        # The discarded diagonal permits h0=(1,0,0,0,0), h1=0.
        # Its square parameter coefficient is 1, so it is not an assignment.
        self.assertEqual(verify.contraction([1, 0]), [[1, 0, 0], [0, 1, 0]])
        for prime in (3, 5):
            self.assertEqual(verify.assignment_dimension(2, 4, [0, 2], prime), 1)
            self.assertEqual(verify.assignment_dimension(2, 4, [0, 2], prime, True), 1)

    def test_rank_uses_the_field_not_rational_arithmetic(self):
        matrix = [[1, 1], [1, -1]]
        self.assertEqual(verify.rank_mod(matrix, 2), 1)
        self.assertEqual(verify.rank_mod(matrix, 3), 2)

    def test_pinned_local_sources(self):
        sources = json.loads((PACKAGE / 'sources.json').read_text())
        for item in sources['local_dependencies']:
            with self.subTest(path=item['path']):
                self.assertEqual(hashlib.sha256((ROOT / item['path']).read_bytes()).hexdigest(), item['sha256'])


if __name__ == '__main__':
    unittest.main()
