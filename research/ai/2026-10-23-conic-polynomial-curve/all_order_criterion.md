# The complete all-order normal-class criterion on the affine conic base

October 23, 2026. Claim `AI-CONIC-ALL-ORDER-CRITERION-002` is written
and unreviewed. It combines the new polynomial curve with the credited
complete two-jet criterion and exact linear-component curves from PR101.

## Precise statement

Work over \(\mathbb C\) with the canonical 4096-term integer source
and the credited fourteen-row constant conic maps at an arbitrary
affine parameter triple \((a,b,c)\in\mathbb C^3\). The first-source
flattening has leading rank twelve. Write \(N_1,N_2\) for the two
normalized nonboundary tangent classes of PR101.

For every projective class \([\lambda:\mu]\in\mathbb P^1(\mathbb C)\),
represented by \((\lambda,\mu)\ne(0,0)\), the following are equivalent:

1. Some first tangent whose normal component is
   \(\lambda N_2+\mu N_1\) extends to a rank-twelve incidence two-jet.
2. Some first tangent with that normal component extends to an actual
   formal incidence curve with fourteen-row maps over \(\mathbb C[[t]]\)
   and first-source rank twelve.
3. Some first tangent with that normal component extends to polynomial
   maps \(B(t),C(t)\) of degrees at most one and three, respectively,
   with the same leading ranks and fixed first-source kernel \(K\).
4. The scalar equation

   \[
   (a-c)(b+c)(c\lambda^3+\mu^3)=0                             \tag{1}
   \]

   holds.

All existence statements allow a suitable boundary component of the
first tangent. A two-jet or formal curve may in general move its
first-source kernel; item3 supplies a fixed-kernel representative when
the condition holds. The normal tangent is nonzero because
\(N_1,N_2\) are an independent normal basis and
\((\lambda,\mu)\ne(0,0)\).

The equation is homogeneous in \((\lambda,\mu)\), so its vanishing
depends only on the projective class. Stating the normal component for
a chosen representative also specifies its scale; the constructions
below realize that scale by rescaling \(t\).

## Imported results and exact scope

The [PR101 proof](../2026-10-21-conic-second-jets/proof.md), pinned at
commit `539b539dc4eac09114899fd76472aee2d78d9f62`, supplies:

- `AI-CONIC-TANGENT-001`: the complete tangent consists of the smooth
  68-dimensional boundary tangent and the two independent normals.
- `AI-CONIC-SECOND-JET-002`, Section4: for every affine complex base
  and every projective normal class, some first tangent extends to a
  two-jet if and only if (1) holds. The result allows arbitrary boundary
  velocity, arbitrary second-row coefficients and a moving source
  kernel. Its pure-normal cases are verified separately from its
  Laurent chart; necessity therefore includes \(\lambda=0\) and
  \(\mu=0\).
- `AI-CONIC-POLYNOMIAL-JET-003`, Section5: on either linear component
  \(a=c\) or \(b=-c\),

  \[
  B(t)=B_0+t(\lambda N_{B,2}+\mu N_{B,1}),\qquad
  C(t)=C_0+t(\lambda N_{C,2}+\mu N_{C,1})                       \tag{2}
  \]

  are exact fixed-kernel incidence curves for every \(\lambda,\mu\).
  Their unchanged constant minors give the required formal ranks.

The full proof file, source operator, exact verifier and witness archive
are byte-pinned in this package's `sources.json`. These imported results
retain their written, unreviewed status. This note does not replace
their complete tangent/cohomology computation with a finite sample.

## Proof of the equivalence

Item3 implies item2 by viewing each polynomial as a formal power series.
Item2 implies item1 by reducing the formal curve modulo \(t^3\).
The leading minors remain units, so this reduction is a two-jet in the
same incidence problem. The complete PR101 necessity then proves
item1 implies item4.

It remains to prove that (1) supplies the polynomial curves of item3.
If \(a=c\) or \(b=-c\), use the already-credited linear curves (2).
Both degrees are at most one, so the required degree bounds hold.

Suppose instead that \((a-c)(b+c)\ne0\). Then (1) gives
\(c\lambda^3+\mu^3=0\). One must have \(\lambda\ne0\): if
\(\lambda=0\), the equation would force \(\mu^3=0\), contradicting
the nonzero projective representative. Hence put

\[
d=\mu/\lambda,\qquad c=-d^3.
\]

The [polynomial construction](proof.md) of
`AI-CONIC-POLYNOMIAL-CURVE-001` supplies degree-one/degree-three maps
with this constant base and normal component \(N_2+dN_1\). Substitute
\(\lambda t\) for its deformation parameter. The resulting first
normal component is

\[
\lambda(N_2+dN_1)=\lambda N_2+\mu N_1.
\]

The substitution preserves polynomial degrees, the exact source-kernel
identity and the constant unit minors. This proves item3 for the cubic
component, including \(\mu=0\), when \(d=0\) and \(c=0\).

For completeness, the projective class with \(\lambda=0\) has
\(\mu\ne0\), and (1) reduces exactly to
\((a-c)(b+c)=0\). Thus the linear-component construction already covers
every admissible class at that projective point. No projective normal
direction is omitted. This completes all four implications.

## What this closes and what it does not

Within the stated affine conic base chart, the two-jet scalar obstruction
is the complete obstruction to the **existence of an all-order lift
for a nonzero normal class**. Every allowed class has an explicit
polynomial representative of bounded degree.

The claim does not say that a prescribed full first jet extends, that
an arbitrary existing two-jet extends, or that every choice of boundary
velocity works. The new cubic curve changes the first boundary velocity
relative to the earlier fixed-jet witnesses. Existence of one suitable
representative also does not establish formal smoothness of the entire
incidence scheme or algebraizability of every formal curve.

The parameters \(a,b,c\) describe the credited affine base chart;
projective base charts outside it are not covered by this theorem.
Only the normal direction ranges over the whole projective line.
The result concerns rank-twelve incidence of two fourteen-row maps. It
does not supply 110-dimensional long target legs, the complete matrix
tensor \(M(10,10,11)\), a matrix-target degeneration, or a smaller
matrix multiplication exponent.
