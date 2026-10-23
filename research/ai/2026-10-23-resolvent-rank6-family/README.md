# A four-dimensional family in the fixed-resolvent rank-six locus

The fixed-resolvent space contains a four-dimensional linear subspace whose
nonzero elements all have ordinary matrix rank exactly six over every field.
Its projectivization is a `P^3` inside the rank-six locus. This is a partial
description; the full rank-six locus is not classified.

For each nonzero member, every three-dimensional subspace `L` of its image
gives the compression alignment from the preceding minimum-rank theorem.
Choosing rank-109 maps `P` and `C` with `ker(P)=L` and
`im(C)=X^-1(L)` realizes a nonzero compression kernel at total rank loss six.
This is a linear-map example only: it is not a tensor degeneration or matrix
target, and these ranks do not satisfy `PC=I_110`.

Claim `AI-RESOLVENT-RANK6-FAMILY-001` remains written and unreviewed.

## Files

- `proof.md` gives the all-field argument and the compression construction.
- `verify.py` checks the four exact six-row identities and replays the
  predecessor's 31-minor lower-bound certificate.
- `../../../results/resolvent-rank6-family-2026-10-23/verification.json`
  records the exact support checks.
- `manifest.json` pins the verifier, proof, and result.

## Reproduction

Run from the repository root:

```sh
python research/ai/2026-10-23-resolvent-rank6-family/verify.py
python -m unittest discover -s tests -p test_resolvent_rank6_family.py -v
```

The verifier uses the Python standard library and the maintained exact
reconstruction from `research/ai/2026-10-23-resolvent-minrank/verify.py`.
