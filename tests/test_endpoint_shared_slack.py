"""Acceptance checks for the conditional source-aspect extension."""

import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    'endpoint_shared_slack', ROOT / 'research/ai/2026-10-20-construction-sprint/verify_shared_slack.py')
VERIFIER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFIER)


class SharedSlackTests(unittest.TestCase):
    def test_exact_root_enclosures_and_endpoint(self):
        expected = json.loads((ROOT / 'results/endpoint-construction-sprint-2026-10-20/shared-slack.json').read_text())
        self.assertEqual(VERIFIER.verify(), expected)
        self.assertEqual([x['comparison'] for x in expected['cases']], [-1, -1, 0, 1])
        self.assertEqual(expected['cases'][1]['conditional_omega'], '2247/1000')
        self.assertFalse(expected['constructs_tensor_maps'])
        self.assertFalse(expected['improves_omega'])


if __name__ == '__main__':
    unittest.main()
