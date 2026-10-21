"""Independent finite coverage and offset consistency for the C29 route."""
from itertools import combinations, product
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-20-c29-near-capacity'
RESULTS = ROOT/'results/c29-near-capacity-2026-10-20'
sys.path.insert(0,str(PACKAGE))
import cyclic_packing as cyclic
import normal_triples
import fiber_frontier
import identity_gluing
import offset_gluing


class C29NearCapacityTests(unittest.TestCase):
    def test_normal_classification_by_both_enumerations(self):
        expected = json.loads((RESULTS/'normal-triples.json').read_text())
        self.assertEqual(normal_triples.report(),expected)
        self.assertEqual(expected['independent']['class_triples_covered'],2000376)
        self.assertEqual(expected['independent']['positive_translation_class_triples'],84)

    def test_cyclic_packing_against_small_bruteforce(self):
        for order in range(3,8):
            seeds = [[0],[0,1],[0,2],list(range(min(3,order))) ]
            for rows in product(seeds,repeat=3):
                domains = [cyclic.options(row,order) for row in rows]
                brute = any(not(a & b or a & c or b & c)
                            for a,b,c in product(*domains))
                result = cyclic.pack(domains,order)
                self.assertEqual(result['satisfiable'],brute)
                if brute:
                    self.assertTrue(all(not a & b for a,b in combinations(result['selected_masks'],2)))
        with self.assertRaises(ValueError):
            cyclic.pack([[1]],5)

    def test_full_direction_frontier_replay(self):
        expected = json.loads((RESULTS/'fiber-frontier.json').read_text())
        actual = json.loads(json.dumps(fiber_frontier.run()))
        self.assertEqual(actual,expected)
        self.assertEqual(actual['bases_covered'],6)
        self.assertEqual(actual['local_survivors'],12)

    def test_identity_lists_by_independent_complete_placement_loop(self):
        source = RESULTS/'fiber-frontier.json'
        expected = json.loads((RESULTS/'identity-gluing.json').read_text())
        actual = json.loads(json.dumps(identity_gluing.run(source)))
        self.assertEqual(actual,expected)
        for record in actual['records']:
            cells = record['cells']
            for pair_index,(f,g) in enumerate([(0,1),(1,2),(2,0)]):
                masks = []
                cardinality = 0
                for i,a in enumerate(fiber_frontier.SCALARS):
                    values = {(pow(a,-1,29)*(y-x)) % 29
                              for x,y in product(fiber_frontier.points(cells[f][i]),
                                                 fiber_frontier.points(cells[g][i]))}
                    cardinality += len(values)
                    masks.append([sum(1 << ((v+t) % 29) for v in values) for t in range(29)])
                brute = []
                for x,y,z in product(range(29),repeat=3):
                    union = masks[0][0] | masks[1][x] | masks[2][y] | masks[3][z]
                    if union.bit_count() == cardinality:
                        brute.append([x,y,z])
                self.assertEqual(brute,record['identity_pair_packing_lists'][pair_index])
            self.assertEqual(record['coherent_triples'],0)

    def test_full_affine_gluing_independent_of_telescoping_test(self):
        expected = json.loads((RESULTS/'offset-gluing.json').read_text())
        actual = json.loads(json.dumps(offset_gluing.run(RESULTS/'fiber-frontier.json')))
        self.assertEqual(actual,expected)
        self.assertEqual(actual['compatible_affine_systems'],0)
        coefficients = [[1,2,0,0,0,0,0,0],[0,1,0,0,0,0,0,0]]
        basis = offset_gluing.extend((),coefficients,[7,3])
        self.assertIsNotNone(basis)
        self.assertIsNone(offset_gluing.extend(basis,[[1,0,0,0,0,0,0,0]],[2]))


if __name__ == '__main__':
    unittest.main()
