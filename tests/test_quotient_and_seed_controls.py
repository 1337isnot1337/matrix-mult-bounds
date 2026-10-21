"""Replay saved exact construction maps and the cyclic scalar invariant."""

import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-20-anisotropic-constructions'
RESULTS = ROOT / 'results/anisotropic-constructions-2026-10-20'


def load_module(name):
    spec = importlib.util.spec_from_file_location(name, PACKAGE / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class QuotientAndSeedControls(unittest.TestCase):
    def test_three_quotient_invariant_and_complete_tensor(self):
        module = load_module('parity_structure_three_quotients')
        expected = json.loads((PACKAGE / 'parity_structure_three_quotients_certificate.json').read_text())
        self.assertEqual(module.verify(), expected)
        self.assertEqual(expected['complete_trilinear_coefficients_checked'], 2187)
        self.assertEqual(expected['examples'][0]['scalar_defect_frobenius_norm_squared'], '27')

    def test_a23_quotient_control_and_corrupted_map(self):
        certificate = RESULTS / 'parity_balancing_quotient_control_a23_m4.json'
        script = PACKAGE / 'parity_balancing_quotient_control.py'
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'verified.json'
            command = [sys.executable, '-S', str(script), '--certificate', str(certificate), '--output', str(output)]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads(output.read_text())['verification']
            self.assertEqual(report['target_coefficients_checked'], 4096)
            self.assertEqual(report['source_terms_checked'], 216)
            self.assertTrue(report['all_kernel_maps_zero'])
            altered = json.loads(certificate.read_text())
            row = altered['map_numerators']['A'][0]
            index = next(i for i, value in enumerate(row) if value)
            row[index] += 1
            invalid = Path(directory) / 'invalid.json'
            invalid.write_text(json.dumps(altered))
            command[4] = str(invalid)
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('complete full-source coefficient identity failed', result.stderr)

    def test_a88_sparse_seed_and_coefficient_tamper(self):
        # This module shares only the standard-library contraction helpers.
        previous = list(sys.path)
        sys.path.insert(0, str(PACKAGE))
        try:
            module = load_module('parity_structure_a88_seed')
            witness = json.loads((PACKAGE / 'parity_structure_a88_seed_sparse.json').read_text())
            maps = witness['integer_maps']
            report = module.verify(maps)
            self.assertEqual(report['source_terms'], 262144)
            self.assertEqual(report['target_terms'], 3375)
            self.assertEqual(report['map_nonzero_counts'], [462, 462, 462])
            altered = copy.deepcopy(maps)
            altered[0][0][0][1] += 1
            with self.assertRaisesRegex(ValueError, 'complete A88-to-M15 coefficient identity failed'):
                module.verify(altered)
        finally:
            sys.path[:] = previous


if __name__ == '__main__':
    unittest.main()
