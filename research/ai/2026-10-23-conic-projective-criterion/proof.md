# The complete projective conic normal-class criterion

## Claim and scope

**AI-CONIC-PROJECTIVE-CRITERION-001.** Work over \(\mathbb C\). Consider the conic product-quotient boundary base parameterized by

\[
([r:s],[a_0:a_1],[b_0:b_1])\in(\mathbb P^1)^3.
\]

The literal source, the four fixed rows \(G\), and the first-leg coordinate
kernel are those of the credited conic second-jet theorem, PR101. Every point
of this projective base has leading row ranks \(14,14\), first flattening rank
\(12\), and a two-dimensional normal quotient to the smooth boundary family.
Define its normal basis \(N_1,N_2\) in (5) below.

For a **nonzero** projective normal class
\([\lambda:\mu]\), meaning \(\lambda N_2+\mu N_1\), the following are equivalent:

1. Some first tangent with this normal class admits a second jet in the full
   moving-kernel rank-twelve incidence.
2. Some such tangent extends to a formal curve in that incidence.
3. Some such tangent extends to exact polynomial coefficient maps with the
   original coordinate kernel fixed, and with unit constant rank minors.
4. The homogeneous equation

   \[
   \boxed{(a_1r-a_0s)(b_1r+b_0s)(s\lambda^3+r\mu^3)=0}
   \tag{1}
   \]

   holds.

The first boundary velocity is free in this statement. The theorem neither
prescribes the complete first jet nor asserts that every higher jet with this
normal class extends. In particular it does not alter the separate obstruction
for a prescribed complete third jet. Polynomial maps are polynomial germs at
\(t=0\); the minors are units in \(\mathbb C[[t]]\). No assertion about every
finite nonzero value of \(t\) is needed.

The affine case \(r=a_0=b_0=1\) is credited to PR101 and the all-order
polynomial-curve package in PR136. The new content is completeness at all
missing projective base points, the explicit transition of the normal class,
and exact polynomial curves there. All work is written and computationally
replayed; it is not independently mathematically reviewed or Lean formalized.

## 1. Literal source and homogeneous leading frames

Write \(I(i,j,z)=28i+7j+z\). The source contains all 4096 terms

\[
\sum_{i,j,p,q,r',s'=0}^3
 e_{I(i,s',6-p-q)}\otimes e_{I(p,j,6-r'-s')}
 \otimes e_{I(r',q,6-i-j)}.
\tag{2}
\]

The prime marks in this sum distinguish the summation indices from the
homogeneous base coordinates. Let

\[
A_0=\{I(i,j,z):i,j\in\{1,2\},\ z\in\{0,3,6\}\},\qquad
K=\{0,\ldots,111\}\setminus A_0.
\]

There are twelve leading source coordinates and one hundred kernel
coordinates. The four common rows are
\(G_z=e_{I(0,3,z)}-e_{I(3,0,z)}\), for \(z=1,2,4,5\).

Set

\[
\begin{split}
u&=(a_1r,-a_1s,a_0r,-a_0s)^T,\\
v&=(-b_1r,b_0r,b_1s,-b_0s)^T,\\
\Delta&=(a_1r-a_0s)(b_1r+b_0s).
\end{split}
\tag{3}
\]

Then \(u^Tv=-\Delta\). Both \(u\) and \(v\) are nonzero at every projective
base point. Define seven-dimensional row hyperplanes in eight coordinates by
the kernel lines

\[
\ker\overline U=\langle(rv,-sv)\rangle,\qquad
\ker\overline V=\langle(ru,-su)\rangle.
\]

The first four coordinates represent the coefficient of \(x^0\), and the last
four the coefficient of \(x^3\). Thus their seven-by-four polynomial cores are
\(U_0(x)=U_{00}+x^3U_{03}\) and \(V_0(x)=V_{00}+x^3V_{03}\).

These formulas identify the homogeneous continuation of the preceding biform
base
\(g=(r x_0+s x_1)(r y_0-s y_1)\), with residual forms
\(a_0x_0+a_1x_1\) and \(b_0y_0+b_1y_1\). The acceptance program compares both
complete affine frames and both normals to the byte-pinned PR101 maps by row
changes of determinant one. The biform and hyperplane parameterizations are
regular on the whole product of projective lines: the kernel vector is never
zero, and the unit frames below give local regular lifts. Their equality on
the dense affine chart therefore identifies the base everywhere. This
identification alone is not used to extend the obstruction calculation;
Sections 3 and 4 check the missing tangent and curvature cases.

Here is an explicit frame construction without a hidden chart denominator.
Normalize either \(r=1\) or \(s=1\), and normalize either coordinate of each
residual line to one. The eight-coordinate kernel then has a component
\(w_p=\pm1\). For every \(j\ne p\), take
\(e_j-(w_j/w_p)e_p\). These seven rows have a unit minor. Replace two of them
by the two constant \(G\) cores, using a constant two-by-two minor equal to
\(\pm1\). The new seven-by-seven minor remains \(\pm1\). The two \(G\) cores
annihilate the kernel identically, including \(r=0\) and either residual point
at infinity.

For a core component \(2j+r'\), embed its coefficient of \(x^p\) by

\[
\begin{split}
B[2\ell+\epsilon,I(p,3j,4-3r'+\epsilon)]
  &=[x^p]U[\ell,2j+r'],\\
C[2m+\epsilon,I(3r',p,4-3j+\epsilon)]
  &=[x^p]V[m,2j+r'],
\end{split}
\tag{4}
\]

where \(j,r',\epsilon\in\{0,1\}\). All unlisted entries are zero. This doubles
the seven-row frame by the two parities, yielding unit fourteen-row minors.
The first four rows are exactly \(G\).

Substitution in (2) makes the two core labels agree. The first short
coordinates are \(2-\epsilon_C,2-\epsilon_B\), and the first long coordinate is
six minus the exponent of \(x\) in \(UV^T\). Thus a product supported only in
\(x\)-degrees \(0,3,6\) has every coefficient on \(K\) zero. The leading
product has that support. The \(G\times G\) block supplies a constant
twelve-by-twelve minor of determinant \(-1\), so its rank is exactly twelve.
This proves the required leading ranks at infinity, without a limiting-rank
assumption.

## 2. Normal coordinates and rescaling

Define column vectors \(A,D\) locally by

\[
A=U_{03}v/r=U_{00}v/s,\qquad
D=V_{03}u/r=V_{00}u/s,
\]

using only the expression with the normalized nonzero denominator. The kernel
relations show that these definitions agree on the overlap and give

\[
U_0v=(s+rx^3)A,\qquad V_0u=(s+rx^3)D.
\]

Neither \(A\) nor \(D\) is zero: otherwise the relevant eight-column frame
would annihilate two independent vectors instead of its single kernel line.
For \(i=1,2\), define the literal map pairs

\[
N_i:\quad U_i=x^iAu^T,\qquad V_i=-x^iDv^T.
\tag{5}
\]

Their complete first product derivative is zero. Sections 3 and 4 prove that
they are a basis of the normal quotient at every point; nonzero entries alone
would not prove that assertion.

Rescaling \((r,s)\) by \(\tau\), the first residual form by \(\alpha\), and the
second by \(\beta\) scales both normals by the same factor
\(\tau\alpha\beta\), up to the common changes of row frames. Indeed \(u,v\)
scale by \(\tau\alpha,\tau\beta\), while \(A,D\) scale by \(\beta,\alpha\).
Consequently \([\lambda:\mu]\) is a well-defined projective coordinate on
these two normal directions under residual-chart normalizations. Equation
(1) is homogeneous, so its zero set does not depend on any of these choices.

## 3. Complete calculation when r is nonzero

Normalize \(r=1\) and put \(c=s\). The following four disjoint residual strata
cover both projective residual lines; no nonzero residual value is excluded:

| Stratum | \((a_0,a_1)\) | \((b_0,b_1)\) | \(\Delta\) |
| --- | --- | --- | --- |
| finite | \((1,a)\) | \((1,b)\) | \((a-c)(b+c)\) |
| a infinity | \((0,1)\) | \((1,b)\) | \(b+c\) |
| b infinity | \((1,a)\) | \((0,1)\) | \(a-c\) |
| both infinity | \((0,1)\) | \((0,1)\) | \(1\) |

The finite stratum is the credited complete PR101 calculation, transported by
the verified unit row changes. For each of the other three strata, the saved
certificate and acceptance program rebuild the **complete** row-gauged first
operator from (2). They do not restrict the fourteen output rows to the core
ansatz. The source projection uses the constant twelve-row \(G\times G\) minor.

As in PR101, the pure boundary sector has 1176 unknowns and 720 constant
leading eliminations. Each middle sector has 784 unknowns and 560 constant
leading eliminations. All remaining pivots are rational nonzero constants.
The resulting kernel dimensions are \(64,3,3\). In the middle sectors the
three displayed fields are two plane motions and \(N_i\); in the pure sector
they are the 56 row motions inside the boundary spaces and the eight other
plane motions. Their changes from the computed kernel bases have constant
unit determinants. Thus the total tangent dimension is 70 and its boundary
subspace has dimension 68 on each missing stratum.

The boundary family is the same smooth family of three two-planes and two
fourteen-planes in their sixteen-dimensional boundary spaces used in PR101.
The plane tangent fields are recomputed in the new frames. Its 68 independent
tangents are therefore integrable boundary directions, including at the
residual points at infinity.

Next the acceptance program rebuilds the full two middle curvature quotients,
including all 68 boundary first velocities and all second-map coefficients.
For \(\lambda\mu\ne0\), normalize \([\lambda:\mu]=[1:d]\). On \(d\ne0\),
the combined compatibility matrix has 49 pivots, each a rational nonzero
constant times a power of \(d\). Every remaining coefficient of a boundary
velocity is zero. The residual ideals are exactly

\[
\begin{array}{c|c}
\text{stratum}&\text{mixed residual ideal generator}\\ \hline
a\text{ infinity}&(b+c)(c+d^3)\\
b\text{ infinity}&(a-c)(c+d^3)\\
\text{both infinity}&c+d^3.
\end{array}
\tag{6}
\]

These are ideal equalities, rather than radical or generic-rank conclusions.
Every residual is its stated generator times a Laurent polynomial, and at
least one quotient is a Laurent unit. The exported operations and both
containments are exactly replayed.

The pure classes are checked separately without inverting \(d\). Their
residual ideals are \((\Delta)\) for \(N_1\), and \((c\Delta)\) for \(N_2\).
The relevant own boundary-velocity block is zero; the opposite square block
vanishes with zero opposite velocity. Hence all projective normal directions,
including \(\lambda=0\) and \(\mu=0\), give exactly

\[
\Delta(c\lambda^3+\mu^3)=0.
\tag{7}
\]

The pinned PR101 quotient construction eliminates the complete moving-kernel
coefficient by its unit output minor. It also accounts for the quadratic
boundary contribution through the smooth boundary family. Using it with the
new complete tangent bases therefore proves necessity for arbitrary second
maps and arbitrary kernel motion, not only for the later explicit curves.

## 4. The conic chart at infinity

Consider the coordinate reversal on every source leg,

\[
R:I(i,j,z)\longmapsto I(3-i,3-j,6-z).
\tag{8}
\]

Changing all six summation indices in (2) by \(q\mapsto3-q\) proves that
\(R\otimes R\otimes R\) permutes the 4096 source terms. It preserves \(A_0\)
and \(K\), and takes the span of \(G\) to itself. Its action on the homogeneous
base is

\[
([r:s],[a_0:a_1],[b_0:b_1])
\longmapsto([s:r],[a_1:a_0],[b_1:b_0]).
\tag{9}
\]

Let \(J\) reverse the four component labels. In core notation, with the
two parity rows interchanged, the transformed leading cores are
\(x^3U_0(1/x)J\) and \(x^3V_0(1/x)J\). The transformed homogeneous vectors obey
\(u'=-Ju\), \(v'=Jv\), \(A'=A\), \(D'=-D\), before the harmless row changes.
Consequently

\[
R(N_1)=-N'_2,\qquad R(N_2)=-N'_1,
\qquad [\lambda:\mu]\longmapsto[\mu:\lambda].
\tag{10}
\]

The acceptance program checks (8) as a literal permutation and (10) on every
entry of both complete maps. For every residual stratum it also computes the
row changes to normalized frames in the other conic chart and proves their
determinants are \(\pm1\). There is no inversion of the conic coordinate.
In particular this comparison remains valid at \(r=0\).

Under (9), \(\Delta'=-\Delta\), while
\(s'\mu^3+r'\lambda^3=r\mu^3+s\lambda^3\). Equation (1) is therefore
preserved. Every point with \(r=0\) is carried to the already checked
\(r'=1,s'=0\) chart with some residual projective points. All four such
residual possibilities were included in Section 3. The complete tangent
basis, unit leading ranks and full second-jet criterion transport under this
source symmetry. This proves necessity and the normal-quotient assertion on
the remaining conic chart.

In particular, at \([r:s]=[0:1]\),
\(\Delta=-a_0b_0\). If both residual coordinates \(a_0,b_0\) are nonzero,
exactly the pure class \(N_1\), or \([\lambda:\mu]=[0:1]\), survives. If either
residual point is at infinity, \(\Delta=0\) and every normal class survives.
There is no extra component caused by a loss of the leading rank.

More precisely, the set of liftable projective normal classes has exactly
three irreducible components. The first two are the graphs
\([a_0:a_1]=[r:s]\) and \([b_0:b_1]=[r:-s]\). The third is
\([r:s]=[\lambda^3:-\mu^3]\), with the two residual lines free. Each is a
product of three projective lines under its graph parameterization. This is
a statement about the set of liftable classes; it does not assert a scheme
structure for the full incidence. On the third component the map to the
conic parameter is a degree-three map, with the two pure normal fibers at
\(r=0\) and \(s=0\).

## 5. Exact polynomial curves

The following formulas prove sufficiency directly. They are embedded by (4),
and every coefficient map of the mixed and conic-infinity formulas is saved.
The acceptance program independently contracts every product coefficient
against all 4096 terms of (2).

### The two linear factors

At any projective base with \(\Delta=0\), let
\(h=\lambda x^2+\mu x\). Then

\[
U=U_0+t h Au^T,\qquad V=V_0-t h Dv^T
\tag{11}
\]

is exact. Its first cross term is zero by (5); its quadratic term is
\(\Delta t^2h^2AD^T=0\). Thus \(UV^T=U_0V_0^T\), for every nonzero normal
class, including the intersection of the two linear factors.

### The cubic factor at r nonzero

Normalize \(r=1\). If \(c\lambda^3+\mu^3=0\), then \(\lambda\ne0\), so set
\(d=\mu/\lambda\), \(c=-d^3\), and use the class \([1:d]\). This includes
\(d=0\). Put

\[
\rho=d+\Delta t,\qquad P_z=x^2+zx+z^2,
\qquad \beta=3d^2t+3d\Delta t^2+\Delta^2t^3.
\]

Define

\[
\begin{split}
U&=U_0+tP_dAu^T,\\
V_b&=V_0+\beta Dv^T,\\
V&=V_b-tP_\rho Dv^T.
\end{split}
\tag{12}
\]

All coefficients are polynomials in the residual parameters, \(d\), and
\(t\). The notation \(\beta\) does not divide by \(\Delta\): the displayed
polynomial satisfies \(\Delta\beta=\rho^3-d^3\). Therefore

\[
U_0v=(x^3-d^3)A,\qquad V_bu=(x^3-\rho^3)D.
\]

Expansion of the two rank-one corrections gives

\[
UV^T-U_0V_b^T
=AD^T P_dP_\rho\{t(d-\rho)+t^2\Delta\}=0.
\tag{13}
\]

Both \(U_0\) and \(V_b\) have only \(x\)-degrees zero and three. Hence the
source kernel remains fixed at every order. The nonboundary parts of the
first coefficients are exactly \((x^2+dx)Au^T\) and
\(-(x^2+dx)Dv^T\), so the normal class is \([1:d]\). Their constant terms are
allowed boundary velocities. There is no guard on either residual parameter,
\(d\), or \(\Delta\).

The cubic terms of \(V\) cancel. Equivalently, its complete literal formula is

\[
V=V_0+t(2d^2-dx-x^2)Dv^T+\Delta t^2(d-x)Dv^T.
\tag{12a}
\]

Thus all four finite mixed families have degrees \((1,2)\) in \(t\).
This choice of a boundary velocity uses \(v\) itself, so it does not need a
residual coordinate to be nonzero.

### The cubic factor at r zero

Normalize \(r=0,s=1\). If \(\Delta\ne0\), equation (1) forces
\([\lambda:\mu]=[0:1]\). Here \(U_0v=A\) and \(V_0u=D\). Use

\[
U=U_0+t x Au^T,\qquad
V=V_0-t x Dv^T-\Delta t^2x^2Dv^T.
\tag{14}
\]

The terms of orders one and two cancel exactly, and

\[
UV^T=U_0V_0^T+\Delta^2t^3x^3AD^T.
\tag{15}
\]

The remaining term has allowed degree three, so the fixed source kernel is
again exact. Formula (14) is also valid at \(\Delta=0\); formula (11) supplies
all other normal classes there.

The leading maps of (11), (12) and (14) are the unit frames already proved.
Their minors thus have nonzero constant terms, and the displayed normal
classes are nonzero. Rescaling \(t\) realizes any nonzero scalar
representative of the projective normal direction. Exact polynomial germs
give formal curves; truncation gives second jets. Sections 3 and 4 give the
opposite implication, completing the equivalence.

## 6. Evidence and limits

`certificates.json.gz` records the three complete missing-stratum tangent
calculations, both curvature quotients per stratum, all unit eliminations,
and both containments for each residual ideal. `curves.json.gz` records all
four finite mixed families and all four conic-infinity families as literal
coefficient maps. The acceptance program rebuilds the former from the pinned
full source operator and checks the latter with a separate literal contraction
loop. It imports no curve constructor.

The source records pin the exact PR101 proof, model, verifier and results,
their biform predecessors, and the credited PR136 affine gauge proof. The
projective closure is proved only for this conic base and its two-dimensional
normal quotient. No matrix multiplication target, global incidence-component
classification, or exponent improvement follows from this theorem alone.
