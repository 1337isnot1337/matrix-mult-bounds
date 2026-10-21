"""Complex graph closure, modular certificate rejection and graph charts."""
import copy
import importlib.util
from itertools import combinations
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('mixed_graph_verifier', ROOT / 'research/ai/2026-10-21-mixed-five-space-graphs/verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class MixedGraphTests(unittest.TestCase):
    def test_complete_source_and_certificate_replay(self):
        saved = ROOT / 'results/mixed-five-space-graphs-2026-10-21/report.json'
        self.assertEqual(verify.report(), json.loads(saved.read_text()))
        for case in verify.report()['cases']:
            self.assertEqual(case['final_nonplane_dimension'], 0)
            self.assertEqual([(s['before'], s['after']) for s in case['terminal'] if s['kind'] == 'mixed_row'], [(10, 2), (2, 0)])

    def test_duplicated_quadratic_witness_is_rejected(self):
        record = json.loads((verify.HERE / 'quadratic-witnesses.json').read_text())[0]
        witnesses = copy.deepcopy(record['selected_minors'])
        witnesses[-1] = witnesses[0]
        matrix = verify.graph_data(tuple(record['graph']))['q_remaining']
        with self.assertRaisesRegex(ArithmeticError, 'dependent'):
            verify.quadratic_span(matrix, witnesses)

    def test_prime_divisible_denominator_is_rejected(self):
        matrix = verify.sp.SparseMatrix(6, 1, {(0, 0): verify.sp.Rational(1, verify.PRIME), (3, 0): 1})
        with self.assertRaisesRegex(ArithmeticError, 'denominator'):
            verify.quadratic_span(matrix, [[0, 1, 0, 1]])

    def test_coordinate_complement_recovers_mixed_graph(self):
        # A non-coordinate boundary space; replay the chart lemma by solving
        # in the actual six-dimensional ambient space, independently of Z.
        sp = verify.sp
        boundary = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0],
                              [0, 0, 0, 1], [2, -1, 3, 1], [1, 4, -2, 2]])
        graph = sp.Matrix([2, -1, 1, 3, -2, 1])
        covered = 0
        for pair in combinations(range(6), 2):
            coordinate = sp.eye(6)[:, list(pair)]
            basis = boundary.row_join(coordinate)
            if basis.det() == 0:
                continue
            solution = basis.inv()*graph
            representative = coordinate*solution[4:, :]
            self.assertEqual(graph-representative, boundary*solution[:4, :])
            self.assertTrue(all(representative[i] == 0 for i in set(range(6))-set(pair)))
            covered += 1
        self.assertGreater(covered, 0)


if __name__ == '__main__':
    unittest.main()
