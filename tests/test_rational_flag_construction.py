"""Exact coefficient checks for the partial flag and explicit T4 maps."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def module(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


EXPLICIT = module('explicit_rational_t4', 'research/ai/2026-10-21-rectangular-t4-certificate/verify_explicit.py')
FIRST_FLAG = module('first_polynomial_flag', 'research/ai/2026-10-20-rectangular-module/verify_first_flag.py')
RESULTS = ROOT / 'results/rectangular-t4-certificate-2026-10-21'


class RationalFlagConstructionTests(unittest.TestCase):
    def test_every_explicit_coefficient_and_all_map_ranks(self):
        data = json.loads((RESULTS / 'rational-witness.json').read_text())
        expected = json.loads((RESULTS / 'rational-verification.json').read_text())
        expected.pop('witness_sha256')
        self.assertEqual(EXPLICIT.verify(data), expected)

    def test_corrupted_output_coefficient_is_rejected(self):
        data = copy.deepcopy(json.loads((RESULTS / 'rational-witness.json').read_text()))
        data['z'][0][0] = str(int(data['z'][0][0])+1)
        with self.assertRaises(AssertionError):
            EXPLICIT.verify(data)

    def test_all_saved_partial_flag_controls(self):
        saved = json.loads((ROOT / 'results/rectangular-module-2026-10-20/first_flag.json').read_text())
        count = 0
        for record in saved['records']:
            with self.subTest(m=record['m'], B=record['B']):
                actual = FIRST_FLAG.verify(record['m'], record['B']-record['N'])
                self.assertEqual(actual, record)
                count += actual['all_first_three_input_coefficients_checked']
        self.assertEqual(count, 89739)


if __name__ == '__main__':
    unittest.main()
