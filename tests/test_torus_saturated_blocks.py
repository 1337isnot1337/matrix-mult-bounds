import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'research/ai/2026-10-20-anisotropic-constructions/torus_saturated_blocks.py'
SPEC = importlib.util.spec_from_file_location('torus_saturated_blocks', PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class SaturatedBlockTests(unittest.TestCase):
    def test_saved_certificate_recomputed_and_tamper_rejected(self):
        saved = ROOT / 'results/anisotropic-constructions-2026-10-20/torus-saturated-width13.json'
        result = MODULE.verify_saved(saved)
        self.assertTrue(result['profile_excluded'])
        self.assertTrue(result['capacity_feasible'])
        self.assertEqual(result['decisive_rank_comparison'], {
            'source': 16, 'codimension': 4,
            'necessary_target_rank': 12, 'actual_target_rank': 9,
        })
        result['decisive_rank_comparison']['actual_target_rank'] = 12
        with tempfile.TemporaryDirectory() as directory:
            tampered = Path(directory) / 'tampered.json'
            tampered.write_text(json.dumps(result))
            with self.assertRaisesRegex(ArithmeticError, 'certificate mismatch'):
                MODULE.verify_saved(tampered)

    def test_saturation_hypothesis_and_orientation_are_enforced(self):
        profile = MODULE.width13_profile()
        with self.assertRaisesRegex(ValueError, 'must be nonzero and saturated'):
            MODULE.saturated_block(8, 8, profile, 0, -13, 13)
        forward = MODULE.saturated_block(8, 8, profile, 0, -11, 11)
        reverse = MODULE.saturated_block(8, 8, profile, 0, 11, -11)
        self.assertTrue(forward['excluded'])
        self.assertFalse(reverse['excluded'])
        self.assertEqual(reverse['target_third_flattening_rank'], 12)

    def test_positive_identity_and_cyclic_unequal_vertex_lists(self):
        identity = MODULE.screen(1, 1, [[[0], [0], [0]]])
        self.assertFalse(identity['excluded'])
        self.assertEqual(len(identity['saturated_blocks']), 3)
        # An actual M2 tensor with three different charge lists. Independently
        # enumerate all eight multiplication terms, checking every weight pair.
        block = [[0, 1], [0, 2], [-1, 0]]
        for leg in range(3):
            expected = {}
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        vertices = [i, j, k]
                        charges = [block[t][vertices[t]] for t in range(3)]
                        wx = charges[leg] - charges[(leg + 1) % 3]
                        wy = charges[(leg + 1) % 3] - charges[(leg + 2) % 3]
                        expected.setdefault((wx, wy), set()).add(
                            (0, vertices[(leg + 2) % 3], vertices[leg]))
            for weights, units in expected.items():
                self.assertEqual(set(MODULE.target_image([block], leg, *weights)), units)
                self.assertEqual(MODULE.target_rank([block], leg, *weights), len(units))
        failure = MODULE.screen(1, 1, [block])
        self.assertTrue(failure['capacity_failures'])
        self.assertEqual(failure['saturated_blocks'], [])


if __name__ == '__main__':
    unittest.main()
