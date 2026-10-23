from fractions import Fraction
import importlib.util
from itertools import permutations, product
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "research/ai/2026-10-23-monomial-recognition/verify.py"
SPEC = importlib.util.spec_from_file_location("monomial_recognition", SCRIPT)
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def brute_coordinate_recognition(terms):
    axes = [sorted({t[k] for t in terms}) for k in range(3)]
    for output in range(3):
        inputs = [k for k in range(3) if k != output]
        r, s = (len(axes[k]) for k in inputs)
        if len(axes[output]) != r+s-1 or len(terms) != r*s:
            continue
        for orders in product(*(list(permutations(axis)) for axis in axes)):
            maps = [{v: i for i, v in enumerate(axis)} for axis in orders]
            actual = {tuple(maps[k][t[k]] for k in range(3)) for t in terms}
            wanted = set()
            for i, j in product(range(r), range(s)):
                entry = [0, 0, 0]
                entry[inputs[0]], entry[inputs[1]], entry[output] = i, j, i+j
                wanted.add(tuple(entry))
            if actual == wanted:
                return True
    return False


class MonomialRecognitionTests(unittest.TestCase):
    def test_all_small_supports_against_arbitrary_permutations(self):
        full = [(i, j, i+j) for i in range(2) for j in range(3)]
        for mask in range(1, 1 << len(full)):
            terms = [t for k, t in enumerate(full) if mask & (1 << k)]
            with self.subTest(mask=mask):
                self.assertEqual(VERIFY.recognize(terms) is not None,
                                 brute_coordinate_recognition(terms))

    def test_every_three_by_three_support_matches_archived_recognizer(self):
        full = [(i, j, i+j) for i in range(3) for j in range(3)]
        for mask in range(1, 1 << len(full)):
            terms = [t for k, t in enumerate(full) if mask & (1 << k)]
            self.assertEqual(VERIFY.recognize(terms) is not None,
                             VERIFY.ARCHIVE.recognize(terms)["kind"] == "convolution")

    def test_gapped_labels_and_each_output_axis(self):
        base = [(i, j, i+j) for i in range(2) for j in range(3)]
        for output in range(3):
            for scale in (1, 7):
                terms = []
                for i, j, k in base:
                    if output == 2:
                        t = (i, j, k)
                    elif output == 0:
                        t = (k, -i, j)
                    else:
                        t = (-i, k, j)
                    terms.append((scale*t[0]-13, scale*t[1]+4, scale*t[2]-9))
                block = VERIFY.recognize(terms)
                self.assertIsNotNone(block)
                self.assertEqual(block["output_axis"], output)

    def test_support_hypotheses_and_missing_entry(self):
        for terms in ([], [(0, 0, 0)]*2, [(0, 0, 1)]):
            with self.assertRaises(ValueError):
                VERIFY.recognize(terms)
        punctured = [(i, j, i+j) for i in range(3) for j in range(3) if (i, j) != (1, 1)]
        self.assertIsNone(VERIFY.recognize(punctured))

    def test_ordered_census_and_exact_asymmetry(self):
        report = VERIFY.run(2, 5)
        self.assertEqual(report["cases_tested"], 51)
        self.assertEqual(report["orientation_counts"], {"a<b": 21, "a=b": 9, "a>b": 21})
        self.assertEqual(report["unequal_dimension_pairs_with_different_scores"], 12)
        self.assertEqual(report["exact_violation_count"], 0)
        forward, reverse = report["first_asymmetric_pair"]
        self.assertEqual(forward["ratio_exact"], "13/14")
        self.assertEqual(reverse["ratio_exact"], "9/14")
        for record in (report["best"], report["best_nontrivial"], forward, reverse):
            VERIFY.replay_record(record)
        forward["target_exact"] = "0"
        with self.assertRaisesRegex(ValueError, "does not replay"):
            VERIFY.replay_record(forward)

    def test_scores_match_exact_archived_values(self):
        h = VERIFY.ARCHIVE.slopes(8)
        for a, b in ((2, 3), (3, 2), (3, 3)):
            for wx, wy in product(product(range(2), repeat=a), product(range(2), repeat=b)):
                actual = VERIFY.score(wx, wy, h)
                archived = VERIFY.ARCHIVE.inspect(wx, wy, None, h)
                self.assertEqual(actual["source_exact"], archived["source_exact"])
                self.assertEqual(actual["target_exact"], archived["target_exact"])
                self.assertEqual(Fraction(actual["ratio_exact"]),
                                 Fraction(archived["target_exact"])/Fraction(archived["source_exact"]))


if __name__ == "__main__":
    unittest.main()
