"""Exact reference and recorded-history controls; no NumPy dependency."""
import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = ROOT/'research/ai/2026-10-20-paired-direct-sums'
sys.path.insert(0, str(DIRECTORY))
SPEC = importlib.util.spec_from_file_location('q_product_projection_checked', DIRECTORY/'q_product_projection.py')
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


class ProductProjectionTests(unittest.TestCase):
    def test_complete_rational_reference_coefficients_and_repair_minors(self):
        for n, error, positions in [(5, [0, 1], 4096), (6, [19, 100], 10000), (7, [11, 36], 20736)]:
            with self.subTest(n=n):
                result = CHECK.verify(n)
                self.assertEqual(result['exact_relative_squared_error'], error)
                self.assertEqual(result['all_target_coefficient_positions_checked'], positions)
                self.assertEqual(result['fixed_reference_repair_border_rank_lower_bound'], (n-5)**2)
                self.assertEqual(result['exact_matrix_multiplication_target_reached'], n == 5)

    def test_three_complete_pilot_histories(self):
        results = ROOT/'results/paired-direct-sums-2026-10-20'
        audit = json.loads((results/'q-metaplectic-history-audit.json').read_text())
        count = 0
        for pilot in audit['pilots']:
            saved = json.loads((results/pilot['artifact']).read_text())
            completed = saved['completed_run']
            self.assertEqual(completed['history'], pilot['original_history_records'])
            self.assertEqual(completed['iterations_completed'], 1000)
            self.assertEqual(completed['actual_stop_reason'], 'iteration_budget')
            self.assertEqual(saved['discovery_checkpoint_sha256'], pilot['original_discovery_checkpoint_sha256'])
            count += len(pilot['original_history_records'])
        self.assertEqual(count, 123)


if __name__ == '__main__':
    unittest.main()
