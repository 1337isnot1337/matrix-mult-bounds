"""Explicit matrices and independent coverage for the normal-coset bound."""
from collections import Counter
from itertools import combinations_with_replacement,product
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-20-normal-coset-koszul'
RESULTS = ROOT/'results/normal-coset-koszul-2026-10-20'
sys.path.insert(0,str(PACKAGE))
import certificate as coset_certificate
import count_frontier
import rectangular_certificate


class NormalCosetKoszulTests(unittest.TestCase):
    def test_explicit_matrices_and_complete_seven_fiber_receipt(self):
        expected = json.loads((RESULTS/'certificate.json').read_text())
        self.assertEqual(coset_certificate.report(),expected)
        for item in expected['applications'].values():
            self.assertTrue(item['excluded'])
            rank = coset_certificate.rank_mod(coset_certificate.three_slice_matrix(item['blocks']),103)
            self.assertEqual(rank,item['proved_characteristic_zero_rank'])
        self.assertEqual(expected['all_F8_seven_fiber_size_patterns']['minimum_Koszul_rank'],129)
        self.assertFalse(coset_certificate.block_certificate([2],8)['excluded'])

    def test_scalar_blocks_and_rank_one_special_case(self):
        for blocks in [[1],[1,1],[2],[3],[1,2,3]]:
            matrix = coset_certificate.three_slice_matrix(blocks)
            expected = 3*sum(k*k for k in blocks)-blocks.count(1)
            self.assertEqual(coset_certificate.rank_mod(matrix),expected)
        with self.assertRaises(ValueError):
            coset_certificate.rank_mod([[1]],100)

    def test_every_small_rectangular_slice_and_direct_sum(self):
        for a,b,c in product(range(1,5),repeat=3):
            matrix = coset_certificate.rectangular_three_slice_matrix([(a,b,c)])
            expected = c*(3*min(a,b)-int(a==b==1))
            self.assertEqual(coset_certificate.rank_mod(matrix),expected)
        blocks = [(4,2,3),(2,4,1),(1,2,4),(2,1,4),(1,1,3)]
        expected = sum(c*(3*min(a,b)-int(a==b==1)) for a,b,c in blocks)
        self.assertEqual(coset_certificate.rank_mod(
            coset_certificate.rectangular_three_slice_matrix(blocks)),expected)

    def test_complete_rectangular_count_cover_and_invalid_byte(self):
        data = (RESULTS/'rectangular-cover.bin').read_bytes()
        expected = json.loads((RESULTS/'rectangular-cover.json').read_text())
        self.assertEqual(rectangular_certificate.replay(data),expected)
        self.assertEqual(expected['bounded_compositions_covered'],3535)
        self.assertEqual(expected['explicit_triangles_checked'],466859)
        self.assertGreater(expected['minimum_explicit_rank'],128)
        with self.assertRaises(ValueError):
            rectangular_certificate.replay(bytes([147])+data[1:])
        with self.assertRaises(ValueError):
            rectangular_certificate.verify_pattern_coverage(rectangular_certificate.patterns()[:-1])

    def test_three_point_difference_space_and_sharp_four_point_example(self):
        A,B,C = {0,1,2},{0,4,8},{0,16,32,48}
        difference = lambda row:{x^y for x,y in product(row,repeat=2)}
        AB = {a^b for a,b in product(A,B)}
        self.assertEqual(difference(AB),set(range(16)))
        self.assertEqual(len({a^b^c for a,b,c in product(A,B,C)}),36)
        self.assertLess(len({a^b^c for a,b,c in product(A,B,C|{1})}),45)

    def test_complete_count_frontier_with_independent_coordinate_loop(self):
        expected = json.loads((RESULTS/'count-frontier.json').read_text())
        self.assertEqual(count_frontier.run(),expected)
        patterns = [tuple(row) for row in expected['cyclic_pattern_classes']]
        histogram = Counter()
        survivors = []
        for triple in combinations_with_replacement(range(len(patterns)),3):
            a,b,c = [patterns[i] for i in triple]
            best = max(3*sum(min(x,y,z)**2 for x,y,z in
                             zip(a,count_frontier.rotate(b,j),count_frontier.rotate(c,k)))
                       for j,k in product(range(7),repeat=2))
            histogram[str(best)] += 1
            if best <= 128:
                survivors.append({'indices':list(triple),'maximum_Koszul_rank':best})
        self.assertEqual(dict(histogram),expected['maximum_rank_histogram'])
        self.assertEqual(survivors,expected['unexcluded_pattern_triples'])
        self.assertEqual(len(survivors),1566)


if __name__ == '__main__':
    unittest.main()
