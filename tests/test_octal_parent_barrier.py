"""Independent coverage and corruption checks for the fixed-parent barrier."""
import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'research/ai/2026-10-20-octal-parent-barrier'))
import parent_barrier as barrier


class OctalParentBarrierTests(unittest.TestCase):
    def test_seed_group_relations_and_corruption(self):
        group = barrier.cubic_group()
        parent = barrier.cubic_parent(group)
        sets, rows = barrier.transformed_seed(parent, 1, (0, 0, 0), 0)
        self.assertEqual(barrier.verify_circuit(group, sets, rows), 4)
        with self.assertRaises(ValueError):
            barrier.verify_circuit(group, sets, rows[:-1])
        broken = copy.deepcopy(sets)
        broken[0][0] = parent[0][0]
        with self.assertRaises(ValueError):
            barrier.verify_circuit(group, broken, rows)

    def test_max_plus_against_small_exhaustive_cycles(self):
        for length, cap, low, high in [(3, 3, 2, 4), (4, 4, 3, 6), (5, 2, 1, 3)]:
            maxima, _ = barrier.cycle_maxima(length, cap, low, high)
            brute, count = barrier.exhaustive_maxima(length, cap, low, high)
            self.assertEqual(maxima, brute)
            self.assertEqual(count, (cap + 1) ** length)

    def test_full_orbit_table_volume_and_gate_receipt(self):
        expected = json.loads((ROOT / 'results/octal-parent-barrier-2026-10-20/certificate.json').read_text())
        result = barrier.report(exhaustive=True)
        self.assertEqual(result, expected)
        self.assertEqual(result['orbit']['support_relations_checked'], 43008)
        self.assertEqual(result['independent_enumeration']['vectors_checked'], 4782969)
        self.assertEqual(result['volume_bound']['max_volume'], 92928)
        with self.assertRaises(ValueError):
            barrier.gate_certificate(110000)


if __name__ == '__main__':
    unittest.main()
