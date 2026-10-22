"""Independent coefficient replay and tamper controls for the modular barrier."""
import copy
import importlib.util
from itertools import product
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-21-a5-peirce'
RESULTS = ROOT/'results/a5-peirce-2026-10-21'
spec = importlib.util.spec_from_file_location('a5_tight_verifier', PACKAGE/'verify_tight.py')
verifier = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verifier)


class A5TightBarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = json.loads((RESULTS/'tight-certificate.json').read_text())

    def test_complete_integer_and_field_replay(self):
        result = verifier.verify(self.certificate)
        self.assertEqual(result, json.loads((RESULTS/'tight-verification.json').read_text()))
        self.assertEqual(result['source_coefficients_checked'], 216000)
        self.assertEqual(result['leading_terms'], 277)
        self.assertEqual(result['entropy_lower_bound'], '517/5')
        self.assertFalse(result['exponent_improvement'])

    def test_field_laws_and_inverses(self):
        T = verifier.TABLE
        self.assertEqual(T[2][2], 3)
        for a in range(1, 4):
            self.assertEqual(T[a][verifier.INVERSE[a]], 1)
        for a, b, c in product(range(4), repeat=3):
            self.assertEqual(T[T[a][b]][c], T[a][T[b][c]])
            self.assertEqual(T[a][b ^ c], T[a][b] ^ T[a][c])

    def test_singular_basis_and_source_pole_are_rejected(self):
        bad = copy.deepcopy(self.certificate)
        bad['basis'][0] = bad['basis'][1]
        with self.assertRaisesRegex(ValueError, 'singular'):
            verifier.verify(bad)
        bad = copy.deepcopy(self.certificate)
        bad['degeneration_weights'][0][0] -= 100
        with self.assertRaisesRegex(ValueError, 'pole'):
            verifier.verify(bad)

    def test_tightness_and_coefficient_tampering_are_rejected(self):
        bad = copy.deepcopy(self.certificate)
        bad['tight_weights'][0][0] = bad['tight_weights'][0][1]
        with self.assertRaisesRegex(ValueError, 'injective'):
            verifier.verify(bad)
        bad = copy.deepcopy(self.certificate)
        bad['leading_tensor'][0][3] ^= 1
        with self.assertRaisesRegex(ValueError, 'source coefficients'):
            verifier.verify(bad)

    def test_entropy_and_cover_tampering_are_rejected(self):
        bad = copy.deepcopy(self.certificate)
        bad['coefficient_field'] = 'F5'
        with self.assertRaisesRegex(ValueError, 'coefficient field'):
            verifier.verify(bad)
        bad = copy.deepcopy(self.certificate)
        bad['probability_denominator'] += 1
        with self.assertRaisesRegex(ValueError, 'rational distribution'):
            verifier.verify(bad)
        bad = copy.deepcopy(self.certificate)
        bad['marginal_counts'][0][0] += 1
        with self.assertRaisesRegex(ValueError, 'marginals'):
            verifier.verify(bad)
        bad = copy.deepcopy(self.certificate)
        bad['cover_projection'][0]['image'] = (bad['cover_projection'][0]['image']+1) % 60
        with self.assertRaisesRegex(ValueError, 'projection|homomorphism'):
            verifier.verify(bad)


if __name__ == '__main__':
    unittest.main()
