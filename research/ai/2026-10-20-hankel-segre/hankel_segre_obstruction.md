# A secant-curve obstruction for ordinary cyclic-source restrictions

October 20, 2026. AI-derived written proof with a separate research
agent's check. Not formalized or externally peer reviewed. It excludes
ordinary restrictions and supplies no smaller matrix multiplication
exponent.

## Result

Let `a,b>=2`, `m=a+b-1`, `N=abm`, and let `A(a,b)` be the three-factor
cyclic convolution source in the existing anisotropic package. Suppose an
ordinary linear restriction takes it to a direct sum containing a block
`M(l,h,n)`. Let the full target leg dimensions be `D_X,D_Y,D_Z`, with the
selected block's first leg of dimension `lh`. Put `k_Y=N-D_Y` and
`k_Z=N-D_Z`.

For every integer `r>=1` satisfying

\[
r<\min(a,b),\qquad a+b-2\ge3r-1,
\]

the following implication is necessary:

\[
n+k_Y+k_Z<(r+1)ab\quad\Longrightarrow\quad lh\le rab. \tag{1}
\]

The two cyclic versions hold as well. For a square direct sum with common
total leg dimension `D` and a block of size `n`, this becomes

\[
n^2>rab\quad\Longrightarrow\quad n+2(N-D)\ge(r+1)ab. \tag{2}
\]

This strengthens the earlier rank-one Hankel-locus test. It does not
replace its additional three-leg condition for small nonscalar blocks.

For the selected source `A(5,6)` and target `M16` direct sum `M4`, take
`r=2`. Here `N=300`, `D=272`, `ab=30`, and the larger block gives

\[
16+2(300-272)=72<90=3ab,
\qquad 16^2=256>60=2ab.
\]

Thus the proposed ordinary restriction is impossible. This does not
exclude a singular degeneration to that target. The old conditional
exponent arithmetic remains valid if such a singular degeneration is
constructed.

## 1. An elementary intersection fact for the rational normal curve

Work over an algebraically closed field of characteristic zero. For an
effective finite divisor `Z` on `P1`, let `W_Z` be the vector span of its
degree-`d` rational-normal-curve image, including derivative vectors when
`Z` is nonreduced. Its length counts multiplicities.

For any divisor of length at most `d+1`, its evaluation and derivative
functionals on binary forms of degree `d` are independent. This is the
ordinary Hermite interpolation statement: in an affine coordinate avoiding
the divisor, the Chinese remainder map to the local rings at its points
is surjective on polynomials of degree below its length. A projective
change of variable deals with infinity.

Consequently, whenever `length(Z union W)<=d+1`,

\[
W_Z\cap W_W=W_{Z\cap W}. \tag{3}
\]

Indeed, choose the confluent evaluation basis for the union. Both spans
are coordinate subspaces in that independent basis, and their common
coordinates are exactly the derivative orders in the intersection.

Let `Sigma_r` be the affine cone over the `r`-th secant variety, using
the convention that `Sigma_1` is the curve cone. Every nonzero element
of `Sigma_r` lies in `W_Z` for a divisor of length at most `r`. This
includes tangent and higher osculating limits: effective divisors of
degree `r` form a projective parameter space, and their spans have the
constant vector dimension `r` when `r<=d+1`. The associated projective
incidence bundle has closed image and contains the ordinary secant spans.

If `2r<=d+1`, each such element has a unique minimal supporting divisor.
To see this, compare any two length-at-most-`r` supports using (3), then
remove every unused highest derivative coefficient. The resulting
divisor is contained in both and is the unique minimal choice.

## 2. Lines in the secant variety

**Line lemma.** If `d>=3r-1` and a vector space `L` is contained in
`Sigma_r`, then all of `L` lies in `W_Z` for one divisor `Z` of length
at most `r`.

First take `f,g` in `L`, with minimal supports `Z_f,Z_g`. Let
`U=Z_f union Z_g`. Their leading nonzero derivative coefficients show
that, for all but finitely many scalars `t`, the vector `f+t*g` uses
every highest derivative order in `U`. It is therefore not in the span
of any proper subdivisor of `U`.

On the other hand `f+t*g` belongs to `Sigma_r`, so it has a support
`Z_t` of length at most `r`. The union of `U` and `Z_t` has length at
most `3r<=d+1`. Equation (3) places `f+t*g` in `W_(U intersect Z_t)`.
The preceding minimality forces `U` to be contained in `Z_t`. Hence
`length(U)<=r`, and every pair of points on the line has its supports
in one length-at-most-`r` divisor.

For an arbitrary `L`, choose an element whose minimal support has maximal
length `s`. Such a maximum exists because lengths are integers from zero
to `r`. Apply the pairwise conclusion using `s` in place of `r`: all
elements of `L` are in `Sigma_s`, and `d>=3r-1>=3s-1`. The union of the
maximal support with any other support has length at most `s`, so the
other support is contained in the maximal one. This proves the lemma.

The argument includes nonreduced supports. An honest-Waring-rank-only
line theorem would not suffice here.

## 3. Bilinear families cannot move the supporting divisor

Let `Phi:U tensor V -> K^(d+1)` be linear, where `K` is algebraically
closed of characteristic zero. Suppose every `Phi(u tensor v)` is in
`Sigma_r`, with `d>=3r-1`. Then

\[
\operatorname{rank}\Phi\le r. \tag{4}
\]

Let `s<=r` be the maximum minimal-support length on its decomposable
inputs. If the image is zero there is nothing to prove. Otherwise the
inputs with length exactly `s` form a nonempty Zariski open subset of
`U times V`: this is the complement of the preimage of `Sigma_(s-1)`.

For generic fixed `u`, the linear space `Phi(u tensor V)` contains a
length-`s` element and is contained in `Sigma_s`. The line lemma gives
one support `Z_u` of length `s` for the entire space. For two such
generic vectors `u,u'`, choose `v` for which both images have length
`s`. The linear space `Phi(span(u,u') tensor v)` lies in `Sigma_s`.
The line lemma forces the union of `Z_u` and `Z_u'` to have length at
most `s`. Since both have length `s`, they are equal. Thus one fixed
support contains the images for generic `u` and every `v`. Linearity
then puts the full image in its `s`-dimensional span, proving (4).

The same conclusion holds over any characteristic-zero field after
extending scalars to its algebraic closure; matrix rank is unchanged.

## 4. Apply the lemma to the polynomial Hankel symbol

The existing polynomial-rank-locus note defines the source slice `M_F`
and its symbol

\[
f_k(x,z)=\sum_{i<a,s<b}F_{i,k,s}x^i z^s,\qquad
B_F(x,z)=(f_{p+q}(x,z))_{p<a,q<b}.
\]

Its two polynomial-multiplication injections prove

\[
\operatorname{rank}M_F\ge ab\operatorname{rank}_{\mathbb C(x,z)}B_F.
                                                               \tag{5}
\]

This is adopted from the existing package, not a new result here.
The exact imported source is
[`polynomial_rank_locus.md` at e44aaff22af7863e0a1f5db66d187ae997c82184](https://github.com/1337isnot1337/matrix-mult-bounds/blob/e44aaff22af7863e0a1f5db66d187ae997c82184/research/ai/2026-10-20-anisotropic-constructions/polynomial_rank_locus.md).
The branch need not be merged into `main` for this immutable reference to
identify the premise precisely.

The classical Hankel determinantal description identifies the sequences
whose `a`-by-`b` Hankel matrix has rank at most `r` with `Sigma_r` for
the degree-`a+b-2` rational normal curve, provided `r<min(a,b)`.
This is an external input. One inspected source is Conca,
Mostafazadehfard, Singh and Varbaro, *Hankel determinantal rings have
rational singularities*, Advances in Mathematics 335 (2018),
Introduction and Sections 1-2, especially formula (2.0.1):
https://www.math.utah.edu/~singh/publications/conca_mostafazadehfard_singh_varbaro.pdf
The source describes the generic Hankel minors and their secant-variety
coordinate rings over an arbitrary field. Only the characteristic-zero
geometric consequence is used here.

For an ordinary restriction, the transpose of each leg map embeds the
corresponding concise target dual space into source slices. A rank-one
matrix parameter in the selected `M(l,h,n)` block has target slice rank
`n`. The two other maps can lower ordinary matrix rank by at most their
kernel dimensions. Thus its nonzero source lift satisfies

\[
\operatorname{rank}M_F\le n+k_Y+k_Z. \tag{6}
\]

Under the premise of (1), (5) and (6) give symbol rank at most `r`.
Write this lifted slice as a bilinear function of the two rank-one
matrix vectors. Its rank-`(r+1)` minors vanish as polynomials in the
complex vector parameters, so those polynomial identities also hold for
parameters over the algebraic closure of `C(x,z)`. Section 3, applied
over that field, says that the matrix listing the `lh` long-coordinate
sequences of the full lifted block has rank at most `r` over `C(x,z)`.
Every `(r+1)`-minor of that matrix is therefore the zero polynomial.

Now evaluate its entries at an `a`-by-`b` Cartesian grid of distinct
complex `x` and `z` values. At each node, the evaluated block space has
dimension at most `r`. Evaluation at all `ab` nodes is injective on the
source coefficient arrays, because each polynomial has separate degrees
below `a` and `b`. The lifted block has dimension `lh`, so

\[
lh\le rab.
\]

This proves (1), and (2) follows by substituting the square dimensions.
The proof does not assume that the common divisor over `C(x,z)` is
constant in `x,z`; the interpolation argument is what retains that case.

## Scope and relation to earlier work

The earlier package classifies the full source locus below `2ab` and
uses coherent rank-one Hankel factors. The present argument instead uses
the geometry of the rank-one parameter variety of a matrix block and
higher Hankel secants. The polynomial multiplication inequality and the
source indexing are inherited unchanged.

The target comparison uses actual ordinary maps in (6). Along a
singular degeneration the approximating target slice can have higher
rank before the limit, so (6) cannot be applied with its limiting rank.
No arbitrary-degeneration exclusion is claimed.

The auxiliary `equality_probe.py` was a rejected first guess: it found
426 counterexamples over F2 to an overly narrow rank-`2ab` slice
classification at `a=b=2`. That guess is not a lemma in this proof.
The new argument's degree and middle-catalecticant hypotheses exclude
that format at `r=2`.

The exact companion controls check confluent interpolation and explicit
symbol ranks. Such checks do not prove the universal geometric lemmas.
The mathematical claim rests on the written proof above. A second
research agent checked the support-divisor, line and Segre arguments and
the polynomial evaluation step; external review remains desirable.
