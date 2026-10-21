"""Complete polynomial replay and independent evaluated source contractions."""
from collections import defaultdict
import copy
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-21-mixed-first-jets'
RESULTS = ROOT / 'results/mixed-first-jets-2026-10-21'


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


verify = load('mixed_jet_verify', PACKAGE / 'verify.py')
construct = load('mixed_jet_construct', PACKAGE / 'construct.py')
cyclic = load('mixed_jet_original_source', ROOT / 'research/ai/2026-10-20-cyclic-mixed-map/verify.py')


def evaluate(certificate, parameters):
    p0 = verify.pad_top(certificate['leading_rows'], 18)
    q0 = verify.pad_top(certificate['leading_rows'], 10)
    p1 = [{} for _ in range(4)]+verify.rows(certificate['first_constant_B_new'])
    q1 = [{} for _ in range(4)]+verify.rows(certificate['first_constant_C_new'])
    p2, q2 = [{} for _ in range(18)], [{} for _ in range(10)]
    y, z = defaultdict(Fraction), defaultdict(Fraction)

    def add_rows(target, source, coefficient):
        for i, row in enumerate(source):
            for j, value in row.items():
                target[i][j] = target[i].get(j, 0)+coefficient*value

    for i, a in enumerate(parameters):
        add_rows(p1, verify.pad_top(certificate['first_top_directions'][i][:4], 18), a)
        add_rows(q1, verify.pad_top(certificate['first_top_directions'][i][4:], 10), a)
        add_rows(p2, [{} for _ in range(4)]+verify.rows(certificate['second_linear_B_new'][i]), a)
        add_rows(q2, [{} for _ in range(4)]+verify.rows(certificate['second_linear_C_new'][i]), a)
        for r, c, n, d in certificate['first_row_corrections'][i]:
            y[r, c] += a*Fraction(n, d)
    for record in certificate['second_quadratic']:
        i, j = record['monomial']
        a = parameters[i]*parameters[j]
        add_rows(p2, verify.pad_top(record['B_top'], 18), a)
        add_rows(q2, verify.pad_top(record['C_top'], 10), a)
        for r, c, n, d in record['first_row_correction']:
            z[r, c] += a*Fraction(n, d)
    return (p0, p1, p2), (q0, q1, q2), y, z


def original_contract(left, right):
    bcols, ccols = defaultdict(list), defaultdict(list)
    for i, row in enumerate(left):
        for j, value in row.items():
            if value:
                bcols[j].append((i, value))
    for i, row in enumerate(right):
        for j, value in row.items():
            if value:
                ccols[j].append((i, value))
    tensor = defaultdict(Fraction)
    for a, b, c in cyclic.source_terms(4):
        i, k, s = a//28, (a//4) % 7, a % 4
        j, p, z = b//28, (b//7) % 4, b % 7
        h, q, r = c//16, (c//4) % 4, c % 4
        first = (4*i+s)*7+6-k
        second = (4*p+j)*7+6-z
        third = (4*r+q)*7+6-h
        for x, bv in bcols[second]:
            for y, cv in ccols[third]:
                tensor[first, x, y] += bv*cv
    return {key: value for key, value in tensor.items() if value}


def corrected_coefficients(ps, qs, y, z):
    coefficients = [defaultdict(Fraction) for _ in range(7)]
    for i, p in enumerate(ps):
        for j, q in enumerate(qs):
            for key, value in original_contract(p, q).items():
                coefficients[i+j][key] += value
    result = []
    for order in range(7):
        row = defaultdict(Fraction, coefficients[order])
        for shift, correction in ((1, y), (2, z)):
            if order < shift:
                continue
            for (i, j), value in correction.items():
                if value:
                    for (a, b, c), coefficient in coefficients[order-shift].items():
                        if a == j:
                            row[i, b, c] -= value*coefficient
        result.append({key: value for key, value in row.items() if key[0] in verify.KERNEL and value})
    return result


class MixedFirstJetTests(unittest.TestCase):
    def test_reconstruct_family_from_seed(self):
        seed = json.loads((PACKAGE / 'seed.json').read_text())
        self.assertEqual(construct.construct(seed), json.loads((RESULTS / 'twojet-family.json').read_text()))

    def test_complete_polynomial_coefficient_replay(self):
        certificate = json.loads((RESULTS / 'twojet-family.json').read_text())
        self.assertEqual(verify.verify(certificate), json.loads((RESULTS / 'twojet-report.json').read_text()))

    def test_independent_generic_source_contraction(self):
        certificate = json.loads((RESULTS / 'twojet-family.json').read_text())
        parameters = (1, -1, 2, 1, 0, -2, 1, 1, -1, 2, 1, 0, 1, -1, 1, 2)
        ps, qs, y, z = evaluate(certificate, parameters)
        self.assertEqual(corrected_coefficients(ps, qs, y, z)[:3], [{}, {}, {}])

    def test_changed_second_derivative_is_rejected(self):
        certificate = copy.deepcopy(json.loads((RESULTS / 'twojet-family.json').read_text()))
        entry = next(row[0] for matrix in certificate['second_linear_B_new'] for row in matrix if row)
        entry[1] += 1
        with self.assertRaisesRegex(ArithmeticError, 'second linear parameter'):
            verify.verify(certificate)

    def test_second_order_acceptance_does_not_assert_higher_order_cancellation(self):
        certificate = json.loads((RESULTS / 'twojet-family.json').read_text())
        ps, qs, y, z = evaluate(certificate, (1,)+(0,)*15)
        residues = corrected_coefficients(ps, qs, y, z)
        self.assertEqual(residues[:3], [{}, {}, {}])
        matrix = sp.MutableSparseMatrix(112, 180,
                                        {(a, 10*b+c): value for (a, b, c), value in residues[3].items()})
        self.assertEqual(len(matrix.to_DM().rref()[1]), 8)


if __name__ == '__main__':
    unittest.main()
