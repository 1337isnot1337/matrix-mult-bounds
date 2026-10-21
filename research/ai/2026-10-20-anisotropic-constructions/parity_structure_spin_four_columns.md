# Four complete new vertices: an exact M(3,7,27) restriction

October 21, 2026. This construction extends the
[four-chain spin core](parity_structure_spin_w34.md) by four second
vertices, with all 27 middle-channel entries for each new vertex. It
gives an ordinary rational restriction

\[
 A(8,8)\longrightarrow M(3,7,27).                                  \tag{1}
\]

The full original-source coefficient identity is verified. The full
response of the saved second and third maps has rank exactly 576.
This response cost is too large to keep these particular maps in
the current square-target assembly: the entire permitted first-map
space has dimension 405. The construction is an exact channel
completion, with this stated limitation; it does not establish a
smaller matrix multiplication exponent.

## 1. Coordinate convention and retained core

Every source leg uses $F(i,k,s)$ in column $(15i+k)8+s$. Source terms
are

\[
 X(i,p+q,s)Y(p,r+s,j)Z(r,i+j,q),\qquad i,j,p,q,r,s<8.                \tag{2}
\]

Start with the saved $M(3,3,28)$ maps, delete original middle channel
zero, and relabel the remaining channels $0,\ldots,26$. Keep the
nine old first maps, the 81 retained second maps, and the 81 retained
third maps. This gives the usual $M(3,3,27)$ core. No Laurent repair
is used in (1).

For the full target (1), use $I<3$, $J<7$, $\alpha<27$, with row
orders $7I+J$, $27J+\alpha$, and $27I+\alpha$. The old first rows
are reindexed from $3I+J$ to $7I+J$, for $J<3$.

## 2. Twenty-seven separate third-map channels

The retained third maps have long coordinate $H\le8$ and last short
coordinate $q=0,1$. At each of the following three endpoint positions,
their restriction has exactly the displayed spin form:

| Retained channel $\alpha$ | First short coordinate $r$ | Long pair |
|---|---:|---|
| 0 | 0 | 7, 8 |
| 14 | 1 | 7, 8 |
| 5 | 2 | 7, 8 |

For a channel assigned to $(r,H)$, the form is

\[
 Z_{\alpha0}\mapsto F(r,H,1),\qquad
 Z_{\alpha1}\mapsto\frac{F(r,H,0)-F(r,H+1,1)}2,\qquad
 Z_{\alpha2}\mapsto F(r,H+1,0).                                    \tag{3}
\]

The table describes only those endpoint coordinates of the retained
maps. Their other coefficients remain in the construction.

For the other 24 channels, enumerate $\alpha\notin\{0,5,14\}$ in
increasing order. Write its enumeration index as $3r+b$, with
$0\le r<8$ and $0\le b<3$. Add the form (3) at

\[
 H=9+2b.                                                          \tag{4}
\]

These 24 added pairs have disjoint source coordinates, and all have
$H\ge9$. The old first maps use $i=0,1$; every old second map uses
$j<8$. Hence the old first and second maps only see $i+j\le8$ in
the third leg. Adding (4) preserves the complete old core exactly.

Assign each of the 27 channels a pair $(L_\alpha,j_\alpha)$ by

\[
 (L_0,j_0)=(0,1),\quad(L_{14},j_{14})=(1,1),\quad
 (L_5,j_5)=(2,1),                                                  \tag{5}
\]

and, for the enumeration in (4),

\[
 (L_\alpha,j_\alpha)=(r,3+2b).                                   \tag{6}
\]

Thus $H=6+j_\alpha$ in every case. The assignments are also saved in
the map JSON. They are used to construct maps, not as a substitute for
the complete coefficient replay.

## 3. Two six-dimensional first-map cells

For each $t\in\{3,6\}$ introduce two new second vertices, with
$p=t$ and $p=t+1$. For every middle channel set

\[
 Y_{J\alpha}\mapsto F(p,L_\alpha,j_\alpha).                       \tag{7}
\]

For these vertices use first maps with short coordinates $i=6,7$
and $s=0$. Equation (2) then forces $r=L_\alpha$ and
$H\in\{6+j_\alpha,7+j_\alpha\}$. By (3)--(6), exactly the
intended middle channel appears. For fixed $p$, the response is

\[
 F(6,p+1,0)Z_{\alpha0}
 +\frac{F(6,p,0)-F(7,p+1,0)}2Z_{\alpha1}
 +F(7,p,0)Z_{\alpha2}.                                            \tag{8}
\]

The following six first vectors make (8) the exact matrix-unit pairing
for both vertices at once:

| First entry within one cell | Source image |
|---|---|
| $U_{0,0}$ | $F(6,t+1,0)+F(7,t+2,0)$ |
| $U_{1,0}$ | $2F(6,t,0)$ |
| $U_{2,0}$ | $F(7,t,0)$ |
| $U_{0,1}$ | $F(6,t+2,0)$ |
| $U_{1,1}$ | $-2F(7,t+2,0)$ |
| $U_{2,1}$ | $F(7,t+1,0)+F(6,t,0)$ |

For $t=3$ these become target vertices $J=3,4$; for $t=6$ they become
$J=5,6$. They form bases of two disjoint six-dimensional coordinate
spaces, with long-coordinate bands $3,4,5$ and $6,7,8$ respectively.
The complete contribution is

\[
 \sum_{I=0}^{2}\sum_{J=3}^{6}\sum_{\alpha=0}^{26}
 X_{IJ}Y_{J\alpha}Z_{\alpha I}.                                   \tag{9}
\]

There are no remaining old/new mixed coefficients. The old first
maps have $k\le2$, while the new second maps have $p\ge3$, so their
contraction is zero. The new first maps have $k\ge3$, while the old
second and all third maps have $p,q<2$, so that contraction is zero
as well. The two new cells have disjoint long bands, and (8) checks
the two vertices inside each cell. Combining (9) with the old core
proves (1).

## 4. Exact full response cost

Let $R$ be the contraction of the full 960-dimensional first source
leg with the saved 189 second and 81 third rows. This uses every first
source direction, not merely the 21 selected first maps.

The support of $R$ is exactly

\[
 \{F(i,k,s):i,s<8,\ 0\le k\le8\},
\]

which has 576 coordinates. The response decomposes into three blocks
with disjoint source supports and disjoint output supports:

| Source long band | Second target rows | Source dimensions | Certified rank |
|---|---|---:|---:|
| 0, 1, 2 | 0 through 80 | 192 | 192 |
| 3, 4, 5 | 81 through 134 | 192 | 192 |
| 6, 7, 8 | 135 through 188 | 192 | 192 |

The complete response is rebuilt from the actual rational maps.
The supplied three minors, each of size 192, have determinants
12,738, 45,481, and 45,481 modulo 65,521. These are rational lower
bounds. The exact coordinate supports give the corresponding upper
bounds. Therefore

\[
 \operatorname{rank}R=576.                                        \tag{10}
\]

The response of the constructed first target has dimension 21.
Its full preimage in the source first leg consequently has dimension

\[
 960-576+21=405.                                                   \tag{11}
\]

Any ordinary extension retaining these second and third maps as the
corresponding subarray of a larger matrix target must send its entire
first image into that preimage. This remains true if the old first
maps are allowed to change. Thus such a target's first dimension
cannot exceed 405. In particular, fixed-map targets of dimensions
774 or 778 are excluded here. This is a statement about the saved
second and third maps; it does not exclude constructions that move
them, or arbitrary degenerations of the source.

The useful construction in (1) fills every middle channel. Its
limitation in (10) identifies the next requirement: new vertices
must share substantially more response directions with the retained
core than these disjoint long bands do.

## 5. Reproduction and accepted scope

The saved maps have dimensions $(21,960)$, $(189,960)$, $(81,960)$,
denominators $2,48,24$, and respectively 32, 3,854, and 1,362 nonzero
entries. The standard-library verifier enumerates all 262,144 source
terms and checks all 321,489 target coefficients. Exactly 567 target
coefficients are one, as required for $M(3,7,27)$; all others are zero.
It also regenerates all three response minors and verifies their
disjoint supports.

```bash
python -S research/ai/2026-10-20-anisotropic-constructions/parity_structure_spin_four_columns.py
python -S -m unittest discover -s tests -p test_parity_structure_spin_four_columns.py
```

Passing `--write-maps` to the script reconstructs the maps from the
frozen W34 seed using only integer arithmetic. The ordinary verifier
reads the actual exported maps and needs no optional dependencies.
The tests reject both a nonzero alteration of an added third-map
coefficient and a false response-minor certificate.

The accepted files are the [maps](../../../results/anisotropic-constructions-2026-10-20/parity_structure_spin_four_columns_maps.json),
[response minors](../../../results/anisotropic-constructions-2026-10-20/parity_structure_spin_four_columns_response_minors.json),
and [replay report](../../../results/anisotropic-constructions-2026-10-20/parity_structure_spin_four_columns_certificate.json).
No external independent review or formalization is claimed.
