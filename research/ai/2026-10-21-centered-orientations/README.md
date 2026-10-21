# Costed aggregation of four partial transposes

October 21, 2026. AI-derived written identities and obstructions, with exact
finite controls. There is no external mathematical review or formal proof.
**These tensors are not matrix multiplication, and no smaller exponent is
established. No map from the paired source Q(n,4) is supplied here.**

This calculation investigates whether centering and contraction aggregation
can provide a scalable paired-source construction. The explicit aggregation
has a small cross-term correction, but it has two separate limitations: the
four retained products have different orientations, and the leading rank-one
aggregate has the wrong character cost for the paired-source criterion.

## 1. Shared input and coordinate conventions

Let s be a positive integer, d=3, and n=s^3. Write the coordinates of an
arbitrary n-by-n matrix A as

\[
A_{p,q},\qquad p=(p_1,p_2,p_3),\quad q=(q_1,q_2,q_3),
\quad p_i,q_i\in\{0,\ldots,s-1\}.
\]

For a binary vector sigma, let p^sigma take coordinate p_i when sigma_i=0
and q_i when sigma_i=1; let q^sigma use the opposite choice. Set

\[
\mathcal C=\{000,011,101,110\}.
\]

There are four separate B and C blocks, each with n coordinates. Define

\[
R_s=\sum_{p,q} A_{p,q}
  \sum_{\sigma\in\mathcal C} B^\sigma_{p^\sigma}
                                     C^\sigma_{q^\sigma}.
\tag{1}
\]

Its format is `(n^2,4n,4n)`. The first input A is shared by all four blocks;
the A coordinates are not four independent matrices. In matrix-slice form,
the first slice map is

\[
\rho(A)=\operatorname{diag}
 (A,A^{T_2T_3},A^{T_1T_3},A^{T_1T_2}).
\tag{2}
\]

Here T_i swaps the i-th row and column scalar coordinates, and no complex
conjugation occurs. Identifying the opposite edge pairs of K4 as
`(01,23),(02,13),(03,12)` identifies the four row-coordinate sets with its
four vertex stars. This is an indexing description, not an additional
source tensor or a matrix multiplication equivalence.

## 2. Exact aggregation with twelve small corrections

Form the trilinear aggregate

\[
G_s=\sum_{p,q} A_{p,q}
 \left(\sum_{\sigma\in\mathcal C}B^\sigma_{p^\sigma}\right)
 \left(\sum_{\tau\in\mathcal C}C^\tau_{q^\tau}\right).
\tag{3}
\]

This is a sum of n^2 rank-one tensors. Every diagonal pair sigma=tau gives
the corresponding term of (1). If sigma and tau are distinct, they differ
in exactly two coordinates. At each such coordinate, the B and C factors
use the same scalar index and omit the other scalar index. At the remaining
coordinate they use both indices. Thus the mixed B/C term depends on four
scalar indices. Sum A over the other two indices and call that linear form
the corresponding two-coordinate marginal. The mixed tensor E_(sigma,tau)
is a sum of s^4 rank-one terms, one for each of the four retained indices.
Consequently the exact integer coefficient identity is

\[
R_s=G_s-\sum_{\sigma\ne\tau}E_{\sigma,\tau},\qquad
\operatorname R(R_s)\le s^6+12s^4=n^2+12n^{4/3}.
\tag{4}
\]

All twelve ordered pairs are counted. The correction is explicitly part
of this algorithm; it is not being discarded as an asymptotic zero. One
could instead annihilate these marginals by centering, but that would also
restrict the A space and require an account of the omitted A directions.

More generally, a binary code C of length d gives the same construction
with

\[
\operatorname R(R_{s,C})\le s^{2d}
 +\sum_{\sigma\ne\tau\in C}s^{2d-\operatorname{dist}(\sigma,\tau)}.
\tag{5}
\]

This follows from the same omitted-index count, without a limiting argument.

The centering and aggregation viewpoint was motivated by Solomonik and
Bläser, *Simultaneous Matrix Multiplication by Tensor Contraction
Aggregation*, [arXiv:2610.26563v1](https://arxiv.org/html/2610.26563v1),
Sections 5.2–5.3 and 5.6. Their paper treats independent contractions and
credits earlier aggregation methods. Equations (1)–(5) and the shared-input
orientation analysis here are deductions in this session. We make no
historical priority claim for these elementary identities.

## 3. The complete leading-source cost

Equation (4) is a restriction of a diagonal tensor of size n^2+12n^(4/3).
For a normalized tensor character lambda this gives only

\[
\lambda(R_s)\le n^2+12n^{4/3}.
\tag{6}
\]

The paired-source criterion needs a construction from Q(n,4), whose
character at the balanced 9/4 endpoint has the relevant order n^(3/2).
The leading n^2 in (6) exceeds that scale. An auxiliary correction with
exponent 4/3 does not repair the leading-source mismatch. In particular,
(4) does not instantiate the construction premise in
[the correction-budget note](../2026-10-21-correction-budget/README.md).

There is a separate explicit character source that is cheaper than (6)
in exponent, but still insufficient in its leading coefficient. Define

\[
D_s=\sum_{i=0}^{s-1}a_i(b_i c_*+b_*c_i),
\quad\text{format }(s,s+1,s+1).
\]

It is an ordinary restriction of the direct sum of the two dot products
missing C and B. Thus, in the repository's character notation,

\[
\lambda(D_s)\le s^{p_C}+s^{p_B}.
\]

In D_s^(tensor 6), select the four B support patterns that are K4 vertex
stars and the four C patterns that are their complements. Every scalar
coordinate of a source term belongs to exactly one of B and C. Therefore a
selected B star can pair only with its own complementary C pattern, and
this restriction is exactly R_s. This gives the costed inequality

\[
\lambda(R_s)\le(s^{p_B}+s^{p_C})^6.
\tag{7}
\]

At p_B=p_C=3/4, the right side is `64 n^(3/2)`. The hypothetical
same-orientation matrix target has character `4^(3/4) n^(3/2)` in that
orientation. Since 64 is larger than 4^(3/4), this upper bound gives no
endpoint contradiction, even if the missing untwisting were available.
For unequal p_B and p_C its leading exponent is also worse than the target's
`3(p_B+p_C)` as a power of s. Equations (6) and (7) account for their whole
sources; neither is an unproved Q-source map.

## 4. Full-format degeneration cannot untwist R_s

Assume s>=2. With the standard orthonormal coordinate bases, the three
flattening Gram matrices of R_s are exactly

\[
4I_{n^2},\qquad nI_{4n},\qquad nI_{4n}.
\tag{8}
\]

Indeed each A coordinate occurs four times, each long coordinate occurs n
times, and two support terms never agree on a complementary pair of
coordinates. This last condition proves that the off-diagonal Gram entries
vanish; equal coordinate counts alone would not suffice. The same Gram
identities hold for M(n,4,n). Thus both tensors have zero moment map for
`SL(n^2) x SL(4n) x SL(4n)` and have closed SL orbits.

For completeness, the external geometric input is the complex affine
Kempf–Ness theorem: a complex reductive group acting on a finite-dimensional
Hermitian vector space, with unitary maximal compact action, has a closed
orbit through any zero of the moment map. Distinct closed orbits are
separated by the affine invariant quotient. We use Hoskins,
*Stratifications associated to reductive group actions on affine spaces*,
2013, [Theorem 4.2 and its preceding quotient discussion](https://userpage.fu-berlin.de/hoskins/strat_affine.pdf),
with the trivial character and the special-linear product above.

The two tensors are not isomorphic. The slice space of R_s contains
rho(I)=I_(4n). Its normalized slice space is the space in (2), which is
not closed under matrix multiplication. To see this, take

\[
X=E_{01}\otimes I_s\otimes I_s,\qquad
Y=E_{10}\otimes I_s\otimes I_s.
\]

The first block of rho(X)rho(Y) is XY. The block transposing factors 1 and
3 is X^(T_1T_3)Y^(T_1T_3), whereas the same block of rho(XY) is
(XY)^(T_1T_3). They differ by the embedded nonzero commutator of E_01 and
E_10. The first block fixes the only possible preimage, so the product is
outside the slice space.

In contrast, the normalized slice space of M(n,4,n) is `Mat_n tensor I_4`,
an algebra. This is an isomorphism invariant in the form used here: an
arbitrary two-sided equivalence P S Q becomes conjugation after normalizing
at the image of an invertible slice. In the target algebra, normalization
at any invertible member gives the same algebra. Therefore an isomorphism
would force closure of the normalized source slice space, a contradiction.

Finally, a GL degeneration between nonzero SL-polystable tensors of the
same format can only connect GL-isomorphic tensors. One can check the
scalar issue directly. Along a Puiseux curve write the three GL maps as a
common scalar c(t) times SL maps, after a finite extension. A homogeneous
SL invariant nonzero at the source forces val(c)>=0 if the limit exists.
A homogeneous invariant nonzero at the semistable target forces
val(c)<=0, so val(c)=0. All limiting invariant values then equal those of
c(0) times the source. The unique closed orbit in this invariant fiber
contains both polystable points, so they are SL equivalent after that
scalar. This contradicts the preceding algebra calculation.

Hence R_s does not degenerate to M(n,4,n) in its full format. This statement
allows arbitrary Laurent maps. It does not exclude larger sources with
auxiliary tensors, dimension changes, or partial targets.

## 5. Literal symmetric/skew repair has quadratic cost

Consider the literal difference between (2) and
`diag(A,A,A,A)`. Its first flattening has kernel consisting of matrices A
fixed by all three even partial transposes. The group they generate has
four elements. On the s^6 coordinate entries, the identity fixes s^6
entries and each of the other three elements fixes s^4. The fixed-space
dimension is the number of coordinate orbits, so elementary orbit counting
gives

\[
\dim\ker=\frac{s^6+3s^4}{4},\qquad
\operatorname{rank}(\text{first flattening of the difference})
=\frac34(s^6-s^4)
=\frac34(n^2-n^{4/3}).
\tag{9}
\]

Equivalently, write `Mat_s=Sym_s direct-sum Skew_s`. The only sectors fixed
by all even transposes are the threefold symmetric and threefold skew
sectors. Their dimensions add to `(s^6+3s^4)/4`.

Border rank is at least any flattening rank. Therefore this specified
direct additive repair has quadratic cost. This is not a lower bound for
every possible auxiliary construction after arbitrary changes of basis.

For comparison, the two-channel centered identity gives the shared-input
tensor `diag(A,A^T)`. Without imposing centering, subtracting its two
row/column marginal sums gives the exact upper bound `n^2+2n`. Its literal
repair to `diag(A,A)` has first-flattening rank `n(n-1)/2`. Thus the same
orientation issue already appears in the two-channel calibration.

## 6. Verification and remaining construction question

`verify.py` uses only Python's standard library. It verifies the expanded
integer aggregate and every correction for s=2,3,4; exact Gram identities;
the nonzero normalized-slice product witness; and the first-flattening
repair rank by enumerating all coordinate orbits. It separately expands
the six-factor D_s support restriction at s=2,3. The certificate records
the exact coverage and does not treat finite checks as proofs of the
general statements.

From the repository root:

```sh
python research/ai/2026-10-21-centered-orientations/verify.py --output results/centered-orientations-2026-10-21/certificate.json
python -m unittest discover -s tests -p 'test_centered_orientations.py' -v
```

A useful next construction would have to supply both a sufficiently cheap
source and a same-orientation partial matrix target, with every omitted
coefficient accounted for. The correction count in (4), the character
upper bound in (7), and the fixed full-format obstruction do not supply
such a family.
