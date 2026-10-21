import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-20-anisotropic-constructions/coordinate_compression_limit.py"
SPEC = importlib.util.spec_from_file_location("coordinate_compression_limit", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class CommonCoordinateCodeTests(unittest.TestCase):
    def test_saved_collisions_and_seed_injectivity(self):
        saved = json.loads((ROOT / "results/anisotropic-constructions-2026-10-20/coordinate-compression-limit.json").read_text())
        self.assertEqual(json.loads(json.dumps(MODULE.report())), saved)
        self.assertEqual(saved["common_coordinate_code_ceiling"], 24)
        for entry in saved["collision_certificates"]:
            self.assertTrue(MODULE.verify_collision(8, 8, entry["vertices"], entry["collision"]))

    def test_altered_source_coordinate_rejected(self):
        entry = MODULE.report()["collision_certificates"][0]
        altered = copy.deepcopy(entry["collision"])
        altered["common_source_coordinate"][1] += 1
        with self.assertRaisesRegex(ArithmeticError, "do not coincide"):
            MODULE.verify_collision(8, 8, entry["vertices"], altered)


if __name__ == "__main__":
    unittest.main()
