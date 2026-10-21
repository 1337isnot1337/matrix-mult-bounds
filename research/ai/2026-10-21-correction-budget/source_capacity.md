# Source dimensions with a border-rank correction

October 21, 2026. Written deduction, audited by another agent in the
same generating session. No independent review or exponent improvement.

## Finite statement

Work over C. Let T have leg dimensions at most D_A, D_B, D_C. Let R
have border rank at most s. If a degeneration of T direct-sum R gives

\[
M(l,h,r)=\sum_{i=1}^l\sum_{\alpha=1}^h\sum_{j=1}^r
 a_{ij}\otimes b_{i\alpha}\otimes c_{\alpha j},
\]

then

\[
\begin{split}
lr&\le D_A+s,\\
s&\ge r\left\lceil\frac{\max(0,lh-D_B)}h\right\rceil,\\
s&\ge l\left\lceil\frac{\max(0,rh-D_C)}h\right\rceil.
\end{split}
\tag{1}
\]

The last two bounds can be much stronger than the corresponding
ordinary flattening deficits. They apply to arbitrary local maps and
their limits. No regularity is assumed for the individual summands in
a Laurent presentation.

## Proof, including the limit step

Use the target spaces A, B, C, of dimensions lr, lh, hr. Write
`k=max(0,lh-D_B)`. Every ordinary local image S of T direct-sum R has a
k-dimensional subspace U of B-dual annihilating the B-support of the
image of T. Consequently the restriction of S to U has A-flattening
rank at most s: it is the corresponding image of R, and flattening
rank is a lower bound for border rank.

Consider all pairs (S,U), with U in the Grassmannian Gr(k,B-dual),
such that this restricted A-flattening has rank at most s. The rank
condition is closed: in each Grassmannian chart it is given by the
size-(s+1) minors of the universal restricted flattening. These local
conditions agree on overlaps. The Grassmannian is projective, so
projection to the affine tensor space is proper and has closed image.
Thus every degeneration of an ordinary local image retains some such
U. This justifies the assertion for limits even when chosen local
matrices have poles. For k=0 the same argument is vacuous, as required.

Identify U with a k-dimensional space of l-by-h matrices. Let W be
the joint span of all their columns. Contracting the displayed matrix
tensor with every element of U shows that its restricted A-support is
exactly

\[
W\otimes\mathbb C^r.
\]

Each target column j contributes an independent copy of W, and all
the columns of every matrix in U occur. Hence the restricted
A-flattening has rank r dim(W). Since all matrices in U have columns
in W, one has `k<=h dim(W)`. This proves the B assertion in (1).
Interchanging the B and C roles proves the C assertion. The first
assertion is the usual A-flattening bound and subadditivity of its rank.

The algebraic-geometric facts used above are standard: the
[Grassmannian construction, Stacks Project Tag 089R](https://stacks.math.columbia.edu/tag/089R),
[projective morphisms are proper, Tag 01WC](https://stacks.math.columbia.edu/tag/01WC),
and [proper morphisms are universally closed, Tag 01W0](https://stacks.math.columbia.edu/tag/01W0).
Only these geometric facts are imported; the matrix-support calculation
is given here. No historical novelty of (1) is asserted.

The concurrent [two-source budget note in PR 51](https://github.com/1337isnot1337/matrix-mult-bounds/blob/dab88a63efb7b93be1e302d932c497d1a3ca19db/research/ai/2026-10-20-anisotropic-constructions/two_source_budget.md)
uses six simultaneous kernel spaces to bound two arbitrary source
summands for a square target. It was inspected before this package was
published. The present calculation uses one rectangular target leg and
the auxiliary border-rank bound; it is not presented as a replacement
or a strengthening of that different two-source inequality.

## Consequence for the paired source

The native paired source is

\[
Q(n,b)=\sum_{p,q<n}\sum_{y,v<b}
 A_{pq}\otimes B_{y,q+v}\otimes C_{p+y,v}.
\]

Its leg dimensions are n squared and b(n+b-1) on each long leg. Fix
positive integers b and h. Suppose one unbounded sequence of genuine
complex degenerations

\[
Q(n,b)\oplus R_n\ \rightsquigarrow\ M(l_n,h,r_n)
\]

has `border-rank(R_n)=o(n^2)`, `l_n/n -> rho>0`, and
`r_n/n -> sigma>0`. Dividing (1) by n squared gives

\[
\rho\sigma\le1,\qquad \rho h\le b,\qquad \sigma h\le b.
\tag{2}
\]

For example, if rho h>b, the B bound has positive quadratic leading
coefficient `sigma*(rho*h-b)/h`, contradicting the correction hypothesis.
The C bound works in the same way.

It follows that

\[
\rho\sigma h\le\min\{h,b^2/h\}\le b.
\tag{3}
\]

In particular the sufficient margin from the separate
[critical-coefficient criterion](critical_coefficient.md) obeys

\[
(\rho\sigma h)^{3/4}-\tfrac43\sqrt b
\le b^{3/4}-\tfrac43\sqrt b.
\tag{4}
\]

The maximal volume in (3) is attained only at h=b and
rho=sigma=1. The right side of (4) is positive for integer b exactly
when b>=4, since the equivalent condition is `b>256/81`. Thus changing
the target shape cannot make this same algebraic margin positive at
widths one, two, or three while retaining subquadratic auxiliary rank.
For instance a width-two source with near-full outer dimensions and
target inner dimension four needs auxiliary border rank at least
`(1/2-o(1))*n^2`.

This is a necessary capacity condition, not a construction. It neither
proves that the feasible equal-width geometry can be realized nor
excludes improvements from other sources or spectral arguments.

## Exact finite controls

`source_capacity.py` independently contracts the displayed matrix
tensor against rational matrix subspaces and forms the entire restricted
A-flattening. It compares that rank with r times the separately computed
joint column rank. Coordinate and mixed subspaces include sharp ceiling
examples and an example with a strictly larger rank. A deliberate
coefficient deletion breaks the expected equality and is rejected.
These checks illustrate the finite calculation; the all-size and closed
limit statements depend on the proof above.

From the repository root, using only Python's standard library:

```sh
python -S research/ai/2026-10-21-correction-budget/source_capacity.py
python -S -m unittest discover -s tests -p test_source_capacity.py -v
```
