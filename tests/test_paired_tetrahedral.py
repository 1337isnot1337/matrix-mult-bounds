"""Exact finite-symmetry controls; no numerical-search success is assumed."""
import importlib.util
from pathlib import Path
import unittest


DIRECTORY = Path(__file__).resolve().parents[1] / "research/ai/2026-10-20-paired-direct-sums"


def module(filename):
    spec = importlib.util.spec_from_file_location(filename, DIRECTORY / (filename+".py"))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


class PairedTetrahedralTests(unittest.TestCase):
    def test_native_kernel_covariance_and_odd_rank(self):
        result = module("tetrahedral_kernel").certificate()
        self.assertTrue(result["native_source_covariance"])
        self.assertEqual(result["compressed_first_slice_ranks"], [4, 3, 4, 3, 3, 3, 4, 3, 4])
        self.assertEqual(result["rank_three_minor_determinant"], 1)

    def test_fixed_sector_and_exact_scalar_defect(self):
        result = module("scalar_symmetry_obstructions").certificate()
        self.assertTrue(result["a4_equivariant_p3_to_m3_ordinary_restriction_excluded"])
        self.assertEqual(result["polarization_full_coefficient_positions_checked"], 27)
        self.assertEqual(result["full_sl2_necessary_scalar_summands"], 9)
        self.assertTrue(result["full_sl2_any_number_of_trivial_scalars_excluded"])
        self.assertFalse(result["matrix_multiplication_construction"])

    def test_every_scalar_repair_phase_has_nonzero_determinant(self):
        result = module("tetrahedral_scalar_obstruction").certificate()
        self.assertEqual([row["determinant"] for row in result["phase_certificates"]], [256, -256, -256])
        self.assertTrue(result["all_phases_rejected"])
        self.assertFalse(result["construction_supplied"])

    def test_scalar_extension_is_explicit(self):
        result = module("narrow_scalar_search").exact_control()
        self.assertEqual(result["source_shape"], (5, 7, 7))
        self.assertEqual(result["source_terms"], 17)
        self.assertTrue(result["appended_scalar_term_checked"])


if __name__ == "__main__":
    unittest.main()
