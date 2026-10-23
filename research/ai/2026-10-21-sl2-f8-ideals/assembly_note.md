# A conditional packet sum and its dense coordinate obstruction

October21,2026. AI-SL2-F8-ASSEMBLY-022 and AI-GROUP-DENSE-COORDINATE-023.
Written conditional implication and obstruction, unreviewed. No improved
arithmetic exponent is established.

## 1. The missing simultaneous degeneration

Consider one copy of the complex SL(2,F8) group-algebra tensor. The selected
simultaneous target is

```
D = 2*M(8,9,9) direct_sum 2*M(9,8,9) direct_sum 2*M(9,9,8)
                   direct_sum M(7,7,7).                    (1)
```

Its three leg dimensions are all499; the source dimensions are504.
The previous note supplies the individual punctured packets and a separate
M7 control. Their simultaneous realization in(1) is missing. An individual
source realization for every block does not supply one joint realization.

If a general complex tensor degeneration from this one source to D existed,
then omega<=56/25=2.24, with the usual exact division-free complex-field
circuits of cost O(n^(56/25+epsilon)) for every fixed positive epsilon.
No such degeneration has been constructed here.

## 2. Complete conditional exponent implication

Schönhage's asymptotic sum inequality and border conversion give, for a
joint degeneration to rectangular matrix blocks,

```
sum_blocks (a*b*c)^(omega/3) <= sum_source d_i^omega.       (2)
```

The external sources retain their credit: Schönhage,
[*Partial and Total Matrix Multiplication*](https://doi.org/10.1137/0210032)
(1981), and the existing Bini border-conversion bridge. For the simultaneous
group-algebra comparison in the ordinary case see Cohn, Kleinberg, Szegedy
and Umans, [*Group-theoretic Algorithms for Matrix Multiplication*](https://arxiv.org/abs/math/0511460),
Theorem5.5. Passing to border degenerations uses the same interpolation
and tensor-power overhead already recorded in the repository's bridge.
The model is over C; F8 indexes a finite group and is not the coefficient
field of the arithmetic circuits. No auxiliary factor is cancelled.

For(1), divide the difference of the two sides by9^s and put

```
F(s)=6*(8/9)^(s/3)-3-3*(7/9)^s-(8/9)^s-(1/9)^s.
```

The integer interval certificate at tau=56/25 and scale10^10 gives

```
source upper numerator = 8308262316124
target lower numerator = 8323212635541
strict difference      =   14950319417 > 0.
```

Thus F(tau)>0. For0<s<=9/4, its derivative is positive. Indeed,
log(9/7)>2/9, log(9/8)<1/8 and (7/9)^s>(7/9)^3 imply

```
F'(s) > 3*(2/9)*(7/9)^3-2*(1/8) = 557/8748 > 0,
```

after dropping the other positive derivative terms and bounding the one
negative term. The existing external9/4 theorem gives omega<=9/4. If
omega>=tau, monotonicity would give F(omega)>0, contradicting(2). Hence
the missing degeneration would imply omega<tau, and in particular the
stated exponent upper bound with every positive slack.

The inequalities are exact: every source upper interval and target lower
interval is checked by integer powers. The derivative estimate is a
rational strict bound. No decimal optimization is an acceptance step.

## 3. Necessary general rank tests

All full-space Koszul powers pass. The target block multiset is invariant
under tensor-leg permutations, so the253 powers tested using exterior
duality cover every leg ordering. This uses the existing exact matrix
Koszul formula and the semisimple padding derivation.

The complete rank-locus profile also passes. If V_r(S) is the affine
variety of source slices of rank at most r, and the target first leg has
dimension M inside source dimension N, a general necessary inequality is

```
dim V_r(S)-dim V_r(T) <= N-M.                              (3)
```

For a first-leg restriction, intersect V_r(S) with the M-dimensional input
subspace. The projective dimension theorem gives affine dimension at
least dim V_r(S)-(N-M) whenever this is positive. Maps on the remaining
legs do not increase matrix rank. The rank-locus fiber in fixed target
projective space cannot lose dimension at the limit, by upper
semicontinuity for this proper family. This proves(3); if its right-side
dimension lower bound is nonpositive, the assertion is automatic. This
extends the existing minimum-rank source-locus argument, with the same
complex-field and degeneration hypotheses.

For rectangular direct-sum blocks, a rank-k input matrix in an a-by-b
block costs slice rank c*k and has locus dimension k*(a+b-k). Exact integer
dynamic programming computes the whole profile. All505 rank budgets
satisfy(3), with N-M=5. These necessary tests do not construct D.

## 4. Positive marginal completion for a dense Latin tensor

The following elementary quantitative lemma excludes a coordinate assembly
of(1). It is a locally written completion argument, with no claim of
historical priority for fractional marginals or the Neumann-series method.

Let a Latin tensor have N labels in each leg, with exactly one supported
triple for each pair of labels. Select m=N-k labels in each leg. Prescribe
probability marginals a,b,c on those selected labels, each between
(1-eta)/m and(1+eta)/m. If

```
3*(k+m*eta) < N-6*k,                                      (4)
```

then a strictly positive distribution on every remaining supported triple
has exactly those marginals. Writing E for the number of remaining edges,
every edge mass can be at least

```
[1-3*(k+m*eta)/(N-6*k)]/E.                                (5)
```

Here is a proof. Every selected vertex has degree d_v between N-2k and m.
Let A be the vertex-edge incidence matrix. Its Gram matrix has diagonal
blocks D=diag(d_v); each off-diagonal block B is an all-ones matrix minus
a zero-one matrix with row and column sums at most k.

Work on vertex potentials whose d-weighted mean is zero separately in
each leg. Cross operators D^-1*B preserve these three zero-mean spaces,
since B has the appropriate row and column degrees. If u has weighted
mean zero in one leg, writing d_v=m-r_v with0<=r_v<=k gives
abs(sum_v u_v)<=k*norm(u)_infinity. A row of B then has absolute value at
most2k*norm(u)_infinity. Each cross operator consequently has norm at most
2k/(N-2k), and the sum of its two off-diagonal operators has norm at most
4k/(N-2k).

Start with edge mass1/E and let delta be the difference between the desired
and resulting vertex marginals. Its total is zero on each leg. The operator
D^-1*A*A^t is I+R on the weighted zero-mean spaces, with norm(R) bounded
as above. Condition(4) implies N>6k, so its Neumann inverse exists and the
equation A*A^t*u=delta has a solution there with

```
norm(u)_infinity <= norm(delta)_infinity/(N-6k).
```

Add A^t*u to the uniform edge masses. This corrects the marginals exactly.
Every edge changes by at most3*norm(delta)_infinity/(N-6k). Since the
average degree E/m differs from each degree by at most k,

```
E*norm(delta)_infinity <= k+m*eta.
```

This proves(5), which is strictly positive under(4). The correction has
total mass zero. All assertions are finite-dimensional; rational input
data also admit a rational solution. A test independently solves the
full rational marginal equations in a cyclic order-thirteen example
with different deleted labels and nonuniform marginals.

## 5. The conditional target requires input mixing

Suppose(1) were obtained by choosing499 distinct group basis labels per
leg and applying diagonal weights to them, with no input mixing or
coalescing of labels. Give each punctured block target mass75/499 and
the M7 block mass49/499. These masses sum to one. Uniform distributions
inside the matrix blocks then have marginal values, relative to1/499,
equal to25/24,25/27 or1. Thus eta=2/27 is enough in every leg.

The group multiplication tensor is Latin. With N=504,k=5,m=499,
condition(4) reads1133/9<474. The positive mass factor in(5) is3133/4266.
The selected source support therefore has a strictly positive distribution
with exactly the target's marginals, for every choice of the499 labels.

A diagonal degeneration has nonnegative weight on every selected source
edge and weight zero on every intended target edge. The target distribution
has average weight zero. The strictly positive source distribution with
the same marginals has the same average. Consequently every selected
source edge must have weight zero. Yet every source vertex has degree at
least494, whereas every target matrix-unit vertex has degree at most9.
There are unavoidable unwanted source edges, which cannot survive at
weight zero. This is a contradiction.

Therefore injective group-basis coordinate embeddings and diagonal
weights cannot realize(1). Arbitrary linear input mixing and general
complex degenerations remain outside this obstruction. The conditional
2.24 implication remains unproved because its joint source map is missing.
The separately verified local packets are not evidence of that joint map.

## Reproduction

```sh
python research/ai/2026-10-21-sl2-f8-ideals/packet_assembly.py --output results/local/sl2-f8-packet-assembly.json
python -m unittest discover -s tests -p test_sl2_f8_packet_assembly.py -v
```

The maintained test also performs an independent exact rational marginal
solve, checks all interval powers and verifies the strict positivity bound.
