"""Exact rank certificates and independent source/jet coefficient controls."""
from collections import defaultdict
import importlib.util
import json
from pathlib import Path
import random
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


extension = load('quantum_extensions', ROOT / 'research/ai/2026-10-21-quantum-extension-spaces/extensions.py')
cyclic = load('extension_canonical_source', ROOT / 'research/ai/2026-10-20-cyclic-mixed-map/verify.py')


class QuantumExtensionTests(unittest.TestCase):
    def test_exact_report_replay(self):
        saved = json.loads((ROOT / 'results/quantum-extension-spaces-2026-10-21/certificates.json').read_text())
        self.assertEqual(json.loads(json.dumps(extension.report())), saved)

    def test_bilinear_tensor_against_original_cyclic_source(self):
        actual = defaultdict(int)
        left, right = defaultdict(list), defaultdict(list)
        for j, row in enumerate(extension.EB):
            for k, value in row.items():
                left[k].append((j, value))
        for j, row in enumerate(extension.EC):
            for k, value in row.items():
                right[k].append((j, value))
        positions = {a: i for i, a in enumerate(extension.OUTSIDE)}
        for a, b, c in cyclic.source_terms(4):
            i, k, s = a//28, (a//4) % 7, a % 4
            j, p, z = b//28, (b//7) % 4, b % 7
            h, q, r = c//16, (c//4) % 4, c % 4
            u = (4*i+s)*7+6-k
            v = (4*p+j)*7+6-z
            w = (4*r+q)*7+6-h
            if u in positions:
                for x, a_value in left[v]:
                    for y, b_value in right[w]:
                        actual[positions[u], 20*x+y] += a_value*b_value
        expected = extension.matrices()[3]
        independent = sp.MutableSparseMatrix(100, 400, dict(actual))
        self.assertEqual(independent, expected)

    def test_coupled_system_against_direct_first_coefficient(self):
        _, _, _, _, top, annihilator = extension.matrices()
        rng = random.Random(202610751)
        rows = [{j: rng.choice((-1, 1)) for j in rng.sample(range(112), 28)}
                for _ in range(8)]
        variables = sp.Matrix([row.get(j, 0) for row in rows for j in range(112)])
        derivative = (extension.contract(rows[:4], extension.G, extension.OUTSIDE)
                      + extension.contract(extension.G, rows[4:], extension.OUTSIDE))
        quotient = derivative*annihilator.T
        self.assertEqual(top*variables, sp.Matrix(list(quotient)))

    def test_kernel_directions_preserve_first_partial_saturation(self):
        _, _, _, _, top, _ = extension.matrices()
        reduced, pivots = top.to_DM().rref()
        reduced = reduced.to_Matrix()
        free = [j for j in range(896) if j not in pivots]
        for chosen in (free[0], free[len(free)//2], free[-1]):
            vector = [sp.Integer(0)]*896
            vector[chosen] = 1
            for i, p in enumerate(pivots):
                vector[p] = -reduced[i, chosen]
            rows = [{j: vector[112*i+j] for j in range(112) if vector[112*i+j]}
                    for i in range(8)]
            # Two new rows on each side exercise both boundary and inner bases.
            p1 = rows[:4]+[extension.EB[0], extension.EB[-1]]
            q1 = rows[4:]+[extension.EC[3], extension.EC[-2]]
            leading = extension.G+[{}, {}]
            s0 = extension.contract(leading, leading, range(112))
            s1_kernel = (extension.contract(p1, leading, extension.OUTSIDE)
                         + extension.contract(leading, q1, extension.OUTSIDE))
            self.assertEqual(extension.rational_rank(s0.col_join(s1_kernel)), 12)


if __name__ == '__main__':
    unittest.main()
