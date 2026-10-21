import hashlib
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / 'research/ai/2026-10-20-anisotropic-constructions'
RESULTS = ROOT / 'results/anisotropic-constructions-2026-10-20'
SPEC = importlib.util.spec_from_file_location('parity_balancing_newton_pruning_audit',
                                             HERE / 'parity_balancing_newton_pruning_audit.py')
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class IndependentNewtonTests(unittest.TestCase):
    def test_independent_full_source_replay_matches_every_primary_mask(self):
        actual = MODULE.replay()
        expected = json.loads((RESULTS / 'parity_balancing_newton_pruning_audit.json').read_text())
        self.assertEqual(json.loads(json.dumps(actual)), expected)
        primary = json.loads((RESULTS / 'torus-support-peeling-a88-m27-m7.json').read_text())
        self.assertEqual(len(actual['rounds']), len(primary['rounds']))
        alive = set(range(960))
        for independent, certified in zip(actual['rounds'], primary['rounds']):
            self.assertEqual(independent['available_dimension'], certified['input_dimension'])
            self.assertEqual(independent['matrix_unit_lift_rank_upper_bound'], certified['rank_limit'])
            self.assertEqual(independent['restricted_source_nonzero_terms'], certified['retained_source_terms'])
            alive.difference_update(row['coordinate'] for row in certified['removed_coordinates'])
            digest = hashlib.sha256(json.dumps(sorted(alive), separators=(',', ':')).encode()).hexdigest()
            self.assertEqual(independent['output_coordinate_sha256'], digest)
        self.assertEqual(len(alive), 468)
        self.assertLess(len(alive), primary['target_dimension_each_leg'])


if __name__ == '__main__':
    unittest.main()
