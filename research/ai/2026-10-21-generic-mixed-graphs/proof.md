# An open set of arbitrary mixed graphs has only plane normals

Written proof, unreviewed, October 21, 2026. Claim
`AI-GENERIC-MIXED-GRAPHS-094`. This is an open-set local exclusion for the
canonical A4 leading flags, rather than a classification of every graph
or a smaller matrix multiplication exponent.

At b=1, let a and h0,...,h5 be arbitrary complex parameters. Use the
rank-one partner frames

    u_B=(a,-a,-1,1),       v_C=(a,1,a,1).

The B first space is its full maximal seven-frame. The C first space is
any five-space in its maximal seven-frame containing

    m_C(v_C)+sum_(j=0)^5 h_j*d_j,                       (1)

where d0,...,d5 are the six boundary vectors. These first spaces are the
effective quotients modulo the four leading G rows, as in claims088--093.
The C boundary four-space is
arbitrary. The h_j are constant graph parameters; epsilon denotes a
formal degeneration parameter.

**Result.** There is an explicitly defined nonempty Zariski-open set U
of the seven parameters (a,h0,...,h5) such that only the four common-plane
normal directions satisfy the necessary target conditions. U contains

    a=1,       h=(1,2,0,0,0,0).                        (2)

The prior shifted induction excludes M(10,10,11) for these first spaces
and arbitrary higher maps. A source torus transports this conclusion to
a nonempty open set on the b!=0 partner chart. No classification of the
closed complement is claimed.

## 1. Fixed necessary equations over the whole graph parameter space

Adopt claim088's complete88-dimensional full-B normal family, virtual C
correction and sixteen adapted low-rank source slices. Their correction
errors factor through Psi and vanish on the actual C first space.
The saturated target rank gap forces those sixteen adapted slices to
vanish there too. These are the same necessary conditions used in
claims090--093, with their arbitrary-boundary-four-space quantifier.

Stack Psi and those slices into seven312-by88 coefficient blocks
Z0(a),...,Z6(a), polynomial over Q[a]. For a normal vector n, the312 rows
of the resulting C-covector matrix annihilate the actual C five-space.
The actual mixed row (1) therefore gives the equations

    M(a,h)*n=0,       M=Z6+sum h_j*Zj.                 (3)

The full C-covector matrix has rank at most two, because the ambient C
frame has dimension seven and its kernel contains the five-space.
Deleting its mixed column and retaining any subset of rows preserves
this rank bound. No assumption that the selected rows uniformly span
the full obstruction is needed.

## 2. A rational32-dimensional superset and its two blocks

The certificate selects56 rows I of (3) and56 pivot columns P. Write
F for the remaining32 normal coordinates and set

    A(rho)=M(rho)[I,P],       D(rho)=det A(rho),
    K(rho)[F,:]=I32,
    K(rho)[P,:]=-A(rho)^(-1)*M(rho)[I,F],              (4)

where rho=(a,h). At (2), the exact determinant is6561. Hence D is a
nonzero polynomial, and K is defined on the open chart D!=0. Every
actual normal satisfying all312 equations (3) lies in this32-dimensional
superset. We do not need to assert that the other256 equations follow
from the selected56 away from the witness point.

The source's88 coordinates partition into two fixed44-coordinate groups.
For every a, every source-covector row has coefficients in only one
group, across all seven C columns. This is checked as an identity in
Q[a], before specializing any graph parameter. The selected56 equations
and pivot columns split28+28; the free coordinates split16+16. Thus (4)
preserves the two groups over Q(a,h0,...,h5).

Let Pi be the fixed88-by4 common-plane matrix. Its columns annihilate
all seven Z blocks and the full virtual tensor, and two columns lie in
each group. The32-by4 free-coordinate matrix Pi_F is constant. The
certificate also supplies a constant32-by28 matrix L with14 columns in
each group. Direct calculation gives

    det[Pi_F,L] = -40443431633289216 != 0.              (5)

Since M[I,:]*Pi=0 and K has an identity free block, uniqueness in (4)
gives K*Pi_F=Pi. Therefore every actual normal can be written uniquely as

    n=Pi*p+K(rho)*L*x,       x in C^28.                (6)

This is a valid quotient by the four planes throughout D!=0. It uses a
constant complement, so no additional parameter denominator is hidden
in the choice of normal coordinates.

## 3. Cubic minors of two fourteen-variable blocks

Retain the56 specified source-covector rows in the six boundary columns,
and substitute n=K*L*x. By the symbolic source partition in Section2,
the resulting matrix S(rho,x) splits vertically into two28-by6 blocks,
one in each set of14 variables. Denote them B0(rho,x0) and B1(rho,x1).
There are no cross-block coefficients. The rank bound from Section1
implies rank Bg<=2 for g=0,1.

For each block the certificate lists559 actual three-by-three minors.
Write their cubic forms as f_(g,w)(rho,xg). Define the degree-four
coefficient matrix Cg(rho) whose rows are the coefficients of

    x_j*f_(g,w)(rho,x),       j=0,...,13, w=0,...,558,   (7)

in all2380 monomials of degree four in14 variables. It has7826 rows and
2380 columns. Its entries are rational functions whose denominators
divide powers of D. Multiplying by D^3 gives polynomial coefficients,
so its maximum-rank condition is Zariski open on D!=0.

Now define the promised set precisely:

    U={rho : D(rho)!=0,
             rank C0(rho)=rank C1(rho)=2380}.          (8)

If rho lies in U and rank Bg<=2, every selected cubic minor is zero.
Consequently all forms in (7) vanish. Full column rank says they span
all quartic forms, including each x_j^4. Over C this forces every x_j=0.
Both blocks vanish in this way, so (6) leaves only the four plane normals.

## 4. Exact nonemptiness certificate

Everything in (4)--(7) specializes to rational numbers at (2). Both the
normal minor6561 and the basis determinant (5) are units modulo32003,
which is prime. Every rational coefficient denominator used by the
checker is separately checked to be a unit modulo this prime.

At this point, the559 cubic coefficient rows have rank559 in the560-
dimensional space of cubics, in each block. The checker performs exact
Gaussian elimination modulo32003 and reduces them to a basis. It then
multiplies every basis cubic by every one of the14 variables. These
products have rank2380 in the2380-dimensional quartic coefficient space,
again in each block.

The products of a cubic row basis lie in the span of (7): row operations
are scalar linear combinations, and multiplication by x_j respects such
combinations. Thus the original matrices C0,C1 have full column rank
modulo32003. Each has a maximal minor nonzero modulo32003, and that same
rational minor is nonzero over Q and C. This proves (2) lies in U. It
proves U is nonempty and hence dense in the irreducible affine parameter
space C^7. It is not an inference that all parameter values behave like
one finite experiment; the nonvanishing minors define the open set (8).

The two cubic spans are deliberately not described as all560-dimensional.
One quartic step is necessary for this certificate. Randomly sampling
4500 minors originally missed a sparse pure-cube witness in each block;
targeting its three rows and columns supplied the missing constraint.
The maintained checker replays the final witnesses and performs no
random search.

## 5. Extension to the nonzero-b chart

Adopt the verified source torus D_lambda e_(i,j,z)=lambda^(i+j+z)e_(i,j,z).
Each source tensor term has total weight18, so the torus scales the
source by the nonzero scalar lambda^18. It preserves the canonical
leading flag and the boundary modules. The maximal B and C frame
covariances are checked symbolically by this package.

For general partner parameters a,b, their mixed vector has weight7,
and the six boundary vectors have weights

    (2,5,5,8,8,11).

Consequently the transformed graph parameters are

    a'=a/lambda,       b'=b/lambda,
    h'_j=h_j*lambda^(weight_j-7).

For b!=0 take lambda=b. The normalized b'=1 parameters are

    a'=a/b,
    h'=(h0/b^5,h1/b^2,h2/b^2,b*h3,b*h4,b^4*h5).        (9)

This is a birational change of parameters on b!=0. The inverse image of
U under (9) is therefore a nonempty open set on that partner chart.
The source scalar is absorbed in the arbitrary first-leg map. The
arbitrary boundary four-space is carried to an arbitrary boundary
four-space, so the original quantifier is preserved.

## 6. All-order consequence

Use the shifted moving-plane induction of the cited third-boundary and
mixed-five-space proofs. If the first normal error from moving boundary
modules is at epsilon^N, and the first new output orders are s_B,s_C,
the off-diagonal equations appear at N+s_B and N+s_C. Earlier corrected
residues lie in the old cross and cancel in W0. At N+s_B+s_C the
double-new-output residue is the same virtual tensor whose obstruction
and sixteen slices occur in Section1. Higher source corrections and
boundary terms have zero double projection at that order.

For first data in (8), the normal lemma forces a common-plane error.
Absorb it into the moving plane and increase N. The leading first data
stay fixed during these positive-order changes, so the same normal
lemma applies at each step. Both output maps remain inside rank56
boundary modules over C((epsilon)); they cannot attain the two110-
dimensional target legs. This excludes M(10,10,11) for arbitrary later
maps, unequal delayed growth and a Laurent first-leg map, under the
stated canonical leading normalization.

## 7. The remaining exceptional geometry

Let E be the proper closed complement of U in the b=1 graph parameter
space. Fix a C five-space V and write W=V intersect boundary, dim W=4.
If m+h lies in V, the same V also contains m+h+w for every w in W.
Therefore a target construction with these first spaces would require

    {a} times (h+W) subset E.                           (10)

The obstruction applies to any representative lying in U. Thus the next
problem is to understand affine four-planes contained in the exceptional
rank-drop fibers. We do not show here that no such planes exist, nor
classify the points where the chosen normal chart fails. Earlier axis
and exceptional-point theorems retain their separate proofs.

This is a written, unreviewed open-set exclusion. Other graph strata,
smaller first spaces, other leading flags and the exponent below9/4
remain open. Finite replay and repository CI do not constitute an
independent review of the formal-induction argument.
