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

    _, unit, inverse, normalized, high = source.outer_source()
    if source.multiply(unit, inverse) != source.identity(28):
        raise ValueError('the outer source unit is not invertible')
    nilpotent = source.full_normalized_matrix(normalized[0], 0)
    supports = []
    for k in range(3, 7):
        for i in range(4):
            outer_index = 4 * i
            matrix = high[outer_index]
            rows = [r for r, row in enumerate(matrix) if any(row)]
            if rows != EXPECTED_ROWS:
                raise ValueError(f'f_({i},0) at middle index {k} has unexpected support {rows}')
            if any(type(value) is not int for row in matrix for value in row):
                raise ValueError('source reconstruction produced noninteger entries')

            source_slice = source.full_normalized_matrix(normalized[outer_index], k)
            actual = source.multiply(nilpotent, source_slice)
            q_matrix = source.multiply(inverse, matrix)
            expected = source.zeros(112, 112)
            for outer_row in range(28):
                h, r = divmod(outer_row, 4)
                for outer_column in range(28):
                    h_prime, r_prime = divmod(outer_column, 4)
                    row = (h * 4 + 3) * 4 + r
                    column = (h_prime * 4 + k - 3) * 4 + r_prime
                    expected[row][column] = q_matrix[outer_row][outer_column]
            if actual != expected:
                raise ValueError(f'f_({i},0) does not occupy only block (3,{k - 3})')

            supports.append({
                'middle_index': k,
                'block_position': [3, k - 3],
                'outer_parameter': [i, 0],
                'nonzero_rows_after_unit_normalization': rows,
            })

    return {
        'field_scope': 'every field; exact integer row-support identities and unit pivots',
        'outer_parameters': expected_labels,
        'middle_indices': [3, 4, 5, 6],
        'block_positions': [[3, column] for column in range(4)],
        'family_dimension': 16,
        'common_row_support': EXPECTED_ROWS,
        'generator_supports': supports,
        'full_source_embeddings_checked': 16,
        'minimum_nonzero_rank': 6,
        'rank_loss_six_alignment_realizable': True,
        'normalized_product_PC_identity': False,
        'full_rank_six_locus_classified': False,
        'tensor_degeneration_constructed': False,
        'exponent_improvement': False,
    }


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))
