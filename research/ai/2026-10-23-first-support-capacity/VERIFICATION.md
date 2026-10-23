# Verification receipt

Date: October 23, 2026. Base main:
`3008d704d1797da02f7bf3f29cc1dbd4c0e7fa93`.

The following commands completed successfully in the topic worktree:

```sh
python research/ai/2026-10-23-first-support-capacity/verify.py --check
python -m unittest discover -s tests -p test_first_support_capacity.py -v
python -m unittest discover -s tests -p test_research.py -v
git diff --check
```

The focused module has eight tests. The existing research and repository
module has eighteen tests, including claim status, all relative Markdown
links, the archived source manifest and the unchanged 38-source registry.
The standalone verifier regenerated the saved certificate exactly.

## Exact coverage

- Every coefficient in the four-term M(2,1,2) pole-cancellation identity,
  both annihilator contractions, and a determinant-minus-one regular
  first-support minor.
- Five native target-contraction support unions: one noncoordinate
  rectangular example and four explicit oblique annihilator patterns.
- Native paired-source slices constructed both from the complete source
  sum and the offset formula. Polynomial controls include H=1, H=1+xy,
  and H=1+xy+x-squared*y-squared, over Q, F2 and F3.
- Exact containing-space membership and first-map rank products,
  including one deficient factor map.
- Two surjective long-map controls with kernel dimensions sixteen:
  slice losses five-plus-six retain rank five, while five-plus-seven
  attain rank four. This checks the boundary used in the stratum proof.
- Width bounds at n=200 for widths one through four; exact capped
  thresholds for c=0 through 8; all 6561 stated integer deficiency and
  positive-dimension choices in the finite control range.
- Rejection of an altered Laurent coefficient and an altered saved
  certificate.

The verifier reads only the two locally pinned main-branch source notes.
PR147's comparison is an immutable URL/hash citation, with its coordinate
annihilators reconstructed here. No unavailable file is imported. Neither
archive directory, maintained dependency list, nor external source
registry was changed.

## Mathematical review scope

A separate agent in the same generating session checked the Laurent
saturation and union-support proofs, the native source orientation,
fixed-H degrees and containing spaces, closed divisor incidence and
fiber dimensions, two-sided rank loss, both Segre inequalities, the
integer threshold choice, and descent from algebraic closure. The
coordinating parent separately read both bound derivations.

These are same-session checks, not independent mathematical review.
Finite exact tests do not establish the universal algebraic-geometric
dimension statements. Both claim records remain
`proof-written-unreviewed`; neither is formalized or improves the
matrix multiplication exponent.

## Later full regression

The coordinating parent subsequently completed the full local suite at
commit `66c463682c899f3d6cffa5f5f438812bf0981fd4`, tree
`931dfcffdf98fce09201d88569953457ebdd362c`. All 871 tests across 204
modules passed, with no failures, errors or skips. The four disjoint
groups contain 214, 206, 224 and 227 tests. All five archived reports
replayed with identical exact payloads; both archive directories remain
unchanged from `fe602e418743f37a7cfa54d788b64aaf8a9d6095`.

The [full receipt](../../../results/first-support-capacity-2026-10-23/README.md)
retains complete logs, status records, coverage identifiers and hashes.
The Python files were not changed while packaging that evidence. The
eighteen repository checks were rerun after the receipt and status text
were added. These documentation checks are separate from the full
871-test run; hosted CI at the final commit remains a separate gate.

## Artifact hashes

| File | SHA-256 |
|---|---|
| verify.py | `50ba5aa7b92097ccfbc6308df771b6057cf02d04d30e32bfd9f1e88a80e4f9ca` |
| certificate.json | `e25d418c175256db4126139047ae48572b867f4b23512bda2e4f6161ec00de78` |
| test_first_support_capacity.py | `d7e79669179604a8839be2a248a40681ddf753c8ee53ead5cb6c0ffdc32dc349` |
