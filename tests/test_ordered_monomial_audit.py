"""Independent certificate replay and orientation-complete search controls."""
from copy import deepcopy
import hashlib
import importlib.util
from itertools import permutations, product
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-ordered-monomial-audit"
RESULTS = ROOT / "results/ordered-monomial-audit-2026-10-23"
SPEC = importlib.util.spec_from_file_location("ordered_monomial_audit", PACKAGE / "check.py")
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


def recognizes_by_arbitrary_bijections(terms):
    axes = [sorted({t[k] for t in terms}) for k in range(3)]
    for out in range(3):
        first, second = [k for k in range(3) if k != out]
        a, b = len(axes[first]), len(axes[second])
        if len(axes[out]) != a + b - 1 or len(terms) != a * b:
            continue
        lookup = {(t[first], t[second]): t[out] for t in terms}
        if len(lookup) != a * b:
            continue
        for xs in permutations(axes[first]):
            for ys in permutations(axes[second]):
                labels = [set() for _ in range(a + b - 1)]
                for i, x in enumerate(xs):
                    for j, y in enumerate(ys):
                        labels[i + j].add(lookup[x, y])
                if all(len(values) == 1 for values in labels) and len(
                        set().union(*labels)) == a + b - 1:
                    return True
    return False


class OrderedMonomialAuditTests(unittest.TestCase):
    def test_recognition_against_all_bijections_on_511_supports(self):
        source = [(i, j, i + j) for i, j in product(range(3), repeat=2)]
        for mask in range(1, 1 << len(source)):
            terms = [term for k, term in enumerate(source) if mask & (1 << k)]
            self.assertEqual(CHECK.block(terms)["kind"] == "convolution",
                             recognizes_by_arbitrary_bijections(terms), terms)

    def test_nonuniform_singleton_labels(self):
        terms = [(7, j, 7 + j) for j in (0, 1, 5, 20)]
        self.assertEqual(CHECK.block(terms)["kind"], "convolution")

    def test_input_exchange_changes_scoring(self):
        self.assertEqual(CHECK.inspect((0, 0), (0, 1, 1, 0))["ratio_exact"], "1")
        self.assertEqual(CHECK.inspect((0, 1, 1, 0), (0, 0))["ratio_exact"], "1/2")

    def test_complete_ordered_small_scope(self):
        report = CHECK.census(2, 5)
        self.assertEqual(report["cases"], 51)
        self.assertEqual(report["historical_a_le_b_cases"], 30)
        self.assertEqual(report["additional_a_gt_b_cases"], 21)
        self.assertEqual(report["violations"], 0)
        self.assertEqual([(s["a"], s["b"]) for s in report["dimensions"]],
                         [(2, 2), (2, 3), (3, 2)])

    def test_corrupted_certificate_fields_rejected(self):
        original = CHECK.expected_record((0, 0), (0, 1, 1, 0))
        mutations = [
            lambda r: r["support_certificate"]["zero_terms"].pop(),
            lambda r: r["support_certificate"]["sectors"].reverse(),
            lambda r: r["blocks"][0].update(a=99),
            lambda r: r["score"].update(target_exact="999"),
            lambda r: r["support_certificate"]["weights"]["z"].__setitem__(0, 1),
        ]
        for mutation in mutations:
            record = deepcopy(original)
            mutation(record)
            with self.assertRaises(ValueError):
                CHECK.verify_record(record)

    def test_weights_must_be_integers(self):
        for value in (0.0, False, "0"):
            with self.assertRaisesRegex(ValueError, "integer"):
                CHECK.inspect((value, 0), (0, 1))

    def test_every_reviewed_record_digest(self):
        report = json.loads((RESULTS / "reviewed-records.json").read_text())
        self.assertEqual(sum(len(r["records"]) for r in report["reports"]), 60)
        for source in report["reports"]:
            for record in source["records"]:
                actual = CHECK.expected_record(record["x"], record["y"])
                encoded = json.dumps(actual, sort_keys=True, separators=(",", ":")).encode()
                self.assertEqual(hashlib.sha256(encoded).hexdigest(), record["sha256"])

    def test_saved_dimension_coverage_and_witnesses(self):
        for name in ("binary", "ternary"):
            report = json.loads((RESULTS / (name + ".json")).read_text())
            q, n = report["alphabet_size"], report["max_sum"]
            expected = {(a, b): (q**a - (q - 1)**a) * (q**b - (q - 1)**b)
                        for a in range(2, n - 1) for b in range(2, n - a + 1)}
            self.assertEqual({(r["a"], r["b"]): r["cases"] for r in report["dimensions"]}, expected)
            self.assertEqual(report["cases"], sum(expected.values()))
            for row in report["dimensions"]:
                for key in ("best", "best_nontrivial"):
                    record = row[key]
                    if record is not None:
                        self.assertEqual(CHECK.inspect(record["weights"]["x"],
                                                       record["weights"]["y"]), record)


if __name__ == "__main__":
    unittest.main()
