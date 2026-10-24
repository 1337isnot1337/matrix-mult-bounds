# Characteristic-two geometric quadratic equality spaces

October 24, 2026. Proof written and unreviewed. This continuation uses
the literal source convention and descent argument of [proof.md](proof.md).
It addresses the characteristic-two boundary left by the odd-characteristic
Hessian proof. Exact polynomial checks and a separate same-session audit accompany the
proof; neither constitutes independent mathematical review. The audit caught
a missing adfi term in the first quartic expansion; the corrected term is
present below, and a mutation test rejects that original omission.

**Theorem.** Over a field K of characteristic two, the six-dimensional
K-linear coefficient spaces with geometric source rank at most fourteen
are exactly the spaces with a common nonzero kernel vector or a common
nonzero left-kernel vector. The condition is geometric: det R vanishes as
a polynomial on the space, not merely at its K-rational points.

Work over an algebraic closure k. The common-kernel description descends
by the stacked-matrix argument in proof.md. Put eta=(0,1,0)^t and
write e(M)=eta^t M eta, D(M)=det M. The pinned determinant proof, Section 9,
cancels the integer normalization before reduction and gives

    det R = D^2 G9,      det R|_(e=0) = D^5|_(e=0).       (1)

Its precise polynomial G9, with the original monomial coefficient order,
will be used below. No division by 2048 in characteristic two occurs.

If e vanishes on a six-space W of geometric source rank at most fourteen,
(1) makes every coefficient matrix singular. The singular six-space lemma
in proof.md gives the conclusion. Otherwise

    U = W intersection {e=0}

has dimension five and consists of singular coefficient matrices.

## 1. Singular five-spaces

Every five-dimensional singular subspace U of Mat_3(k) is either contained
in a six-dimensional common-kernel or common-left-kernel space, or is

    {M : M(E) is contained in L},                       (2)

for a two-dimensional domain subspace E and a one-dimensional image
subspace L. The latter space has dimension five.

Here is a proof. The rank-at-most-one lemma in proof.md implies that U
contains a rank-two matrix. Temporarily choose arbitrary domain and
codomain bases to make it A=diag(1,1,0). For B in U the polynomial
identity det(A+tB)=0 gives

    B=[[P,u],[v^t,0]],
    det(A+tB)=-t^2 v^t u-t^3 v^t adj(P)u.              (3)

Let I be the image of U in the four-dimensional space of pairs (u,v).
It is isotropic for the nondegenerate polar form of v^t u, hence dim I<=2.
The kernel K0 of this projection is a subspace of Mat_2(k), of dimension
at most four. Thus dim I is one or two.

If dim I=1, then K0=Mat_2(k). Varying P in (3) forces u=0 or v=0 for
its generator. U has a common kernel or common left kernel.

If dim I=2, then dim K0=3. For each (u,v) in I the linear functional
P -> v^t adj(P)u vanishes on K0, since all P in a fiber can be shifted
by K0. These functionals therefore lie in a fixed one-dimensional
annihilator. If they are all zero, every pair has u=0 or v=0; the union
of two linear-subspaces argument gives a common kernel or left kernel.

Otherwise one nonzero functional is determined by nonzero factors u0,v0.
Every pair with both factors nonzero determines a proportional rank-one
functional, hence u is proportional to u0 and v to v0. Such pairs form
a nonempty open subset of the irreducible affine plane I. The linear
conditions just obtained consequently hold on all of I. Dimension two
then gives

    I={(alpha*u0,beta*v0):alpha,beta in k}.

The isotropy identity forces v0^t u0=0. A simultaneous change in the two
rank-two blocks, preserving A, and rescaling the parameters makes
u0=(1,0)^t and v0=(0,1)^t. Thus K0 is the hyperplane p21=0. Choose a
linear section P(alpha,beta) of the projection to I. Equation (3) gives
alpha*beta*p21(alpha,beta)=0 as a polynomial, so p21(alpha,beta)=0.
All matrices in U therefore have the form

    [[p11,p12,alpha],[0,p22,0],[0,beta,0]].

These are all matrices supported in the first row or second column.
Undoing the temporary bases gives (2). These arbitrary basis changes
classify coefficient spaces only; no source-rank invariance under all
GL3 changes is asserted.

## 2. Permitted binary changes of variables

For g=[[alpha,beta],[gamma,delta]] in GL2(k), substitution in a binary
quadratic acts on its coefficient vector by

    A(g)=[[alpha^2,alpha*gamma,gamma^2],
          [0,det(g),0],
          [beta^2,beta*delta,delta^2]].                 (4)

Independent binary substitutions act on coefficient matrices as
M -> A(g) M A(h)^t. They preserve source rank: the source is the natural
contraction Sym^4(X)^* -> Sym^2(X)^* in the first binary variable and
multiplication Sym^2(Z) -> Sym^4(Z) in the second, contracted with the
biform. The induced maps on each source and target factor are invertible.
This uses the ordinary monomial bases and their duals, not a self-duality
identification or division by two. Formula (4) also gives

    e(A(g) M A(h)^t)=det(g)*det(h)*e(M).

On the coefficient plane eta-perp (the square quadratics), A(g) acts
transitively on nonzero lines: over k every vector there is the square
of a nonzero linear form. On kernel vectors the group is the inverse
transpose action, with the same orbits as A(h)^t because h ranges over
all of GL2(k). Its three projective
orbits have representatives

    eta,    e0=(1,0,0)^t,    e0+eta.                    (5)

To see this, write any vector other than a multiple of eta uniquely as
(s^2,s*t,t^2)+lambda*eta, with (s,t) nonzero. The transpose of (4) acts
on the evaluation vector by the ordinary change of the pair (s,t), and
on eta by det(g). Send (s,t) to (1,0); its stabilizer has arbitrary
nonzero determinant, so lambda can then be normalized to zero or one.

## 3. Exclude a five-space of type (2)

Because e vanishes on U in (2), one has eta in E and L contained in
eta-perp. Indeed, if eta were outside E, M eta could vary arbitrarily;
once eta belongs to E, its possible images fill L. The rank condition
e(M)=0 then forces L into eta-perp.

The actions (4) on the square coefficient lines independently normalize
L to span(e0) and E to span(e1,e2). For the domain assertion, the
annihilator of E is a coefficient line in eta-perp, so the same action
applies. Thus U becomes the full first-row/first-column space. Subtract
members of U from a member of W with e=1. The e=1 slice then contains

    M=[[0,0,1],[0,1,f],[1,h,i]],

for some fixed f,h,i. Formula (1) gives D=1, T4=0, A2=0 and hence

    det R(M)=1.                                      (6)

This contradicts geometric bounded rank. Case (2) is excluded.

## 4. Common-kernel spaces away from the middle vector

Suppose U is contained in C={M:Mv=0}, a six-dimensional compression space.
The left-kernel case follows by transposition: the literal source for M^t
is a row/column permutation of R(M)^t and has the same rank.

If v is not proportional to eta, e is a nonzero functional on C. Hence
U=C intersection {e=0}. Use (5) to normalize v to e0 or e0+eta.

For v=e0 the entire e=1 slice of W consists of matrices

    [[a,b,c],[d,1,f],[g,h,i]],

where a,d,g are fixed and b,c,f,h,i vary freely. The following determinant
identities are specializations of the literal source identity (1):

| Free entries | det R |
| --- | --- |
| b=c=f=h=0, i=1 | a^6 |
| b=f=h=i=0, c=1 | g^6 |
| after a=g=0: b=i=1, c=f=h=0 | d^5 |

Thus a=d=g=0, so every member of W kills e0 and W=C by dimension.

For v=e0+eta the e=1 slice is

    [[a+b,b,c],[d+1,1,f],[g+h,h,i]],

with a,d,g fixed and b,c,f,h,i free. The first two specializations in
the table still give a^6 and g^6. Therefore a=g=0. Taking b=t, i=1,
c=f=h=0 gives

    det R=t^5*d^2*(d^3+d+t).                          (7)

If d is nonzero, choose t outside {0,d^3+d} in k. Equation (7) contradicts
bounded rank, so d=0. Now W=C, as required. This choice over k is why
pointwise tests over a finite field do not suffice.

## 5. The middle-kernel case

Let v=eta, so C is the space with middle column zero and e annihilates C.
Now U is an arbitrary hyperplane in C. A member M0 of W with e=1 has
middle column (b,1,h)^t, a binary quadratic with two distinct roots over k.
Indeed its two partial derivatives have no common projective zero, so
its two linear factors are independent. An invertible binary substitution
sends those factors to the coordinate forms and the column to a nonzero
multiple of eta. Normalize e again to one. The e=1 slice M0+U is consequently an affine hyperplane
in the six-dimensional affine family

    M=[[a,0,c],[d,1,f],[g,0,i]].

In these six variables D=ai+cg, and the highest total-degree part of
its source determinant is

    (det R)_top = D^2*T_top^2,                        (8)
    T_top=(ai+cg)^2+a*d*f*i+a*f^2*g+c*d^2*i+c*d*f*g.

It has degree twelve. This follows directly from (1): T4=T_top+cg,
A2=df, and the only degree-eight term in G9 is T_top^2.

Neither D nor T_top has a linear factor. Both are bihomogeneous in the
two variable groups (a,d,g) and (c,f,i), with degrees (1,1) and (2,2).
Any linear factor must belong to a single group: otherwise its minimum
and maximum degrees in the first group differ, and the corresponding
width of a product is the sum of the widths in this integral domain,
whereas a bihomogeneous polynomial has width zero.

For T_top, the coefficients of i^2,c^2,ci are a^2,g^2,d^2. Their gcd is
one, so no factor involving only the first group divides T_top. The
coefficients of a^2,g^2,ag are i^2,c^2,f^2, likewise of gcd one, excluding
a factor in the second group. The same argument with the coefficients
of i,c and a,g excludes linear factors of D.

If det R vanished on an affine hyperplane, its affine linear defining
polynomial would divide det R, since the field is infinite. Its nonzero
homogeneous linear part would then divide (det R)_top. Equation (8) and
the preceding factor analysis rule this out. Thus the middle-kernel case
admits no such six-space extension.

These cases exhaust U. Every bounded-rank W is therefore a coefficient
compression space. Conversely D vanishes identically on either compression
type, so (1) makes det R vanish identically. Together with descent this
proves the theorem. The characteristic-two argument uses neither the odd
Hessian normalization nor a finite census, and supplies no tensor target
or exponent improvement.
