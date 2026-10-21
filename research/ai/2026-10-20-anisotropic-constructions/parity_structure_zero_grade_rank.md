# Minimum slice rank of the zero-grade source

October 21, 2026. Every nonzero slice of the zero-grade sub-tensor of
A(a,a) has rank at least a. For A(8,8), an ordinary graded target
with a scalar summand in its zero-grade sub-tensor must therefore
have zero-grade leg dimension at most 60.

## A residual two-torus proves the minimum

Write a zero-grade source variable as X(i,s), meaning the original
common coordinate F(i,i+s,s). Use Y(p,j) and Z(r,q) on the other
legs. The nonzero coefficients satisfy

\[
q=i+s-p,\qquad r=j+p-s,\qquad 0\le i,j,p,q,r,s<a.\tag{1}
\]

For arbitrary alpha,beta, assign the three coordinate weights

\[
\alpha i+\beta s,\quad -\beta p+(\alpha-\beta)j,\quad
(\beta-\alpha)r-\alpha q.\tag{2}
\]

Their sum is zero on (1). Choose alpha=a+1 and beta=1. Then all
first-leg weights are distinct. For any nonzero slice coefficient
vector f, scale by this torus and divide by the least exponent on
its support. The limit is a nonzero multiple of one coordinate
slice. For a nonzero parameter the transformations on the other
two legs are invertible diagonal maps, together with a scalar
factor, so slice rank is unchanged. Rank cannot increase in the
limit. It therefore suffices to bound every coordinate slice.

Fix i,s. For each p satisfying 0<=i+s-p<a, the permitted j values
give exactly a-|p-s| entries in its matrix slice. The row index is
(p,j), while the column is (j+p-s,i+s-p). Both are distinct across
the permitted choices. Thus this slice is a partial permutation
matrix and has rank

\[
\sum_{\substack{0\le p<a\\0\le i+s-p<a}}(a-|p-s|)\ge a.\tag{3}
\]

Indeed p=s is always permitted and contributes a entries. The
corner i=s=0 attains a, so the minimum is exactly a. This argument
works for arbitrary complex slice coefficients; the finite replay
checks the coordinate matrices and the torus identity.

## The ordinary graded target consequence

The source zero-grade spaces each have dimension a squared. Suppose
an ordinary graded restriction has zero-grade target dimension d
and the target zero-grade tensor has a nonzero slice of rank one.
Lift that slice through the first map. It is nonzero because the
target is concise on that leg. Projecting the other two source
spaces, each with kernel dimension a squared minus d, reduces
matrix rank by at most twice that number. Equations (2)-(3) give

\[
1+2(a^2-d)\ge a,
\qquad d\le a^2-\left\lceil\frac{a-1}{2}\right\rceil.\tag{4}
\]

For a=8 this is d<=60. This is an ordinary restriction bound; it is
not asserted for arbitrary degenerations.

## Consequences for common M27 direct sum M7 charge profiles

For a square matrix block whose three vertex charge profiles agree,
the zero-grade tensor is the direct sum of M_m over all charge
multiplicities m. Its zero-grade dimension is the sum of m squared.
A multiplicity one supplies the rank-one slice required in (4).

Every source weight lies between -14 and 14, so each common target
vertex profile has width at most 14. Placing 27 vertices in at most
15 charge bins has minimum square sum 51. A seven-vertex profile
with no multiplicity one has minimum square sum 17, attained by
multiplicities 3,2,2. Those minima would already total 68>64.
Consequently any capacity-feasible common M27 direct sum M7 profile
has a zero-grade scalar slice, and its total zero-grade dimension
must be at most 60.

The large and small square sums are odd. Their minimum values are
51 and 7. The only remaining pairs are therefore

\[
(51,7),\qquad(53,7),\qquad(51,9).\tag{5}
\]

In particular, the width-12 large profile consisting of twelve
multiplicities two and one multiplicity three has square sum 57.
Adding any seven-vertex small profile gives dimension at least 64,
so every such width-12 alternative is excluded as an ordinary
common-profile graded restriction.

## Exact controls and provenance

`parity_structure_zero_grade_rank.py` checks all 262,144 original
A88 source terms, extracts the zero-grade tensor, verifies (2),
and computes all 64 coordinate slice ranks by distinct rows and
columns. No numerical library is used.

```
python -S research/ai/2026-10-20-anisotropic-constructions/parity_structure_zero_grade_rank.py
```

The residual two-torus proof was proposed by the parent research
agent and checked by a second agent in this generating session;
no external independent review is claimed. No matrix multiplication
exponent improvement follows from this obstruction alone.
