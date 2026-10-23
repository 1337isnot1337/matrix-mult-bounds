"""The exact fixed-repaired-core gate, with its narrow scope retained."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-20-anisotropic-constructions/spin_endpoint_extension.py"
SPEC = importlib.util.spec_from_file_location("spin_endpoint_extension", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class SpinEndpointExtensionTests(unittest.TestCase):
    def test_exact_forced_image_and_injective_G1(self):
        report = MODULE.verify()
        self.assertEqual(report["G1_column_rank"], 120)
        self.assertEqual(report["forced_first_image_dimension"], 778)
        self.assertTrue(report["first_core_images_may_change_by_kernel_vectors"])
        self.assertFalse(report["D774_extension_excluded"])
        self.assertFalse(report["changed_retained_maps_excluded"])

    def test_excluded_channel_cannot_be_used_in_minor(self):
        data = json.loads(MODULE.endpoint.MAPS.read_text())
        specification = json.loads(MODULE.MINOR.read_text())
        changed = copy.deepcopy(specification)
        changed["selected_row_labels_i_s_I_beta"][0][3] = 0
        with self.assertRaises(ArithmeticError):
            MODULE.rebuild_minor(data, changed)


if __name__ == "__main__":
    unittest.main()
