# A seven-by-five point stratum has only common-plane normal motion

Written proof, unreviewed, October 21, 2026. Claim
`AI-MIXED-FIVE-SPACE-POINT-087`. Work over C with the canonical leading
four-row flags and source of the preceding normal packages.

Fix the compatible rank-one mixed partners u=v=(0,0,0,1). Let the B first
quotient be its maximal seven-space and let the C first quotient be any
five-space with nonzero mixed projection. Then every matrix-target
admissible first normal error is a common-plane motion. The earlier
shifted moving-boundary induction therefore excludes M(10,10,11) on
this stratum, including arbitrary later coefficients, boundary graphs,
delayed unequal first orders, and an arbitrary Laurent first map.

This does not exclude all seven-by-five partner lines. Reversal gives
u=v=(1,0,0,0), and exchange gives the opposite five-by-seven orientation.
Neither this local exclusion nor its finite replay improves omega.

## 1. Fixed frames and virtual corrections

Use the preceding maximal frames at a=b=0. Their first six columns are
the boundary quotient vectors d1,d3,d5,d7,d9,d11 and their seventh is the
mixed vector m(e3). Write them as B7 and C7. Compatibility puts every
allowed C five-space V inside C7: the pure mixed product is zero, and
the two mixed-boundary graph contributions have disjoint source supports.
Both graph terms must lie in the full boundary annihilators, as in the
seven-frame and mixed-hyperplane proofs. Thus this parametrization omits
no boundary graph. In these coordinates V has dimension five and is not
contained in the first six coordinate directions.

The canonical first normal equations leave 228 parameters. Imposing all
B7 off-diagonal correction equations leaves a complete 88-dimensional
kernel. Parameterize it by D. Its C7 correction obstruction is a matrix

    Psi(D): C^7 -> C^200.

The necessary condition is V contained in ker Psi(D), so rank Psi(D)<=2.

Solve every B7 correction equation exactly. For C7 use a fixed partial
inverse of the rank-56 correction operator. These C corrections need
not solve the equations on all seven columns. The verifier constructs
their complete residual, jointly linear in D and a C7 input, and checks
that it is a constant linear combination of the rows of Psi(D). Thus
the corrections solve every required equation after restriction to V.
This factorization is essential; the unrestricted virtual C rows are
not asserted to be genuine corrections.

The virtual double-new-output third coefficient is

    J_D(x,b,c) = T(x,b',c)+T(x,b,c')-T(y_x,b,c),

on the 64-dimensional long source kernel K_inf and B7,C7. It is linear
in the 88 parameters. Restricting c to V gives the actual coefficient.
Different allowed correction choices have differences in the boundary
spaces. They do not change this coefficient because
T(K_inf,F_B,F_C)=0. The verifier exports all 3136-by-88 coefficients.

## 2. Three implications that do not choose the five-space

Maintain a matrix Z(D) whose rows vanish on V. Initially Z=Psi. Extra
rows will be rows of source slices of J_D already proved zero on V.
It always has seven columns, so rank Z(D)<=2.

First, perform ordinary constant rational row operations on the joint
coefficient matrix of Z. They preserve its pointwise rowspace for every
D. Subtracting such rows from each B row of a source slice of J does not
change the slice restricted to V. The verifier uses exact reduced row
echelon form in the combined (C coordinate, parameter) columns.

Second, suppose the support of such a reduced source slice is covered
by at most two B-row or C-column vertices. Its matrix rank is at most
two for every D, before and after restricting to V. The actual terminal
coefficient is this slice plus the old four-row/four-column cross. That
cross has maximum rank eight. The saturated limit is R plus W0, where
R is the target slice space Mat10 tensor I11 and W0 lies in the old
cross. If a slice has rank at most two, its R component consequently
has rank at most ten. A nonzero element of R has rank at least eleven.
The R component is zero; double projection then makes the slice zero.
Its raw rows can be added to Z. The saved certificate gives an explicit
cover of size one or two for each added source slice.

Third, every three-by-three minor of Z(D) vanishes. The certificate uses
only triangular minors with diagonal entries c1*L(D), c2*L(D), c3*L(D),
where the ci are nonzero rational numbers. Their determinants are
c1*c2*c3*L(D)^3. Hence L(D)=0 over C. All positions, forms, scales and
kernel substitutions are exported and checked exactly.

There is one further linear implication from mixedness. If a row of Z
is (0,0,0,0,0,0,L(D)), it annihilates V. Some vector of V has nonzero
seventh coordinate, so L(D)=0. This implication does not require a
specified mixed vector or a chosen basis for V.

## 3. Complete finite elimination

Apply those implications repeatedly. Each kernel is the complete exact
kernel of the forced linear forms; none is selected by sampling.
The normal dimensions are

    88, 68, 54, 30, 18, 12, 4.

Initially the sixteen source rows with short first index 2 and long
index 1,2,4,5 have small support. Further reductions expose more such
rows. After reaching twelve parameters, the final four source indices
36,37,39,40 also acquire covers of size at most two and vanish on V.
The certificate adds 32 source slices in total. At the end Z and the
reduced virtual third tensor are identically zero. The final normal
basis has rank four and its joint span with the independently known
four common-plane directions also has rank four. This proves equality
with that plane kernel, for every admissible complex V.

The earlier exploratory reduction to thirty parameters had not yet
used mixedness. Its four surviving source components were intermediate
residues, not surviving target candidates. They are eliminated here.

## 4. Shifted orders and output rank

Adopt the order argument of the third-boundary proof, Section 6. At the
first normal error t^N D from a moving boundary, the B and C equations
above occur at N+s_B and N+s_C. Until N+s_B+s_C, corrected residues lie
in the old cross and can be canceled in W0. At that terminal order the
double projection is exactly J_D restricted to the first spaces. Higher
source corrections, derivatives of the moving kernel, and boundary
parts have zero double projection there. This argument applies to any
first subspaces inside F_B,F_C, including the mixed frames used here.

The elimination therefore applies at every induction step, for unequal
positive s_B,s_C as well as ordinary first order. Absorb the resulting
common-plane error into the moving plane and increase the order. Both
regular output maps remain in rank-56 boundary modules over C((t)).
Their ranks cannot reach the two 110-dimensional target legs, even with
a Laurent first map. This proves the stated point-stratum exclusion.

The adopted source identities and shifted-order argument are not new
discoveries of this package. The new work is the five-space elimination
and its explicit certificates. Independent mathematical review and a
uniform argument for all rank-one partner lines remain open.
