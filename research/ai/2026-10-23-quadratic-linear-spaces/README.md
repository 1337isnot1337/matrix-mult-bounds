# Sharp dimension-six bounds for linear biform families

October 23, 2026. Owner-directed Codex research. Written and unreviewed;
same-session checks are not independent mathematical review. No improved
matrix-multiplication exponent is claimed.

For the nine-dimensional coefficient space of biforms with separate
degrees at most two, the [proof](proof.md) establishes two sharp bounds
for the full 15-by-15 crossed source R_(3,3):

| Hypothesis on a linear family W | Sharp bound |
| --- | --- |
| Every F2 vector has source rank at most14 | dim W<=6 |
| Every F2 vector has source rank at most12 | dim W<=6 |
| Over any field, every vector after algebraic closure has source rank at most12 | dim W<=6 |

A fixed horizontal or vertical linear factor attains dimension six.
The binary upper bound uses a three-dimensional space whose seven
nonzero vectors all have full source rank; any seven-dimensional space
must intersect it. Its seven exact integer determinants are
-1,7,3,1,43,1,1, all odd.

The geometric rank-12 proof is separate. The merged quadratic index
formula identifies that rank locus with the union of the vertical- and
horizontal-factor loci. Each is an irreducible projective multiplication
image of P1 times P5 and has dimension at most six. Each spans P8,
so neither can contain a P6. The proof works in every characteristic
and allows repeated factors and factors at infinity.

## The field distinction is necessary

A rank cap on all binary vectors need not persist after extending
scalars. The six-dimensional binary family with basis

    1, x^2, (1+x+x^2)z, z^2, xz^2, x^2 z^2

has rank at most14 on all its F2 vectors. But over
F4=F2[alpha]/(alpha^2+alpha+1), its vector

    x^2+(1+x+x^2)z+(x+alpha x^2)z^2

has full determinant1. The verifier checks this with exact F4
arithmetic and independently as an invertible 30-by-30 binary map.
Thus the binary theorem does not assert the corresponding geometric
rank-14 theorem over arbitrary fields. For an infinite field, a cap
on every field-valued vector does imply the minor identities required
by the geometric rank-12 theorem.

## Finite classification and verification

[verify.py](verify.py) independently builds the literal crossed matrix;
it imports no other research implementation. The saved
[report](../../../results/quadratic-linear-spaces-2026-10-23/controls.json)
contains:

- All 511 nonzero binary source ranks: 49 of rank9, 198 of rank12,
  132 of rank14, and 132 of rank15.
- The compact seven-point upper certificate and a dimension-six
  fixed-factor lower certificate.
- A census of all 43,435 dimension-seven binary subspaces: each
  contains at least six rank15 points and at least32 points above rank12.
- A census of all 788,035 dimension-six binary subspaces: exactly
  six have cap12; exactly twenty have cap14. The latter comprise
  fourteen coefficient compression spaces and six additional spaces.
- The explicit extension-field counterexample above.

The report stores the census counts, minima, and surviving spaces;
the rejected subspaces are regenerated during replay. This is a finite
classification of binary dimension-six spaces, separate
from the two dimension-bound proofs. It does not classify geometric
equality cases over arbitrary fields. Neither upper-bound proof requires
the exhaustive subspace census.

From the repository root:

```sh
python research/ai/2026-10-23-quadratic-linear-spaces/verify.py --output /tmp/quadratic-linear-spaces-controls.json
python -m unittest discover -s tests -p 'test_quadratic_linear_spaces.py'
```

The six focused tests replay the compact certificates and complete
report, reject corrupted certificates, independently check the
dimension-seven census through binary character sums, verify the F4
counterexample by restriction of scalars, and check source hashes.

## Provenance and scope

The mathematical prerequisites are the merged
[kernel-index package](../2026-10-23-quadratic-kernel-indices/README.md)
and standard projective geometry, all pinned in
[sources.json](sources.json). No unmerged torsion result is required.
The original crossed source and the prior individual-slice results
retain their credit.

These results bound whole linear families of slices in one source
block. A tensor-target application must still establish that its
proposed maps impose the corresponding source-rank cap. No compatible
three-leg maps, full cyclic-source classification, or exponent
improvement follows from the dimension bounds alone.
