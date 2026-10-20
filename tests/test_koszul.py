"""Compare the all-size formulas to independently assembled exact matrices."""
import importlib.util
from itertools import permutations
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


koszul = load("maintained_koszul", ROOT / "research/ai/2026-10-20-koszul/koszul.py")
tensor = load("archived_tensor_checks", ROOT / "research/ai/2026-10-20-session2/tensor_checks.py")


class KoszulTests(unittest.TestCase):
    def test_formulas_against_exact_coefficient_matrices(self):
        count = 0
        for a in range(1, 5):
            for b in range(a, 5):
                dims, terms = tensor.convolution(a, b)
                for perm in permutations(range(3)):
                    oriented = [dims[i] for i in perm]
                    support = [tuple(t[i] for i in perm) for t in terms]
                    for p in range(oriented[0]):
                        actual = tensor.koszul_matrix(oriented, support, p).rank()
                        self.assertEqual(actual, koszul.intrinsic_rank(*oriented, p),
                                         (a, b, perm, p))
                        count += 1
        self.assertEqual(count, 180)

    def test_padding_against_exact_coefficient_matrices(self):
        for a, b, output in [(2, 2, 0), (2, 3, 0), (2, 3, 2)]:
            dims, terms = tensor.convolution(a, b, output)
            for extra in (1, 2):
                ambient = dims[0] + extra
                for p in range(ambient):
                    actual = tensor.koszul_matrix([ambient, *dims[1:]], terms, p).rank()
                    self.assertEqual(actual, koszul.padded_rank(*dims, ambient, p))

    def test_archive_audit(self):
        report = koszul.audit_archive()
        self.assertEqual((report["candidate_cases"], report["excluded_cases"],
                          report["surviving_cases"]), (85, 85, 0))
        expected = json.loads((ROOT / "results/koszul-2026-10-20/candidate_audit.json").read_text())
        self.assertEqual(report, expected)
        for c in report["cases"]:
            self.assertTrue(c["obstructing_degrees"])
            for p in c["obstructing_degrees"]:
                self.assertGreater(c["target_ranks"][p], c["source_ranks"][p])

    def test_previous_best_border_rank_obstruction(self):
        rank = koszul.intrinsic_rank(10, 4, 7, 6)
        self.assertEqual(rank, 840)
        self.assertEqual(3 * rank // koszul.choose(9, 6), 30)
        self.assertGreater(30, 10 + 12 - 1)

    def test_invalid_dimensions(self):
        for dims in [(0, 2, 1), (3, 3, 3)]:
            with self.assertRaises(ValueError):
                koszul.intrinsic_rank(*dims, 1)
        with self.assertRaises(ValueError):
            koszul.padded_rank(3, 2, 2, 2, 1)


if __name__ == "__main__":
    unittest.main()
