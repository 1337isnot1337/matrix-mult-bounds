# Necessary tests for the finite convolution target

AI-derived calculations and written proofs, October 20, 2026; unreviewed.
No smaller exponent or new degeneration is established. This continues
[the finite target](finite_amplitude.md): let S_a be the tensor product of
all six leg permutations of C(a,a), and V_a=a^2(2a-1). Each leg of S_a has
dimension V_a^2. A degeneration S_4 to M(106,106,106) would imply
omega<=2.249, but remains unconstructed.

## 1. Every singleton quantum functional passes the target

Work over C. For positive a,b set A=a-1, B=b-1, and m=A+B+1. Apply
invertible diagonal maps to C(a,b) so its coefficient at (i,j,i+j) becomes
the positive square root of

    p_(i,j) = binom(A,i) binom(B,j) / [m binom(A+B,i+j)].     (1)

This is possible by scaling the first two coordinates by square roots of
the numerator binomials and output k by 1/sqrt(m binom(A+B,k)).
Vandermonde's identity gives output marginal 1/m. For the input marginals,
use the elementary beta integral

    1/[m binom(A+B,k)] = integral_0^1 t^k(1-t)^(A+B-k) dt.

Summing (1) over j, the binomial theorem leaves

    binom(A,i) integral_0^1 t^i(1-t)^(A-i) dt = 1/a.

The other input marginal is 1/b. These identities also show normalization.
The reduced density matrices have no off-diagonal entries: any two
convolution support triples agreeing in two positions agree in the third.
Thus all three quantum marginals are exactly uniform.

For nonnegative theta_X+theta_Y+theta_Z=1, the singleton lower quantum
functional is the exponential of the supremum of the theta-weighted
marginal entropy over invertible local maps. Entropy cannot exceed the log
of the leg dimension. The displayed scaling attains all three bounds at
once, proving

    F_theta(C(a,b)) = a^theta_X b^theta_Y m^theta_Z.          (2)

The external definition and the equality with the upper quantum functional
are Definition 3.16 and Theorem 3.30 of Christandl--Vrana--Zuiddam,
[arXiv:1709.07851v3](https://arxiv.org/abs/1709.07851v3), May 26, 2018.
Their singleton functionals are universal spectral points over C. The
inspected PDF has SHA-256
`80da2b563058bfc7d478fc0f47a510692192e0381ab546a09f723801342daf5c`.
The normalization is an elementary rederivation, with no priority claim.

Tensoring the six normalized states gives uniform marginals of dimension
V_a^2. The same entropy upper bound therefore gives F_theta(S_a)=V_a^2.
The normalized square matrix multiplication tensor likewise has uniform
marginals and F_theta(M(n,n,n))=n^2. Consequently the entire singleton
quantum-functional family gives only

    12544 >= 11236

for S_4 to M106. It does not reject this proposed degeneration, even after
taking tensor powers. These functionals are not asserted to exhaust the
asymptotic spectrum. Passing them is not a construction.

## 2. Entropy loss excludes coordinate matrix extraction also at a=5

All entropies in this section use natural logarithms. First let p,q be
independent probability distributions on {0,...,D}, with D>=1, and let r
be their sum distribution on {0,...,2D}. Put m=2D+1. The endpoints and
central coefficient obey

    r_D >= p_0 q_D + p_D q_0 >= 2 sqrt(r_0 r_(2D)).          (3)

Write v for total variation distance from the uniform distribution u on
m entries. Each coordinate differs from 1/m by at most v. If v>=1/m
there is nothing to show; otherwise (3) implies

    1/m+v >= 2(1/m-v), hence v>=1/(3m).

For completeness, Pinsker's inequality here follows from log-sum on the
event {s:r_s>=u_s}. Its binary relative entropy, as a function of its first
probability x with the second fixed at y, has second derivative
1/[x(1-x)]>=4 and value and derivative zero at x=y. Integration gives
KL(r||u)>=2v^2. The endpoint cases follow by continuity. Thus

    H(r) <= log(m)-delta_m,  delta_m=2/(9m^2).               (4)

Now extract a matrix block M(l,h,n) from S_a^q by coordinate injections,
nonzero constant scalars and diagonal weights on all three legs. Let
D=a-1 and m=2a-1. Each source factor is a coordinate restriction of the
group tensor Z/m, with two short labels in [0,D] and the negative of their
sum on the long leg. For each factor, the intended labels admit integer
potentials

    alpha_(i,j)=u_i+v_j,
    beta_(j,k)=-v_j+w_k,
    gamma_(k,i)=-w_k-u_i.                                  (5)

These are integer, rather than just modular, because the intended
convolution equations hold without wraparound. For the displayed ordering
of the two short legs, their widths satisfy

    width(u)+width(v)<=D,  width(w)+width(v)<=D.

If width(v)>=1, the integer sum u+v+w has at most 2D values. Its entropy is
at most log(2D), which is no greater than log(m)-delta_m, since
log(m/(m-1))>=1/m>delta_m. If v is constant, shift u and w separately into
[0,D] and apply (4) to their independent distributions. If the two short
legs occupy a different pair of positions, the common potential in the
two width inequalities is u or w instead; the same argument applies.

Choose i,j,k uniformly and independently. The abelian opposite-relation
argument in [the preceding note](finite_amplitude.md#5-coordinate-maps-with-diagonal-weights-cannot-supply-this-target)
makes their vector sum u_i+v_j+w_k injective modulo m. It is therefore also
injective as an integer vector. Its entropy equals log(l*h*n), whereas
subadditivity over the 6q source factors and the preceding estimate give

    log(l*h*n) <= 6q (log(m)-delta_m).                      (6)

Coordinates of a vertex vector need not be independent; entropy
subadditivity requires no such assumption. The independent variables in
(4) are different matrix vertices within one source factor.

At an endpoint character every matrix block has value (l*h*n)^(3/4).
Let its leg dimensions be L=l*h, H=h*n, N=n*l. By (6),

    (l*h*n)^(3/4)
      <= [m^(6q) exp(-6q delta_m)]^(1/12) (L H N)^(1/3).

For a direct sum of blocks, Holder and the three leg budgets V_a^(2q)
give total character value at most

    [V_a^2 sqrt(m) exp(-delta_m/2)]^q.

Since lambda(S_a^q)=P(a,a)^(9q/2) at the endpoint, this extraction method
cannot force a profile lower bound larger than

    B_a exp(-delta_m/9),  B_a=[a^8(2a-1)^5]^(1/9).          (7)

At a=5, delta_m/9=2/6561. The inequality exp(x)>=1+x bounds (7) above by
B_5*6561/6563. It is strictly below the critical ceiling U_5=28^(4/3)/6:

    6^9 * 5^8 * 9^5 * 6561^9 < 28^12 * 6563^9.            (8)

The earlier bound B_5 alone failed this comparison. Equation (8) now
excludes this all-power direct-sum coordinate-and-weight method also at
a=5. It is a limitation on the method's lower-bound certificate, not an
upper bound on the actual P(5,5). General linear input mixing, arbitrary
Laurent maps and all a>=6 are not excluded by this statement.

The abelian group argument is adopted from the concurrent group worker's
Section 4.1 at `dcfc1ef1f80558c8e7b6c3f8c1f02e4dced94226`. The additional
integer-width and entropy estimates above are local written derivations.

## 3. Arbitrary Laurent output does not rescue the coordinate-input target

Let a source tensor be a coordinate restriction of the tensor of a finite
abelian group G, with d available coordinates on the third leg. Suppose
the maps on the first two legs select distinct source coordinates for each
target coordinate, multiplied by arbitrary nonzero Laurent scalars. Allow
an arbitrary Laurent matrix on the third leg. If its limit is M(l,h,n),
then necessarily

    h(3ln-2d) <= |G|.                                      (9)

As usual the inequality is informative only when its left side is positive.
Also d>=ln follows from conciseness. These hypotheses allow degeneration,
not just constant restrictions, but still require coordinate inputs.

To prove (9), write alpha_(i,j), beta_(j,k) for the input group labels and
their scalar valuations as a_(i,j), b_(j,k). For each desired output (i,k)
let its active set be

    S_(i,k)={alpha_(i,j)+beta_(j,k):j=1,...,h}.

These sets are disjoint. Indeed, a shared source output would give two
desired input valuation sums g,g' and two output-entry valuations c,c'
with g+c=g'+c'=0. The crossed outputs are undesired, so g+c'>0 and
g'+c>0, an impossibility. There is no cancellation because each input pair
has exactly one source contribution. This is the concurrent product
worker's [Laurent active-set lemma](../2026-10-20-mixed-restrictions/laurent_capacity.md#1-disjointness-uses-valuations-not-output-row-weights),
merged in `7d97155`; the same proof applies to the group labels here.

It follows that the number of nonsingleton active sets is at most
E=d-ln. The singleton positions form a bipartite graph on i and k.
Relative to j=1, attach to row i the word of group differences
alpha_(i,j)-alpha_(i,1), together with valuation differences
a_(i,j)-a_(i,1). Attach the analogous word to column k using beta,b.
An edge occurs exactly when these words are negatives. For a singleton,
valuation sums must be equal since every desired pair uses the same output
entry. Conversely opposite words make the group sums constant, hence
give a singleton. Thus the graph is a disjoint union of complete bipartite
components, with possible isolated vertices.

There are at least ln-E edges. If ln-2E<=0 then (9) is automatic. Otherwise
some row has at least n-E/l neighbors. Let its component have r rows and
s columns, so s>=n-E/l. Every one of the l-r outside rows misses all s
columns; hence (l-r)s<=E and

    rs >= ls-E >= ln-2E.                                  (10)

Restrict to these r rows, all h middle vertices, and these s columns.
Each output now has one distinct active source coordinate. Replace its
output row by that entry alone, and replace nonzero Laurent scalars by
their leading monomials. All desired coefficients are retained; each
undesired coefficient is deleted or still has positive valuation. This
produces a three-coordinate-map diagonal-weight degeneration to M(r,h,s).
The adopted abelian opposite-relation lemma gives rhs<=|G|, proving (9).

For S_4, d=12544 and |G|=7^6=117649. In the square case (9) is

    n(3n^2-25088) <= 117649.

The left side is 79887 at n=93 and 133480 at n=94. Its forward difference
9n^2+9n+3-25088 is positive for every n>=94. Thus any square target in
this larger class has n<=93. In particular H106 is excluded because

    106(3*106^2-25088)=913720>117649.

This is an upper bound, not a construction of M93. The earlier n<=49
bound remains stronger within its smaller class of three coordinate maps.
The new result permits arbitrary output mixing but shows that an H106
witness must genuinely mix coordinates in at least one input map.

## Verification

`finite_target_screens.py` checks exact rational marginals, finite
convolution distributions, the integer comparison (8), and (9) at the
selected sizes. Its separate graph check enumerates all four-type row and
column count vectors of total sizes 1 through 6, verifying (10) directly.
The regression tests compare these calculations with the saved report.
These finite checks do not replace the general proofs or independent review.
