import importlib.util
from itertools import combinations, permutations, product
import json
from math import prod
from pathlib import Path
import sys
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-23-central-cover-joint-frontier'
sys.path.insert(0, str(PACKAGE))
spec = importlib.util.spec_from_file_location('central_joint_frontier', PACKAGE/'frontier.py')
model = importlib.util.module_from_spec(spec)
spec.loader.exec_module(model)
import cube_cover


def explicit_koszul_rank(shape, scalars, ambient, power):
    a, b, c = shape
    tensor = [(i*b+j, j*c+k, k*a+i)
              for i in range(a) for j in range(b) for k in range(c)]
    tensor += [(a*b+r, b*c+r, c*a+r) for r in range(scalars)]
    inputs = list(combinations(range(ambient), power))
    outputs = list(combinations(range(ambient), power+1))
    row_index = {row: i for i, row in enumerate(outputs)}
    matrix = sp.zeros(len(outputs)*(c*a+scalars), len(inputs)*(b*c+scalars))
    for x, y, z in tensor:
        for column, wedge in enumerate(inputs):
            if x in wedge:
                continue
            new_wedge = tuple(sorted(wedge+(x,)))
            sign = (-1)**sum(v < x for v in wedge)
            matrix[row_index[new_wedge]*(c*a+scalars)+z,
                   column*(b*c+scalars)+y] += sign
    return matrix.rank()


class CentralCoverJointFrontierTests(unittest.TestCase):
    def test_complete_exact_family_replay(self):
        actual = json.loads(json.dumps(model.frontier()))
        saved = json.loads((ROOT/'results/central-cover-joint-frontier-2026-10-23/frontier.json').read_text())
        self.assertEqual(actual, saved)
        self.assertEqual(actual['sorted_shapes_checked'], 866)
        self.assertEqual(actual['dimension_compatible_family_members'], 41132)
        self.assertEqual([(row['shape'], row['scalar_outputs'])
                          for row in actual['improving_survivors_before_cube']],
                         [([9, 9, 11], r) for r in (11, 12, 13)])
        self.assertEqual(actual['improving_survivors'], [])
        self.assertEqual([row['strict_gap'] for row in actual['cube_exclusions']],
                         [76910, 106953, 137554])

    def test_cube_class_replay_and_corruption_controls(self):
        directory = ROOT/'results/central-cover-joint-frontier-2026-10-23'
        certificate = json.loads((directory/'cube-certificate.json').read_text())
        source = json.loads((ROOT/'results/sl2-finite-slices-2026-10-21/cover-certificate.json').read_text())
        report = cube_cover.verify(certificate, source['basis_degrees'])
        self.assertEqual(report['slice_upper_bound'], 1012332)
        self.assertEqual(report['one_leg_coordinate_multiplicity_checked'], 1728000)
        bad = json.loads(json.dumps(certificate))
        bad['rows'][0]['cutoffs'] = [-1, -1, -1]
        with self.assertRaisesRegex(ValueError, 'uncovered'):
            cube_cover.verify(bad, source['basis_degrees'])
        bad = json.loads(json.dumps(certificate))
        bad['rows'][1]['degree_counts'][0] += 1
        with self.assertRaisesRegex(ValueError, 'block counts'):
            cube_cover.verify(bad, source['basis_degrees'])

    def test_target_cube_formula_against_literal_direct_sum_expansion(self):
        for shape in ((1, 2, 3), (2, 3, 4), (9, 9, 11)):
            a, b, c = shape
            rotations = [(a, b, c), (b, c, a), (c, a, b)]
            for scalars in (0, 1, 3, 11):
                total = 0
                for chosen in product((False, True), repeat=3):
                    factors = [rotations[i] if keep else (1, 1, 1)
                               for i, keep in enumerate(chosen)]
                    x, y, z = [prod(factor[i] for factor in factors) for i in range(3)]
                    total += scalars**(3-sum(chosen))*min(x*y, y*z, z*x)
                self.assertEqual(cube_cover.joint_target_cube(shape, scalars), total)

    def test_joint_koszul_formula_against_literal_small_matrices(self):
        for shape in sorted(set(permutations((1, 2, 1)))):
            predicted = model.joint_ranks(shape, 1, 4)
            for power, rank in enumerate(predicted):
                self.assertEqual(explicit_koszul_rank(shape, 1, 4, power), rank)

    def test_profile_and_koszul_give_distinct_scalar_caps(self):
        source_profile = model.profile(model.DEGREES)
        self.assertTrue(all(row['minimum_dimension_margin'] >= 0
                            for row in model.profile_checks((9, 9, 11), 13, source_profile)))
        self.assertTrue(any(row['minimum_dimension_margin'] < 0
                            for row in model.profile_checks((9, 9, 11), 16, source_profile)))
        source = model.source_ranks(model.DEGREES)
        target13 = model.joint_ranks((9, 9, 11), 13)
        target14 = model.joint_ranks((9, 9, 11), 14)
        self.assertTrue(all(t <= s for t, s in zip(target13, source)))
        self.assertGreater(target14[57], source[57])

    def test_conditional_gate_rejects_an_unproved_stronger_number(self):
        with self.assertRaisesRegex(ValueError, 'not strict'):
            model.conditional_gate(13, model.Q(2))
        gate = model.conditional_gate(13, model.Q(2223, 1000))
        self.assertGreater(model.Q(gate['strict_margin_lower']), 0)
        self.assertFalse(gate['actual_improvement_established'])


if __name__ == '__main__':
    unittest.main()
