# Allowing extra shared source coordinates

Continuation of the October 20 construction sprint. This is a conditional
extension of the existing [fat-point growth criterion](../2026-10-20-concavity-equivalence/fatpoint_growth_route.md).
The required tensor maps remain unconstructed. No smaller exponent is proved.

## Construction question

Let `m` tend to infinity through an unbounded sequence, write
`N_m=m(m+1)/2`, and allow integers `a_m>=m`, `k_m>=1`, and `B_m`.
Suppose actual complex tensor degenerations can be constructed with

\[
C(a_m,B_m)\unrhd T_m\otimes B_X(k_m),\qquad
\limsup\frac{a_m}{m}\le\sigma,\qquad
\limsup\frac{B_m}{k_mN_m}\le\rho,                 \tag{1}
\]

where `sigma>=1` and `rho>=1` are fixed finite constants. The target and
the orientation of its shared leg are exactly those in the cited criterion.
In particular, the target's nonshared flattening forces `B_m>=k_mN_m`.

The source's shared dimension need not equal `m`. Cases such as
`a_m=m+1`, or more generally `a_m=m+o(m)`, retain the same asymptotic
consequence as the equal-shared-dimension construction. Even a small fixed
relative increase can be allowed.

## Conditional inequality

Use the preceding criterion's notation: `d=1/t`, the homogeneous profile
`F`, `f(s)=F(1,s)`, and its positive thin slope `L`. The external baseline
and its detecting-character argument give the relevant range `d>=4/3`.
This note imports those established hypotheses and the shared-leg entropy
inequality; it does not supply a new spectrum theorem.

Since `a_m=O(m)` and `B_m>=k_mN_m`, one has `B_m/a_m -> infinity`.
Homogeneity and `P<=F` give

\[
\frac{P(a_m,B_m)}{k_m m^{d+1}}
\le
\left(\frac{a_m}{m}\right)^{d-1}
\frac{B_m}{k_m m^2}
\frac{f(B_m/a_m)}{B_m/a_m}.
\]

Its upper limit is at most `rho sigma^(d-1)L/2`. The target side is
unchanged from the cited proof:

\[
\liminf\frac1{m^{d+1}}\sum_{u=1}^{m}P(u,m+1-u)
\ge\int_0^1F(x,1-x)\,dx
\ge\frac{L2^{2-d}}{d(d+1)}.
\]

Monotonicity under (1), multiplicativity of the EPR factor, and the
shared-leg entropy inequality therefore imply

\[
\boxed{\rho\,\sigma^{d-1}d(d+1)2^d\ge8.}       \tag{2}
\]

The left side is strictly increasing for `d>0`, since its logarithmic
derivative is `log(sigma)+1/d+1/(d+1)+log(2)>0`. Consequently, a uniform
construction satisfying

\[
\rho\,\sigma^{1/3}<\frac9{7\,2^{1/3}}          \tag{3}
\]

would force a strict uniform separation from `d=4/3` and hence a smaller
arithmetic matrix multiplication exponent by the same external detecting
character argument. This conclusion remains conditional on all the maps
and asymptotic bounds in (1).

At cost `rho=1`, condition (3) is exactly

\[
\sigma<\frac{729}{686}.
\]

Thus a cost-one construction with `a_m/m -> 1` retains the previously
recorded conditional consequence `omega<=125/56`. A cost-one construction
with `limsup a_m/m<=21/20` would still imply `omega<=2247/1000`.
Neither family is constructed here.

## Exact numeric certificate

For `rho=1`, `sigma=u/v`, and `d=p/q>1`, the strict comparison of the
left side of (2) with eight is equivalent to the integer inequality

\[
u^{p-q}[p(p+q)]^q2^p
<v^{p-q}q^{2q}2^{3q}.                            \tag{4}
\]

The verifier checks (4) for `(u,v,p,q)=(1,1,168,125)` and
`(21,20,1000,749)`. It also checks the endpoint equality
`sigma=729/686,d=4/3` and a failing larger proposed improvement as a
negative control. No floating-point comparison is used for acceptance.

## What this changes in the search

The next finite probe is `C(5,10) -> T_4`, allowing a general rectangular
shared map and Laurent maps on the other two legs. The repository's
earlier coordinate/permutation search at this format is explicitly
credited in [mixed restrictions](../2026-10-20-mixed-restrictions/README.md).
The new question allows dense linear combinations and does not repeat
that coordinate search.

Ordinary maps are still excluded in this probe: a nonzero convolution
slice has rank ten, and reducing the output dimension from fourteen to
ten leaves rank at least six, whereas a coherent slice of `T_4` has rank
four. The desired construction therefore requires a genuine degeneration.
A successful isolated finite probe would be useful but would not by
itself establish the unbounded family required in (1).

This note extends the source aspect allowed by an existing conditional
proof. It neither constructs the missing maps nor claims independent
mathematical review or formalization.
