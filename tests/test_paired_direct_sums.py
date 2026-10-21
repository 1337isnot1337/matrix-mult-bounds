"""Independent coefficient controls for the paired direct-sum frontier."""
from fractions import Fraction
import importlib.util
from itertools import combinations
import json
from math import comb
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "paired_direct_sums", ROOT / "research/ai/2026-10-20-paired-direct-sums/frontier.py")
F = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(F)
JET_SPEC = importlib.util.spec_from_file_location(
    "paired_laurent_coefficients", ROOT / "research/ai/2026-10-20-paired-direct-sums/laurent_search.py")
JET = importlib.util.module_from_spec(JET_SPEC)
JET_SPEC.loader.exec_module(JET)


def load_discovery_module(name):
    spec = importlib.util.spec_from_file_location(
        name, ROOT / f"research/ai/2026-10-20-paired-direct-sums/{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def coefficient_rank_mod_two(shapes, ambient, degree):
    """Build the complete direct-sum Koszul matrix from tensor terms."""
    terms = []
    a_offset = b_offset = c_offset = 0
    for l, b, r in shapes:
        for i in range(l):
            for j in range(b):
                for k in range(r):
                    terms.append((a_offset+i*r+k, b_offset+i*b+j, c_offset+j*r+k))
        a_offset += l*r
        b_offset += l*b
        c_offset += b*r
    if a_offset > ambient:
        raise ValueError("source first leg is too small")
    row_ids = {}
    pivots = {}
    for subset in combinations(range(ambient), degree):
        mask = sum(1 << i for i in subset)
        for second in range(b_offset):
            vector = 0
            for first, source_second, third in terms:
                if source_second != second or (mask >> first) & 1:
                    continue
                row = (mask | (1 << first), third)
                if row not in row_ids:
                    row_ids[row] = len(row_ids)
                vector ^= 1 << row_ids[row]
            while vector:
                pivot = vector.bit_length()-1
                if pivot in pivots:
                    vector ^= pivots[pivot]
                else:
                    pivots[pivot] = vector
                    break
    return len(pivots)


class PairedDirectSumsTests(unittest.TestCase):
    def test_exact_second_order_pole_controls(self):
        report = load_discovery_module("higher_jet_search").exact_controls()
        self.assertTrue(report["exact_second_order_control_passed"])
        self.assertTrue(report["pole_detected_despite_correct_target_coefficient"])
        self.assertEqual(report["nonzero_coefficients_by_degree"], [0, 0, 3, 0, 0, 0, 0])

    def test_exact_narrow_source_coefficient_control(self):
        report = load_discovery_module("narrow_source_search").exact_control()
        self.assertTrue(report["exact_control_passed"])
        self.assertTrue(report["sign_error_detected"])
        self.assertEqual(report["full_target_positions_checked"], 64)

    def test_exact_algebra_accepts_only_the_matrix_control(self):
        report = load_discovery_module("kernel_algebra_search").exact_control()
        self.assertTrue(report["matrix_tensor_control"]["accepted"])
        self.assertFalse(report["closed_nonmatrix_control"]["accepted"])
        self.assertFalse(report["closed_center_one_nonsemisimple_control"]["accepted"])

    def test_small_laurent_target_passes_first_leg_screen(self):
        shapes = ((1, 3, 3), (3, 3, 2))
        self.assertIsNone(F.first_obstruction(3, shapes))
        self.assertEqual([sum(F.format_of(shape)[k] for shape in shapes) for k in range(3)],
                         [9, 12, 15])

    def test_full_rational_laurent_controls(self):
        report = JET.exact_controls()
        self.assertTrue(report["exact_controls_passed"])
        self.assertTrue(report["deliberate_pole_detected_despite_correct_constant_term"])
        self.assertEqual(report["w_nonzero_coefficients_by_degree"], [0, 3, 3, 1])
        self.assertEqual(report["p2_nonzero_coefficients_by_degree"], [0, 8, 0, 0])

    def test_direct_sum_padding_matches_explicit_coefficients(self):
        for shapes, ambient in [(((2, 2, 2), (1, 1, 1)), 6),
                                (((1, 2, 2), (2, 1, 1)), 5)]:
            for p in range(ambient):
                expected = sum(F.block_ranks(shape, ambient)[p] for shape in shapes)
                self.assertEqual(coefficient_rank_mod_two(shapes, ambient, p), expected)

    def test_individual_tests_do_not_replace_sum_test(self):
        shapes = ((2, 6, 3), (6, 9, 5))
        for shape in shapes:
            self.assertIsNone(F.first_obstruction(6, (shape,)))
        self.assertEqual(F.first_obstruction(6, shapes), {
            "power": 1, "source_rank": 2360, "target_rank": 2376})

    def test_selected_matrix_ranks_match_partition_formula(self):
        # The imported partition/Weyl formula is distinct from the Euler
        # sum used to generate the maintained padded-rank certificate.
        for l, r in ((4, 10), (10, 6)):
            for p in range(l*r):
                self.assertEqual(F.RANKS.matrix_basic_rank(l, r, p),
                                 F.RANKS.matrix_partition_rank(l, r, p))

    def test_selected_certificate_and_strict_gate(self):
        path = ROOT / "results/paired-direct-sums-2026-10-20/selected-target.json"
        self.assertEqual(json.loads(path.read_text()), F.selected_certificate())
        for base, numerator in [(15840, 27519), (25920, 39763)]:
            self.assertLess(numerator**1500, base**1121 * 20**1500)
        self.assertGreater(27519+39763, 3364*20)
        with self.assertRaises(ArithmeticError):
            F.conditional_gate(10, F.SELECTED_SHAPES, omega=Fraction(56, 25))

    def test_small_frontier_replay(self):
        saved = json.loads((ROOT / "results/paired-direct-sums-2026-10-20/frontier-through-10.json").read_text())
        for a in range(2, 7):
            self.assertEqual(F.frontier_one_size(a), saved["records"][a-2])

    def test_integer_root_bounds_and_target_normalization(self):
        for volume in (1, 16, 81, 256, 440, 720):
            lower, upper = F.root_interval(volume, 19)
            fourth_power = volume**3 << 76
            self.assertLessEqual(lower**4, fourth_power)
            self.assertGreaterEqual(upper**4, fourth_power)
            self.assertLessEqual(upper-lower, 1)
        selected = F.SELECTED_SHAPES
        exchanged = [(r, b, l) for l, b, r in reversed(selected)]
        self.assertEqual(F.canonical_pair(selected), F.canonical_pair(exchanged))
        self.assertTrue(F.improves_endpoint(10, (440, 720)))
        self.assertFalse(F.improves_endpoint(10, (440,)))


if __name__ == "__main__":
    unittest.main()
