# A quadratic injectivity range on the paired source's long legs

October 23, 2026. Written, unreviewed proof. No independent review,
formalization, construction, or improved exponent is claimed.

## Statement and source convention

Let a>=2, D=a-1, h=2a-1 and N=ah. Use the maintained paired source

    P_a = sum A_(u,q) B_(y,q+v) C_(u+y,v),
          0<=u,q,y,v<a.

Its format is (a^2,N,N). Let

    K_p^B: wedge^p B tensor A* -> wedge^(p+1) B tensor C

be exterior multiplication by its B coordinate, with the other two
coordinates as input and output. Over **every field**, for

    0 <= p <= a(a-1),

this map is injective. Consequently its rank is

    a^2 binom(N,p).                                      (1)

The map is also surjective for N-a<=p<=N, with rank

    N binom(N,p+1).                                      (1b)

The same holds on the C leg, with the short A leg as the input.
This is not an all-power rank formula. For a=2, the first degree beyond
this interval already has a kernel: K_3^B has rank 70, with domain
dimension 80. The supplied integer kernel and modular minor certify
that finite characteristic-zero rank. No general sharpness assertion
about the endpoint in (1) is made.

The source coefficients and short-leg rank formula are adopted from the
maintained paired-source package, pinned in sources.json. The following
long-leg argument does not assume its short-leg cohomological formula.

## 1. A symmetric Hankel tensor

Let H_a have coordinates

    H_a = sum d_(q+v) e_q f_v,      0<=q,v<a,

with first-leg dimension h and two other legs of dimension a. Write
J_k for its first-leg exterior map, with input e*. Then

    rank J_k = a min{binom(h,k),binom(h,k+1)}.           (2)

Here and below an out-of-range exterior power is zero.

It suffices to prove injectivity for k<a. Extend the field if needed
to obtain h distinct scalars alpha_i; ranks are unchanged by extension.
Put u_i=(1,alpha_i,...,alpha_i^D). Inverse Vandermonde interpolation
gives a first-leg basis d'_i in which

    H_a = sum_i d'_i tensor u_i tensor u_i.

Any at most a of the u_i are independent. For a proposed kernel vector
write x_S in e* for each k-element subset S of this first-leg basis.
At an exterior output T of size k+1 the equation is

    sum_(i in T) +/- u_i(x_(T-i)) u_i = 0.

Since k+1<=a, every coefficient vanishes. For each fixed S this gives
u_i(x_S)=0 for every i outside S. There are h-k>=a such indices, so
x_S=0. This proves injectivity. The symmetry between e and f and
transpose duality identify the rank at k with the rank at h-k-1.
This gives surjectivity for k>=a-1 and proves (2), in every
characteristic. In particular,

    ker J_k = 0 for k<a.                               (3)

## 2. Evaluate the first short coordinate on a projective line

Let E have basis e_y, 0<=y<a, and let W have basis d_j, 0<=j<h,
so B=E tensor W. On the projective line with coordinates [s:t] put

    b_j(s,t) = sum_(y=0)^D s^(D-y) t^y B_(y,j).

These vectors define the rank-h subbundle

    S = O(-D) tensor W  inside  B tensor O.

Its quotient Q is explicitly

    Q = O(1)^(Dh).                                     (4)

Indeed the quotient E tensor O -> O(1)^D has adjacent rows
t e_y - s e_(y+1). Its kernel is the monomial column
(s^D,s^(D-1)t,...,t^D). Removing its first column gives determinant
(-s)^D, and removing its last gives t^D. Thus it is surjective on
the two standard charts, over any field. Tensor with W to get (4).

A vector x in the domain of K_p^B, with coefficients
x_(S;u,q), determines the section

    X(s,t) = sum_(S,u,q) s^(D-u)t^u x_(S;u,q)
                         B_S tensor e_q*

of wedge^p B tensor e* tensor O(D). This association is injective,
because the a degree-D monomials are independent.

Evaluate the C coordinate of K_p^B(x) by sending C_(z,v) to
s^(2D-z)t^z f_v. The result is

    sum_(q,v) b_(q+v)(s,t) wedge X_q(s,t) tensor f_v.   (5)

The identity follows directly from z=u+y. Both factors on the right
have degree D, so it is an identity of homogeneous degree-2D
polynomials, including both projective charts. If K_p^B(x)=0, (5)
vanishes identically.

## 3. The kernel bundle has a negative-degree filtration

At a point of the line, split B locally as S direct_sum Q. Exterior
degree in S gives

    wedge^p B = direct_sum_k wedge^k S tensor wedge^(p-k) Q.

The operator in (5) raises this S degree by one. On the kth summand
it is J_k, with the harmless local line-bundle factors included.
Thus its kernel is a vector bundle R_p, with a filtration whose
successive quotients are

    ker J_k tensor O(-Dk) tensor wedge^(p-k) Q.         (6)

One can obtain the filtration without choosing a global splitting:
filter wedge^p B by the number of S factors. On either standard chart
a splitting gives the displayed kernels; transitions preserve this
filtration. The dimensions of J_k are constant, so these are vector
bundles, rather than an inference about a generic fiber.

Only k>=a contributes, by (3). After the twist O(D) appropriate to X,
(4) makes every nonzero quotient in (6) a direct sum of copies of

    O(D-Dk+p-k) = O(p+D-ak).                           (7)

If p<=a(a-1), the largest possible degree, at k=a, is at most -1.
Every quotient therefore has no global sections. Induction through
the filtration gives H^0(R_p(D))=0. This step uses only left exactness
of global sections; it does not assume the filtration splits or that
its higher cohomology vanishes. The elementary fact H^0(P^1,O(d))=0
for d<0 follows by comparing polynomials on the two standard charts;
it is also the n=1,q=0 case of the cited Stacks lemma.

By (5), a kernel vector x would give a section X of R_p(D). Hence
X=0, and injectivity of x -> X gives x=0. This proves (1).

## 4. The upper exterior degrees are surjective

The fiber cokernel of (5) has a parallel filtration. At output S-degree
k+1 its graded piece uses coker J_k and wedge^(p-k)Q. Include k=-1
for the output part of S-degree zero. By (2), these cokernels are zero
for k>=a-1. The remaining k<=a-2 require p-k<=Dh. If p>=N-a, however,

    p-k >= N-a-(a-2) = Dh+1.

Every such exterior power of Q is zero. Therefore the evaluated bundle
map is surjective in every fiber, and there is an exact sequence

    0 -> R_p(D) -> wedge^p B tensor e* tensor O(D)
      -> wedge^(p+1) B tensor f tensor O(2D) -> 0.

Every nonzero quotient of R_p(D) in (7) has k<=h, so its degree is at
least p+D-ah=p-(N-a+1), which is at least -1 in this interval.
The projective-line identity H^1(O(d))=0 for d>=-1 then gives
H^1(R_p(D))=0 by induction through the filtration. The long exact
sequence of global sections proves (1b). The global section map is
exactly K_p^B, by (5) and the independence of the degree-2D monomials.
No global splitting of the kernel bundle is assumed here either.

## 5. An all-degree lower bound on source rank

The same filtration bounds the dimension of global sections in every
degree. Define

    U(a,p) = sum_(k=a)^h a*(binom(h,k)-binom(h,k+1))
                    *binom(Dh,p-k)*max(p+D-ak+1,0).

The kernel of K_p^B is H^0(R_p(D)), not just a subspace of it: both
directions follow from the homogeneous coefficient identity (5).
Left exactness through the filtration gives

    dim ker K_p^B <= U(a,p),
    rank K_p^B >= max(0,a^2*binom(N,p)-U(a,p)).          (8)

This is a source **lower** bound. It can certify that a proposed target
rank is no larger than the source, but cannot exclude a degeneration.
Counting the associated graded sections as an equality would be wrong:
extension maps can prevent sections from lifting. At a2,p3, U=12
while the exact kernel dimension is10. The integer countercontrol
therefore also tests this distinction.

## 6. The other long leg and the screening consequence

Exchange B and C, replace A_(u,q) by A_(q,u), and reorder the long
coordinates B_(y,j) <-> C_(j,y). The source formula is preserved
(rename the remaining short indices y and v). This proves the C-leg
assertions with the same intervals and bound.

Any dimension-compatible padded target has its short input dimension
at most a^2. Its long-leg exterior rank is at most
a^2 binom(N,p), the source's full column rank in (1). Therefore neither
long-leg test in this interval can exclude **any** such target.
In particular, the 28 maintained short-leg survivors through a=16
require long-leg degrees at least 183, 211 and 241 at a=14,15 and16,
respectively, for a new exclusion. The full-row interval is also
incapable of excluding a padded target. Thus the only remaining degrees
for a new long-leg rank exclusion are

    a(a-1)+1 <= p <= a(2a-1)-a-1.

At a14,15,16 these intervals are [183,363], [211,419], [241,479].
These conclusions need no target rank formula and do not claim that
those intermediate degrees pass.

The exact ranks in the intermediate degrees, the target degenerations and the
exponent question remain open. Finite-field source ranks outside the
proved interval are only lower bounds for characteristic-zero ranks.

## Attribution and verification boundary

The tensor, spectral interpretation and previous frontier retain the
maintained paired-source package's credits. The interpolation, explicit
quotient sequence, filtered-kernel argument and application here are
owner-directed Codex work. No historical priority is claimed.
Concurrent [PR143](https://github.com/1337isnot1337/matrix-mult-bounds/pull/143)
records interpolation bounds through p=a, an all-degree support floor,
and an exact a3 rank atlas. Its common a2,p3 rank70 is reproduced here
as a control. That package remains separate; the present filtered-bundle
argument supplies the longer injective interval and the surjective end.
Basic exterior algebra, Vandermonde interpolation and vector-bundle
filtrations are standard tools. The line-bundle cohomology facts are
credited to [Stacks, Lemma 30.8.1](https://stacks.math.columbia.edu/tag/01XT),
inspected October 23, 2026, with its arbitrary-field hypotheses.

Exact coefficient ranks check finite source sizes and the symmetric
Hankel calculation. They do not formalize this all-size argument.
The beyond-interval integer kernel is a countercontrol to a proposed
full-column claim in every degree. Nothing here constructs a target
or improves the matrix multiplication exponent.
