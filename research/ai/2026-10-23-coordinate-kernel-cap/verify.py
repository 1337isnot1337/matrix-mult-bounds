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
               "ten_coordinate_subspaces": 8008,
               "mixed_pairs_closed_with_coordinate_kernels": 16}
    if record is None:
        record = json.loads((RESULT / "verification.json").read_text())
    require(record == summary, "Changed verification summary or inflated scope")
    return summary


if __name__ == "__main__":
    argparse.ArgumentParser(description=__doc__).parse_args()
    print(json.dumps(verify(), sort_keys=True))
