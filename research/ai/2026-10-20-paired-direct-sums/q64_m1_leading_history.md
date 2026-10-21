# M1 leading points in the Q(6,4) Laurent search

The two bounded searches recorded here did not produce an exact
degeneration. They isolate two useful structural facts: a sparse
leading point has insufficient first-order support, and an endpoint
leading point from the exact Q(5,4) construction passes that support
test. Letting either leading point move did not solve the full tensor
coefficient equations.

The source and target conventions are

\[
Q(6,4)=\sum_{p,q<6;\ y,v<4}
 A_{p,q}B_{y,q+v}C_{p+y,v},\qquad
M(5,4,5)=\sum_{i,k<5;\ j<4}a_{i,k}b_{i,j}c_{j,k}.
\]

Source indices are `6*p+q`, `9*y+s`, and `4*z+v`.
Target indices are `5*i+k`, `4*i+j`, and `5*j+k`.
Both searches have auxiliary rank zero.

## The prescribed row powers

Outer index zero is the old block. Give each map row the Laurent power

\[
w_A(i,k)=-[i>0]-[k>0],\quad
w_B(i,j)=[i>0],\quad w_C(j,k)=[k>0].
\]

The resulting coefficient counts, by powers \(-2,-1,0,1,2\), are
\(256,2176,5136,2176,256\). All 7,568 nonpositive coefficient positions
are required equations. This includes every unwanted coefficient, not
only the 100 target monomials. Positive coefficients may remain.

The old B and C rows define a linear map
\(H_0:\mathbb C^{36}\to\operatorname{Mat}_4\).
For a successful monomial-row map, the 24 non-old A rows are independent
and lie in \(K_0=\ker H_0\). Thus \(\operatorname{rank}H_0\le12\)
is necessary in this model. The 16 corner rows must further annihilate
the first-order cross map \(H_1\), so
\(\operatorname{rank}(H_1|_{K_0})\le\dim K_0-16\).
For either exact leading point below, \(\dim K_0=32\), giving the
necessary bound 16.

These statements concern the specified monomial row powers. They do not
exclude arbitrary Laurent families with different leading cancellations.

## Exact sparse leading-point obstruction

For \(y,v\in\{0,1\}\), set old middle index \(j=2y+v\) and take

\[
b_{0,j}\leftarrow B_{y,v},\qquad
c_{j,0}\leftarrow C_{y,v},\qquad
a_{0,0}\leftarrow A_{0,0}.
\]

This gives an exact leading \(M(1,4,1)\). Its four independent source
slices are supported on \(p,q<2\), and \(H_0\) has rank four.

Consider the first-order target edge \(a_{i,0}\), \(i>0\). Its
leading A vector lies in \(K_0\). In a term using the fixed old C map,
one must have \(p+y\le1\) and \(v\le1\). Therefore \(p,y\le1\).
Membership in \(K_0\) then forces \(q\ge2\). All such edge
contributions consequently lie in the span of the ten source B columns

\[
B_{y,s},\qquad y\in\{0,1\},\quad s\in\{2,3,4,5,6\}.
\]

The four required target edge slices together have B flattening rank
\(4\cdot4=16\). A linear map from this ten-dimensional source support
cannot produce that rank. Hence this **fixed** leading point cannot be
extended in the stated row-power chart. Higher coefficients respecting
the same lower row powers cannot alter this first edge coefficient.
The symmetric argument applies on C.

More generally, the same fixed sparse seed for
\(Q(n,4)\to M(n-1,4,n-1)\) has first-edge support at most
\(2(n-1)\), while the target requires \(4(n-2)\). The strict
inequality excludes this seed for every \(n\ge4\). This is a support
argument over any field. The accompanying rational checks verify the
support ranks at \(n=3,4,5,6\).

## Endpoint leading point and the inherited first jet

The second point is obtained from the previously certified integer
[Q(5,4) to M4 restriction](../2026-10-20-paired-construction/outer_product_injection.md).
Embed its source indices into Q(6,4) and retain its old outer row and
column zero as the leading block. The old B rows are

\[
B_{0,1},\quad B_{0,0}+B_{0,4},\quad
B_{3,1},\quad B_{3,0}+B_{3,4};
\]

the old C rows are

\[
C_{1,0},\quad C_{1,3},\quad
C_{0,0}+C_{4,0},\quad C_{0,3}+C_{4,3}.
\]

Again \(H_0\) has rank four. Each first-edge source flattening now has
rank 32. Thus the preceding ten-versus-sixteen obstruction does not
apply to this point.

Writing \(f(X)=(X_1,X_0+X_4)\), its source quotient is
\(f\otimes f\). Define

\[
P=\ker f=\langle1-t^4,t^2,t^3,t^5\rangle.
\]

Using all three inherited non-old outer rows of the exact M4 map,
the separate integer/rational computation gives

\[
\operatorname{rank}H_0=4,\qquad
\operatorname{rank}(H_1|_{K_0})=16,\qquad
\ker(H_0,H_1)=P\otimes P.
\]

All six inherited edge slices reconstruct exactly. The remaining kernel
has dimension 16. These ranks identify the corner that a fourth-row
extension of those fixed inherited maps would need to use. The resulting
corner tensor is excluded even from degenerating to M4 by the separate
[endpoint corner obstruction](../2026-10-20-paired-construction/m1_endpoint_corner.md).
Consequently, passing the first-edge support test does not provide a
construction. Moving the first-order maps so that their corner kernel
changes is a different search.

## Two completed moving-leading pilots

Both runs used complex coefficients, all 24 non-old A rows and all
source columns of the B and C maps as free variables, a Frobenius norm
bound 30 on each complete map, and 1,500 ALS updates. The old leading
maps were initialized exactly but were allowed to move during fitting.
The target gauge used upper triangular physical outer transformations
and an unrestricted middle transformation. This preserves the exact
row-power acceptance equations while changing their numerical norms.

The sparse run used seed 202610451. The product run used seed 202610452:
it started from the embedded exact M4, extended its first-map product
space by \(t^5\), and randomized only the fourth outer B and C rows.
The saved artifacts contain every complex map coefficient and every
retained sampled record, including the actual 1,500-update stops.

| Initialization | Best sampled update | Best required relative error | Final relative error |
|---|---:|---:|---:|
| Sparse leading point | 700 | 0.117524459634 | 0.140701616594 |
| Endpoint product leading point | 1400 | 0.073039696741 | 0.077074460452 |

The normalization is the Frobenius error on the 7,568 required positions
divided by \(\|M(5,4,5)\|_F=10\). At the saved sparse point, the pole
norm is 0.9999866 and the constant coefficient error is 0.6174356.
At the saved product point they are 0.6390409 and 0.3537039. These are
failed equations, not approximate certificates.

Both saved points also have numerical leading rank 16. The singular-value
tail after the necessary rank 12 is 0.2677878 and 0.1394734, respectively.
The endpoint initialization therefore did not prevent leading-rank drift
when all leading maps were free.

Minimizing map norm over the full physical diagonal target orbit gives
required relative errors 0.2903847 and 0.0962109. This shows that part of
the smaller raw errors depends on the current gauge. The three resulting
map norms are equal, approximately 26.3473 and 29.3217 for the two points.
The diagonal stationarity residuals are below \(3\cdot10^{-16}\).

In the operator regrouping, the physical weights have only the three
levels \(-1,0,1\). Exact acceptance would make \(E=T-I\) satisfy
\(E^3=0\). The saved points fail this necessary condition as well.
The cube norm is recorded as a diagnostic; it is not a distance to the
set of nilpotent tensors. The extracted strictly positive part cubes to
zero, checking the degree convention separately from the failed maps.

## Reproduction and status

Exact gates and embedded M4 coefficients use only the standard library:

```sh
python -S research/ai/2026-10-20-paired-direct-sums/q64_m1_leading_exact.py
python -S -m unittest discover -s tests -p test_q64_m1_leading.py -v
python -S research/ai/2026-10-20-paired-direct-sums/q64_experiment_replay.py \
  results/paired-direct-sums-2026-10-20/q64-m1-sparse-checkpoint.json \
  results/paired-direct-sums-2026-10-20/q64-m1-product-checkpoint.json
```

Optional discovery and numerical conditioning diagnostics require NumPy:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  research/ai/2026-10-20-paired-direct-sums/q64_m1_leading_search.py \
  --seed-kind product --seed 202610452 --iterations 1500 \
  --norm-budget 30 --prefix /tmp/q64-m1-product
```

The initial numerical arrays can be regenerated exactly in the recorded
runtime from the seeds and the maintained integer source certificate.
Different numerical linear algebra runtimes can follow different floating
point trajectories. The portable saved-coefficient replay is the check on
the reported finite points.

The [ridge history correction](q64_ridge_metadata_correction.md) explains
the repaired sampled regularization metadata. It does not change these
maps or any coefficient error. Neither numerical search proves a tensor
degeneration, a global obstruction, or a smaller matrix multiplication
exponent.
