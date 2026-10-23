# A quadratic repair barrier for variable-coefficient long-leg maps

October 23, 2026. Owner-directed AI-derived argument. Proof written; no independent review or formalization. This is a necessary-condition theorem for an **ordinary** restriction of the paired source. It neither constructs an exponent-improving family nor rules out singular Laurent degenerations.

## The tensor and the shift-window condition

Fix a field K, integers n>=1, m>=2 and D>=0. Use the maintained source and target coefficient conventions

\[
 Q_{n,m}=\sum_{p,q=0}^{n-1}\sum_{y,v=0}^{m-1}
     A_{p,q}B_{y,q+v}C_{p+y,v},\qquad
 M_{n,m,n}=\sum_{i,h=0}^{n-1}\sum_{t=0}^{m-1}
     a_{i,h}b_{h,t}c_{t,i}.
\]

The first-leg map A is **arbitrary**. On source columns s outside an exceptional set E_B of size e_B, require the B map

\[
 B_{y,s}\mapsto\sum_{t=0}^{m-1}\sum_{k=-D}^{D}
       \beta_{y,t,k}(s)b_{s-k,t}.
 \tag{1}
\]

The coefficients \(\beta_{y,t,k}(s)\) may depend on s and n without any Toeplitz assumption. On columns z outside an exceptional set E_C of size e_C, require the other long leg to be Toeplitz:

\[
 C_{z,v}\mapsto\sum_{u=0}^{m-1}\sum_{\ell=-D}^{D}
       \gamma_{v,u,\ell}c_{u,z-\ell}.
 \tag{2}
\]

Discard target outer coordinates outside 0,...,n-1. Maps on exceptional source columns are arbitrary, including nonlocal maps. The same D is used for convenience; replacing it with the maximum of two bandwidths suffices.

Write \(L=m-1+D\), \(I=\{L,\ldots,n-1-L\}\), and, when n>2L,

\[
 Q_0=\{q\in I:q+v\notin E_B\ (0\le v<m)\},\qquad
 P_0=\{p\in I:p+y\notin E_C\ (0\le y<m)\}.
\]

For q in Q_0 and any y,t,k, form the **shift-window vector**

\[
 w_{q,y,t,k}=(\beta_{y,t,k}(q),\beta_{y,t,k}(q+1),\ldots,
                 \beta_{y,t,k}(q+m-1))\in K^m.
 \tag{3}
\]

Let W_B be their common K-linear span (all q in Q_0, all y,t,k). The hypothesis is

\[
                    r=\dim_K W_B<m.                 \tag{4}
\]

Unlike a single-window rank restriction, (4) requires one fixed proper channel subspace across **all** good q and all stencil coefficients. In particular, its basis may depend on n but not on q, y, t, or k.

**Theorem (one variable long leg, proper shift-window span).** For every choice of the maps above satisfying (4), and R=M-(A,B,C)(Q),

\[
 \operatorname{rank}_{a\mid b\otimes c}(R)\ \ge
 \bigl(n-2L-me_B\bigr)_+\bigl(n-2L-me_C\bigr)_+,
 \qquad\underline R(R)\ \ge
 \bigl(n-2L-me_B\bigr)_+\bigl(n-2L-me_C\bigr)_+.
 \tag{5}
\]

For n<=2L, interpret the bound as zero. The border-rank inequality holds over an algebraic closure of K. In a family with fixed m, D=o(n), e_B+e_C=o(n), and r<m for every sufficiently large n, the correction border rank is at least \(n^2-o(n^2)\). Therefore these ordinary maps cannot supply an \(o(n^2)\) auxiliary correction, including the previously proposed \(O(n)\) or \(O(n^{4/3})\) budgets.

## Proof

Since W_B has basis \(\phi_1,\ldots,\phi_r\in K^m\), there are scalars \(h_{q,y,t,k,j}\) such that, simultaneously for every v in {0,...,m-1},

\[
 \beta_{y,t,k}(q+v)=\sum_{j=1}^r h_{q,y,t,k,j}\phi_j(v).
 \tag{6}
\]

For p in P_0 and q in Q_0, neither exceptional map occurs in the source slice A_{p,q}. All shifted target indices are interior because p,q are at distance at least L from the boundary. Encode a target b-c tensor as an m-by-m Laurent-polynomial matrix, assigning \(b_{q',t}c_{u,p'}\) the monomial \(X^{q'}Y^{p'}\) in entry (t,u). Substituting (6) into the source slice gives

\[
 T_{p,q;t,u}(X,Y)=X^qY^p\sum_{j=1}^r
    \underbrace{\left(\sum_{y,k}h_{q,y,t,k,j}X^{-k}Y^y\right)}_{F_{q,j,t}}
    \underbrace{\left(\sum_{v,\ell}\phi_j(v)\gamma_{v,u,\ell}X^vY^{-\ell}\right)}_{G_{j,u}}.
 \tag{7}
\]

Notice that \(F_{q,j,t}\) can vary arbitrarily with q while **G_{j,u} is independent of both p and q**. This is why a common window span, rather than separate low-dimensional spans for individual windows, is necessary for this argument.

Let \(a_{p,q}(z)\) be the first-leg coefficient induced at source coordinate (p,q) when the target first leg is contracted with \(z=(z_{i,h})\in K^{n^2}\). Set

\[
 V=\{z:a_{p,q}(z)=0\text{ whenever }(p,q)\notin P_0\times Q_0\}.
\]

There are at most \(n^2-|P_0||Q_0|\) linear conditions, so \(\dim V\ge |P_0||Q_0|\). For every z in V, (7) shows that the contracted mapped source has the form

\[
 T(z)=\sum_{j=1}^r H_{z,j}(X,Y)G_j(X,Y)^T,
\quad H_{z,j,t}=\sum_{(p,q)\in P_0\times Q_0}
 a_{p,q}(z)X^qY^pF_{q,j,t}.
 \tag{8}
\]

Consequently \(\operatorname{rank}_{K(X,Y)}T(z)\le r<m\). In contrast, the contracted matrix tensor is

\[
 M(z)=\left(\sum_{i,h}z_{i,h}X^hY^i\right)I_m.
 \tag{9}
\]

For z nonzero, the Laurent polynomial in (9) is nonzero by monomial independence, so M(z) has rank m over K(X,Y). Thus R(z)=M(z)-T(z) cannot be zero for any nonzero z in V. The first-leg flattening of R is injective on V, hence its rank is at least \(\dim V\ge|P_0||Q_0|\). Each exceptional B column spoils at most m possible q, and each exceptional C column spoils at most m possible p. Therefore \(|Q_0|\ge(n-2L-me_B)_+\) and \(|P_0|\ge(n-2L-me_C)_+\), proving (5). Flattening rank is lower semicontinuous and no larger than tensor border rank over the algebraic closure. QED.

## Explicit genuinely variable coefficient classes

**Polynomial coefficients.** Suppose every coefficient \(\beta_{y,t,k}(s)\), with different coefficients allowed for every triple (y,t,k), is polynomial in the image of integer s in K of degree at most d. By the binomial theorem, for fixed q each function v -> \(\beta_{y,t,k}(q+v)\) lies in the common span of \(1,v,\ldots,v^d\), evaluated at v=0,...,m-1. Therefore \(r\le d+1\). In particular all polynomial bulk maps of degree at most m-2 satisfy the theorem. The identity holds in every characteristic; evaluation collisions can only reduce the span dimension.

**Exponential-polynomial coefficients.** More generally, assume a finite *common* set of nonzero scalars \(\lambda\in K\) and bounds d_lambda>=1 such that

\[
 \beta_{y,t,k}(s)=\sum_{\lambda}\lambda^sP_{y,t,k,\lambda}(s),
 \qquad\deg P_{y,t,k,\lambda}<d_\lambda.
\]

For each q, the window function in v belongs to the fixed span of \(\lambda^v v^j\), j=0,...,d_lambda-1. Hence \(r\le\sum_\lambda d_\lambda\). If this sum is <m, (5) applies. Examples are a polynomial times one geometric modulation, or two distinct geometric modulations when m>=3. All coefficients may vary separately in the y,t,k indices.

**Common recurrences.** The same conclusion holds over any K if all bulk sequences s -> \(\beta_{y,t,k}(s)\) obey the same monic constant-coefficient recurrence of order r<m on the relevant consecutive columns. Indeed the recurrence expresses every m-term window as one fixed linear combination of its first r values, with r common basis vectors in K^m. This formulation does not require the recurrence to split into roots in K.

**Mirrored version.** Interchange the two long legs. If B is Toeplitz and C has variable coefficients \(\gamma_{v,u,\ell}(z)\), replace (3) by the y-windows \((\gamma_{v,u,\ell}(p+y))_{y=0}^{m-1}\), spanning one fixed subspace W_C of dimension <m for all good p,v,u,ell. Expanding that common y-basis places the fixed factor on the B side of (7), and the same contraction argument proves (5).

## What this does not establish

A fully arbitrary variable-coefficient map can have a full m-dimensional shift-window span, even with D=0 and no exceptional columns: take the m sequences \(\beta_{y,0,0}(s)=1_{s\equiv y\pmod m}\) for y=0,...,m-1. Their simultaneous windows form a permutation basis of K^m over every field. The proof above then gives no rank gap. This observation is **not** a construction of a small correction.

Nor does the theorem cover a q-dependent basis W_q, both long legs varying without a common fixed factor, large exceptional-column sets, or singular Laurent trajectories with cancellation between source and auxiliary poles. It is not a general ordinary-rank or border-rank obstruction for Q(n,m). To escape this particular no-go theorem, one ordinary map with C Toeplitz needs full channel-window span m for large n. That condition is necessary, not sufficient.

The exact verifier checks five instances over F_101: linear and quadratic polynomial B bulk coefficients, two geometric modulations, a repeated-root geometric modulation with deliberately nonlocal exception columns on both legs, and nonzero bandwidth. It independently checks the common-window identities, direct source contractions against (7), and the full residual flattening with non-Toeplitz A mixing. Observed ranks are 64, 100, 100, 144, 144, versus proved finite lower bounds 16, 16, 16, 25, 36. A deliberately full-window control confirms the hypothesis is not automatic. These finite checks do not prove the arbitrary-field statement.

```sh
python -S research/ai/2026-10-23-shift-window-long-legs/verify.py --output results/shift-window-long-legs-2026-10-23/verification.json
python -m unittest discover -s tests -p test_shift_window_long_legs.py -v
```

## Provenance

This extension uses the project's maintained Q(n,m) and correction-budget definitions and continues the concurrently open two-Toeplitz obstruction PR #157. It is a new local linear-algebra argument allowing one genuinely variable-coefficient leg, without importing any external theorem. The exact source references, dependency hashes, attribution, and limited verification status are recorded in `sources.json`. No independent review, priority claim, or exponent gain is asserted.
