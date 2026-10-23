"""Accept exported maps by direct source expansion and exact finite-field ranks.

No discovery imports or third-party dependencies. These controls support the
written proof; they do not establish its universal quantifiers.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
from math import comb
from pathlib import Path
import sys

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]
RESULT = ROOT / "results/two-variable-long-legs-2026-10-23"
DEPENDENCIES = {
    "research/ai/2026-10-20-paired-construction/outer_product_injection.md",
    "research/ai/2026-10-21-correction-budget/README.md",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def clean(values, prime):
    return {k: v % prime for k, v in values.items() if v % prime}


def rank(rows, prime):
    pivots = {}
    for original in rows:
        row = clean(original, prime)
        while row:
            lead = min(row)
            if lead not in pivots:
                inv = pow(row[lead], -1, prime)
                pivots[lead] = {k: v*inv % prime for k, v in row.items()}
                break
            scale = row[lead]
            for k, value in pivots[lead].items():
                new = (row.get(k, 0) - scale*value) % prime
                if new:
                    row[k] = new
                else:
                    row.pop(k, None)
    return len(pivots)


def coefficient(c, leg, first, target, shift, column):
    arrays = c[leg + "_stencils"]
    if leg == "c":
        weights = [f[column] for f in c["c_profiles"]]
    elif c["b_mode"] == "polynomial":
        weights = [column**j for j in range(len(arrays))]
    else:
        weights = [pow(root, column, c["prime"]) for root in c["b_roots"]]
    return sum(w*a[first][target][shift+c["D"]]
               for w, a in zip(weights, arrays)) % c["prime"]


def b_window_coordinates(c, q, y, t, k):
    arrays = c["b_stencils"]
    if c["b_mode"] == "polynomial":
        return [sum(comb(d, a)*q**(d-a)*arrays[d][y][t][k+c["D"]]
                    for d in range(a, len(arrays))) % c["prime"]
                for a in range(len(arrays))]
    return [pow(root, q, c["prime"])*arr[y][t][k+c["D"]] % c["prime"]
            for root, arr in zip(c["b_roots"], arrays)]


def basis(c, a, v):
    return v**a if c["b_mode"] == "polynomial" else pow(c["b_roots"][a], v, c["prime"])


def terms(c, leg, small, column):
    n, m, D = c["n"], c["m"], c["D"]
    if column in c[leg + "_exceptions"]:
        # Deliberately nonlocal exceptional images on both legs.
        return [((3*column+2*small+t+1) % n, t, 1+small+3*t) for t in range(m)]
    return [(column-k, t, coefficient(c, leg, small, t, k, column))
            for t in range(m) for k in range(-D, D+1) if 0 <= column-k < n]


def source_slice(c, p, q):
    out = defaultdict(int)
    for y in range(c["m"]):
        for v in range(c["m"]):
            for h, t, b in terms(c, "b", y, q+v):
                for i, u, g in terms(c, "c", v, p+y):
                    out[t, u, h, i] += b*g
    return clean(out, c["prime"])


def channel_slice(c, p, q):
    """Equation (5), independently from the full native source contraction."""
    out = defaultdict(int)
    m, D = c["m"], c["D"]
    for a in range(len(c["b_stencils"])):
        for j, profile in enumerate(c["c_profiles"]):
            left, right = defaultdict(int), defaultdict(int)
            for t in range(m):
                for y in range(m):
                    for k in range(-D, D+1):
                        h = b_window_coordinates(c, q, y, t, k)[a]
                        left[t, -k, y] += h*profile[p+y]
            for u in range(m):
                for v in range(m):
                    for ell in range(-D, D+1):
                        right[u, v, -ell] += basis(c, a, v)*c["c_stencils"][j][v][u][ell+D]
            for (t, dx, dy), x in clean(left, c["prime"]).items():
                for (u, ex, ey), z in clean(right, c["prime"]).items():
                    out[t, u, q+dx+ex, p+dy+ey] += x*z
    return clean(out, c["prime"])


def good_indices(c):
    n, m, D = c["n"], c["m"], c["D"]
    interior = range(m-1+D, n-(m-1+D))
    return ([p for p in interior if all(p+y not in c["c_exceptions"] for y in range(m))],
            [q for q in interior if all(q+v not in c["b_exceptions"] for v in range(m))])


def check_case(c):
    n, m, D, prime = (c[k] for k in ("n", "m", "D", "prime"))
    require(prime in (2, 3, 101), "Unsupported control field")
    ps, qs = good_indices(c)
    require(ps and qs, "Control must have good slices")
    windows = []
    for q in qs:
        for y in range(m):
            for t in range(m):
                for k in range(-D, D+1):
                    h = b_window_coordinates(c, q, y, t, k)
                    window = [coefficient(c, "b", y, t, k, q+v) for v in range(m)]
                    require(all(window[v] == sum(h[a]*basis(c, a, v) for a in range(len(h))) % prime
                                for v in range(m)), "Invalid common window identity")
                    windows.append(dict(enumerate(window)))
    r = rank(windows, prime)
    profiles = [{i: value for i, value in enumerate(f) if i not in c["c_exceptions"]}
                for f in c["c_profiles"]]
    stencil_rows = [dict(enumerate(value for first in a for target in first for value in target))
                    for a in c["c_stencils"]]
    s = rank(profiles, prime)
    require(s == rank(stencil_rows, prime) == len(profiles), "C profiles must be independent")
    require(r == len(c["b_stencils"]) and r*s < m, "No strict channel gap")
    for leg in ("b", "c"):
        columns = [z for z in range(n+m-1) if z not in c[leg + "_exceptions"]]
        require(any(coefficient(c, leg, small, t, 0, columns[0]) !=
                    coefficient(c, leg, small, t, 0, z)
                    for z in columns for small in range(m) for t in range(m)),
                leg.upper() + " control is not variable")
    for p in ps:
        for q in qs:
            require(source_slice(c, p, q) == channel_slice(c, p, q), "Source/channel identity failed")
    rows = [defaultdict(int) for _ in range(n*n)]
    def col(t, u, h, i):
        return ((h*m+t)*m+u)*n+i
    for i in range(n):
        for h in range(n):
            for t in range(m):
                rows[i*n+h][col(t, t, h, i)] = 1
    for p in range(n):
        for q in range(n):
            # An unrestricted, nonlocal first-leg map, shared by direct controls.
            first_terms = [(p, q, 1), ((p+q+1) % n, (2*p+3*q+1) % n, 2),
                           ((3*p+1) % n, (q+2) % n, -1)]
            for (t, u, h, i), value in source_slice(c, p, q).items():
                for a, b, scale in first_terms:
                    rows[a*n+b][col(t, u, h, i)] -= scale*value
    observed = rank(rows, prime)
    lower = len(ps)*len(qs)
    L = m-1+D
    explicit = max(0, n-2*L-m*len(c["b_exceptions"]))*max(0, n-2*L-m*len(c["c_exceptions"]))
    require(observed >= lower >= explicit, "Residual repair bound failed")
    return {"name": c["name"], "prime": prime, "n": n, "m": m, "D": D,
            "window_rank": r, "profile_rank": s, "channels": r*s,
            "good_p": len(ps), "good_q": len(qs), "explicit_lower_bound": explicit,
            "good_slice_lower_bound": lower, "residual_rank_mod_prime": observed,
            "checked_channel_slices": lower,
            "checked_windows": len(windows), "both_maps_variable": True}


def boundary_control(c):
    require(c["m"] == 4 and len(c["b_stencils"]) == len(c["c_profiles"]) == 2,
            "Changed equality boundary")
    p, q = (indices[0] for indices in good_indices(c))
    direct = source_slice(c, p, q)
    require(direct == channel_slice(c, p, q), "Boundary coefficient identity failed")
    symbol = [defaultdict(int) for _ in range(4)]
    for (t, u, h, i), value in direct.items():
        symbol[t][u] += value  # X=Y=1; full rank certifies the rational symbol rank.
    observed = rank(symbol, c["prime"])
    require(observed == 4, "Equality control must attain full symbol rank")
    return {"width": 4, "channels": 4, "symbol_rank_at_X1_Y1_F101": observed,
            "strict_hypothesis_holds": False}


def check_sources(record=None):
    record = record if record is not None else json.loads((PACKAGE / "sources.json").read_text())
    require(record["base_commit"] == "3008d704d1797da02f7bf3f29cc1dbd4c0e7fa93", "Changed baseline")
    entries = record["local_dependencies"]
    require(len(entries) == len(DEPENDENCIES) and {e["path"] for e in entries} == DEPENDENCIES,
            "Changed dependency inventory")
    for e in entries:
        require(hashlib.sha256((ROOT / e["path"]).read_bytes()).hexdigest() == e["sha256"],
                "Source pin mismatch: " + e["path"])
    return len(entries)


def verify(record=None, progress=None):
    record = record if record is not None else json.loads((RESULT / "maps.json").read_text())
    require(len(record["cases"]) == 6 and len({c["name"] for c in record["cases"]}) == 6,
            "Changed finite control inventory")
    pins = check_sources()
    cases = []
    for c in record["cases"]:
        cases.append(check_case(c))
        if progress is not None:
            progress(c["name"] + ": pass")
    return {"status": "pass", "source_pins": pins,
            "cases": cases,
            "boundary": boundary_control(record["boundary"]),
            "scope": "Finite exact controls only; universal theorem is written and unreviewed.",
            "improves_omega": False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = json.dumps(verify(progress=lambda message: print(message, file=sys.stderr, flush=True)),
                        indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report)
    else:
        print(report)
