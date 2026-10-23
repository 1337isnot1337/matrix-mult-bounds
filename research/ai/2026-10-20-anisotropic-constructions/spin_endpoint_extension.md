# A sharp extension gate for the repaired spin core

October 21, 2026. The repaired maps give an actual ordinary restriction
$A(8,8)\to M(3,3,27)$ with first response rank $191$. This note proves
that **those particular second- and third-leg rows cannot be retained
in an ordinary extension to $M_{27}\oplus M_7$**. The first-core maps
are allowed to change by arbitrary response-kernel vectors.

The statement does not exclude a changed retained third map, the
$D=774$ target $M_{27}\oplus M_6\oplus M_3$, an unrestricted source
construction, or a singular construction. The dimension count alone
is compatible with the repaired core; the extra coefficient condition
below is what closes this fixed extension.

## 1. The first image is forced at dimension 778

Let the common source basis be $F(i,k,s)$, with $i,s<8$ and $k<15$.
The original source coefficients are

\[
 X(i,p+q,s)Y(p,r+s,j)Z(r,i+j,q).
 \tag{1}
\]

Fix the repaired rows $Y^0_{J\alpha},Z^0_{I\beta}$, with
$I,J<3$ and $\alpha,\beta<27$, and define

\[
 \Psi(f)_{J\alpha,I\beta}=T(f,Y^0_{J\alpha},Z^0_{I\beta}).
\]

Their verified response rank is $191$. The entire kernel is

\[
 K=W\oplus\mathbb Qe,\qquad
 W=\operatorname{span}\{F(i,k,s):k\ge3\},\quad
 \dim W=768,\quad e=F(7,0,7).
 \tag{2}
\]

Indeed the response is supported on the other $191$ coordinates with
$k<3$, and its saved $191\times191$ minor is nonsingular. Let $X^0_{IJ}$
be the nine known preimages of the matrix-slice responses. The full
preimage of their span is

\[
 H=K+\operatorname{span}\{X^0_{IJ}:I,J<3\},\qquad \dim H=778.
 \tag{3}
\]

In any extension retaining $Y^0,Z^0$, every other first target unit
has zero response on these retained rows. Hence the entire first
image lies in $H$. The concise target $M_{27}\oplus M_7$ has common
leg dimension $27^2+7^2=778$, so its first map is injective and its
image must be all of $H$.

The nine actual first-core images may be

\[
 \widetilde X_{IJ}=X^0_{IJ}+w_{IJ},\qquad w_{IJ}\in K.
 \tag{4}
\]

No step below assumes that these $w_{IJ}$ vanish.

## 2. A 120-column convolution map

For a second source vector $y$, write
$y_p(L,j)=y(p,L,j)$, where each block $y_p$ has $15\cdot8=120$
coordinates. Fix the middle label $\alpha=0$. Define the linear map

\[
 G_1:\mathbb Q^{120}\longrightarrow\mathbb Q^{4992}
\]

by

\[
 (G_1v)_{i,s,I,\beta}
 =\sum_{\substack{0\le L<15,\ 0\le j<8\\0\le L-s<8}}
 v(L,j)\,Z^0_{I\beta}(L-s,i+j,1),
 \quad i,s<8,\ I<3,\ 1\le\beta<27.
 \tag{5}
\]

There are $8\cdot8\cdot3\cdot26=4992$ output coordinates. The
entry of its matrix in column $8L+j$ and row $(i,s,I,\beta)$ is exactly
the saved third-map coefficient at $F(L-s,i+j,1)$, or zero when
$L-s$ is outside $0,\ldots,7$.

The supplied certificate selects $120$ of these output rows. Its
$120\times120$ integer numerator minor is nonsingular modulo $65521$.
Consequently $G_1$ is injective over the rationals. The verifier
regenerates every minor entry from the actual repaired-map export;
it does not use a stored numerical matrix or accept a rank assertion.

## 3. Descending through the first long coordinate

Suppose an extension existed. Choose one new second-vertex index
$j_0\notin\{0,1,2\}$ in the $27$-dimensional square block, and let
$y$ be the image of its matrix unit $Y_{j_0,0}$.
For every retained $Z^0_{I\beta}$ with $\beta\ne0$, the target
coefficient is zero for every first target input. Since the first
image is all of $H$,

\[
 T(h,y,Z^0_{I\beta})=0
 \quad\text{for every }h\in H,\ I<3,\ \beta\ne0.
 \tag{6}
\]

The retained third map uses only last short indices $q=0,1$.
At first long coordinate $k=8$, equation (1) therefore has only
the pair $(p,q)=(7,1)$. All $F(i,8,s)$ belong to $W\subseteq H$,
so (6) becomes $G_1y_7=0$. Injectivity gives $y_7=0$.

At $k=7$, the only possible pairs are $(7,0)$ and $(6,1)$.
The first has already vanished, so $G_1y_6=0$ and $y_6=0$.
Repeating this argument down through $k=3$ proves

\[
 y_2=y_3=\cdots=y_7=0.
 \tag{7}
\]

This argument applies to arbitrary coefficients in all $960$ second
source directions. It did not presuppose a support restriction for
the new row.

## 4. The remaining response has rank at most one

By (7), $y$ uses only $p=0,1$. Together with the retained third-map
support $q=0,1$, equation (1) shows that

\[
 T(w,y,Z^0)=0\qquad(w\in W).
 \tag{8}
\]

The target identities also give
$T(\widetilde X_{IJ},y,Z^0)=0$ for every actual first-core image:
its second-vertex index is below three, whereas $y$ has second-vertex
index $j_0$. The $768$ directions in $W$ and the nine actual vectors
$\widetilde X_{IJ}$ are independent. Applying $\Psi$ proves this,
because it vanishes on $W$ and has nine independent values on the
latter vectors.

Thus the bilinear form

\[
 H\times\operatorname{span}(Z^0)\longrightarrow\mathbb Q,
 \qquad(h,z)\longmapsto T(h,y,z)
\]

vanishes on a $777$-dimensional first subspace of the
$778$-dimensional $H$. Its matrix rank is at most one.
In the desired matrix tensor, contraction with $Y_{j_0,0}$ has
rank three on the full first leg and the retained third rows:
the three independent pairs are

\[
 X_{0,j_0}Z_{0,0},\qquad X_{1,j_0}Z_{0,1},\qquad X_{2,j_0}Z_{0,2},
\]

where the last notation denotes the retained variables $Z_{\alpha,I}$
with $\alpha=0$. This contradicts the rank bound one and proves the
claimed fixed-core extension exclusion.

## 5. Replay and constructive consequence

The check first replays the actual repaired restriction and its exact
$191$-rank response certificate. It then rebuilds the small additional
minor from the retained $Z$ coefficients:

```bash
python -S research/ai/2026-10-20-anisotropic-constructions/spin_endpoint_extension.py
```

The new minor is
[spin-endpoint-extension-minor.json](../../../results/anisotropic-constructions-2026-10-20/spin-endpoint-extension-minor.json),
and the complete replay report is
[spin-endpoint-extension-certificate.json](../../../results/anisotropic-constructions-2026-10-20/spin-endpoint-extension-certificate.json).
The verifier uses only the standard library.

A construction continuing toward the $778$-dimensional target must
change this retained pair of maps or create additional first-kernel
freedom. The $774$-dimensional alternative has four dimensions of
slack inside $H$, so the forced-image step used here does not apply.
No exclusion for that alternative is asserted.

The rank data and the moving-first-lift argument have been checked by
different agents in this generating session. No external independent
review or formalization is claimed.
