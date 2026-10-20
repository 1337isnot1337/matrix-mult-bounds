# The fat-point route requires a singular degeneration

October 20, 2026. AI-derived written proof, unreviewed and not formalized.
No exponent improvement is established. This rules out constant linear maps
for the stated source/target family; it does not rule out border degenerations.

Let `T_a` and `N_a=a(a+1)/2` be the target in the
[growth route](fatpoint_growth_route.md), and put `M=k N_a`.

## Exact-restriction lower bound

If `C(A,B)` restricts by constant linear maps to `T_a tensor B_X(k)`, with
the first source input as the shared leg, then

$$\boxed{B\ge 2kN_a-ka-A+1=ka^2-A+1.}$$

In particular, if `a` tends to infinity and `A/a` stays bounded, then

$$\liminf\frac{B}{kN_a}\ge2.$$

This is incompatible with the growth route's cost below `1.020472`. It
applies to arbitrary linear maps on all three legs, including arbitrary shared
bases, within the stated exact-restriction class.

## Proof

Contract a nonzero first-leg functional into `C(A,B)`. The resulting matrix
is multiplication by a nonzero polynomial of degree at most `A-1`:

$$\mathbb C[t]_{<B}\longrightarrow\mathbb C[t]_{<A+B-1}.$$

It is injective, because the polynomial ring is an integral domain. Thus
every nonzero source slice has column rank `B`.

The target is concise on all three legs. Consequently its first-leg
functional space injects into the source's first-leg functional space, its
`M`-dimensional matrix domain injects into the source's `B`-dimensional
domain, and its `M`-dimensional matrix codomain is obtained by a surjective
map from the source's `(A+B-1)`-dimensional codomain.

After restricting any nonzero slice to the target domain, its rank is `M`.
Projecting the codomain can lower rank by at most `A+B-1-M`. Every nonzero
target first-leg slice must therefore have rank at least

$$M-(A+B-1-M)=2M-A-B+1. \tag{1}$$

For the canonical target, contract the coordinate functional selecting `X_0`.
In each degree sector `C(u,a+1-u)` it leaves the single nonzero entry with
both monomial exponents zero. The sectors have disjoint matrix rows and
columns, so this slice has rank `a` in `T_a`, and rank `ka` in its `k` copies.
It is nonzero. Substituting in (1) gives the claimed bound.

More generally this proof uses the minimum slice rank; using only the generic
slice rank, about `N_a/2`, would give a weaker asymptotic cost `3/2`.

## Boundary of the argument

Matrix rank can drop in a limit. The nonzero constant slice lower bound after
composition therefore does not persist under singular parameter-dependent
maps. This proof cannot be used to reject the growth route's border premise.

The first input must be the source shared leg. Returning auxiliary factors,
changing the source tensor, or assigning a larger shared source space can
change the conclusion. For the asymptotic corollary, the actual requirement
is `A/(kN_a)->0`; bounded `A/a` is a sufficient case.

The canonical common X identification is also specified. Arbitrary unrelated
identifications of individual blocks need not have a common rank-`ka` slice.
The all-degree growth target is canonical and has the required slice.

This prevents searching for a constant-factorization certificate at the
desired cost and then mistaking poor numerical conditioning for the only
remaining problem. The next task is an actual singular degeneration and its
exact leading-coefficient certificate.

The ingredients are elementary slice ranks and rank loss under projection.
The target and its interpolation certificate come from the concurrent Koszul
worker; the present restriction obstruction does not claim a new border-rank
lower bound or historical priority.

The concurrent source-obstruction note at
[`6bdab15`](https://github.com/1337isnot1337/matrix-mult-bounds/commit/6bdab15)
uses the same rank-loss principle with the maximum target slice, obtaining an
asymptotic `3/2` cost. The special slice above strengthens that exact-restriction
consequence to cost two. Their catalecticant argument for shared-coordinate
degenerations is stronger than the separate homomorphism test in this branch;
it does not apply to arbitrary shared `GL(a)` transformations.
