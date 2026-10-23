# Exact map freedoms of the four-chain spin core

October 21, 2026. This note records explicit ways to move the saved
[four-chain spin maps](parity_structure_spin_w34.md) while preserving
their matrix multiplication coefficients. All ranks below have exact
integer kernel certificates and nonzero minors over a finite field.
These are constructive parameter spaces for extending the core; they
do not complete a square matrix tensor or improve the exponent.

## 1. Source and retained core

Write the three source legs in the common coordinates
$F(i,k,s)$, with $i,s<8$ and $k<15$. The source tensor is

\[
 T=\sum_{i,p,r,j,q,s=0}^{7}
 X(i,p+q,s)Y(p,r+s,j)Z(r,i+j,q).
 \tag{1}
\]

Start with the exact four-chain restriction
$A(8,8)\to M(3,3,28)$ and remove original middle channel zero.
Relabel its other channels as $0,\ldots,26$. The retained first
images are denoted $x_{IJ}$; the retained second and third images
are $y_{J\alpha}$ and $z_{\alpha I}$. They satisfy

\[
 T(x_{IJ},y_{J'\alpha},z_{\beta I'})
 =\delta_{II'}\delta_{JJ'}\delta_{\alpha\beta}.
 \tag{2}
\]

The three deleted third images are denoted $d_0,d_1,d_2$.
Every assertion in this note concerns these particular saved maps
and this particular deleted channel.

The complete first response of the retained second and third maps
is supported on

\[
 S=\operatorname{span}\{F(i,k,s):k<3\},\qquad \dim S=192.
\]

A recomputed 192-square minor proves that this response is injective
on $S$, both before and after the deletion. Its full kernel is
therefore the 768-dimensional coordinate space with $k\ge3$.
The preimage of the nine-dimensional span of the first responses
in (2) has dimension $768+9=777$.

## 2. All added-row kernels with the first maps fixed

For a possible additional second or third image, the equations
against two retained legs are linear. Define

\[
 \begin{aligned}
 K_Y&=\{u:T(x_{IJ},u,z_{\alpha I'})=0
                  \text{ for every }I,J,I',\alpha\},\\
 K_Z&=\{v:T(x_{IJ},y_{J'\alpha},v)=0
                  \text{ for every }I,J,J',\alpha\}.
 \end{aligned}
 \tag{3}
\]

Each system has 729 scalar equations. The exact results are:

| Free leg | Nonzero source columns in its equations | Equation rank | Complete kernel dimension |
|---|---:|---:|---:|
| $Y$ | 237 | 224 | 736 |
| $Z$ | 216 | 213 | 747 |

For the second leg, all nonzero columns lie in

\[
 B_Y=\operatorname{span}\{F(p,L,j):p<3,\ L<10,\ j<8\},
 \qquad\dim B_Y=240.
\]

The three absent coordinates inside $B_Y$ are $F(p,0,5)$, $p<3$.
The certificate gives 13 independent integer relations among the
other 237 columns. Together with the 723 absent coordinate axes,
they are a full basis of $K_Y$.

For the third leg, the actual support is all of

\[
 B_Z=\operatorname{span}\{F(r,H,q):r<8,\ H<9,\ q<3\},
 \qquad\dim B_Z=216.
\]

There are three independent integer relations inside this support.
Together with the 744 outside coordinate axes, they give a full
basis of $K_Z$.

These equations assume the stated first images $x_{IJ}$. Moving
those first images changes the added-row equations.

## 3. A particularly simple description of the low third-leg freedom

The three omitted third rows $d_0,d_1,d_2$ lie in $B_Z$ and are
independent. The original 28-channel coefficient identity gives

\[
 T(x_{IJ},y_{J'\alpha},d_{I'})=0.
\]

Since $\dim(K_Z\cap B_Z)=216-213=3$, it follows that

\[
 K_Z\cap B_Z=\operatorname{span}\{d_0,d_1,d_2\}.
 \tag{4}
\]

Consequently every change to a retained third image, supported in
$B_Z$ and preserving (2) with the other maps fixed, has exactly the
form

\[
 z'_{\alpha I}=z_{\alpha I}
        +\sum_{a=0}^{2}c_{\alpha I,a}d_a.
 \tag{5}
\]

The coefficients are independent for each retained row. The
description is more general than applying a common middle-channel
basis change to all three values of $I$.

## 4. Eight second-leg directions that remain free against all old third rows

Let

\[
 L_Y=\operatorname{span}\{F(p,L,j):p<2,\ L<10,\ j<8\},
 \qquad \dim L_Y=160.
\]

Impose the second-leg kernel equations against all 84 original
third rows, including the three deleted ones. Their exact rank on
$L_Y$ is 152. Thus

\[
 U=\{u\in L_Y:T(x_{IJ},u,z)=0
          \text{ for all original third rows }z\}
 \tag{6}
\]

has dimension eight. The certificate supplies an explicit integral
basis $u_1,\ldots,u_8$ and replays all $9\cdot84$ coefficients of
each vector.

Equations (5) and (6) give an exact joint family:

\[
 \begin{aligned}
 y'_{J\alpha}&=y_{J\alpha}
                  +\sum_{\ell=1}^{8}a_{J\alpha,\ell}u_\ell,\\
 z'_{\alpha I}&=z_{\alpha I}
                  +\sum_{a=0}^{2}c_{\alpha I,a}d_a.
 \end{aligned}
 \tag{7}
\]

Every choice of the $81\cdot8+81\cdot3=891$ parameters preserves
(2). Indeed, the terms linear in the third correction vanish by
the deleted-channel identity. The terms linear in the second
correction, and all terms containing both corrections, vanish
by (6). The first maps remain fixed. The second and third maps
remain injective because their contraction still equals the
concise tensor in (2).

All maps in (7) use $p<2$ and $q<2$. Their first response therefore
remains supported on $S$. This support statement alone gives
neither a rank reduction nor a larger tensor restriction.

## 5. Two exact checks on the scope of this joint family

For $f=F(7,0,7)$ or $F(7,2,7)$, define the endpoint matrices

\[
 \begin{aligned}
 A_f&=(T(f,y_{J\alpha},z_{\beta I})),\\
 B_f&=(T(f,u_\ell,z_{\beta I})),\\
 D_f&=(T(f,u_\ell,d_a)).
 \end{aligned}
 \tag{8}
\]

For both choices, the replay finds:

* a nonzero six-square minor of $A_f$;
* only four nonzero rows of $B_f$;
* every coefficient of $D_f$ equal to zero;
* every coefficient $T(f,y_{J\alpha},d_a)$ equal to zero.

Thus the endpoint response after (7) is $A_f+A B_f$, independent
of the third-leg parameters. It cannot vanish: $A_f$ has rank at
least six, while $A B_f$ has rank at most four.

This conclusion is restricted to (7). In particular, it does not
cover second-leg directions that depend on the moving third map,
changes to the retained first maps, other channel hyperplanes, or
non-coordinate first response directions. Those are separate
construction problems.

## 6. Exact replay and files

The verifier reads the actual rational maps. It independently
enumerates all 32,768 terms of the $A(4,8)$ lift and all 262,144 terms
of the $A(8,8)$ lift, checking 15,876 and 63,504 output coefficients.
It then rebuilds the response equations, checks each saved minor
modulo the prime $1,000,000,007$, and checks every kernel coefficient
over the integers. A nonzero modular minor certifies the same
rank lower bound over $\mathbb Q$; the explicit kernel basis
certifies the matching upper bound.

~~~bash
python -S research/ai/2026-10-20-anisotropic-constructions/parity_balancing_spin_w34_freedoms.py
python -S -m unittest discover -s tests -p test_parity_balancing_spin_w34_freedoms.py
~~~

The [certificate](../../../results/anisotropic-constructions-2026-10-20/parity_balancing_spin_w34_freedoms_certificate.json)
contains the actual minors and integral vectors. The
[report](../../../results/anisotropic-constructions-2026-10-20/parity_balancing_spin_w34_freedoms_report.json)
records the complete replay. Numerical discovery arrays are not
used for acceptance. The proof and verifier were checked by a second
agent in this generating session. No external independent review or
formalization is claimed.
