"""Independent rational replay of the finite T4 existence certificate.

This implementation reads only the certificate. It constructs all 400
coefficients directly from the 50 source terms and obtains the selected
Jacobian columns by exact integer finite differences. Every variable occurs
linearly in each polynomial, so these differences are exact derivatives.
"""
from fractions import Fraction
from pathlib import Path
import argparse
import hashlib
import json


def replay(path):
    raw = path.read_bytes()
    data = json.loads(raw)
    center = data["center_numerators"]
    denominator = data["center_denominator"]
    chosen = data["free_coordinate_indices"]
    inverse = data["inverse_numerators"]
    inv_den = data["inverse_denominator"]
    nodes = [(a, p-a) for p in range(4) for a in range(p+1)]
    yw, zw = (-1, -1, 0, 1), (-1, 0, 1, 1)
    positions, desired = [], []
    for x in range(4):
        for y, (a, b) in enumerate(nodes):
            for z, (c, d) in enumerate(nodes):
                if yw[a+b]+zw[c+d] <= 0:
                    positions.append(100*x+10*y+z)
                    desired.append(int(a+b+c+d == 3 and x == a+c))
    assert len(positions) == 172 and sum(desired) == 20
    assert len(center) == 260 and len(set(chosen)) == 172

    def expand(point):
        tensor = [0]*400
        for i in range(5):
            for j in range(10):
                for x in range(4):
                    for y in range(10):
                        input_product = point[5*x+i]*point[20+10*y+j]
                        for z in range(10):
                            tensor[100*x+10*y+z] += input_product*point[120+14*z+i+j]
        return [tensor[k] for k in positions]

    initial = expand(center)
    residual = [v-t*denominator**3 for v, t in zip(initial, desired)]
    columns = []
    for coordinate in chosen:
        shifted = center.copy()
        shifted[coordinate] += 1
        values = expand(shifted)
        columns.append([v-u for v, u in zip(values, initial)])
    common = inv_den*denominator**2
    defect_num = 0
    for i, row in enumerate(inverse):
        row_error = sum(abs((common if i == j else 0)-sum(r*d for r, d in zip(row, col)))
                        for j, col in enumerate(columns))
        defect_num = max(defect_num, row_error)
    delta = Fraction(defect_num, common)
    eta = Fraction(max(abs(sum(r*f for r, f in zip(row, residual))) for row in inverse),
                   inv_den*denominator**3)
    norm = Fraction(max(sum(abs(r) for r in row) for row in inverse), inv_den)
    bound = Fraction(max(abs(v) for v in center), denominator)
    radius = Fraction(data["radius_numerator"], data["radius_denominator"])
    # At most 50 monomials, each contributing six ordered second partials.
    q = delta+norm*300*(bound+radius)*radius
    image = eta+q*radius
    assert delta < 1 and q < 1 and image < radius
    return {
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "source_terms_per_coefficient": 50,
        "full_tensor_positions_per_evaluation": 400,
        "constrained_positions": len(positions),
        "target_nonzero_coefficients": sum(desired),
        "jacobian_method": "exact one-coordinate integer finite differences",
        "selected_jacobian_columns": len(chosen),
        "inverse_defect_bound": str(delta),
        "initial_correction_bound": str(eta),
        "contraction_factor_bound": str(q),
        "image_radius_bound": str(image),
        "radius": str(radius),
        "exact_existence_certificate_passed": True,
        "external_mathematical_review": False,
        "improves_omega": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = replay(args.certificate)
    content = json.dumps(result, indent=2)+"\n"
    if args.output:
        args.output.write_text(content)
    print(content)
