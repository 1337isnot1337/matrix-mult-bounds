# Universal constant-compression bound for the A4 outer space

The [written proof](proof.md), claim `AI-A4-ARBITRARY-COMPRESSION-001`,
proves over the complex numbers that every rank-26 compression of the
specified 46-dimensional matrix space

    E = G + [G,F] + FGF,   F = G00,   E subset Mat28

has image dimension at least 38. A simultaneous torus limit reduces
arbitrary input/output subspaces to graded flags while keeping arbitrary
subspaces inside each weight space. Exact zero-block equations and
quadratic minors cover 2,806 of 2,809 weight-budget pairs. Explicit minor
identities and a shared-flag argument cover the final three.

By the credited [prior low-rank reduction](../2026-10-23-conjugation-limit/LOW_RANK_REDUCTION.md),
every constant rank-110 compression of the fixed full 112-dimensional
two-sided conjugation limit therefore has dimension at least 104. The
necessary target condition is dimension at most 103. This closes all
constant compressions in that one specified family, including arbitrary
Laurent first maps. Moving compressions and different singular paths are
outside the theorem. There is no full matrix target or exponent gain.

## Exact acceptance

From the repository root, with the maintained requirements installed:

```sh
python research/ai/2026-10-23-a4-compression-algebra/verify.py
python -m unittest discover -s tests -p 'test_a4_arbitrary_compression.py' -v
```

The [retained certificate](../../../results/a4-compression-algebra-2026-10-23/certificate.json)
records every budget pair and 24 rational linear combinations of literal
block minors. The [accepted report](../../../results/a4-compression-algebra-2026-10-23/verification.json)
records complete coverage. Acceptance independently reconstructs the
literal source, exact source unit, 46 independent matrices, grading,
all zero-block nullspaces, necessary minors, Hessian ranks, and the nine
coupled blocks in degrees six through eight. It does not use a numerical
tolerance, a modular rank upper bound, or a Groebner basis.

Discovery is optional and separate from acceptance:

```sh
python research/ai/2026-10-23-a4-compression-algebra/discover.py --output results/local/a4-compression-certificate.json
python research/ai/2026-10-23-a4-compression-algebra/verify.py --certificate results/local/a4-compression-certificate.json
```

The package [pins its prior inputs](sources.json) and preserves their
attribution. This is a written, unreviewed theorem with exact finite
acceptance. Proof checks within the generating session are not independent
mathematical review or formalization. The initial [question checkpoint](QUESTION.md)
is retained as a record of the investigation's starting point.
