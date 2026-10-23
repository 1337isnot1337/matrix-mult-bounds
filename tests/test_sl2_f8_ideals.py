"""Independent integer projection checks for imported subgroup-ideal cuts."""
import copy
import hashlib
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-21-sl2-f8-ideals'
RESULTS = ROOT/'results/sl2-f8-ideals-2026-10-21'
sys.path.insert(0,str(PACKAGE))
import sl2_f8_ideal_certificate as ideals


class SL2F8IdealTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.expected = json.loads((RESULTS/'projections.json').read_text())

    def test_exact_projection_replay_and_reproduction(self):
        self.assertEqual(ideals.verify_report(self.expected)['subgroup_projections_verified'],3)
        self.assertEqual(ideals.report(),self.expected)
        self.assertEqual([r['verification']['ideal_dimension_upper_bound'] for r in self.expected['records']],[308,440,244])

    def test_invalid_rank_projection_and_subgroup(self):
        row = self.expected['records'][0]
        with self.assertRaises(ValueError):
            ideals.verify_projection(row['subgroup'],row['central_projection'],307)
        bad = list(row['central_projection'])
        bad[1] = str(int(1))
        with self.assertRaises(ValueError):
            ideals.verify_projection(row['subgroup'],bad,308)
        with self.assertRaises(ValueError):
            ideals.verify_projection(row['subgroup'][:-1],row['central_projection'],308)
        bad = copy.deepcopy(self.expected)
        bad['records'][1]['complete_coset_forbidden_on_legs'][2] = True
        with self.assertRaises(ValueError):
            ideals.verify_report(bad)

    def test_zero_idempotent_cannot_contain_the_subgroup_and_identity_is_safe(self):
        H = self.expected['records'][0]['subgroup']
        with self.assertRaises(ValueError):
            ideals.verify_projection(H,['0']*9,0)
        identity = ['1']+['0']*8
        receipt = ideals.verify_projection(H,identity,504)
        self.assertEqual(receipt['ideal_dimension_upper_bound'],504)
        self.assertFalse(any(v>receipt['ideal_dimension_upper_bound'] for v in [450,450,324]))

    def test_all_remaining_formats_and_selected_nine_cycle_boundary(self):
        data = json.loads((ROOT/'results/semisimple-koszul-2026-10-21/frontiers.json').read_text())
        formats = data['sources'][1]['koszul_surviving_shapes']
        for a,b,c in formats:
            self.assertGreater(min(a*b,b*c,c*a),308)
            self.assertGreater(min(a*b,b*c,c*a),244)
        self.assertEqual(self.expected['records'][1]['complete_coset_forbidden_on_legs'],[True,True,False])

    def test_concurrent_lemma_import_is_pinned_and_attributed(self):
        manifest = json.loads((PACKAGE/'import.json').read_text())
        blob = (PACKAGE/manifest['local_path']).read_bytes()
        self.assertEqual(hashlib.sha256(blob).hexdigest(),manifest['sha256'])
        self.assertEqual(manifest['commit'],'b6f01fb781d64589e8681f5bfbff8750291daaf6')
        self.assertIn('unreviewed',manifest['role'])


if __name__=='__main__':
    unittest.main()
