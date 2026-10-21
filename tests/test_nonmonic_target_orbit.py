"""Exact controls for the nonmonic balanced-flag construction question."""
from pathlib import Path
import random
import sys
import unittest
import sympy as sp

PACKAGE = Path(__file__).resolve().parents[1] / "research/ai/2026-10-20-new-source-constructions"
sys.path.insert(0, str(PACKAGE))
from torus_exact import ExactModel, Field, rank_field
import general_target_orbit as general
import symmetric_pairing
import eliminated_torus
from chamber_system import ChamberModel
import chamber_elimination


class TargetOrbitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = ExactModel()

    def test_unimodular_orbit_minor_and_relations(self):
        model = self.model
        self.assertEqual(model.incidence.shape, (20,24))
        self.assertEqual(model.minor.det(), -1)
        self.assertEqual(model.minor * model.inverse, sp.eye(18))
        self.assertEqual(len(model.relations), 2)
        for relation in model.relations:
            self.assertEqual(sum(value == 1 for value in relation), 4)
            self.assertEqual(sum(value == -1 for value in relation), 4)
            self.assertEqual(list(model.incidence.T * sp.Matrix(relation)), [0]*24)

    def test_uniform_selected_minor_and_lattice_relations(self):
        for m in range(2,7):
            report=general.structure(m)
            self.assertEqual(report['orbit_dimension'],m*m+m-2)
            self.assertIn(report['selected_minor_determinant'],(-1,1))
            self.assertEqual(report['relation_count'],(m-3)*(m-2)*(m+2)//6)
            self.assertTrue(report['all_relations_annihilate_incidence'])

    def test_uniform_reconstruction_over_both_fields(self):
        rng=random.Random(20261021)
        for m in range(2,9):
            for order in (3,4):
                field=Field(order)
                for _ in range(10):
                    scales={row:rng.randrange(1,order) for row in general.rows(m)}
                    values={(u,a,c):field.product([scales['x',a+c],scales['y',u,a],scales['z',u,c]])
                            for u,a,c in general.triples(m)}
                    recovered,actual=general.normalize(m,values,field)
                    self.assertEqual(actual,values)
                    self.assertEqual(recovered['x',0],1)
                    self.assertEqual(recovered['x',1],1)
                    for u in range(m):self.assertEqual(recovered['y',u,0],1)
                    unselected=set(general.triples(m))-set(general.selected_triples(m))
                    if unselected:
                        corrupt=values.copy();term=min(unselected)
                        corrupt[term]=field.mul(corrupt[term],2)
                        _,actual=general.normalize(m,corrupt,field)
                        self.assertNotEqual(actual,corrupt)

    def test_field_tables(self):
        for order in (3,4):
            field = Field(order)
            for a in range(order):
                self.assertEqual(field.add(a,field.neg(a)),0)
                if a:
                    self.assertEqual(field.mul(a,field.inv(a)),1)
                for b in range(order):
                    for c in range(order):
                        self.assertEqual(field.mul(a,field.add(b,c)),
                                         field.add(field.mul(a,b),field.mul(a,c)))

    def test_target_normalization_over_both_fields(self):
        rng = random.Random(20261020)
        model = self.model
        for order in (3,4):
            field = Field(order)
            for _ in range(100):
                scalars = [rng.randrange(1,order) for _ in range(24)]
                values = [field.product(scalars[j] for j in (p,4+y,14+z))
                          for p,y,z in model.targets]
                recovered = model.normalize_target(values,order)
                self.assertEqual(values,[field.product(recovered[j] for j in (p,4+y,14+z))
                                         for p,y,z in model.targets])
                corrupt = values[:]
                corrupt[13] = field.mul(corrupt[13],2)
                with self.assertRaises(ValueError):
                    model.normalize_target(corrupt,order)

    def test_sparse_equations_against_polynomial_products(self):
        rng = random.Random(912)
        model = self.model
        for order in (3,4):
            field = Field(order)
            for _ in range(6):
                variables = [rng.randrange(order) for _ in model.variables]
                values = [0]*len(model.system.keys)
                for index,value in model.system.constant_values.items():
                    values[index] = int(value)
                for index,value in zip(model.variables,variables):
                    values[index] = value
                matrices = [[[0]*width for _ in range(rows)] for rows,width in ((4,4),(10,10),(10,13))]
                for (leg,row,drop),value in zip(model.system.keys,values):
                    degree = model.system.degrees[leg][row]
                    column = degree-drop if leg<2 else 12-degree+drop
                    matrices[leg][row][column] = value
                expected = []
                for p,y,z in model.all_triples:
                    expected.append(field.sum(field.mul(field.mul(matrices[0][p][i],matrices[1][y][j]),
                                                        matrices[2][z][i+j])
                                              for i in range(4) for j in range(10)))
                actual,_ = model.coefficient_values(variables,field)
                self.assertEqual(actual,expected)

    def test_zero_point_is_not_a_construction(self):
        for order in (3,4):
            check = self.model.replay([0]*len(self.model.variables),order)
            self.assertEqual(check["zero_target_coefficients"],20)
            self.assertFalse(check["nonsingular_hensel_premise"])

    def test_symmetric_pairing_reconstructs_original_coefficients(self):
        rng = random.Random(73129)
        model = self.model
        retained = symmetric_pairing.coefficient_triples(model)
        self.assertEqual(len(retained), 67)
        self.assertEqual(sum(wanted for _, wanted in retained), 10)
        for order in (3, 4):
            field = Field(order)
            for _ in range(8):
                monic = lambda degree: [rng.randrange(order) for _ in range(degree)] + [1]
                g = [monic(3), monic(2), [0, 1], [1]]
                p = [monic(degree) for degree in model.system.degrees[1]]
                h = monic(3)
                values = symmetric_pairing.coefficient_vector(model, g, p, h, order)
                actual, _ = model.coefficient_values(values, field)
                expected = []
                for x, y, z in model.all_triples:
                    polynomial = [1]
                    for factor in (h, g[x], p[y], p[z]):
                        polynomial = symmetric_pairing.convolution(
                            polynomial, factor, field.add, field.mul, 0)
                    expected.append(polynomial[12] if len(polynomial) > 12 else 0)
                self.assertEqual(actual, expected)
                lookup = dict(zip(model.all_triples, actual))
                for (x, y, z), value in lookup.items():
                    self.assertEqual(value, lookup[x, z, y])
                replay = model.replay(values, order)
                self.assertEqual(replay['toric_errors'], [0, 0])

    def test_eliminated_torus_matches_every_original_equation(self):
        rng = random.Random(99138)
        model = self.model
        for order in (3, 4):
            field = Field(order)
            for _ in range(8):
                free = [rng.randrange(order) for _ in model.system.free]
                scales = [rng.randrange(1, order) for _ in model.columns]
                values, residuals = eliminated_torus.eliminate(
                    model, free, scales, eliminated_torus.ConcreteOps(order))
                actual, _ = model.coefficient_values([values[j] for j in model.variables], field)
                lookup = dict(zip(model.columns, scales))
                errors = []
                for value, (p,y,z), (_,wanted) in zip(actual, model.all_triples, model.equations):
                    target = field.product(lookup.get(j, 1) for j in (p,4+y,14+z)) if wanted else 0
                    errors.append(field.add(value, field.neg(target)))
                offset = 0
                remaining = []
                for level in model.system.levels:
                    for row in level['rows']:
                        self.assertEqual(errors[offset+row], 0)
                    remaining.extend(errors[offset+row] for row in level['remaining_rows'])
                    offset += len(level['constraints'])
                self.assertEqual(len(remaining), 53)
                self.assertEqual(residuals, remaining)
                self.assertEqual([values[j] for j in model.system.free], free)

    def test_general_chamber_reproduces_the_predecessor(self):
        generalized = ChamberModel([0,201,403,607],100)
        self.assertEqual(generalized.system.degrees,self.model.system.degrees)
        self.assertEqual(generalized.system.keys,self.model.system.keys)
        self.assertEqual(generalized.equations,self.model.equations)
        self.assertEqual(generalized.all_triples,self.model.all_triples)
        with self.assertRaises(ValueError):
            ChamberModel([7,14,21,0],1)

    def test_new_chamber_checks_all_nonpositive_coefficients(self):
        model = ChamberModel([0,301,628,844],100)
        self.assertEqual(len(model.equations),115)
        self.assertEqual(len(model.zero_indices),95)
        rng = random.Random(11473)
        for order in (3,4):
            field = Field(order)
            for _ in range(4):
                variables = [rng.randrange(order) for _ in model.variables]
                full = [0]*len(model.system.keys)
                for index,value in model.system.constant_values.items():
                    full[index] = int(value)
                for index,value in zip(model.variables,variables):
                    full[index] = value
                matrices = [[[0]*width for _ in range(rows)] for rows,width in ((4,4),(10,10),(10,13))]
                for (leg,row,drop),value in zip(model.system.keys,full):
                    degree = model.system.degrees[leg][row]
                    column = degree-drop if leg<2 else 12-degree+drop
                    matrices[leg][row][column] = value
                actual,_ = model.coefficient_values(variables,field)
                expected = dict(zip(model.all_triples,actual))
                expected.update({triple:0 for triple in model.forced_zero_entries})
                checked = 0
                for p in range(4):
                    for y in range(10):
                        for z in range(10):
                            weight = model.weights[0][p]+model.weights[1][y]+model.weights[2][z]
                            if weight>0:
                                continue
                            coefficient = field.sum(field.product((matrices[0][p][i],matrices[1][y][j],matrices[2][z][i+j]))
                                                    for i in range(4) for j in range(10))
                            self.assertEqual(coefficient,expected[p,y,z])
                            checked += 1
                self.assertEqual(checked,model.structure()['total_nonpositive_entries'])

    def test_rank_replay_rejects_a_dropped_pivot(self):
        for order in (3,4):
            field=Field(order)
            self.assertEqual(rank_field([[1,0],[0,1]],field)[0],2)
            self.assertEqual(rank_field([[1,1],[1,1]],field)[0],1)

    def test_new_chamber_unit_elimination_reconstructs_all_equations(self):
        model = chamber_elimination.build_model()
        self.assertEqual(len(model.system.free), 60)
        self.assertEqual(sum(len(level['pivots']) for level in model.system.levels), 65)
        rng = random.Random(763120)
        for order in (3, 4):
            field = Field(order)
            for _ in range(6):
                free = [rng.randrange(order) for _ in model.system.free]
                scales = [rng.randrange(1, order) for _ in model.columns]
                values, residuals = eliminated_torus.eliminate(
                    model, free, scales, eliminated_torus.ConcreteOps(order))
                coefficients, _ = model.coefficient_values([values[j] for j in model.variables], field)
                lookup = dict(zip(model.columns, scales))
                errors = []
                for value, (p,y,z), (_,wanted) in zip(coefficients, model.all_triples, model.equations):
                    target = field.product(lookup.get(j, 1) for j in (p,4+y,14+z)) if wanted else 0
                    errors.append(field.add(value, field.neg(target)))
                offset, remaining = 0, []
                for level in model.system.levels:
                    self.assertIn(level['minor_determinant'], (-1, 1))
                    for row in level['rows']:
                        self.assertEqual(errors[offset+row], 0)
                    remaining.extend(errors[offset+row] for row in level['remaining_rows'])
                    offset += len(level['constraints'])
                self.assertEqual(len(remaining), 50)
                self.assertEqual(residuals, remaining)
                self.assertEqual([values[j] for j in model.system.free], free)


if __name__ == "__main__":
    unittest.main()
