"""Independent small partition enumeration and exact frontier replay."""

import importlib.util
import json
from math import isqrt
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT/'research/ai/2026-10-20-anisotropic-constructions/square_sum_frontier.py'
SPEC = importlib.util.spec_from_file_location('square_sum_frontier', PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def partitions(total, largest):
    if total == 0:
        yield []
    for n in range(min(largest, isqrt(total)), 0, -1):
        for tail in partitions(total-n*n, n):
            yield [n]+tail


class SquareSumFrontierTests(unittest.TestCase):
    def test_small_dynamic_program_against_partitions(self):
        for a, b in ((2, 2), (2, 3), (3, 3), (3, 4)):
            size = a*b*(a+b-1)
            for d in range(1, size+1):
                expected = []
                for shape in partitions(d, isqrt(d)):
                    loss = size-d
                    if any(n+2*loss < a*b for n in shape):
                        continue
                    if any(n > 1 and n+2*loss < 2*a*b for n in shape):
                        continue
                    upper_r = min(a-1, b-1, (a+b-1)//3)
                    if any(n*n > r*a*b and n+2*loss < (r+1)*a*b
                           for n in shape for r in range(1, upper_r+1)):
                        continue
                    if min(a, b) >= 3 and a+b-1 >= 6 and any(
                            n >= 3 and n+2*loss == 2*a*b for n in shape):
                        continue
                    if shape.count(1) > 1 and 2+2*loss < 2*a*b:
                        continue
                    expected.append(sum(MODULE.score_interval(n)[1] for n in shape))
                actual = MODULE.dimension_frontier(a, b, d)['upper_score_numerator']
                self.assertEqual(actual, max(expected) if expected else None)

    def test_full_saved_frontier(self):
        expected = json.loads((ROOT/'results/anisotropic-constructions-2026-10-20/square-sum-frontier.json').read_text())
        actual = MODULE.report()
        self.assertEqual(actual, expected)
        self.assertEqual(actual['source_count'], 52)
        self.assertEqual(actual['first_passing_source_dimension'], 784)
        self.assertTrue(all(r['all_partitions_below_critical_score']
                            for r in actual['source_frontiers'] if r['source_leg_dimension'] < 784))
        row = next(r for r in actual['source_frontiers'] if r['a'] == r['b'] == 5)
        self.assertEqual(row['maximum']['upper_score_numerator'], 18916994428)
        self.assertLess(18916994428, 21952*MODULE.SCALE)
        self.assertFalse(actual['new_exponent_established'])

    def test_conditional_integer_certificate(self):
        self.assertGreater(150**2247, 77567**1000)
        self.assertGreater(30**2247, 2084**1000)
        self.assertGreater(77567+2084, 43**3)
        self.assertTrue(MODULE.admissible_partition(7, 8, [25, 5]))
        self.assertFalse(MODULE.admissible_partition(5, 6, [16]))
        self.assertFalse(MODULE.admissible_partition(5, 6, [16, 4]))
        self.assertFalse(MODULE.admissible_partition(5, 6, [16, 3, 3]))


if __name__ == '__main__':
    unittest.main()
