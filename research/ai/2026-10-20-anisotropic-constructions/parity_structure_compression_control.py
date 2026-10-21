"""Exact standard-library A(2,2) -> M(2,2,2) physical-compression control."""

from collections import Counter
from itertools import product


def maps():
    """Rows E00,E01,E10,E11; columns use common F(i,k,s) order."""
    coordinates = ((0, 1, 1), (0, 2, 0), (1, 0, 1), (1, 1, 0))
    return [[(row, (i * 3 + k) * 2 + s, 1) for row, (i, k, s) in enumerate(coordinates)]
            for _ in range(3)]


def contract(selected_maps):
    columns = []
    for leg in selected_maps:
        active = {}
        for row, col, coefficient in leg:
            active.setdefault(col, []).append((row, coefficient))
        columns.append(active)
    image = Counter()
    for i, j, p, q, r, s in product(range(2), repeat=6):
        indices = ((i * 3 + p + q) * 2 + s, (p * 3 + r + s) * 2 + j,
                   (r * 3 + i + j) * 2 + q)
        for x, y, z in product(*(columns[axis].get(indices[axis], ()) for axis in range(3))):
            image[(x[0], y[0], z[0])] += x[1] * y[1] * z[1]
    return {key: value for key, value in image.items() if value}


def verify(selected_maps=None):
    selected_maps = maps() if selected_maps is None else selected_maps
    expected = {(2 * i + j, 2 * j + k, 2 * k + i): 1 for i, j, k in product(range(2), repeat=3)}
    if contract(selected_maps) != expected:
        raise ValueError("The complete physical-compression control is not M2")
    # The physical core is on vertices (i,q)=(0,1),(1,0), indices1,2.
    selected_vertices = (1, 2)
    for leg in selected_maps:
        for row in range(4):
            physical = [[0] * 4 for _ in range(4)]
            for output_row, column, coefficient in leg:
                if output_row != row:
                    continue
                s = column % 2
                k = column // 2 % 3
                i = column // 6
                for p in range(2):
                    q = k - p
                    if 0 <= q < 2:
                        physical[2 * i + q][2 * p + s] += coefficient
            compressed = [physical[i][j] for i, j in product(selected_vertices, repeat=2)]
            if compressed != [int(k == row) for k in range(4)]:
                raise ValueError("A physical top-block identity failed")
    return {"source": [2, 2], "target_vertices": [2, 2, 2], "source_dimension": 12,
            "target_dimensions": [4, 4, 4], "source_terms_checked": 64,
            "complete_target_coefficients_checked": 64, "target_nonzero_coefficients": 8,
            "physical_frame_permutation": [1, 2, 0, 3],
            "all_three_physical_top_blocks_exact": True,
            "complete_integer_tensor_identity": True, "new_exponent_established": False}


if __name__ == "__main__":
    import json
    print(json.dumps(verify(), indent=2))
