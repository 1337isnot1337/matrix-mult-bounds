"""Exact output-collision ansatz for mixed-target one-parameter degenerations.

Input legs use coordinate selections/permutations. Each output coordinate
may be a sum of source output coordinates. SAT witnesses are replayed by
an independent coefficient loop; UNSAT is a solver result in this ansatz.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from math import lcm
import hashlib
import json
import os
from pathlib import Path


def points(m):
    return [(a, degree - a) for degree in range(m) for a in range(degree + 1)]


def verify_witness(witness):
    m, B = witness["m"], witness["B"]
    A = witness.get("source_A", m)
    if not isinstance(m, int) or not isinstance(B, int) or m < 1 or B < 1:
        raise ArithmeticError("invalid source dimensions")
    coordinates = points(m)
    xp, yp = witness["source_x_indices"], witness["source_y_indices"]
    wx, wy, wz = (witness["weights"][axis] for axis in ("x", "y", "z"))
    n = len(coordinates)
    if [len(xp), len(yp), len(wx), len(wy), len(wz),
            len(witness["output_source_indices"])] != [m, n, m, n, n, n]:
        raise ArithmeticError("incorrect coordinate or weight lengths")
    if any(not isinstance(v, int) for row in (xp, yp, wx, wy, wz) for v in row):
        raise ArithmeticError("integer coordinates and weights required")
    if any(len(row) != len(set(row)) for row in witness["output_source_indices"]):
        raise ArithmeticError("duplicate source index in an output sum")
    output = [set(row) for row in witness["output_source_indices"]]
    if len(set(xp)) != m or any(not 0 <= v < A for v in xp) or len(set(yp)) != len(coordinates):
        raise ArithmeticError("noninjective input maps")
    if any(not 0 <= value < B for value in yp):
        raise ArithmeticError("invalid input coordinate")
    if any(not 0 <= value < B + A - 1 for row in output for value in row):
        raise ArithmeticError("invalid output coordinate")
    retained = positive = checked = 0
    for p in range(m):
        for y, (a, b) in enumerate(coordinates):
            for z, (c, d) in enumerate(coordinates):
                expected = int(a + b + c + d == m - 1 and p == a + c)
                actual = int(xp[p] + yp[y] in output[z])
                weight = wx[p] + wy[y] + wz[z]
                checked += 1
                if actual and weight < 0:
                    raise ArithmeticError("negative supported coefficient")
                if weight == 0 and actual != expected:
                    raise ArithmeticError("incorrect leading coefficient")
                if expected and weight != 0:
                    raise ArithmeticError("desired coefficient not weight zero")
                if actual and weight == 0:
                    retained += 1
                if actual and weight > 0:
                    positive += 1
    return {"coefficients_checked": checked, "retained_terms": retained,
            "discarded_positive_terms": positive, "coefficient_verified": True}


def search(m, B, timeout_ms=60000, seed=0, slope=1, query_path=None, source_A=None,
           capacity_cuts=False):
    import z3

    D = m - 1
    coordinates = points(m)
    N = len(coordinates)
    A = source_A if source_A is not None else m
    s = z3.Solver()
    s.set(timeout=timeout_ms, random_seed=seed)
    xp = [z3.Int(f"xp_{p}") for p in range(m)]
    yp = [z3.Int(f"yp_{i}") for i in range(N)]
    eta = [z3.Real(f"eta_{i}") for i in range(m)]
    s.add(*[z3.And(v >= 0, v < A) for v in xp], z3.Distinct(*xp))
    s.add(*[z3.And(v >= 0, v < B) for v in yp], z3.Distinct(*yp))
    s.add(eta[0] == 0)
    capacity_metadata = None
    if capacity_cuts:
        import collision_combinatorics as combinatorics

        s.add(xp[0] < xp[-1])  # Reflect both source inputs if necessary.
        active = []
        for z, (gamma, delta) in enumerate(coordinates):
            sector = m-gamma-delta
            for i, (a, b) in enumerate(coordinates):
                if a+b+1 == sector:
                    active.append((z, yp[i]+xp[a+gamma]))
        for index, (z, value) in enumerate(active):
            for other_z, other_value in active[index+1:]:
                if z != other_z:
                    s.add(value != other_value)
        capacity_metadata = {"active_sets_disjoint": True,
                             "excess_capacity": A+B-1-N}
        if A == m and B == N:
            candidates = (combinatorics.endpoint_candidates(m) if m >= 6 else
                          combinatorics.normalized_permutations(m, m-1))
            s.add(z3.Or(*[z3.And(*[xp[i] == value for i, value in enumerate(candidate)])
                          for candidate in candidates]))
            capacity_metadata["normalized_shared_candidates"] = len(candidates)
    count = 0
    for z, (gamma, delta) in enumerate(coordinates):
        sector = m - gamma - delta
        for i, (alpha, beta) in enumerate(coordinates):
            if alpha + beta + 1 != sector:
                continue
            wanted_p = alpha + gamma
            wanted_k = yp[i] + xp[wanted_p]
            for j, (a, b) in enumerate(coordinates):
                other_sector = a + b + 1
                for p in range(m):
                    if other_sector == sector and p == a + gamma:
                        continue  # Another desired coefficient may share this output coordinate.
                    weight = slope * (p - a - gamma) + eta[other_sector - 1] - eta[sector - 1]
                    s.add(z3.Implies(wanted_k == yp[j] + xp[p], weight > 0))
                    count += 1
    query = s.to_smt2()
    if query_path:
        query_path.write_text(query)
    result = s.check()
    report = {"m": m, "source_A": A, "B": B, "N": N, "slope": slope,
              "solver": z3.get_version_string(), "solver_seed": seed,
              "timeout_ms": timeout_ms, "collision_implications": count,
              "query_sha256": hashlib.sha256(query.encode()).hexdigest(),
              "result": str(result), "unrestricted_nonexistence_claim": False,
              "scope": "Coordinate injections on both input legs, arbitrary output-coordinate sums, target-compatible affine internal weights."}
    if capacity_metadata is not None:
        report["capacity_cuts"] = capacity_metadata
    if result == z3.sat:
        model = s.model()
        xi = [model.eval(v).as_long() for v in xp]
        yi = [model.eval(v).as_long() for v in yp]
        offsets = [Fraction(model.eval(v).numerator_as_long(), model.eval(v).denominator_as_long()) for v in eta]
        scale = lcm(*(value.denominator for value in offsets))
        offsets = [int(value * scale) for value in offsets]
        wx = [slope * p * scale for p in range(m)]
        wy = [-slope * a * scale + offsets[a+b] for a, b in coordinates]
        wz = [-slope * c * scale - offsets[D-c-d] for c, d in coordinates]
        output = []
        for c, d in coordinates:
            sector = m - c - d
            output.append(sorted({yi[i] + xi[a+c] for i, (a, b) in enumerate(coordinates)
                                  if a + b + 1 == sector}))
        witness = {"m": m, "source_A": A, "B": B, "source_x_indices": xi,
                   "source_y_indices": yi, "output_source_indices": output,
                   "weights": {"x": wx, "y": wy, "z": wz}}
        report["witness"] = witness
        report["verification"] = verify_witness(witness)
    elif result == z3.unknown:
        report["reason_unknown"] = s.reason_unknown()
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--m", type=int, default=4)
    parser.add_argument("--B", type=int)
    parser.add_argument("--source-A", type=int)
    parser.add_argument("--capacity-cuts", action="store_true")
    parser.add_argument("--timeout-ms", type=int, default=60000)
    parser.add_argument("--seed", type=int)
    parser.add_argument("--slope", type=int, default=1)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    seed = args.seed if args.seed is not None else int.from_bytes(os.urandom(4), "big") & 0x7fffffff
    B = args.B if args.B is not None else args.m*(args.m+1)//2
    args.output.parent.mkdir(parents=True, exist_ok=True)
    result = search(args.m, B, args.timeout_ms, seed, args.slope,
                    args.output.with_suffix(".smt2"), source_A=args.source_A,
                    capacity_cuts=args.capacity_cuts)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: value for key, value in result.items() if key != "witness"}, indent=2))
