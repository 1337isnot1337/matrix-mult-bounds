"""All-degree, signed coefficient checks for the narrow Q_(3,2) source."""

import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'research/ai/2026-10-20-paired-construction/narrow_koszul_exact.py'
SPEC = importlib.util.spec_from_file_location('narrow_koszul_exact', PATH)
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class NarrowKoszulTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = module.run()

    def test_all_25_rational_rank_comparisons(self):
        expected_source = [[8, 72, 272, 568, 720, 568, 272, 72, 8],
                           [9, 72, 242, 424, 413, 224, 64, 8],
                           [9, 72, 242, 424, 413, 224, 64, 8]]
        expected_target = [[6, 54, 216, 474, 612, 474, 216, 54, 6],
                           [9, 72, 222, 354, 321, 168, 48, 6],
                           [9, 72, 222, 354, 321, 168, 48, 6]]
        self.assertEqual(self.report['comparison_count'], 25)
        for leg in range(3):
            records = [r for r in self.report['records'] if r['leg'] == leg]
            self.assertEqual([r['source_rank_q'] for r in records], expected_source[leg])
            self.assertEqual([r['target_rank_q'] for r in records], expected_target[leg])
        self.assertTrue(self.report['all_pass'])
        self.assertFalse(self.report['improves_omega'])

    def test_mod_two_lower_ranks_and_full_long_leg_padding(self):
        for record in self.report['records']:
            self.assertEqual(record['source_rank_q'], record['source_rank_mod2'])
            self.assertEqual(record['target_rank_q'], record['target_rank_mod2'])
            if record['leg'] in (1, 2):
                self.assertEqual(record['target']['dimensions'][record['leg']], 8)
                self.assertLessEqual(record['power'], 7)

    def test_known_positive_q2_control_is_not_excluded(self):
        # Q_(2,2)=P2 has the independently verified exact M2 restriction in
        # exact_p2.py and chain_family.py. Every necessary rank test must pass.
        report = module.run(2, 2)
        self.assertEqual(report['comparison_count'], 16)
        self.assertTrue(report['all_pass'])


if __name__ == '__main__':
    unittest.main()
