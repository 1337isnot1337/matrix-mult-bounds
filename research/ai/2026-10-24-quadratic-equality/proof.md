# Odd-characteristic geometric quadratic equality spaces

Status: proof written and unreviewed, October 24, 2026. This is owner-directed
Codex work, with a separate same-session audit of the October 23 scratch.
Neither that audit nor exact arithmetic supplies independent review. No tensor
target or improved matrix-multiplication exponent is claimed.

## Theorem and literal source

Let K be any field of characteristic different from two. For M in Mat_3(K),
write f_M(x,z)=sum M[i,s] x^i z^s, with 0<=i,s<=2. Its literal source R(M)
is the 15-by-15 matrix with rows (j,L), 0<=j<=2, 0<=L<=4, and columns (H,r),
0<=H<=4, 0<=r<=2, each pair in lexicographic order, and entries

    R(M)[(j,L),(H,r)] = M[H-j,L-r],

where coefficients outside 0,...,2 are zero. Suppose W is a six-dimensional
K-linear space and rank R(M)<=14 for every M in W after algebraic closure.
Then, for a nonzero vector v in K^3, either

    W={M:Mv=0}  or  W={M:v^t M=0}.

Conversely every such space has dimension six and satisfies the geometric
rank bound. The hypothesis is polynomial vanishing of det R on W; testing
only the K-rational points does not replace it over a finite field.

The previously written all-field cap-six theorem establishes maximality.
This note classifies the equality spaces in odd characteristic. It does not
classify characteristic-two equality spaces or linear families in larger
coefficient blocks. The result concerns rank at most fourteen; members of
these spaces can have lower rank.

## Claim and reduction

Let k be algebraically closed of characteristic other than two. At every
invertible point of the residual source-determinant hypersurface, its second
fundamental quadratic form on the eight-dimensional tangent hyperplane has rank
at least five. It follows that a six-dimensional linear space of coefficient
matrices with geometric source rank at most fourteen has coefficient determinant
identically zero. The elementary equality classification of singular 3-by-3
spaces then says it has a common kernel vector or a common left-kernel vector.

Use the pinned determinant package's invertible linear change from the monomial coordinates to an
ordinary Gram matrix. Write the resulting matrix as N. The local defining
function may be taken to be

\[
 f(N)=\det(2Q-\operatorname{tr}(Q)I),\qquad Q=(NN^t)^{-1}.
\]

Using the left Gram matrix here is legitimate: (NN^t)^(-1) and (N^tN)^(-1)
are similar, and f depends only on their characteristic coefficients. The pinned proof, Section 8, gives Delta(M)=4096 Delta0(N) and
Delta0(N)=det(NN^t)^3 f(N). Both multipliers are units at an invertible
point in odd characteristic. On the tangent hyperplane their
quadratic terms therefore differ only by a nonzero scalar.

Put S=2Q-tr(Q)I. At a point where f=0, the identities already established in
the cap proof give rank(S)=2, and, for U=adj(S), tau=tr(U) is nonzero. The
rank-one operator U/tau is a symmetric idempotent. Its image is consequently a
nonisotropic line: if a nonzero vector spanning that line were isotropic, the
associated rank-one symmetric operator would have square zero rather than be
idempotent. After an orthogonal change of basis, this line is the first
coordinate. Since SU=0 and Q commutes with U, we have

\[
 Q=\begin{pmatrix}\mu&0\\0&B\end{pmatrix},\qquad
 B=B^t\in\operatorname{Mat}_2(k),\quad
 \operatorname{tr}B=\mu\ne0,\quad d=\det B\ne0.
\]

Here mu=tr(Q)/2 is nonzero by the identity 8det(Q)=tr(Q)tau. No diagonalization
of B is required, so the argument includes nonsemisimple symmetric B.

## Exact tangent quadratic

Use a left perturbation N(z)=(I+zF)N, and write

\[
 F=\begin{pmatrix}x&p^t\\q&C\end{pmatrix},\qquad p,q\in k^2.
\]

Modulo z^3, the inverse Gram matrix is Q+zQ1+z^2Q2, where

\[
 Q_1=-F^tQ-QF,\qquad
 Q_2=(F^t)^2Q+F^tQF+QF^2.
\]

The linear coefficient of f(N(z)) is
8d*(tr(BC)-mu*x). It is a nonzero functional, so the tangent condition is

\[
 \mu x=\operatorname{tr}(BC).
\]

At z=0 the lower-right block of S is 2B-2mu I=-2adj(B). Its determinant is
4d. Divide the determinant locally by the determinant of this block and use its
Schur complement as a local defining function. Its quadratic coefficient on
the tangent hyperplane is the sum of two quadratic forms on independent
variable sets:

\[
\begin{split}
 q_C(C)={}&\frac3\mu\operatorname{tr}(BC)^2
             -\operatorname{tr}(C^tBC)-2\operatorname{tr}(BC^2),\\
 q_4(p,q)={}&q^tBq-\mu p^tp+2p^t(\mu I-B)q
            +\frac2d(\mu p+Bq)^tB(\mu p+Bq).
\end{split}
\]

Indeed, the Schur complement coefficient before imposing the tangent condition
is `(Q2)11-tr((Q2)22)+(2/d)*(Q1)12*B*(Q1)21`; substituting the displayed Q1,Q2
gives these formulas. Equivalently, the coefficient of z^2 in the original
3-by-3 determinant f(N(z)), on the tangent hyperplane, is exactly
`4d*(q_C+q_4)`. The maintained verifier checks this latter identity directly by
column multilinearity of the determinant, without using the Schur complement
to calculate that coefficient.

## The four-dimensional block

Set r=p+q. By the 2-by-2 Cayley-Hamilton relation B^2=mu B-d I,

\[
 q_4=r^tP r-2r^tBq-q^t\operatorname{adj}(B)q,\qquad
 P=-\mu I+\frac{2\mu^2}{d}B.
\]

The q-block is invertible. Its Schur complement is K/d, where

\[
 K=(3\mu^2-d)B-2\mu d I,\qquad
 \det K=d(d^2+3\mu^4).
\]

Consequently rank(q4)>=2; if d^2+3mu^4 is nonzero, then rank(q4)=4.

## The C-block

Adding a scalar multiple of I to C does not change qC, including its mixed
terms with any C. Since the characteristic is not two, C splits uniquely into
a tracefree matrix and a scalar matrix. Thus the rank of qC equals the rank of
its restriction to the three-dimensional tracefree space. Write

\[
 B=\begin{pmatrix}u&v\\v&w\end{pmatrix},\quad
 C=\begin{pmatrix}y&z\\h&-y\end{pmatrix},\quad \mu=u+w.
\]

The symmetric coefficient matrix of the quadratic form mu*qC on (y,z,h) is

\[
 T_C=\begin{pmatrix}
 -12uw&4uv-2vw&2uv-4vw\\
 4uv-2vw&-u^2-uw+3v^2&-u^2-2uw+3v^2-w^2\\
 2uv-4vw&-u^2-2uw+3v^2-w^2&-uw+3v^2-w^2
 \end{pmatrix}.
\]

Direct expansion gives

\[
 \det T_C=12\mu^2d(\mu^2-d).
\]

Furthermore qC([[0,1],[-1,0]])=mu, so rank(qC)>=1 in every odd
characteristic, including characteristic three.

If d^2+3mu^4 is nonzero, the combined tangent quadratic has rank at least
4+1=5. If it is zero, the characteristic cannot be three because d is nonzero.
Also d cannot equal mu^2, since that would imply 4mu^4=0. Thus in this case
det(TC) is nonzero and rank(qC)=3, while rank(q4)>=2. Again the combined rank
is at least five. This covers every odd characteristic without dividing by
three or seven.

The bound five is attained in the local forms in characteristics three and
seven: take B=I, so mu=2 and d=1. In characteristic three the two block ranks
are (4,1); in characteristic seven they are (2,3). Therefore a proof claiming a
uniform rank six or seven would be false.

## Consequence for six-dimensional equality spaces

Suppose W has dimension six, has source determinant identically zero, and
contains an invertible coefficient matrix. Since its polynomial ring is a
domain, the universal determinant factorization forces the residual factor to
vanish identically on W. Choose an invertible member and work at its normalized
image N. Because W is linear, its six-dimensional direction space is contained
in the eight-dimensional tangent hyperplane, and the tangent quadratic vanishes
identically on it.

In characteristic different from two, polarization then makes the quadratic
form's symmetric coefficient matrix zero on the 6-by-6 block associated with
this subspace. Such an 8-by-8 matrix has rank at most four: the remaining two
rows and columns span a matrix of rank at most four. This contradicts the rank
at least five just proved. Hence no invertible member exists.

## Singular six-spaces and descent

For completeness the singular-space equality lemma used here is proved over
an algebraically closed field k in any characteristic. This extends the
same argument in Section 9 of the pinned determinant proof beyond the
characteristic-two setting where it was first needed.

A linear space of matrices of rank at most one has dimension at most three.
Fix a nonzero member u0*v0^t. Every other nonzero rank-one member u*v^t
has u proportional to u0 or v proportional to v0; otherwise their sum has
rank two by bases for the two independent left and right pairs. The space
lies in the union of the two three-dimensional spaces with one factor fixed.
A linear space contained in a union of two linear subspaces is contained in
one: the sum of a member of each set difference would lie in neither.

Now let U be a six-dimensional singular coefficient space. It contains a
rank-two member. Change domain and codomain bases to make that member
A=diag(1,1,0). These arbitrary GL3 changes classify coefficient matrices
only; they are not asserted to preserve the source-rank condition. For
B in U, the linear coefficient of det(A+tB) makes b33=0. Write

    B=[[P,u],[v^t,0]],
    det(A+tB)=-t^2 v^t u-t^3 v^t adj(P)u.

The image I of U under B -> (u,v) is isotropic for q(u,v)=v^t u. Its polar
form ((u,v),(u',v')) -> v^t u'+v'^t u is nondegenerate over every field.
Thus dim I<=2. The projection kernel has dimension at most four, since
only P varies. Equality dim U=6 forces both bounds to be equalities and
the kernel contains every P. Hence, for each (u,v) in I, the identity
v^t adj(P)u=0 holds for all P. The two-by-two adjugate is a linear bijection,
so u=0 or v=0. The union-of-two-subspaces argument forces I to be one
coordinate plane. Therefore U is all matrices with last column zero or
last row zero in the temporary bases. Undoing these bases proves the
common-kernel or common-left-kernel classification.

Apply this lemma to the six-space whose coefficient determinant was shown
to vanish in the preceding section. Conversely a common-kernel or
common-left-kernel space has det M identically zero, so the pinned universal
identity 2048 det R=det M * Delta makes det R zero in odd characteristic.

Finally this description descends from the algebraic closure to K. For a
K-basis M1,...,M6 of W, the common kernel is the nullspace of the stacked
matrices Mi, a matrix over K. Its dimension is unchanged by scalar extension.
A nonzero common kernel over the closure therefore gives a nonzero common
kernel over K. The same argument applies to the transposed matrices for
the other type. The full space killing a fixed nonzero K-vector has dimension
six, so containment of W is equality. This proves the stated theorem over K.

## Verification record and remaining boundary

`verify.py` verifies the exact tangent coefficient identity by
a separate expansion of the 3-by-3 determinant, the change r=p+q, det(K),
det(TC), and the nonzero skew value. Its five retained bounded modular controls are:

| characteristic | B | rank(q4) | rank(qC) | total |
| --- | --- | --- | --- | --- |
| 3 | I | 4 | 1 | 5 |
| 5 | diag(1,2) | 4 | 3 | 7 |
| 5 | [[1,1],[1,0]] | 4 | 3 | 7 |
| 7 | I | 2 | 3 | 5 |
| 13 | diag(1,2) | 3 | 3 | 6 |

The non-diagonal B over F5 has repeated eigenvalue with a nonzero nilpotent
part, so it explicitly controls one nonsemisimple case. All controls meet
mu*d!=0. These samples check implementations and exceptional arithmetic;
the uniform rank bound follows from the exact formulas and case split.

These five inputs are inherited scratch controls, not new discovery cases.
The exact symbolic identities hold over Z[1/(2*mu*d)] and support the
all-odd-characteristic argument without reducing a rational identity through
an excluded denominator. The verifier also checks the differential and the
scalar radical of the C-block.

The unresolved boundary is characteristic-two equality classification. The
current char2 cap argument gives a five-dimensional singular intersection
with e=0 for a hypothetical noncompression equality space, and the
six-dimensional singular-space equality lemma does not classify that
intersection. No characteristic-two equality claim follows from this file.
