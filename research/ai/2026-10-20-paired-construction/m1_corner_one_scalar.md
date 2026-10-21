# One scalar does not repair the endpoint corner

**Theorem over C.** Let R be the explicit `(16,18,18)` tensor in
[m1_endpoint_corner.md](m1_endpoint_corner.md), and let D1 be a rank-one
scalar tensor on three new source coordinates. Then

\[
R\oplus D_1\not\unrhd M(4,4,4).
\]

This is an obstruction for that fixed reduced source, including arbitrary
degeneration of the reduced source. It does not exclude a general Q64
construction, a different corner, or correction by two or more scalars.
The last assertion is deliberately separate: the two-scalar ordinary
case is discussed in a companion note, without a two-scalar degeneration
claim. No exponent improvement is claimed here.

## 1. The two alternatives for an ordinary image

Write the ordinary output maps as

\[
A_R:A_R^{\rm source}\longrightarrow\bar A_{16},\qquad
B_R:B_{18}\longrightarrow\bar B_{16},\qquad
C_R:C_{18}\longrightarrow\bar C_{16},
\]

and let the scalar term map to `a_* tensor b_* tensor c_*`. The source
first space of R has dimension 16. Consider any resulting tensor T in
the fixed target space `V=bar A tensor bar B tensor bar C`.

If `A_R` is singular, choose a nonzero target A functional that vanishes
on its image. Its contraction with T is a scalar multiple of
`b_* tensor c_*`, and therefore has rank at most one. This includes the
case where that contraction is zero.

If `A_R` is invertible, use its dual isomorphism to pull the source
four-dimensional family

\[
F_0=t^5\otimes P,\qquad
P=\langle1-t^4,t^2,t^3,t^5\rangle,
\]

back to a four-dimensional subspace `F` of target A functionals. Every
source R slice in `F0` has rank at most four, and the family has aggregate
long supports of dimensions `(14,4)`. On F the scalar contributes

\[
\ell(\alpha)b_*\otimes c_*,
\]

for a linear form `ell` on F. Consequently, every T slice from F has
rank at most five. The aggregate B support is at most 15 and the
aggregate C support at most five.

These are upper bounds on supports of the sum, so they do not assume
that supports of two summands add. Cancellation can only decrease the
bounds.

Thus every ordinary image lies in the union of the following two sets:

1. `Z1`: tensors possessing a nonzero A functional whose slice rank is at
   most one.
2. `Y`: tensors with a four-dimensional A-functional space F such that
   every slice has rank at most five, and the whole family's long
   supports have dimensions at most 15 and at most five, respectively.

## 2. Both sets are closed

The first set is closed by projective slice incidence, as in the
endpoint-corner note.

For the second, use the parameter space

\[
\mathcal G=
\operatorname{Gr}(4,\bar A^*)\times
\operatorname{Gr}(15,\bar B)\times
\operatorname{Gr}(5,\bar C).
\]

The Grassmannians are projective: their Pluecker realizations are the
closed loci of decomposable exterior vectors, defined by the Pluecker
relations. They carry the indicated tautological subspaces. For the
standard Grassmannian functor and its subspace interpretation, see the
Stacks Project, [Tag 089R](https://stacks.math.columbia.edu/tag/089R),
Section 27.22, accessed 2026-10-21.

Inside `V times G`, impose both of the following conditions:

\[
T(F)\subseteq H_B\otimes H_C,
\tag{1}
\]

\[
\operatorname{rank}T(\alpha)\le5
\quad\hbox{for every }\alpha\in F.
\tag{2}
\]

Condition (1) is a closed linear-bundle incidence. On a local frame
`f1,...,f4` for F, write `alpha=sum u_i f_i`. Condition (2) says that all
coefficients in the four variables `u_i` of every `6 by 6` minor of
`T(alpha)` vanish. There are finitely many such polynomial equations,
and the condition is invariant under a change of frame. Therefore the
incidence is closed globally.

Projection from this incidence to V is projective, hence closed. The
image is exactly Y: any support space of smaller dimension can be
extended to the displayed dimensions 15 and five. Projective morphisms
are proper by the Stacks Project,
[Tag 01WC](https://stacks.math.columbia.edu/tag/01WC), Lemma 29.44.5, and
proper morphisms are universally closed by
[Tag 01W0](https://stacks.math.columbia.edu/tag/01W0), Definition 29.42.1,
accessed 2026-10-21.

The finite union `Z1 union Y` is closed. It contains every ordinary image
of `R direct-sum D1`, and therefore contains every degeneration into the
fixed target format.

## 3. M4 belongs to neither set

A nonzero A slice of M4 is, after reordering bases, a nonzero `4 by 4`
matrix tensored with `I4`. Its rank belongs to `{4,8,12,16}`, so M4 is
outside Z1.

Suppose it belonged to Y. Every nonzero slice from the four-dimensional
F would have rank at most five, so all would have rank exactly four.
The corresponding `4 by 4` matrices would form a four-dimensional
linear space of rank-one matrices.

Such a space has a common image or a common coimage. Indeed, two
rank-one matrices with independent images and independent coimages
have a rank-two sum. If one matrix shares only the image of a fixed
member and another shares only its coimage, those two matrices again
have a rank-two sum. Thus the whole space has one fixed factor.

At dimension four, its aggregate supports after tensoring with I4 are
exactly `(16,4)` or `(4,16)`. Neither satisfies the simultaneous bounds
`(15,5)` in Y. This proves the theorem.

## Exact controls and review scope

The adjacent Python file uses only the standard library and the already
certified canonical R tensor. In an explicit image with `A_R` the
identity, it maps the scalar into a new B and C coordinate and into the
first basis direction of F. The four displayed basis slices have ranks
`(5,4,4,4)` and aggregate supports `(15,5)`, showing the upper bounds
used in the proof. A second explicit control makes `A_R` singular and
shows a rank-one scalar-only slice.

```bash
python -S research/ai/2026-10-20-paired-construction/m1_corner_one_scalar.py
python -S -m unittest discover -s tests -p 'test_m1_corner_one_scalar.py'
```

The theorem is a written algebraic argument with same-session exact
controls and review. It is not an external reviewed result, and the
finite controls are not a substitute for the quantified proof above.
