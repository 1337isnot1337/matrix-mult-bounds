"""Check finite graph witnesses; no matching search is used by this verifier."""
from __future__ import annotations

import argparse
from collections import Counter
import gzip
import hashlib
from itertools import combinations, product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULT = ROOT / "results/coordinate-kernel-cap-2026-10-23"
CERTIFICATE = RESULT / "matchings.json.gz"
DEPENDENCIES = {
    "research/ai/2026-10-23-regular-leg-frontier/proof.md",
    "research/ai/2026-10-20-anisotropic-constructions/polynomial_rank_locus.md",
    "research/ai/2026-10-20-graded-quantum-flags/saturation.md",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_sources(record=None):
    if record is None:
        record = json.loads((PACKAGE / "sources.json").read_text())
    require(record["field"] == "C", "Changed field")
    entries = record["local_dependencies"]
    require(len(entries) == len(DEPENDENCIES)
            and {x["path"] for x in entries} == DEPENDENCIES, "Changed source inventory")
    for entry in entries:
        require(hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest()
                == entry["sha256"], "Changed source: " + entry["path"])
    require(hashlib.sha256(CERTIFICATE.read_bytes()).hexdigest()
            == record["certificate_sha256"], "Changed exported certificate")


def graph(subset):
    """Rows (j,L), columns (H,r); a g_(i,z) coefficient has sixteen edges."""
    adjacency = [set() for _ in range(28)]
    for cell in subset:
        require(type(cell) is int and 0 <= cell < 16, "Invalid biform cell")
        i, z = divmod(cell, 4)
        for j, r in product(range(4), repeat=2):
            adjacency[7*j+r+z].add(4*(j+i)+r)
    return adjacency


def source_control():
    """Independent original six-index census and endpoint reversal."""
    actual = [set() for _ in range(16)]
    terms = set()
    for i, j, p, q, r, z in product(range(4), repeat=6):
        term = ((i, p+q, z), (j, p, r+z), (i+j, q, r))
        terms.add(term)
        if p == q == 0:
            actual[4*i+z].add((7*j+r+z, 4*(i+j)+r))
    for cell in range(16):
        expected = {(u, v) for u, neighbors in enumerate(graph([cell])) for v in neighbors}
        require(actual[cell] == expected and len(expected) == 16, "Source graph mismatch")
    reversed_terms = {((3-i, 6-k, 3-z), (3-j, 3-p, 6-l), (6-h, 3-q, 3-r))
                      for (i, k, z), (j, p, l), (h, q, r) in terms}
    require(reversed_terms == terms and len(terms) == 4096, "Endpoint reversal failed")
    return {"original_source_terms": 4096, "endpoint_graph_edges": 256,
            "coefficient_graphs": 16, "endpoint_reversal": True}


def torus_control(coefficients=(1, 16, 256)):
    alpha, beta, gamma = coefficients
    weights = [
        {i*alpha-k*beta+z*gamma for i, k, z in product(range(4), range(7), range(4))},
        {j*alpha+p*beta-l*gamma for j, p, l in product(range(4), range(4), range(7))},
        {-h*alpha+q*beta+r*gamma for h, q, r in product(range(7), range(4), range(4))},
    ]
    require([len(w) for w in weights] == [112]*3, "Source torus weights are not simple")
    count = 0
    for i, j, p, q, r, z in product(range(4), repeat=6):
        total = (i*alpha-(p+q)*beta+z*gamma
                 + j*alpha+p*beta-(r+z)*gamma
                 - (i+j)*alpha+q*beta+r*gamma)
        require(total == 0, "Source torus does not preserve a coefficient")
        count += 1
    return {"coefficients": list(coefficients), "distinct_weights": [112]*3,
            "source_coefficients_checked": count, "all_total_weights_zero": True}


def initial_kernel_control():
    """An exact noncoordinate quotient whose projected rank drops at its torus limit."""
    import sympy as s

    first = list(product(range(2), range(3), range(2)))
    rows = list(product(range(2), range(2), range(3)))
    columns = list(product(range(3), range(2), range(2)))
    ai, bi, ci = ({x: i for i, x in enumerate(basis)}
                  for basis in (first, rows, columns))
    b_pivots = [bi[0, 0, 0], bi[0, 0, 1]]
    c_pivots = [ci[1, 0, 0], ci[1, 0, 1]]
    b_extra, c_extra = bi[0, 1, 0], ci[2, 1, 1]
    b_weights = [j+16*p-256*l for j, p, l in rows]
    c_weights = [-h+16*q+256*r for h, q, r in columns]
    b_orders = [b_weights[b_extra]-b_weights[p] for p in b_pivots]
    c_orders = [c_weights[c_extra]-c_weights[p] for p in c_pivots]
    require(b_orders == [16, 272] and c_orders == [271, 15], "Wrong torus quotient orders")

    def quotient(pivots, extra, value):
        keep = [i for i in range(12) if i not in pivots]
        matrix = s.zeros(10, 12)
        for j, k in enumerate(keep):
            matrix[j, k] = 1
        for k in pivots:
            matrix[keep.index(extra), k] = -value
        return matrix

    projected_ranks = []
    for value in (0, 1):
        left = quotient(b_pivots, b_extra, value)
        right = quotient(c_pivots, c_extra, value)
        require(left.rank() == right.rank() == 10, "Quotient dimension changed")
        flat = s.zeros(100, 12)
        for i, j, p, q, r, z in product(range(2), repeat=6):
            av, bv, cv = ai[i, p+q, z], bi[j, p, r+z], ci[i+j, q, r]
            for u in range(10):
                if left[u, bv]:
                    for v in range(10):
                        flat[10*u+v, av] += left[u, bv]*right[v, cv]
        projected_ranks.append(flat.rank())
    require(projected_ranks == [11, 12], "Torus specialization rank-drop control failed")
    return {"source_a": 2, "quotient_ranks": [10, 10],
            "left_kernel_pivots": b_pivots, "left_extra_coordinate": b_extra,
            "right_kernel_pivots": c_pivots, "right_extra_coordinate": c_extra,
            "left_positive_orders": b_orders, "right_positive_orders": c_orders,
            "projected_rank_at_zero": 11, "projected_rank_at_one": 12,
            "kernel_dimension_at_zero": 1, "kernel_dimension_at_one": 0}


def check_witness(subset, witness):
    adjacency = graph(subset)
    require(isinstance(witness, list) and len(witness) in (24, 25),
            "Invalid matching size")
    require(all(isinstance(edge, list) and len(edge) == 2
                and all(type(v) is int and 0 <= v < 28 for v in edge)
                for edge in witness), "Invalid matching edge")
    left = {u for u, v in witness}
    right = {v for u, v in witness}
    require(len(left) == len(right) == len(witness), "Matching repeats a vertex")
    require(all(v in adjacency[u] for u, v in witness), "Matching edge absent from source")
    if len(witness) == 25:
        return "matching_25"

    # Any cover of size24 chooses exactly one endpoint of every matched edge;
    # no unmatched vertex may be chosen. x_i=1 means choose its left endpoint.
    li = {u: i for i, (u, v) in enumerate(witness)}
    ri = {v: i for i, (u, v) in enumerate(witness)}
    chosen_left = set()
    chosen_right = set()
    implications = []
    for u, neighbors in enumerate(adjacency):
        for v in neighbors:
            if u not in li:
                require(v in ri, "Unmatched source edge")
                chosen_right.add(ri[v])
            elif v not in ri:
                chosen_left.add(li[u])
            else:
                # Cover u or v: x_(ri[v])=1 forces x_(li[u])=1.
                implications.append((ri[v], li[u]))
    changed = True
    while changed:
        before = (len(chosen_left), len(chosen_right))
        for antecedent, consequent in implications:
            if antecedent in chosen_left:
                chosen_left.add(consequent)
            if consequent in chosen_right:
                chosen_right.add(antecedent)
        changed = before != (len(chosen_left), len(chosen_right))
    require(not chosen_left & chosen_right, "Conflicting cover implications")
    require(len(chosen_left | chosen_right) == 24, "Cover is not uniquely forced")
    require(len(chosen_left) in (0, 24), "Minimum cover uses both sides")
    cover_left = {witness[i][0] for i in chosen_left}
    cover_right = {witness[i][1] for i in chosen_right}
    require(all(u in cover_left or v in cover_right
                for u, neighbors in enumerate(adjacency) for v in neighbors),
            "Forced cover misses an edge")
    return "unique_left_24" if chosen_left else "unique_right_24"


def check_certificate(record=None):
    if record is None:
        record = json.loads(gzip.decompress(CERTIFICATE.read_bytes()))
    require(record["scope"] == "Every ten-coordinate biform subspace; coordinate kernels only",
            "Changed certificate scope")
    entries = record["witnesses"]
    require(len(entries) == 8008, "Incomplete ten-subset census")
    counts = Counter()
    for subset, entry in zip(combinations(range(16), 10), entries):
        require(entry["cells"] == list(subset), "Missing, repeated or reordered subset")
        counts[check_witness(subset, entry["matching"])] += 1
    require(counts == {"matching_25": 7744, "unique_left_24": 132,
                       "unique_right_24": 132}, "Changed matching census")
    return dict(sorted(counts.items()))


def verify(record=None):
    check_sources()
    summary = {"proof_status": "proof-written-unreviewed", "independent_review": False,
               "improves_omega": False, "target_constructed": False,
               "source_control": source_control(), "matching_census": check_certificate(),
               "source_torus": torus_control(), "torus_limit_control": initial_kernel_control(),
               "ten_coordinate_subspaces": 8008,
               "mixed_pairs_closed_with_coordinate_kernels": 16,
               "mixed_pairs_closed_by_written_torus_transfer": 16}
    if record is None:
        record = json.loads((RESULT / "verification.json").read_text())
    require(record == summary, "Changed verification summary or inflated scope")
    return summary


if __name__ == "__main__":
    argparse.ArgumentParser(description=__doc__).parse_args()
    print(json.dumps(verify(), sort_keys=True))
