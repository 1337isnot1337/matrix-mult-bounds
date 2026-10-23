"""Exact source-coefficient regression for the singular integer pilot."""

import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-21-singular-pilots/verify_c45.py"
SPEC = importlib.util.spec_from_file_location("singular_c45", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class SingularPilotTests(unittest.TestCase):
    def test_full_integer_witness_matches_saved_certificate(self):
        saved = json.loads((ROOT / "results/singular-pilots-2026-10-21/c45_integer_witness.json").read_text())
        self.assertEqual(MODULE.replay(), saved)

    def test_constant_tensor_is_matrix_multiplication(self):
        constant = MODULE.replay()["constant_terms"]
        expected = [[0, 2*i+s, 2*i+j, 2*j+s, 1]
                    for i in range(2) for j in range(2) for s in range(2)]
        self.assertEqual(sorted(constant), sorted(expected))


if __name__ == "__main__":
    unittest.main()
