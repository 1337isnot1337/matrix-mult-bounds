"""Torus incidence, exact positive packets and complete doubled-coset cover."""
import copy
from itertools import combinations
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-21-sl2-f8-ideals'
RESULTS = ROOT/'results/sl2-f8-ideals-2026-10-21'
sys.path.insert(0,str(PACKAGE))
import torus_packets
from group_exact import pair_map
from stream_potentials import verify_stream_witness,support,weight
from verify_stream_reports import verify_cut


class SL2F8TorusPacketTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.expected = json.loads((RESULTS/'torus-packets.json').read_text())

    def test_complete_torus_geometry_and_doubled_right_cosets(self):
        self.assertEqual(torus_packets.geometry_report(),self.expected)
        self.assertEqual(len(self.expected['TPP_torus_triples']),252)
        self.assertEqual(self.expected['non_TPP_extra_relation_count'],3024)
        self.assertEqual(self.expected['doubled_right_coset_pairs_checked'],972)
        self.assertEqual(self.expected['minimum_doubled_right_coset_difference_intersection'],11)

    def test_unique_blocks_force_direction_rigidity(self):
        blocks = self.expected['involution_blocks']
        edge = {tuple(t) for t in self.expected['TPP_torus_triples']}
        containing = {}
        for B in blocks:
            for pair in combinations(B,2):
                self.assertNotIn(pair,containing)
                containing[pair] = set(B)
        self.assertEqual(len(containing),378)
        # For every fixed direction and every other two, all TPP completions
        # are the two remaining points of their one four-point block.
        for a,b in combinations(range(28),2):
            completions = {c for c in range(28) if tuple(sorted((a,b,c))) in edge}
            self.assertEqual(completions,containing[a,b]-{a,b})

    def test_punctured_packet_is_a_strict_integer_degeneration(self):
        packet = self.expected['punctured_packet']
        self.assertEqual(verify_stream_witness(torus_packets.group(),packet['sets'],packet['potentials']),packet['verification'])
        self.assertEqual(packet['verification']['shape'],[8,9,9])
        self.assertEqual(packet['verification']['intended_terms'],648)
        self.assertEqual(packet['verification']['extra_supported_terms'],567)
        self.assertEqual(packet['verification']['minimum_extra_weight'],1)
        extra = {weight(v,packet['potentials'],[8,9,9])
                 for v in support(torus_packets.group(),packet['sets'])
                 if (v[0],v[1],v[3])!=(v[5],v[2],v[4])}
        self.assertEqual(extra,{1})
        with self.assertRaises(ValueError):
            verify_stream_witness(torus_packets.group(),packet['sets'],[0]*26)

    def test_order_three_translation_needs_three_punctures(self):
        for indices in combinations(range(28),3):
            rel = torus_packets.packet_relation(indices)
            if rel and any(len(torus_packets.powers(g))==3 for g in rel):
                selected = next(i for i,g in enumerate(rel) if len(torus_packets.powers(g))==3)
                packet = torus_packets.punctured_packet(indices,selected)
                break
        self.assertEqual(packet['verification']['shape'][selected],6)
        self.assertEqual(packet['verification']['intended_terms'],486)
        self.assertEqual(packet['verification']['minimum_extra_weight'],1)

    def test_full_parent_cycle_and_corrupt_weight(self):
        cut = self.expected['full_parent_positive_cycle']
        self.assertTrue(verify_cut(torus_packets.group(),cut,[9,9,9]))
        bad = copy.deepcopy(cut)
        bad['weights'][0] += 1
        with self.assertRaises(ValueError):
            verify_cut(torus_packets.group(),bad,[9,9,9])

    def test_separate_ordinary_controls_are_not_an_assembly(self):
        for name,shape,terms in [('full_TPP_control',[9,9,9],729),('seven_packet_control',[7,7,7],343)]:
            data = self.expected[name]
            receipt = verify_stream_witness(torus_packets.group(),data['sets'],data['potentials'])
            self.assertEqual(receipt,data['verification'])
            self.assertEqual(receipt['shape'],shape)
            self.assertEqual(receipt['intended_terms'],terms)
            self.assertEqual(receipt['extra_supported_terms'],0)
        self.assertFalse(self.expected['improves_omega'])


if __name__=='__main__':
    unittest.main()
