# Verification receipt

Date: October 23, 2026. Base:
`7690348a792c5734d6f00d7fa7a9e6ce8dc37daa`.

## Commands and completed finite scope

```sh
python research/ai/2026-10-23-diagonal-first-support/verify.py --check
python -m unittest discover -s tests -p test_diagonal_first_support.py -v
python -m unittest discover -s tests -p test_research.py -v
git diff --check
```

All commands completed successfully. The new module's eight focused
tests and the existing research module's eighteen checks passed,
including all relative Markdown links, claim
statuses, the archive manifest and the unchanged 38-source registry.

The standalone verifier reconstructs the following exact controls:

- Six shift-transpose first maps, r=2 through 7, with explicit unit
  triangular minors of size r-squared. It checks the shifted transpose
  coefficient order, not just the ranks.
- Complete diagonal polynomial identities over Q, F2 and F3, both
  before and after a genuine diagonal-vanishing bilinear change. The
  perturbed off-diagonal output is invertible. For the tested ruling
  u=(1,...,1), the original image has zero common left and right
  kernels and upper rank at most two.
- Joint square spaces for two noncoordinate disjoint factor kernels,
  and r-dimensional cross spaces for a shared kernel vector at r=2
  through 8, over all three tested fields. No division by two occurs.
- A native Q(5,4) slice reconstructed from every source coefficient
  and independently from the offset formula. Its coefficient rank is
  two, raw slice rank twenty and target diagonal slice rank four.
  Both polynomial containing spaces have dimension twenty.
- Every feasible deficiency pair for each budget e=0 through 500:
  197324 pairs, with all twelve threshold splits checked for each.
  Integer square-root endpoints, the joint budget maximum and the
  minimal rounded repair bounds are checked exactly.
- Rejection of an altered diagonal coefficient, a changed source
  hash, a changed bound in the saved certificate and an omitted pin.

Four imported source files are byte-pinned. No prior Python or test
file is changed. The standalone verifier uses the standard library
and does not execute prior source files.

## Mathematical and regression limits

The coordinating parent and a separate agent in the same generating
session checked the written proof: the quadratic Veronese intersection,
closed kernel-inclusive inverse images, the common-kernel cross space,
the joint triangular budget, all threshold splits, characteristic two
and algebraic-closure descent. These are same-session checks, not
independent mathematical review or formalization.

The exact controls do not certify the universal projective dimension
or divisor-incidence theorems. Their sources and hypotheses remain
explicit in the proof. The claim remains `proof-written-unreviewed`.
The first-map examples supply no long maps to the matrix target, and
no Laurent extension or exponent improvement is claimed.

The inherited [871-test full regression receipt](../../../results/first-support-capacity-2026-10-23/README.md)
belongs to the earlier support-capacity commit `66c4636`. This focused
follow-up does not relabel that run as a full test of its new code.
Parent integration and final-head hosted CI remain separate gates.

## Artifact hashes

Source pins are in [sources.json](sources.json); the complete finite
report is [certificate.json](certificate.json).

| File | SHA-256 |
|---|---|
| README.md | `3aa453f2b91f22a91392fa37c66c70476e296f805f248ae1f99ef754af5e8dab` |
| verify.py | `6aefad740ad7be3f7e62f693427b7ed5e172d090b068fff991aa9990ee73c60c` |
| certificate.json | `fd23ad2e2df5802087bf7538b10f706967baf91d424eb81138338d6dbe56814f` |
| test_diagonal_first_support.py | `269aa95b2c29a5facf2c268c42d684653b35f2ba88bb1fd447d9749bd8ba11ff` |
