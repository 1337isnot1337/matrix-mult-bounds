"""Exact Cartan character screens at a=5; no matrix degeneration is constructed."""
from itertools import product
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from torus import multiply, positive_factors


def cross_character(left, right):
    return multiply(left, right[::-1])


def full_leg_dual():
    p = multiply(multiply([1]*5, [1]*5), [1]*9)
    pairs, nodes = positive_factors(p, 15, 15)
    short = [1, 2, 3, 3, 3, 2, 1]
    long = [1, 1, 1, 2, 2, 1, 2, 2, 1, 1, 1]
    assert pairs == [[short, long], [long, short]]
    # Normalize the long vertex to weights 0..10, the short one to 2..8.
    # The third vertex is forced into weights 2..8 by the support width.
    rows, rhs = [], []
    for other, offset, weights in ((long, 0, (-8, -7, 7, 8)), (short, 2, (0,))):
        for weight in weights:
            rows.append([other[i+2-offset-weight] if 0 <= i+2-offset-weight < len(other)
                         else 0 for i in range(7)])
            rhs.append(p[weight+8])
    assert [sum(row[i] for row in rows) for i in range(7)] == [3]*7
    assert sum(rhs) == 33
    return {"full_leg_dimension": 225, "vertex_dimensions": [15, 15],
            "positive_factor_pairs": pairs, "coefficient_search_nodes": nodes,
            "third_vertex_weight_range": [2, 8], "dual_constraint_rows": rows,
            "dual_right_sides": rhs, "sum_of_rows": [3]*7, "sum_of_right_sides": 33,
            "maximum_third_vertex_dimension_upper_bound": 11}


def almost_full_leg():
    p = multiply(multiply([1]*5, [1]*5), [1]*9)
    records = []
    for k in range(17):
        q = p.copy()
        q[k] -= 1
        shift = 0
        while q[0] == 0:
            shift += 1
            q.pop(0)
        while q[-1] == 0:
            q.pop()
        pairs, nodes = positive_factors(q, 14, 16)
        assert not pairs
        records.append({"deficit_exponent": k, "reduced_coefficients": q,
                        "monomial_shift": shift, "coefficient_search_nodes": nodes,
                        "positive_factor_pairs": pairs})
    return {"target_leg_dimension": 224, "vertex_dimensions": [14, 16],
            "records": records, "total_coefficient_search_nodes": sum(r["coefficient_search_nodes"] for r in records),
            "surviving_pair_characters": 0}


def candidate_family(a):
    d, radius = a-1, 2*a-2
    u = [1, 1]+[2]*(2*a-5)+[1, 1]
    w = [1]+[2]*(a-2)+[1]+[2]*(a-2)+[1]
    p = multiply(multiply([1]*a, [1]*a), [1]*(2*a-1))
    pairs = [cross_character(u, u), cross_character(u, w), cross_character(w, u)]
    assert all(len(pair) == len(p) and all(x <= y for x, y in zip(pair, p)) for pair in pairs)
    b_weight = [(j, q, k) for j, q, k in product(range(a), range(a), range(2*a-1))
                if k-j-q == -d]
    c_weight = [(k, q, r) for k, q, r in product(range(2*a-1), range(a), range(a))
                if k-q-r == -d]
    # The source A extreme weight has i=s=0 and p=q=D. Its selected
    # B,C block has exactly a ones in distinct rows and columns.
    entries = [(b_weight.index((j, d, j)), c_weight.index((j, d, j))) for j in range(a)]
    assert len(set(r for r, c in entries)) == len(set(c for r, c in entries)) == a
    source_dimension = len(b_weight)
    target_dimension = pairs[1][radius-d]
    assert source_dimension == p[radius-d]
    lost = source_dimension-target_dimension
    lower = a-2*lost
    volume = sum(u)**2*sum(w)
    return {"a": a, "shape": [sum(u), sum(u), sum(w)], "U_and_V": u, "W": w,
            "source_character": p, "target_pair_characters": pairs,
            "extreme_source_slice_rank": a, "extreme_source_slice_nonzero_positions": entries,
            "other_source_weight_dimension": source_dimension,
            "other_target_weight_dimension": target_dimension, "ordinary_compressed_rank_lower_bound": lower,
            "target_extreme_slice_rank": w[d], "ordinary_extreme_slice_test_excludes": w[d] < lower,
            "passes_finite_exponent_threshold": 216*volume > (6*a-2)**4,
            "constructed": False}


def report():
    full, almost = full_leg_dual(), almost_full_leg()
    family = [candidate_family(a) for a in (3, 4, 5)]
    assert [r["ordinary_extreme_slice_test_excludes"] for r in family] == [False, True, False]
    assert 635040**449 > 28**1800
    return {"field": "C", "source_action": "Specified diagonal Cartan action",
            "full_leg_screen": full, "one_missing_dimension_screen": almost, "candidate_family": family,
            "excluded_a5_previously_unexcluded_constant_shapes_with_this_action": [[13, 14, 16], [13, 15, 15], [14, 15, 15]],
            "remaining_shape_with_exhibited_necessary_characters": [14, 14, 15],
            "conditional_exponent_upper_bound": "449/200",
            "conditional_integer_certificate": "635040**449 > 28**1800",
            "required_matrix_degeneration_constructed": False, "general_degeneration_excluded": False,
            "new_exponent_established": False}


if __name__ == "__main__":
    print(json.dumps(report(), indent=2))
