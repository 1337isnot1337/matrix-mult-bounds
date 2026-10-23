import importlib.util
import json
from pathlib import Path
import unittest


ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/'research/ai/2026-10-20-anisotropic-constructions/parity_structure_spin44_double_endpoint.py'
SPEC=importlib.util.spec_from_file_location('double_endpoint_recovery',PATH)
MODULE=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class DoubleEndpointTests(unittest.TestCase):
    def test_complete_original_source_and_rank(self):
        report=MODULE.verify()
        self.assertEqual(report['source_terms_checked'],262144)
        self.assertEqual(report['all_target_coefficients_checked'],59049)
        self.assertEqual(report['nonzero_target_coefficients'],243)
        self.assertEqual(report['full_response_rank_exact'],190)
        self.assertEqual(report['fixed_core_first_preimage_dimension_exact'],779)
        self.assertFalse(report['new_exponent_established'])

    def test_nonzero_map_tamper(self):
        data=json.loads(MODULE.MAPS.read_text())
        data['maps']['Y']['entries'][0][2]*=2
        with self.assertRaises(ArithmeticError):MODULE.verify(data=data)

    def test_nonzero_graph_tamper(self):
        witness=json.loads(MODULE.WITNESS.read_text())
        witness['A']['entries'][0][2]*=2
        with self.assertRaises(ArithmeticError):MODULE.verify(witness=witness)

    def test_changed_minor_is_rejected(self):
        minor=json.loads(MODULE.MINOR.read_text())
        minor['determinant_mod_prime']+=1
        with self.assertRaises(ArithmeticError):MODULE.verify(minor=minor)


if __name__=='__main__':unittest.main()
