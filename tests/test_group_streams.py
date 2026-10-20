"""Independent checks for sparse certificates and exact mask backtracking."""
from itertools import combinations,product
import copy
import json
from pathlib import Path
import random
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
RESEARCH=ROOT/'research/ai/2026-10-20-group-potentials'
RESULTS=ROOT/'results/group-potentials-2026-10-20'
sys.path.insert(0,str(RESEARCH))
import group_exact
import octal_group as octal
import octal_normalization as normalization
from mask_packing import exact_pack
from stream_potentials import verify_stream_witness
from verify_stream_reports import verify_report
from octal_fixed_frontier import planes,options


class GroupStreamTests(unittest.TestCase):
    def test_exact_mask_backtracking_against_bruteforce(self):
        choices=[1,3,5,7,15,85]
        orbit=lambda mask:sorted({sum(1<<(v^h) for h in range(8) if mask&(1<<h)) for v in range(8)})
        for seeds in product(choices,repeat=3):
            rows=[orbit(s) for s in seeds]
            expected=any(not (a&b or a&c or b&c) for a,b,c in product(*rows))
            result=exact_pack(rows)
            self.assertEqual(result['satisfiable'],expected)
            if expected:self.assertTrue(all(not a&b for a,b in combinations(result['selected_masks'],2)))
        with self.assertRaises(ValueError):exact_pack([[1,2,4]])

    def test_octal_field_and_lazy_group_law(self):
        for a,b,c in product(range(8),repeat=3):
            self.assertEqual(octal.fm(a,octal.fm(b,c)),octal.fm(octal.fm(a,b),c))
            self.assertEqual(octal.fm(a,b^c),octal.fm(a,b)^octal.fm(a,c))
        G=octal.cubic_group();rng=random.Random(822)
        self.assertEqual(sum(d*d for d in G['irreducible_degrees']),3584)
        for a in range(1,8):self.assertEqual(octal.fm(a,octal.inverse(a)),1)
        for g in rng.sample(range(3584),120):
            self.assertEqual(G['mul'][g][G['inv'][g]],0)
            self.assertEqual(G['mul'][G['inv'][g]][g],0)
            h,k=rng.randrange(3584),rng.randrange(3584)
            self.assertEqual(G['mul'][G['mul'][g][h]][k],G['mul'][g][G['mul'][h][k]])

    def test_streaming_verifier_checks_all_control_terms(self):
        G=group_exact.group(5)
        report=json.loads((RESULTS/'sl2-5-control3-3-3.json').read_text())
        w=report['witness'];receipt=verify_stream_witness(G,w['sets'],w['potentials'])
        self.assertEqual(receipt['intended_terms'],27)
        self.assertEqual(receipt['extra_supported_terms'],1)
        self.assertEqual(receipt['minimum_extra_weight'],w['verification']['minimum_extra_weight'])
        with self.assertRaises(ValueError):verify_stream_witness(G,w['sets'],[0]*9)

    def test_cubic_parent_and_all_87_sparse_circuits(self):
        report=json.loads((RESULTS/'octal-cubic-deletions-lazy.json').read_text())
        result=verify_report(report)
        self.assertEqual(result['exact_cuts_replayed'],87)
        self.assertFalse(result['exact_witness_replayed'])
        broken=copy.deepcopy(report);broken['cuts'][0]['weights'][0]*=2
        with self.assertRaises(ValueError):verify_report(broken)

    def test_normalization_by_actual_group_operations(self):
        G=octal.group();rng=random.Random(416)
        base=json.loads((RESULTS/'octal-direction-triples.json').read_text())['surviving_direction_triples'][0]['base_columns']
        for _ in range(40):
            offsets=[{a:rng.randrange(64) for a in range(1,8)} for f in range(3)]
            normalized=normalization.normalize(base,offsets);target=normalization.point_sets(base,normalized['offsets'])
            original=normalization.point_sets(base,offsets);h=normalized['common_translation_conjugator']
            for f in range(3):
                right=normalized['right_translation_vectors'][f]
                mapped={G['mul'][G['mul'][h][G['mul'][g][right]]][G['inv'][h]] for g in original[f]}
                self.assertEqual(mapped,set(target[f]))
                self.assertEqual(normalized['offsets'][f][1],0)
            self.assertEqual(normalized['offsets'][0][2],0)

    def test_local_frontier_normalizations_and_saved_packings(self):
        all_planes=planes();self.assertEqual(len(all_planes),651)
        for r in [2,4,6,8]:
            A={0,1,r,1^r}
            self.assertEqual(sum(A.intersection(B)=={0} for B in all_planes),560)
        report=json.loads((RESULTS/'octal-fixed-frontier.json').read_text())
        self.assertEqual(report['complete_normalized_cases'],6720)
        self.assertEqual(len(report['survivors']),126)
        for entry in report['survivors']:
            r=entry['first_template_ratio'];v=entry['second_short_direction']
            w=min(x for x in entry['second_plane'][1:] if x!=v)
            rows=options([0,1,r],[0,v,w],1,v)
            selected=entry['local_packing']
            self.assertTrue(all(mask in row for mask,row in zip(selected,rows)))
            self.assertTrue(all(not a&b for a,b in combinations(selected,2)))


if __name__=='__main__':unittest.main()
