"""Complete unequal-target replays and empty-fiber regression coverage."""
from itertools import product
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-20-c29-near-capacity'
RESULTS = ROOT/'results/c29-near-capacity-2026-10-20'
sys.path.insert(0,str(PACKAGE))
import cyclic_packing
import fiber_frontier
import rectangular_gluing
import source_frontier


class C29RectangularTests(unittest.TestCase):
    def test_empty_masks_preserve_complete_packing(self):
        domains = [cyclic_packing.options(row,5) for row in [[],[0,1],[0,2]]]
        brute = any(not(a&b or a&c or b&c) for a,b,c in product(*domains))
        self.assertEqual(cyclic_packing.pack(domains,5)['satisfiable'],brute)
        self.assertTrue(cyclic_packing.pack([[0],[0]],5)['satisfiable'])

    def test_two_list_join_against_three_list_enumeration(self):
        choices = [[(0,0,0)],[(1,2,3),(4,5,6)],[(28,27,26),(25,24,23)],
                   [(0,0,0),(7,8,9),(22,21,20)]]
        for lists in product(choices,repeat=3):
            brute = sum(all(sum(column)%29==0 for column in zip(*rows))
                        for rows in product(*lists))
            self.assertEqual(rectangular_gluing.coherent_triples(lists)[0],brute)

    def test_complete_source_frontier(self):
        expected = json.loads((RESULTS/'source-frontier.json').read_text())
        self.assertEqual(source_frontier.run(),expected)
        self.assertEqual(expected['sorted_shapes_with_minimum_two_checked'],512)
        self.assertEqual(expected['surviving_shapes'],[[9,9,11],[9,10,10],[10,10,10]])

    def test_both_complete_rectangular_frontiers_and_gluing(self):
        for shape,count in [((9,10,10),392),((9,9,11),48)]:
            suffix = '-'.join(map(str,shape))
            source = RESULTS/f'fiber-frontier-{suffix}.json'
            expected = json.loads(source.read_text())
            actual = json.loads(json.dumps(fiber_frontier.run(shape=shape)))
            self.assertEqual(actual,expected)
            self.assertEqual(actual['local_survivors'],count)
            expected_gluing = json.loads((RESULTS/f'identity-gluing-{suffix}.json').read_text())
            actual_gluing = json.loads(json.dumps(rectangular_gluing.run(source)))
            self.assertEqual(actual_gluing,expected_gluing)
            self.assertEqual(actual_gluing['coherent_configurations'],0)


if __name__ == '__main__':
    unittest.main()
