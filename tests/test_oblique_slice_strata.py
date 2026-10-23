"""Focused exact contraction checks for the adapted oblique residual."""
import importlib.util
from pathlib import Path
import unittest


SRC = Path(__file__).resolve().parents[1] / "research" / "ai" / "2026-10-23-oblique-slice-strata" / "verify.py"
SPEC = importlib.util.spec_from_file_location("oblique_slice_strata_verify", SRC)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ObliqueSliceStrataTests(unittest.TestCase):
    def test_binary_complete(self):
        result = MODULE.verify(exhaustive_k=3)
        self.assertEqual(result["exhaustive_GF2_checks"], sum(2**(3+2*k)+2*2**(5+2*k) for k in range(4)))
        self.assertEqual(result["odd_prime_checks"], 3*5*3*48)
        self.assertEqual(result["rational_checks"], 5*3*32)

    def test_rank_two_linear_families(self):
        k = 3
        dims, _ = MODULE.tensor(k)
        self.assertEqual(dims, (9, 11, 11))
        for i in range(k+1):
            vec = [0] * dims[0]
            vec[0 if i == 0 else i+2] = 1
            self.assertEqual(MODULE.literal_slice(k,0,vec,101),2)
        for i in range(k+1):
            vec = [0] * dims[0]
            vec[1 if i == 0 else 3+k+(i-1)] = 1
            self.assertEqual(MODULE.literal_slice(k,0,vec,101),2)
        self.assertEqual(MODULE.literal_slice(
            k,0,[1,1]+[0]*(dims[0]-2),101),4)
        self.assertEqual(MODULE.literal_slice(
            k,0,[0,0,1]+[0]*(dims[0]-3),101),4)

    def test_boundary_and_zero(self):
        for k in (0,1,3,5):
            dims,_ = MODULE.tensor(k)
            for leg, dimension in enumerate(dims):
                self.assertEqual(
                    MODULE.literal_slice(k,leg,[0]*dimension,2),0)
                self.assertEqual(
                    MODULE.expected_rank(k,leg,[0]*dimension,2),0)
            self.assertEqual(
                MODULE.literal_slice(k,0,[1]+[0]*(dims[0]-1),2),2)
            self.assertEqual(
                MODULE.literal_slice(k,0,[0,0,1]+[0]*(dims[0]-3),2),4)


if __name__ == "__main__":
    unittest.main()
