# Unequal paired convolution sources

October 20, 2026. AI-derived written proof and exact finite search, unreviewed.
No matrix degeneration or exponent below 9/4 is constructed here.

This extends the earlier equal-source [Koszul formula](../2026-10-20-paired-sources/all_koszul.md)
to two different convolution factors. The cohomological method and the equal-source
argument are adopted from that package. The new content is the unequal formula,
its precise equality range, a universal upper bound, and a smaller finite
construction target.

## 1. Source and rank formula

For positive integers a,b,c,d, define

    Q(a,b;c,d) = C(a,b)_(X,Y,Z) tensor C(c,d)_(X,Z,Y).

Its coefficient tensor and dimensions are

    sum_(p<a,q<c,y<b,t<d) X_(p,q) Y_(y,q+t) Z_(p+y,t),
    v=ac,  Y=b(c+d-1),  Z=(a+b-1)d.

Assume a,c>=2, a<=b+1 and c<=d+1. For the first-leg Koszul map

    K_s: exterior^s(X) tensor Y* -> exterior^(s+1)(X) tensor Z,

the exact rank over every field is

    rank K_s(Q) = Y binom(v-2,s) + Z binom(v-2,s-1)
                   +2(a-1)(c-1) binom(v-3,s-1).             (1)

Binomial coefficients outside their range are zero. At a=b=c=d this reduces
to the earlier equal-source formula. The hypotheses are used for equality;
the exact-rank function rejects inputs outside them. The polynomial remains
an upper bound without either range hypothesis, as proved below.

### Cohomological realization

On X=P^1 times P^1, put A=a-1, C=c-1 and

    L=O(A,C),  F=O(b-1,-c-d).

Multiplication induces

    H^0(L) tensor H^1(F) -> H^1(F+L).

The two-chart cohomology formula gives dimensions v,Y,Z. In monomial bases,
the input x^y z^(-j-1), multiplied by x^p z^q, survives precisely when
j=q+t with 0<=t<d. Its output index is (p+y,t). These are exactly Q's
coefficients. The projective-space cohomology formula is the external result
in the [Stacks Project, tag 01XT](https://stacks.math.columbia.edu/tag/01XT).

Let e_i be the first-leg basis, and form the universal section

    u=sum_i e_i tensor monomial_i(L).

Fix s and take the complex of bundles

    D^k=exterior^(s+k)(X) tensor (F+kL),

with differential u wedge. On every standard product chart, one monomial
section is a unit. Contraction in that coordinate contracts the complex.
Its bounded product Cech double complex therefore has zero total cohomology.
The standard spectral sequence is

    E_1^(k,q)=exterior^(s+k)(X) tensor H^q(F+kL) => 0,
    d_r:(k,q)->(k+r,q-r+1).

This is the bounded double-complex construction from the
[Stacks Project, tag 012X](https://stacks.math.columbia.edu/tag/012X),
as already used in the equal-source proof.

### Why the parameter conditions suffice

Only cohomology rows q=0,1,2 occur. For k>=-1 the first degree of F+kL is
at least b-a>=-1, so the q=2 row is supported only at k<=-2. For k<=2 the
second degree is at most c-d-2<=-1, so the q=0 row is supported only at k>=3.
These are exactly where a<=b+1 and c<=d+1 enter.

Every differential d_r with r>=3 vanishes. The only possible d_3 would start
in q=2 at k<=-2 and land in q=0 at k+3<=1, where the group is zero. On E_2,
the q=2 row can only map by d_2 to the q=1 row at k<=0. The q=1 row at k<=0
has no possible outgoing d_2 to q=0. Since E_3=E_infinity=0, these d_2 maps
are isomorphisms between the nonzero E_2 groups in those regions.

Take Euler characteristics in the entire q=2 row and the q=1 row truncated
at k=0. The differential from k=0 to k=1 in the latter row is K_s. Removing
its image from the last term changes that truncated Euler characteristic by
rank K_s. The E_2 groups in the two regions cancel in pairs under d_2, whose
column shift is even. Thus

    rank K_s = sum_(j>=0) (-1)^j binom(v,s-j)
                   [h^1(F-jL)-h^2(F-jL)].                 (2)

All sums are finite because the exterior power vanishes outside 0,...,v.
There is no h^0 term for j>=0. The Euler characteristic of F-jL is the
product of its two shifted degrees, so the bracket in (2) is

    (b-jA)(c+d-1+jC).

This quantity can be negative; it records h^1 minus h^2, not a dimension.
Multiplying its alternating generating series by (1+z)^v gives

    Y(1+z)^(v-1) + (Z-Y)z(1+z)^(v-2)
                         +2AC z(1+z)^(v-3).

Taking the coefficient of z^s proves (1). No maximal-rank assumption for
an intermediate differential is used.

### Universal upper bound outside the equality range

For every positive a,b,c,d with a,c>=2, the right side of (1) is an upper
bound for rank K_s over every field. It need not be the exact rank. The
program also takes its minimum with the domain and codomain dimensions.

To prove this, retain the same double complex and remove the two range
hypotheses. The q=2 row is now supported at k<=-1, since the first degree
of F+kL is nonnegative for k>=0. The q=0 row is supported at k>=2, since
the second degree at k=1 is -d-1<=-2. Differentials d_r with r>=4 vanish,
and d_3 can only go from position (-1,2) to position (2,0).

Write T_k=E_2^(k,2), M_k=E_2^(k,1), B_k=E_2^(k,0). For k<=-3, the map

    d_2:T_k -> M_(k+2)

is an isomorphism: neither its kernel nor its cokernel can participate in
another differential, and total cohomology vanishes. The chain

    T_(-2) -> M_0 -> B_2

is injective at its first term and exact at its middle term for the same
reason. Thus dim M_0 - dim T_(-2) is rank(d_2:M_0->B_2).

The truncated Euler calculation that led to (2) remains valid as an Euler
expression, even when it is no longer the rank. Its value is

    rank K_s + sum_(k<=0) (-1)^k dim M_k
                     -sum_(k<=-1) (-1)^k dim T_k.

The isomorphisms at k<=-3 cancel paired terms. The remaining expression is

    rank K_s + rank(d_2:M_0->B_2) + dim T_(-1).          (4)

Both correction terms are nonnegative. The same generating-series
calculation gives the right side of (1), proving the bound. Under the
original hypotheses T_(-1) and B_2 vanish, recovering equality. This also
explains why extending equality beyond that range was invalid: for example,
Q(4,1;2,2) at s=1 has rank 24 and polynomial value 32.

### An edge-source candidate excluded on its other input leg

The edge source Q(2,1;25,29)=EPR_2 tensor C(25,29), with dimensions
(50,53,58), initially passes every first-leg comparison for M(7,6,7).
However, permuting the legs (X,Y,Z) to (Z,Y,X) gives source Q(2,1;29,25)
and target M(6,7,7), whose first-leg dimensions are 58 and 42.

At s=22 the universal bound and padded matrix formula give

    source rank <= 228031988498086500,
    target rank  = 228398726394095712.

The positive gap 366737896009212 excludes this candidate under arbitrary
tensor degeneration. This comparison uses the upper bound, since c=29 and
d=25 violate the equality condition c<=d+1. It closes the candidate rather
than furnishing a matrix multiplication improvement. The exact certificate
is preserved in `edge-exclusion.json`.

## 2. A finite unequal-source target

The finite search retains outer matrix sizes a,c. Its smallest survivor by
maximum source-leg dimension is

    Q(10,9;12,12) -> M(10,14,12).                         (H)

| Tensor | First leg | Second leg | Third leg |
| --- | ---: | ---: | ---: |
| Source | 120 | 207 | 216 |
| Target | 120 | 140 | 168 |

All 120 first-leg Koszul comparisons pass with strict slack. This is smaller
than the previous equal-source survivor P_14, with dimensions (196,378,378).
It is not a statement about the smallest target among every possible source
or every matrix shape. **The degeneration (H) is unconstructed.**

The matrix comparison uses the existing characteristic-free
[matrix Euler formula](../2026-10-20-paired-sources/matrix_euler.md).
The preserved target certificate records every source and target rank.

### Conditional exponent implication

The existing shifted-tripling and two-sector constructions imply, for every
character with t>0,

    6 P(a,b) <= [3(a+b)-2]^(1/t).                         (3)

Indeed, tripling gives P(a,3b+a-1)>=3P(a,b); apply the two-sector inequality
to the reversed dimensions (3b+a-1,a). This adopts the two constructions
used in [finite_amplitude.md](../2026-10-20-koszul/finite_amplitude.md).

Take all six leg permutations of (H), tensor them together, and use character
monotonicity and multiplicativity. The result is

    P(10,9) P(12,12) >= 10*14*12 = 1680.

The six-permutation product removes the oriented dot-product parameters;
each matrix dimension occurs with exponent 6t. Equation (3) would then give

    60480^t <= 3850,
    omega <= 3 log(3850)/log(60480) < 22496/10000.

The last strict comparison has the integer certificate

    60480^22496 > 3850^30000.

The descriptive real bound is approximately 2.2495306348. Both numbers are
conditional on (H), whose construction is the missing premise. The external
detecting-character theorem and the 9/4 baseline remain OpenAI's work.

### Two additional scope checks

Every nonzero first slice of Q(a,b;c,d) has rank at least bd. Choose the
lexicographically first nonzero coefficient X_(p0,q0), then use rows
(y,q0+t) and columns (p0+y,t). Ordered first by y and then by t, the resulting
bd-square minor is block triangular, with determinant X_(p0,q0)^(bd).
This is the triangular-minor method already used for the equal paired source.

An ordinary restriction to M(l,m,r) therefore requires

    m(l+r-1) <= Y+Z-bd.

For (H) this is 294<=315, so the necessary condition passes. This does not
assert the existence of ordinary maps.

The source is a coordinate restriction of the abelian group tensor
Z/18 times Z/23. Its order is 414, while the target volume is 1680.
The existing abelian opposite-relation lemma therefore excludes coordinate
injections with diagonal weights. This adopts the argument in
[finite_amplitude.md, Section 5](../2026-10-20-koszul/finite_amplitude.md#5-coordinate-maps-with-diagonal-weights-cannot-supply-this-target).
General input mixing remains outside that obstruction.

## 3. Exact coverage and reproduction

The recorded frontier includes 15,327 source quadruples satisfying

    2<=a<=c<=20, ac<=169, a-1<=b<=2a, c-1<=d<=2c,

with b<=d when a=c. It considers all positive middle sizes of M(a,m,c).
For each source it computes the greatest m permitted by all first-leg
Koszul ranks and the smallest m passing one of the three recorded finite
profile costs. There are 121 surviving source quadruples. No target is
constructed. The other full-leg Koszul families and other target outer
dimensions are not claimed as covered by this frontier.

```sh
python research/ai/2026-10-20-unequal-paired/unequal_paired.py --mode controls --output /tmp/unequal-controls.json
python research/ai/2026-10-20-unequal-paired/unequal_paired.py --mode frontier --output /tmp/unequal-frontier.json
python research/ai/2026-10-20-unequal-paired/unequal_paired.py --mode target --output /tmp/unequal-target.json
python research/ai/2026-10-20-unequal-paired/unequal_paired.py --mode upper-controls --output /tmp/unequal-upper-controls.json
python research/ai/2026-10-20-unequal-paired/unequal_paired.py --mode edge-exclusion --output /tmp/unequal-edge-exclusion.json
python -m unittest discover -s tests -p test_unequal_paired.py -v
```

The controls build 437 characteristic-two coefficient maps and 12 signed
maps over F_65521 independently of formula (1). Tests replay the full stated
frontier, check the selected 120 ranks and exact exponent comparison, and
check the equal-source specialization and parameter guard. Finite controls
support implementation validation; the written argument supplies the general
formula. Separate coefficient controls outside the equality hypotheses
validate the universal-bound implementation. No independent mathematical
review or formalization is claimed.
