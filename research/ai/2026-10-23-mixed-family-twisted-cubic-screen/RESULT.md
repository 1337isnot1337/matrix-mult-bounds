# At most seven displayed T4 shared factors can match the source evaluation curve

October 23, 2026. Exact finite rational linear algebra with a written
incidence argument. This is a restricted-decomposition result; it does not
exclude the single-copy degeneration or improve the exponent.

## Result

The ten shared projective points are copied with their source commit and file
hash in [`input-points.json`](../../../results/mixed-family-twisted-cubic-screen-2026-10-23/input-points.json).
They are the displayed shared factors of the border-rank-10 interpolation
certificate for `T4`, in coordinate order `(t^3, s*t^2, s^2*t, s^3)`.

For each seven-point subset, form the `7 x 10` evaluation matrix of the
quadratic monomials `x_i*x_j`, `0 <= i <= j < 4`. Every one of the 120
matrices has rank 7. Its kernel `Q` is therefore the three-dimensional space
of quadrics through those seven points. Multiplication

\[
  \mathbb Q^4 \otimes Q \longrightarrow \mathbb Q^{20}
\]

maps linear forms times quadrics into cubic forms. Its kernel is the space of
linear syzygies among a basis of `Q`. The exact dimensions across the 120
subsets are:

| Linear-syzygy dimension | Number of seven-point subsets |
|---:|---:|
| 0 | 23 |
| 1 | 45 |
| 2 | 40 |
| 3 | 12 |

No eight-point subset has all of its seven-point subsets with syzygy
dimension at least two. The complete counts of eight-, nine-, and ten-point
sets by the minimum syzygy dimension among their seven-point subsets are in
[`certificate.json`](../../../results/mixed-family-twisted-cubic-screen-2026-10-23/certificate.json).

The seven-point ceiling is sharp for this curve-incidence test. Points 1
through 7 have common quadrics

\[
\begin{aligned}
Q_1&=x_0x_2+3x_0x_3-x_1x_2-2x_1x_3+x_2^2,\\
Q_2&=3x_0x_3-2x_1x_3+x_2x_3,\\
Q_3&=2x_0x_3-x_1x_3+x_3^2.
\end{aligned}
\]

These are the maximal minors, up to signs and order, of

\[
\begin{pmatrix}
x_3 & x_3\\
2x_0-x_1-x_2 & -x_2-x_3\\
-3x_0+2x_1 & x_2
\end{pmatrix}.
\]

For the smoothing check, perturb this matrix by
\[
\epsilon\begin{pmatrix}
x_0 & x_1\\
x_1 & x_2\\
x_2 & x_3
\end{pmatrix}.
\]

The seven points have coordinate rank 4, so they lie on no common plane.
For the height check, `Q2` and `Q3` have gcd `x3`, while `Q1` is not
divisible by `x3`; thus all three quadrics have no common linear factor.
They span a three-dimensional space, so they cannot have a common quadratic
factor. Their maximal-minor ideal has no codimension-one component, and the
determinantal height bound gives height 2. Hilbert-Burch gives resolution
`0 -> S(-3)^2 -> S(-2)^3 -> I -> 0`, Hilbert numerator
`1 - 3*t^2 + 2*t^3`, and Hilbert polynomial `3*n + 1`. The explicit
one-parameter perturbation above has smooth twisted-cubic fibers generically,
with this determinantal curve as flat limit. This is a point-set incidence
example; it does not align the evaluation-node parameters or establish a
tensor degeneration. The exact generic/special-fiber checks are recorded in
[`verify_t4_curve_smoothing.sing`](../../../tools/verify_t4_curve_smoothing.sing).
The matching Hilbert numerators give the same Hilbert function in every
degree, which certifies flatness at the special fiber.

## Incidence argument

For a twisted cubic in projective three-space, the three-dimensional space of
quadrics through it has two independent linear syzygies. Consider a family
of projectively transformed twisted cubics and a limit of their ten source
evaluation factors. The three-dimensional quadratic spaces have a limit in
the Grassmannian. The two-dimensional syzygy spaces also have a limit, so the
limiting three-space of quadrics has at least two independent linear
syzygies. Every limiting factor point is in the zero set of this limiting
quadratic space, by continuity of evaluation.

If seven of the displayed target points are such limits, their quadratic
evaluation rank is 7. Their common quadratic space is consequently exactly
that limiting three-space, and its linear-syzygy dimension must be at least
two. The finite certificate finds that every eight-point set contains a
seven-point subset failing this necessary condition. Hence at most seven of
the ten displayed target factors can be pointwise limits of distinct source
evaluation factors under a common varying change of basis on the shared
four-space.

The Grassmannian compactness argument only needs a convergent subsequence of
the quadratic and syzygy subspaces. It does not require the limiting cubic
curve to be smooth or to have any particular factorization.

## Verification

Run:

```sh
python tools/verify_t4_twisted_cubic_subset_screen.py
```

The verifier uses Python's standard-library `Fraction` arithmetic. It
enumerates all 120 seven-point sets, then all 45 eight-point sets, 10
nine-point sets, and the single ten-point set. It writes the complete exact
rank and syzygy-dimension certificate to `results/mixed-family-twisted-cubic-screen-2026-10-23/certificate.json`.

The optional Singular 4.4.1 check runs with:

```sh
Singular -q tools/verify_t4_curve_smoothing.sing
```

Over `Q(epsilon)` it reports curve-cone dimension 2, degree 3, Hilbert
numerator `1,0,-3,2,0`, and singular-locus cone dimension 0. At
`epsilon=0` it reports the same dimension, degree, and Hilbert numerator.

## Scope

The result applies only when the ten source terms are the standard
ten-node evaluation restriction of `C(4,10)`, their shared factors move
together on a projectively transformed twisted cubic, and the proposed
termwise matches converge to distinct members of the displayed target
interpolation factor set. It rules out eight or more such matches, improving
the earlier all-ten quadratic test for this one route. The seven-point
example above shows that curve containment alone cannot lower this threshold.

It does not rule out a degeneration `C(4,10) -> T4`. In particular, it says
nothing about different border-rank decompositions of `T4`, collisions,
coefficients that cancel between terms, non-termwise limits, or general
Laurent-polynomial changes on all three legs. It supplies no premise for the
unbounded four-sector family and no exponent improvement. The calculation
and argument have not received independent mathematical review or Lean
formalization.
