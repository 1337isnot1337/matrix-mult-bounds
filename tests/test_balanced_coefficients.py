"""Exact equivalence controls for the restricted monic coefficient system."""
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-20-balanced-coefficients'
sys.path.insert(0, str(PACKAGE))
from coefficient_system import System
from finite_field import equations, replay, rank_mod
import finite_field
import field_four

spec = importlib.util.spec_from_file_location('independent_exact_flags',
    ROOT/'research/ai/2026-10-20-singular-flags/exact_flags.py')
flags = importlib.util.module_from_spec(spec); spec.loader.exec_module(flags)


class BalancedCoefficientTests(unittest.TestCase):
    def test_saved_system_counts_and_unimodular_elimination(self):
        system = System()
        saved = json.loads((ROOT/'results/balanced-coefficients-2026-10-20/elimination.json').read_text())
        self.assertEqual(system.summary(), saved)
        self.assertEqual((saved['initial_complex_variables'], saved['retained_complex_parameters'],
                          saved['polynomial_conditions']), (125, 57, 53))
        self.assertEqual(sum(len(level['pivots']) for level in system.levels), 68)
        for level in system.levels:
            matrix = level['matrix'].extract(level['rows'], level['pivots'])
            self.assertEqual(level['inverse']*matrix, sp.eye(len(level['pivots'])))
            self.assertTrue(all(value.q == 1 for value in level['inverse']))

    def test_exact_reconstruction_matches_every_direct_coefficient(self):
        for case in range(3):
            system = System()
            free = [Fraction(((i+2)*7+case)%5-2, 1+case) for i in range(len(system.free))]
            residuals, values = system.evaluate_exact(free)
            tensor = flags.tensor(*system.matrices(values))
            selected = []
            for level in system.levels:
                for row, (p,y,z,wanted) in enumerate(level['constraints']):
                    error = tensor[(p*10+y)*10+z]-wanted
                    if row in level['rows']: self.assertEqual(error, 0)
                    else: selected.append(Fraction(error))
            self.assertEqual(selected, residuals)

    def test_bidirectional_recovery_on_exact_monic_maps(self):
        system = System()
        original = [Fraction((11*i)%7-3) for i in range(len(system.keys))]
        for index,value in system.constant_values.items(): original[index] = value
        tensor = flags.tensor(*system.matrices(original))
        # Feed the exact coefficients of independently multiplied monic maps.
        # This controls both directions of the elimination, not a T4 witness.
        for level in system.levels:
            level['constraints'] = [(p,y,z,Fraction(tensor[(p*10+y)*10+z]))
                                    for p,y,z,_ in level['constraints']]
        residuals, recovered = system.evaluate_exact([original[i] for i in system.free])
        self.assertTrue(all(value == 0 for value in residuals))
        self.assertEqual(recovered, original)

    def test_full_equations_and_formal_jacobian_over_small_fields(self):
        system = System()
        variables, eqs = equations(system)
        self.assertEqual((len(variables), len(eqs)), (125, 121))
        for prime in [2, 3, 5]:
            values = [(17*j+3)%prime for j in range(125)]
            report = replay(system, values, prime)
            coeffs = [0]*len(system.keys)
            for index,value in system.constant_values.items(): coeffs[index] = int(value)
            for index,value in zip(variables, values): coeffs[index] = value
            tensor = flags.tensor(*system.matrices(coeffs))
            wrong = sum(bool(int(tensor[(p*10+y)*10+z]-wanted)%prime)
                        for level in system.levels for p,y,z,wanted in level['constraints'])
            self.assertEqual(report['nonzero_equations'], wrong)
            self.assertFalse(report['nonsingular_hensel_premise'])
        self.assertEqual(rank_mod([[1, 1, 0], [1, 0, 1]], 2)[0], 2)
        self.assertEqual(rank_mod([[1, 1], [1, 1]], 3)[0], 1)

    def test_extension_field_arithmetic_and_jacobian_controls(self):
        mul = field_four.multiply
        for a in range(4):
            self.assertEqual(mul(a, 1), a)
            if a: self.assertEqual(mul(mul(a,a),a), 1)
            for b in range(4):
                self.assertEqual(mul(a,b), mul(b,a))
                for c in range(4):
                    self.assertEqual(mul(a,mul(b,c)), mul(mul(a,b),c))
                    self.assertEqual(mul(a,b^c), mul(a,b)^mul(a,c))
        system = System()
        for value in [0, 1]:
            coefficients = [value]*125
            binary = replay(system, coefficients, 2)
            extension = field_four.replay(system, coefficients)
            for key in ['nonzero_equations', 'jacobian_rank', 'nonsingular_hensel_premise']:
                self.assertEqual(binary[key], extension[key])

    def test_formal_jacobian_by_exact_multiaffine_differences(self):
        system = System(); _, eqs = equations(system)
        self.assertTrue(all(len(set(term)) == len(term) for terms,_ in eqs for term in terms))
        def evaluate(values, prime):
            result = []
            for terms,wanted in eqs:
                value = -wanted
                for term in terms:
                    product = 1
                    for index in term: product *= values[index]
                    value += product
                result.append(value%prime)
            return result
        for prime in [2, 3]:
            values = [(7*i+3)%prime for i in range(125)]
            before = evaluate(values, prime); expected = [[0]*125 for _ in eqs]
            for column in range(125):
                changed = values.copy(); changed[column] += 1
                for row,value in enumerate(evaluate(changed, prime)):
                    expected[row][column] = (value-before[row])%prime
            captured = []
            def capture(matrix, p):
                captured.append(matrix)
                return rank_mod(matrix, p)
            with patch.object(finite_field, 'rank_mod', side_effect=capture):
                replay(system, values, prime)
            self.assertEqual(captured[0], expected)


if __name__ == '__main__': unittest.main()
