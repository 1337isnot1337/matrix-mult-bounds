"""Exact arithmetic for an unproved finite-profile improvement criterion."""
import argparse
from fractions import Fraction
import json
from pathlib import Path


def diagonal(a):
    h = Fraction(1)
    for j in range(1, a):
        h *= Fraction(3*j+1, 3*j)
    return Fraction(3*a-1, 2)*h


def report():
    required = Fraction(13, 12)*diagonal(4)
    assert required == Fraction(5005, 486)
    lhs = 5005**2249
    rhs = 22**3000*81**2249
    assert lhs > rhs
    assert 3816**2249 > 22**6000
    records = []
    for a in range(1, 17):
        d = diagonal(a)
        volume = a*a*(2*a-1)
        difference = (6*a-2)**8-6**6*volume**3
        records.append({"a": a, "matching_diagonal": str(d),
            "endpoint_ceiling_ratio_cubed": str(Fraction((6*a-2)**4)/(6*d)**3),
            "matrix_dimension_screen_difference": difference,
            "matrix_extraction_dimension_screen_excludes": difference >= 0})
    return {"status": "conditional implication; universal lower-bound premise unproved",
        "new_exponent_established": False,
        "premise": {"minimum_t": "749/1000", "P_4_4_lower": str(required),
                    "relative_gain": "13/12"},
        "conditional_rational_exponent": "2249/1000",
        "integer_certificate": {"lhs": "5005**2249", "rhs": "22**3000*81**2249",
            "lhs_strictly_larger": lhs > rhs,
            "lhs_bit_length": lhs.bit_length(), "rhs_bit_length": rhs.bit_length()},
        "finite_tensor_target": {"source": "tensor product of all six leg permutations of C(4,4)",
            "source_leg_dimensions": [12544]*3, "source_border_rank_upper_bound": 117649,
            "target": "M(106,106,106)", "target_leg_dimensions": [11236]*3,
            "constructed": False, "integer_certificate": "3816**2249 > 22**6000",
            "integer_certificate_passes": 3816**2249 > 22**6000,
            "n105_endpoint_test": (36*105)**3 > 22**8,
            "n106_endpoint_test": (36*106)**3 > 22**8},
        "records": records}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(report(), indent=2)+"\n")
    print("Exact conditional certificate checked; the lower-bound premise is unproved.")
