"""Replay the all-parameter identities and independently check both strata."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-21-both-mixed-first-spaces'
RESULTS = ROOT / 'results/both-mixed-first-spaces-2026-10-21'


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


verify = load('both_mixed_verification', PACKAGE / 'verify.py')
original = load('both_mixed_original_source', ROOT / 'tests/test_mixed_first_jets.py')


class BothMixedFirstSpaceTests(unittest.TestCase):
    def test_complete_symbolic_partner_identities_and_exact_controls(self):
        self.assertEqual(verify.report(), json.loads((RESULTS / 'report.json').read_text()))

    def test_independent_source_replay_for_both_rank_strata(self):
        for filename in ('seven-seven-seed.json', 'invertible-lines-seed.json'):
            seed = json.loads((RESULTS / filename).read_text())
            left = verify.third.verify.rows(seed.get('B_rows', seed.get('first_constant_B_new')))
            right = verify.third.verify.rows(seed.get('C_rows', seed.get('first_constant_C_new')))
            p0, q0 = verify.extension.G+[{} for _ in left], verify.extension.G+[{} for _ in right]
            p1, q1 = [{} for _ in range(4)]+left, [{} for _ in range(4)]+right
            coefficients = [original.original_contract(p0, q0),
                            verify.third.verify.add((1, original.original_contract(p1, q0)),
                                                    (1, original.original_contract(p0, q1))),
                            original.original_contract(p1, q1)]
            for tensor in coefficients:
                self.assertFalse(any(a in verify.extension.OUTSIDE for a, b, c in tensor))

    def test_changed_boundary_graph_is_rejected(self):
        seed = json.loads((RESULTS / 'seven-seven-seed.json').read_text())
        left = verify.third.verify.rows(seed['B_rows'])
        right = verify.third.verify.rows(seed['C_rows'])
        incompatible = next(row for row in verify.data()['B'][:12]
                            if any(verify.extension.contract([row], right, verify.extension.OUTSIDE)))
        for j, value in incompatible.items():
            left[-1][j] = left[-1].get(j, 0)+value
        seed['B_rows'] = [[[j, int(value.numerator), int(value.denominator)]
                          for j, value in row.items() if value] for row in left]
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / 'changed-seed.json'
            path.write_text(json.dumps(seed))
            with self.assertRaisesRegex(ArithmeticError, 'do not annihilate H'):
                verify.check_seed(path, (7, 7))


if __name__ == '__main__':
    unittest.main()
