# A concrete fat-point construction threshold for beating 9/4

October 20, 2026. AI-derived research, unreviewed and not formalized.
**The required degeneration below is unconstructed. No smaller exponent is
proved.** This extends the Koszul worker's degree-three target to an all-degree
growth question, without claiming its interpolation construction as new.

## Construction question selected for continued research

For each integer `a>=1`, let `N_a=a(a+1)/2` and define the tensor

$$T_a=\sum_{i+j+k+l=a-1}X_{i+k}Y_{i,j}Z_{k,l}.$$

The two nonshared spaces have coordinates indexed by monomials in two variables
of total degree at most `a-1`, hence dimension `N_a`. The shared space has
dimension `a`. Splitting according to the degree of Y gives `a` matched sectors
whose tensors are `C(u,a+1-u)`, with their outputs as the common shared space.
The case `a=4` is the Koszul worker's target at branch revision `30219d0`.

Can one construct, along unbounded integers `a`, with some integers `k_a>=1`,

$$C(a,B_a)\ \unrhd\ T_a\otimes B_X(k_a),\qquad
\limsup_{a\to\infty}\frac{B_a}{k_aN_a}\le\rho,$$

with the same `rho < 9/(7*2^(1/3))`, approximately `1.02047`?

This would force a strict exponent improvement. Coordinate selection and
diagonal weights cannot achieve cost one even for the degree-three case,
as the Koszul worker proves. The question here requires new linear bases or
a different degeneration, not a rerun of that failed monomial search.

## Why this threshold matters

This is a conditional implication under the preceding scaling theorem, not
a construction certificate. Put `d=1/t` for an arbitrary character and let
`F` be its homogeneous limit. For each fixed integer `a`, concavity gives the
positive finite thin slope

$$S_a=\lim_{b\to\infty}\frac{P(a,b)}b.$$

Let `L=lim_{s->infinity} F(1,s)/s`. It is finite by concavity and positive
by iterated tripling. The same tripling iteration, followed by the thin limit,
gives for every positive integer `a,b`

$$P(a,b)\le S_a\left(b+\frac{a-1}{2}\right). \tag{1}$$

The scaling theorem gives `P(a,b)<=F(a,b)`. Letting `b` tend to infinity in
that inequality shows `S_a<=L a^(d-1)`. On the other hand, use (1) at `(n,ns)`
for integer `s>=1`, divide by `n^d`, and take lower limits:

$$\liminf_n\frac{S_n}{n^{d-1}}\ge\frac{F(1,s)}{s+1/2}.$$

Let `s` tend to infinity. Thus

$$\lim_{a\to\infty}\frac{S_a}{a^{d-1}}=L. \tag{2}$$

For `f(s)=F(1,s)` and `v=f(1)`, its right derivative at one is at least `L`
and at most `dv/2`, by the one-sided symmetry argument. Therefore `v>=2L/d`.
Every subsequent increment is at least its limiting slope `L`, giving

$$f(s)\ge L\left(s+\frac2d-1\right)\quad(s\ge1).$$

By symmetry and homogeneity,

$$F(x,y)\ge L\min(x,y)^{d-1}
\left(\max(x,y)+(2/d-1)\min(x,y)\right). \tag{3}$$

If the proposed degeneration exists at cost `rho`, multiplicativity, the
dot-product value and shared-leg entropy give

$$P(a,B_a)\ge k_a\sum_{u=1}^aP(u,a+1-u).$$

The target Y flattening forces `B_a>=k_a N_a`, hence `B_a/a` tends to infinity
along the constructed sequence. The upper bound `P<=F` and homogeneity give

$$\frac{P(a,B_a)}{k_a a^{d+1}}
\le\frac{B_a}{k_a a^2}\frac{f(B_a/a)}{B_a/a}.$$

Its upper limit is at most `rho L/2`. On the target side, the scaling limit and rank bound permit
bounded convergence for the step functions on `0<x<1`: each scaled term is
at most one, and the limiting profile is continuous in the interior. Hence

$$\frac{\rho L}{2}\ge\int_0^1F(x,1-x)\,dx
\ge\frac{L\,2^{2-d}}{d(d+1)}.$$

The last integral is the elementary integral of (3) on the two halves of the
unit interval. Cancel `L>0` to obtain the quantitative necessary inequality

$$\boxed{\rho\,d(d+1)2^d\ge8.} \tag{4}$$

At `d=4/3`, the right cost threshold is

$$\rho\ge\frac9{7\,2^{1/3}},\qquad
\left(\frac9{7\,2^{1/3}}\right)^3=\frac{729}{686}>1.$$

Since the left side of (4) is strictly increasing in `d>0`, any fixed cost
below this threshold forces `d>4/3` uniformly over all characters and yields
a smaller exponent by the external detecting-character argument.

For the **unproved** cost-one construction, the exact integer comparison

$$[168(168+125)]^{125}2^{168}
 < [125^2]^{125}2^{375}$$

places the root above `d=168/125`. Thus that construction would certify
`omega<=125/56`, approximately `2.23214`. This is solely a conditional target.
The finer root can be displayed numerically, but acceptance needs no floating
point arithmetic.

This argument only needs one `k_a` at each admissible `a`, not a separate
large-`k` limit at fixed `a`. The thin-slope identity (2) is independently
useful but is not required for this weaker construction premise.

The concurrent Koszul note at
[`292ba18`](https://github.com/1337isnot1337/matrix-mult-bounds/commit/292ba18)
studies the same all-degree targets and critical cost threshold. Its
quantitative criterion uses a diagonal tangent bound and a tripling lower
envelope. The present argument uses the exact asymptotic slope `L` on both
sides, giving the stronger conditional cost-one rational consequence
`125/56` under the same sequence premise. Neither note supplies the premise;
the overlapping targets and critical threshold are not counted twice.

## Initial obstruction checks and unresolved work

The tensor `T_a` has border rank `N_a`: triangular-grid interpolation proves
the upper bound, and its full `N_a`-dimensional Y flattening proves the lower
bound. This is the standard interpolation construction used by the other
worker at `a=4`, extended to the degree-`a-1` triangular lower set.

Every full-space Koszul flattening passes at the proposed cost one. Along the
shared `a`-dimensional source leg, with `B=kN_a>=a`, the source formula reduces to

$$\operatorname{rank}K_p(C(a,B))=(B+p)\binom{a-1}{p}.$$

The target's border rank `B` bounds its corresponding rank by
`B binom(a-1,p)`. The other input leg is either full column rank or has rank
at least that border-rank upper bound, by the Koszul worker's same argument
with `4` replaced by `a`. The source output's Koszul map has maximal matrix
rank; the padded target cannot exceed it. These tests are necessary only.

In fact the target reaches that shared-leg rank bound for every `p`:

$$\sum_{u=1}^a\min\left\{u\binom ap,(a+1-u)\binom a{p+1}\right\}
=N_a\binom{a-1}p.$$

The first term is the smaller one precisely for `u<=a-p`. Sum the two
arithmetic progressions to obtain the equality. This extends the other
worker's degree-three observation to every degree.

The outstanding task is an actual degeneration from the specified convolution
source, or a stronger obstruction. Interpolation from a diagonal rank-`N_a`
tensor is insufficient: there is no established restriction returning that
diagonal tensor from `C(a,kN_a)` with the required shared input dimension.

`fatpoint_route.py` exports the exact threshold and a rational conditional
root certificate, and checks the displayed rank identity through `a=32`.
Independent exact coefficient matrices test `a=1,...,5`. The general
implications above are written arguments; these computations do not supply
the missing source degeneration.

## Attribution

- [Scaling limit and one-sided derivative argument](homogeneous_rigidity.md).
- The Koszul branch, observed at
  [`30219d0`](https://github.com/1337isnot1337/matrix-mult-bounds/commit/30219d0),
  `research/ai/2026-10-20-koszul/research_note.md`, Sections 6-8:
  degree-three target, interpolation certificate, all-leg Koszul screening and
  the coordinate/diagonal-weight obstruction. Those results belong to that
  concurrent worker and are not independent review here.
- OpenAI's character, shared-leg and detecting-character machinery and
  Uznański's replication construction are the attributed external inputs listed
  in the preceding note. None was locally rebuilt in Lean.
