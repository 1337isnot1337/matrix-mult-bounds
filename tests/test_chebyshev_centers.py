"""Independent small enumeration and exact normalized degeneration controls."""
import itertools
import json
from pathlib import Path
import sys
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research/ai/2026-10-20-koszul"))
import chebyshev_centers


def brute_centers(m):
    """Fix each full order first; use a distinct-coordinate matching test."""
    result = {}
    for tail in itertools.permutations(range(1, m)):
        order = (0,) + tail
        position = {degree: i for i, degree in enumerate(order)}

        def first_degree(y, z):
            degrees = {abs(y - z), y + z} & position.keys()
            return min(degrees, key=position.get) if degrees else None

        for c in range(m):
            for d in range(max(0, c - m + 1), c + m):
                if c == d:
                    continue
                choices = [
                    [z for z in range(2 * m - 1)
                     if first_degree(c, z) == order[b]
                     and first_degree(d, z) == order[b + 1]]
                    for b in range(m - 1)]
                choices[0] = [z for z in choices[0] if z == c]

                def matching(column, used):
                    if column == m - 1:
                        return True
                    return any(matching(column + 1, used | {z})
                               for z in choices[column] if z not in used)

                if matching(0, set()):
                    result.setdefault(order, set()).add(c)
                    break
    return result


def coefficients(i, j):
    if i == 0 or j == 0:
        return {i + j: sp.Integer(1)}
    return {i + j: sp.Rational(1, 2), abs(i - j): sp.Rational(1, 2)}


class ChebyshevTests(unittest.TestCase):
    def test_independent_two_row_enumeration(self):
        for m in range(2, 7):
            result = chebyshev_centers.centers(m)
            actual = {tuple(item["permutation"]): set(item["centers"])
                      for item in result["orderings"]}
            self.assertEqual(actual, brute_centers(m), m)

    def test_polynomial_coefficients(self):
        t = sp.Symbol("t")
        for i in range(8):
            for j in range(8):
                expansion = sum(value * sp.chebyshevt(k, t)
                                for k, value in coefficients(i, j).items())
                self.assertEqual(sp.expand(sp.chebyshevt(i, t) *
                                          sp.chebyshevt(j, t) - expansion), 0)

    def test_exact_small_controls(self):
        for m in (2, 3):
            record = json.loads((ROOT / "results/koszul-2026-10-20" /
                                 f"chebyshev_m{m}_certificate.json").read_text())
            b = record["B"]
            expected, live_z = set(), set()
            start = 0
            for u, sign in zip(record["order"], record["signs"]):
                center = start + u - 1 if sign == 1 else start
                output = {center + sign * c for c in range(m + 1 - u)}
                self.assertFalse(live_z & output)
                live_z.update(output)
                expected.update((a + c, center - sign * a, center + sign * c)
                                for a in range(u) for c in range(m + 1 - u))
                start += u
            self.assertEqual(start, b)
            self.assertEqual(set(record["order"]), set(range(1, m + 1)))
            self.assertEqual(expected, {tuple(term) for term, _ in record["wanted"]})
            weights = record["weights"]
            scales = list(map(sp.Rational, record["coefficient_scaling_exponents"]))
            actual, extras = {}, 0
            for i in range(m):
                for j in range(b):
                    for z, value in coefficients(i, j).items():
                        if z not in live_z:
                            continue
                        ids = (i, m + j, m + b + z)
                        exponent = sum(weights[index] for index in ids)
                        self.assertGreaterEqual(exponent, 0)
                        if exponent == 0:
                            actual[i, j, z] = value * sp.Integer(2) ** sum(
                                scales[index] for index in ids)
                        else:
                            extras += 1
            self.assertEqual(actual, dict.fromkeys(expected, sp.Integer(1)))
            self.assertEqual(extras, record["extras"])

    def test_archived_completed_range(self):
        report = json.loads((ROOT / "results/koszul-2026-10-20" /
                             "chebyshev_centers.json").read_text())
        self.assertEqual([r["m"] for r in report["results"]], list(range(4, 39)))
        for result in report["results"]:
            self.assertEqual(result["status"], "complete")
            self.assertEqual(chebyshev_centers.summary(result)["multiple_center_examples"], [])


if __name__ == "__main__":
    unittest.main()
