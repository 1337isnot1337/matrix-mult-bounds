"""Run a deterministic share of the complete unittest discovery suite."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def cases(suite):
    for test in suite:
        if isinstance(test, unittest.TestSuite):
            yield from cases(test)
        else:
            yield test


def select_shard(suite, index, count):
    if count < 1 or not 0 <= index < count:
        raise ValueError("shard count must be positive and index must be in range")
    discovered = list(cases(suite))
    modules = sorted({test.__class__.__module__ for test in discovered})
    selected_modules = set(modules[index::count])
    selected = [test for test in discovered
                if test.__class__.__module__ in selected_modules]
    return unittest.TestSuite(selected), {
        "total_tests": len(discovered),
        "total_modules": len(modules),
        "selected_modules": sorted(selected_modules),
        "test_ids": [test.id() for test in selected],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--shard-index", type=int, default=0)
    parser.add_argument("--shard-count", type=int, default=1)
    parser.add_argument("--list", action="store_true", help="list coverage without running tests")
    args = parser.parse_args()
    if args.shard_count < 1 or not 0 <= args.shard_index < args.shard_count:
        parser.error("shard count must be positive and index must be in range")
    suite, coverage = select_shard(
        unittest.TestLoader().discover(str(ROOT / "tests")),
        args.shard_index, args.shard_count,
    )
    if args.list:
        print(json.dumps(coverage, indent=2))
        return 0
    print(f"Group {args.shard_index + 1}/{args.shard_count}: "
          f"{suite.countTestCases()}/{coverage['total_tests']} tests in "
          f"{len(coverage['selected_modules'])}/{coverage['total_modules']} modules",
          flush=True)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
