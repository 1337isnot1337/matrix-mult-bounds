# Low channel rank survives auxiliary Laurent cancellation

October 23, 2026. Owner-directed OpenAI Codex work. Claims
`AI-LAURENT-CHANNEL-SEPARATION-001` and
`AI-LAURENT-PAIRED-REPAIR-002` are written and unreviewed.
There is no improved matrix multiplication exponent.

## Result and its relation to the ordinary obstructions

The ordinary arguments in PR157, PR173 and PR179 leave open whether poles
in the paired-source maps and an auxiliary tensor can cancel and evade
their channel-rank obstruction. The lemma below closes that escape under
the same low channel-rank hypothesis over the **entire Laurent field**.
The first map and the auxiliary maps are arbitrary. Pole orders are
unrestricted. The two source contributions need not have separate limits.

The key step is to take a common kernel over the Laurent field before
specializing. It is not valid to specialize the raw constant coefficient
of a matrix that still has poles.

For the paired source, the result applies to near-full rectangular target
legs as well as the full target. At fixed source and target middle widths,
sublinear filter bandwidth and exceptional-column counts force an
auxiliary border-rank cost of at least `n^2-o(n^2)`. This includes filters
and common channel bases that move with the Laurent parameter. A family
whose generic channel rank reaches the target width is outside the result.

## 1. The formal channel-separation lemma

Let K be a field, O=K[[t]] and L=K((t)). Fix target spaces with basis

    a_(i,j), b_(j,alpha), c_(beta,i),
    0<=i<l, 0<=j<r, 0<=alpha,beta<h,

where h>=2. The target is

\[
 M(l,h,r)=\sum_{i,j,\alpha}a_{i,j}b_{j,\alpha}c_{\alpha,i}.
\]

The first target space has dimension D=l*r. Encode a contraction on its
first leg as an h-by-h matrix of polynomials. A coefficient at
`b_(j,alpha)c_(beta,i)` contributes `X^j Y^i` in entry `(alpha,beta)`.
Call this K-linear encoding Psi. For a first covector w it gives

\[
 \Psi(M(w))=L_w(X,Y)I_h,\qquad
 L_w=\sum_{i,j}w_{i,j}X^jY^i.                         \tag{1}
\]

Distinct monomials show that L_w is nonzero whenever w is nonzero.

Suppose S(t) and E(t) are tensors over L in the target format and

\[
 S(t)+E(t)=M(l,h,r)+O(t).                             \tag{2}
\]

Equation (2) means coefficientwise regularity and equality of the
constant coefficient, including every off-target coefficient. Neither
S nor E is assumed regular separately. Suppose V is an L-linear
subspace of first covectors, of dimension d, with

\[
 \operatorname{rank}_{L(X,Y)}\Psi(S(t)(w))<h
       \quad\hbox{for every }w\in V.                \tag{3}
\]

**Lemma.** The first flattening of E(t) has rank at least d over L.

### Proof

Assume that its rank k is smaller than d. Rank-nullity gives

\[
 \dim_L\bigl(V\cap\ker(E(t):A^*\to B\otimes C)\bigr)
       \ge d-k>0.
\]

Choose a nonzero vector w(t) in this intersection. Its finitely many
coordinates are Laurent series. Multiply the vector by the inverse of
their smallest power of t. It then belongs to O^D and has a nonzero
constant vector w_0. This multiplication keeps it in both L-linear
subspaces. No claim is needed about the specialization of V itself.

Since E(t)(w(t))=0 exactly, (2) gives

\[
 S(t)(w(t))=(S(t)+E(t))(w(t))=M(w_0)+O(t).             \tag{4}
\]

This particular source contraction is therefore regular, even if the
source tensor has poles on other covectors. By (3), the determinant of
its h-by-h channel matrix is zero over L(X,Y). Its entries in (4) are
polynomials in X,Y with coefficients in O. Taking their constant t
coefficients is now legitimate and gives

\[
 0=\det\Psi(M(w_0))=L_{w_0}(X,Y)^h.
\]

The polynomial ring K[X,Y] is an integral domain. Thus L_(w_0)=0,
contradicting w_0 nonzero and monomial independence in (1). This proves
the lemma over every field. The same proof uses all suitable minors if
a smaller explicit channel-rank cap is desired. QED.

### Auxiliary tensors and border rank

If E(t) is the image of a fixed auxiliary tensor R under three Laurent
linear maps, its first flattening rank is no greater than that of R.
The lemma therefore proves

\[
 \operatorname{rank}(R_{A\mid BC})\ge d,
 \qquad \underline{R}(R)\ge d.                       \tag{5}
\]

The second inequality uses the elementary flattening lower bound for
border rank: all (k+1)-minors vanish on rank-k tensors and on their
algebraic closure. No additivity of tensor rank or border rank is used.
Arbitrary separate maps on a direct sum split into its two tensor
contributions, so (5) applies to degenerations from Q direct_sum R.
The statement is formal over K; over C it applies to complex formal
degenerations and the usual algebraic border rank. A ramified parameter
can be renamed t without changing the argument.

### Why a raw constant coefficient is insufficient

The Laurent matrix

\[
 \begin{pmatrix}t^{-1}&1\\1&t\end{pmatrix}
 =\begin{pmatrix}t^{-1}\\1\end{pmatrix}(1\quad t)
\]

has rank one over L. Its raw coefficient at t^0 is
`[[0,1],[1,0]]`, which has rank two over every field. The proof above
does not make this invalid specialization: equation (4) first removes
all poles by choosing an exact auxiliary-kernel vector.

## 2. Paired source and exact good-index count

Fix source width m>=1 and outer source size n. Use

\[
 Q_{n,m}=\sum_{p,q=0}^{n-1}\sum_{y,v=0}^{m-1}
       A_{p,q}B_{y,q+v}C_{p+y,v}.                    \tag{6}
\]

Let 1<=l,r<=n and let the target middle width be h>=2. The first map
from the n^2 source coordinates to the l*r target coordinates is
arbitrary over L. On the two long legs, fix bandwidth D>=0 and
exceptional source-column sets E_B,E_C, of sizes e_B,e_C. These sets
are fixed for the entire formal family at the chosen n. On other
columns use

\[
 B_{y,s}\mapsto\sum_{\alpha=0}^{h-1}\sum_{k=-D}^D
     \beta_{y,\alpha,k}(s,t)b_{s-k,\alpha},           \tag{7}
\]

\[
 C_{z,v}\mapsto\sum_{\beta=0}^{h-1}\sum_{u=-D}^D
     \gamma_{v,\beta,u}(z,t)c_{\beta,z-u}.            \tag{8}
\]

All coefficients lie in L. Omit target outer indices outside their
respective ranges. Maps on exceptional columns are completely arbitrary
over L and may be nonlocal.

The safe source intervals are

\[
 I_B=\{D,\ldots,r-m-D\},\qquad
 I_C=\{D,\ldots,l-m-D\},
\]

with an empty set when its upper endpoint is below D. They lie inside
`{0,...,n-1}` because l,r<=n. Set

\[
 Q_0=\{q\in I_B:q+v\notin E_B\ (0\le v<m)\},
\]

\[
 P_0=\{p\in I_C:p+y\notin E_C\ (0\le y<m)\}.
\]

Every corresponding source term uses the rules (7)-(8), and all its
shifted target coordinates are present. Each exceptional column removes
at most m source indices. Consequently

\[
 |Q_0|\ge g_B=(r-m+1-2D-me_B)_+,\qquad
 |P_0|\ge g_C=(l-m+1-2D-me_C)_+.                    \tag{9}
\]

This one-sided safe interval is slightly larger than the symmetric
interior used in the earlier ordinary proofs. No source coordinate or
boundary term is dropped unless its first-map coefficient is explicitly
killed below.

## 3. A common factor for two moving variable-coefficient maps

Assume the m-entry windows

\[
 (\beta_{y,\alpha,k}(q,t),\ldots,
   \beta_{y,\alpha,k}(q+m-1,t)),
 \quad q\in Q_0,
\]

span one common subspace of L^m of dimension at most a. Let
`phi_1,...,phi_a` be a basis. Thus, for all the displayed indices,

\[
 \beta_{y,\alpha,k}(q+v,t)
 =\sum_{j=1}^a H_{q,y,\alpha,k,j}(t)\phi_j(v,t).      \tag{10}
\]

Assume also that the C coefficients have a common expansion in b
column profiles:

\[
 \gamma_{v,\beta,u}(z,t)
   =\sum_{s=1}^b\psi_s(z,t)\Gamma_{s,v,\beta,u}(t),   \tag{11}
\]

at every good column used above. The profiles may vary with z,n,t.
The coefficients Gamma are independent of z. All bases and profiles
are allowed to move with t. The substantive requirement is

\[
                         a b<h.                    \tag{12}
\]

A Toeplitz B map has a<=1. A Toeplitz C map has b<=1. One moving
variable map with proper common window span and one Toeplitz map is
therefore included. So is the two-variable profile class of PR179.
These ranks must be bounded over L, not merely after setting t=0.

For a good source coordinate (p,q), direct substitution into (6)
gives its channel matrix as

\[
 X^qY^p\sum_{j=1}^a\sum_{s=1}^b
       F_{p,q,j,s}(X,Y,t)G_{j,s}(X,Y,t)^T,            \tag{13}
\]

where the components of these h-vectors are

\[
 F_{p,q,j,s,\alpha}
 =\sum_{y,k}H_{q,y,\alpha,k,j}(t)
                 \psi_s(p+y,t)X^{-k}Y^y,
\]

\[
 G_{j,s,\beta}
 =\sum_{v,u}\phi_j(v,t)\Gamma_{s,v,\beta,u}(t)
                 X^vY^{-u}.                         \tag{14}
\]

The right vectors G are independent of p,q. Hence every linear
combination of good source slices has rank at most a*b over L(X,Y).
The word common in the hypotheses is necessary; individually low-rank
source slices with unrelated factors do not imply this conclusion.

## 4. Formal repair theorem, including near-full outer dimensions

Suppose separate Laurent maps give

\[
 Q_{n,m}\oplus R\ \unrhd\ M(l,h,r)
\]

with (7)-(12) on the Q part of the long maps. Every first-leg map
and every auxiliary map is arbitrary. If the resulting tensor is
M+O(t), then

\[
 \boxed{\operatorname{rank}(R_{A\mid BC}),\ \underline R(R)
 \ \ge\ \bigl(lr-n^2+|P_0||Q_0|\bigr)_+
 \ \ge\ \bigl(lr-n^2+g_Bg_C\bigr)_+.}             \tag{15}
\]

To prove this, contract the target first leg by w and write f_(p,q)(w)
for its induced source coefficient. Impose f_(p,q)(w)=0 on every
source coordinate outside P_0 x Q_0. These are at most
`n^2-|P_0||Q_0|` homogeneous equations on lr variables over L. Their
kernel V therefore has dimension at least
`lr-n^2+|P_0||Q_0|`, or zero if that number is negative. Equations
(13)-(14) give rank less than h on V. Apply the lemma and (5).

At fixed m,h and l=n-c_1, r=n-c_2 for fixed nonnegative c_1,c_2,
if D=o(n) and e_B+e_C=o(n), the last expression in (15) is

\[
                              n^2-o(n^2).            \tag{16}
\]

The same conclusion holds for l/n and r/n tending to one. Thus this
formal map class cannot meet a subquadratic auxiliary border-rank
budget, including the maintained O(n), O(n^(4/3)), or o(n^(3/2))
sufficient construction premises. Increasing a pole order does not
evade (15). Making the generic common channel rank reach h, losing the
common factorization, or using a macroscopic exceptional region remains
outside it. The mirrored statement follows by exchanging the long legs.

## 5. Evidence and remaining construction problem

The proof is the all-size argument. `verify.py` separately expands the
literal source (6), compares the full good-slice Laurent coefficients
with (13), checks exact finite residual flattening ranks, and retains
all pole coefficients. Its controls also demonstrate why a raw constant
coefficient can increase rank, and why a low rank only at t=0 is not
the hypothesis. The finite controls do not prove the general lemma.

No construction is supplied. Full generic window rank and nonlocal maps
remain candidates, and can be tested without assuming this theorem
excludes them. The next constructive task is an explicit periodic or
nonlocal encoding whose channel matrix has full generic rank and whose
complete residual can be repaired within the stated asymptotic budget.

## Attribution

PR157 at `9e830aa7af430b74febc93aeb8a975b1e356d744` supplies the ordinary
two-Toeplitz channel-rank argument. PR173 at
`ce270d3276bd90253d3ba3a1eb5757ff3677ce61` supplies the common window
expansion on one variable leg. PR179 at
`f74aa2d5141411e314568040de3670cc8ff7a6de` supplies the second profile
expansion for ordinary maps. Their exact URLs and source hashes are in
`sources.json`. They remain unmerged concurrent work at this snapshot;
none is imported by the verifier or presented as independently reviewed.

The maintained Q convention and correction criterion retain their own
credits. The contribution here is the primitive auxiliary-kernel lemma,
its all-order Laurent application, and the near-full dimension count.
Every algebraic fact used by the new lemma is proved above. There is no
new external theorem dependency, priority claim, external mathematical
review or proof-assistant formalization.
