"""Exact fixed-core extension gate for the repaired 27-channel spin maps.

The target's first image is forced only at common leg dimension778.
The result does not concern an unrestricted source or a changed Z map.
"""

import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import parity_structure_spin_endpoint as endpoint


ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / "results/anisotropic-constructions-2026-10-20"
MINOR = DIRECTORY / "spin-endpoint-extension-minor.json"
REPORT = DIRECTORY / "spin-endpoint-extension-certificate.json"


def rebuild_minor(data, specification):
    maps, denominators = endpoint.parse_maps(data)
    Z = {(row, column): value for row, column, value in maps[2]}
    prime = specification["prime"]
    labels = specification["selected_row_labels_i_s_I_beta"]
    if prime != 65521 or specification["excluded_middle_coordinate"] != 0:
        raise ArithmeticError("The G1 certificate uses the wrong field or channel")
    if specification["fixed_Z_denominator"] != denominators[2]:
        raise ArithmeticError("The G1 denominator does not match the actual map")
    if len(labels) != 120 or len(set(map(tuple, labels))) != 120:
        raise ArithmeticError("The G1 minor needs120 distinct rows")
    matrix = []
    for label in labels:
        if len(label) != 4 or any(type(value) is not int for value in label):
            raise ArithmeticError("A G1 row label has the wrong format")
        i, s, I, beta = label
        if not (0 <= i < 8 and 0 <= s < 8 and 0 <= I < 3 and 1 <= beta < 27):
            raise ArithmeticError("A G1 row uses an excluded or out-of-range channel")
        row = []
        for L in range(15):
            for j in range(8):
                r = L-s
                column = endpoint.coordinate(r, i+j, 1) if 0 <= r < 8 else None
                row.append(0 if column is None else Z.get((27*I+beta, column), 0))
        matrix.append(row)
    determinant = endpoint.determinant_mod(matrix, prime)
    if not determinant:
        raise ArithmeticError("The rebuilt G1 minor is singular")
    return determinant


def verify():
    data = json.loads(endpoint.MAPS.read_text())
    response_minor = json.loads(endpoint.MINOR.read_text())
    core = endpoint.verify(data, response_minor)
    if core.get("full_response_rank_exact") != 191 or core.get("fixed_core_first_preimage_dimension_exact") != 778:
        raise ArithmeticError("The repaired core does not have the forced first preimage")
    specification = json.loads(MINOR.read_text())
    determinant = rebuild_minor(data, specification)
    return {
        "source": "A(8,8)", "fixed_rectangular_core": "M(3,3,27)",
        "fixed_maps_sha256": hashlib.sha256(endpoint.MAPS.read_bytes()).hexdigest(),
        "response_minor_sha256": hashlib.sha256(endpoint.MINOR.read_bytes()).hexdigest(),
        "extension_minor_sha256": hashlib.sha256(MINOR.read_bytes()).hexdigest(),
        "core_response_rank": 191, "forced_first_image_dimension": 778,
        "high_long_coordinate_subspace_dimension": 768,
        "actual_first_core_images": 9,
        "quotient_dimension_after_annihilation": 1,
        "required_new_Y_unit_response_rank": 3,
        "G1_full_matrix_shape": [4992, 120], "G1_column_rank": 120,
        "G1_minor_integer_determinant_mod_65521": determinant,
        "excluded_middle_coordinate_in_G1": 0,
        "excluded_extension": "M(27,27,27) direct sum M(7,7,7)",
        "scope": "Ordinary extensions retaining the repaired Y and Z rows exactly",
        "first_core_images_may_change_by_kernel_vectors": True,
        "D774_extension_excluded": False,
        "changed_retained_maps_excluded": False,
        "arbitrary_degenerations_excluded": False,
        "new_exponent_established": False,
    }


if __name__ == "__main__":
    report = verify()
    REPORT.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))
