"""Complete unequal F8 count cover; exact replay rejects corrupt witnesses."""
import copy
from itertools import product
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-21-f8-coordinate-closure'
RESULTS = ROOT/'results/f8-coordinate-closure-2026-10-21'
sys.path.insert(0,str(PACKAGE))
import closure_certificate
import discover_pencils


class F8CoordinateClosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = json.loads((ROOT/'results/f8-unequal-2026-10-20/koszul-pencils.json').read_text())
        cls.even = json.loads((RESULTS/'even-pencils.json').read_text())
        cls.packed = (RESULTS/'count-cover.zlib').read_bytes()
        cls.raw = closure_certificate.unpack(cls.packed)
        cls.receipt = closure_certificate.replay(cls.raw,cls.base,cls.even)

    def test_complete_all_size_frontier_and_cover_receipt(self):
        self.assertEqual(self.receipt,json.loads((RESULTS/'count-cover.json').read_text()))
        self.assertEqual(self.receipt['minimal_formats_covered'],12)
        self.assertEqual(self.receipt['pair_tags_checked'],9539875)
        self.assertEqual(self.receipt['explicit_triangles_checked'],90)
        self.assertFalse(self.receipt['improves_omega'])

    def test_even_pencils_reproduce_and_corruption_is_rejected(self):
        self.assertEqual(discover_pencils.discover(),self.even)
        bad = copy.deepcopy(self.even)
        bad['records'][0]['integer_slices'][0][0][0] = 0.5
        with self.assertRaises(ValueError):
            closure_certificate.tables(self.base,bad)
        bad = copy.deepcopy(self.even)
        bad['records'][0]['rank_lower_bound'] += 1
        with self.assertRaises(ValueError):
            closure_certificate.tables(self.base,bad)

    def test_invalid_pair_and_triangle_tags(self):
        with self.assertRaises(ValueError):
            closure_certificate.replay(bytes([255])+self.raw[1:],self.base,self.even)
        first = next(row for row in self.receipt['formats'] if row['explicit_triangles_checked'])
        offset = first['explicit_tag_offset']
        bad = self.raw[:offset]+bytes([255,255])+self.raw[offset+2:]
        with self.assertRaises(ValueError):
            closure_certificate.replay(bad,self.base,self.even)

    def test_compressed_truncation_and_trailing_bytes(self):
        for bad in [self.packed[:-1],self.packed+b'x']:
            with self.assertRaises(ValueError):
                closure_certificate.unpack(bad)

    def test_six_slice_pencil_excludes_former_count_survivor(self):
        row = next(r for r in self.even['records'] if (r['a'],r['b'],r['slice_dimension'])==(3,4,6))
        matrix = closure_certificate.koszul_matrix(row['integer_slices'],2)
        self.assertEqual([len(matrix),len(matrix[0])],[60,60])
        self.assertEqual(closure_certificate.rank_mod(matrix,103),60)
        self.assertEqual(row['rank_one_contribution'],10)
        table = closure_certificate.tables(self.base,self.even)[3][3]
        S,T,U = (0,0,0,4,4,4,4),(0,4,4,0,4,4,4),(3,)*7
        rank = max(sum(z*table[x][y] for x,y,z in zip(U,closure_certificate.rotate(S,j),closure_certificate.rotate(T,k)))
                   for j,k in product(range(7),repeat=2))
        self.assertEqual(rank,720)
        self.assertGreater(rank,64*10)


if __name__=='__main__':
    unittest.main()
