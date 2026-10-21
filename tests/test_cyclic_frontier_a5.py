import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "cyclic_frontier_a5", ROOT / "research/ai/2026-10-20-cyclic-equivariant/frontier_a5.py")
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class CyclicFrontierA5Tests(unittest.TestCase):
    def test_complete_exact_frontier(self):
        path = ROOT / "results/cyclic-equivariant-2026-10-20/a5-character-frontier.json"
        self.assertEqual(json.loads(json.dumps(v.report())), json.loads(path.read_text()))

    def test_dual_certificate_and_remaining_candidate(self):
        dual = v.full_leg_dual()
        self.assertEqual(dual["sum_of_rows"], [3]*7)
        self.assertEqual(dual["sum_of_right_sides"], 33)
        candidate = v.candidate_family(5)
        self.assertEqual(candidate["shape"], [14, 14, 15])
        self.assertFalse(candidate["ordinary_extreme_slice_test_excludes"])
        self.assertTrue(candidate["passes_finite_exponent_threshold"])


if __name__ == "__main__":
    unittest.main()
