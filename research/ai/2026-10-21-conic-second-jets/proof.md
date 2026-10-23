# Tangents and second-order compatibility at the affine conic flags

Status: written, unreviewed, computer-assisted algebra over C. No exponent
improvement, formalization, independent review, or historical priority is
claimed. The precise subject is the rank-twelve incidence of two
fourteen-row maps of a fixed 112-cubed source. This is not the full matrix
target, whose source and output requirements are substantially larger.

## 1. Source, base, and jet convention

Use the credited canonical source of `quantum-extension-spaces/extensions.py`,
with index `(i,j,z) -> (4i+j)7+z`, and all 4096 terms

```
(A(i,s,6-p-q), B(p,j,6-r-s), C(r,q,6-i-j)),  0<=i,j,p,q,r,s<=3.
```

For two 14-by112 row maps B,C let Phi(B,C) be the 112-by196 first
flattening. Let I consist of `(i,s,z)` with i,s in {1,2}, z in {0,3,6};
let K be its 100-coordinate complement. The four fixed leading rows G
are `e_(0,3,z)-e_(3,0,z)`, z in {1,2,4,5}.

Fix a,b,c in C. In the predecessor's biform bases take

```
g=(1+c*x)(1-c*y),  lx=1+a*x,  ly=1+b*y,
u=g*ly,  v=g*lx.
```

Quotient the six-dimensional U and V spaces by u and v respectively,
and tensor both quotient maps with the two-dimensional auxiliary space.
Lifting the resulting ten rows to the raw 16-dimensional boundary and
prepending G gives B0,C0. `model.base()` rebuilds these maps from the
predecessor's pinned basis changes; no ignored discovery output is read.
Both row pivot minors on the raw 16 boundary coordinates with the first
two omitted have determinant identically one. Phi0 is zero on K, and its
I rows W have an invertible constant 12-column minor. In particular all
these statements hold at special a,b,c, without genericity conditions.

Write B(t)=B0+t*B1+t^2*B2 and similarly for C, without factorials. A
rank-twelve two-jet means that the Schur complement of Phi with respect
to this 12-column minor vanishes modulo t^3. This permits the first-source
kernel to move. A normal class means a first tangent modulo the boundary
family defined below. N1,N2 are the explicit normalized lifts exported in
`witnesses.json.gz`. They agree with the two conic normal directions,
after subtracting plane directions. Their first flattening derivatives
vanish on **all 112** source coordinates, not just K. They are indexed by
the middle short coordinate 1 or 2; write a class as lambda*N2+mu*N1.

## 2. The boundary family has dimension 68

Let P3 be the four-dimensional space of polynomials of degree at most3.
Choose three independently moving two-planes UA,UB,UC in P3. For a plane
U put V(U)=ann(Sym^2 U) in the reversed coefficient pairing with the
seven-dimensional polynomial space of degree at most6. This is a
four-plane: the three products of a basis of U are independent, since a
nonconstant rational function cannot satisfy a nonzero constant
quadratic polynomial. Form the two sixteen-dimensional spaces

```
B16 = UA tensor UC tensor V(UB),
C16 = UB tensor UA tensor V(UC).
```

The C row coordinate convention swaps the two short slots relative to B.
Choose a fourteen-plane inside each sixteen-plane. In the source
contraction, the first short i slot factors through P3/UC, and its short
s slot factors through P3/UB: substitution of a vector in UC or UB makes
one long-slot pairing vanish. The first long slot factors through the
three products Sym^2 UA. Thus the first flattening has dimension at most
2*2*3=12 for every such choice.

Each short factor support of a fourteen-plane is the entire corresponding
two-plane, since loss of one short dimension would leave at most eight
rows. Its long factor support is the entire four-plane, since loss of
one long dimension would leave at most twelve rows. Consequently the
short supports recover UA,UB,UC from the pair. On the open support-rank
charts this recovery is regular. The parameterization is therefore an
immersion near our point. Its dimension is

```
3*dim Gr(2,4) + 2*dim Gr(14,16) = 12+56 = 68.
```

At the base all three planes are span{1,t^3}. `model.geometry()`
differentiates their graphs and V(U)'s annihilator equations to produce
all twelve plane fields. The other 56 fields vary the two missing
boundary rows independently in each of the fourteen rows on each leg.
The earlier common-plane model had only sixty base fields. It does not
suffice to establish necessity of a curvature condition.

## 3. Completeness of the tangent calculation

Fix the two GL14 row gauges using the determinant-one pivot minors.
There remain 2*14*(112-14)=2744 row variables. The linearized Schur
complement splits by source long degree into three disjoint blocks:

| Block | Row variables | First constant eliminations | Further constant-unit pivots | Kernel dimension |
| --- | ---: | ---: | ---: | ---: |
| Pure boundary, long degrees 0,3,6 | 1176 | 720 | 392 | 64 |
| Middle short 1, long degrees 2,5 | 784 | 560 | 221 | 3 |
| Middle short 2, long degrees 1,4 | 784 | 560 | 221 | 3 |

These are complete blocks: the two gauges remove only raw endpoint/LONG
coordinates; every other source row coordinate belongs to exactly one
listed block. All 100 source coordinates and all 196 output pairs are
included. `model.sector()` constructs the operators by contracting the
4096 terms, projects out W using its invertible minor, and eliminates
only constant invertible leading blocks. `unit_eliminate` then performs
polynomial row operations whose divisors are nonzero rational constants.
No a,b,c value is excluded. Every remaining coefficient row vanishes.
The compressed certificates contain the full polynomial kernels,
reduced matrices, and every chosen unit pivot.

The 64-dimensional boundary kernel is identified coefficientwise with
the 56 internal fields and the eight UB,UC plane fields by an invertible
constant-determinant change of basis. Each three-dimensional middle
kernel is identified with its two UA plane fields and Ni, also by a
constant-determinant change of basis. The determinants and full
identifications are replayed, not inferred from a numerical rank. Thus
at every affine base the full row-gauged tangent dimension is 70,
exactly the 68 boundary fields plus N1,N2.

## 4. Complete curvature quotient

Given boundary velocity w and normal velocity n, subtract the second jet
of an actual curve in the smooth boundary family with velocity w. Its
pure boundary-square curvature is thereby accounted for. Phi_N is
identically zero, so the kernel-motion cross term involving Phi_N is
zero. The remaining second equation, modulo the complete second-row
operator and the moving first-source kernel, consists of the normal
square and its bilinear cross term with all 68 boundary fields. The
mixed N1,N2 quadratic contraction on K is identically zero.

Both relevant source long-residue sectors are included. For each, the
784 arbitrary relevant second row coefficients are reduced using the
560 constant leading eliminations and 221 constant-unit pivots. The
result has 324 distinct equations in two blocks of 68 base coefficients
and one square column. These are exactly the two exported 324-by137
cohomology matrices. Other second row coordinates belong to the other
residue blocks and cannot change either of these equations. Conversely,
when both systems are soluble, reconstruction through the pivot
operations supplies the required relevant second row coefficients;
the remaining sectors are supplied by the boundary curve.

On the chart lambda=1, mu=d with d nonzero, combine the two systems,
scaling their square columns by 1 and d^2. This gives a 648-by69 system
for the same 68 boundary velocities. Forty-nine row pivots are units in
Q[a,b,c,d,d^-1]; no a,b,c expression is inverted. Every remaining
coefficient row is zero. Every residual is divisible by

```
F=(a-c)*(b+c)*(c+d^3),
```

and an actual residual is -F/d. Hence the residual ideal is
exactly (F), with multiplicity, rather than merely having the same zero
set. The replay checks both ideal containments explicitly, along with
all permitted divisors.

The pure fibers are checked separately, since Laurent pivots cannot be
specialized blindly to d=0. For pure N2 its own-sector base-velocity
block is identically zero and its square residual ideal is
`(c*(a-c)*(b+c))`. For pure N1 the analogous ideal is
`((a-c)*(b+c))`. In each case every residual is a polynomial multiple of
the generator and one is its positive or negative. In the opposite
sector the square term is zero, and w=0 solves it when the own-sector
square is zero. These cases and the mixed chart cover P1. Rescaling
t by a nonzero lambda or mu preserves two-jet existence. We conclude:

**For every a,b,c in C and every nonzero [lambda:mu], some first tangent
with that normal class extends to a rank-twelve two-jet if and only if**

```
(a-c)*(b+c)*(c*lambda^3+mu^3)=0.
```

This is existence after allowing a suitable boundary tangent. It is not
a claim that every representative of the class extends, or that the
base remains fixed.

## 5. Positive witnesses and the retained third-order error

On a=c or b=-c the quadratic K contraction of each Ni is zero, and their
mixed contraction is also zero. Therefore B0+t*(lambda*N_B2+mu*N_B1),
C0+t*(lambda*N_C2+mu*N_C1) preserve K exactly for all parameters.
Their ranks are fourteen near zero. These are exact linear-map curves
in the rank-twelve incidence, not full matrix-target completions.

On c=-d^3 the exported maps B0+t*B1+t^2*B2, C0+t*C1 have polynomial
coefficients in a,b,d, including d=0. B2 has 32 nonzero entries. The
56-dimensional internal boundary velocity is supported on eight B
coefficients; the C and plane velocities are zero. Direct contraction
verifies Phi1_K=0 and Phi2_K=Y2*W on all 100*196 coefficients. No
cohomology reduction is trusted for this positive check. Every map
coefficient and the moving-source correction Y2 is exported.

For this particular truncation, after the corresponding order-two
source correction, the uncorrected third Schur coefficient has 184
nonzero polynomial entries. This is a negative control against calling
the two-jet an all-order construction. Additional higher row coefficients
might cancel it; no such impossibility is proved here. The projective
base charts outside g00=lx0=ly0=1 also remain outside this package.

## 6. Attribution and consequence

The source, root flags, normal basis, biform identification and complete
projective conic classification are inherited local work, pinned in
`sources.json`; PR94 is credited for the conic. This continuation adds
the independent-three-plane boundary model, the complete affine tangent
module, the all-base-velocity second-order criterion, and the explicit
cubic-component two-jet. All code, algebra and prose were prepared with
OpenAI Codex under the repository owner's direction. Self-replay and CI
are computational checks, not independent mathematical review.

No external theorem beyond elementary polynomial and linear algebra is
imported for this continuation. In particular the earlier balanced-gap
package's Kronecker theorem is not used in this local curvature proof.
A two-jet condition does not supply later coefficients, appropriate
Laurent growth, 110-dimensional target legs, or the full matrix target.
The exponent goal remains open.
