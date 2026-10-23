# An exact 29-product aggregation construction

## Result and scope

Let `M(a,b,c)` denote the usual matrix multiplication tensor, with first
matrix `a` by `b`, second matrix `b` by `c`, and output `a` by `c`. Over
every field of characteristic zero, the exported family proves, for each
integer n >= 1,

\[
 R\!\left(M(n^3,n^3,n^3)^{\oplus29}\right)
 \le r_{29}(n)
 =(n+1)^9+9(n+1)^8+36(n+1)^7+3(n+1)^6.                 \tag{1}
\]

This is an exact rank construction, not a numerical approximation. It
aggregates 29 independent products; the products do not share input
variables. The proof consists of a uniform centered tensor identity and
an exhaustive finite combinatorial certificate.

The external comparison is Solomonik and Blaeser,
arXiv:2610.26563v2 (2026-10-22), Sections 5.6 and 8.2, file `ex28.txt`:

\[
 r_{28}(n)=(n+1)^9+9(n+1)^8+35(n+1)^7+4(n+1)^6.       \tag{2}
\]

The aggregation, centering, and inclusion-exclusion method are external
prior work. The local contribution is the explicit 29-product family
and its cost comparison. No global priority or optimality is claimed.
The proof is written and unreviewed. There is no new bound below 9/4.

## 1. Exact finite certificate

Let F = {0,...,8}. Each row t in `witness_29.json` gives an ordered
partition `(U_t,V_t,W_t)` of F, with three coordinates in each part.
The parts specify omitted coordinates of the three input factors.
For an ordered mixed triple `(i,j,k)`, let

\[
 \eta_r(i,j,k)={\bf1}_{r\in U_i}+{\bf1}_{r\in V_j}
                         +{\bf1}_{r\in W_k}.
\]

The set-based verifier checks every one of the 29^3 = 24,389 triples:

| Class | Count | Treatment |
| --- | ---: | --- |
| Diagonal i=j=k | 29 | Desired matrix products |
| Off-diagonal, some eta_r=2 | 23,072 | Centering kills the coefficient |
| Off-diagonal, no eta_r=2 | 1,288 | Replicated-coordinate corrections |
| Off-diagonal, every eta_r=1 | 0 | These would be an invalid extra product |

The last two rows overlap only in their descriptions of the test, not
in their counted terms: the fourth row is an additional zero-count
failure check. For every surviving off-diagonal triple, the replicated
set

\[
 R_{ijk}=U_i\cap V_j\cap W_k
\]

is nonempty. The collection Q of all nonempty subsets of such sets has
9 singletons, all 36 pairs, and exactly these three triples:

\[
 \{1,3,4\},\quad\{1,5,8\},\quad\{3,5,7\}.           \tag{3}
\]

The complete Q is exported, rather than inferred from an advertised
cost. The verifier recomputes it and checks the cancellation coefficient
of every one of the 1,288 terms. It uses Python sets and membership
counts; discovery used C++ integer masks. These are separate
implementations, not independent mathematical review.

## 2. Rational centered dual embeddings

Put x=n+1. Define the x by n matrix E whose first n rows form the
identity and whose last row consists of minus ones. Put

\[
 G=E^{\mathsf T}E=I+{\bf1}{\bf1}^{\mathsf T},\qquad
 G^{-1}=I-\frac1{x}{\bf1}{\bf1}^{\mathsf T},\qquad
 D=EG^{-1}.                                            \tag{4}
\]

Both E and D have column sums zero, and `E^T D=I`. All coefficients
belong to Q. Thus these maps exist over every characteristic-zero field.
They also work in other characteristics whenever x is nonzero, but
that extension is not needed for the stated theorem.

For a product t, its X variables carry coordinates outside U_t, its Y
variables coordinates outside V_t, and its Z variables coordinates
outside W_t. Each original coordinate has dimension n. Apply E or D
independently on each active coordinate, giving arrays with local
dimension x. For a coordinate present in two factors of a diagonal
product, apply E to the earlier factor in the order X,Y,Z and D to the
later factor. In particular, X always uses E and Z always uses D; Y
uses E on U_t and D on W_t.

Because `E^T D=I`, the diagonal trilinear contraction of the transformed
arrays is exactly the original one. Grouping the three sets of three
coordinates identifies it with `M(n^3,n^3,n^3)`.

## 3. Aggregates and correction identity

For any coordinate subset P, define A(P) by summing over assignments
of x possible values to the coordinates in F minus P. Its first factor
is the sum of the transformed X arrays from products satisfying
`P subset U_t`; its second factor uses products satisfying
`P subset V_t`; its third uses `P subset W_t`. Each array is evaluated
on its active coordinates, which are disjoint from P.

This definition is a sum of at most x^(9-|P|) products of one linear
form in each input group. Consequently

\[
 R(A(P))\le x^{9-|P|}.                                \tag{5}
\]

Consider the tensor

\[
 A(\varnothing)+\sum_{P\in Q}(-x)^{|P|}A(P).          \tag{6}
\]

Expand it by the independent product labels `(i,j,k)`. If some
coordinate has eta=2, it appears in just one of the three transformed
arrays. Summing that coordinate gives zero, since both E and D are
centered. No correction can delete this coordinate: a correction P
contributes to this triple only when `P subset R_ijk`, where eta=3.
Thus the term vanishes in every contributing aggregate.

For a triple with no eta=2, the only coordinates deleted by a
contributing correction are replicated coordinates. Let R=R_ijk.
They appear in none of the three arrays, so A(empty) has a factor
x^|R|, and A(P) has the corresponding factor x^(|R|-|P|).
After the scalar in (6), every contributing term is therefore the same
residual contraction multiplied by `(-1)^|P| x^|R|`.

For an off-diagonal survivor, R is nonempty and Q contains all its
nonempty subsets. Its coefficient is

\[
 x^{|R|}\sum_{P\subseteq R}(-1)^{|P|}
   =x^{|R|}(1-1)^{|R|}=0.                              \tag{7}
\]

For a diagonal triple R is empty. Only A(empty) contributes, and
Section 2 identifies that contribution with the required matrix
product. There are no other compatible off-diagonal triples by the
finite certificate. Equation (6) is therefore exactly the direct sum
of the 29 desired tensors. Summing (5) over the correction counts
proves (1) for every n in the stated field model.

## 4. Strict uniform improvement in cost per output

From (1) and (2), for x=n+1,

\[
 29r_{28}(n)-28r_{29}(n)
   =x^6(x^3+9x^2+7x+32)>0.                             \tag{8}
\]

Thus `r29/29 < r28/28` for every positive n. The added total cost of
one extra output is only

\[
 r_{29}(n)-r_{28}(n)=x^6(x-1).                         \tag{9}
\]

This comparison concerns the two stated upper bounds. It does not
assert optimal rank, a runtime improvement, or a better strategy for
every requested batch size. At n=19 the two budgets are respectively
788,672,000,000 and 787,456,000,000 scalar multiplications, for 29 and
28 outputs. Encoding and additions are outside this bilinear count.

## 5. Consequence for the exponent target

The external asymptotic sum inequality turns (1) into

\[
 \omega\le\frac{\log(r_{29}(n)/29)}{3\log n}
 \quad(n\ge2).
\]

There is an exact all-n reason that this displayed budget cannot reach
9/4 by this substitution. Weighted AM-GM gives

\[
 n+1=\frac n3+\frac n3+\frac n3+1
 \ge 4\left(\frac n3\right)^{3/4}.
\]

Therefore `r29(n) >= (n+1)^9 > 29*n^(27/4)` for every real n>0.
The strict step is certified by the integer identity

\[
 4^{36}-29^4\,3^{27}
 =4{,}716{,}973{,}042{,}654{,}866{,}123{,}349>0.
\]

This is a lower bound on the value of the **stated upper-bound
polynomial**, not a lower bound on the true tensor rank or on omega.
It rules out extracting an improved exponent from this cost formula
alone, at every local dimension.

For example, the floating evaluation at n=19 is about 2.719966, far
above the current 9/4 baseline. This decimal is only an illustration
of the distance to the target; the exact tensor identity and cost
comparison do not depend on it.

The family is a concrete positive construction in the independent
multiple-target direction. No restriction of a polynomial source to
this family is supplied, and no critical 9/4 cost certificate is
violated. A new link or a substantially stronger family would be
required to turn this kind of ingredient into a smaller exponent.
The existing shared-input partial-transpose note remains distinct and
retains its source credit and obstruction scope.

## 6. Reproduction and evidence

From the repository root:

```sh
python research/ai/2026-10-23-aggregation-families/verify.py
python -m unittest discover -s tests -p test_aggregation_families.py -v
```

The acceptance check is deterministic, exact, and needs only the
Python standard library. Discovery is optional; the verifier can
export the attributed external seed in the mask format used by the
C++ search. See README.md for those commands and the completed search
coverage. No optimizer result or floating residual is an acceptance
premise. The imported baseline and its hash are recorded in
`sources.json`.
