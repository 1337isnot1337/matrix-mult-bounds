"""Export graph matchings. Acceptance is performed by the separate verifier."""
from __future__ import annotations

import gzip
from itertools import combinations
import json

import verify


def matching(adjacency):
    mate = [-1]*28

    def augment(u, seen):
        for v in sorted(adjacency[u]):
            if v in seen:
                continue
            seen.add(v)
            if mate[v] < 0 or augment(mate[v], seen):
                mate[v] = u
                return True
        return False

    for u in range(28):
        augment(u, set())
    return [[u, v] for v, u in enumerate(mate) if u >= 0]


def main():
    entries = []
    for subset in combinations(range(16), 10):
        edges = matching(verify.graph(subset))
        verify.require(len(edges) in (24, 28), "Unexpected discovery matching size")
        edges = edges[:25]
        verify.check_witness(subset, edges)
        entries.append({"cells": list(subset), "matching": edges})
    record = {"scope": "Every ten-coordinate biform subspace; coordinate kernels only",
              "witnesses": entries}
    verify.RESULT.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(record, separators=(",", ":")).encode()
    verify.CERTIFICATE.write_bytes(gzip.compress(payload, mtime=0))
    print(json.dumps({"subsets": len(entries), "compressed_bytes": verify.CERTIFICATE.stat().st_size,
                      "verification_census": verify.check_certificate()}, sort_keys=True))


if __name__ == "__main__":
    main()
