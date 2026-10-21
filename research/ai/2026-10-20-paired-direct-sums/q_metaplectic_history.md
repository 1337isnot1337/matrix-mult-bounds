# Nonlocal long-map probes and an exact product-projection reference

Three bounded ordinary-map searches in a twelve-operator space found
no exact restriction. Two return to the product projection with
relative errors sqrt(19)/10 and sqrt(11)/6. A Fourier/chirp-dominant
start reaches a different failed point, but its source row spaces
also numerically factor through product subspaces. The rational
projection identity below explains the first two error values without
certifying any saved floating-point map as exact.

## Operator space and complete coefficient objective

The source is

\[
Q(n,4)=\sum_{p,q<n;\ y,v<4}A_{p,q}B_{y,q+v}C_{p+y,v}.
\]

Set r=n-1 and m=n+3. The target is M(r,4,r), with first indices
`r*i+k` and long indices `4*i+j`, `r*j+k`. Let E_v send e_q to
e_(q+v). In the native source slice, the block indexed by y,v is
E_v A^T E_y^T. Each of the sixteen blocks of a long map is an
r by m matrix.

We restrict these long blocks to the span of twelve specified matrices:
the two product inverse operators described below, followed by the
first r rows of

\[
I,\ J,\ F,\ F^{-1},\ G,\ G^{-1},\ FG,\ FG^{-1},\ GF,\ G^{-1}F.
\]

Here F is the m-point Fourier matrix with entries
exp(2 pi i s t/m)/sqrt(m), J reflects an index modulo m, and G is the
diagonal chirp with entries exp(pi i s squared/m). Their dimensions and
phases vary with n. This is a nonlocal operator probe, not a fixed-period
local filter. The twelve matrices are orthonormalized before fitting,
so each complete long-map Frobenius norm equals the norm of its block
coefficient array.

The first map is unrestricted and is solved linearly at each ALS step.
At n=6 it has 900 complex parameters, at n=7 it has 1,764; each long
map has 192. Every coefficient is required: 10,000 positions for n=6
and 20,736 for n=7. No off-diagonal or boundary coefficients are omitted,
and every source has auxiliary rank zero. An unbounded exact version
would be relevant to the project's
[near-full correction criterion](../2026-10-21-correction-budget/README.md);
these finite failed searches do not establish it.

Each run has a complete-map norm budget 25 and exactly 1,000 ALS updates.
The physical middle GL4 gauge and global mode balancing preserve the
operator ansatz and target. Unrestricted outer gauges are not used.
The saved points retain all map entries, operator coefficients, basis
entries, sampled ridge parameters, and the actual stop.

## Completed experiments

| n | Initialization | Seed | Best relative full error | Long numerical ranks | Map norms at saved point |
|---:|---|---:|---:|---|---|
| 6 | Product inverse plus nonlocal perturbation | 202610461 | 0.435889894354 | 18, 18 | 5.01330 each |
| 7 | Product inverse plus nonlocal perturbation | 202610462 | 0.552770798393 | 20, 20 | 5.36011 each |
| 6 | Fourier/chirp-dominant blocks | 202610463 | 0.606947683016 | 18, 18 | 15.09677 each |

All three complete the prescribed 1,000 updates. The first two saved
best sampled points are at updates 150 and 125; subsequent changes
in their reported errors are at floating-point precision. The third
saved point is at update 1,000.

The first two initializations use the product outer space

\[
U=\langle t,t^2,\ldots,t^{n-2},1-t^{n-1}\rangle
\]

and inner space W=span(1,t3), with a perturbation of norm scale 0.15
in the other operator directions. Both initial long maps have full
target rank. The additional operator coefficients decay to about
1e-12, and the maps return to the product span.

The third start uses no explicit product inverse in its raw long blocks.
For the six operators O=(F,F inverse,FG,FG inverse,GF,G inverse F),
its initial B block is i^(alpha*y) O_((alpha+2y) mod 6)/2; the C block
is i^(-beta*v) O_((2beta+v+3) mod 6)/2. A small perturbation of scale
0.03 breaks the finite block symmetry. Its first map is the bounded
linear least-squares solution for those long maps. Product inverse
directions remain permitted during the fit.

This third run keeps substantial nonproduct operator coefficients,
with norms approximately 14.679 and 14.512. Nevertheless, the
orthonormal source row-space diagnostics identify the same broader
product geometry. Its A row space has two outer partial flattenings
with five singular values sqrt(5) and remaining singular values below
1.5e-11. Each long source row space has inner dimension two and uses
the complete nine-dimensional polynomial-output space, to residual
partial singular values below 4e-11.

These are numerical factorization diagnostics with relative rank
threshold 1e-8. They do not prove exact factorization of the saved
floating coefficients. They also do not exclude other points in this
operator space or arbitrary nonlocal maps. No further starts in this
finite basis are included.

## Exact rational reference for the product loss

Let n be at least five, r=n-1, and m=n+3. Multiplication

\[
U\otimes W\longrightarrow\mathbb Q[t]_{<m}
\]

has input dimension 2r and output rank m. Its only dependencies are
the n-5 duplicate monomial pairs

\[
t^{i+1}\cdot t^3=t^{i+4}\cdot1,\qquad 0\le i<n-5.
\]

The two products involving 1-t^(n-1) have unique lowest and highest
coefficients, and all other distinct monomials are independent. This
proves the asserted rank and complete list of dependencies.

Let D list these products as rows. The explicit rational dual L in
`q_product_projection.py` satisfies D^T L=I_m. Its input projection
P=L D^T is symmetric and idempotent. It is the identity on independent
input coordinates and the matrix with all four entries 1/2 on each
duplicate pair. Thus rank(P)=m, and all coefficients are rational.

Use this dual on both long legs of Q(n,4), retaining only native inner
coordinates zero and three, and use U tensor U on the first leg.
The complete resulting tensor, after a permutation of indices, is
P tensor P. Under the same permutation the desired matrix tensor is
I_(2r) tensor I_(2r). Therefore

\[
\|T_{\rm ref}\|_F^2=m^2,\qquad
\langle T_{\rm ref},M\rangle=m^2,\qquad
\frac{\|M-T_{\rm ref}\|_F^2}{\|M\|_F^2}
=1-\frac{(n+3)^2}{4(n-1)^2}.
\]

The exact rational verifier checks the full paired coefficient formula,
including every zero entry, at n=5,6,7. The squared coefficient errors
are respectively 0,19,44, with squared relative errors 0,19/100,11/36.
The n=5 member is the previously known product-injection calibration.
Only that member reaches the full matrix target. The error tends to
sqrt(3)/2 as n grows. Agreement of a numerical error with this formula
does not identify or exactify the numerical maps.

### This fixed reference needs a quadratic additive correction

Let d=n-5 and E=M-T_ref. In its first flattening, select A rows (i,k)
with i,k<d and long columns B_(i,3) C_(3,k). Both binary middle indices
are one, so the off-diagonal links of a duplicate pair are absent.
The selected submatrix is exactly (3/4) I_(d squared). Consequently

\[
\underline R(E)\ge\operatorname{rank}(E_A)\ge(n-5)^2.
\]

The first inequality follows because a sum or limit of r rank-one
tensors has flattening rank at most r. Thus an O(n) additive repair
cannot correct this particular family while leaving its mapped tensor
fixed. This formalizes the product-projection repair limitation; it is
not an obstruction to jointly changing the maps and auxiliary tensor.

## Verification and retained evidence

The two standard-library tests verify the rational reference at all
34,832 coefficient positions across n=5,6,7 and the explicit repair
minors. They also compare all 123 sampled records against the retained
original emitted JSON records and check the complete 1,000-update stops.
Each history stores a copied ridge list, so no sampled regularization
value is replaced by a later update.

The complete saved floating-point coefficient replays cover 40,736
positions across the three searches. Their reported relative errors
agree within 1.2e-16. The optional controls check the known n=5 integer
map in the numerical operator layout, all three block designs with
all operator directions active, and byte-for-byte regeneration of the
three original initial arrays in the recorded numerical runtime.
Initialization checks repeat zero optimization updates.

```sh
python -S -m unittest discover -s tests -p test_q_product_projection.py -v
python -S research/ai/2026-10-20-paired-direct-sums/q_product_projection.py
python -S research/ai/2026-10-20-paired-direct-sums/q_metaplectic_replay.py \
  results/paired-direct-sums-2026-10-20/q-metaplectic-n6-checkpoint.json \
  results/paired-direct-sums-2026-10-20/q-metaplectic-n7-checkpoint.json \
  results/paired-direct-sums-2026-10-20/q-metaplectic-n6-nonproduct-checkpoint.json
```

Optional NumPy controls, diagnostics, and discovery:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  research/ai/2026-10-20-paired-direct-sums/q_metaplectic_controls.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  research/ai/2026-10-20-paired-direct-sums/q_metaplectic_blocks.py \
  --n 6 --seed 202610461 --iterations 1000 --norm-budget 25 --prefix /tmp/q-meta6
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  research/ai/2026-10-20-paired-direct-sums/q_metaplectic_blocks.py \
  --n 7 --seed 202610462 --iterations 1000 --norm-budget 25 --prefix /tmp/q-meta7
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  research/ai/2026-10-20-paired-direct-sums/q_metaplectic_nonproduct.py \
  --prefix /tmp/q-meta-nonproduct
```

Different numerical linear algebra runtimes may follow different
trajectories or produce different initial floating-point array hashes.
The standard-library replays establish the stated finite evidence.
There is no new exact matrix multiplication algorithm or exponent
improvement in these three searches.
