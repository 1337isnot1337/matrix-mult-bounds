import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / 'research/ai/2026-10-20-anisotropic-constructions/parity_balancing_cross_module_replay.py'
SPEC = importlib.util.spec_from_file_location('exact_cross_module_lifts', MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
RESULTS = ROOT / 'results/anisotropic-constructions-2026-10-20'


class ExactCrossModuleLiftTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reduced = json.loads((RESULTS / 'crossed-module11-witness.json').read_text())
        cls.full = json.loads((RESULTS / 'parity_balancing_cross_module11_full_maps.json').read_text())

    def test_complete_saved_maps_and_reconstructed_lifts(self):
        reduced = copy.deepcopy(self.reduced)
        reduced['status'] = 'untrusted metadata is ignored'
        report = MODULE.verify(reduced)
        actual = MODULE.verify_exported_lifts(self.full)
        self.assertEqual(report['full_sources'], actual)
        self.assertEqual([r['source_terms_checked'] for r in actual], [32768, 262144])
        self.assertEqual([r['target_shape'] for r in actual], [[4, 4, 11], [4, 4, 22]])
        self.assertEqual([r['nonzero_target_coefficients'] for r in actual], [176, 352])
        self.assertFalse(report['new_exponent_established'])

    def test_modified_actual_full_map_is_rejected(self):
        changed = copy.deepcopy(self.full)
        changed['constructions'][1]['maps'][0]['entries'][0][2] *= 2
        with self.assertRaises(ArithmeticError):
            MODULE.verify_exported_lifts(changed)

    def test_zero_duplicate_and_invalid_denominator_are_rejected(self):
        zero = copy.deepcopy(self.full)
        zero['constructions'][0]['maps'][1]['entries'] = []
        duplicate = copy.deepcopy(self.full)
        entries = duplicate['constructions'][0]['maps'][0]['entries']
        entries.append(entries[0][:])
        bad_denominator = copy.deepcopy(self.full)
        bad_denominator['constructions'][0]['maps'][1]['denominator'] = -2860
        for changed in (zero, duplicate, bad_denominator):
            with self.subTest(changed=changed is zero):
                with self.assertRaises(ArithmeticError):
                    MODULE.verify_exported_lifts(changed)


if __name__ == '__main__':
    unittest.main()
