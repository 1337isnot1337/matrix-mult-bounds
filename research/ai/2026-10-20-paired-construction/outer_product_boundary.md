# The boundary-column extension of the recovered seed cannot add an outer row

## Scope

The exact maps in `outer_product_injection.md` give
\(Q_{k+1,k}\ge M(k,4,k)\), for every \(k\ge2\). One natural next
construction is to retain those maps as the constant term of a Laurent
extension from \(Q_{k+2,k}\) to \(M(k+1,4,k+1)\). This note excludes
the following particular chart, including arbitrary higher orders.

The constant B and C maps retain **every old source column** of the
integer seed. Their new boundary columns can take arbitrary values in
the old output supports. The four new output B coordinates and four new
output C coordinates are zero at the constant term. Higher coefficients
of B and C are arbitrary regular power series; the A map is allowed an
arbitrary finite Laurent pole.

No extension in this chart exists. This does not exclude a leading map
which changes old source columns, a different exact M4 seed, a path with
singular long-leg maps, or a general Q(6,4) degeneration. There is no
exponent claim.

The argument is a same-session written proof with integer controls.
No external mathematical review is claimed.

## 1. The enlarged source and free boundary columns

Put \(n=k+2\). The enlarged source is

\[
Q_{n,k}=\sum_{p,q<n}\sum_{y,v<k}
A_{p,q}B_{y,q+v}C_{p+y,v}.
\]

The convolution output degree ranges from 0 to \(2k\). Compared with
the Q(k+1,k) seed, exactly these columns are new:

\[
B_{y,2k}\quad(0\le y<k),\qquad C_{2k,v}\quad(0\le v<k).
\]

Write their arbitrary images as \(b_y\) and \(c_v\). All other
source-column images agree with the old seed. The old B output space
has coordinates \(b_{i,2\alpha+\beta}\), with \(i<k\) and
\(\alpha,\beta<2\). The old C output space has coordinates
\(c_{2\alpha+\beta,h}\), with \(h<k\).

Let \(S_0\) be the source after these two constant long-leg maps, leaving
its \(n^2\)-dimensional A space unchanged.

## 2. Every such constant pair loses at most one A direction

Project the old B output onto its coordinates with \(\alpha=0\), and
the old C output onto its coordinates with \(\beta=0\). Each projected
space has dimension \(2k\). Set

\[
u_q=B_{0,q}\text{ after the old B map},\qquad
v_p=C_{p,0}\text{ after the old C map},
\quad 0\le p,q\le k+1.
\]

The \(k+2\) vectors \(u_q\) are linearly independent, and so are
the \(v_p\). Indeed, each list consists of distinct columns of the
invertible \(2k\)-by-\(2k\) matrix L in the seed construction;
\(k+2\le2k\).

With all new columns zero, the doubly projected A contraction is exactly

\[
F(X)=\sum_{p,q=0}^{k+1}X_{p,q}u_q\otimes v_p.
\tag{1}
\]

It is injective. This follows from the linear independence of the two
lists, not from a numerical rank test.

Only the source corner \(p=q=k+1\) can change (1) when the free
boundary columns are turned on. A new B column requires
\(q+v=2k\), hence \(q=k+1,v=k-1\). The old C image with
\(v=k-1\) is killed by the C projection. It can survive only if that
C column is also new, requiring \(p=k+1,y=k-1\). The argument for
a new C column is the same. Consequently the projected map is

\[
F(X)+X_{k+1,k+1}\,\pi_B(b_{k-1})\otimes\pi_C(c_{k-1}).
\tag{2}
\]

As a linear map from the A parameter space, (2) is an injective map
plus a map of rank at most one. Therefore

\[
\operatorname{rank}_A S_0\ge(k+2)^2-1,
\qquad \dim\ker(S_0:A^*\to B\otimes C)\le1.
\tag{3}
\]

This bound holds for **every** value of every free boundary column in
the chart.

## 3. The one-dimensional loss is attainable

Choose all new boundary images zero except

\[
b_{k-1}=u_{k+1},\qquad c_{k-1}=-v_{k+1}.
\tag{4}
\]

Before this change, the corner source slice has only one surviving
term, \(u_{k+1}\otimes v_{k+1}\). The new source term with
\(y=v=k-1\) contributes its negative. Thus the full corner slice
vanishes, including all unprojected output coordinates. Together with
(3), this proves

\[
\operatorname{rank}_A S_0=(k+2)^2-1,\qquad
\ker S_0=\langle A_{k+1,k+1}^*\rangle.
\]

For Q(6,4), the concrete changes are

\[
B_{3,8}\mapsto\text{old image of }B_{0,5},\qquad
C_{8,3}\mapsto-\text{old image of }C_{5,0}.
\]

The resulting A rank is exactly 35. A stored 35-by-35 integer minor
has determinant -1. All 256 coefficients of the A(5,5) slice are zero.

The old M4 restriction is preserved: its A map only uses source indices
\(p,q\le4\), whereas a new B or C column requires respectively
\(q=5\) or \(p=5\).

## 4. A full extension needs at least 2k+1 lost directions

This step is independent of the preceding boundary calculation.
Suppose regular \(B(t),C(t)\), and a Laurent \(A(t)\), give
\(M(k+1,4,k+1)+O(t)\). Let

\[
S(t)=(\mathrm{id}\otimes B(t)\otimes C(t))Q_{k+2,k}.
\]

Over the Laurent-series field, the A-slice space of S(t) has dimension
at most \((k+2)^2\). Its saturated limit W has the same dimension and
contains both the ordinary limit of every source slice and every
regular Laurent combination of the source slices. One precise
construction is to intersect the Laurent slice space with the free
power-series module of output coefficients, and reduce that saturated
module modulo t. A saturated submodule over this discrete valuation
ring has a torsion-free quotient, so its reduction has its full rank.

Thus W contains \(\operatorname{im}S_0\) and the entire
\((k+1)^2\)-dimensional target slice space E.

All source slices at t=0 are supported on the old
\((4k)\)-by-\((4k)\) B/C support. The intersection of E with this
old support has dimension exactly \(k^2\): it consists precisely of
the target matrix coefficients \(a_{i,h}\) with \(i,h<k\).
Indeed, the remaining target coefficients use a new B row or a new C
column, and these matrix-unit supports cannot cancel each other.

Writing \(r=\operatorname{rank}_A S_0\), we obtain

\[
(k+2)^2\ge\dim W
\ge\dim(E+\operatorname{im}S_0)
\ge(k+1)^2+r-k^2=r+2k+1.
\]

Therefore such an extension requires

\[
\dim\ker S_0\ge2k+1.
\tag{5}
\]

For the Q(6,4) to M(5,4,5) step, the required kernel dimension is nine.
Equation (3) bounds it by one throughout the boundary-column chart.
This contradiction excludes the chart for arbitrary Laurent order of
A and arbitrary regular higher coefficients of B and C. Restricting
to a first-order fit is unnecessary.

## 5. Exact controls

`q64-boundary-chart.json` stores the crossed maps, the zero corner,
the 35 minor rows and columns, and its determinant. The program also
checks the unmodified rank 36 and an arbitrary integer assignment of
all eight free boundary columns against the exact rank-one update
formula. The latter is a finite control of the symbolic proof, not
an exhaustive proof about arbitrary boundary values.

The tests repeat the exact construction for k=2 through 6 and check
that every old source column is unchanged.

```bash
python research/ai/2026-10-20-paired-construction/outer_product_boundary.py
python -m unittest discover -s tests -p test_outer_product_boundary.py -v
```

The next constructive search must change more than these boundary
columns or use a different leading family. No conclusion about those
possibilities follows from this chart calculation.
