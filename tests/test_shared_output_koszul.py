"""Exact witness replay and independent literal block-decomposition controls."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "research/ai/2026-10-23-shared-output-koszul/verify.py"
SPEC = importlib.util.spec_from_file_location("shared_output_koszul", MODULE)
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


class SharedOutputKoszulTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = json.loads((VERIFY.RESULTS / "certificate.json").read_text())

    def test_saved_exact_certificate_and_report(self):
        report = VERIFY.verify(self.certificate)
        self.assertEqual(report, json.loads((VERIFY.RESULTS / "verification.json").read_text()))
        self.assertEqual(report["source"]["koszul_rank"], 2595)
        self.assertEqual(report["target"]["koszul_rank"], 2616)

    def test_literal_unsplit_decomposition(self):
        for names in (["E3", "E3"], ["E3", "O"], ["E2", "O"], ["O", "O"]):
            with self.subTest(names=names):
                actual = len(VERIFY.rref(VERIFY.full_matrix(names))[1])
                split = sum(VERIFY.EXPECTED_INTRINSIC[name] for name in names)
                split += VERIFY.EXPECTED_CROSS["/".join(names)]
                self.assertEqual(actual, split)

    def test_corrupt_nonzero_minor_is_rejected(self):
        certificate = copy.deepcopy(self.certificate)
        certificate["cross/E4/E4"]["minor_determinant"] = "0"
        with self.assertRaisesRegex(ValueError, "nonzero minor"):
            VERIFY.verify(certificate)

    def test_corrupt_kernel_is_rejected(self):
        certificate = copy.deepcopy(self.certificate)
        entry = certificate["cross/E4/E4"]["kernel_vectors"][0]
        entry["entries"][str(entry["free_column"])] = "2"
        with self.assertRaisesRegex(ValueError, "kernel independence"):
            VERIFY.verify(certificate)

    def test_literal_coefficient_change_is_rejected(self):
        matrix = VERIFY.cross_matrix("E4", "E4")
        matrix[0][0] += 1
        with self.assertRaisesRegex(ValueError, "literal matrix digest"):
            VERIFY.verify_rank_certificate(matrix, self.certificate["cross/E4/E4"])


if __name__ == "__main__":
    unittest.main()
