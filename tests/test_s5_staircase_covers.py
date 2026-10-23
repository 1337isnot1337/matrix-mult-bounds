"""Literal small support controls and full finite staircase census replay."""

from hashlib import sha256
import importlib.util
from itertools import combinations_with_replacement, product
import json
from math import comb
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-23-s5-staircase-covers'
spec = importlib.util.spec_from_file_location('s5_staircase_census', PACKAGE/'staircases.py')
census = importlib.util.module_from_spec(spec)
spec.loader.exec_module(census)


def triples(n):
    return [v for v in product(range(n+1), repeat=3) if sum(v) <= n]


def covers(cuts, principal, central):
    return all(any(p[i] <= cuts[i][e[i]] for i in range(3))
               for p in principal for e in central)


class S5StaircaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT/'results/s5-staircase-covers-2026-10-23/census.json').read_text())

    def test_complete_census_reproduces_all_eight_minima(self):
        self.assertEqual(census.export(), self.report)
        self.assertEqual(self.report['total_first_staircases_checked'], 891888)
        self.assertEqual(self.report['improved_word_count'], 0)

    def test_minimal_third_threshold_against_literal_small_supports(self):
        for maximum in range(3):
            for k in range(3):
                principal, central = triples(maximum), triples(k)
                for ascending in combinations_with_replacement(range(-1, maximum+1), k+1):
                    first = list(reversed(ascending))
                    third = census.third_leg(first, maximum)
                    self.assertTrue(covers([first, first, third], principal, central))
                    for other in product(range(-1, maximum+1), repeat=k+1):
                        predicted = all(x >= y for x, y in zip(other, third))
                        self.assertEqual(covers([first, first, other], principal, central), predicted)

    def test_saved_witnesses_cover_majorants_and_count_every_staircase(self):
        pin = self.report['source_pin']
        self.assertEqual(sha256((ROOT/pin['path']).read_bytes()).hexdigest(), pin['sha256'])
        for row in self.report['rows']:
            j, k = row['principal_factors'], row['central_factors']
            cuts = row['cutoffs']
            self.assertEqual(cuts[0], cuts[1])
            self.assertTrue(all(all(a >= b for a, b in zip(cut, cut[1:])) for cut in cuts))
            self.assertTrue(covers(cuts, triples(6*j), triples(k)))
            self.assertEqual(row['first_staircases_checked'], comb(6*j+k+2, k+1))
            polynomial = census.principal_counts(j)
            cost = sum(16**(3-j)*comb(k, e)*sum(polynomial[:cut[e]+1])
                       for cut in cuts for e in range(k+1))
            self.assertEqual(cost, row['cost'])
            self.assertEqual(cost, row['prior_weighted_cost'])

    def test_general_small_cost_search_against_full_threshold_enumeration(self):
        for coefficients in ([2], [2, 3], [1, 4, 2]):
            maximum = len(coefficients)-1
            for central_counts in ([3], [1, 2], [1, 2, 1]):
                k = len(central_counts)-1
                principal, central = triples(maximum), triples(k)
                best = sum(coefficients)*sum(central_counts)
                for ascending in combinations_with_replacement(range(-1, maximum+1), k+1):
                    first = list(reversed(ascending))
                    for third in product(range(-1, maximum+1), repeat=k+1):
                        if covers([first, first, third], principal, central):
                            cost = sum(central_counts[e]*sum(coefficients[:cut[e]+1])
                                       for cut in (first, first, third) for e in range(k+1))
                            best = min(best, cost)
                self.assertEqual(census.optimize(coefficients, central_counts)['cost'], best)

    def test_unequal_third_leg_formula_against_literal_support(self):
        for maximum in range(3):
            for k in range(3):
                principal, central = triples(maximum), triples(k)
                firsts = [list(reversed(x)) for x in combinations_with_replacement(
                    range(-1, maximum+1), k+1)]
                for first, second in product(firsts, repeat=2):
                    third = [max([-1] + [maximum-2-first[a]-second[b]
                                         for a in range(k-c+1) for b in range(k-c-a+1)
                                         if first[a] < maximum and second[b] < maximum])
                             for c in range(k+1)]
                    self.assertTrue(covers([first, second, third], principal, central))
                    for c, value in enumerate(third):
                        if value >= 0:
                            lowered = third[:]
                            lowered[c] -= 1
                            self.assertFalse(covers([first, second, lowered], principal, central))

    def test_complete_unequal_report_and_all_retained_witnesses(self):
        report = json.loads((ROOT/'results/s5-staircase-covers-2026-10-23/three-leg-census.json').read_text())
        self.assertTrue(report['complete'])
        self.assertEqual([r['principal_factors'] for r in report['completed_rows']], list(range(4)))
        self.assertEqual(sum(r['unordered_pair_universe'] for r in report['completed_rows']), 77392758)
        self.assertEqual(sum(r['evaluated_pairs'] for r in report['completed_rows']), 5207743)
        for row, equal in zip(report['completed_rows'], self.report['rows'][:4]):
            j, k = row['principal_factors'], row['central_factors']
            self.assertEqual(row['staircases'], comb(6*j+k+2, k+1))
            n = row['staircases']
            self.assertEqual(row['unordered_pair_universe'], n*(n+1)//2)
            self.assertTrue(covers(row['cutoffs'], triples(6*j), triples(k)))
            self.assertEqual(row['cost'], equal['cost'])

    @unittest.skipUnless(shutil.which('g++'), 'optional C++ cross-check needs g++')
    def test_separate_cpp_complete_unequal_enumeration(self):
        with tempfile.TemporaryDirectory(prefix='s5-three-legs-') as temporary:
            binary = str(Path(temporary)/'three-legs')
            subprocess.run(['g++', '-O3', '-std=c++17', str(PACKAGE/'discovery/three_legs.cpp'),
                            '-o', binary], check=True, capture_output=True, timeout=120)
            output = subprocess.run([binary], check=True, capture_output=True,
                                    text=True, timeout=120).stdout
        self.assertEqual(output, (PACKAGE/'discovery/three_legs_cpp.log').read_text())
        report = json.loads((ROOT/'results/s5-staircase-covers-2026-10-23/three-leg-census.json').read_text())
        lines = output.splitlines()
        for i, row in enumerate(report['completed_rows']):
            fields = lines[4*i].split()
            self.assertEqual([int(fields[p]) for p in (1, 3, 5, 7)],
                             [row['principal_factors'], row['staircases'],
                              row['evaluated_pairs'], row['cost']])
            self.assertEqual([list(map(int, line.split())) for line in lines[4*i+1:4*i+4]],
                             row['cutoffs'])


if __name__ == '__main__':
    unittest.main()
