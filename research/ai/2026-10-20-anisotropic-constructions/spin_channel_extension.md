# An exact eight-entry extension on a private middle channel

October 21, 2026. This note gives an actual rational extension of the
[four-chain spin core](parity_structure_spin_w34.md). It attaches eight
new second-leg entries and their 24 first-leg entries, all using one
retained middle channel. The complete source coefficient identity is
verified. The additional first response has rank exactly 24, so it
introduces no response directions beyond the 24 supplied first entries.

This is a partial matrix tensor. Each new second vertex still lacks 26
of its 27 required middle-channel entries. A full square target and a
smaller matrix multiplication exponent are not established.

## 1. The tensor that is constructed

Delete original middle coordinate zero from the saved
$A(8,8)\to M(3,3,28)$ maps. Relabel the remaining original coordinates
$1,\ldots,27$ as $0,\ldots,26$. The retained tensor is

\[
 \sum_{I,J=0}^{2}\sum_{\alpha=0}^{26}
 X_{IJ}Y_{J\alpha}Z_{\alpha I}.
 \tag{1}
\]

The construction adds variables $U_{Iv}$ and $V_v$, with $I<3$ and
$v<8$, and realizes exactly

\[
 \sum_{I,J=0}^{2}\sum_{\alpha=0}^{26}
 X_{IJ}Y_{J\alpha}Z_{\alpha I}
 +\sum_{v=0}^{7}\sum_{I=0}^{2} U_{Iv}V_vZ_{0I}.
 \tag{2}
\]

Thus the new component is a copy of $M(3,8,1)$ sharing its third leg
with the three variables $Z_{0I}$ of the original core. It is not a
direct sum. Its three leg dimensions are $(33,89,81)$.

## 2. The private boundary coefficients

Use source coordinates $F(i,k,s)$, where $i,s<8$ and $k<15$. The source
terms are

\[
 X(i,p+q,s)Y(p,r+s,j)Z(r,i+j,q).
 \tag{3}
\]

The saved third map uses only $q=0,1$. On the part of its support with
$r=0$ and $H\ge5$, all retained middle coordinates except the newly
labelled coordinate zero vanish. For that coordinate, the only
nonzero coefficients are

| Third target entry | Source coordinate | Coefficient |
|---|---|---:|
| $Z_{00}$ | $F(0,7,1)$ | $1$ |
| $Z_{01}$ | $F(0,7,0)$ | $1/2$ |
| $Z_{01}$ | $F(0,8,1)$ | $-1/2$ |
| $Z_{02}$ | $F(0,8,0)$ | $1$ |

These statements concern only the specified boundary part of the
third rows. The rows also have coefficients elsewhere. They follow
directly from the actual exported rational map; the full replay below
does not assume them in place of checking source coefficients.

For a new second vector $F(p,0,j)$ with $j=5$ or $7$, equation (3)
forces $r=s=0$. Put $a=7-j$ and $b=8-j$. Its response is therefore

\[
 X(a,p+1,0)Z_{00}
 +\frac{X(a,p,0)-X(b,p+1,0)}2Z_{01}
 +X(b,p,0)Z_{02}.
 \tag{4}
\]

In particular no other retained middle coordinate occurs.

## 3. Four disjoint six-dimensional cells

For each pair

\[
 (t,j)\in\{3,6\}\times\{5,7\},
\]

adjoin the second vectors

\[
 V_0\longmapsto F(t,0,j),\qquad
 V_1\longmapsto F(t+1,0,j).
\]

Within that cell, let $a=7-j$, $b=8-j$, and use these first maps:

| First entry | Source image |
|---|---|
| $U_{0,0}$ | $F(a,t+1,0)+F(b,t+2,0)$ |
| $U_{1,0}$ | $2F(a,t,0)$ |
| $U_{2,0}$ | $F(b,t,0)$ |
| $U_{0,1}$ | $F(a,t+2,0)$ |
| $U_{1,1}$ | $-2F(b,t+2,0)$ |
| $U_{2,1}$ | $F(b,t+1,0)+F(a,t,0)$ |

Substitution in (4) gives exactly

\[
 \sum_{I=0}^2\sum_{v=0}^1 U_{Iv}V_vZ_{0I}.
\]

The first images form a basis of the six coordinate directions
$\{F(a,k,0),F(b,k,0):t\le k\le t+2\}$. The four cells have disjoint
sets of these directions: the first short indices are either
$\{0,1\}$ or $\{2,3\}$, and the long indices are either
$\{3,4,5\}$ or $\{6,7,8\}$. Equation (4) also shows that their mixed
coefficients vanish.

All 24 new first images have long coordinate at least three. The
retained second and third maps use $p,q<2$, so their response on these
new first vectors is zero. Conversely, the old first images use long
coordinates below three, whereas every new second vector has
$p\ge3$. Their mixed coefficients are zero as well. This proves (2).

## 4. Exact response accounting

The retained second and third maps have first response rank 192 on
exactly the coordinates $F(i,k,s)$ with $k<3$. The supplied minor
checks this after the middle-coordinate deletion, rather than
inferring it from the 28-channel map.

The new second rows respond only on

\[
 E=\operatorname{span}\{F(i,k,0):i<4,\ 3\le k\le8\},
 \qquad\dim E=24.
\]

Their response is injective on $E$, because the 24 first images above
form a basis of $E$ and have 24 independent matrix-entry responses in
(2). The old response vanishes on $E$, and the added response vanishes
on the old 192 source coordinates. Consequently the full response
rank is exactly $192+24=216$.

The first response span of the constructed tensor has dimension 33.
Its entire preimage in the 960-dimensional source first leg therefore
has dimension

\[
 960-216+33=777.
\]

The construction preserves the first-image capacity of the retained
core while adding these actual entries. It does not by itself remove
the fixed-map dimension barrier for a target with common leg
dimension 778. Nor does it complete the remaining channels of the
774-dimensional alternative.

## 5. Complete replay

The standard-library verifier enumerates all 262,144 source terms and
checks all 237,897 target coefficients. Exactly 267 are nonzero: 243
from the retained core and 24 from the attachment. It rebuilds the
192-dimensional retained response minor, checks the complete response
support, and rereads the exported maps.

```bash
python -S research/ai/2026-10-20-anisotropic-constructions/spin_channel_extension.py
python -S -m unittest discover -s tests -p test_spin_channel_extension.py
```

The actual maps are in
[spin-channel-extension-maps.json](../../../results/anisotropic-constructions-2026-10-20/spin-channel-extension-maps.json),
the retained-response minor is in
[spin-channel-extension-core-minor.json](../../../results/anisotropic-constructions-2026-10-20/spin-channel-extension-core-minor.json),
and the replay report is in
[spin-channel-extension-certificate.json](../../../results/anisotropic-constructions-2026-10-20/spin-channel-extension-certificate.json).

The discovery used a finite-field affine recurrence to locate a private
channel. The accepted construction consists of the rational maps and
complete integer coefficient replay above. The proof and a separate
replay of the saved maps were checked by a second agent in this
generating session. No external independent review or formalization is
claimed.
