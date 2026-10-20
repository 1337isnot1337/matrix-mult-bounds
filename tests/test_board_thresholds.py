"""Integer consequences of cited bounds, not a proof of the external bounds."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "board_thresholds", ROOT / "research/ai/2026-10-20-koszul/board_thresholds.py")
thresholds = importlib.util.module_from_spec(spec)
spec.loader.exec_module(thresholds)


class ThresholdTests(unittest.TestCase):
    def test_strict_power_boundary(self):
        for n in range(2, 101):
            r = thresholds.strict_rank_ceiling(n)
            self.assertLess(r ** 4, n ** 9)
            self.assertGreaterEqual((r + 1) ** 4, n ** 9)
        self.assertEqual(thresholds.strict_rank_ceiling(16), 511)

    def test_corrected_window(self):
        for n in range(3, 38):
            self.assertGreater(thresholds.exact_rank_floor(n), thresholds.strict_rank_ceiling(n))
        self.assertEqual(thresholds.exact_rank_floor(38), 3585)
        self.assertEqual(thresholds.strict_rank_ceiling(38), 3585)

    def test_report_replay(self):
        path = ROOT / "results/koszul-2026-10-20/board_thresholds.json"
        self.assertEqual(thresholds.run(), json.loads(path.read_text()))


if __name__ == "__main__":
    unittest.main()
