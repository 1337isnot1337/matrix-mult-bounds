"""Exact controls for the written rank-three Hankel obstruction.

Finite controls do not formalize Borel fixed points or the dimension proof.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
import sympy as sp


def partitions(total, maximum=None):
    if total == 0:
        yield ()
        return
    for first in range(min(total, maximum or total), 0, -1):
        for rest in partitions(total-first, first):
            yield (first,)+rest


def residual_boxes(lengths, k):
    return sum(max(n-k, 0) for n in lengths[k:])


def ferrers_controls():
    counts = 0
    rows = []
    diagrams = [p for d in range(25) for p in partitions(d)]
    for k in [1, 2, 3]:
        minima = [None, None]
        for p in diagrams:
            counts += 1
            residual = residual_boxes(p, k)
            for c, bound in [(1, (k+1)**2), (2, (k+1)*(k+2))]:
                if residual >= c:
                    if sum(p) < bound:
                        raise ArithmeticError("Ferrers budget failed")
                    if minima[c-1] is None or sum(p) < minima[c-1]["dimension"]:
                        minima[c-1] = {"dimension": sum(p), "diagram": list(p)}
        rows.append({"parameter_rank": k, "minimum_one_box": minima[0],
                     "minimum_two_boxes": minima[1]})
    return {"all_partitions_of_sizes": [0, 24], "diagrams": len(diagrams),
            "rank_diagram_cases": counts, "budgets": rows}


def projection_control(lengths, k):
    m, n = len(lengths), max(lengths)
    U = sp.Matrix(m, k, lambda i, j: (i+1)**j)
    V = sp.Matrix(n, k, lambda i, j: (i+2)**j)
    jacobian = []
    for i, width in enumerate(lengths):
        for j in range(width):
            row = [0]*((m+n)*k)
            for s in range(k):
                row[i*k+s] = V[j, s]
                row[m*k+j*k+s] = U[i, s]
            jacobian.append(row)
    rank = sp.Matrix(jacobian).rank()
    codimension = sum(lengths)-rank
    if codimension != residual_boxes(lengths, k):
        raise ArithmeticError("Generic-flag tangent control failed")
    return {"diagram": list(lengths), "parameter_rank": k,
            "U": [list(U.row(i)) for i in range(m)],
            "V": [list(V.row(i)) for i in range(n)],
            "dimension": sum(lengths), "jacobian_rank": rank,
            "image_codimension": codimension}


def coordinate_section(omitted):
    for s in range(8):
        support = [j for j in [s-1, s+9] if 0 <= j <= 15]
        normal = [2*s, 2*s+1]
        if set(support+normal).isdisjoint(omitted):
            break
    else:
        raise ArithmeticError("Coordinate section lacks a transverse control")
    positions = [(i, j) for i in range(8) for j in range(9) if i+j in support]
    rows = sorted({i for i, _ in positions})
    columns = sorted({j for _, j in positions})
    if len(positions) != 7 or len(rows) != 7 or len(columns) != 7:
        raise ArithmeticError("Rank-seven partial permutation failed")
    order = [columns.index(next(j for a, j in positions if a == i)) for i in rows]
    inversions = sum(order[i] > order[j] for i in range(7) for j in range(i+1, 7))
    return {"omitted_coordinates": list(omitted), "annihilator_monomial_index": s,
            "unit_moment_indices": support, "normal_coordinate_indices": normal,
            "minor_rows": rows, "minor_columns": columns,
            "minor_determinant": (-1)**inversions}


def reduced_conormal_control():
    z = sp.symbols("z")
    roots = range(-3, 4)
    qpoly = sp.Poly(sp.prod(z-t for t in roots), z)
    q = [qpoly.nth(j) for j in range(8)]
    h = [sum(t**j for t in roots) for j in range(16)]
    H = sp.Matrix(8, 9, lambda i, j: h[i+j])
    left = H.T.nullspace()
    right = H.nullspace()
    if len(left) != 1 or len(right) != 2:
        raise ArithmeticError("Reduced rank-seven control failed")
    def multiply(a, b):
        return [sum(a[i]*b[j] for i in range(len(a)) for j in range(len(b))
                    if i+j == d) for d in range(len(a)+len(b)-1)]
    normals = [multiply(list(left[0]), list(r)) for r in right]
    squared = multiply(q, q)
    expected = [squared+[0], [0]+squared]
    if sp.Matrix(normals+expected).rank() != 2:
        raise ArithmeticError("Conormal product space failed")
    return {"roots": list(roots), "moments": h, "annihilator": q,
            "hankel_rank": 7, "leading_seven_minor": H[:7, :7].det(),
            "conormal_basis": normals, "q_squared_basis": expected}


def applications():
    result = []
    for x, y in [(28, 31), (29, 30)]:
        result.append({"target": [x, y, 31], "source": [8, 9],
                       "source_leg_dimension": 1152, "long_leg_loss": 475,
                       "parameter_rank": 3, "lift_rank_upper_bound": 568,
                       "strict_rank_threshold": 576, "hankel_rank_upper_bound": 7,
                       "first_parameter_dimension": x*y,
                       "minimum_symbol_image_dimension": (x*y+71)//72,
                       "maximum_symbol_image_dimension": 16,
                       "required_projection_dimension": 20,
                       "ordinary_restriction_excluded_by_written_proof": True})
    return result


def report():
    return {
        "proof_status": "proof-written-unreviewed",
        "ferrers": ferrers_controls(),
        "projection_controls": [projection_control(p, k) for p, k in [
            ((4, 4, 4, 4), 3), ((5, 5, 5, 5), 3),
            ((5, 5, 5, 4), 3), ((4, 4, 4), 2)]],
        "coordinate_sections": [coordinate_section(omitted) for c in range(4)
                                for omitted in itertools.combinations(range(16), c)],
        "reduced_conormal": reduced_conormal_control(),
        "section_dimension_contradictions": [
            {"codimension_of_W": c, "putative_component_dimension_lower": 14-c,
             "annihilator_incidence_dimension_upper": c+5}
            for c in [1, 2, 3]],
        "applications": applications(),
        "M30": {"parameter_rank": 2, "lift_rank_upper_bound": 564,
                 "rank_three_lift_upper_bound": 594,
                 "required_projection_dimension": 12,
                 "symbol_image_dimension_interval": [13, 16],
                 "excluded_by_this_argument": False},
        "singular_degenerations_excluded": False,
        "independent_review": False, "improves_omega": False,
    }


def exact_integer(value):
    if not isinstance(value, sp.Integer):
        raise TypeError("The exact control export expected an integer")
    return int(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    data = report()
    args.output.write_text(json.dumps(data, indent=2, default=exact_integer)+"\n")
    print(f"Checked {data['ferrers']['rank_diagram_cases']} Ferrers cases and "
          f"{len(data['coordinate_sections'])} coordinate sections; two written ordinary exclusions, M30 open.")
