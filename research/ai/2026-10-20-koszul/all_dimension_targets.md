# All-dimension mixed targets and a quantitative construction criterion

October 20, 2026. AI-derived written proofs, unreviewed. **The source
degenerations in Section 4 are not constructed. No smaller exponent is proved.**
This extends the four-dimensional target of the earlier note; the interpolation
construction is standard and no historical priority is claimed.

## 1. The target for every shared dimension

For an integer m>=2, set D=m-1 and N=m(m+1)/2. Define

\[
T_m=\sum_{a+b+c+d=D}X_{a+c}Y_{a,b}Z_{c,d},
\]

where the Y and Z coordinates are indexed by nonnegative exponent pairs of
total degree at most D. The dimensions are (m,N,N). Grouping Y coordinates by
degree u-1 and Z coordinates by degree m-u gives exactly the m matched sectors

\[
C(u,m+1-u),\qquad 1\le u\le m,
\]

sharing their full output coefficient space X, with the canonical common basis.
Write T_{m,k}=T_m tensor B_X(k): its dimensions are (m,kN,kN), and it has k copies
of each sector.

**Border rank.** The border rank of T_{m,k} is exactly kN. Here is an explicit
certificate for T_m, avoiding a numerical interpolation inverse. At the N nodes
(i,j) with i+j<=D, put k'=D-i-j and

\[
\ell_{ij}(s,t)=\binom{s}{i}\binom{t}{j}\binom{D-s-t}{k'}.
\]

These degree-D polynomials are the Lagrange basis on the triangular grid. For
another grid point (r,q), a nonzero value requires r>=i, q>=j, and r+q<=i+j,
which together force (r,q)=(i,j); the value there is one. Their leading-degree
coefficient is

\[
w_{x,ij}=[s^xt^{D-x}]\ell_{ij}
=\frac{(-1)^{k'}}{i!j!k'!}\binom{k'}{x-i}, \tag{1}
\]

with the binomial coefficient zero outside its range. If F and G are arbitrary
polynomials of total degree at most D, then

\[
\sum_{i+j\le D}\epsilon^{-D}
 \left(\sum_{x=0}^D w_{x,ij}X_x\right)
 F(\epsilon i,\epsilon j)G(\epsilon i,\epsilon j) \tag{2}
\]

has no negative powers, constant term T_m, and remaining degree at most D.
Indeed, interpolation reproduces each monomial of degree <=D: all lower-degree
coefficients cancel, and degree D supplies exactly its coefficient vector.
Higher degrees carry a positive power of epsilon. This is a border-rank-N
certificate from a diagonal source, not from a convolution source.

The Y flattening has disjoint nonempty row supports: an (X_x,Z_{c,d}) position
determines a=x-c and b=D-a-c-d uniquely. Thus its rank is N. Concatenating k
copies of (2) and applying the same flattening argument proves border rank kN;
no general additivity of border rank is assumed.

## 2. Every full-space Koszul family survives

Compare T_{m,k} with C(m,B), where B=kN. For the m-dimensional shared leg,
the output-convolution formula in the earlier note gives

\[
\begin{aligned}
\operatorname{rank}K_p(T_{m,k})
&=k\sum_{u=1}^m\min\{u\binom mp,(m+1-u)\binom m{p+1}\}\\
&=B\binom{m-1}p. \tag{3}
\end{aligned}
\]

The minimum changes branch at u=m-p. Summing the two arithmetic progressions
proves the second line. The source rank is

\[
\operatorname{rank}K_p(C(m,B))
=B\binom{m-1}p+(m-p)\binom{m-1}{p-1}, \tag{4}
\]

so it is at least (3) for every 0<=p<m. Independent invertible X identifications
of the individual sectors preserve (3). The rest of this section uses the
canonical target, for which Section 1 supplies the border-rank bound.

For the B-dimensional source input, its Koszul rank is the full column rank
m binom(B,p) when p<=B-m. No target in the same padded format can exceed this.
For p>=B-m the source rank is (m+p) binom(B-1,p), at least
B binom(B-1,p). The latter is an upper bound for the target by its border rank B.
For the (B+m-1)-dimensional source output, the source has maximal Koszul rank
in every degree by the output formula, again at least the padded target rank.
These arguments cover all three full-space families. They do not cover every
projected or Young flattening and do not prove degeneration existence.

## 3. A general coordinate-weight obstruction

Consider only source-coordinate selection, nonzero rescaling, permutations,
and diagonal integer weights; no linear combinations or coordinate collisions
are allowed. If this ansatz realizes T_{m,k} from C(m,B), then

\[
\boxed{B\ge kN+k\left\lfloor\frac{(m-1)^2}{4}\right\rfloor
                   -\left\lfloor\frac{m-1}{2}\right\rfloor.} \tag{5}
\]

Here coordinates are consecutive integer exponents in the source support
0<=z-y<=m-1. A sector with nonshared sizes u,v=m+1-u contains the complete
u-by-v rectangle. Its two coordinate widths have sum at most m-1 and at least
(u-1)+(v-1)=m-1. Both sets therefore are intervals. If its Y interval starts
at b, its Z interval is [b+u-1,b+m-1].

For m>=3 the present C(2,m-1) sector forces the weights of X_0,...,X_{m-1}
to be affine in the index: subtract the zero-weight equations in its two rows.
For m=2 any two X weights already are affine. Absorb that affine function into
the Y and Z weights using x=z-y. Within a sector all Y weights now equal a
constant c_i, and all Z weights equal -c_i. A cross edge from sector i to j
has weight c_i-c_j. Cross edges in both directions cannot both vanish in the
limit, since that would require both differences to be strictly positive.

Order the mk disjoint Y intervals. Suppose two consecutive intervals have
lengths u,u' and g unused coordinates between them. Cross edges in both
directions occur precisely when g<=m-1-max(u,u'). Thus

\[
g\ge m-\max(u,u')=\min(m-u,m-u'). \tag{6}
\]

The multiset of values w=m-u consists of k copies of each of 0,...,m-1. Each
edge in this ordered path contributes the smaller endpoint weight. Assign
each edge to such an endpoint. A vertex receives at most two edges, so the
sum of the mk-1 edge costs is at least the sum of the mk-1 smallest entries
of the doubled multiset of vertex weights. This lower bound is

\[
k\lfloor(m-1)^2/4\rfloor-\lfloor(m-1)/2\rfloor.
\]

Summing (6) and adding the kN occupied Y coordinates proves (5). We do not
claim that this necessary bound suffices for a degeneration. For m=4 it
recovers B>=12k-1. Uniformly over k>=1, the ratio of the bound in (5) to kN
tends to 3/2 as m tends to infinity.

## 4. A construction criterion with an explicit exponent consequence

**Unproved construction premise H(rho).** There are unbounded integers m,
positive integers k_m and source lengths B_m such that

\[
C(m,B_m)\unrhd T_{m,k_m},\qquad
\limsup_{m\to\infty}\frac{B_m}{k_m m(m+1)/2}\le\rho. \tag{7}
\]

The limit is along the constructed sequence. It may use arbitrary linear
changes of basis and polynomial degenerations. No such sequence is supplied.

For

\[
1\le\rho<\rho_c:=\frac9{7\sqrt[3]2}=1.0204721048\ldots,
\]

let d_rho>4/3 be the unique positive solution of

\[
Q(d_\rho)=\rho,\qquad
Q(d)=\frac{8}{d(d+1)2^d}. \tag{8}
\]

**Conditional theorem.** H(rho) implies omega<=3/d_rho<9/4. In particular,
H(1) implies omega<=2.231837587...; an exact, slightly weaker consequence is
omega<=125/56=2.232142857... . These are conditional conclusions only.

The improved limiting-slope estimate is attributed to the concurrent agent's
[cf79709](https://github.com/1337isnot1337/matrix-mult-bounds/commit/cf79709).
It strengthens our earlier tangent-based estimate at `292ba18`. The argument
below also verifies it for the single joint sequence (7), without requiring a
separate k-to-infinity construction at every fixed m. This reconciliation is
not another independent discovery of the common critical cost threshold.

**Proof.** Use the actual symmetrized profile P and rescaled profile F from
[the analytic bridge](scaling_rigidity.md), and put d=1/t. The external baseline
gives d>=4/3. It suffices to consider t>2/3, hence d<3/2: the other characters
already give a square exponent at most two. Each oriented dot parameter is
then positive, since the other two are at most one.

The shared-leg power-sum inequalities imply

\[
P(m,B_m)\ge k_m\sum_{u=1}^m P(u,m+1-u). \tag{9}
\]

For completeness, for each orientation pi use the powered sum with shared-leg
parameter p_pi. Apply generalized Holder with weights p_pi/(6t), which sum to
one, to obtain the symmetrized sum (9). Thus no additivity of P on a shared-leg
sum is assumed.

Replication and the rescaling limit give P(a,b)<=F(a,b) for every integer pair.
Put f(s)=F(1,s), c=f(1)>0, and L=lim_{s->infinity} f(s)/s. Concavity makes L
finite. Iterated tripling at 1, followed by concavity between the resulting
points, gives f(s)>=(2c/3)(s+1/2) for s>=1, so L>0. Every secant slope is at
least L. Symmetry and one-sided concavity give

\[
L\le f'_+(1)\le dc/2,\qquad
f(s)\ge c+L(s-1)\ge L(s+2/d-1). \tag{10}
\]

By symmetry and homogeneity this becomes

\[
F(x,y)\ge L\min(x,y)^{d-1}
                         (\max(x,y)+(2/d-1)\min(x,y)). \tag{11}
\]

The rescaling limit and Fatou's lemma, applied to the nonnegative step function
with value m^{-d}P(u,m+1-u) on ((u-1)/m,u/m], show

\[
\liminf\frac{\sum_{u=1}^m P(u,m+1-u)}{m^{d+1}}
\ge\int_0^1 F(x,1-x)\,dx
\ge L J(d),
\]

where the pointwise limit on 0<x<1 follows by monotonicity and the continuous
rescaling limit, and

\[
J(d)=2\int_0^{1/2}x^{d-1}(1+(2/d-2)x)\,dx
=\frac{2^{2-d}}{d(d+1)}.
\]

The Y flattening gives B_m>=k_m N, so B_m/m tends to infinity even when k_m
stays bounded. By homogeneity and the definition of L,

\[
\frac{P(m,B_m)}{k_m m^{d+1}}
\le\frac{B_m}{k_m m^2}\frac{f(B_m/m)}{B_m/m},
\qquad\limsup\frac{P(m,B_m)}{k_m m^{d+1}}\le\frac{\rho L}{2}.
\]

Divide (9) by k_m m^{d+1} and combine these bounds to get rho L/2>=L J(d),
or rho>=Q(d). The function Q is strictly decreasing:

\[
(\log Q)'=-\log2-\frac1d-\frac1{d+1}<0.
\]

Also Q(4/3)=rho_c and Q(3/2)=8 sqrt(2)/15<1, so 4/3<d_rho<3/2 for the stated
rho range. Every relevant character has d>=d_rho. The external detecting-
character/spectral argument therefore gives omega<=3/d_rho, in the same exact
complex division-free arithmetic model and with the usual arbitrary epsilon
in the running-time exponent.

For the rational consequence at rho=1, the verifier proves Q(a/b)>1 with
a=168, b=125 by the integer comparison

\[
2^{3b}(b^2)^b>2^a\bigl(a(a+b)\bigr)^b.
\]

Thus d_1>168/125, yielding the displayed rational exponent. The decimal
root is descriptive, not the acceptance certificate. This proves the
conditional implication, not its premise. In fact, (5) excludes H(rho) for
rho<3/2 within the specified coordinate-weight ansatz.

## 5. Evidence and remaining construction problem

`all_dimension_targets.py` checks the explicit interpolation coefficients,
Koszul sums, the exact rational exponent implication, and the coordinate
gap formula. The general statements rely on the proofs above, not finite
replay. See the corresponding tests and result manifest for exact coverage.

The concrete open task is to construct (7) with less than 2.04721048 percent
asymptotic overhead, or find an invariant excluding it under general changes
of basis. A construction only at fixed m, including m=4, does not satisfy (7).

External dependencies are the same pinned OpenAI character/counting results
and Uznański v2 rescaling theorem cited in `scaling_rigidity.md`. The local
Koszul formulas and four-dimensional precursor are in `research_note.md`.
