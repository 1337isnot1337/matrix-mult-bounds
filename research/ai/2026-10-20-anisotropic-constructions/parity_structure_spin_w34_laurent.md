# A coupled Laurent repair and an exact two-channel extension

October 21, 2026. These are exact rational constructions from the original
$A(8,8)$ source. They use the [four-chain spin maps](parity_structure_spin_w34.md)
and the [private-channel extension](spin_channel_extension.md).

The first construction gives $M(3,3,27)$ for **every nonzero parameter**
$t$, with a rank-two coefficient of $t^{-1}$ in the second map. Its
response at the original source coordinate $F(7,0,7)$ vanishes identically.
The second construction attaches eight private entries and has a specified
twelve-term error of degree one, so its constant tensor is obtained by a
degeneration. A restriction and rescaling of that construction gives a
third tensor exactly for every $t\ne0$: $M(3,3,27)$ with a full
$M(3,4,2)$ extension sharing two middle channels. In particular, evaluating
the third family at $t=1$ gives an ordinary rational restriction.

No full square target or smaller matrix multiplication exponent is
established by these constructions.

## 1. Source and target coordinates

All three source legs use the same order

\[
 F(i,k,s)\longleftrightarrow (15i+k)8+s,
 \qquad 0\le i,s<8,\quad 0\le k<15.
\]

The source terms are

\[
 X(i,p+q,s)Y(p,r+s,j)Z(r,i+j,q),
 \qquad i,j,p,q,r,s<8.                         \tag{1}
\]

Begin with the saved $M(3,3,28)$ maps and delete original middle
coordinate zero. The retained original middle coordinates $1,\ldots,27$
are relabelled $\alpha=0,\ldots,26$. The retained target is

\[
 M=\sum_{I,J=0}^2\sum_{\alpha=0}^{26}
 X_{IJ}Y_{J\alpha}Z_{\alpha I}.               \tag{2}
\]

Its row orders are $3I+J$, $27J+\alpha$, and $27I+\alpha$.
Write $Y_R,Z_R$ for the retained maps, and $Y_D,Z_D$ for the three
deleted rows on each corresponding leg. Let $Y_A$ be the three rows at
retained middle coordinate $\alpha=16$, originally coordinate 17.
The first map remains the saved nine-row map throughout this section.

## 2. Two endpoint correction systems

Use the 160-dimensional second-source space

\[
 \mathcal V=\operatorname{span}
 \{F(p,L,j):p<2,\ L<10,\ j<8\}.
\]

There are eight independent vectors in this space that contract to zero
against the saved first map and **all 84** original third-map rows. Put
these vectors in the rows of $F$. The reconstruction script computes
them over $\mathbb Q$ and checks all $756\times8$ constraint coefficients;
it does not infer a rational kernel solely from a modular calculation.

Let $E$ map a vector of $\mathcal V$ to its response against $Z_R$ at
the original first-source coordinate $F(7,0,7)$. The following two
systems have exact rational solutions:

\[
 N_0=Y_D+TF,\qquad EN_0^{\mathsf T}=0,        \tag{3}
\]

\[
 Y_0=Y_R-CF-BY_A,\qquad EY_0^{\mathsf T}=0.  \tag{4}
\]

Here $T$ is $3\times8$, $C$ is $81\times8$, and $B$ is $81\times3$.
The endpoint response of $F$ has dimension four, while the joint
response of $F$ and $Y_A$ has dimension six. The selected solution has
zero third column in $B$. The product $BN_0$ has rank exactly two.
The exported maps include $F,N_0,B$ as auxiliary rational arrays; the
accepted tensor identities below are also checked directly on the
exported maps, independently of the reconstruction procedure.

Let $Z_1$ place the three deleted rows $Z_D$ at retained target channel
16 and put zero in its other rows. Define

\[
 \begin{split}
 X(t)&=X,\\
 Y(t)&=t^{-1}BN_0+Y_0,\\
 Z(t)&=Z_R+tZ_1.
 \end{split}                                                        \tag{5}
\]

These are maps over $\mathbb Q(t)$, with a nonzero simple pole in
$Y(t)$. Their exact exported sizes are:

| Map coefficient | Denominator | Nonzero entries |
|---|---:|---:|
| $X$ | 2 | 16 |
| $[t^{-1}]Y(t)$ | 56 | 1,612 |
| $[t^0]Y(t)$ | 672 | 3,615 |
| $[t^0]Z(t)$ | 24 | 1,266 |
| $[t^1]Z(t)$ | 24 | 50 |

## 3. Exact cancellation, including the pole

The eight rows of $F$ vanish against the first map and all original
third rows. Original middle coordinates zero and 17 are distinct, so
$Y_D$ pairs to zero with $Z_R$, and $Y_A$ pairs to zero with $Z_D$.
It follows that the degree-minus-one and degree-one terms in the
pullback of (1) under (5) vanish.

The constant correction from $BN_0$ paired with $Z_1$ equals the
response of $BY_A$ paired with $Z_R$: both select the same first
matrix entries and the third target rows at channel 16. This cancels
the term subtracted in (4). The $CF$ term vanishes. The resulting
tensor is therefore exactly (2) for every $t\ne0$.

Equations (3) and (4) kill the endpoint response against $Z_R$. On the
second-source space used here, the endpoint response against the
deleted $Z_D$ rows is zero. Thus the full response at $F(7,0,7)$ is
identically zero as a Laurent polynomial. The verifier checks all its
$3\cdot81^2=19,683$ coefficients directly.

At $t=1$, the first response has rank exactly 191. Its source support
is contained in the 192 coordinates with $k=0,1,2$, because the second
map uses $p=0,1$ and the third uses $q=0,1$. The endpoint is absent.
The regenerated $191\times191$ minor has determinant 18,316 modulo
65,521. The coordinate support proves the rational upper bound and
the nonzero minor proves the rational lower bound.

## 4. Eight private entries and a controlled degree-one error

Use the private attachment variables $U_{Iv},V_v$, $I<3$, $v<8$, in
the order of the [saved attachment maps](spin_channel_extension.md).
All 24 added first rows have long coordinate at least three, while
the old second and third rows have $p,q<2$. Every added second row
has $p\ge3$, while the old first rows have long coordinate below
three. These support statements remain valid for every coefficient
of (5), so they exclude all old/new mixed terms that do not belong
to the attachment.

Keep all added first and second maps constant, and replace just the
core maps by (5). The resulting Laurent pullback is exactly

\[
 M+\sum_{v=0}^{7}\sum_{I=0}^{2}U_{Iv}V_vZ_{0I}
 +t\sum_{I=0}^{2}
 \left(U_{I2}V_0+U_{I3}V_1+U_{I6}V_4+U_{I7}V_5\right)Z_{16,I}.
                                                                    \tag{6}
\]

The last term comes from the actual deleted third rows in $Z_1$.
The exact replay determines all twelve coefficients, including their
signs. There are no negative-power terms and no other positive-power
terms. The map format is $(33,89,81)$.

Consequently (6) degenerates to its 267-term constant tensor as
$t\to0$. For a nonzero parameter, it also contains the displayed
twelve-term error. The statement here is a degeneration to the
private-entry target, not an exact realization of that target for
every nonzero parameter.

## 5. Four complete two-channel vertices

In (6), retain only $U_{I2},U_{I3},U_{I6},U_{I7}$ and multiply
$V_0,V_1,V_4,V_5$ by $t^{-1}$. Then the entire pullback is constant:

\[
 M+\sum_{I=0}^{2}\sum_{v\in\{2,3,6,7\}}
 U_{Iv}\bigl(V_vZ_{0I}+V_{v-2}Z_{16,I}\bigr).                       \tag{7}
\]

This is a full $M(3,4,2)$ extension sharing channels 0 and 16 of the
old third leg. Its map format is $(21,89,81)$, with 267 nonzero tensor
coefficients. All coefficients of degrees minus one and plus one are
zero. It is exact for every $t\ne0$, and evaluation at $t=1$ is an
ordinary rational restriction from $A(8,8)$. The ordinary maps are
saved separately and replayed from their actual coefficients.

The two-channel extension supplies eight new second entries for four
new second vertices. A full 27-channel extension would require 108
such entries. Equation (7) does not assert that those missing entries
can be added while retaining the present maps.

## 6. Complete replay and files

All replayers enumerate all 262,144 original source terms. After
clearing map denominators, every coefficient check uses integers.

| Construction | Laurent coefficient slots checked | Nonzero constant coefficients | Nonzero positive coefficients |
|---|---:|---:|---:|
| Core (5) | 177,147 | 243 | 0 |
| Eight-entry composition (6) | 713,691 | 267 | 12 |
| Two-channel composition (7) | 454,167 | 267 | 0 |

The ordinary $t=1$ maps for (7) undergo an additional check of all
151,389 target coefficients. The tests include a tamper that moves
a coefficient between the polar and constant maps while preserving
their value at $t=1$, so evaluation at one parameter cannot substitute
for the Laurent coefficient check.

```bash
python -S research/ai/2026-10-20-anisotropic-constructions/parity_structure_spin_w34_laurent.py
python -S research/ai/2026-10-20-anisotropic-constructions/parity_structure_spin_w34_laurent_extension.py
python -S -m unittest discover -s tests -p test_parity_structure_spin_w34_laurent.py
```

The optional reconstruction script requires NumPy and SymPy. The
accepted replayers and tests require only Python's standard library.
The maps and certificates are:

- [Core Laurent maps](../../../results/anisotropic-constructions-2026-10-20/parity_structure_spin_w34_laurent_maps.json),
  [response minor](../../../results/anisotropic-constructions-2026-10-20/parity_structure_spin_w34_laurent_response_minor.json),
  and [core replay report](../../../results/anisotropic-constructions-2026-10-20/parity_structure_spin_w34_laurent_certificate.json).
- [Eight-entry Laurent maps](../../../results/anisotropic-constructions-2026-10-20/parity_structure_spin_w34_laurent_extension_maps.json).
- [Two-channel Laurent maps](../../../results/anisotropic-constructions-2026-10-20/parity_structure_spin_w34_two_channel_maps.json)
  and [ordinary maps at one](../../../results/anisotropic-constructions-2026-10-20/parity_structure_spin_w34_two_channel_t1_maps.json).
- [Composition replay report](../../../results/anisotropic-constructions-2026-10-20/parity_structure_spin_w34_laurent_extension_certificate.json).

These are finite exact constructions, not a new exponent certificate.
No external independent review or formalization is claimed.
