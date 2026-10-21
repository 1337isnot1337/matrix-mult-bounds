"""Source derivation, finite coverage, positive control and damaged certificates."""
import importlib.util
import json
from pathlib import Path
import sys
import unittest
import tempfile

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT/'research/ai/2026-10-20-heisenberg-five'
sys.path.insert(0, str(RESEARCH))
spec = importlib.util.spec_from_file_location('heisenberg_exact_verify', RESEARCH/'verify.py')
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)
from group_exact import verify_witness
from coset_controls import all_controls
import normal_closure


class HeisenbergFiveTests(unittest.TestCase):
    def test_source_and_entire_two_coset_certificate(self):
        receipt = verify.replay(ROOT/'results/heisenberg-five-2026-10-20/two-coset.json')
        self.assertEqual(receipt['source']['characters'], 29)
        self.assertEqual(receipt['source']['exact_inner_products'], 841)
        self.assertEqual(receipt['normalization']['first_set_images'], 600)
        self.assertEqual(receipt['finite_triples_replayed'], 400)
        self.assertFalse(receipt['exponent_improvement'])

    def test_known_subgroup_positive_control(self):
        G = verify.group()
        index = {g: i for i, g in enumerate(G['matrices'])}
        sets = [[index[t, 0, 0] for t in range(5)],
                [index[0, t, 0] for t in range(5)],
                [index[t, t, 3*t*t % 5] for t in range(5)]]
        receipt = verify_witness(G, sets, [0]*15)
        self.assertEqual(receipt['intended_terms'], 125)
        self.assertEqual(receipt['extra_relations'], 0)

    def test_damaged_circuit_and_group_product_are_rejected(self):
        first = json.loads((ROOT/'results/heisenberg-five-2026-10-20/'
                            'two-coset.cuts.jsonl').read_text().splitlines()[0])
        first['weights'][0] = -1
        with self.assertRaises(ValueError):
            verify.verify_cut(verify.group(), first)
        G = verify.group()
        G['mul'][1][1] = 0
        with self.assertRaisesRegex(ValueError, 'representation law'):
            verify.source_characters(G)

    def test_subgroup_averaging_and_projection_controls(self):
        report = all_controls()
        self.assertEqual([r['pairwise_distinct_direction_triples_checked']
                          for r in report['subgroups']], [648, 15000, 115248])
        self.assertEqual(report['projected_supports']['affine_coordinate_classes'], 7)
        self.assertEqual(report['averaging']['right_stabilizer_orders'], [5]*3)

    def test_exact_normal_count_closure_and_damaged_report(self):
        path = ROOT/'results/heisenberg-five-2026-10-20/normal-closure.json'
        receipt = normal_closure.replay(path)
        self.assertEqual(receipt['balanced_pairs_checked'], 3003)
        self.assertEqual(receipt['unequal_triples_checked'], 410333)
        report = json.loads(path.read_text())
        report['line_pair_counts'][0] += 1
        with tempfile.TemporaryDirectory() as directory:
            bad = Path(directory)/'damaged.json'
            bad.write_text(json.dumps(report))
            with self.assertRaises(ValueError):
                normal_closure.replay(bad)

    def test_larger_progression_circuits(self):
        receipt = verify.replay_progressions(ROOT/'results/heisenberg-five-2026-10-20/'
                                             'progressions-p11-k3.json')
        self.assertEqual(receipt['short_circuits_checked'], 38)
        self.assertFalse(receipt['complete_source_exclusion'])


if __name__ == '__main__':
    unittest.main()
