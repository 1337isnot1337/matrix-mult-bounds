# A certified finite rectangular convolution degeneration

Date: October 21, 2026.

**Result.** There are exact real constant matrices that give a degeneration

\[
C(5,10)\unrhd T_4.
\]

The conclusion follows from a rational contraction certificate, whose
acceptance uses only integer and rational arithmetic. The displayed numerical
discovery point is an approximation to the exact matrices. It is not asserted
to solve the polynomial equations exactly.

This is a finite construction. It does not supply a family for all sizes and
does not establish a matrix multiplication exponent below \(9/4\).
The argument and certificate were produced by coordinated AI agents in this
owner-directed research session. Same-session checks are not external
mathematical review or formal verification. No historical priority is claimed.

## Explicit rational refinement

A later [polynomial-flag construction](rational_flag_construction.md) gives
explicit rational matrices for the same finite degeneration. It replaces
existence near a rational center with a direct rational coefficient identity.
The [rational witness](../../../results/rectangular-t4-certificate-2026-10-21/rational-witness.json)
and its [independent full-coefficient replay](../../../results/rectangular-t4-certificate-2026-10-21/rational-verification.json)
are retained alongside the original contraction certificate. The rational
maps work over every field of characteristic zero.

The two certificates are different constructions of the same finite result.
The original exact contraction proof remains valid. Neither certificate
supplies the unbounded family needed to lower the exponent.

## 1. Source, target, and map orientation

The convolution source is

\[
C(5,10)=\sum_{i=0}^{4}\sum_{j=0}^{9}X_iY_jZ_{i+j}.
\]

Its three source dimensions, in this order, are \((5,10,14)\).
The canonical target is

\[
T_4=\sum_{a+b+c+d=3}X_{a+c}Y_{a,b}Z_{c,d}.
\]

It has dimensions \((4,10,10)\) and exactly twenty coefficients equal to one.
All other coefficients are zero. Both ten-dimensional target factors have
the node order

\[
(0,0),(0,1),(1,0),(0,2),(1,1),(2,0),
(0,3),(1,2),(2,1),(3,0).
\]

Write the constant target-by-source maps as

\[
A\in\mathbb R^{4\times5},\qquad
Y\in\mathbb R^{10\times10},\qquad
Z\in\mathbb R^{10\times14}.
\]

In particular, the source factor of dimension ten maps through \(Y\), and
the source factor of dimension fourteen maps through \(Z\). Before applying
weights, the coefficient at target coordinates \((x,y,z)\) is

\[
Q_{x,y,z}(A,Y,Z)=
\sum_{i=0}^{4}\sum_{j=0}^{9}A_{x,i}Y_{y,j}Z_{z,i+j}.
\tag{1}
\]

The 260 map entries are listed row by row, first \(A\), then \(Y\), then
\(Z\). Their index intervals are \(0\!:\!19\), \(20\!:\!119\), and
\(120\!:\!259\), respectively. This ordering is part of the certificate.

## 2. The 172 coefficient equations

Give the target rows of \(Y\) and \(Z\), according to their total degree
\(p\in\{0,1,2,3\}\), the following weights:

| Total degree \(p\) | 0 | 1 | 2 | 3 |
| --- | ---: | ---: | ---: | ---: |
| \(Y\) row weight \(f(p)\) | -1 | -1 | 0 | 1 |
| \(Z\) row weight \(g(p)\) | -1 | 0 | 1 | 1 |

Every \(A\) row has weight zero. Set

\[
Y(\varepsilon)_{y,j}=\varepsilon^{f(\deg y)}Y_{y,j},\qquad
Z(\varepsilon)_{z,k}=\varepsilon^{g(\deg z)}Z_{z,k}.
\]

Each target coefficient is exactly one Laurent monomial in \(\varepsilon\),
with coefficient (1). The twenty nonzero target entries all have weight
zero because \(g(q)=-f(3-q)\).

For every coordinate of nonpositive weight, impose

\[
Q_{x,y,z}(A,Y,Z)=(T_4)_{x,y,z}.
\tag{2}
\]

There are 48 negative-weight and 124 zero-weight coordinates, hence 172
equations. Each equation is a sum of fifty trilinear monomials and a
constant in \(\{0,-1\}\). An exact solution of (2) gives

\[
(A\otimes Y(\varepsilon)\otimes Z(\varepsilon))C(5,10)
=T_4+\varepsilon E_1+\varepsilon^2E_2
\]

for fixed tensors \(E_1,E_2\). This is the required degeneration.

The same constant matrices also work with the natural degree weights
\(w_X=-3\), \(w_Y(p)=p\), and \(w_Z(q)=q\). Indeed,
\(p+q\le3\) implies \(p\le3-q\). Since \(f\) is nondecreasing,

\[
f(p)+g(q)=f(p)-f(3-q)\le0.
\]

Thus every one of the 140 natural-grading equations is among (2).
The verifier checks this inclusion directly. With those weights, the
positive remainder has degree at most three.

## 3. Rational data and the exact existence proof

The [certificate](../../../results/rectangular-t4-certificate-2026-10-21/certificate.json)
specifies a rational center \(x_0\in\mathbb Q^{260}\), a list of 172 free
coordinate indices, a rational matrix \(R\in\mathbb Q^{172\times172}\),
and the rational radius

\[
r=10^{-8}.
\]

Both the center and \(R\) are stored as integer numerators with common
denominator \(2^{40}\). The other 88 coordinates remain fixed at their
rational center values. Write \(u\in\mathbb R^{172}\) for the free
coordinates, \(u_0\) for their center, and \(F(u)\in\mathbb R^{172}\)
for the left side minus the right side of (2).

Let \(J_0=DF(u_0)\). The integer-only verifier computes the following
quantities exactly as rational numbers:

\[
\eta=\|RF(u_0)\|_\infty,\qquad
\delta=\|I-RJ_0\|_\infty,\qquad
B=\|R\|_\infty,\qquad
M=\|x_0\|_\infty.
\]

Matrix norms here are maximum absolute row sums. The approximate inverse
\(R\) is part of the proposed data; its reliability is established by the
exact bound on \(\delta\), not by the floating inversion used to discover it.

On the closed cube \(\|u-u_0\|_\infty\le r\), all 260 map entries have
absolute value at most \(M+r\). Each monomial in (1) has at most six
ordered second partial derivatives, each of absolute value at most
\(M+r\). There are fifty monomials per equation. Therefore

\[
\|DF(u)-J_0\|_\infty\le300(M+r)r.
\tag{3}
\]

This bound remains valid when a coordinate is fixed, because deleting
derivatives only reduces the absolute row-sum bound.

Consider the polynomial map

\[
G(u)=u-RF(u).
\]

Equations (3) and the induced matrix-norm inequality give the Lipschitz
bound

\[
\|G(u)-G(v)\|_\infty\le q\|u-v\|_\infty,
\qquad
q=\delta+300B(M+r)r.
\]

Also

\[
\|G(u)-u_0\|_\infty\le\eta+qr.
\]

The [exact verification report](../../../results/rectangular-t4-certificate-2026-10-21/verification.json)
records rational values and proves

\[
\delta<1,\qquad q<1,\qquad \eta+qr<r.
\tag{4}
\]

For orientation, the decimal displays are approximately

| Quantity | Decimal display |
| --- | ---: |
| \(\eta\) | \(8.161\times10^{-12}\) |
| \(\delta\) | \(7.829\times10^{-11}\) |
| \(B\) | 95.964 |
| \(M\) | 1.918 |
| \(q\) | 0.000553 |
| \(\eta+qr\) | \(1.369\times10^{-11}\) |
| \(r\) | \(10^{-8}\) |

These rounded displays do not participate in any acceptance decision.

For completeness, (4) implies existence without any numerical assumption.
Start the iteration \(u_{n+1}=G(u_n)\) at \(u_0\). It remains in the
closed cube, and consecutive distances decrease by a factor at most \(q\).
The geometric-series bound makes this a Cauchy sequence. Its limit
\(u_*\) lies in the cube and satisfies \(G(u_*)=u_*\) by continuity.
Since \(\|I-RJ_0\|_\infty<1\), the geometric matrix series shows that
\(RJ_0\), and hence the square matrix \(R\), is invertible. Consequently
\(RF(u_*)=0\) implies \(F(u_*)=0\).

This proves that exact real matrices satisfying all 172 equations exist.
Section 2 then gives the claimed degeneration over \(\mathbb R\), and by
extension over \(\mathbb C\). No assertion over every field is made.

The target is concise in all three factors. Thus the resulting constant
maps have full row rank: diagonal row rescaling preserves map rank, while
matrix flattening rank cannot increase at a tensor limit. This observation
does not replace any coefficient equation or numerical check.

## 4. Reproduction and evidence boundaries

From the repository root, run:

```sh
python research/ai/2026-10-21-rectangular-t4-certificate/verify_certificate.py results/rectangular-t4-certificate-2026-10-21/certificate.json
python -m unittest discover -s tests -p test_rectangular_t4_certificate.py -v
```

The verifier uses only the Python standard library. Python optimization
(`-O`) is unsupported because the acceptance checks use assertions.
It rebuilds all coefficient polynomials and derivatives from the source
indices, performs the rational matrix products, and checks (4). It does
not import the numerical discovery code. The certificate file records
all data needed for this replay.

The [discovery report](../../../results/rectangular-t4-certificate-2026-10-21/discovery.json)
preserves the floating residual, map singular values, and Jacobian
diagnostic. A full actual-tensor fit first suggested the three degree
weights; the coefficient solve then reached a well-conditioned numerical
zero. Rounding that point, selecting a Jacobian minor, and rounding its
inverse produced the rational data. Only the exact argument above supports
the finite existence claim.

The broader open target remains an all-size construction with source
\(C(m+O(1),m(m+1)/2+O(m))\). The present proof settles one finite instance
and does not address those quantifiers. It is compatible with the earlier
square-shared-source obstruction because its shared source dimension is
five, while the target shared dimension is four. It also lies outside the
previously studied symmetric two-weight split.

## 5. Independent same-session coefficient replay

The primary agent wrote a second verifier that reads only the frozen certificate.
It expands all 400 target positions from the fifty original source monomials.
It then recomputes the 172 selected Jacobian columns by exact one-coordinate
integer finite differences. Each variable occurs linearly in each coefficient,
so those finite differences are exact derivatives at the integer center.
This does not reuse the first verifier's derivative implementation.

The independent replay obtains exactly the same rational values for eta, delta,
q, and the image radius. Its [report](../../../results/rectangular-t4-certificate-2026-10-21/independent-verification.json)
records the SHA-256 of the certificate and the matching fractions. Run it with:

```sh
python research/ai/2026-10-21-rectangular-t4-certificate/independent_replay.py results/rectangular-t4-certificate-2026-10-21/certificate.json
```

The primary agent also checked the contraction argument, the source orientation,
the twenty target terms, and the natural-grading inclusion. This is independent
implementation within the same AI session; external mathematical review remains
outstanding.
