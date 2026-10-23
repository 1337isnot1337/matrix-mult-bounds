"""Exact identity and mutation controls for the split-derived border seed."""
import copy
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest


PACKAGE = (Path(__file__).resolve().parents[1]
           / "research/ai/2026-10-23-flip-escape")
SPEC = importlib.util.spec_from_file_location("split_border_seed", PACKAGE / "verify_split.py")
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)


def evaluated_tensor(terms, parameter):
    """A scalar-evaluation control independent of formal Laurent collection."""
    result = [Fraction(0)] * 10000
    for term in terms:
        evaluated = []
        for entries, width in zip(term, (20, 25, 20)):
            vector = [Fraction(0)] * width
            for coordinate, coefficient, exponent in entries:
                vector[coordinate] = Fraction(coefficient) * parameter ** exponent
            evaluated.append(vector)
        u, v, w = evaluated
        for a, x in enumerate(u):
            if not x:
                continue
            for b, y in enumerate(v):
                if not y:
                    continue
                for c, z in enumerate(w):
                    result[(a * 25 + b) * 20 + c] += x * y * z
    return result


class SplitBorderSeedTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = json.loads((PACKAGE / "split_certificate.json").read_text())

    def test_complete_exact_replay_and_regeneration(self):
        result = V.verify(self.certificate)
        self.assertEqual(result["negative_coefficients"], 0)
        self.assertEqual(result["constant_positions_checked"], 10000)
        self.assertEqual(result["positive_nonzero_coefficients"], 51)
        self.assertEqual(result["distinct_first_leg_directions"], 72)
        self.assertFalse(result["Q64_maps_constructed"])
        self.assertFalse(result["rank_record_claimed"])
        self.assertFalse(result["improves_omega"])
        self.assertEqual(V.build_certificate(), self.certificate)

    def test_independent_finite_parameter_split_identity(self):
        target = [Fraction(0)] * 10000
        for i in range(4):
            for j in range(5):
                for k in range(5):
                    target[((5*i+j)*25+(5*j+k))*20+(4*k+i)] = 1
        for parameter in (Fraction(2), Fraction(-3, 2)):
            surviving = evaluated_tensor(self.certificate["surviving_factors"], parameter)
            discarded = evaluated_tensor(self.certificate["discarded_factors"], parameter)
            self.assertEqual([x+y for x, y in zip(surviving, discarded)], target)
            self.assertNotEqual(surviving, target)

    def test_rejects_changed_factor_and_missing_term(self):
        changed = copy.deepcopy(self.certificate)
        changed["surviving_factors"][0][0][0][1] = str(
            -Fraction(changed["surviving_factors"][0][0][0][1]))
        with self.assertRaises(ValueError):
            V.verify_laurent_identity(changed)
        changed = copy.deepcopy(self.certificate)
        changed["surviving_factors"].pop()
        with self.assertRaisesRegex(ValueError, "number of rank-one terms"):
            V.verify_laurent_identity(changed)

    def test_rejects_noncontracting_discarded_factor(self):
        changed = copy.deepcopy(self.certificate)
        changed["discarded_factors"][0][0][0][2] = -1
        with self.assertRaisesRegex(ValueError, "nonpositive valuation"):
            V.verify_laurent_identity(changed)

    def test_individual_nilpotence_does_not_replace_common_flag(self):
        # Two individually nilpotent rank-one cyclic representations can
        # generate a nonzero mixed cycle. The common-flag verifier rejects it.
        def one_entry(height, width, i, j):
            return [[Fraction(a == i and b == j) for b in range(width)]
                    for a in range(height)]
        a = one_entry(4, 5, 0, 0)
        b = one_entry(5, 5, 0, 0)
        c0 = one_entry(5, 4, 1, 1)
        c1 = one_entry(5, 4, 0, 0)
        b1 = one_entry(5, 5, 1, 1)
        first = [a, b, c0]
        second = [a, b1, c1]
        self.assertEqual(V.image_flags([first])[-1], [[[] for _ in range(4)],
                                                      [[] for _ in range(5)],
                                                      [[] for _ in range(5)]])
        V.image_flags([second])
        with self.assertRaisesRegex(ValueError, "not jointly nilpotent"):
            V.image_flags([first, second])


if __name__ == "__main__":
    unittest.main()
