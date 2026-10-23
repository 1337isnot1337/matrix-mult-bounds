# Quadratic repair cost for two locally Toeplitz long-leg maps

October 23, 2026. Owner-directed AI-derived mathematical argument. Written proof, not independently reviewed or formalized. It is a scoped **negative** result about ordinary linear restrictions of the paired convolution tensor. It does not improve the matrix multiplication exponent.

## Construction question and result

Can the fixed-width paired-source criterion be achieved by keeping the two long-leg maps translation-equivariant in the bulk, allowing arbitrary mixing on the first leg and sparse exceptional columns on the long legs? The answer is **no** if the translation kernels have sublinear bandwidth and there are sublinearly many exceptional columns.

Fix a field `K`, integers `n >= 1`, `m >= 2`, and `D >= 0`. Write

\[
Q_{n,m}=\sum_{p,q=0}^{n-1}\sum_{y,v=0}^{m-1}
 A_{p,q}B_{y,q+v}C_{p+y,v}, \qquad
M_{n,m,n}=\sum_{i,h=0}^{n-1}\sum_{t=0}^{m-1}
 a_{i,h}b_{h,t}c_{t,i}.
\]

Here the first source leg has dimension `n^2`, and each long source leg has dimension `m(n+m-1)`. The three target dimensions are `n^2,nm,mn`.

Let `A`, `B`, `C` be ordinary, separate linear maps on those legs. **The first map is completely arbitrary:**

\[
 A_{p,q}\longmapsto \sum_{i,h}a^{p,q}_{i,h}a_{i,h}.
\]

Let `E_B,E_C` be sets of source *long-coordinate column indices* in `{0,...,n+m-2}`; their cardinalities are `e_B,e_C`. On all nonexceptional columns require the following Toeplitz rules, with coefficients that can depend arbitrarily on `n`:

\[
 B_{y,s}\longmapsto\sum_{t=0}^{m-1}\sum_{k=-D}^{D}
             \beta_{y,t,k}\,b_{s-k,t}\quad(s\notin E_B),
\]
\[
 C_{z,v}\longmapsto\sum_{u=0}^{m-1}\sum_{\ell=-D}^{D}
             \gamma_{v,u,\ell}\,c_{u,z-\ell}\quad(z\notin E_C).
\]

An output variable with outer index outside `{0,...,n-1}` is omitted. **Every exceptional column is unrestricted**: its map may be nonlocal and may use all target coordinates. The Toeplitz matrices need not be invertible, symmetric, rational, or the same for the two legs.

Put `L=m-1+D` and, for `n>2L`,

\[
  g_B=\max(0,n-2L-m e_B),\qquad
  g_C=\max(0,n-2L-m e_C).
\]

**Theorem (ordinary two-long-leg Toeplitz obstruction).** For the tensor `T=(A,B,C)(Q_{n,m})`, the residual `R=M_{n,m,n}-T` satisfies

\[
 \boxed{\operatorname{rank}_{A\mid B\otimes C}(R)
       \;\ge\; g_Bg_C,
       \qquad \underline R(R)\;\ge\;g_Bg_C.}
 \tag{1}
\]

The bound is also valid as zero when `n<=2L`. The second inequality is border rank over an algebraic closure of `K`, since every flattening rank is a lower bound for border rank.

Consequently, for fixed `m>=2`, any family with `D_n=o(n)` and `e_{B,n}+e_{C,n}=o(n)` has

\[
 \underline R(R_n)\ge n^2-o(n^2).
 \tag{2}
\]

It therefore cannot be repaired by auxiliary tensors of border rank `O(n^alpha)` for any `alpha<2` in an ordinary restriction of `Q_{n,m}\oplus S_n` to the full matrix target. This includes the `O(n)` and `O(n^{4/3})` repair budgets in the project's existing *conditional* exponent route. The conclusion is about this map class only, not about the existence of the unrestricted construction.

## Proof

All calculations use the integral domain `K[X^{\pm1},Y^{\pm1}]`, whose fraction field is `K(X,Y)`. Introduce the Laurent polynomial symbols

\[
 F_t(X,Y)=\sum_{y=0}^{m-1}\sum_{k=-D}^{D}
       \beta_{y,t,k}X^{-k}Y^y,
 \qquad
 G_u(X,Y)=\sum_{v=0}^{m-1}\sum_{\ell=-D}^{D}
       \gamma_{v,u,\ell}X^vY^{-\ell}.
 \tag{3}
\]

Let `I={L,...,n-1-L}`. Define good source indices

\[
 Q_{\mathrm{good}}=\{q\in I:q+v\notin E_B\ \text{for all}\ 0\le v<m\},
\]
\[
 P_{\mathrm{good}}=\{p\in I:p+y\notin E_C\ \text{for all}\ 0\le y<m\}.
\]

Each exceptional B column removes at most `m` values of `q`, and likewise for C. Thus `|Q_good|>=g_B` and `|P_good|>=g_C`. Let `G=P_good x Q_good`, so `|G|>=g_Bg_C`.

For `(p,q) in G`, all source indices `B_{y,q+v}` and `C_{p+y,v}` use their Toeplitz rules. Moreover, because `p,q` are at least `L` away from both outer boundaries, *every* `b_{q+v-k,t}` and `c_{u,p+y-ell}` in those rules has outer index between `0` and `n-1`. In particular no finite-output truncation occurs. Encode a B-C target tensor by its `m x m` Laurent polynomial matrix: the coefficient of `b_{q',t}c_{u,p'}` contributes `X^{q'}Y^{p'}` in entry `(t,u)`. Direct substitution into the source gives for the individual A-source slice

\[
  \sum_{y,v,k,\ell}\beta_{y,t,k}\gamma_{v,u,\ell}
      X^{q+v-k}Y^{p+y-\ell}
     =X^qY^p F_t(X,Y)G_u(X,Y).
 \tag{4}
\]

The separation on the right is the key point: for every good source slice, its entire target middle-channel matrix has *rank at most one over `K(X,Y)`*, independently of the values and support of the two Toeplitz kernels.

Now contract the first target leg with an arbitrary linear functional `w=(w_{i,h})` and denote by

\[
 a_{p,q}(w)=\sum_{i,h}w_{i,h}a^{p,q}_{i,h}
\]

the coefficient induced on original A-source coordinate `(p,q)`. Consider the subspace

\[
 V=\{w:\;a_{p,q}(w)=0\ \text{whenever }(p,q)\notin G\}.
\]

These are at most `n^2-|G|` homogeneous linear constraints on the `n^2` coordinates of `w`; hence `dim(V)>=|G|>=g_Bg_C`, regardless of the first-leg map.

For `w in V`, the contracted mapped source has coefficient matrix

\[
 T(w)=U_w(X,Y)\,F(X,Y)G(X,Y)^T,
\quad
 U_w=\sum_{(p,q)\in G}a_{p,q}(w)X^qY^p.
 \tag{5}
\]

The contracted target has coefficient matrix

\[
 M(w)=L_w(X,Y) I_m, \qquad
 L_w=\sum_{i,h=0}^{n-1} w_{i,h}X^hY^i.
 \tag{6}
\]

If `R(w)=0`, equations (5)-(6) give `L_w I_m=U_w FG^T` over `K(X,Y)`. For `L_w != 0`, the left matrix has rank `m>=2` and the right matrix has rank at most one, a contradiction. Thus `L_w=0`. Its monomials are distinct, so every `w_{i,h}=0`. The residual flattening is therefore injective on `V`, proving the first inequality (1). The border-rank inequality follows from flattening monotonicity. For `D_n,e_B,e_C=o(n)` and fixed `m`, the product `g_Bg_C` is `n^2-o(n^2)`, giving (2). QED.

## Scope, controls, and next target

This proof assumes ordinary local linear maps and a genuine bounded-stencil Toeplitz rule on **both** long legs outside specified column exceptions. It permits arbitrary first-leg mixing and arbitrary nonlocal maps on the exceptions. It does **not** cover maps with `Theta(n)` distinct non-Toeplitz source columns, arbitrary variable-coefficient bulk maps, subspaces that mix B and C source legs, or singular Laurent limits in which divergent Q and auxiliary contributions cancel. No general lower bound on `Q_{n,m}` degenerations is asserted.

The middle-width hypothesis is sharp for the argument: when `m=1` and `D=0`, identity-index maps give `Q_{n,1}=M(n,1,n)` exactly, so the residual is zero.

The standard-library exact verifier contracts the source and target coefficients for five finite tests, including arbitrary non-Toeplitz first-leg mixing and one deliberately nonlocal B and C exceptional column. It checks the polynomial symbols on every good source index, then computes the full residual flattening rank over `F_101`. Observed ranks are `36,36,64,81,100`, each above the corresponding bound. These finite controls are **not** the proof of the all-size theorem.

```sh
python -S research/ai/2026-10-23-toeplitz-long-legs/verify.py --output results/toeplitz-long-legs-2026-10-23/verification.json
python -m unittest discover -s tests -p test_toeplitz_long_legs.py -v
```

**Next precise construction target:** allow one of B or C to have a genuinely variable-coefficient bulk map while the other retains bandwidth `o(n)`, and determine whether the resulting channel-symbol module can have full generic rank `m` with `o(n^{3/2})` repair. Any candidate must state complete coefficient identities and quantify exceptional columns. A separate, more ambitious target is a singular Laurent construction whose Q and auxiliary pole coefficients cancel; this theorem cannot adjudicate that case.

## Attribution and dependencies

This is a new scoped deduction from the maintained coefficient definition of `Q`, not a reproduction of an external theorem. The source convention and the unconstructed correction route are inherited from `research/ai/2026-10-20-paired-construction/outer_product_injection.md` and `research/ai/2026-10-21-correction-budget/README.md`. Their original authorship and claim status are unchanged. The only imported algebraic facts are the elementary rank bound for an outer product over a field, monomial independence, and the fact that a flattening rank lower-bounds border rank. No claim of historical priority, independent review, or exponent improvement is made.
