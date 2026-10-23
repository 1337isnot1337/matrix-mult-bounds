"""Independent controls for the exact external-seed flip component."""
import copy
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest


PACKAGE = (Path(__file__).resolve().parents[1]
           / "research/ai/2026-10-23-flip-escape")
SPEC = importlib.util.spec_from_file_location(
    "external_flip_component", PACKAGE / "verify_component.py")
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)


class FlipComponentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.factors = V.load_seed()
        cls.certificate = json.loads((PACKAGE / "component_certificate.json").read_text())

    def test_complete_witness_and_regeneration(self):
        result = V.verify_certificate(self.factors, self.certificate)
        self.assertEqual(result["cross_class_unit_minors"], 3306)
        self.assertEqual(result["class_sizes"], {"1": 40, "2": 18})
        self.assertEqual(result["individual_trace_values"], {"1": 52, "2": 24})
        self.assertEqual(result["sum_trace"], 100)
        self.assertFalse(result["improves_omega"])
        self.assertEqual(V.build_certificate(self.factors), self.certificate)

    def test_rejects_wrong_minor_and_incomplete_coverage(self):
        changed = copy.deepcopy(self.certificate)
        changed["unit_minors"][0][-1] *= -1
        with self.assertRaisesRegex(ValueError, "determinant replay"):
            V.verify_certificate(self.factors, changed)
        changed = copy.deepcopy(self.certificate)
        changed["unit_minors"].pop()
        with self.assertRaisesRegex(ValueError, "Missing"):
            V.verify_certificate(self.factors, changed)

    def test_rational_refactorization_preserves_tensor_and_pairing(self):
        # G=[[2,3],[1,4]], det=5; use literal inverse transpose,
        # independently of any refactorization helper in the verifier.
        groups = [group for group in self.certificate["groups"] if len(group) == 2]
        for group in groups:
            u = [[sign * x for x in self.factors["u"][i]] for i, sign in group]
            v = [self.factors["v"][i] for i, _ in group]
            index, sign = group[0]
            w = [sign * x for x in self.factors["w"][index]]
            new_u = [[2*x+y for x, y in zip(*u)],
                     [3*x+4*y for x, y in zip(*u)]]
            new_v = [[Fraction(4*x-3*y, 5) for x, y in zip(*v)],
                     [Fraction(-x+2*y, 5) for x, y in zip(*v)]]
            for a in range(20):
                for b in range(25):
                    self.assertEqual(sum(new_u[k][a]*new_v[k][b] for k in range(2)),
                                     sum(u[k][a]*v[k][b] for k in range(2)))
            c = V.trace_product(u[0], v[0], w)
            self.assertEqual([[V.trace_product(x, y, w) for y in new_v]
                              for x in new_u], [[c, 0], [0, c]])


if __name__ == "__main__":
    unittest.main()
