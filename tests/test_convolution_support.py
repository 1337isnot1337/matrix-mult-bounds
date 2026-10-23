"""Coverage and adversarial replay tests for arbitrary convolution relabelings."""
import copy
import importlib.util
from itertools import permutations, product
import json
from pathlib import Path
import random
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


support = load('convolution_support', ROOT / 'tools/convolution_support.py')
archive = load('old_support_search', ROOT / 'research/ai/2026-10-20/search_degenerations.py')


class ConvolutionSupportTests(unittest.TestCase):
    def test_all_small_shapes_axes_and_seeded_permutations(self):
        rng = random.Random(20261023)
        count = 0
        for a, b in product(range(1, 6), repeat=2):
            for axes in permutations(range(3)):
                labels = []
                for size in (a, b, a + b - 1):
                    values = list(range(-3 * size, 0, 3))
                    rng.shuffle(values)
                    labels.append(values)
                terms = [tuple((labels[0][i], labels[1][j], labels[2][i+j])[k]
                               for k in axes) for i in range(a) for j in range(b)]
                rng.shuffle(terms)
                cert = support.recognize(terms)
                self.assertIsNotNone(cert, (a, b, axes))
                self.assertTrue(support.verify(terms, json.loads(json.dumps(cert))))
                self.assertEqual(cert, support.recognize(reversed(terms)))
                count += 1
        self.assertEqual(count, 150)

    def test_exhaustive_two_by_three_colorings(self):
        # An independent finite oracle enumerates coordinate permutations,
        # while the recognizer solves additive equations. Include nonsurjective
        # colorings and every false complete bipartite support in this format.
        canonical = [(i, j, i+j) for i in range(2) for j in range(3)]
        expected = set()
        for x in permutations(range(2)):
            for y in permutations(range(3)):
                for z in permutations(range(4)):
                    expected.add(tuple(sorted((x[i], y[j], z[k]) for i, j, k in canonical)))
        accepted = 0
        for colors in product(range(4), repeat=6):
            terms = [(i, j, colors[3*i+j]) for i in range(2) for j in range(3)]
            cert = support.recognize(terms)
            self.assertEqual(cert is not None, tuple(terms) in expected, colors)
            if cert is not None:
                support.verify(terms, cert)
                accepted += 1
        self.assertEqual(accepted, len(expected))
        self.assertEqual(accepted, 144)

    def test_stronger_block_score_witness(self):
        terms = json.loads((ROOT / 'tests/fixtures/relabelled_convolution.json').read_text())
        old = archive.recognize(terms)
        new = support.recognize(terms)
        self.assertEqual(old['kind'], 'slice_lower_bound')
        h = archive.slopes(10)
        self.assertEqual(archive.profile(old['a'], old['b'], h), 4)
        self.assertEqual(str(archive.profile(new['a'], new['b'], h)), '70/9')
        self.assertTrue(support.verify(terms, new))

    def test_false_supports_rejected(self):
        terms = [(i, j, i+j) for i in range(3) for j in range(4)]
        self.assertIsNone(support.recognize(terms[:-1]))
        # Same dimensions, term count, and complete input pairs; wrong sum colors.
        damaged = terms.copy()
        damaged[1] = (0, 1, 2)
        self.assertIsNone(support.recognize(damaged))
        # Full Latin-square support cannot be a convolution.
        self.assertIsNone(support.recognize([(i, j, (i+j) % 3)
                                             for i in range(3) for j in range(3)]))

    def test_certificate_tampering_rejected(self):
        terms = [(i, j, i+j) for i in range(3) for j in range(4)]
        cert = support.recognize(terms)
        changes = [lambda c: c.update(a=4), lambda c: c.update(output_axis=True),
                   lambda c: c.update(schema='wrong'), lambda c: c.pop('maps'),
                   lambda c: c['maps'][0].pop(),
                   lambda c: c['maps'][0].append(c['maps'][0][0]),
                   lambda c: c['maps'][0][0].__setitem__(1, 1),
                   lambda c: c['maps'][2].__setitem__(slice(0, 2),
                       [[c['maps'][2][0][0], c['maps'][2][1][1]],
                        [c['maps'][2][1][0], c['maps'][2][0][1]]]),
                   lambda c: c['maps'][2].reverse()]
        for change in changes[:-1]:
            bad = json.loads(json.dumps(cert))
            change(bad)
            with self.assertRaises(ValueError):
                support.verify(terms, bad)
        # Map order itself is immaterial; genuine bijections must replay.
        reordered = copy.deepcopy(cert)
        changes[-1](reordered)
        self.assertTrue(support.verify(terms, reordered))
        with self.assertRaises(ValueError):
            support.verify(terms[:-1], cert)

    def test_input_validation(self):
        for terms in (None, [0], [], [(0, 0, 0)] * 2, [(0, 0)], [(0, 0, True)], [(0, 0, 0.0)]):
            with self.assertRaises(ValueError):
                support.recognize(terms)


if __name__ == '__main__':
    unittest.main()
