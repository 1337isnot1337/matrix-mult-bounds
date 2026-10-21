import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "research/ai/2026-10-20-anisotropic-constructions/crossed_module11.py"
SPEC = importlib.util.spec_from_file_location("crossed_module11", MODULE)
MODULE11 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE11)


class CrossedModule11Tests(unittest.TestCase):
    def test_complete_construction_and_original_source_replay(self):
        witness = json.loads(MODULE11.WITNESS.read_text())
        actual = MODULE11.verify_witness(witness)
        actual["witness_sha256"] = hashlib.sha256(MODULE11.WITNESS.read_bytes()).hexdigest()
        self.assertEqual(actual, json.loads(MODULE11.REPORT.read_text()))
        self.assertEqual(actual["coefficient_replay"]["nonzero_target_coefficients"], 44)
        self.assertEqual(actual["join_determinant"], "-3575/128")
        self.assertFalse(actual["new_exponent_established"])

    def test_modified_source_map_is_rejected(self):
        witness = json.loads(MODULE11.WITNESS.read_text())
        changed = copy.deepcopy(witness)
        changed["Z"]["entries"][0][2] += 1
        with self.assertRaises(ArithmeticError):
            MODULE11.verify_witness(changed)

    def test_false_join_or_exponent_claim_is_rejected(self):
        witness = json.loads(MODULE11.WITNESS.read_text())
        changed = copy.deepcopy(witness)
        changed["join_determinant"] = "1"
        with self.assertRaises(ArithmeticError):
            MODULE11.verify_witness(changed)
        changed = copy.deepcopy(witness)
        changed["new_exponent_established"] = True
        with self.assertRaises(ArithmeticError):
            MODULE11.verify_witness(changed)


if __name__ == "__main__":
    unittest.main()
