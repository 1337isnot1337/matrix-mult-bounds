# A rank frontier for two regular maps of the cyclic source

October 23, 2026. Owner-directed OpenAI Codex work. Written and
unreviewed over C; no formalization or smaller exponent is claimed.

## 1. Adopted source and saturation results

Let A_a be the cyclic product of three C(a,a), a>=2, and put
N=a^2(2a-1), m=a^2. Every leg has dimension N and the source is invariant
under leg permutations. Its slice map is

    M(F)_((j,p,L),(H,q,r)) = F_(H-j,p+q,L-r),

with coefficients outside 0<=i,s<a, 0<=k<2a-1 set to zero.
The following are prior repository results, not new claims here:

* Every nonzero slice has matrix rank at least m. The minimum-rank
  locus is F=u tensor h tensor v with scalar Hankel rank(h)=1.
* Every nonzero slice of matrix rank below 2m has the form g tensor h,
  where g is an a-by-a coefficient array and h has scalar Hankel rank
  one. Every linear space consisting of such slices has one fixed h.
  Consequently its vector dimension is at most m.
* For two regular leg maps of constant ranks b,c, let rho be the rank
  of the projected source flattening at zero. If the third map is any
  Laurent map and the limit is M(l,beta,n), with its l*n-dimensional
  leg on that third side, then

      rho <= N-l*n+floor(b/beta)*floor(c/beta).          (1)

The first two facts are proved in the pinned cyclic finite-target note
and polynomial-rank-locus note. Equation (1) is the pinned saturated
row-lattice argument. In particular it applies to arbitrary higher jets,
and includes every final output substitution in the regular maps.
Its proof uses elementary formal-series linear algebra and target joint
row/column supports. No external slice-rank theorem is needed here.

## 2. Compression kernel bounds

Let P and Q be the constant maps on the two regular legs, of ranks b,c.
Write the projected slice map as F -> P M(F) Q, choosing the transpose
convention on Q as necessary. Let W be its kernel and put

    delta=(N-b)+(N-c)=2N-b-c.

For F in W, two-sided matrix compression loses at most delta ranks, so

    rank M(F) <= delta.                                 (2)

Thus delta<m implies W=0 and rho=N. If delta<2m, the adopted low-rank
classification puts W inside the m-dimensional space with one fixed
coherent h. This includes W=0; otherwise apply the linear-space part of
that classification. In either case

    delta<2m  ==>  dim W<=m,  rho>=N-m.                 (3)

These are basis-independent statements for arbitrary complex P,Q.
They do not assume coordinate projections or any regular unit lift.
The strict threshold in (3) matters: at rank 2m a slice with separable g
and a scalar Hankel factor of rank two is outside the adopted locus.
We do not claim the resulting rank frontier is optimal.

There is a sharper statement at delta=m when b,c<N: the kernel has
dimension at most one. Indeed all its nonzero slices have rank exactly
m. A line in the minimum-rank cone can vary only u or only v, with the
other factors fixed; the coherent middle curve has no projective line.
For every such slice, equality in (2) forces

    ker P subset im M(F),    ker M(F) subset im Q.      (3a)

To check this, the image of M(F) on im Q has rank at least m-(N-c)=N-b
and lies in ker P of that exact dimension. Hence it equals ker P and
the kernel of M(F) lies in im Q by dimension count. In particular both
ker P and (im Q)^perp are nonzero common subspaces, respectively of
the column and row spaces of all these slices.

For F=u tensor h tensor v, the row space is, up to fixed permutations,
(u*S_(a-1)) tensor span(h_right) tensor C^a, and the column space is
C^a tensor span(h_left) tensor (v*S_(a-1)). Here S_d is the degree-d
binary-form space. Along a nonconstant pencil of u, the intersection
of u*S_(a-1) is zero: a nonzero degree-(2a-2) binary form has only
finitely many divisors of degree a-1 up to scalar, whereas that pencil
has infinitely many distinct members. This contradicts the common
nonzero row subspace in (3a). A varying v similarly contradicts the
common nonzero column subspace. Therefore a two-dimensional W is
impossible. The one-hidden-slice coordinate controls attain this bound.

For clarity, if W=0 then the regular projected source flattening has a
unit maximal minor and a right inverse over C[[t]]. Regularity of the
final tensor therefore forces the remaining Laurent map to be regular.
All three constant maps then give an ordinary restriction. This is the
prior saturation argument, not an assumption of bounded pole order.

## 3. The two-long-leg A4 obstruction

Take a=4, so N=112 and m=16. The target is M(10,10,11), with leg
dimensions 100,110,110. Suppose the two maps to the 110-dimensional legs
are regular, with limiting ranks b,c. The remaining map may be Laurent.
Assume, toward a contradiction, b+c>=193. Then delta<=31<32, and (3)
gives rho>=96. In (1), beta=11 and l*n=100, so

    96 <= rho <= 12+floor(b/11)*floor(c/11).

The two integer floors are at most 10, and their product must be at
least 84. If neither is 10 the product is at most 81. Thus one rank is
110 and the other is at least 99. It follows that b+c>=209 and
delta<=15<16. The projected source flattening is injective by (2), so
the third map is regular. The prior ordinary A4 obstruction excludes
the target: every nonzero source slice retains rank at least 12 under
the two full-rank 110-dimensional target maps, while the target has
rank-11 slices.

Therefore every such degeneration must satisfy

    b+c<=192.                                          (4)

Equivalently its two regular long maps must lose at least 28 ranks in
total relative to their target dimensions. This covers every finite
Laurent pole order and every higher regular jet. It is a necessary
condition, not an existence result for pairs satisfying (4).

## 4. A mixed short/long frontier

Now suppose the maps to target legs 100 and 110 are regular, of ranks
p<=100 and q<=110. The remaining 110-dimensional map may be Laurent.
For p+q>=193, equations (1) and (3), now with beta=10 and l*n=110, give

    96 <= rho <= 2+floor(p/10)*floor(q/10).

Hence the floor product is at least 94. Either p=100 and q>=100, or
90<=p<=99 and q=110. If p+q>=209, (2) forces the remaining map regular,
and the ordinary target is excluded. At p+q=208, delta=16 and both
constant-map defects are positive, so the sharper kernel bound in
Section 2 gives dim W<=1. Consequently rho>=111,
whereas (1) is at most 102 in the two possible rank pairs (100,108)
and (98,110). These pairs are excluded as well.

The remaining rank pairs with p+q>=193 are exactly

    (100,q), 100<=q<=107;   (p,110), 90<=p<=97.         (5)

The finite screen records these sixteen survivors. They pass only
these necessary tests; no maps or jets for them have been constructed.
Pairs of total rank at most192 are not closed by this argument.

## 5. Scope, evidence and attribution

The new deductions are the compression-kernel bound (3), its sharp
one-dimensional equality refinement, the all-order
rank budget (4), and the explicitly limited mixed frontier (5). The
source formulas, minimum-rank classification, below-twice-minimum locus,
saturation support inequality and ordinary target exclusion retain the
prior packages' credit. Exact paths and SHA-256 pins are in sources.json.
No new external theorem or historical priority is claimed.

The verifier independently enumerates the original six source indices
for coordinate compression controls. It checks an attained m-dimensional
hidden coherent subspace, a one-dimensional hidden source slice, and
rank-2m endpoint controls. It exhausts the 12321 long/long and 11211
short/long integer rank pairs, using only certified bounds. The symbolic
proof establishes the arbitrary-complex-map and all-order quantifiers;
the finite controls do not formalize those statements or review them
independently. Lower-rank regular pairs, two polar maps, and the full
matrix construction remain open. The exponent remains9/4.
