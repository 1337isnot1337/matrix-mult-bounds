# An exact all-size construction after quotienting the pole space

October 20, 2026. AI-derived written proof, externally unreviewed. This is
an actual degeneration of a **projection** of the target. It does not
construct the full target or improve the matrix multiplication exponent.

## 1. The projected problem has a positive solution

Keep `m=2s`, `D=m-1`, `N=m(m+1)/2` from the [shared-family note](README.md),
and put `R=s+1`. Let `E` be the evaluation projection

\[
E(X_i)=\sum_{j=0}^{R-1}j^i\widehat X_j.
\]

Its kernel is the degree-`D` binary-form space divisible by
`g(t)=prod_(j=0)^(R-1)(t-j)`. Thus it is exactly the pole image of the
shared family, in the coefficient conventions used there. The projected
target is

\[
\overline T_m=(E\otimes I\otimes I)T_m
=\sum_{a+b+c+d=D}\sum_{j=0}^{R-1}
j^{a+c}\widehat X_jY_{a,b}Z_{c,d}. \tag{1}
\]

**Proposition.** For every `s>=2`, there is an explicit rational Laurent
degeneration

\[
C(R,N)\unrhd\overline T_m. \tag{2}
\]

The shared map in this construction is constant and invertible. The target
has dimensions `(R,N,N)`, with nonshared flattening ranks
`N-s(s-1)/2`; the omitted directions are retained as zero coordinates.

The construction uses the exact identity

\[
N=DR+1,\qquad N+R-1=(D+1)R. \tag{3}
\]

The first identity gives `D` full residue levels and one final constant
in the source input. The second gives `D+1` full residue levels in the
source output. All maps are given next; there is no existence assumption.

## 2. Explicit source maps

View `C(R,N)` as univariate multiplication of polynomials of degrees below
`R` and `N`, with product degree below `(D+1)R`. Let `ell_j(t)` be the
degree-below-`R` Lagrange polynomial for node `j` among `0,...,R-1`.
The constant shared map replaces the first-leg source polynomial basis
by these `ell_j`.

For a polynomial `f`, write `rem_g(f)` for its remainder modulo the monic
polynomial `g`. Every output polynomial has a unique expansion

\[
H(t)=\sum_{h=0}^{D}g(t)^h H_h(t),\qquad \deg H_h<R. \tag{4}
\]

For target input coordinate `Y_(a,b)`, put `u=a+b`, `h=D-u` and use the
source polynomial

\[
F_{a,b}(t,\epsilon)
=\epsilon^{-h}g(t)^h\operatorname{rem}_g(t^a). \tag{5}
\]

Its degree is below `N`: for `u=0` it is `g^D`, of degree `N-1`; for
`u>0` it lies in an earlier full residue level. Replacing each source input
coordinate by the corresponding coefficient of (5) defines the entire
second-leg map.

For target output coordinate `Z_(c,d)`, put `v=c+d`. Define the source
output functional

\[
\Lambda_{c,d,\epsilon}(H)
=\epsilon^v\sum_{j=0}^{R-1}j^c H_v(j). \tag{6}
\]

Applying (6) to each output monomial defines the third-leg map. These are
ordinary linear functionals with Laurent-monomial scalar factors. Their
coefficients are rational, since the nodes and the monic polynomial are
rational.

## 3. Full coefficient verification

The coefficient of `Xhat_j Y_(a,b) Z_(c,d)` after the three maps is

\[
\Lambda_{c,d,\epsilon}(\ell_j F_{a,b}). \tag{7}
\]

Both `ell_j` and `rem_g(t^a)` have degree below `R`. Their product therefore
has at most two nonzero `g`-adic digits:

\[
\ell_j(t)\operatorname{rem}_g(t^a)=M_0(t)+g(t)M_1(t),
\qquad \deg M_0,\deg M_1<R. \tag{8}
\]

Consequently (7) can be nonzero only if `v=h` or `v=h+1`. In the first case
its parameter exponent is zero and its coefficient is

\[
\sum_{k=0}^{R-1} k^c M_0(k)
=\sum_{k=0}^{R-1} k^c\ell_j(k)k^a=j^{a+c}. \tag{9}
\]

This is precisely (1), since `v=h` is equivalent to `u+v=D`. In the second
case the parameter exponent is one. Every other coefficient vanishes,
including every coefficient at a negative power. Thus the full transformed
tensor is `Tbar_m+epsilon E_m` for a fixed rational tensor `E_m`, proving
(2). No cancellation outside the explicitly checked digit decomposition is
being assumed.

The target's input kernel is equally explicit. At each degree `u`, the
evaluation map on binary forms has kernel dimension `max(0,u+1-R)`, since
it has the `R` distinct evaluation nodes. Summing from `u=0` to `D` gives
`s(s-1)/2`; the other nonshared leg is symmetric.

This construction resolves a necessary projected subproblem positively.
It does not recover the `s-1` pole directions removed by `E`. Keeping those
directions under the shared factor `epsilon^(-1)` introduces carries to the
next residue level. Matching those carries to the full target remains open.

## 4. Why the full shared family needs a Laurent nonshared map

The following scoped observation rules out making both nonshared maps
regular in the **full** construction problem with the exact shared map
`A_epsilon` from (1) of the companion note. The overall scalar normalization
of that shared map is part of the hypothesis.

**Proposition.** There are no two maps `Y_epsilon,Z_epsilon`, both regular
at zero, such that

\[
(A_\epsilon\otimes Y_\epsilon\otimes Z_\epsilon)C(m,N)
\longrightarrow T_m. \tag{10}
\]

Write `A_epsilon=A_regular+epsilon^(-1)A_pole` and let
`L=im A_pole=g S^(s-2)`. The quotient map `E` above kills `L`.
Applying it to (10) and taking the constant term would give

\[
\overline T_m
=(EA_{\rm regular}\otimes Y_0\otimes Z_0)C(m,N).
\]

Hence both leading nonshared maps must have rank at least

\[
r=N-s(s-1)/2. \tag{11}
\]

The coefficient of `epsilon^(-1)` in (10) must vanish. Contracting its
shared leg by any covector that is nonzero on `im A_pole` gives

\[
(Y_0\otimes Z_0)C(m,N)(f)=0
\]

for a nonzero source polynomial `f`. Its source slice is multiplication
by `f`, an injective `N`-by-`N+D` matrix. Applying rank-`r` nonshared maps
can lower its rank to no less than

\[
2r-(N+D)=N-s(s-1)-D=s^2+1>0. \tag{12}
\]

This contradicts the required zero slice. For `m=4`, (11) says that both
leading ranks are at least nine, and (12) gives the contradiction `rank>=5`.

This proof does not permit regular leading matrices to replace arbitrary
Laurent maps. Moving an additional scalar pole between the three factors
can change its hypothesis. At least one genuinely Laurent nonshared map is
needed in the normalization fixed here; that case remains open.

## 5. Exact controls and provenance

Run from the repository root:

```sh
python research/ai/2026-10-20-singular-shared-normalization/verify_projection.py --max-s 5 --output results/singular-shared-normalization-2026-10-20/projection.json
```

The verifier expands all source products in rational coefficients, applies
the explicit output functionals, and checks every resulting tensor
coefficient for the selected sizes. Required zeros and all negative
exponents are checked. The all-size conclusion is the written proof, not
a finite experiment.

The `g`-adic filtration and Chinese remainder description are standard
polynomial constructions; no historical novelty is claimed for them. The
specific projected-target maps were derived in this AI session. The regular
map obstruction was also obtained by the sibling construction agent in the
same session at `m=4`; this is overlapping same-session work, not external
independent review. All full-target maps remain missing.
