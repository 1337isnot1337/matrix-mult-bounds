"""Exact continuation of the P2 polynomial-quotient construction.

For this *specified* quotient, solve all intertwining equations needed for
P_a -> M(a,m,a) with first map A_(p,q) -> a_(q,p).  Failed quotients do not
exclude other maps or singular degenerations.  Standard-library rational
arithmetic is used throughout.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import product
import argparse
import json
from pathlib import Path


def echelon(rows):
    pivots = {}
    for original in rows:
        row = {col: Fraction(value) for col, value in original.items() if value}
        while row:
            col = min(row)
            value = row[col]
            if col not in pivots:
                pivots[col] = {j: x/value for j, x in row.items()}
                break
            for j, x in pivots[col].items():
                row[j] = row.get(j, 0)-value*x
                if not row[j]:
                    del row[j]
    return pivots


def nullspace(rows, columns):
    pivots = echelon(rows)
    answer = []
    for free in range(columns):
        if free in pivots:
            continue
        vector = {free: Fraction(1)}
        for col in sorted(pivots, reverse=True):
            value = -sum(x*vector.get(j, 0) for j, x in pivots[col].items() if j != col)
            if value:
                vector[col] = value
        answer.append(vector)
    return pivots, answer


def quotient_coordinates(a):
    # C_(z,v) is represented by u^z v^v.  The quotient kernel is
    # (1+u*v) span{u^y v^j : 0<=y<a, 0<=j<a-1}.
    graph = defaultdict(list)
    for y, j in product(range(a), range(a-1)):
        left, right = (y, j), (y+1, j+1)
        graph[left].append(right)
        graph[right].append(left)
    lookup = {}
    components = []
    for coordinate in product(range(2*a-1), range(a)):
        if coordinate in lookup:
            continue
        number = len(components)
        components.append([])
        stack = [(coordinate, 1)]
        while stack:
            vertex, sign = stack.pop()
            if vertex in lookup:
                if lookup[vertex] != (number, sign):
                    raise ArithmeticError("Inconsistent quotient relation")
                continue
            lookup[vertex] = (number, sign)
            components[number].append([list(vertex), sign])
            stack.extend((neighbor, -sign) for neighbor in graph[vertex])
    if len(components) != a*a:
        raise ArithmeticError("Unexpected quotient dimension")
    return lookup, components


def equations(a):
    lookup, components = quotient_coordinates(a)
    n = a*(2*a-1)
    quotient_dimension = len(components)
    actions = {}
    for p, r in product(range(a), repeat=2):
        out = [dict() for _ in range(quotient_dimension)]
        for y, v in product(range(a), repeat=2):
            component, sign = lookup[p+y, v]
            out[component][y*(2*a-1)+r+v] = sign
        actions[p, r] = out
    rows = []
    for q, p, r in product(range(a), repeat=3):
        if q != r:
            for action in actions[p, r]:
                if action:
                    rows.append({q*n+j: value for j, value in action.items()})
        elif q:
            for first, second in zip(actions[p, q], actions[p, 0]):
                row = {q*n+j: value for j, value in first.items()}
                for j, value in second.items():
                    row[j] = row.get(j, 0)-value
                    if not row[j]:
                        del row[j]
                if row:
                    rows.append(row)
    return rows, a*n, actions, components


def analyze(a):
    rows, columns, actions, components = equations(a)
    pivots, basis = nullspace(rows, columns)
    output_vectors = []
    for vector in basis:
        if any(sum(value*vector.get(j, 0) for j, value in row.items()) for row in rows):
            raise ArithmeticError("An exact nullspace vector fails an equation")
        for p in range(a):
            out = {k: sum(value*vector.get(j, 0) for j, value in action.items())
                   for k, action in enumerate(actions[p, 0])}
            output_vectors.append({k: value for k, value in out.items() if value})
    output_rank = len(echelon(output_vectors))
    if len(basis) < a or output_rank < a*a:
        status = "This quotient cannot realize M(a,a,a) with the specified first map."
    else:
        status = "Necessary linear capacity checks pass; no higher-size construction is asserted."
    return {
        "a": a, "source_dimensions": [a*a, a*(2*a-1), a*(2*a-1)],
        "square_target_dimensions": [a*a]*3,
        "first_map": "A_(p,q) -> a_(q,p)",
        "quotient_kernel": "(1+u*v) span{u^y v^j : 0<=y<a, 0<=j<a-1}",
        "quotient_dimension": len(components), "quotient_components": components,
        "linear_equations": len(rows), "unknowns": columns,
        "exact_rational_rank": len(pivots), "middle_mode_dimension": len(basis),
        "combined_output_span_rank": output_rank, "status": status,
        "exact_nullspace_residuals_zero": True, "improves_omega": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sizes", type=int, nargs="+", default=[2, 3, 4])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    reports = [analyze(a) for a in args.sizes]
    if args.output:
        args.output.write_text(json.dumps(reports, indent=2)+"\n")
    print(json.dumps([{k: v for k, v in report.items() if k != "quotient_components"}
                      for report in reports], indent=2))
