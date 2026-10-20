"""Independent support and matching checks for the mixed-weight covers."""
from fractions import Fraction
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research/ai/2026-10-20-koszul"))
import weight_slice_covers as covers


def support(m, alpha, beta):
    points = [(a, b) for b in range(m) for a in range(m-b)]
    edges = {}
    for a, b in points:
        adjacent = []
        for c, d in points:
            power = alpha*(a+b+c+d-m+1)-beta*(a+c)
            wanted = a == c == 0 and b+d == m-1
            if power > 0 or (power == 0 and wanted):
                adjacent.append((c, d))
        edges[a, b] = adjacent
    return edges


def matching_size(edges):
    matching = {}
    def augment(row, visited):
        for col in edges[row]:
            if col in visited:
                continue
            visited.add(col)
            if col not in matching or augment(matching[col], visited):
                matching[col] = row
                return True
        return False
    return sum(augment(row, set()) for row in edges)


class WeightSliceCoverTests(unittest.TestCase):
    def test_every_allowed_edge_is_covered(self):
        for m in range(2, 9):
            for alpha, beta in ((1,1), (3,2), (2,1), (5,2), (1,-1), (1,2)):
                result = covers.best_cover(m, alpha, beta)
                rows, cols = covers.cover(m, alpha, beta, result["threshold"])
                self.assertEqual(len(rows)+len(cols), result["rank_upper_per_copy"])
                graph = support(m, alpha, beta)
                for row, adjacent in graph.items():
                    for col in adjacent:
                        self.assertTrue(row in rows or col in cols)
                self.assertLessEqual(matching_size(graph), len(rows)+len(cols))

    def test_balanced_formula_and_independent_matchings(self):
        for m in range(2, 41):
            d = m-1
            threshold = d if d % 2 else d-1
            rows, cols = covers.cover(m, 2, 1, threshold)
            expected = m*(m+1)//2-m//2
            self.assertEqual(len(rows)+len(cols), expected)
            self.assertEqual(covers.best_cover(m, 2, 1)["rank_upper_per_copy"], expected)
            if m <= 10:
                self.assertEqual(matching_size(support(m, 2, 1)), expected)

    def test_uniform_lattice_estimate(self):
        for m in range(2, 35):
            d = m-1
            for beta in range(1, 7):
                for alpha in range(beta, 2*beta+1):
                    r = Fraction(alpha, beta)
                    count = sum(2*((alpha-beta)*a+alpha*b) > alpha*d
                                for a, b in covers.nodes(m))
                    bound = r*d*d/8+(1+r)*d/2+1
                    self.assertLessEqual(count, bound)

    def test_boundary_entry_requires_extra_row(self):
        rows, cols = covers.cover(5, 2, 1, 4)
        self.assertIn((0, 2), rows)
        self.assertNotIn((0, 2), cols)
        self.assertIn((0, 2), support(5, 2, 1)[0, 2])

    def test_replay_report_and_replicated_target(self):
        saved = json.loads((ROOT / "results/koszul-2026-10-20/weight_slice_covers.json").read_text())
        self.assertEqual(covers.report(), saved)
        case = saved["four_block_replicated_case"]
        self.assertEqual(case["necessary_B"], 12*case["k"]-3)
        self.assertGreater(case["necessary_B"], case["proposed_B"])


if __name__ == "__main__":
    unittest.main()
