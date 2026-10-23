"""Exact finite controls for the written geometric argument, not its formalization."""
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import unittest
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-rank-three-hankel"
RESULT = ROOT / "results/rank-three-hankel-2026-10-23/controls.json"
SPEC = importlib.util.spec_from_file_location("test_rank_three_hankel", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


class RankThreeHankelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.saved = json.loads(RESULT.read_text())

    def test_complete_ferrers_inventory_and_sharp_budgets(self):
        ways = [1]+[0]*24
        for part in range(1, 25):
            for total in range(part, 25):
                ways[total] += ways[total-part]
        count = 0
        for total in range(25):
            diagrams = list(v.partitions(total))
            self.assertEqual(len(diagrams), ways[total])
            self.assertEqual(len(set(diagrams)), len(diagrams))
            for p in diagrams:
                self.assertEqual(sum(p), total)
                self.assertEqual(tuple(sorted(p, reverse=True)), p)
                self.assertTrue(all(n > 0 for n in p))
            count += len(diagrams)
        self.assertEqual(count, 7338)
        self.assertEqual(self.saved["ferrers"], v.ferrers_controls())
        self.assertEqual(self.saved["ferrers"]["rank_diagram_cases"], 22014)
        for row, one, two in zip(self.saved["ferrers"]["budgets"], [4, 9, 16], [6, 12, 20]):
            self.assertEqual(row["minimum_one_box"]["dimension"], one)
            self.assertEqual(row["minimum_two_boxes"]["dimension"], two)

    def test_projection_jacobians_and_independent_tangent_annihilators(self):
        for row in self.saved["projection_controls"]:
            lengths = row["diagram"]
            m, n, k = len(lengths), max(lengths), row["parameter_rank"]
            u = sp.symbols("u:"+str(m*k))
            w = sp.symbols("v:"+str(n*k))
            U = sp.Matrix(m, k, u)
            V = sp.Matrix(n, k, w)
            outputs = [(U*V.T)[i, j] for i, width in enumerate(lengths) for j in range(width)]
            values = dict(zip(u+w, sum(row["U"], [])+sum(row["V"], [])))
            J = sp.Matrix(outputs).jacobian(u+w).subs(values)
            self.assertEqual(J.rank(), row["jacobian_rank"])
            A = sp.Matrix(row["U"]).T.nullspace()
            B = sp.Matrix(row["V"]).T.nullspace()
            tensors = [a*b.T for a in A for b in B]
            outside = [(i, j) for i in range(m) for j in range(n) if j >= lengths[i]]
            equations = sp.Matrix([[T[i, j] for T in tensors] for i, j in outside])
            kernel_dimension = len(tensors)-(equations.rank() if outside else 0)
            self.assertEqual(kernel_dimension, row["image_codimension"])
        self.assertEqual([r["image_codimension"] for r in self.saved["projection_controls"]], [1, 2, 1, 2])

    def test_all_697_coordinate_sections_and_nonreduced_endpoint_schemes(self):
        rows = self.saved["coordinate_sections"]
        expected = {omitted for c in range(4) for omitted in itertools.combinations(range(16), c)}
        self.assertEqual({tuple(row["omitted_coordinates"]) for row in rows}, expected)
        self.assertEqual(len(rows), 697)
        families = {}
        for s in range(8):
            support = [j for j in [s-1, s+9] if 0 <= j <= 15]
            h = [int(j in support) for j in range(16)]
            H = sp.Matrix(8, 9, lambda i, j: h[i+j])
            self.assertEqual(H.rank(), 7)
            q = sp.zeros(8, 1)
            q[s] = 1
            self.assertEqual(H.T*q, sp.zeros(9, 1))
            r0, r1 = sp.zeros(9, 1), sp.zeros(9, 1)
            r0[s] = 1
            r1[s+1] = 1
            self.assertEqual(H*r0, sp.zeros(8, 1))
            self.assertEqual(H*r1, sp.zeros(8, 1))
            nonzero_rows = [i for i in range(8) if any(H.row(i))]
            nonzero_columns = [j for j in range(9) if any(H.col(j))]
            determinant = H.extract(nonzero_rows, nonzero_columns).det()
            families[s] = (support, nonzero_rows, nonzero_columns, determinant)
        for row in rows:
            s = row["annihilator_monomial_index"]
            support, minor_rows, minor_columns, determinant = families[s]
            self.assertTrue(set(row["omitted_coordinates"]).isdisjoint(row["unit_moment_indices"]))
            self.assertTrue(set(row["omitted_coordinates"]).isdisjoint(row["normal_coordinate_indices"]))
            self.assertEqual(row["normal_coordinate_indices"], [2*s, 2*s+1])
            self.assertEqual(row["unit_moment_indices"], support)
            self.assertEqual(row["minor_rows"], minor_rows)
            self.assertEqual(row["minor_columns"], minor_columns)
            self.assertEqual(row["minor_determinant"], determinant)

    def test_reduced_annihilator_and_conormal_coefficients(self):
        row = self.saved["reduced_conormal"]
        h, q = row["moments"], row["annihilator"]
        H = sp.Matrix(8, 9, lambda i, j: h[i+j])
        self.assertEqual(H.T*sp.Matrix(q), sp.zeros(9, 1))
        self.assertEqual(H.rank(), 7)
        z = sp.symbols("z")
        polynomial = sum(a*z**i for i, a in enumerate(q))
        self.assertEqual(sp.expand(polynomial-sp.prod(z-t for t in row["roots"])), 0)
        square = sp.Poly(polynomial**2, z)
        expected = [[square.nth(i) for i in range(16)],
                    [0]+[square.nth(i) for i in range(15)]]
        self.assertEqual(row["q_squared_basis"], expected)
        self.assertEqual(sp.Matrix(row["conormal_basis"]+expected).rank(), 2)
        self.assertEqual(H[:7, :7].det(), row["leading_seven_minor"])

    def test_application_budgets_and_honest_square_boundary(self):
        for row in self.saved["applications"]:
            x, y, z = row["target"]
            loss = (1152-x*z)+(1152-y*z)
            self.assertEqual(loss, 475)
            self.assertEqual(3*z+loss, 568)
            self.assertLess(3*z+loss, 8*72)
            self.assertGreater(x*y, 12*72)
            self.assertEqual((x*y+71)//72, 13)
            self.assertLess(row["maximum_symbol_image_dimension"], row["required_projection_dimension"])
        for row in self.saved["section_dimension_contradictions"]:
            self.assertLess(row["annihilator_incidence_dimension_upper"], row["putative_component_dimension_lower"])
        square = self.saved["M30"]
        self.assertLess(2*30+2*(1152-900), 576)
        self.assertGreaterEqual(3*30+2*(1152-900), 576)
        self.assertEqual(square["required_projection_dimension"], 3*4)
        self.assertLessEqual(square["required_projection_dimension"], square["symbol_image_dimension_interval"][0])
        self.assertFalse(square["excluded_by_this_argument"])
        self.assertFalse(self.saved["singular_degenerations_excluded"])
        self.assertFalse(self.saved["independent_review"])
        self.assertFalse(self.saved["improves_omega"])

    def test_pins_manifest_and_complete_control_replay(self):
        self.assertEqual(self.saved, json.loads(json.dumps(v.report(), default=v.exact_integer)))
        with self.assertRaises(TypeError):
            v.exact_integer(sp.Rational(1, 2))
        for name in ["sources.json", "manifest.json"]:
            data = json.loads((PACKAGE / name).read_text())
            entries = data["local_dependencies"] if name == "sources.json" else [
                {"path": p, "sha256": h} for p, h in data["sha256"].items()]
            for row in entries:
                self.assertEqual(hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest(),
                                 row["sha256"], row["path"])


if __name__ == "__main__":
    unittest.main()
