# A changed first core with twelve exact matrix channels

Research construction, October 21, 2026. There is an explicit rational
ordinary restriction

\[
A(8,8)\longrightarrow M(4,4,12).
\tag{1}
\]

Its first map differs from the canonical crossed-module core. The full
response of its other two maps has rank **186**, while the four-factor
flattening with its first map fixed has rank **481**. Consequently this
particular core passes two necessary tests for extending it toward the
current larger target. No such extension, and no smaller matrix
multiplication exponent, is established here.

## 1. The actual maps

Use common coordinates $F(i,k,s)$ on each source leg, numbered
$(15i+k)8+s$, where $0\le i,s<8$ and $0\le k<15$. The source coefficients
are one at

\[
X(i,p+q,s)Y(p,r+s,j)Z(r,i+j,q).
\tag{2}
\]

Let $Y^0,Z^0$ be the rational eleven-channel maps in
`crossed-module11-witness.json`. Their complete reduced identity is

\[
\sum_{a=0}^{3}\sum_{j=0}^{7}
Y^0_{u'\alpha,(a+u,j)}Z^0_{i'\beta,(a,j+i)}
=\delta_{u'u}\delta_{i'i}\delta_{\alpha\beta},
\tag{3}
\]

for binary $i,u,i',u'$ and $0\le\alpha,\beta<11$.
Index the two four-dimensional vertices by
$I=2i+t$ and $J=2p+u$, with binary labels. For the first eleven channels,
put the coefficients of $Y^0,Z^0$ at

\[
\begin{aligned}
Y^0_{u\alpha,(L,j)}&:
 E_{J,\alpha}\mapsto F(2p,2L,j),\\
Z^0_{i\alpha,(a,H)}&:
 E_{\alpha,I}\mapsto F(2a,H,t).
\end{aligned}
\tag{4}
\]

This retains just the even copy of the matched construction. Add a
twelfth channel, denoted $*$, by

\[
E_{J,*}\mapsto F(7,7+J,7),\qquad
E_{*,I}\mapsto F(7,7+I,7).
\tag{5}
\]

Finally, change the first map to

\[
E_{I,J}\mapsto F(i,2p+t,2u)+F(I,14,J).
\tag{6}
\]

The maps have shapes $16\times960$, $48\times960$, and $48\times960$.
They have respectively 32, 1,226, and 438 nonzero entries. The common
denominators are $1,2860,8$.

For two old channels, the first long-coordinate equation identifies
the binary labels $p,t$, and the remaining equations reduce to (3).
The added first coordinate in (6) has long index 14, whereas two old
maps can only produce long indices 0 through 3.

For two new channel maps, (2) forces $p=q=r=j=7$ and then forces the
first short coordinates to be precisely $I,J$. Thus the added term in
(6) gives the required coefficient one. Every old first term has long
index at most 3 and contributes zero here.

An old $Y$ and new $Z$ can only produce first long index 7 or 9. A new
$Y$ and old $Z$ can only produce index 7 or 8. Neither possibility
appears in (6). This checks every mixed coefficient, so (1) follows.

## 2. Full response of the two non-first maps

Let $\Psi$ contract the full 960-dimensional first source space against
the actual $Y,Z$ maps in (4)--(5). No first-map restriction is imposed
when computing this response.

The support of $\Psi$ has the following description. Each listed entry
is a possible nonzero coordinate $F(i,k,s)$.

| Pair of map types | First-coordinate support |
|---|---|
| Old $Y$, old $Z$ | $k\in\{0,1,2,3\}$, $0\le i<8$, $s\in\{0,2,4,6\}$ |
| Old $Y$, new $Z$ | $k\in\{7,9\}$, $0\le i<8$, $s=1$ |
| New $Y$, old $Z$ | $k\in\{7,8\}$, $i\in\{0,1\}$, $1\le s\le7$ |
| New $Y$, new $Z$ | $k=14$, $0\le i,s<4$ |

For example, the old/new equation for the second long coordinate is
$2L=7+s$. Since $L\le4$, it forces $s=1$. In the opposite mixed case,
the third long coordinate satisfies $H=i+7$, with $H\le8$, so
$i\in\{0,1\}$. The second equation gives $s=7+J-2a\ge1$.

The only overlap between the two mixed support descriptions occurs
at $k=7$, $i\in\{0,1\}$, $s=1$. The counts by long coordinate are

\[
(32,32,32,32)\quad\text{at }k=0,1,2,3;
\qquad20,14,8,16\quad\text{at }k=7,8,9,14.
\]

Their sum is 186. This proves $\operatorname{rank}\Psi\le186$ over
$\mathbb Q$. Rebuilding all actual response coefficients and eliminating
over the prime field of order 65521 gives rank 186. All denominators
are invertible in that field, so this proves the matching rational
lower bound:

\[
\operatorname{rank}\Psi=186,\qquad\dim\ker\Psi=774.
\tag{7}
\]

For an ordinary extension retaining these two maps, all first-leg
units outside the sixteen units of the rectangular core must lie in
$\ker\Psi$. Hence a concise equal-leg target of dimension $D$ must
satisfy $D-16\le774$, or $D\le790$. The dimension
$27^2+7^2=778$ satisfies this necessary inequality. Satisfying it does
not supply the other maps or their multiplication identities.

## 3. The first-map change removes the previous fixed-core ceiling

Fix the actual first map (6), leave the other source legs unrestricted,
and flatten by grouping $(I,Y)$ against $(J,Z)$. Its two summands have
disjoint row and column supports. The canonical summand uses first
short coordinate $p<4$ on $Y$ and last short coordinate $q<4$ on $Z$.
The corner summand has $p=q=7$.

The canonical summand has rank 360, as verified in the full-source
control of `parity_balancing_crossed_flattening.py`. The corner summand
has coefficients

\[
Y(7,r+J,j)Z(r,I+j,7),\qquad
0\le I,J<4,\quad0\le r,j<8.
\tag{8}
\]

Its flattening is the tensor product of the two convolution matrices
with coefficient conditions $L=r+J$ and $H=I+j$. Each matrix has rank
11: its eleven nonzero output rows have disjoint supports. The corner
rank is therefore $11^2=121$, and the complete rank is

\[
360+121=481.
\tag{9}
\]

The replay also checks (9) directly from all original source terms,
without trusting either stored rank. The actual flattening has 1,472
nonzero rows and 481 distinct nonzero indicator rows. The supports of
different row patterns are pairwise disjoint, which proves the rank
exactly over $\mathbb Q$.

The corresponding flattening of $M(4,4,r)$ has rank $16r$. Thus this
fixed first map only gives the necessary upper bound $r\le30$.
In particular $16\cdot27=432<481$. This is a change in the exact
first map, rather than a basis change within the old sixteen source
directions.

## 4. Complete replay and scope

The compact JSON file stores the three actual maps. The verifier reads
those entries, enumerates all $8^6=262,144$ original source terms,
and checks every one of the $16\cdot48^2=36,864$ target coefficients.
Exactly 192 coefficients equal one and all others equal zero. It also
rebuilds the full first response and the first-core flattening. The
tests replace a nonzero map coefficient by a different nonzero value
and require rejection.

```bash
python -S research/ai/2026-10-20-anisotropic-constructions/parity_structure_cross_module_corner.py
python -S -m unittest discover -s tests -p test_parity_structure_cross_module_corner.py
```

The verifier uses only the standard library. Generation additionally
reads the already stored eleven-channel rational witness; it does not
require a numerical optimizer. The construction is a twelve-channel
rectangular core that passes two specified necessary assembly tests.
The full $M_{27}\oplus M_7$ target remains unconstructed.
