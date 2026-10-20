"""Finite regression tests for the second-pass checkpoint, not a proof audit."""
import gzip
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SESSION = ROOT / "research" / "ai" / "2026-10-20-session2"
RESULTS = ROOT / "results" / "session2-2026-10-20"


def load(name):
    spec = importlib.util.spec_from_file_location(name, SESSION / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


dimension = load("dimension_search")
tensor = load("tensor_checks")


class CheckpointTests(unittest.TestCase):
    def test_profile(self):
        self.assertEqual(dimension.profile(2, 2), Fraction(10, 3))
        self.assertEqual(dimension.profile(3, 3), Fraction(56, 9))
        self.assertEqual(dimension.profile(1, 11), 11)

    def test_small_candidate(self):
        self.assertEqual(dimension.solve(3, 3, 0)["ratio"], "57/56")

    def test_full_dimension_replay(self):
        expected = json.loads(gzip.decompress((RESULTS / "dimension_search.json.gz").read_bytes()))
        actual = dimension.run()
        self.assertEqual(actual, expected)
        self.assertEqual((actual["orientation_cases"], actual["candidate_cases"]), (189, 85))

    def test_tensor_replay(self):
        expected = json.loads((RESULTS / "tensor_checks.json").read_text())
        actual = json.loads(json.dumps(tensor.run()))
        # The package version is environment metadata, not a mathematical result.
        expected.pop("sympy_version")
        actual.pop("sympy_version")
        self.assertEqual(actual, expected)

    def test_rank_one_koszul_bound(self):
        M = tensor.koszul_matrix([4, 1, 1], [(0, 0, 0)], 2)
        self.assertEqual(M.rank(), 3)

    def test_shared_sector_koszul_direct_sum(self):
        dims, terms = tensor.convolution(2, 3, 0)
        target = [(x, y + 2 * h, z + 3 * h) for h in range(3) for x, y, z in terms]
        self.assertEqual(tensor.koszul_matrix([4, 6, 9], target, 2).rank(), 36)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            dimension.solve(0, 2, 0)
        with self.assertRaises(ValueError):
            tensor.convolution(2, 2, 3)

    def test_draft_status(self):
        data = json.loads((SESSION / "claims.json").read_text())
        self.assertFalse(data["new_exponent_established"])
        draft = next(x for x in data["claims"] if x["id"] == "DRAFT-STRONG-SEARCH-011")
        self.assertEqual(draft["completed_runs"], 0)


if __name__ == "__main__":
    unittest.main()
