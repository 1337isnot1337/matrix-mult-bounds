# A universal determinant identity for the complete quadratic block

October 23, 2026. Owner-directed Codex research, written and unreviewed.
All checking described here belongs to the generating session; it is
not independent mathematical review or formalization. The result is a
polynomial identity for one crossed source block and a sharp geometric
linear-space dimension bound over every field. It gives no compatible tensor construction or
matrix-multiplication exponent improvement.

The literal source and prior distinction between pointwise and geometric
rank bounds retain their credits to the merged biform and linear-space
packages. The normal-form proof below is explicit; the classical
orthogonal-group correspondence is also cited as background. Exact
versions, source hashes and discovery provenance are in
[sources.json](sources.json).

## 1. Coefficient conventions and theorem

Let M=(m_(i,s)) for 0<=i,s<=2 be the coefficient matrix of

    F(X,Z)=sum m_(i,s) X0^(2-i) X1^i Z0^(2-s) Z1^s,
    f(x,z)=sum m_(i,s) x^i z^s.

The full literal fifteen-by-fifteen source has entries

    R(M)[(j,L),(h,r)] = m_(h-j,L-r),
    0<=j,r<=2,                 0<=L,h<=4,                (1)

with out-of-range coefficient indices interpreted as zero. Rows are
ordered first by j, then L; columns first by h, then r. These orders
fix the determinant sign. No source endpoint is removed.

Define

    J = [[0,0,-2], [0,1,0], [-2,0,0]],
    H = M^t J M J,
    Q(H) = 2 adj(H)-tr(adj(H)) I_3,
    Delta(M) = det Q(H).                                 (2)

Here adj is the classical adjugate, defined for singular matrices too.
The polynomial Delta is homogeneous of degree twelve in the entries
of M, with Delta(I_3)=2048, so it is nonzero in every odd
characteristic.

**Theorem A (integer polynomial identity).** In Z[m_00,...,m_22],

    2048 det R(M) = det(M) Delta(M).                      (3)

Equivalently, if s1=tr(H), s2=tr(adj(H)), s3=det(H), then

    Delta(M)=s2^3-4 s1 s2 s3+8 s3^2.                     (4)

The identity specializes over every field. If char K is not two, it
gives the pointwise criterion

    rank R(M)<=14  iff  det(M)=0 or Delta(M)=0.            (5)

In characteristic two, J has rank one, so H has rank at most one and
adj(H)=0. Both sides of the cleared identity (3) then vanish
identically. This specialization gives no rank criterion; division by
2048 is not allowed. Section 9 instead factors out 2048 in the integer
polynomial ring before reduction, yielding a useful characteristic-two
identity.

**Theorem B (linear-space reduction, char K not two).** Let W be a
K-linear subspace of the nine-dimensional coefficient space. The
following are equivalent:

1. rank R(M)<=14 for every M in W tensor_K Kbar.
2. det(M) vanishes identically on W, or Delta(M) vanishes identically
   on W.

“Identically” means as a polynomial in coordinates on W. The geometric
hypothesis in item 1 is essential over finite fields; checking only
K-rational points does not justify a polynomial identity. Over infinite
K, vanishing on every K-point is enough. No irreducibility assertion
about Delta, or classification of its linear spaces, is made.

**Coefficient-space consequence.** Over every characteristic, a linear
space on which the coefficient determinant vanishes as a polynomial has
dimension at most six. This classical special case is rederived in
Section 6, without a historical-priority claim. Consequently, in
characteristic different from two, any geometrically rank-at-most-14
space W of dimension at least seven must satisfy Delta|W=0 and contain
an invertible coefficient matrix over Kbar. If K is infinite, such a
member already exists over K. This does not bound the dimensions of
linear spaces in the degree-twelve locus by itself; Section 8 supplies
the additional local argument.

**Theorem C (sharp rational rank-fourteen bound).** If W is a Q-linear
subspace with rank R(M)<=14 for every M in W, then dim W<=6, and
this is sharp. In fact the three explicit integer coefficient matrices
in Section 7 span a rational three-space whose every nonzero member
has source rank fifteen. The proof lifts the merged seven-point binary
certificate; it does not use the determinant identity or a new census.

**Theorem D (sharp geometric bound in odd characteristic).** Let K be
any field of characteristic different from two. If W is a K-linear
coefficient space with rank R(M)<=14 for every M in W tensor_K Kbar,
then dim_K W<=6. The bound is sharp. For infinite K the same conclusion
follows from a rank cap on all K-rational members. Over finite K the
geometric hypothesis is retained.

The new ingredient is a direct quadratic-expansion argument at an
invertible coefficient matrix in the degree-twelve locus. It uses no
classification of that locus, no new external structural theorem, and
no generic diagonalization in positive characteristic.

**Theorem E (sharp geometric bound in characteristic two).** The
conclusion of Theorem D also holds over every field of characteristic
two. Thus the sharp geometric dimension bound is six over every field.
The proof in Section 9 uses an integral refinement of (3), a
classification of six-dimensional singular coefficient spaces, and
an explicit source determinant on a two-parameter affine family. It
does not assert a classification of all source-rank-fourteen spaces
attaining dimension six. The finite-field geometric hypothesis remains
unchanged.

## 2. Invariance and the exact source representation

We prove (3) first over k=Qbar. Binary quadratic coefficients (a,b,c)^t
have discriminant b^2-4ac=(a,b,c)J(a,b,c)^t. An SL2 substitution on
binary variables therefore induces a coefficient matrix T satisfying

    T^t J T=J,                  det T=1.

Independent substitutions in X and Z act by M -> T M U^t. For such
T,U one has

    det(T M U^t)=det(M),
    H(T M U^t)=U H(M) U^-1.                              (6)

The right side of (3) is consequently invariant under the substitutions.

For the left side, let V_d denote degree-d homogeneous binary forms
with the ordinary monomial basis, and let V_d^* carry its literal dual
basis. The tensor F defines the natural contraction/multiplication map

    V_4(X)^* tensor V_2(Z) -> V_2(X)^* tensor V_4(Z).     (7)

Contraction by X0^(2-i)X1^i sends the dual basis element indexed h
to that indexed h-i, while multiplication by Z0^(2-s)Z1^s sends the
basis element indexed r to that indexed r+s. Thus (7) has exactly
matrix (1). Literal dual bases, rather than differential-operator
normalizations, account for the absence of binomial coefficients.

Naturality transforms (7) by the source and target representation
matrices. Symmetric powers of an SL2 matrix and their duals have
determinant one: in general
det(Sym^d g)=(det g)^(d(d+1)/2), as follows on diagonal matrices and
then on a dense set of diagonalizable matrices. Tensor products here
also have determinant one. Hence det R is invariant under both SL2
substitutions, with its exact sign fixed by (1).

## 3. The full orthogonal action and a dense normal form

Over k, the null conic of J consists of square binary forms:

    [u:v] |-> [u^2:2uv:v^2].                             (8)

Every h in SO(J) induces an automorphism of this conic and hence of
P1. An automorphism of P1 is fractional linear: the degree of its
rational function multiplied by the degree of its inverse is one.
Choose a GL2 matrix for it and rescale to determinant one, possible
over k. Its binary-quadratic action rho(g) and h induce the same
projective action on the conic. Their quotient fixes that conic
pointwise and is scalar. To see this last statement, three noncollinear
conic points make the quotient diagonal, and a fourth conic point with
all three coordinates nonzero forces its diagonal entries equal.
Write h=c rho(g). Preservation of J gives c^2=1, and determinant one
gives c^3=1, so c=1. The SL2 coefficient action is therefore onto
SO(J) on k-points.

This explicit argument fixes our coefficient convention. The classical
isomorphism PGL2 ~= SO3 is also given in Conrad and Lichtenstein,
[Linear Algebraic Groups I](https://math.stanford.edu/~conrad/252Page/handouts/alggroups.pdf),
revision February 8, 2020, Example A.5.2, page 77, via conjugation on
traceless two-by-two matrices. It is background consistent with (8),
rather than an imported matrix normalization.

Choose iota^2=-1 and a square root of two in k. Let P have as columns
the coefficient vectors of

    b1=(X0^2+X1^2)/sqrt(2),
    b2=iota*(X0^2-X1^2)/sqrt(2),
    b3=sqrt(2)*iota*X0*X1.

Then P^t J P=-2 I_3. Writing M=P N P^t turns the action into the usual
SO3 by SO3 action N -> U N V^t, and H is similar to 4 N^t N.

Consider the nonempty open set where N^t N has distinct nonzero
eigenvalues; N=diag(1,2,3) is an example. Eigenvectors of this symmetric
matrix for distinct eigenvalues are orthogonal. No eigenvector in
their basis is isotropic, since it would then be orthogonal to every
basis vector, contradicting nondegeneracy. Normalize them, adjusting
one sign if necessary, to form V in SO3. For chosen square roots s_j
of the eigenvalues, the columns of N V diag(s_j^-1) are orthonormal.
Adjusting one square-root sign makes this matrix U have determinant
one. Thus

    U^t N V=diag(s1,s2,s3).                              (9)

Both orthogonal transformations lift to SL2 substitutions by (8).
This is only a dense-open normal form; no diagonalization of every
singular or repeated-eigenvalue matrix is assumed.

The diagonal family in the b-basis is exactly the three-parameter
family

    F=A*(X0^2 Z0^2+X1^2 Z1^2)
          +B*(X1^2 Z0^2+X0^2 Z1^2)+C*X0 X1 Z0 Z1,
    M=[[A,0,B],[0,C,0],[B,0,A]].                         (10)

Indeed, setting alpha=A+B, beta=A-B, gamma=C/2 gives

    F=alpha b1(X)b1(Z)-beta b2(X)b2(Z)-gamma b3(X)b3(Z).

This invertible linear parameter change permits every diagonal matrix in (9). The
orbits of (10) therefore contain a dense open subset of coefficient
space.

## 4. Exact three-parameter calculation

For (10), put d=A^2-B^2. Then det M=C d. Every nonzero entry of R
has j+L and h+r of the same parity. Reordering each index set by parity
gives an eight-by-eight block and a seven-by-seven block. Each ordering
permutation has 28 inversions, so their combined sign is positive.
Direct polynomial determinant expansion of the two blocks gives

    det R_even = -(d^2-AB C^2)(d^2+AB C^2),
    det R_odd  = -C d (2d^2-(A^2+B^2)C^2).              (11)

These are bounded symbolic identities in A,B,C, reconstructed from
(1) by the companion verifier. Multiplying them determines det R on
the entire three-parameter family, not just sampled parameter values.

Let e1,e2,e3 be the elementary symmetric polynomials in
alpha^2,beta^2,gamma^2, with the parameters just defined. Rewriting the product
in (11) gives the polynomial identity

    det R=2 C d (e2^3-4e1 e2 e3+8e3^2).                 (12)

Meanwhile H has eigenvalues 4alpha^2,4beta^2,4gamma^2. For any three-by-three
matrix H, the eigenvalues of adj(H) on the dense set of matrices with
distinct eigenvalues are h2*h3, h1*h3, h1*h2. Their elementary
symmetric functions are s2,s1*s3,s3^2. Expanding the product of twice
each such eigenvalue minus s2 proves

    det(2 adj(H)-s2 I)=s2^3-4s1 s2 s3+8s3^2.            (13)

Both sides are integer polynomials, so this identity holds for all H.
Scaling H's eigenvalues by four now gives

    Delta(M)=4096 (e2^3-4e1 e2 e3+8e3^2).               (14)

Equations (12)--(14) and det M=C d prove (3) on (10), with exact
constant 4096/2=2048 and without assuming C d nonzero.

Both sides of (3) are invariant by Section 2; Section 3 shows that
orbits of (10) cover a dense open set over Qbar. Their difference,
a polynomial, consequently vanishes identically over Qbar. Its integer
coefficients must all vanish, proving the identity over Z and every
claimed specialization. This dense-open argument supplies the universal
step; finite numerical checks do not supply it.

For comparison with the alternate normalization in the verifier, set

    B=[[0,0,1],[0,-2,0],[1,0,0]],
    H0=B^-1 M^t B^-1 M.

Over Z[1/2], J=-2B^-1 and H is similar to 4H0. An adjugate of a
three-by-three matrix scales by the square of that scalar. Thus
Delta(M)=4096 det(2 adj(H0)-tr(adj(H0)) I), and (3) is equivalently

    det R=2 det(M) det(2 adj(H0)-tr(adj(H0)) I).          (15)

The operator to diagonalize in the J-coordinates is A=MJ: its J-adjoint
A*=J^-1 A^t J satisfies A*A=H. Treating M itself as that operator
would use the wrong normalization.

## 5. Geometric linear families

Choose a K-basis M1,...,Mm for W and write M(t)=sum t_i Mi. A
geometric rank cap of fourteen is equivalent to

    det R(M(t))=0 in K[t1,...,tm].                       (16)

Indeed the determinant is the only maximal minor, and a polynomial
vanishing on every point over the infinite algebraic closure is zero.
For char K not two, (3) turns (16) into

    det(M(t)) Delta(M(t))=0.

The parameter polynomial ring is an integral domain, so one factor
is the zero polynomial. Conversely, either factor being the zero
polynomial implies (16) and the geometric rank cap. This proves
Theorem B, including the zero subspace.

The conclusion does not merely select a factor separately at each
point: one fixed factor vanishes identically on the whole family.
For an infinite ground field, the same polynomial reasoning starts
from a rank cap on all its rational points. For a finite ground field
that inference is invalid without the geometric hypothesis. The prior
linear-space package exhibits this distinction for the same source.
No claim that the degree-twelve factor is irreducible is needed.

## 6. The coefficient-determinant alternative has dimension at most six

We give a rederivation of this classical small matrix-space bound. Only
the geometric assertion is used: det|W is the zero polynomial. Extend
scalars to k=Kbar. If dim W>=7, restrict to any seven-dimensional
subspace; it is enough to exclude that case. Under the nondegenerate
pairing <A,M>=tr(A^t M), its annihilator S=W^perp has dimension two.
For v!=0 put

    ev_v: W -> k^3,       M |-> Mv,
    E_v={u v^t : u in k^3}.

The dual evaluation sends u to the functional M |-> u^t Mv, hence

    rank ev_v=3-dim(S intersection E_v).                 (17)

It depends only on [v] in P2. A drop below rank three occurs precisely
at the right factors of nonzero rank-one matrices in S.

The rank-one locus Sigma in P(S)=P1 is closed, defined by the
two-by-two minors, so it is finite or all of P1. If it is finite,
the exceptional right factors form a finite set, and each intersection
S intersection E_v has dimension one. An intersection of dimension two
would put all of S inside E_v, contradicting finiteness of Sigma.

If Sigma is all of P1, choose independent rank-one matrices u v^t
and x y^t spanning S. The pairs (u,x) and (v,y) cannot both be
independent: left and right basis changes would then send these
matrices to E_11 and E_22, whose sum has rank two in every
characteristic. Exactly one pair is dependent, since the matrices
are independent. Thus either

    S={u z^t : z in V},  with fixed u!=0 and dim V=2,
or  S={z v0^t : z in U}, with fixed v0!=0 and dim U=2.    (18)

In the first case, (17) has rank two on the projective line P(V)
and three off it. In the second it has rank one at [v0] and three
off that single point.

Consider the incidence variety

    Z={(M,[v]) in W x P2 : Mv=0}.

Over a constant-rank stratum in P2, its fibers are the kernels of
ev_v, of dimension 7-rank ev_v. They are locally products: choose
a nonzero maximal minor and solve those coordinates by elimination.
The complete stratum list gives

| Base stratum | Its dimension | Evaluation rank | Incidence dimension |
| --- | ---: | ---: | ---: |
| Complement of the exceptional locus | 2 | 3 | 6 |
| Finite Sigma: exceptional right factors | 0 | 2 | 5 |
| Common-left-factor case in (18): P(V) | 1 | 2 | 6 |
| Common-right-factor case in (18): [v0] | 0 | 1 | 6 |

Only the applicable exceptional row is used in each case. The finite
union of these locally closed strata has dimension at most six.
But every M in W is singular and has a nonzero kernel vector, so the
image of Z -> W contains all k-points of W and has closure W, of
dimension seven. This contradicts the image-dimension bound. The
dimension facts used are [Stacks 33.20.4(2)](https://stacks.math.columbia.edu/tag/0B2L),
[33.20.5(2)](https://stacks.math.columbia.edu/tag/0B2M), and
[33.34.1](https://stacks.math.columbia.edu/tag/0B2P): image dimension
cannot increase, product dimensions add, and dim Pn=n. No generic
finiteness of the projection or unique kernel line is assumed.

Therefore dim W<=6, in every characteristic. Matrices killing a
fixed nonzero vector form a six-dimensional example, so this
coefficient-determinant bound is sharp; its equality cases are not
classified here.

Finally apply Theorem B. If a geometric source-rank-14 family has
dimension at least seven and char K is not two, its coefficient
determinant is not identically zero. Thus Delta vanishes identically
on the family, and some coefficient matrix is invertible over Kbar.
For infinite K, the nonzero determinant polynomial also has a nonzero
value over K. Existence of such a K-rational member is not inferred
for finite fields. This reduces a hypothetical larger source-rank-14
space to the invertible part of the degree-twelve locus. Section 8
rules out that remaining alternative in every odd characteristic.

## 7. An explicit rational full-rank three-space

The merged [linear-space proof, Section 2](../2026-10-23-quadratic-linear-spaces/proof.md)
gives the integer polynomials

    t1=x^2+xz+z^2,
    t2=x+x^2+(1+x^2)z+xz^2,
    t3=1+x+x^2+(x+x^2)z+x^2 z^2.                        (19)

Their reductions span a three-dimensional space over F2 whose seven
nonzero elements all have source rank fifteen. Here is the exact
inherited certificate, using bit 3s+i for the coefficient of x^i z^s:

| Binary combination | Mask | det R of its integer 0,1 coefficient lift |
| --- | ---: | ---: |
| t1 | 84 | -1 |
| t2 | 174 | 7 |
| t1+t2 | 250 | 3 |
| t3 | 311 | 1 |
| t1+t3 | 355 | 43 |
| t2+t3 | 409 | 1 |
| t1+t2+t3 | 461 | 1 |

The additions in this table are binary, followed by lifting each bit
to 0 or 1. The integer combinations of (19) need not equal those
lifts; their determinants are congruent modulo two, which is exactly
what is required. These seven determinant computations are inherited
from the pinned merged package, not claimed as new finite experiments.

Let T_Q be the rational span of (19). Their binary independence implies
rational independence: a rational dependence could be cleared to an
integer coefficient tuple with at least one odd entry, contradicting
binary independence after reduction. Thus dim T_Q=3.

For any nonzero rational combination of (19), clear the coefficient
denominators and divide by the largest common power of two. This gives
an integer combination f with at least one odd coefficient in its
three-term expression, without changing its rank over Q. Its reduction
modulo two is one of the seven nonzero binary combinations above.
The literal matrix construction has integer coefficients and commutes
with reduction. Consequently det R(f) is odd and in particular nonzero.
Every nonzero member of T_Q therefore has source rank fifteen.

If dim W>=7, then in the nine-dimensional rational coefficient space

    dim(W intersection T_Q)>=dim W+3-9>=1.

This gives a nonzero member of W with source rank fifteen, a
contradiction. Hence dim W<=6. Sharpness follows from the six-dimensional
space f=z(A(x)+z B(x)), deg A,deg B<=2: all three rows with L=0
in (1) vanish, so its source rank is at most twelve. This proves
Theorem C without a denominator-dependent choice of a reduced basis
for W, and without inferring polynomial vanishing from finite points.

Since Q is infinite, its pointwise and geometric rank-cap hypotheses
are equivalent. This closes the rational question independently of the
determinant identity and of the odd-characteristic argument that follows.

## 8. The geometric bound in every odd characteristic

Extend scalars to k=Kbar; this preserves the dimension and the geometric
hypothesis. By Sections 5--6, a putative space W of dimension at least
seven must have Delta identically zero and contain an invertible
coefficient matrix. We will obtain a contradiction locally at any such
member, without imposing a generic eigenvalue condition.

First use the invertible matrix P from Section 3, now over k, and write
M=P N P^t. Its construction uses only iota^2=-1, a square root of two,
and division by two, all available over this algebraically closed field
of odd characteristic. It is simply an invertible linear coordinate
change on coefficient matrices. Write

    H_N=N^t N,
    Delta_0(N)=det(2 adj(H_N)-tr(adj(H_N)) I).

The matrix H_M=M^t J M J from Section 1 is similar to 4H_N, so

    Delta(M)=4096 Delta_0(N).                            (20)

Thus the transformed linear space, still denoted W, is contained in
Delta_0=0 and has an invertible member N. The factor 4096 is nonzero;
no positive-characteristic orthogonal diagonalization is being used.

On the open set of invertible N define the regular rational function

    Q=H_N^-1,       t=tr(Q),       S=2Q-t I,
    Phi(N)=det(S).

The adjugate formula gives the exact unit relation

    Delta_0(N)=det(H_N)^3 Phi(N).                        (21)

The exponent is three. Since det(H_N)=det(N)^2 is nonzero here,
Phi vanishes identically on the open part of W. We work directly
with Phi, so no assertion about a Hessian under an unspecified change
of defining equation is needed.

At the chosen point, put U=adj(S) and tau=tr(U). We first prove that

    rank S=2,        tau!=0,
    G=-Q(2U-tau I)Q is invertible and symmetric,
    tr(H_N G)=0.                                        (22)

Indeed det S=0 and tr S=-t. For any three-by-three matrix with trace
s, adjugate trace tau and determinant zero, its characteristic
polynomial gives det(S-sI)=-s tau. Here S-(tr S)I=2Q, hence

    8 det(Q)=t tau.                                     (23)

Q is invertible and the characteristic is not two, so tau is nonzero.
Thus U is nonzero; det S=0 implies rank S=2 and rank U=1. For a
rank-one matrix U, writing U=ab^t shows U^2=(tr U)U=tau U. Therefore

    (2U-tau I)^2=tau^2 I.                               (24)

This matrix, and consequently G, is invertible. Q and U are symmetric,
so G is symmetric. Finally SU=0 gives QU=(t/2)U. Cyclicity of trace
then yields

    tr(H_N G)=-tr((2U-tau I)Q)
              =-2(t/2)tau+tau t=0.

All identities (22)--(24) hold in every odd characteristic, including
three. In particular, none divides by three, by an eigenvalue
discriminant, or by a potentially zero trace other than the nonzero
quantity established in (23).

The matrix G is exactly the gradient with respect to the symmetric
Gram matrix H_N: for a symmetric first variation B, the identities
dQ=-Q B Q and d(det S)=tr(adj(S) dS) give

    dPhi_H(B)=tr(U(2dQ-tr(dQ)I))=tr(G B).                (25)

For a first variation B of N, rather than of H_N, the chain rule gives

    dPhi_N(B)=2 tr((N G)^t B).                           (26)

Since 2NG is invertible, this is a nonzero linear functional. Its
kernel T is an eight-dimensional tangent hyperplane in Mat_3(k).
Because Phi vanishes on W near N, the linear space W, viewed as the
directions at N, lies in T.

Consider the three-dimensional subspace of tangent directions

    V={K N : K^t=-K}.

It is contained in T, because the first variation of H_N along these
directions is zero. More precisely,

    (N+z K N)^t(N+z K N)=H_N+z^2 N^t K^t K N.           (27)

Here z is a formal expansion parameter, separate from the original
biform variable. All denominators are invertible at z=0, so (27)
and the following coefficient calculation are valid in k[[z]], with
no analytic or characteristic-zero assumption. Put A=N G N^t.
It is symmetric and invertible, and tr A=tr(H_N G)=0. By (25),

    [z^2] Phi(N+z K N)=tr(A K^t K).                     (28)

Parametrize skew matrices by kappa=(k1,k2,k3)^t using

    K(kappa)=[[0,-k3,k2],[k3,0,-k1],[-k2,k1,0]].

The direct integer matrix identity
K(kappa)^t K(kappa)=(kappa^t kappa)I-kappa kappa^t,
together with tr A=0, turns (28) into

    [z^2] Phi(N+z K(kappa)N)=-kappa^t A kappa.           (29)

Equivalently, the second directional derivative is
-2 kappa^t A kappa. Thus the quadratic coefficient on V is a
nondegenerate ternary quadratic form, since A is invertible and the
characteristic is odd.

Both W and V lie in the eight-dimensional space T, so

    dim(W intersection V)>=dim W+3-8>=2.                (30)

For every direction B in that intersection, the entire line N+zB
lies in W. Relation (21) therefore makes Phi(N+zB) identically zero
as a rational function, and its quadratic coefficient vanishes. The
form (29) vanishes on a linear subspace of dimension at least two.
Polarization in odd characteristic makes that subspace totally
isotropic for the associated nondegenerate bilinear form on V.
But if E is such a subspace, E is contained in E-perp and
dim(E-perp)=3-dim E, so 2 dim E<=3. This contradicts (30).

The hypothetical dimension-at-least-seven W cannot exist. Together
with the coefficient-singular case in Section 6, this proves the
upper bound in Theorem D. The same six-dimensional family
z(A(x)+z B(x)) used in Section 7 has three zero source rows over every
field and supplies sharpness. No equality-case classification is
asserted. Over an infinite original field, pointwise vanishing of the
source determinant is a polynomial identity, so it also implies this
geometric bound. Over finite fields that replacement of the hypothesis
is not made. Characteristic two remains outside this local argument:
the discriminant normalization and polarization both require two to
be invertible.

## 9. Characteristic two: integral refinement and a singular hyperplane

Write the original coefficient matrix, in exactly the basis of (1), as

    M=[[a,b,c],[d,e,f],[g,h,i]],        D=det M.

Define the following integer polynomials of degrees two and four:

    A2=2ai+2cg-bh-df,
    T4=a^2 i^2-abhi-2acgi+ach^2-adfi+af^2 g
       +b^2 gi-bcgh+bdfh-befg+c^2 g^2+cd^2 i
       -cdeh-cdfg+ce^2 g.                              (31)

Direct three-by-three multiplication and adjugate expansion give

    s1=e^2+4A2,       s2=8eD+16T4,       s3=16D^2.

These are integer polynomial equalities, including all signs in (31).
Put B4=eD+2T4. Substituting into (4), and using
B4^2-e^2 D^2=4eDT4+4T4^2, gives

    Delta=512(B4^3-e^2 B4 D^2-4A2 B4 D^2+4D^4)
         =2048 P12,
    P12=D^4+(eD+2T4)(eDT4+T4^2-A2 D^2).                (32)

Cancellation of 2048 in the integral domain Z[a,...,i], using (3),
therefore proves det R=D P12 as an integer polynomial identity. This
cancellation precedes specialization. In characteristic two, (32)
becomes

    P12=D G9,
    G9=D^3+e^2 D T4+e T4^2+e A2 D^2,
    det R=D^2 G9.                                      (33)

In particular, restriction to the original-coordinate hyperplane e=0
gives the decisive polynomial identity

    det R|_(e=0)=D^5|_(e=0).                           (34)

We next supply the equality case of the coefficient-singular bound
needed here. Let k be algebraically closed of characteristic two and
let U be a six-dimensional subspace of Mat_3(k) all of whose members
are singular. Then U is either the full space of matrices killing a
fixed nonzero vector or the full space whose images lie in a fixed
hyperplane.

First, a linear space of matrices of rank at most one has dimension
at most three. Indeed, choose a nonzero member u0 v0^t. A rank-one
member u v^t must have u proportional to u0 or v proportional to v0:
otherwise their sum has rank two, as is seen by choosing bases for the
two independent left and right pairs. Thus the space is contained in
the union of the two three-dimensional spaces with fixed left or
fixed right factor. A linear space contained in the union of two
linear subspaces lies in one of them: if neither containment held,
the sum of a vector in each difference would lie in neither. This
proves the bound.

Consequently U contains a matrix of rank two. Temporarily changing
the domain and codomain bases of coefficient matrices makes this
member diag(1,1,0). These arbitrary GL3 changes are used only to
classify singular coefficient spaces, not as asserted symmetries of
the source R. For B in U the coefficient of t in det(diag(1,1,0)+tB)
forces b33=0. Write

    B=[[P,u],[v^t,0]],   P in Mat_2(k),   u,v in k^2.

The remaining determinant coefficients are

    det(diag(1,1,0)+tB)=-t^2 v^t u-t^3 v^t adj(P)u.

Let I be the image of U under B -> (u,v). The quadratic form
q(u,v)=v^t u vanishes on I. Its polar form

    ((u,v),(u',v')) -> v^t u'+v'^t u

is nondegenerate alternating on k^2 direct_sum k^2. It vanishes
on I times I, so I is contained in I-perp and dim I<=2. The kernel
of this projection has dimension at most four, because only P can
vary there. As dim U=6, both bounds are equalities: dim I=2, and
the kernel contains every P in Mat_2(k).

For a fixed (u,v) in I, P can therefore vary freely. Singularity of
every corresponding B gives v^t adj(P)u=0 for every P. The adjugate
map on two-by-two matrices is a linear bijection, so this forces
u=0 or v=0. The same union-of-two-subspaces argument makes I one
of the two coordinate planes. Hence U consists of all matrices with
last column zero or all matrices with last row zero in the temporary
bases. Undoing those changes proves the asserted common-kernel or
common-cokernel description in the original coefficient coordinates.

Now extend the field in Theorem E to its algebraic closure k. If a
geometrically rank-at-most-fourteen space has dimension at least seven,
restrict to a seven-dimensional W. All source determinants vanish
as polynomials on W. If e vanishes identically on W, (34) implies
D|W=0 in its polynomial coordinate ring, contradicting Section 6.
Thus e|W is nonzero and

    U=W intersection {e=0}

has dimension six. Equation (34) makes every member of U singular.
Apply the equality description just proved, now in the original
monomial coefficient coordinates.

Put eta=(0,1,0)^t, so e(M)=eta^t M eta. If U is the full space
{M:Mv=0}, its annihilator under the entrywise matrix pairing consists
of the matrices a v^t with a arbitrary. Because e annihilates U,
eta eta^t belongs to this annihilator; equality of these nonzero
rank-one matrices forces v proportional to eta. Thus U is exactly
the space with middle column zero. For a common-cokernel space the
same argument gives exactly the space with middle row zero. No
unrestricted coefficient change of basis is being applied to R here.

Consider the middle-column case. Choose M0 in W with e(M0)=1 and
write its middle column as (b,1,h)^t. Adding arbitrary members of U
shows that W contains, for every a,i in k,

    M(a,i)=[[a,b,0],[0,1,0],[0,h,i]].

In characteristic two put x=ai and y=bh. On this family the formulas
in (31) give D=x, A2=y and T4=x(x+y). Substitution into (33) gives

    G9=x^2(x+y)^2,
    det R(M(a,i))=(ai)^4(ai+bh)^2.                     (35)

Take a=1 and choose i outside {0,bh}. Such an i exists in the
algebraically closed field k. Equation (35) is nonzero, a contradiction.
For the middle-row case transpose these matrices: (1) identifies
R(M^t), up to row and column permutations, with R(M)^t, so its rank
is unchanged. This proves the upper bound in Theorem E. The same
six-dimensional family z(A(x)+z B(x)) supplies sharpness in
characteristic two, completing the geometric bound over every field.

The choice of i above occurs over k, not necessarily the original
finite field. For example, when b=h=1 the polynomial in (35) vanishes
at every pair a,i in F2 but is not the zero polynomial. This is why
the geometric hypothesis is kept throughout. The equality
classification used here concerns singular coefficient spaces only;
it does not classify all source-rank-at-most-fourteen six-spaces.

## 10. Exact checks and remaining scope

The maintained verifier rebuilds all literal matrices with the orders
in (1), rather than importing an earlier verifier. Its bounded report
contains 29 exact rational matrices: five named controls, including
singular coefficient matrices, and 24 controls with seed 20261023.
These reuse the scratch experiment's input set and are not counted as
29 new discovery cases. Three additional rational controls in T_Q
check the source determinant and its odd value after clearing
denominators and removing a common power of two. They retain integer
coefficient overlaps rather than replacing addition by binary XOR.
Eighteen modular controls reduce six integer
matrices modulo 3, 5 and 7: the five named inputs and diag(1,3,1).
The last matrix is invertible over F7 while its source determinant
vanishes, directly testing the degree-twelve alternative. A characteristic-two example
has literal rank fifteen while the cleared identity reads 0=0,
demonstrating the excluded division step.

The parity-block symbolic calculation in (11) uses the three variables
A,B,C. It checks the two block determinants, the two
28-inversion permutation signs, and both invariant normalizations.
No nine-variable symbolic fifteen-by-fifteen determinant is required.
The rational literal determinant uses exact Fraction elimination; the
small invariant matrices use symbolic three-by-three arithmetic. Fourteen
focused tests replay the report and source hashes, check contraction
coordinates and parity signs, reject a corrupted J normalization,
guard exact rational elimination, and verify the finite-field and
rational-lifting boundaries. Five additional local curvature
certificates use two rational points and one point over each of
F3,F5,F7. Independent one-variable determinant expansions check 45
ordinary directional derivatives and 30 skew-direction second
derivatives. The F5 control has a genuine size-two Jordan block in
its Gram matrix, and a corrupted skew sign is rejected. These bounded
checks corroborate Section 8 without imposing a diagonalizability
assumption or replacing its universal algebraic proof.

The characteristic-two extension separately checks (31)--(33) over
the integers and then coefficientwise modulo two: P12 has 776 integer
terms and its residue has 174 terms. A corrupted integer sign in T4,
which would be invisible after reduction modulo two, is rejected. One
specialized four-variable literal fifteen-by-fifteen determinant is
also computed, for M=[[a,b,0],[0,1,0],[0,h,i]]. Over the integers it is

    (ai)^4(ai-bh)(2(ai-bh)^2-ai-bh),

whose characteristic-two reduction agrees with (35). This specialized
symbolic source check is additional to the parity blocks; no general
nine-variable symbolic source determinant is expanded. Eight fresh
finite source controls comprise the four F2 points with b=h=e=1,
and two F4 matrices together with their transposes. Their F4 source
determinants are 3,3,0,0 in the encoding alpha=2,
alpha^2+alpha+1=0. These tests explicitly distinguish the F2
pointwise zero example from polynomial vanishing after extension.

The finite controls corroborate conventions and arithmetic. They do
not prove the dense-open orbit statement, the universal extension, the
linear-space reduction, the incidence dimension bound, Theorem D's
local quadratic obstruction, or Theorem E's coefficient-space argument.
Those steps are the written arguments
above. In particular, the full-suite snapshot at commit 5ea78f5 predates
the addition of Theorems D and E and is retained as a pre-extension baseline,
not reported as validation of the extended proof.

The package does not prove that Delta is irreducible, classify the
spaces attaining dimension six, or supply a compatible tensor
construction or an exponent improvement. The geometric dimension bound
is proved over every field, with separate arguments in odd and even
characteristic. The earlier binary pointwise bound remains a separate,
inherited result; finite-field pointwise conditions are not silently
identified with the geometric hypothesis.
