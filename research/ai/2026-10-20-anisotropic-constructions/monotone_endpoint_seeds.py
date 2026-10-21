"""Exact monomial endpoint seeds; no nonstandard dependencies."""

from collections import Counter
from itertools import product
import json
from pathlib import Path


PROFILE = (1,1,2,2,2,2,2,3,2,2,2,2,2,1,1)


def coordinate_index(a, b, leg, point):
    i, k, s = point
    m = a+b-1
    if leg == 0:
        return (i*m+k)*b+s
    if leg == 1:
        return (s*a+i)*m+k
    return (k*b+s)*a+i


def build_maps(a, b, vertices):
    if len({i for i, _ in vertices}) != len(vertices):
        raise ValueError("The short first indices must be distinct.")
    ordered = sorted(vertices)
    if any(not (0 <= i < a and 0 <= q < b) for i, q in vertices):
        raise ValueError("A vertex is outside the source short ranges.")
    if any(left[1] < right[1] for left, right in zip(ordered, ordered[1:])):
        raise ValueError("The graph must be nonincreasing.")
    n = len(vertices)
    maps = [[], [], []]
    for u, (i, q) in enumerate(vertices):
        for v, (p, s) in enumerate(vertices):
            for leg in range(3):
                maps[leg].append([n*u+v, coordinate_index(a,b,leg,(i,q+p,s)), 1])
    if any(len({col for _, col, _ in entries}) != n*n for entries in maps):
        raise AssertionError("Distinct target units collided on the source.")
    return maps


def contract(a, b, maps):
    lookup = [{column:(row,value) for row,column,value in leg} for leg in maps]
    actual = Counter()
    seen = 0
    for i,p,r in product(range(a), repeat=3):
        for q,s,j in product(range(b), repeat=3):
            physical = ((i,p+q,s),(p,r+s,j),(r,i+j,q))
            columns = [coordinate_index(a,b,leg,point) for leg,point in enumerate(physical)]
            seen += 1
            if all(col in lookup[leg] for leg,col in enumerate(columns)):
                values = [lookup[leg][col] for leg,col in enumerate(columns)]
                actual[tuple(row for row,_ in values)] += values[0][1]*values[1][1]*values[2][1]
    return actual, seen


def target(n, embedding=None):
    indices = range(n) if embedding is None else embedding
    return Counter({(n*i+j,n*j+k,n*k+i):1 for i,j,k in product(indices,repeat=3)})


def verify_case(a, b, vertices, embed=False):
    n = len(vertices)
    maps = build_maps(a,b,vertices)
    actual, seen = contract(a,b,maps)
    if actual != target(n):
        raise AssertionError("The complete monomial matrix tensor identity failed.")
    charges = [i-q for i,q in vertices]
    for u,(i,q) in enumerate(vertices):
        for v,(p,s) in enumerate(vertices):
            if i+s-(q+p) != charges[u]-charges[v]:
                raise AssertionError("A source map violated the claimed torus charge.")
    row = {"source_lengths":[a,b],"vertices":[list(v) for v in vertices],
           "target_size":n,"source_dimensions":[a*b*(a+b-1)]*3,
           "target_dimensions":[n*n]*3,"vertex_charges":charges,
           "maps":maps,"source_terms_checked":seen,
           "exact_nonzero_target_coefficients":len(actual),
           "complete_tensor_identity_exact":True,"all_map_charges_exact":True}
    if embed:
        all_charges = [c for c,count in enumerate(PROFILE) for _ in range(count)]
        selected = [all_charges.index(c+7) for c in charges]
        embedded = [[[27*selected[index//n]+selected[index%n],column,value]
                     for index,column,value in leg] for leg in maps]
        image, checked = contract(a,b,embedded)
        if image != target(27,selected) or checked != seen:
            raise AssertionError("The full-format partial-target embedding failed.")
        row.update({"full_format_dimensions":[778]*3,
                    "full_format_vertex_indices":selected,
                    "full_format_maps":embedded,
                    "full_format_partial_target_exact":True,
                    "full_target_restriction_established":False})
    return row


def report():
    examples = [(2,3,[(0,2),(1,0)],False),
                (4,5,[(0,4),(1,3),(2,3),(3,0)],False),
                (8,8,[(0,7),(1,7),(6,0),(7,0)],False),
                (8,8,[(i,7 if i<4 else 0) for i in range(8)],True)]
    return {"claim":"Monotone physical graphs give exact matrix restrictions.",
            "cases":[verify_case(*case) for case in examples],
            "boundary_slack_units":{"13_to_1":[6,1,7],"1_to_13":[1,13,0]},
            "fixed_other_seed_compatibility_claimed":False,
            "new_exponent_established":False}


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[3]
    path = root / "results/anisotropic-constructions-2026-10-20/monotone-endpoint-seeds.json"
    path.write_text(json.dumps(report(),indent=2)+"\n")
    print(path)
