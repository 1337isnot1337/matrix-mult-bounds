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

## Scope

The result applies only when the ten source terms are the standard
ten-node evaluation restriction of `C(4,10)`, their shared factors move
together on a projectively transformed twisted cubic, and the proposed
termwise matches converge to distinct members of the displayed target
interpolation factor set. It rules out eight or more such matches, improving
the earlier all-ten quadratic test for this one route.

It does not rule out a degeneration `C(4,10) -> T4`. In particular, it says nothing about
different border-rank decompositions of `T4`, collisions, coefficients that
cancel between terms, non-termwise limits, or general Laurent-polynomial
changes on all three legs. It supplies no premise for the unbounded
four-sector family and no exponent improvement. The calculation and argument
have not received independent mathematical review or Lean formalization.
