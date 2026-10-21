"""Exact mixed-basis multiplication controls for the parity A(5,5) face.

This file constructs restrictions, not exponent improvements.  Run directly
to check every coefficient of the full M9 image and its parity-face image.
No numerical zero tests or external coefficient files are used.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import product
import json
from pathlib import Path

import numpy as np


# Rows are polynomials in increasing monomial degree.
U = np.array([[1, 0, 0, 0, 0],
              [0, 0, 0, 0, 1],
              [0, 1, 0, 0, 0]], dtype=np.int64)
V = np.array([[0, 0, 1, 0, 0],
              [1, 0, 0, 0, 1],
              [0, 1, 0, 1, 0]], dtype=np.int64)
R = np.array([[1, 0, 1, 0, -1, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, -1, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, -1, 0, 1, 0, 1, 0, -1, 0],
              [0, 0, 0, 0, 0, 1, 0, -1, 0],
              [-1, 0, 0, 0, 1, 0, 0, 0, -1]], dtype=np.int64)
SHORT_GRADES = (0, 0, 1)


def convolution_product_matrix():
    """Columns are the nine products U_alpha V_beta, ordered 3*alpha+beta."""
    return np.stack([np.convolve(u, v) for u, v in product(U, V)], axis=1)


def source_coordinates(a=5, b=5):
    m = a + b - 1
    return (list(product(range(a), range(m), range(b))),
            list(product(range(b), range(a), range(m))),
            list(product(range(m), range(b), range(a))))


def source_tensor(a=5, b=5, forbidden=None):
    coordinates = source_coordinates(a, b)
    indices = [{v: i for i, v in enumerate(axis)} for axis in coordinates]
    tensor = {}
    for i, p, r in product(range(a), repeat=3):
        for j, q, s in product(range(b), repeat=3):
            wx, wy, wz = p+q-i-s, r+s-j-p, i+j-q-r
            assert wx+wy+wz == 0
            if forbidden is not None and (wx % 2, wy % 2, wz % 2) == forbidden:
                continue
            point = (indices[0][i, p+q, s],
                     indices[1][j, p, r+s],
                     indices[2][i+j, q, r])
            assert point not in tensor
            tensor[point] = 1
    return tensor


def mixed_m9_maps():
    """Return three integer 81-by-225 restriction maps in matrix-index order.

    Vertices I=(alpha1,beta2), J=(alpha2,beta3), K=(alpha3,beta1).
    X rows have index 9*I+J, Y rows 9*J+K, and Z rows 9*K+I.
    """
    coordinates = source_coordinates()
    maps = [np.zeros((81, 225), dtype=np.int64) for _ in range(3)]
    for a1, b2, a2, b3 in product(range(3), repeat=4):
        row = 9*(3*a1+b2)+(3*a2+b3)
        for col, (i, t, s) in enumerate(coordinates[0]):
            maps[0][row, col] = U[a1, i]*R[3*a2+b2, t]*V[b3, s]
    for a2, b3, a3, b1 in product(range(3), repeat=4):
        row = 9*(3*a2+b3)+(3*a3+b1)
        for col, (j, p, t) in enumerate(coordinates[1]):
            maps[1][row, col] = V[b1, j]*U[a2, p]*R[3*a3+b3, t]
    for a3, b1, a1, b2 in product(range(3), repeat=4):
        row = 9*(3*a3+b1)+(3*a1+b2)
        for col, (t, q, r) in enumerate(coordinates[2]):
            maps[2][row, col] = R[3*a1+b1, t]*V[b2, q]*U[a3, r]
    return maps


def apply_sparse(tensor, maps):
    """Apply the maps with exact Python-integer accumulation."""
    for axis, matrix in enumerate(maps):
        by_column = [[(int(row), int(matrix[row, col]))
                      for row in np.flatnonzero(matrix[:, col])]
                     for col in range(matrix.shape[1])]
        transformed = defaultdict(int)
        for point, value in tensor.items():
            for row, coefficient in by_column[point[axis]]:
                image = point[:axis] + (row,) + point[axis+1:]
                transformed[image] += value*coefficient
        tensor = {point: value for point, value in transformed.items() if value}
    return tensor


def multiplication_tensor(n, grades=None, forbidden=None):
    result = {}
    for i, j, k in product(range(n), repeat=3):
        if forbidden is not None:
            parity = (grades[i] ^ grades[j], grades[j] ^ grades[k],
                      grades[k] ^ grades[i])
            if parity == forbidden:
                continue
        result[n*i+j, n*j+k, n*k+i] = 1
    return result


def scalar_sum_injective(left, right):
    sums = [a+b for a, b in product(left, right)]
    return len(set(sums)) == len(sums)


def cartesian_m8_maps():
    """Monomial M8 control, retained for comparison with the mixed M9 map."""
    aa, cc = (0, 4), (0, 1, 2, 3)
    ff, dd = (0, 1, 2, 3), (0, 4)
    gg, ll = (0, 4), (0, 1, 2, 3)
    assert all(scalar_sum_injective(left, right)
               for left, right in ((aa, cc), (ff, dd), (gg, ll)))
    vertices = (list(product(aa, ff)), list(product(dd, ll)),
                [(c, g) for g in gg for c in cc])
    index = [{v: i for i, v in enumerate(axis)} for axis in source_coordinates()]
    maps = [np.zeros((64, 225), dtype=np.int64) for _ in range(3)]
    for i, (a, f) in enumerate(vertices[0]):
        for j, (d, l) in enumerate(vertices[1]):
            maps[0][8*i+j, index[0][a, f+d, l]] = 1
    for j, (d, l) in enumerate(vertices[1]):
        for k, (c, g) in enumerate(vertices[2]):
            maps[1][8*j+k, index[1][c, d, g+l]] = 1
    for k, (c, g) in enumerate(vertices[2]):
        for i, (a, f) in enumerate(vertices[0]):
            maps[2][8*k+i, index[2][a+c, f, g]] = 1
    grades = [[(f-a) % 2 for a, f in vertices[0]],
              [(d-l) % 2 for d, l in vertices[1]],
              [(g-c) % 2 for c, g in vertices[2]]]
    # All three lists agree for this chosen vertex ordering.
    assert grades[0] == grades[1] == grades[2]
    return maps, grades[0]


def verify():
    product_matrix = convolution_product_matrix()
    assert np.array_equal(R @ product_matrix, np.eye(9, dtype=np.int64))
    assert np.array_equal(product_matrix @ R, np.eye(9, dtype=np.int64))
    for alpha, beta in product(range(3), repeat=2):
        parity = SHORT_GRADES[alpha] ^ SHORT_GRADES[beta]
        assert all(t % 2 == parity for t in np.flatnonzero(R[3*alpha+beta]))
    full, face = source_tensor(), source_tensor(forbidden=(1, 1, 0))
    assert len(full) == 15625 and len(face) == 11725
    maps = mixed_m9_maps()
    grades = [SHORT_GRADES[alpha] ^ SHORT_GRADES[beta]
              for alpha, beta in product(range(3), repeat=2)]
    expected_full = multiplication_tensor(9)
    expected_face = multiplication_tensor(9, grades, (1, 1, 0))
    actual_full = apply_sparse(full, maps)
    actual_face = apply_sparse(face, maps)
    assert actual_full == expected_full
    assert actual_face == expected_face
    assert len(actual_full) == 729 and len(actual_face) == 549
    assert [grades.count(v) for v in (0, 1)] == [5, 4]

    # Keeping equal-grade X entries leaves two independent rectangular blocks.
    x_even = {point: value for point, value in actual_face.items()
              if grades[point[0]//9] == grades[point[0] % 9]}
    assert len(x_even) == 5*5*9 + 4*4*9 == 369
    block_terms = [0, 0]
    for (x, y, z), value in x_even.items():
        i, j = divmod(x, 9)
        jj, k = divmod(y, 9)
        kk, ii = divmod(z, 9)
        assert (i, j, k, value) == (ii, jj, kk, 1)
        assert grades[i] == grades[j]
        block_terms[grades[i]] += 1
    assert block_terms == [225, 144]

    m8_maps, m8_grades = cartesian_m8_maps()
    assert apply_sparse(full, m8_maps) == multiplication_tensor(8)
    assert apply_sparse(face, m8_maps) == multiplication_tensor(8, m8_grades, (1, 1, 0))
    return {
        "claim": "Exact restrictions and controls; no smaller exponent established",
        "source": "A(5,5)",
        "source_format": [225, 225, 225],
        "source_terms": len(full),
        "parity_face_forbidden": [1, 1, 0],
        "parity_face_terms": len(face),
        "U": U.tolist(), "V": V.tolist(), "R": R.tolist(),
        "product_matrix": product_matrix.tolist(),
        "both_inverse_identities_exact": True,
        "full_m9_all_coefficients_exact": True,
        "parity_m9_all_coefficients_exact": True,
        "target_m9_format": [81, 81, 81],
        "target_m9_terms": len(actual_full),
        "target_parity_m9_terms": len(actual_face),
        "target_vertex_grades": grades,
        "map_nonzero_counts": [int(np.count_nonzero(matrix)) for matrix in maps],
        "parity_face_x_even_direct_sum": [[5, 5, 9], [4, 4, 9]],
        "parity_face_x_even_format": [41, 81, 81],
        "parity_face_x_even_terms": block_terms,
        "cartesian_m8_full_and_parity_exact": True,
    }


if __name__ == "__main__":
    report = verify()
    output = Path(__file__).with_name("parity_structure_certificate.json")
    output.write_text(json.dumps(report, indent=2) + "\n")
    saved_maps = mixed_m9_maps()
    np.savez_compressed(Path(__file__).with_name("parity_structure_m9_maps.npz"),
                        A=saved_maps[0], B=saved_maps[1], C=saved_maps[2],
                        x=saved_maps[0], y=saved_maps[1], z=saved_maps[2],
                        U=U, V=V, R=R,
                        vertex_grades=report["target_vertex_grades"])
    print(json.dumps({k: v for k, v in report.items()
                      if k not in {"U", "V", "R", "product_matrix"}}, indent=2))
