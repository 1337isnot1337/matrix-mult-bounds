"""Independent exact Laurent replay and malformed-certificate controls."""
import copy
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-conic-third-jets"
RESULTS = ROOT / "results/conic-third-jets-2026-10-23"
spec = importlib.util.spec_from_file_location("conic_laurent_replay", PACKAGE / "verify_laurent.py")
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class LaurentConicThirdJetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.witness = json.loads((RESULTS / "mixed-family.json").read_text())
        cls.predecessor = v.read_predecessor()
        cls.report = json.loads((RESULTS / "mixed-family-verification.json").read_text())

    def test_universal_identity_matches_the_symbolic_report(self):
        self.assertEqual(v.verify(self.witness, self.predecessor), self.report)

    def test_third_maps_and_moving_kernel_cannot_change(self):
        for key, order in (("B", 3), ("C", 3), ("source_row_corrections", 2)):
            with self.subTest(key=key):
                bad = copy.deepcopy(self.witness)
                entry = bad[key][order]["entries"][0]
                entry[2] = f"({entry[2]})+1"
                with self.assertRaisesRegex(ValueError, "Laurent order 3"):
                    v.verify(bad, self.predecessor)

    def test_credited_and_second_coefficients_cannot_change(self):
        for order, message in ((0, "credited"), (1, "credited"), (2, "second correction")):
            with self.subTest(order=order):
                bad = copy.deepcopy(self.witness)
                entry = bad["B"][order]["entries"][0]
                entry[2] = f"({entry[2]})+1"
                with self.assertRaisesRegex(ValueError, message):
                    v.verify(bad, self.predecessor)

    def test_leading_rank_is_checked_beyond_predecessor_agreement(self):
        bad, old = copy.deepcopy(self.witness), copy.deepcopy(self.predecessor)
        bad["B"][0]["entries"] = old["B"][0]["entries"] = []
        with self.assertRaisesRegex(ValueError, "leading minor"):
            v.verify(bad, old)

    def test_claim_schema_chart_and_review_scope_are_required(self):
        alterations = [("schema", "unknown"), ("status", "conjecture"), ("base", "c=d^3"),
                       ("exponent_improvement", True), ("independent_mathematical_review", "false")]
        for key, value in alterations:
            with self.subTest(key=key):
                bad = copy.deepcopy(self.witness)
                bad[key] = value
                with self.assertRaises(ValueError):
                    v.verify(bad, self.predecessor)
        bad = copy.deepcopy(self.witness)
        del bad["schema"]
        with self.assertRaisesRegex(ValueError, "schema"):
            v.verify(bad, self.predecessor)
        with self.assertRaisesRegex(ValueError, "schema"):
            v.verify([], self.predecessor)
        with self.assertRaisesRegex(ValueError, "predecessor"):
            v.verify(self.witness, {})

    def test_sparse_shapes_indices_and_jet_orders_are_checked(self):
        malformed = [
            {"shape": [13, 112], "entries": []},
            {"shape": [14, 112], "entries": [[14, 0, "1"]]},
            {"shape": [14, 112], "entries": [[0, 112, "1"]]},
            {"shape": [14, 112], "entries": [[0, -1, "1"]]},
            {"shape": [14, 112], "entries": [[False, 0, "1"]]},
            {"shape": [14, 112], "entries": [[0, 0, "0"]]},
            {"shape": [14, 112], "entries": [[0, 0, 1]]},
            {"shape": [14, 112], "entries": [[0, 0]]},
            {"shape": [14, 112], "entries": [[0, 0, "1"], [0, 0, "2"]]},
            {"shape": [14, 112], "entries": {}},
            {"shape": [14, 112], "entries": [], "ignored": True},
        ]
        for matrix in malformed:
            with self.subTest(matrix=matrix), self.assertRaises(ValueError):
                v.decode(matrix, (14, 112))
        for key in ("B", "C", "source_row_corrections"):
            bad = copy.deepcopy(self.witness)
            bad[key].pop()
            with self.subTest(key=key), self.assertRaisesRegex(ValueError, "jet order"):
                v.verify(bad, self.predecessor)

    def test_first_source_minor_indices_are_checked(self):
        for replacement in (1, 196, -1, False, "0"):
            bad = copy.deepcopy(self.witness)
            bad["output_pivot_columns"][0] = replacement
            with self.subTest(value=replacement), self.assertRaisesRegex(ValueError, "minor coordinates"):
                v.verify(bad, self.predecessor)
        bad = copy.deepcopy(self.witness)
        bad["output_pivot_columns"].pop()
        with self.assertRaisesRegex(ValueError, "minor coordinates"):
            v.verify(bad, self.predecessor)

    def test_exported_weights_and_denominator_metadata_are_checked(self):
        bad = copy.deepcopy(self.witness)
        bad["second_field_weights"][0] = "0"
        with self.assertRaisesRegex(ValueError, "weight metadata"):
            v.verify(bad, self.predecessor)
        bad = copy.deepcopy(self.witness)
        bad["coefficient_denominators"] = ["a+1"]
        with self.assertRaisesRegex(ValueError, "denominator metadata"):
            v.verify(bad, self.predecessor)

    def test_laurent_arithmetic_and_cancellation_have_exact_controls(self):
        self.assertEqual(v.expression("(a+b)*(a-b)"), v.expression("a**2-b**2"))
        self.assertEqual(v.expression("a/3+a/6"), v.expression("a/2"))
        self.assertEqual(v.expression("d**(-2)"), v.expression("1/d**2"))
        self.assertEqual(v.expression("(d+d)/(2*d)"), v.Polynomial(1))
        polynomial = v.expression("(a+b*d**3)**2/(3*d**2)")
        for a, b, d in ((2, 3, 1), (-1, 2, 2), (0, -4, -2)):
            actual = sum(c * Fraction(a)**i * Fraction(b)**j * Fraction(d)**k
                         for (i, j, k), c in polynomial.terms.items())
            self.assertEqual(actual, Fraction((a+b*d**3)**2, 3*d*d))

    def test_parser_rejects_code_nonrational_operations_and_extra_poles(self):
        invalid = ("1/(d+1)", "1/a", "1/b", "1/d**3", "1/0", "d**a",
                   "a**0.5", "a**(1/2)", "2.0", "True", "None", "c", "a//2",
                   "__import__('os')", "a.__class__", "[a for a in range(2)]",
                   "lambda: 1", "a**1000000", "((a+b)**64)**64",
                   "(((2**64)**64)**64)", "9"*40, "(")
        for text in invalid:
            with self.subTest(text=text), self.assertRaises(ValueError):
                v.expression(text)
        with self.assertRaises(ValueError):
            v.expression(None)

    def test_determinant_expansion_has_sign_and_zero_controls(self):
        matrix = {(0, 0): v.A, (0, 1): v.B, (1, 0): v.D, (1, 1): v.Polynomial(2)}
        expected = 2*v.A-v.B*v.D
        self.assertEqual(v.determinant(matrix, [0, 1]), expected)
        self.assertEqual(v.determinant(matrix, [1, 0]), -expected)
        self.assertEqual(v.determinant(matrix, [0, 0]), v.Polynomial())
        self.assertEqual(v.determinant({}, [0, 1]), v.Polynomial())
        self.assertEqual(v.determinant({}, []), v.Polynomial(1))

    def test_predecessor_hash_is_checked_before_parsing(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "changed.json.gz"
            path.write_bytes(v.PREDECESSOR.read_bytes() + b"changed")
            with self.assertRaisesRegex(ValueError, "predecessor hash"):
                v.read_predecessor(path)

    def test_cli_needs_no_site_packages_or_repository_working_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "nested" / "report.json"
            run = subprocess.run(
                [sys.executable, "-I", "-S", str(PACKAGE / "verify_laurent.py"),
                 str(RESULTS / "mixed-family.json"), "--predecessor", str(v.PREDECESSOR),
                 "--output", str(output)], cwd=directory, capture_output=True,
                text=True, timeout=30, check=True)
            self.assertEqual(json.loads(run.stdout), self.report)
            self.assertEqual(json.loads(output.read_text()), self.report)


if __name__ == "__main__":
    unittest.main()
