import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-20-anisotropic-constructions/fixed_anchor_obstruction.py"
SPEC = importlib.util.spec_from_file_location("fixed_anchor_obstruction", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class FixedAnchorObstructionTests(unittest.TestCase):
    def test_complete_functional_identity_and_corrected_control(self):
        path = ROOT / "results/anisotropic-constructions-2026-10-20/fixed-anchor-obstruction.json"
        self.assertEqual(MODULE.report(), json.loads(path.read_text()))
        self.assertEqual(MODULE.report()["forced_source_value"], 0)
        self.assertEqual(MODULE.report()["corrected_endpoint_value"], 1)

    def test_obstruction_maps_match_the_preserved_hadamard_seed(self):
        path = ROOT / "results/anisotropic-constructions-2026-10-20/parity_balancing_torus_anchor_hadamard_seed.json"
        data = json.loads(path.read_text())
        denominator = data["map_denominator"]
        for (leg, target_row), expected in zip(
            [(0, 25), (0, 53), (1, 675), (1, 703)], MODULE.FIXED_MAPS
        ):
            actual = []
            for row, column, value in data["maps"][leg]:
                if row != target_row:
                    continue
                if leg == 0:
                    i, k, s = column // 120, (column // 8) % 15, column % 8
                else:
                    s, i, k = column // 120, (column // 15) % 8, column % 15
                self.assertEqual(value % denominator, 0)
                actual.append([i, k, s, value // denominator])
            self.assertEqual(sorted(actual), sorted(expected))

    def test_changed_fixed_map_rejected(self):
        maps = copy.deepcopy(MODULE.FIXED_MAPS)
        maps[0][2][-1] = 2
        with self.assertRaisesRegex(ArithmeticError, "functional identity"):
            MODULE.verify_fixed_maps(maps)


if __name__ == "__main__":
    unittest.main()
