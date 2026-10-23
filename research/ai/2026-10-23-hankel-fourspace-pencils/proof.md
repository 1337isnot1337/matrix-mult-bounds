# Tangent jumps and exact extensions of A10 four-space pencils

October 23, 2026. Written proof, unreviewed. Work over C. No independent
mathematical review, formalization, historical priority or exponent gain
is claimed. This continues the prescribed-pencil result of
[PR120 at ee0bdaa](https://github.com/1337isnot1337/matrix-mult-bounds/tree/ee0bdaa49810aebfe7a29e8acb27097df09aa68f/research/ai/2026-10-23-hankel-index-sharpness).
The calculations below are self-contained and do not assume a general
classification of quadratic Hankel pencils.

## 1. The four-space and arbitrary line parameters

Let S be the vector space of 10-by-10 Hankel matrices with moments

    h_3=A, h_7=B, h_11=C, h_15=D,

all other moments zero. Grouping rows by residue alpha modulo four and
columns by residue `3-alpha` gives two copies each of

    K=[[A,B],[B,C],[C,D]]

and its transpose. Thus every matrix in S has rank at most eight. The
three quadratic expressions

    Q_0=BD-C^2,  Q_1=BC-AD,  Q_2=AC-B^2                       (1)

satisfy `A Q_0+B Q_1+C Q_2=B Q_0+C Q_1+D Q_2=0`.
Consequently `P=Q_0+Q_1*z^4+Q_2*z^8` and zP are kernel vectors.
Whenever K has rank two they give both complete kernels, of dimension two.

Now let A,B,C,D be arbitrary linear forms in parameters u,v. Write
`A=A_0*u+A_1*v`, and similarly for the other three forms. Let M be the
3-by-3 coefficient matrix whose rows are Q_0,Q_1,Q_2, using columns
`u^2,uv,v^2`. Define

    chi=det M,
    Delta=3(B_0*C_1-B_1*C_0)-(A_0*D_1-A_1*D_0).             (2)

Assume chi is nonzero. The vector `(Q_0,Q_1,Q_2)` cannot vanish at any
projective point, since M is invertible and `(u^2,uv,v^2)` never vanishes
there. Therefore every member of this pencil has rank exactly eight.

**Theorem.** For every such line with `chi!=0`, the common tangent space
to the rank-at-most-eight Hankel cone along the entire line has dimension
four when `Delta!=0`, and dimension seven when `Delta=0`. In the first
case S is the unique maximal linear Hankel space of rank at most eight
containing that line.

This treats every parameter pair A,B,C,D satisfying the stated polynomial
guards, without assuming equivalence to the original sparse pencil.

## 2. An exact determinant identity

Let N be the 5-by-5 coefficient matrix, in columns `u^4,u^3v,u^2v^2,uv^3,v^4`,
of the five binary quartics

    Q_0^2, 2Q_0 Q_1, Q_1^2+2Q_0 Q_2, 2Q_1 Q_2, Q_2^2.

The following identity holds for all eight coefficients of A,B,C,D:

    det N = -4 Delta chi^3.                                (3)

Here is a bounded polynomial verification of the identity, together with
the extension from its chart. On the dense chart
`A_0*D_1-A_1*D_0!=0`, change u,v so that A=u,D=v, and write

    B=a*u+b*v, C=c*u+d*v.

Then

    M=[[-c^2, a-2cd, b-d^2],
       [ac, ad+bc-1, bd],
       [c-a^2, d-2ab, -b^2]],
    Delta=3(ad-bc)-1.

Expanding the explicitly defined 5-by-5 determinant gives
`det N+4*(3(ad-bc)-1)*(det M)^3=0`. This is an identity in C[a,b,c,d],
checked by the exact coefficient verifier, rather than a parameter grid.
All matrix definitions needed to reproduce this expansion are displayed
above; no unproved numerical factorization is an input.

Under an invertible parameter change g, the determinants of the degree-two
and degree-four monomial representations are `(det g)^3` and `(det g)^10`,
respectively. For example diagonal g gives those exponents by summing
the monomial powers, and triangular elementary changes have determinant
one; these matrices generate GL2. Hence chi transforms with weight three,
Delta with weight one, and both sides of (3) with weight ten. The chart
identity therefore holds on its full dense open set in the eight-variable
coefficient space. Since both sides are polynomials, it holds everywhere.

If chi is nonzero, rank N is at least four. Indeed the products of a
basis of three independent quadratics in u,v span all binary quartics,
so the six products Q_i Q_j have coefficient rank five. The displayed
five rows replace the two rows Q_1^2,Q_0 Q_2 by one linear combination
and retain four other rows, losing at most one rank. Thus (3) gives

    rank N=5 if Delta!=0, and rank N=4 if Delta=0.            (4)

## 3. The complete common tangent space

For a Hankel direction J with moments w_0,...,w_18, use the left and
right kernel vectors P,zP. At a rank-eight matrix, the derivative of
the nine-minors vanishes exactly when all left-kernel/right-kernel
pairings with J vanish. This follows by putting an invertible eight-minor
in the top-left block and differentiating its bordering minors.

The distinct pairings are the coefficients of P squared, shifted by
delta=0,1,2. For each delta they give N times the vector of moments

    (w_delta,w_(delta+4),w_(delta+8),w_(delta+12),w_(delta+16)).

The three sets of five indices are disjoint. The remaining four moments
have indices 3,7,11,15, exactly those of S. The common tangent dimension
is therefore `19-3*rank N`, proving the two values in the theorem.

When Delta is nonzero, every linear Hankel space containing the line
and having rank at most eight is contained in its four-dimensional common
tangent space S. Since S itself has the rank bound, it is the unique
maximal extension. The tangent statement is about the actual Hankel rank
cone as well: the minor equations give an upper bound on its tangents,
while in the Delta-nonzero case the linear subspace S supplies all four
directions. In the exceptional case, Section 4 justifies the actual
tangent dimension seven separately.

## 4. One exceptional seed: tangent dimension seven, maximal extension four

Choose

    A=v, B=0, C=u, D=v.

Here `(Q_0,Q_1,Q_2)=(-u^2,-v^2,uv)`, chi=-1 and Delta=0. The kernel
pairing equations give precisely the following seven-dimensional space:

    w_3=A, w_7=B, w_11=C, w_15=D,
    w_4=x, w_5=y, w_6=z,
    w_16=-2x, w_17=-2y, w_18=-2z,                            (5)

all other moments zero. The capital letters in (5) are free direction
coordinates, not the fixed seed parameters.

For each member of this seed line the determinantal rank cone is smooth
in the full matrix space, but a Hankel linear section can have additional
equations. At each rank-eight Hankel point, however, the Hankel rank locus
has tangent equal to the bordering-minor kernel just used. To see this
without importing reducedness of a determinantal ideal, use the scalar
annihilator chart: write a degree-eight annihilator and eight free initial
moments, and solve the consecutive recurrence when its endpoint coefficient
is nonzero. This gives a smooth parameter chart of dimension sixteen in
the nineteen-dimensional moment space; its three equations have independent
linear terms. The same construction in reversed coordinates or a binary
coordinate chart covers any nonzero degree-eight annihilator. Thus the
three pairings give the actual tangent at every seed point. Their common
kernel really has dimension seven, not just a space of linearized minors.

Nevertheless S is still the **unique** maximal linear extension of this
exceptional seed. Here is the higher-order obstruction. Let J in (5)
belong to a linear rank-at-most-eight extension. The quadratic Schur
coefficients at seed points `[u:v]=[1:0]` and `[1:1]` force, with E=A-D,

    Bx+yz=0, 2By+z^2=0, Bz=0,
    Ex=0, 2Ey+3x^2=0, Ez+3xy=0.                             (6)

These exact coefficients are independently reconstructed from eight-minors
in the verifier. Multiplying the fifth equation by x and using Ex=0
gives `3x^3=0`, hence x=0. Multiplying the second equation by z and using
Bz=0 gives `z^3=0`, hence z=0. If y were nonzero, (6) would imply
B=0 and A=D. In that case the determinant of J is

    det J=-A^4*y^6.                                        (7)

One small verification of (7) splits even and odd indices. The matrix has
the form `[[0,T],[T^T,0]]`, where T is 5-by-5 Hankel with moments
`(0,A,y,0,0,C,0,A,-2y)`. Its determinant is `A^2*y^3`, so (7) follows.

The extension contains the seed endpoint H(0,1), with moments h_3=h_15=1.
It must therefore also contain J+lambda H(0,1) for every lambda. Substituting
in (7) gives `-(A+lambda)^4*y^6`, which cannot vanish identically unless
y=0. Hence x=y=z=0 for every J in the extension. This proves the claim.

The seven tangent directions thus do not give a seven-dimensional linear
rank-bounded extension. The specific direction y=1,A=B=C=D=x=z=0 has
rank eight by itself, but adding H(0,1) gives determinant -1 and rank ten.

## 5. The entire paired exceptional family

The preceding exceptional seed extends to the complete family

    A=v, B=beta*u, C=u, D=v,   chi=beta^3-1!=0.               (8)

Every member has Delta=0 and common tangent dimension seven. **For every
complex beta satisfying the guard in (8), S remains the unique maximal
linear rank-at-most-eight Hankel extension of the entire line.**

To prove this, the five coefficient rows of P squared have moment kernel

    (-2beta,-1,0,beta,2).                                    (9)

This follows directly by multiplying N transposed by (9). Its nullspace
is one-dimensional by Section 2. Accordingly a general common tangent
direction J has the four free S coordinates A,B,C,D and three transverse
coordinates x,y,z. For delta=0,1,2 put e_delta=x,y,z and set

    (w_delta,w_(delta+4),w_(delta+8),w_(delta+12),w_(delta+16))
             =(-2beta,-1,0,beta,2)*e_delta.                 (10)

Here A,B,C,D again denote direction coordinates. Write E=A-D,
F=B-beta*C. The necessary quadratic equations are

    g1=Ex-3beta*yz,        g2=2Ey-3beta*z^2-3x^2,
    g3=Ez-3xy,            g4=Fx-yz,
    g5=2Fy-beta^2*x^2-z^2, g6=Fz-beta^2*xy.                 (11)

No extra exceptional parameter guard is hidden in (11). Here is an
explicit certificate of necessity valid at every beta in (8). At the seed
endpoint H(0,1), the Schur quadratic matrix in its two kernel coordinates
is

    Q_infinity=[[2g4,g5],[g5,2g6]].

Around the seed H(1,t), take the eight-minor on rows and columns 2,...,9.
At t=0 its determinant is the integer one for every beta. Normalize the
two kernel columns to the first two coordinate vectors and differentiate
the quadratic Schur coefficient with respect to the seed parameter t at
zero. The resulting matrix is

    Q_prime=[[-2chi*g1+2beta*(2beta^3-1)*g4,
                         -chi*g2+beta*(2beta^3-1)*g5],
             [-chi*g2+beta*(2beta^3-1)*g5,
                         -2chi*g3+2beta*(2beta^3-1)*g6]].

The verifier reconstructs both matrices from literal source entries and
checks these identities over C[beta,A,B,C,D,x,y,z]. Since the whole seed
line is contained in the proposed extension, both quadratic matrices
vanish. The only division used to recover all six g_i is by the stated
nonzero chi and nonzero integer constants.

Two elementary polynomial identities now give the needed nilpotence:

    3chi*x^3 = x*g2-2y*g1-3beta*x*g5+6beta*y*g4,
    3chi*z^3 = 3z*g5-6y*g6-beta^2*z*g2+2beta^2*y*g3.         (12)

Thus x=z=0 over C. If y were nonzero, (11) would give E=F=0. On that
remaining branch, J has only odd moments. Its even/odd off-diagonal
5-by-5 block has moments

    (-2beta*y,A,-y,beta*C,0,C,beta*y,A,2y).

Its exact determinant is

    chi*y^3*(A^2-beta*C^2-2beta*y^2).                        (13)

The full 10-by-10 determinant is the negative square of (13). Adding
lambda H(0,1) replaces A by A+lambda. The coefficient of lambda^4 in
that full determinant is `-chi^2*y^6`, so vanishing for every lambda
forces y=0. This proves the asserted uniqueness, since S itself supplies
the extension. At beta=0 this agrees with Section 4 after reversing the
sign of its transverse coordinates.

The conclusion is universal over the guarded complex parameter family,
not a finite parameter sweep. At beta^3=1 the guard really fails: chi is
zero and at `[u:v]=[1:beta^2]` all three minors in (1) vanish, giving
source rank four. The constant-rank proof cannot silently specialize
there. No extension classification is claimed for those lines.

## 6. Scope and evidence

The determinant identity is a universal polynomial identity, not an
empirical grid claim. Exact point controls and independent tangent-kernel
reconstruction provide additional checks. All algebra is local elementary
work; the prior prescribed-pencil construction retains its explicit credit.

For chi!=0 and Delta=0, the complete paired family (8) is decided here.
Other exceptional lines, other quadratic
pencils outside S, arbitrary Segre images and singular source degenerations
remain open. A ruling containing any of the lines covered by the extension
theorems has dimension at most four. No ordinary target frontier or matrix
multiplication exponent is changed.
