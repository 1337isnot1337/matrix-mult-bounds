"""Exact finite controls for the fixed-seed first-cross pencil obstruction."""
import argparse
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT/"results/bulk-partial-2026-10-21"


def source_coefficients():
    return [(6*p+q, 9*y+8-q-v, 4*(8-p-y)+v)
            for p in range(6) for q in range(6) for y in range(4) for v in range(4)]


def exact_seed(old):
    coordinates = [5*i+j for i in range(5) for j in range(5) if abs(i-j) in (1, 2)]
    maps = [{}, {}, {}]
    for ii, i in enumerate(old):
        for jj, j in enumerate(old):
            if 5*i+j in coordinates:
                maps[0][6*(2*ii)+2*jj] = coordinates.index(5*i+j)
        for y in range(2):
            for v in range(2):
                k = 2*y+v
                maps[1][9*y+8-2*ii-v] = 4*i+k
                maps[2][4*(8-2*ii-y)+v] = 5*k+i
    actual = {}
    flattened = sp.zeros(36, 400)
    for a, b, c in source_coefficients():
        if b in maps[1] and c in maps[2]:
            flattened[a, 20*maps[1][b]+maps[2][c]] += 1
            if a in maps[0]:
                point = (maps[0][a], maps[1][b], maps[2][c])
                actual[point] = actual.get(point, 0)+1
    expected = {(coordinates.index(5*i+j), 4*j+k, 5*k+i): 1
                for i in old for j in old if i != j for k in range(4)}
    assert actual == expected
    nonzero_A = [i for i in range(36) if any(flattened.row(i))]
    assert nonzero_A == [6*p+q for p in range(4) for q in range(4)]
    assert flattened.rank() == 16
    # The displayed y=v=0 entries give an identity minor without rank heuristics.
    rows = [6*p+q for p in range(4) for q in range(4)]
    columns = [20*maps[1][8-q]+maps[2][4*(8-p)] for p in range(4) for q in range(4)]
    assert flattened.extract(rows, columns) == sp.eye(16)
    return dict(old_vertices=list(old), exact_target_terms=len(actual),
                pre_A_rank=16, kernel_A_coordinates=[i for i in range(36) if i not in rows],
                identity_minor_rows=rows, identity_minor_columns=columns)


def verify_cross_pencil():
    J = sp.zeros(4)
    for i in range(3):
        J[i, i+1] = 1
    # A=(p,q') with p<4,q'<2; B=(output q'+v,y); C=(v,z).
    actual = {}
    for p in range(4):
        for q in range(2):
            for y in range(4-p):
                for v in range(2):
                    actual[(2*p+q, 4*(q+v)+y, 4*v+p+y)] = 1
    expected = {}
    for p in range(4):
        power = J**p
        for q in range(2):
            for y in range(4):
                for z in range(4):
                    if power[y, z]:
                        for v in range(2):
                            expected[(2*p+q, 4*(q+v)+y, 4*v+z)] = int(power[y, z])
    assert actual == expected and len(actual) == 40
    h_coeff = sp.symbols("h0:4")
    a_coeff = sp.symbols("a0:4")
    b_coeff = sp.symbols("b0:4")
    poly = lambda coefficients: sum((c*J**i for i, c in enumerate(coefficients)), sp.zeros(4))
    h, a, b = map(poly, [h_coeff, a_coeff, b_coeff])
    E = sp.Matrix(4, 4, sp.symbols("e0:16"))
    X0, X1, X2 = E*h*h, -E*h, E
    Z0, Z1 = X0*a+X1*b, X1*a+X2*b
    assert all(sp.expand(x) == 0 for x in Z0+Z1*h)
    X0, X1, X2 = E, -E*h, E*h*h
    Z0, Z1 = X0*a+X1*b, X1*a+X2*b
    assert all(sp.expand(x) == 0 for x in Z1+Z0*h)
    r0, r1, r2, r3 = sp.symbols("r0:4")
    r = poly([r0, r1, r2, r3])
    inverse = poly([1/r0, -r1/r0**2, r1**2/r0**3-r2/r0**2,
                    -r1**3/r0**4+2*r1*r2/r0**3-r3/r0**2])
    assert all(sp.cancel(x) == 0 for x in r*inverse-sp.eye(4))
    sharp = (-J**3).row_join(J**2)
    target = sp.zeros(4, 8)
    for row, column in enumerate([2, 3, 6, 7]):
        target[row, column] = 1
    assert sharp.rank() == 2 and target.rank() == 4
    assert sharp[:, [0, 1, 4, 5]] == sp.zeros(4, 4)
    return dict(exact_nonzero_cross_coefficients=len(actual),
                ambient_cross_coefficient_positions=8*12*8,
                both_unit_cases_symbolically_verified=True,
                generic_unit_inverse_verified=True,
                sharp_source_rank_control=2, required_target_edge_rank=4)


def verify():
    return dict(source="Q(6,4)", target="off-diagonal bulk of M(5,4,5)",
                source_format=[36, 36, 36], target_format=[14, 20, 20],
                exact_seed_controls=[exact_seed((0, 1)), exact_seed((1, 2))],
                first_cross=verify_cross_pencil(),
                scope="fixed monomial leading long row spaces and cross A poles of order at most one",
                excludes_arbitrary_Laurent_families=False, improves_omega=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=RESULTS/"certificate.json")
    args = parser.parse_args()
    result = verify()
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result))
