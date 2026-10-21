# An exact eleven-channel crossed convolution module

October 21, 2026. There is an ordinary restriction over the rational
numbers

\[
 \boxed{C(2,4)\otimes C(2,8)\longrightarrow M(2,2,11),} \tag{1}
\]

with the two convolution factors oriented as specified below. The
source format is `(4,40,36)`, the target format is `(4,22,22)`, and
the first leg map is the identity. Complete rational maps and all
coefficient checks are supplied. This improves the coordinate
construction's eight channels for this same source and fixed first
leg. No claim of optimality or matrix multiplication exponent
improvement is made.

The full-source lift gives the additional actual restrictions

\[
 A(4,8)\longrightarrow M(4,4,11),\qquad
 A(8,8)\longrightarrow M(4,4,22).
\]

Their formulas, exported maps, and separate full-source replays are
given in the [lift package](parity_balancing_cross_module_lifts.md).
These subsystems do not establish the larger `M27 direct_sum M7`
target. Compatibility with such an extension remains a separate
construction problem.

## 1. The original source and its four matrices

Use source coordinates

\[
 x_{i,u},\quad y_{a+u,j},\quad z_{a,j+i},
 \qquad i,u\in\{0,1\},\quad0\le a<4,\quad0\le j<8.
\]

The complete source tensor is

\[
 R=\sum_{i,u,a,j}x_{i,u}\,y_{a+u,j}\,z_{a,j+i}.       \tag{2}
\]

It has 128 terms. Number the first, second, and third source
coordinates respectively by `2*i+u`, `8*(a+u)+j`, and `9*a+j+i`.
The two convolution factors in (2) have their long coordinates on
different legs; the source is not a direct sum of two convolutions.

Let

\[
 V=\mathbb Q^{4\times8},\quad
 Y=\mathbb Q^{5\times8},\quad
 Z=\mathbb Q^{4\times9}.
\]

Define `J_0,J_1:V->Y` by the two inclusions on the first index,
and `K_0,K_1:Z->V` by the two coefficient windows on the second:

\[
 (J_uv)_{a+u,j}=v_{a,j},\qquad
 (K_iz)_{a,j}=z_{a,j+i}.                          \tag{3}
\]

The four source matrices are exactly `J_u K_i`. Thus for a fixed
first input `x_(i,u)`, the bilinear contraction is `y^T J_u K_i z`.

## 2. A constructive quotient-and-pair lemma

Choose a subspace `U` of `V`, and let

\[
 W=J_0U+J_1U\subseteq Y.
\]

Form the space of pairs

\[
 \mathcal D=\{(z_0,z_1)\in Z\oplus Z:
 K_1z_0\in U,\ K_0z_1\in U,
 K_0z_0-K_1z_1\in U\}.                           \tag{4}
\]

Suppose there are `r` pairs `(z_0j,z_1j)` in this space for which
the following columns are independent:

\[
 \left[\operatorname{basis}(W),\
 J_0K_0z_{01},\ldots,J_0K_0z_{0r},\
 J_1K_0z_{01},\ldots,J_1K_0z_{0r}\right].         \tag{5}
\]

Choose row functionals `ell_(u,j)` on `Y` that annihilate `W` and
are dual to the two displayed groups of `r` columns. Extend them
arbitrarily if (5) does not span all of `Y`. Send the target third
leg's unit `(j,i)` to `z_ij`, and its second leg's unit `(u,j)` to
the coefficient vector of `ell_(u,j)`.

The first two conditions in (4) kill both off-diagonal choices of
the `K` index after applying these row functionals. The third
condition makes the two diagonal choices equal modulo `W`. The
duality in (5) therefore gives

\[
 \ell_{u,j}J_{u'}K_i z_{i',j'}
 =\delta_{u,u'}\delta_{i,i'}\delta_{j,j'},        \tag{6}
\]

which is exactly the complete matrix tensor `M(2,2,r)`. This is a
constructive sufficient condition; no vanishing of untested mixed
coefficients is assumed.

## 3. Six short polynomial chains

Identify `V` with polynomials in `x,y` having degrees at most three
and seven respectively. Choose the following six polynomials, each
of degree at most two in `x`:

\[
\begin{aligned}
 g_0&=-x^2y-x^2y^3-x^2y^6,\\
 g_1&=-y^6-y^7+x^2y,\\
 g_2&=y^2+xy-x^2y^4,\\
 g_3&=y-xy^5+x^2y^2,\\
 g_4&=y^4-xy^5+x^2y^3,\\
 g_5&=-xy^7+x^2y^3-x^2y^6.
\end{aligned}                                                   \tag{7}
\]

Set

\[
 U=\operatorname{span}\{g_0,xg_0,\ldots,g_5,xg_5\}.
\]

The twelve displayed vectors are independent. Both `J` maps amount
to retaining a polynomial or multiplying it by `x`, now allowing
degree four in `Y`. Consequently `W` is spanned by
`g_j,xg_j,x^2g_j` for the six values of `j`, and has dimension at
most 18. The exact rank certificate gives equality.

The [saved witness](../../../results/anisotropic-constructions-2026-10-20/crossed-module11-witness.json)
includes an integer `20 by 32` matrix `Q` with 49 nonzero entries
whose kernel is exactly `U`. The three conditions in (4) have the
complete matrix

\[
 \begin{pmatrix}
 QK_1&0\\0&QK_0\\QK_0&-QK_1
 \end{pmatrix}.                                  \tag{8}
\]

This `60 by 72` matrix has rank 60, so `dim(D)=12` over the
rationals. The exact maps use eleven of the twelve canonical
free-variable kernel vectors, with zero-based indices

\[
 0,1,2,3,4,6,7,8,9,10,11.
\]

The resulting 40-column matrix (5) is square. With the ordered
`W` basis specified in the witness, its determinant is

\[
 \det B=-\frac{3575}{128}\ne0.                   \tag{9}
\]

Take the last 22 rows of `B^-1` for the second-leg map. The selected
pairs supply the third-leg map. This proves (1) with explicit
constant rational maps.

## 4. Full rational and coefficient verification

The saved second-leg map has shape `22 by 40`, common denominator
2,860, and 611 nonzero entries. The third-leg map has shape
`22 by 36`, denominator eight, and 217 nonzero entries. Target rows
are ordered by `11*u+j` on the second leg and `11*i+j` on the third;
the latter is the coordinate `z_(j,i)` of the matrix product.

The standard-library verifier checks the construction in two ways.
First, it reconstructs `U` from (7), checks `QU=0`, and certifies the
ranks of `U`, `Q`, `W`, and (8) modulo the prime 65,521. The matching
upper bounds are supplied by their dimensions and the eighteen
explicit polynomial-chain vectors, so these are exact rational
rank certificates. It checks every selected pair against all three
conditions in (4), computes (9) with integer Bareiss elimination,
and checks that the saved second-leg map has the required dual
products with `B`.

Separately, it loops over all 128 original source terms in (2),
expands the saved maps, and collects all 10,968 integer
contributions. After cancellation the resulting tensor has exactly
the 44 coefficients of `M(2,2,11)`, each with numerator 22,880 over
the product denominator 22,880. The other 1,892 coefficients vanish.
Thus all 1,936 coefficients, including unwanted terms, are checked.

The full-source lift verifier was run by a second agent in this
generating session. It separately checks all original source terms
of `A(4,8)` and `A(8,8)` using the exported lifted maps. These are
within-session checks; there has been no external independent review
or proof-assistant formalization.

## 5. Scope and composability

The eight-channel coordinate seed uses disjoint two-by-two grid
cells in the two convolution factors. The present construction
uses six overlapping polynomial chains and cancels their shared
directions through (4). The improvement from eight to eleven
channels is an actual ordinary source restriction.

Two matched source copies with their four-dimensional first leg
shared can use the two eleven-channel maps on disjoint auxiliary
coordinates, producing twenty-two channels. This is the source of
the `A(8,8)->M(4,4,22)` lift. Mixing the two matched copies may
provide additional channels, but no such improvement is part of
this certificate. Adding a large square matrix block requires
further compatible source equations; the rectangular subsystem
does not supply them automatically.

Neither displayed full-source lift passes the current finite
`9/4` source-cost gate by itself. No value below `9/4` is claimed.

## Replay

```sh
python -S research/ai/2026-10-20-anisotropic-constructions/crossed_module11.py
python -S -m unittest discover -s tests -p test_crossed_module11.py
```

The [acceptance report](../../../results/anisotropic-constructions-2026-10-20/crossed-module11-certificate.json)
records the exact determinant, map sizes, rank checks, source replay,
and witness hash. Discovery used finite-field rank tests, followed
by rational reconstruction. Acceptance uses only integer arithmetic
and Python's exact rational numbers.
