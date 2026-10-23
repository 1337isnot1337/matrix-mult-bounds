"""Verify the exact support identities for the four-dimensional rank-six family."""
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / 'research/ai/2026-10-23-resolvent-minrank/verify.py'
CERTIFICATE = ROOT / 'results/resolvent-minrank-2026-10-23/certificate.json'
EXPECTED_ROWS = [0, 7, 14, 21, 22, 23]


def load_source_verifier():
    spec = importlib.util.spec_from_file_location('resolvent_minrank_verify', SOURCE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify():
    source = load_source_verifier()
    certificate = json.loads(CERTIFICATE.read_text())
    predecessor = source.verify(certificate)
    if (predecessor['mixed_block_dimension'] != 31
            or predecessor['mixed_block_minimum_rank'] != 6
            or predecessor['full_limiting_space_dimension'] != 112
            or predecessor['full_limiting_space_minimum_rank'] != 6):
        raise ValueError('the pinned minimum-rank prerequisite did not verify')

    _, labels = source.mixed_basis()
    expected_labels = [['f', i, 0] for i in range(4)]
    if any(label not in labels for label in expected_labels):
        raise ValueError('a proposed family generator is absent from the mixed basis')

    _, unit, inverse, _, high = source.outer_source()
    if source.multiply(unit, inverse) != source.identity(28):
        raise ValueError('the outer source unit is not invertible')
    supports = []
    for i in range(4):
        matrix = high[4 * i]
        rows = [r for r, row in enumerate(matrix) if any(row)]
        if rows != EXPECTED_ROWS:
            raise ValueError(f'f_({i},0) has unexpected exact row support {rows}')
        if any(type(value) is not int for row in matrix for value in row):
            raise ValueError('source reconstruction produced noninteger entries')
        supports.append({'parameter': [i, 0], 'nonzero_rows': rows})

    return {
        'field_scope': 'every field; exact integer row-support identities and unit pivots',
        'family_parameters': expected_labels,
        'family_dimension': 4,
        'common_row_support': EXPECTED_ROWS,
        'generator_supports': supports,
        'minimum_nonzero_rank': 6,
        'rank_loss_six_alignment_realizable': True,
        'normalized_product_PC_identity': False,
        'full_rank_six_locus_classified': False,
        'tensor_degeneration_constructed': False,
        'exponent_improvement': False,
    }


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))
