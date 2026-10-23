# Complete rank-six locus of the fixed resolvent

The fixed 112-dimensional limiting matrix space W has a 17-dimensional
linear rank-at-most-six locus. Every nonzero matrix in it has rank six
and the same six-dimensional image. This classification holds over every
field, via exact integer minor certificates.

Over C (or any algebraically closed field), two rank109 compression maps
can kill at most one dimension of W. An explicit compression attains
dimension111, so the loss bound is sharp. This concerns ordinary matrix
rank, not tensor slice rank, and does not improve the exponent.

Claim `AI-RESOLVENT-RANK-SIX-LOCUS-001` is written and unreviewed.
The finite replay is separate from the written determinant-pencil proof.

Run from the repository root:

```sh
python research/ai/2026-10-23-resolvent-rank-six-locus/verify.py results/resolvent-rank-six-locus-2026-10-23/certificate.json
python -m unittest discover -s tests -p test_resolvent_rank_six_locus.py -v
```

The verifier requires only the Python standard library. It reconstructs
the literal outer source, checks 26 triangular seven-minors and five
terminal six-minors, verifies the complete terminal parameter space,
and computes an explicit compressed source-space rank over Q.
Neither discovery code nor a predecessor verifier is imported.

- [Proof and exact scope](proof.md)
- [Immutable source pins and credit](sources.json)
- [Certificate](../../../results/resolvent-rank-six-locus-2026-10-23/certificate.json)
- [Recorded exact report](../../../results/resolvent-rank-six-locus-2026-10-23/verification.json)
- [Certificate and report hashes](manifest.json)

The predecessor supplied the fixed resolvent, its limiting space, and
the sharp minimum rank. This owner-directed OpenAI Codex continuation
classifies its entire rank-six locus and proves the sharp compression
loss. It makes no historical-priority or independent-review claim.
