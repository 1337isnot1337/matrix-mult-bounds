# Disjoint unimodular units and sharp singular-space caps for every size

October23,2026. Written, unreviewed owner-directed Codex continuation.
The unimodularity argument works over every field. The linear-subspace
cap below is stated over C. No target construction or exponent gain.

## 1. Canonical source and the units

For every integer a>=1 set N=a^2(2a-1). The source coefficients are
F_(i,k,s), with0<=i,s<a and0<=k<=2a-2. Its square matrix has rows(j,p,L),
columns(H,q,r) and entries

    M_a(F)_((j,p,L),(H,q,r))=F_(H-j,p+q,L-r),             (1)

where the coefficient is zero outside its index range. The four short
indices j,p,q,r run0,...,a-1 and H,L run0,...,2a-2.

For every c,d in{0,...,a-1}, put

    F^(c,d)_(i,k,s)=1 if(i+s) mod a=c and k mod a=d,
                   0 otherwise.                        (2)

**Theorem.** Each of these a^2 integer matrix slices has determinant
plus or minus one. Their supports partition all N source coordinates.
Consequently the maximum dimension of a complex linear source subspace
consisting entirely of singular matrix slices is exactly

    N-a^2=a^2(2a-2).                                    (3)

Thus every complex source subspace of dimension greater than N-a^2
contains an invertible slice. This covers arbitrary dense subspaces
and every size a, not a finite tested range.

## 2. Factor the full source into two smaller matrices

Let h_d(k)=1 when k mod a=d and0 otherwise, and
g_c(i,s)=1 when(i+s) mod a=c and0 otherwise. Then(2) is g_c(i,s)h_d(k).
Reorder source rows as(p,j,L) and columns as(q,H,r). Equation(1) becomes

    H_d tensor K_c,

where H_d(p,q)=h_d(p+q) is an a-by-a permutation matrix. K_c has rows
(j,L), columns(H,r), each set of size a(2a-1), and entries

    K_c((j,L),(H,r))=g_c(H-j,L-r),                        (4)

again zero unless0<=H-j,L-r<a. It remains to prove K_c invertible
over every field. No Fourier roots, division by a or characteristic
restriction will be used.

## 3. Polynomial equations for a short-matrix kernel

Fix any field K and a vector v_(H,r) in the kernel of K_c. Define

    U_H(y)=sum_(r=0)^(a-1) v_(H,r) y^r,
    f_i(y)=y^((c-i) mod a).

Every U_H has degree at most a-1. For j=0,...,a-1 the output rows
(j,L) of(4) are exactly the coefficients of

    R_j(y)=sum_(i=0)^(a-1) f_i(y) U_(j+i)(y)=0.          (5)

All coefficients are retained, since the product degrees are at most
2a-2. We prove every U_H zero.

### Case c=a-1

Here f_i=y^(a-1-i). For j=0,...,a-2, consecutive equations give

    y R_j-R_(j+1)=y^a U_j-U_(j+a)=0.

The polynomial on the right can vanish with both U degrees at most
a-1 only when U_j=U_(j+a)=0. This kills indices0,...,a-2 and
a,...,2a-2. Equation R_0=0 then gives U_(a-1)=0. At a1 the consecutive
range is empty and R_0=U_0=0 proves the assertion directly.

### Case 0<=c<=a-2

For1<=i<=a-1, one has y f_i-f_(i-1)=0 except at i=c+1, where it is
y^a-1. Also y f_0=f_(a-1)=y^(c+1). Therefore, for j=0,...,a-2,

    y R_j-R_(j+1)
      =y^(c+1)(U_j-U_(j+a))+(y^a-1)U_(j+c+1)=0.        (6)

Since y^(c+1) and y^a-1 are coprime over every field, U_(j+c+1) is
divisible by y^(c+1). Write it y^(c+1)V_j. Cancelling that factor in
(6) gives

    (y^a-1)V_j=U_(j+a)-U_j.

The right side has degree at most a-1. A nonzero left side has degree
at least a. Thus V_j=0, and for every j in0,...,a-2 we have

    U_(j+c+1)=0,        U_(j+a)=U_j.                    (7)

The first identities kill a-1 consecutive indices c+1,...,c+a-1.
Together with the second identities, this kills every residue class
modulo a except c. The only possibly nonzero polynomials are U_c and
U_(c+a), which are equal. In R_0 the sole surviving summand is
f_c U_c=U_c, so it too is zero. This proves the kernel trivial.

These arguments use only polynomial degree, divisibility and the
nonzero constant term of y^a-1. They apply in positive characteristic,
including when the characteristic divides a.

## 4. Integer unimodularity

For fixed a,c the square integer matrix K_c is invertible over every
field by Section3. Its determinant is a nonzero integer by the Q case.
If that integer had any prime divisor p, reduction modulo p would make
K_c singular over F_p, contradicting the same proof. Its determinant
is therefore plus or minus one. The permutation H_d and the source
row/column reorderings also have unit determinants. This proves the
unimodularity assertion for every full matrix in(2).

The supports partition all N coefficients because every(i,k,s) has
exactly one residue pair(c,d). There are a^2 such parts.

## 5. The sharp all-subspace cap

Give coefficient(i,k,s) weight

    w=i+a k+a(2a-1)s.

These are exactly the N distinct integers0,...,N-1. In(1) the weight
decomposes as

    (-j+a p+a(2a-1)L)+(H+a q-a(2a-1)r).

The diagonal coefficient action therefore multiplies the full source
matrix by invertible diagonal Laurent row and column matrices for
nonzero parameter. It preserves rank and the closed singular cone.

Apply the elementary distinct-weight packing lemma in the
[A4 source-cap proof](../2026-10-23-source-singular-space-cap/proof.md),
Section2. A row-echelon limit takes every all-singular complex subspace
to a coordinate all-singular subspace of the same dimension. The a^2
disjoint unit supports force at least a^2 missing coordinates. Hence
dim W<=N-a^2.

For sharpness choose source row(j,p,L)=(0,0,0). Its only potentially
nonzero entries are the a^2 independent coefficients F_(H,q,0), with
0<=H,q<a, on distinct columns(H,q,0). Setting those coefficients to
zero gives an all-singular source subspace of dimension N-a^2. This
proves(3), including the zero-dimensional cap at a1.

The rank-preserving limit is a proof about every complex subspace; no
finite sample or torus-coordinate search supplies that quantifier alone.

## 6. Consequence and limitations

The a4 instance recovers the sharp96-dimensional source cap and its
previously written first-map leading-rank consequence. The new theorem
provides the source cap at every size. It does not show that arbitrary
target degenerations have regular maps, large leading images or the
partial long frames required by the Laurent obstruction. Nor does it
give matrix targets at the cap. The exponent below9/4 remains unproved.

The source convention, earlier single unimodular slice and A4 packing
and diagonal-limit proof retain their credits and exact pins. The
all-field short-kernel recurrence and all-size disjoint unit theorem
are local owner-directed Codex continuations. No new external theorem
is imported. Finite exact controls support the written proof without
formalizing its all-size or all-subspace quantifiers.
