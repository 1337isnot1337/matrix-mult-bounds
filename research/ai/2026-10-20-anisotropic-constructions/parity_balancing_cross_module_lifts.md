# Exact full-source lifts of the eleven-channel module

Research calculation, October 21, 2026. The rational crossed-module
witness gives two actual ordinary restrictions:

\[
 A(4,8)\longrightarrow M(4,4,11),
 \qquad
 A(8,8)\longrightarrow M(4,4,22).
 \tag{1}
\]

Every coefficient of these restrictions is replayed using Python
integers. These are rectangular matrix multiplication tensors. They do
not provide $M_{27}\oplus M_7$, and no smaller matrix multiplication
exponent is established.

## 1. Reduced input

The source $R_0$, of format $(4,40,36)$, is the crossed product
$C(2,4)\otimes C(2,8)$. Its 128 coefficients are one at

\[
 (2i+u,\;8(a+u)+j,\;9a+j+i),
 \qquad i,u\in\{0,1\},\quad0\le a<4,\quad0\le j<8.
\]

The rational maps in `crossed-module11-witness.json` have shapes
$22\times40$ and $22\times36$, with common denominators 2860 and 8.
Their exact identity is

\[
 \sum_{a,j}Y_{v\alpha,\,a+u,j}\,Z_{k\beta,\,a,j+i}
 =\delta_{vu}\delta_{ki}\delta_{\alpha\beta}.
 \tag{2}
\]

Here a target row $v\alpha$ means row $11v+\alpha$, and similarly
for $k\beta$. All four $22\times22$ coefficient matrices are checked,
including their zero entries. The separate crossed-module construction
note proves (2) through a rational subspace and kernel construction.
The replay in this package depends only on the actual exported maps.

## 2. A lift that retains the smaller source cost

Use the common coordinate order

\[
 F(i,k,s),\qquad0\le i<a,\quad0\le s<b,\quad0\le k<a+b-1
\]

for the three legs of $A(a,b)$. Its source terms are

\[
 X(i,p+q,s)Y(p,r+s,j)Z(r,i+j,q),
\]

with $i,p,r\in\{0,\ldots,a-1\}$ and
$j,q,s\in\{0,\ldots,b-1\}$.

More generally suppose $Y,Z$ satisfy (2) for any middle dimension
$n$. Index the two four-dimensional target vertices by
$I=(i,t)$ and $J=(p,u)$, with each coordinate binary. Define the
first map by

\[
 E_{I,J}\longmapsto F(i,2p+t,u).
 \tag{3}
\]

For each coefficient $Y_{u\alpha,(L,j)}$, put that coefficient in

\[
 E_{J,\alpha}\longmapsto F(2p,L,j),
 \tag{4}
\]

for both $p=0,1$. For each coefficient
$Z_{i\alpha,(a,H)}$, put that coefficient in

\[
 E_{\alpha,I}\longmapsto F(a,H,t),
 \tag{5}
\]

for both $t=0,1$.

The equality for the first long coordinate is
$2p'+t'=2p+t$. Since both labels are binary, it forces $p'=p$
and $t'=t$. The remaining two long-coordinate equalities are exactly

\[
 L=a+u,\qquad H=j+i.
\]

Thus the complete full-source contraction reduces to (2). In particular,
every desired matrix multiplication coefficient equals one and every
other coefficient equals zero.

The largest first short coordinate is 3 and the largest last short
coordinate is 7. The long coordinates are at most 8. Consequently all
maps (3)--(5) already lie in $A(4,8)$, whose common leg dimension is
$4\cdot8\cdot11=352$. Its three target leg dimensions are
$(16,4n,4n)$. The construction uses different physical frames for the
two four-dimensional vertices; no equality between those frames is
required for this rectangular target.

## 3. Two matched modules inside the larger source

Two copies of $R_0$ may share their four-dimensional first leg while
using disjoint other legs. Combining two copies of (2) gives
$M(2,2,2n)$. This matched sum has an exact $A(8,8)$ lift that avoids
cross coefficients between its copies.

Let $e\in\{0,1\}$ denote the copy. Replace (3)--(5) by

\[
\begin{aligned}
 E_{I,J}&\longmapsto F(i,2p+t,2u),\\
 Y_{u\alpha,(L,j)}&\longmapsto
   \text{the same coefficient on }E_{J,(e,\alpha)}\mapsto F(2p,e+2L,j),\\
 Z_{i\alpha,(a,H)}&\longmapsto
   \text{the same coefficient on }E_{(e,\alpha),I}\mapsto F(e+2a,H,t).
\end{aligned}
\]

The first long-coordinate equality again fixes $p,t$. The second
one reads

\[
 e_Y+2L=e_Z+2a+2u.
\]

It forces $e_Y=e_Z$ by parity and then $L=a+u$. The final equality
is $H=j+i$. This proves the matched-copy lift with every cross-copy
coefficient zero. Every index lies in $A(8,8)$, of common leg
dimension 960.

## 4. Complete stored witness and replay

`parity_balancing_cross_module11_full_maps.json` stores the three actual
rational maps for each restriction in (1), with all sparse entries and
their common denominators. The verifier reads and contracts these
exported maps themselves; it does not accept their stored metadata as
evidence. It also reconstructs the lifts from the reduced witness and
replays those maps separately.

| Source | Target | Source terms checked | All target coefficients checked | Nonzero target terms |
|---|---|---:|---:|---:|
| $R_0$ | $M(2,2,11)$ | 128 | 1,936 | 44 |
| $A(4,8)$ | $M(4,4,11)$ | 32,768 | 30,976 | 176 |
| $A(8,8)$ | $M(4,4,22)$ | 262,144 | 123,904 | 352 |

The full map nonzero counts are $(16,1222,434)$ and
$(16,2444,868)$, respectively. The denominator product is 22,880.
All contractions are therefore checked after clearing denominators,
using integer arithmetic alone. Equality with the concise matrix
multiplication target also proves that all three parameter maps are
injective; no separate rank assertion is taken from metadata.

Run the independent full-source replay with:

```bash
python -S research/ai/2026-10-20-anisotropic-constructions/parity_balancing_cross_module_replay.py \
  results/anisotropic-constructions-2026-10-20/crossed-module11-witness.json
```

The earlier exact nine-channel witness was also checked by this replay.
It yields $A(4,8)\to M(4,4,9)$ and $A(8,8)\to M(4,4,18)$.
Its [complete rational maps](../../../results/anisotropic-constructions-2026-10-20/crossed-module9-control.json)
and full-source replay report are retained as a construction control;
(1) supplies the stronger module.

## 5. Scope and remaining composition problem

The coordinate-module control gave $M(4,4,8)$ from the smaller source
and $M(4,4,16)$ from the matched larger source. Formula (1) increases
the middle dimension using actual mixed rational maps. It is a
construction in a previously unfilled module family.

A full square target would additionally require the other matrix
blocks and every coefficient coupling them. The current first target
space has dimension 16, and its two other spaces have dimensions 44 or
88. These statements must not be conflated with the 778-dimensional
legs of $M_{27}\oplus M_7$. Neither a full square extension nor the
exponent inequality needed for an improvement follows from this witness.

The reduced construction and the full-source lift have been checked
by different agents in this generating session. No external independent
review or formalization is claimed.
