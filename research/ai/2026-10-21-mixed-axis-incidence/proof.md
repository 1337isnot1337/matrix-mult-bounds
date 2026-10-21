# Closing a mixed-row axis by an auxiliary projection

Written proof, unreviewed, October 21, 2026. Claim
`AI-MIXED-AXIS-CLOSURE-092`. This extends claim091, whose ten-dimensional
necessary family was left unresolved. No matrix multiplication exponent
improvement or historical priority is claimed.

Work over C with the canonical A4 leading flags and rank-one partners
u_B=(a,-a,-1,1), v_C=(a,1,a,1). The B first space is the full maximal
seven-frame. The C first space is any five-dimensional subspace of its
maximal seven-frame containing m+t*d0, where d0 is its first boundary
vector. Here a is arbitrary and t is nonzero. The symbol t denotes the
constant graph parameter; use epsilon for the formal degeneration.

**Result.** Only the four common-plane normal directions satisfy the
necessary target conditions. The shifted moving-plane induction therefore
excludes the target M(10,10,11) on this axis, for arbitrary higher maps,
including delayed unequal first growth and a Laurent map on the source
leg, under the same canonical leading normalization as claims088/091.
The t=0 case is the prior pure-row theorem089. The four-dimensional
boundary part of the C five-space remains arbitrary throughout.

## 1. Import only the certified necessary family

Adopt claim091's complete normal kernel of dimension32, its four plane
directions, and its constant28-dimensional quotient. Let d denote those
quotient coordinates. Stack the C obstruction and the sixteen necessary
vanishing adapted source slices into Z(d). Every row annihilates the
actual C five-space, so rank Z(d) is at most two. Its mixed column is zero.

The selected56 rows S(d) are rows of this obstruction; their spanning
the whole rowspace is not needed. Claim091 proves that rank S(d)<=2
forces W(d)=0. Its complete Laurent kernel is K_W, of size28-by10, for
every a and t!=0. Hence write d=K_W*x, with x in C^10. All identities
below are reconstructed from this original source and this same K_W.

## 2. Two identical blocks

The six boundary columns of S(K_W*x) split into two disjoint row blocks.
The first25-row block depends only on (x0,x2,x3,x4,x5), and the second
only on (x1,x6,x7,x8,x9). Six additional rows vanish. After the saved
row permutation the two25-by6 matrix pencils are identical. The verifier
checks every coefficient, including all cross-block zeros.

It suffices to show that the first block, denoted B(z) for z in C^5,
can have rank at most two only if z1=z2=z3=z4=0. Apply the same conclusion
to the second block. This would leave only x0 and x1.

## 3. A projection with no exceptional parameter pairs

Fix any a,t in C with t!=0. Put u=a^3 and extend scalars to C(ell), with
ell an independent indeterminate. Write the columns of B as
(E0,O0,E1,O1,E2,O2) and form

    R_ell(z) = t^3*(O0-ell*E0, O1-ell*E1, O2-ell*E2).

Let P be its25-by15 joint coefficient matrix, with coordinate order
5*j+i for the coefficient z_i in projected column j. Every coefficient
is polynomial in u,t,ell. The verifier checks the substitution u=a^3
against the complete reconstructed pencil; no a-th roots are chosen.

The saved13-by13 minor has determinant

    t^30*(u-ell)^3*(ell+1)*(-ell+t-1)*F2*F3*D/4,

where

    F2 = 4*ell^2-2*ell*t-4*ell*u+4*ell+t^2+2*t*u-4*u,
    F3 = 8*ell^3+4*ell^2*t-12*ell^2*u+12*ell^2
         -3*ell*t^2+8*ell*t+4*ell*u^2-16*ell*u+4*ell
         +3*t^2*u-2*t*u^2-4*t*u+2*t+4*u^2-4*u,
    D  = ell^2*(t*u-t-u^2+2*u)
         +ell*(-2*t*u^2+3*t*u-2*t+2*u^3-5*u^2+3*u)
         +t*u^3-2*t*u^2+3*t*u-t-u^4+3*u^3-3*u^2.

The determinant is recomputed exactly, not inferred from specializations.
The linear factors and F2,F3 have nonzero constant leading coefficients
in ell. For D put A=[ell^2]D and B=[ell]D. Direct identities give

    (u-1)*B-(-2*u^2+3*u-2)*A = u,       A at u=0 = -t.

If D vanished identically in ell, A=B=0 would force u=0 and then t=0.
That contradicts the hypothesis. Thus the displayed minor is a nonzero
element of C(ell) for EVERY fixed u and t!=0. In particular, this is
not a generic-parameter rank assertion with exceptional pairs omitted.

## 4. The complete relation space and its rank-one locus

The polynomial15-by2 matrix N in certificate.json satisfies P*N=0.
Reshape its columns into5-by3 matrices H0,H1 by H_k[i,j]=N[5*j+i,k].
Their normalization is

    H0 = [(u-ell-1,1,0); (0,0,0); (0,0,0); (0,0,0); (0,0,0)],
    H1[0,1]=0,                  H1[4,2]=-D.

Since D is nonzero in C(ell), N has two independent columns. Along
with the13-minor, this proves rank P=13 and ker P=span(N) at every
allowed fixed parameter pair.

Let Delta13 and Delta23 be the two-by-two minors of H1 in columns0,1
and rows1,3 and2,3 respectively (indices start at zero). Exact expansion
gives the particularly short certificate

    (Delta13+Delta23) at ell=u = t^3.

Therefore the lower four rows of H1 have rank at least two over C(ell).
If alpha*H0+beta*H1 has rank at most one, its lower minors are beta^2
times those of H1. Their nonvanishing forces beta=0. Its lower four rows
then vanish. This classifies all rank-one elements of ker P, including
parameters where any one chosen minor or determinant factor vanishes
at some particular numerical ell.

Now suppose z!=0 and rank B(z)<=2. The projected25-by3 matrix R_ell(z)
has a nonzero right kernel vector y in C(ell)^3. The coefficient vector
with entries z_i*y_j lies in ker P. Reshaping it gives the nonzero
rank-one matrix z*y^T. By the preceding paragraph its lower four rows
vanish. Since y!=0, z1=z2=z3=z4=0. For z=0 the same conclusion is
immediate. This proves the assertion required in Section2.

## 5. The two remaining normal coordinates

Substitute x=(x0,x1,0,...,0) into the six boundary columns of S. Two
explicit triangular three-by-three minors, in the ordered diagonal
positions below, have determinants -x1^3 and -x0^3:

    [(37,1),(28,5),(30,4)],     [(40,1),(32,5),(34,4)].

Each ordered diagonal has coefficients (-1,1,1), and every entry above
that ordered diagonal vanishes. These assertions are checked as identities
in the original matrix, with no division by a or any nonconstant
polynomial in a. Rank S<=2 forces x0=x1=0 over C. The complete normal
dimensions, restoring the four plane directions, are consequently

    32 -> 14 -> 6 -> 4,       quotient dimensions 28 -> 10 -> 2 -> 0.

## 6. All-order consequence and scope

Use the shifted induction in the third-boundary proof, as already
specialized to mixed first spaces in the cited five-space proofs. At the
first normal error epsilon^N from moving boundary modules, the two
off-diagonal equations occur at N+s_B and N+s_C. Before N+s_B+s_C their
corrected residues lie in the old cross and can be canceled in W0. At
N+s_B+s_C the double-new-output residue is the virtual tensor of claim088
restricted to the actual first spaces. Higher source-row corrections
and boundary terms have zero double projection at that order. Its
adapted source slices and obstruction therefore obey the necessary
conditions used in Section1.

The normal calculation forces a common-plane error at every induction
step. Absorb that error into the moving plane and increase N. Both
output maps remain inside rank56 boundary modules over C((epsilon));
they cannot attain the target's two110-dimensional legs. This uses the
prior saturated target rank gap, rather than replacing a formal argument
by a bounded jet calculation.

This closes only the axis m+t*d0 on the b=1 partner chart, together with
its t=0 endpoint by claim089. It does not classify all graph rows,
the fifteen two-coordinate graph charts, other partner strata, smaller
first spaces, or other leading flags. Those questions remain open.

## 7. Discovery versus acceptance

Singular syzygies suggested N; early rational elimination introduced
parameter-dependent denominators and was not used for acceptance. The
maintained verifier uses only SymPy with the root dependencies. It
reconstructs the source coefficients, checks P*N=0, computes the exact
minor, verifies its nonvanishing certificate, and checks the two lower
minors and the final cubics. Neither Singular nor a floating-point
calculation is required to replay the result. This is same-session
verification, not independent mathematical review.
