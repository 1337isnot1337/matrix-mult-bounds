"""Coverage guarantees for the parallel CI runner."""
from collections import Counter
import importlib.util
from pathlib import Path
import unittest


SPEC = importlib.util.spec_from_file_location(
    "test_shard_runner", Path(__file__).resolve().parents[1] / "tools/test_shard.py")
RUNNER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RUNNER)


def sample_suite():
    result = []
    for module in ("alpha", "beta", "delta", "gamma", "omega"):
        for name in ("First", "Second"):
            cls = type(name, (unittest.TestCase,), {
                "__module__": module, "runTest": lambda self: None})
            result.append(cls())
    # Preserve repeated cases as well as nested suites.
    return unittest.TestSuite([unittest.TestSuite(result[:4]),
                               unittest.TestSuite(result[4:]), result[0]])


class TestShardingTests(unittest.TestCase):
    def test_complete_partition_preserves_multiplicity_and_module_fixtures(self):
        original = list(RUNNER.cases(sample_suite()))
        actual, ownership = [], {}
        for index in range(4):
            selected, coverage = RUNNER.select_shard(sample_suite(), index, 4)
            actual.extend(test.id() for test in RUNNER.cases(selected))
            self.assertEqual(coverage["total_tests"], len(original))
            for module in coverage["selected_modules"]:
                self.assertNotIn(module, ownership)
                ownership[module] = index
        self.assertEqual(Counter(actual), Counter(test.id() for test in original))
        self.assertEqual(set(ownership), {test.__class__.__module__ for test in original})

    def test_single_group_retains_discovery_order(self):
        original = [test.id() for test in RUNNER.cases(sample_suite())]
        selected, _ = RUNNER.select_shard(sample_suite(), 0, 1)
        self.assertEqual([test.id() for test in RUNNER.cases(selected)], original)

    def test_failed_import_is_assigned_instead_of_dropped(self):
        suite = unittest.TestLoader().loadTestsFromName("missing_module_for_shard_control")
        total = sum(RUNNER.select_shard(suite, index, 4)[0].countTestCases()
                    for index in range(4))
        self.assertEqual(total, 1)

    def test_invalid_group_bounds_are_rejected(self):
        for index, count in ((0, 0), (-1, 4), (4, 4)):
            with self.assertRaises(ValueError):
                RUNNER.select_shard(sample_suite(), index, count)


if __name__ == "__main__":
    unittest.main()
