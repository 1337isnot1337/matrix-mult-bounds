# Quadratic repair with two variable long maps

October 23, 2026. Owner-directed OpenAI Codex work. Written proof,
unreviewed and not formalized. This is an ordinary-map obstruction.
No matrix target or improved exponent is constructed.

## Statement

Let K be any field, n>=1, m>=2, and D_B,D_C>=0. Use

\[
Q_{n,m}=\sum_{p,q<n}\sum_{y,v<m}A_{p,q}B_{y,q+v}C_{p+y,v},
\qquad M=\sum_{i,h<n}\sum_{t<m}a_{i,h}b_{h,t}c_{t,i}.
\]

All indices start at zero. The first-leg map A is arbitrary. Outside
exceptional source-column sets E_B,E_C, of sizes e_B,e_C, suppose

\[
 B_{y,z}\mapsto\sum_{t<m}\sum_{k=-D_B}^{D_B}
       \beta_{y,t,k}(z)b_{z-k,t},\qquad
 C_{z,v}\mapsto\sum_{u<m}\sum_{\ell=-D_C}^{D_C}
       \gamma_{v,u,\ell}(z)c_{u,z-\ell}.
 \tag{1}
\]

Omit target outer indices outside [0,n). Exceptional columns have
completely arbitrary images, including nonlocal ones. Both coefficient
arrays in (1) may vary with z and n.

Put L=m-1+max(D_B,D_C), I=[L,n-L) intersected with the integers, and

\[
 Q_0=\{q\in I:q+v\notin E_B\text{ for every }v<m\},\quad
 P_0=\{p\in I:p+y\notin E_C\text{ for every }y<m\}.
\]

Let W_B be the common span in K^m of **all** vectors

\[
 (\beta_{y,t,k}(q+v))_{v=0}^{m-1},\quad q\in Q_0,
 \quad y,t<m,\quad -D_B\le k\le D_B.
\]

Write r=dim W_B. This is one common space across q and every stencil
index, not a separate low-dimensional space for each q.

Suppose the C coefficients admit a common profile decomposition

\[
 \gamma_{v,u,\ell}(z)=\sum_{j=1}^s f_j(z)G_{v,u,\ell,j}
 \quad(z\notin E_C),                         \tag{2}
\]

with G constant in z. The functions f_j are arbitrary; they need not
obey a recurrence or have low degree. One may take s to be the dimension
of the span of the coefficient vectors
`(gamma_{v,u,ell}(z))_(v,u,ell)` as z ranges over the good source columns.
A displayed decomposition with possibly nonminimal s also suffices.

**Theorem.** If r*s<m, the residual R=M-(A,B,C)(Q) satisfies

\[
 \operatorname{rank}_{a\mid b\otimes c}R\ge |P_0||Q_0|
 \ge (n-2L-me_C)_+(n-2L-me_B)_+,\qquad
 \underline R(R)\ge |P_0||Q_0|.               \tag{3}
\]

Here x_+=max(x,0); empty interiors give zero. Border rank is taken over
an algebraic closure of K. In particular, for fixed m and bandwidths
and exception counts o(n), the lower bound is n^2-o(n^2).

Consequently, if Q direct-summed with an auxiliary tensor S maps
**ordinarily** to M through long maps of this form on Q, then S has
border rank at least |P_0||Q_0|. Its image must equal R, and linear maps
cannot increase border rank. Such a family cannot use o(n^2) repair.
This assertion does not cover degeneration maps with pole cancellation
between Q and S.

## Proof

Choose a basis phi_1,...,phi_r of W_B, writing

\[
 \beta_{y,t,k}(q+v)=\sum_{a=1}^r h_{q,y,t,k,a}\phi_a(v).
 \tag{4}
\]

Encode a b-c tensor by an m-by-m Laurent polynomial matrix: the
coefficient of b_{h,t}c_{u,i} contributes X^h Y^i to entry (t,u).
This encoding is K-linear and injective.

For a good slice (p,q) in P_0 times Q_0, substitute (2) and (4) in
(1). There are no exceptional columns and no target truncations.
Its symbol is

\[
 T_{p,q}(X,Y)=X^qY^p\sum_{a=1}^r\sum_{j=1}^s
             F_{p,q,a,j}(X,Y)H_{a,j}(X,Y)^T,\tag{5}
\]

where

\[
 F_{p,q,a,j,t}=\sum_{y,k}h_{q,y,t,k,a}f_j(p+y)X^{-k}Y^y,
 \qquad H_{a,j,u}=\sum_{v,\ell}\phi_a(v)G_{v,u,\ell,j}X^vY^{-\ell}.
 \tag{6}
\]

The crucial point is that every H is independent of **both** p and q.
Both long maps vary, but any linear combination of good slices still
has row space inside the span of the same r*s vectors H over K(X,Y).
Its symbol rank is at most r*s<m. Merely bounding the rank of each
individual slice would not justify this step.

Contract the first target leg by z=(z_{i,h}) in K^(n^2). Let a_{p,q}(z)
be the resulting coefficient of source slice (p,q). On the subspace

\[
 V=\{z:a_{p,q}(z)=0\text{ for }(p,q)\notin P_0\times Q_0\},
\]

at most n^2-|P_0||Q_0| linear equations are imposed. Thus dim V is at
least |P_0||Q_0|, without any rank or locality assumption on A.
For z in V, equations (5)-(6) give symbol rank at most r*s for the
contracted mapped source. The contracted target symbol is

\[
                 \left(\sum_{i,h}z_{i,h}X^hY^i\right)I_m.
\]

For z nonzero the displayed scalar is nonzero by monomial independence;
the symbol rank is m. Therefore R(z) cannot vanish for nonzero z in V.
The first flattening of R is injective on V, proving the first bound.
Each exceptional column removes at most m interior p or q indices,
which proves the explicit lower estimate. The sets of matrices of
bounded rank are closed, and a sum of d simple tensors has flattening
rank at most d. This gives the border-rank bound over the algebraic
closure as well. The same injectivity proof works after extending K.
This proves every assertion in (3).

## Consequences and limits

If B coefficients are polynomials in z of degree at most d_B, their
windows belong to the span of 1,v,...,v^d_B over any field. If C
coefficients have degree at most d_C, they have at most d_C+1 profiles.
Thus (d_B+1)(d_C+1)<m suffices. For example, both maps can be genuinely
linear and variable at every source column when m>=5. In positive
characteristic evaluation collisions can only lower these dimensions.

More generally B may obey a common constant-coefficient recurrence of
order r<m on its relevant columns; successive recurrence substitution
gives a common r-dimensional window span. C may use s entirely arbitrary
scalar profiles with independent constant stencil arrays. Only r*s<m
is required. Interchanging B and C gives the mirrored theorem, using
C windows in y and B coefficient profiles in their column index.

The theorem specializes to the one-variable/Toeplitz result with s=1.
It allows both maps to vary, unlike that result. It does not follow
from separate window-rank bounds on the two legs: the fixed coefficient
profiles in (2) are what make H independent of p. Replacing them with
p-dependent basis vectors would invalidate the shared-row-space step.

At r*s=m the rank contradiction is unavailable. An exact width-four
control with two independent linear profiles on each leg has a
full-rank four-by-four contracted source symbol. This is a limit of the
proof method, not a low-repair construction or a counterexample to
some stronger obstruction. Full profile rank, arbitrary Laurent maps,
and general nonlocal bulk maps remain open to this theorem. These
finite controls do not review the all-size proof independently.

## Provenance

The paired source and correction motivation are maintained main
conventions, pinned in sources.json. The common Laurent-symbol and
contraction-kernel method is credited to pending PR173 at
`ce270d3276bd90253d3ba3a1eb5757ff3677ce61` and related PR172 at
`95de5b3a7db04a70ea31230c41d2f15581144882`, following PR157.
This package adds the second-leg profile expansion (2) and the r*s
criterion. Their arguments are reconstructed here; no unmerged package
is required to run this verifier. No external structural theorem,
historical priority, independent review or exponent gain is claimed.
