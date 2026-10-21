import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'research/ai/2026-10-20-anisotropic-constructions/parity_balancing_spin44_freedoms.py'
SPEC = importlib.util.spec_from_file_location('balanced_spin44_freedoms', PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class BalancedSpinFreedomTests(unittest.TestCase):
    def test_actual_ranks_kernels_and_complete_graph_replay(self):
        report = MODULE.verify()
        for leg in ('Y', 'Z'):
            ranks = report['low_coordinate_freedoms'][leg]
            self.assertEqual(ranks['literal_low_domain_dimension'], 160)
            self.assertEqual(ranks['all32_exact_response_rank'], 160)
            self.assertEqual(ranks['retained27_exact_response_rank'], 145)
            self.assertEqual(ranks['retained27_exact_kernel_dimension'], 15)
            self.assertTrue(ranks['kernel_basis_is_exactly_actual_omitted_rows'])
        self.assertEqual(report['low_coordinate_freedoms']['Y']['retained_map_nonzero_coordinate_support'], 158)
        self.assertEqual(report['low_coordinate_freedoms']['Z']['retained_map_nonzero_coordinate_support'], 160)
        self.assertEqual(report['positive_graph_changed_rows_each_leg'], 81)
        self.assertEqual(report['positive_graph_full_source_replay']['target_coefficients_checked'], 59049)
        self.assertEqual(report['positive_graph_full_source_replay']['nonzero_target_coefficients'], 243)
        self.assertTrue(report['nonzero_graph_residual_rejected_by_full_source_replay'])
        self.assertFalse(report['new_exponent_established'])

    def test_duplicate_minor_column_is_rejected(self):
        certificate = json.loads(MODULE.CERTIFICATE.read_text())
        exported = json.loads(MODULE.MAPS.read_text())
        maps, _ = MODULE.parse_full(exported)
        response = MODULE.low_responses(maps)[0]
        record = copy.deepcopy(certificate['ranks']['Y']['full'])
        record['columns'][1] = record['columns'][0]
        with self.assertRaises(ArithmeticError):
            MODULE.check_minor(response, record, MODULE.low_domains()[0], 160, 864)

    def test_zero_omitted_kernel_vector_is_rejected(self):
        exported = json.loads(MODULE.MAPS.read_text())
        maps, _ = MODULE.parse_full(exported)
        domain = MODULE.low_domains()[1]
        response = MODULE.trim_response(MODULE.low_responses(maps)[1])
        vectors = MODULE.omitted_rows(maps[2], domain)
        vectors[0] = {}
        with self.assertRaises(ArithmeticError):
            MODULE.check_deleted_kernel(response, vectors, domain)


if __name__ == '__main__':
    unittest.main()
