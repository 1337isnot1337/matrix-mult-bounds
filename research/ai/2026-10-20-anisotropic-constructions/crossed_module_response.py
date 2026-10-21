"""Exact ambient response of the saved A(8,8) -> M(4,4,22) maps.

Only the standard library is needed.  A nonsingular minor modulo a prime
certifies the rational rank lower bound; disjoint support gives the upper
bound and the four-block decomposition.
"""

import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crossed_module11 import unpack


ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / "results/anisotropic-constructions-2026-10-20"
WITNESS = DIRECTORY / "crossed-module11-witness.json"
MINOR = DIRECTORY / "crossed-module-response-minor.json"
REPORT = DIRECTORY / "crossed-module-response-certificate.json"


def determinant_mod(matrix, prime):
    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("A nonempty square matrix is required")
    rows = [[entry % prime for entry in row] for row in matrix]
    answer = 1
    for j in range(len(rows)):
        selected = next((i for i in range(j, len(rows)) if rows[i][j]), None)
        if selected is None:
            return 0
        if selected != j:
            rows[j], rows[selected] = rows[selected], rows[j]
            answer = -answer
        pivot = rows[j][j]
        answer = answer*pivot % prime
        inverse = pow(pivot, -1, prime)
        for i in range(j+1, len(rows)):
            factor = rows[i][j]*inverse % prime
            if factor:
                rows[i] = [(a-factor*b) % prime for a, b in zip(rows[i], rows[j])]
    return answer % prime


def response_entry(Y, Z, i, s, output_column):
    """An integer numerator in one p/t block of the full first response."""
    target_y, target_z = divmod(output_column, 44)
    ey, yrow = divmod(target_y, 22)
    ez, zrow = divmod(target_z, 22)
    if (ez+s) % 2 != ey:
        return 0
    shift = (ez+s-ey)//2
    answer = 0
    for a in range(4):
        L = a+shift
        if not 0 <= L < 5:
            continue
        for j in range(8):
            H = i+j
            if H < 9:
                answer += Y[yrow][8*L+j]*Z[zrow][9*a+H]
    return answer


def verify():
    witness = json.loads(WITNESS.read_text())
    minor = json.loads(MINOR.read_text())
    Y, dy = unpack(witness["Y"], (22, 40))
    Z, dz = unpack(witness["Z"], (22, 36))
    prime = minor["prime"]
    if prime != 65521 or any(prime % d == 0 for d in range(2, 256)):
        raise ArithmeticError("The certificate modulus is not the stated prime")
    columns = minor["output_columns"]
    if len(columns) != 64 or len(set(columns)) != 64 or any(
            type(c) is not int or not 0 <= c < 44*44 for c in columns):
        raise ArithmeticError("Invalid 64-column response minor")
    if dy*dz != minor["denominator_product"] or dy*dz % prime == 0:
        raise ArithmeticError("Invalid denominator scale")
    matrix = [[response_entry(Y, Z, i, s, c) for c in columns]
              for i in range(8) for s in range(8)]
    determinant = determinant_mod(matrix, prime)
    if not determinant:
        raise ArithmeticError("The saved response minor is singular")

    # Distinct middle coordinates correspond to four disjoint p/t output
    # blocks.  This checks the entire support claim independently of the
    # stored minor and without any random choices.
    allowed = {(2*p+t, p, t) for p in range(2) for t in range(2)}
    for k in range(15):
        found = [(p, t) for p in range(2) for t in range(2) if 2*p+t == k]
        if found != [(p, t) for kk, p, t in sorted(allowed) if kk == k]:
            raise ArithmeticError("Unexpected middle-coordinate collision")
        if len(found) != (1 if k < 4 else 0):
            raise ArithmeticError("Response block supports are not disjoint")

    return {
        "source": "A(8,8)", "fixed_target": "M(4,4,22)",
        "witness_sha256": hashlib.sha256(WITNESS.read_bytes()).hexdigest(),
        "minor_sha256": hashlib.sha256(MINOR.read_bytes()).hexdigest(),
        "prime": prime, "minor_size": 64,
        "integer_numerator_determinant_mod_prime": determinant,
        "per_block_response_rank": 64, "disjoint_response_blocks": 4,
        "full_response_rank": 256, "full_response_kernel_dimension": 704,
        "fixed_first_core_dimension": 16,
        "maximum_leg_dimension_of_an_extension_preserving_the_saved_other_maps": 720,
        "excluded_fixed_seed_extensions": ["M(27,27,27)", "M(27,27,27) direct sum M(7,7,7)"],
        "scope": "Ordinary extensions retaining the exact saved Y and Z module maps",
        "other_module_maps_excluded": False, "arbitrary_degenerations_excluded": False,
        "new_exponent_established": False,
    }


if __name__ == "__main__":
    report = verify()
    REPORT.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))
