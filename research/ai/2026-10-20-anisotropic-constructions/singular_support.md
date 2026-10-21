# Explicit support degenerations and a direct-sum target

October 21, 2026. These are exact intermediate tensor constructions and
conditional target calculations. No degeneration to an exponent-improving
matrix target has been constructed. The proposed parity110 target is now
excluded, even as a singular degeneration, by the stronger
[pairwise-annihilator proof](parity_annihilator.md). The number 2.243 below
is preserved as historical conditional arithmetic, not an established
matrix multiplication exponent.

## Source and exact degeneration

Use the cyclic convolution tensor A(a,b) from the package README. Write
m=a+b-1. Its nonzero coefficients are all one, at

\[
 X=(i,p+q,s),\qquad Y=(j,p,r+s),\qquad Z=(i+j,q,r),
\]

where i,p,r range from zero to a-1 and j,q,s range from zero to b-1.
The three coordinate weights are

\[
 w_X=p+q-i-s,\quad w_Y=r+s-j-p,\quad w_Z=i+j-q-r.
\]

Their sum is zero on every source term. For integer weights, including
negative weights, floor division and parity always have their ordinary
mathematical meanings. The implementation uses Python's `//` and `%`.

Three explicit diagonal one-parameter degenerations were examined.

| Name | Coordinate exponents on X,Y,Z | Minimum total exponent |
| --- | --- | --- |
| step | 1(w_X<0), 1(w_Y<0), 1(w_Z<1) | 1 |
| parity000 | floor(w_X/2), floor(w_Y/2), floor(w_Z/2) | -1 |
| parity110 | floor((w_X+1)/2), floor((w_Y+1)/2), floor(w_Z/2) | 0 |

Multiply each coordinate by epsilon to its stated exponent, divide the
whole tensor by epsilon to the minimum total exponent, and let epsilon
tend to zero. This retains exactly the terms at that minimum, with
coefficient one. Laurent exponents are permitted: the maps are invertible
for nonzero epsilon and the normalized tensor has a finite limit.

For parity000, the possible ordinary parity patterns are 000, 011, 101
and 110, and exactly 000 is discarded. For parity110, exactly 110 is
discarded. Equivalently, use shifted parities

\[
 r_X=(w_X+1)\bmod2,\quad r_Y=(w_Y+1)\bmod2,\quad
 r_Z=w_Z\bmod2.
\]

The parity110 support has r_X+r_Y+r_Z=2. The discarded terms have sum zero.
Every original source coordinate occurs in each of these three retained
supports in the four formats checked below.

| a,b | Source leg dimension | step terms | parity000 terms | parity110 terms |
| --- | ---: | ---: | ---: | ---: |
| 2,2 | 12 | 44 | 48 | 48 |
| 4,4 | 112 | 2400 | 3072 | 3072 |
| 4,5 | 160 | 4600 | 6000 | 6000 |
| 5,5 | 225 | 8875 | 11700 | 11725 |

The formula, valuation levels, coefficient counts and active coordinates
are checked exhaustively by `singular_support.py`. A nonzero coordinate
slice has one nonzero entry in each of its used rows and columns, so its
rank is its number of incident terms. The smallest coordinate slice rank
of the parity110 A(5,5) tensor is twelve on every leg. This explains why
the ordinary full-source rank gap does not carry over to this singular
limit.

## A score bound with an elementary slice-rank proof

Let S have a specified support. Give its coordinates positive real scores
s_X,s_Y,s_Z whose product on every support term is the same constant K.
Set Z_X=sum(s_X), and similarly for the other two legs. Then any
degeneration

\[
 S\unrhd M(l,h,n)
\]

must satisfy

\[
 (lhn)^2\le \frac{Z_XZ_YZ_Z}{K}.                     \tag{1}
\]

If the target is a direct sum of square matrix tensors with sizes n_j,
write D=sum_j n_j^2. The corresponding necessary condition is

\[
 D^3\le \frac{Z_XZ_YZ_Z}{K}.                         \tag{2}
\]

Here is a direct proof. Form the cyclic product
H=S tensor S^cyc tensor S^(cyc squared). Each combined leg has total score
Z_X Z_Y Z_Z, and the product of the three leg scores of each H support
term is K^3. In H to the tensor power q, at least one coordinate of any
support term has score at least K^q. The coordinates of this kind cover
the support. On each leg their number is at most

\[
 \left(\frac{Z_X Z_Y Z_Z}{K}\right)^q,
\]

because the sum of all leg scores is (Z_X Z_Y Z_Z)^q. Consequently
the slice rank of H^q is at most three times that expression.

The slice rank of a square matrix multiplication tensor M(v,v,v) is v^2.
One way to check the lower bound is the antichain-support formula in
Tao and Sawin's Proposition 4: assign generic injective vertex-difference
weights to each leg, giving constant total weight zero on the support.
There are v^3 support terms and each coordinate meets exactly v of them,
so any support cover has at least v^2 coordinates. The converse follows
by taking every coordinate in a single leg. Disjoint blocks have disjoint
supports and covers, so their slice ranks add; their tensor powers are
again direct sums of square matrix tensors. Slice rank does not increase
under restrictions or degeneration, by Corollary 2 in the same source.

The cyclic product of M(l,h,n) and its two rotations is M(lhn,lhn,lhn).
Its q-th power has slice rank (lhn)^(2q). Take q-th roots of the preceding
upper bound and let q tend to infinity to obtain (1). For a direct sum
of square sizes n_j, the cyclic product has a direct sum of square blocks
of sizes n_i n_j n_k. The sum of their squared sizes is D^3, and the
same argument gives (2).

This argument was checked by a second agent in this generating session,
the parity-balancing worker; no external independent review is claimed.
It does not assume that every entropy or quantum-functional
upper bound is attained. The separate balancing note states precisely
what its positive support distributions prove.

## Exact score certificates and the selected source

For the step support use coordinate scores z^v t^w, with v the step
valuation and w the original weight. Their product is z. The source
character counts, and hence all three partition sums, are obtained by
enumerating k-i-s with 0<=i<a, 0<=k<a+b-1 and 0<=s<b. The following
rational choices give strict instances of (1):

| Source | z | t | Excluded target |
| --- | --- | --- | --- |
| step A(4,4) | 1/7 | 3/4 | M(10,10,11) |
| step A(4,5) | 1/7 | 3/4 | M(12,12,13) |
| step A(5,5) | 1/7 | 25/32 | M(14,14,14) |

`singular-support-controls.json` stores every partition sum as an exact
rational and the integer cross-multiplication proving each inequality.
The step source therefore cannot supply the selected large matrix target.

The parity sources permit higher capacity. Give a coordinate of shifted
parity r the score z^r. The support score product is z^2. For parity000
A(5,5), each leg has 113 even and 112 odd coordinates. Taking z=113/56
gives the exact bound

\[
 \frac{(113+112z)^3}{z^2}=9\,567\,936.
\]

For parity110 the three pairs (even,odd) are (112,113), (112,113),
(113,112). Taking z=2 gives

\[
 \frac{338^2\,337}{4}=9\,625\,057.                   \tag{3}
\]

The former proposed target was

\[
 \boxed{\text{parity110 }A(5,5)\ \unrhd\ M(14,14,14)\oplus M(4,4,4).}
                                                               \tag{4}
\]

It uses 14^2+4^2=212 coordinates on each leg, so its left side in (2)
is 212^3=9,528,128. Both parity sources pass this one necessary condition.
The parity110 source has the larger score bound and was selected for an
initial construction search. The subsequent annihilator proof shows that
any degeneration of this source to a direct sum of square matrix tensors
has leg dimension at most 169. It therefore excludes (4) and even M14
alone. Passing the score bound did not establish existence. The numerical
searches on the excluded target have been stopped. Full A(5,5) has an
exact mixed M9 seed, but the subsequent
[complete low-rank-locus argument](polynomial_rank_locus.md) also excludes
its ordinary M14 plus M3 target. That full-source singular target remains
open; no corresponding singular construction has been found.

The exact minimum of the parity110 score expression is at the positive
root of 113 z^2-112 z-226=0, approximately 1.9941061017702753. Its cube-root
capacity is approximately 212.716257. The separate
`parity_balancing.py` package supplies exactly verified support
distributions and a numerical diagonal preconditioner. This preconditioner
is a change of source coordinates; it does not alter the target question.

## Conditional exponent and integer certificate

More generally, if A(a,b) degenerates to a direct sum of square matrix
tensors with sizes n_j, the character rules and both source orientations
in the package README imply

\[
 \sum_j(6n_j)^{3t}\le [3(a+b)-2]^3.                  \tag{5}
\]

Indeed, each of the two oriented source character values is at least
sum_j n_j^(3t). Their product is P(a,b)^(6t), hence P(a,b)^(3t) is at
least that sum. Combine this with 6P(a,b)<=base^(1/t). The same detecting
character argument used in the README converts a strict violation of
(5), with 3t replaced by c, into the conditional bound omega<c.

For (4), the exact integer comparisons are

\[
 84^{2243}>20708^{1000},\qquad
 24^{2243}>1246^{1000},\qquad
 20708+1246=21954>28^3=21952.
\]

Thus construction (4) would give omega<2243/1000=2.243. It is now known
to be impossible from this parity source. The equation
84^c+24^c=28^3 has its root near 2.2429601304. No map realizing (4) has
been found from the full source either. Two smaller conditional direct-sum targets are recorded in
the same exact verifier: A(4,5) to M12 plus M3 gives 2.248, and A(4,4)
to M10 plus M3 gives 2.2492. They are also unconstructed.

## Positive controls and discovery records

For every 1<=a<=b there is an exact coordinate restriction from the
parity110 source to M(a,a,b). Index its target entries by i,j<a and k<b,
and retain source coordinates

\[
 X(i,j)=(i,i+j,j),\qquad
 Y(j,k)=(k,j,j),\qquad
 Z(k,i)=(i+k,i,0).
\]

The three source incidence equations force agreement of the repeated
indices, with no extra target terms. The X weight is zero, so the
ordinary parity pattern is either 000 or 011; both are retained in
parity110. The maps are injective. The verifier checks complete target
coefficient equality for (a,b)=(2,2),(2,3),(5,5), including all 15,625
coefficients of the A(5,5) to M5 control. These small restrictions are
validation controls and do not improve the exponent.

`dense_als.py` accepts the explicit source faces, arbitrary matrix shapes,
direct sums of square blocks, and invertible diagonal source scaling.
It recomputes the residual on every target coefficient. Numerical maps
for a scaled source must be composed with the stored diagonal factors
to obtain maps for the unscaled support tensor. Numerical residuals,
including very small ones, are never accepted as exact certificates.

The `outage_als_engines.js` file and its reports preserve exploratory
calculations made while local Python execution was unavailable. These
include unsuccessful small A(2,2) searches and five large parity000
A(5,5) sweeps toward M14 plus M4. The large five-sweep residual was
0.9513816375603587. The arrays are preserved for continuation; this
experiment supplies neither an exact witness nor an exclusion.

## Sources

- Terence Tao and Will Sawin, [Notes on the slice rank of tensors](https://terrytao.wordpress.com/2016/08/24/notes-on-the-slice-rank-of-tensors/),
  August 24, 2016. Proposition 4 gives the antichain-support formula;
  Corollary 2 gives the closedness used for degeneration monotonicity.
- The [package README](README.md), its cited OpenAI paper and the local
  two-sector proof provide the character comparison used in (5).

All tensor-target implications in this note remain conditional on their
explicitly stated missing maps. The exact support tensors, integer
comparisons, positive controls and finite scores are reproducible from
the accompanying scripts.
