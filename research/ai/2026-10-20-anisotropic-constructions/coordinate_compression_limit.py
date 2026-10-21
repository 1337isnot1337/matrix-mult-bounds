"""Exact row-collision certificates for common physical coordinate codes."""

from itertools import product
import json
from pathlib import Path


def selected_coordinate(vertices, edge):
    u, v = edge
    i, q = vertices[u]
    p, s = vertices[v]
    return [i, q + p, s]


def validate_vertices(a, b, vertices):
    if a < 1 or b < 1 or not vertices:
        raise ValueError("Positive dimensions and a nonempty code are required")
    if len({tuple(v) for v in vertices}) != len(vertices):
        raise ValueError("The physical vertices must be distinct")
    if any(len(v) != 2 or not all(isinstance(x, int) for x in v)
           or not (0 <= v[0] < a and 0 <= v[1] < b) for v in vertices):
        raise ValueError("A physical vertex is outside the source grid")


def find_collision(a, b, vertices):
    validate_vertices(a, b, vertices)
    seen = {}
    for edge in product(range(len(vertices)), repeat=2):
        coordinate = tuple(selected_coordinate(vertices, edge))
        if coordinate in seen:
            return {"first_target_edge": list(seen[coordinate]),
                    "second_target_edge": list(edge),
                    "common_source_coordinate": list(coordinate)}
        seen[coordinate] = edge
    return None


def verify_collision(a, b, vertices, certificate):
    validate_vertices(a, b, vertices)
    first, second = certificate["first_target_edge"], certificate["second_target_edge"]
    if first == second or any(len(edge) != 2 or any(
            not isinstance(v, int) or not (0 <= v < len(vertices)) for v in edge)
            for edge in (first, second)):
        raise ArithmeticError("The collision needs two distinct target matrix units")
    one = selected_coordinate(vertices, first)
    two = selected_coordinate(vertices, second)
    if one != two or one != certificate["common_source_coordinate"]:
        raise ArithmeticError("The two source coordinates do not coincide")
    return True


def integer_ceiling(a, b):
    return max(n for n in range(1, a * b + 1)
               if ((n + a - 1) // a) * ((n + b - 1) // b) <= a + b - 1)


def report():
    grid = list(product(range(8), repeat=2))
    codes = [grid[:27], sorted(grid, key=lambda v: (v[0]+v[1], v))[:27],
             sorted(grid, key=lambda v: ((17*v[0]+29*v[1]) % 67, v))[:27]]
    records = []
    for vertices in codes:
        certificate = find_collision(8, 8, vertices)
        if certificate is None:
            raise AssertionError("A code above the proved ceiling was injective")
        verify_collision(8, 8, vertices, certificate)
        records.append({"vertices": vertices, "collision": certificate,
                        "exact_collision_replayed": True})
    controls = {
        "extreme_M4": [(0, 7), (1, 7), (6, 0), (7, 0)],
        "product_M12": list(product((0, 1, 6, 7), (0, 2, 4))),
    }
    for vertices in controls.values():
        if find_collision(8, 8, vertices) is not None:
            raise AssertionError("An exact seed control lost row injectivity")
    return {"source_lengths": [8, 8], "common_coordinate_code_ceiling": integer_ceiling(8, 8),
            "required_M27_ceiling_product": 16, "available_long_coordinates": 15,
            "collision_certificates": records,
            "seed_injectivity_controls": controls,
            "arbitrary_monomial_maps_excluded": False,
            "general_restrictions_excluded": False,
            "new_exponent_established": False}


if __name__ == "__main__":
    output = Path(__file__).resolve().parents[3] / "results" / "anisotropic-constructions-2026-10-20" / "coordinate-compression-limit.json"
    output.write_text(json.dumps(report(), indent=2) + "\n")
    print(output)
