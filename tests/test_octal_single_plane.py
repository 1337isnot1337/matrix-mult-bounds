"""Replay the completed fixed-base local filter without any SAT dependency."""
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'research/ai/2026-10-20-group-potentials'))
from octal_single_plane_frontier import run, graph_planes
from verify_stream_reports import verify_report
from affine_fiber_certificate import check
from group_koszul_pilot import run as koszul_run


class OctalSinglePlaneTests(unittest.TestCase):
    def test_complete_local_filter_replay(self):
        expected = json.loads((ROOT/'results/group-potentials-2026-10-20/octal-single-plane-local-frontier0.json').read_text())
        actual = run(expected['base_columns'])
        for item in (actual, expected):
            item.pop('elapsed_seconds')
        self.assertEqual(actual, expected)
        self.assertEqual(actual['planes_checked'],3060)
        self.assertEqual(actual['surviving_planes'],0)
        for family in range(3):
            planes = list(graph_planes(actual['base_columns'],family))
            self.assertEqual(len({tuple(row) for row in planes}),255)

    def test_both_native_control_circuits(self):
        for name in ['S2','T3']:
            path = ROOT/f'results/group-potentials-2026-10-20/octal-single-plane-{name}.json'
            data = json.loads(path.read_text())
            self.assertEqual(verify_report(data)['exact_cuts_replayed'],1)
            receipt = check(data['base_columns'],data['cuts'][0]['sets'])
            self.assertEqual(receipt['varying_three_point_planes'],0)
            self.assertEqual(receipt['changed_short_directions'],0)

    def test_exact_group_koszul_pilot_replay(self):
        expected = json.loads((ROOT/'results/group-potentials-2026-10-20/group-koszul-pilot.json').read_text())
        self.assertEqual(koszul_run(),expected)
        self.assertEqual([len(r['excluded_at_powers']) for r in expected],[0,0])


if __name__ == '__main__':
    unittest.main()
