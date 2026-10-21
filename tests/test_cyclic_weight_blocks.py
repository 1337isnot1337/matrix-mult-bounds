from collections import Counter, defaultdict
import gzip
import importlib.util
from itertools import combinations, product
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-20-cyclic-weight-blocks'


def load(name):
    spec = importlib.util.spec_from_file_location(name, PACKAGE/(name+'.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


blocks = load('blocks')
quotient = load('root_quotient')


class CyclicWeightBlockTests(unittest.TestCase):
    def test_complete_retained_block_report(self):
        saved = json.loads(gzip.decompress((ROOT/'results/cyclic-weight-blocks-2026-10-20/blocks.json.gz').read_bytes()))
        self.assertEqual(json.loads(json.dumps(blocks.report())), saved)

    def test_target_ranks_from_independent_full_matrix_tensor(self):
        vertices = [[0, 1, 2, 2, 3, 4], [0, 1, 2, 2, 3, 4], [0, 1, 1, 2, 3, 3, 4]]
        dimensions = list(map(len, vertices))
        weight_spaces = []
        for axis in range(3):
            groups = defaultdict(dict)
            for i, j in product(range(dimensions[axis]), range(dimensions[(axis+1)%3])):
                weight = vertices[(axis+1)%3][j]-vertices[axis][i]
                groups[weight][i, j] = len(groups[weight])
            weight_spaces.append(groups)
        tensors = defaultdict(list)
        for i, j, k in product(*[range(n) for n in dimensions]):
            indices = (i, j, k)
            weights = tuple(vertices[(a+1)%3][indices[(a+1)%3]]-vertices[a][indices[a]] for a in range(3))
            tensors[weights].append(tuple(weight_spaces[a][weights[a]][indices[a], indices[(a+1)%3]] for a in range(3)))
        _, source_groups, _ = blocks.source_blocks(3)
        checked = 0
        for weights, tensor in tensors.items():
            for axis in range(3):
                order = [axis, (axis+1)%3, (axis+2)%3]
                ambient = len(source_groups[axis][weights[axis]])
                dims = (ambient,)+tuple(len(weight_spaces[a][weights[a]]) for a in order[1:])
                terms = [tuple(t[a] for a in order) for t in tensor]
                shapes = [(s[(axis+1)%3], s[(axis+2)%3], s[axis]) for s in blocks.target_shapes(3, weights)]
                for p in range(min(2, ambient-1)+1):
                    expected = sum(blocks.paired.padded_matrix_rank(s, ambient, p) for s in shapes)
                    self.assertEqual(blocks.rank_mod2(dims, terms, p), expected)
                    checked += 1
        self.assertEqual(checked, 489)

    def test_exterior_grades_against_direct_subsets(self):
        _, groups, grades = blocks.source_blocks(3)
        for axis in range(3):
            for members in groups[axis].values():
                vectors = tuple(grades[axis][i] for i in members)
                counts = blocks.wedge_weights(vectors)
                for p in range(len(vectors)+1):
                    direct = Counter(tuple(sum(v[g] for v in subset) for g in range(2))
                                     for subset in combinations(vectors, p))
                    self.assertEqual(counts[p], direct)

    def test_quotient_report_and_independent_finite_field_line(self):
        saved = json.loads((ROOT/'results/cyclic-weight-blocks-2026-10-20/root-quotient.json').read_text())
        self.assertEqual([quotient.quotient_control(D) for D in range(2, 11)], saved['records'])
        prime = 65521
        for D in range(2, 11):
            order = 2*D
            root = next(pow(g, (prime-1)//order, prime) for g in range(2, prime)
                        if all(pow(pow(g, (prime-1)//order, prime), k, prime) != 1
                               for k in range(1, order)))
            inverse = pow(root, -1, prime)
            denominator = pow((root-inverse) % prime, -1, prime)
            qint = lambda n: (pow(root, n, prime)-pow(inverse, n, prime))*denominator % prime
            m = 2*D-2
            trivial_indices = [i for i in range(m+1)
                               if pow(root, m-2*i, prime) == 1
                               and (i == 0 or qint(m-i+1) == 0)
                               and (i == m or qint(i+1) == 0)]
            self.assertEqual(trivial_indices, [D-1])
            self.assertNotEqual(qint(D-1), 0)


if __name__ == '__main__':
    unittest.main()
