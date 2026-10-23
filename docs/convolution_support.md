# Convolution support recognition under arbitrary relabeling

The maintained [recognizer](../tools/convolution_support.py) certifies a
coefficient-one convolution tensor C(a,b) after independent permutations of
its three coordinate sets. Integer labels can be negative or have gaps, and
any leg can be the output. The archived recognizer only tries sorted labels
and their reversals. Neither protected archive is changed.

This is R6 tooling maintenance, separate from PR118's exact ranking and
whole-candidate replay. It adds no research claim or exponent improvement.
The code is a standalone support interface; it does not silently replace
recognition or alter candidate scores in the historical or PR118 searches.

## Concrete improvement

The [saved twelve-term witness](../tests/fixtures/relabelled_convolution.json)
is C(3,4) under the coordinate labels

- x: 0, 2, 1;
- y: 3, 1, 0, 2;
- z: 5, 2, 0, 4, 1, 3.

The archived recognizer returns a slice lower bound of 4. The new recognizer
exports three bijections identifying the entire block as C(3,4), whose
existing scalar-profile lower bound is 70/9. This strengthens recognition
of the same block; it supplies no new degeneration. No improvement in the
unchanged numerical-label monomial search scope is asserted. Arbitrary
coordinate permutations matter when importing supports or permuting bases.

## Discovery and acceptance

For each prospective output leg, the dimensions must be (a,b,a+b-1),
there must be ab distinct terms, and every input pair must appear once.
Discovery solves the exact rational equations X_i+Y_j=Z_k for those terms.
A kernel vector whose input coordinates form arithmetic progressions with
the same step proposes a coordinate permutation. One-dimensional inputs
use the explicit matching directly.

For an actual convolution with both input dimensions at least two, every
kernel vector has X_i=alpha+i*delta and Y_j=beta+j*delta in the true order.
Indeed the equalities X_(i+1)+Y_j=X_i+Y_(j+1) equate every adjacent input
difference. The output coordinates are then alpha+beta+k*delta. The kernel
contains a vector with delta nonzero, so any spanning kernel basis has at
least one such vector. Sorting its coordinates and dividing by the positive
step recovers a true labeling, possibly reversing both inputs and output.
Thus discovery covers every independent relabeling of a convolution. This
is an algorithm correctness argument, not an independently reviewed theorem
about matrix multiplication.

Acceptance does not trust the kernel, its dimension, or any floating value.
It checks that all three proposed maps are integer bijections onto the
specified complete intervals. It then checks equality of the mapped term
set with every (i,j,i+j) of C(a,b). The verifier rejects missing terms,
extra terms, repeated terms, partial maps, repeated map keys, nonbijective
maps and incorrect bijections. A certificate is deterministic for a given
labeled support and identifies a canonical target support, but does not
claim to select a canonical automorphism or a label-independent hash.

Only unit coefficients are supported. The caller must establish this
hypothesis; support alone does not certify tensors with other coefficients.
Repeated terms are rejected rather than silently coalesced. Unsupported
supports return null. Resource use is not bounded independently of support
size; arbitrary large input should not be treated as a cheap search filter.

## Reproduction and coverage

Run from the repository root with standard-library Python only:

```sh
python tools/convolution_support.py tests/fixtures/relabelled_convolution.json > /tmp/convolution-certificate.json
python tools/convolution_support.py tests/fixtures/relabelled_convolution.json --certificate /tmp/convolution-certificate.json
python -m unittest discover -s tests -p test_convolution_support.py -v
```

Six focused tests cover:

- 150 cases: all a,b in 1 through 5, each of six axis permutations, and
  one independently shuffled labeling per case with seed 20261023;
- every one of the 4096 assignments of four output colors to the six
  input pairs of a 2-by-3 block; an independent enumeration of all
  coordinate permutations agrees on precisely 144 accepted supports;
- the exact 4 versus 70/9 score witness, JSON certificate round trips,
  term-order invariance, malformed inputs and damaged certificates.

The implementation and controls are owner-directed Codex work. They reuse
the convolution definition and scalar profile from the
[initial note](../research/ai/2026-10-20/research_note.md), with its existing
external source credits. Rational elimination and coordinate permutation
are elementary methods; no historical novelty is claimed. There is no
new external theorem dependency, independent mathematical review, or
change to the research claim ledger.
