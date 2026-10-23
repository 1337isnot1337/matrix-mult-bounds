# The rank-six locus and sharp critical compression dimension

October 23, 2026. Owner-directed OpenAI Codex work. Written and unreviewed.
No exponent improvement, independent review, or formalization is claimed.

Claim `AI-RESOLVENT-RANK-SIX-LOCUS-001` answers the rank-six classification
question left by the [minimum-rank package](../2026-10-23-resolvent-minrank/proof.md).
That package and PR103 retain credit for the source, fixed resolvent, limiting
space, minimum-rank theorem, and previous compression alignment. Exact source
versions and byte hashes are recorded in `sources.json`.

## 1. Statement and coordinates

Use the predecessor's 112-dimensional space W over a field F. Its matrices
act on V=F^112, decomposed into four blocks of dimension 28. The outer source
has rows (j,L), columns (H,r), and

    S(f)[(j,L),(H,r)] = f[H-j,L-r],

where j,r,i,s range from 0 to 3 and H,L from 0 to 6; unavailable coefficients
are zero. Set f* = sum_{i+s=3} e_is, K=S(f*), G(f)=K^-1 S(f), and
Q(f)=G(e00)G(f). Both K and K^-1 are integer matrices with determinant a unit.
All row and column indices below are zero-based and lexicographic.

Left multiply W by D=diag(K,K,K,K). The resulting space W' has the blocks:

- diagonal blocks all equal to a scalar times K;
- first lower block diagonal equal to S(g2);
- second lower block diagonal equal to S(g1);
- block (3,0) equal to S(g0)+T(f3), where T(f)=S(e00)K^-1 S(f);
- blocks (3,1),(3,2),(3,3) equal to T(f4), T(f5), T(f6), respectively.

The listed terms are added if they share a block. The predecessor proves that
a nonzero scalar or nonzero g2 or g1 forces rank at least 16: inspect blocks
(0,0), (1,0), and (2,0) in that order. A nonzero scalar actually gives rank
at least 28. Each nonzero S(g) has rank at least 16 over every field.

Let F6 be the coordinate subspace of F^28 on rows

    R = {0,7,14,21,22,23}.

Define five matrices

    T_i = T(e_i0),                         0 <= i <= 3,
    T_4 = T(e13+e22+e31) - S(e10).

The theorem is:

1. The rank-at-most-six locus of W is a 17-dimensional linear subspace Z.
   In W' coordinates, its only nonzero block row is the last one. Block (3,0)
   lies in span(T_0,...,T_4), and each other block lies in span(T_0,...,T_3).
2. Every nonzero member of Z has rank exactly six and the same image
   E = D^-1(0 direct-sum 0 direct-sum 0 direct-sum F6).
3. Over an algebraically closed field, for every P of size 110 by 112 and C
   of size 112 by 110, both of rank 109, the space PWC has dimension at least
   111. This is sharp. Its dimension is 111 exactly when there is a nonzero
   X in Z with ker(P) contained in E and im(C)=X^-1(ker(P)). Such X is unique
   up to a nonzero scalar. Otherwise the dimension is 112.

Parts 1 and 2 hold over every field. The explicit compression attaining 111
also works over every field. The universal lower bound and uniqueness in
part 3 use algebraic closure; no extension to arbitrary fields is claimed.

## 2. Exact classification of the mixed outer block

The relation T(f*)=S(e00) permits the gauge

    f' = f-f03 f*,       g' = g+f03 e00.

The mixed matrix S(g)+T(f) is unchanged, and f'03=0. Order its 31 parameters
by the 16 g coefficients followed by the remaining 15 f coefficients.

The certificate contains 26 successive seven-by-seven minors. At each stage,
the selected submatrix is lower triangular, and all diagonal entries equal
a specified linear form ell up to signs. Thus the determinant is +/-ell^7.
If the matrix has rank at most six, ell=0 over any field. One coefficient
of ell is +1 or -1, so this equation eliminates a parameter without division
by a nonunit. The next certificate stage applies after that substitution.

After all 26 stages, the remaining matrix is exactly

    a0 T_0 + a1 T_1 + a2 T_2 + a3 T_3 + t T_4.

In the gauged source parameters this is

    g' = -t e10,
    f' = sum_i ai e_i0 + t(e13+e22+e31).

The verifier checks every above-diagonal zero, every signed diagonal form,
every unit substitution, and equality of all 28-by-28 entries with these
five displayed matrices. This is a finite polynomial-identity certificate,
not extrapolation from rank samples.

Each displayed matrix is supported on the six rows R. Hence every linear
combination has rank at most six. Five further successive six-by-six minors
eliminate all five parameters whenever rank is at most five. Their pivots
and diagonal factors are again units. This proves that the five matrices
are independent and that every nonzero combination has rank exactly six.
Its image is therefore exactly F6.

For the pure high block T(f), set the original g=0. The gauge gives
g'=f03 e00, whereas the reduced form requires g'=-t e10. Since e00 and e10
are independent, f03=t=0. Therefore

    rank T(f) <= 6  iff  f belongs to span(e00,e10,e20,e30).

Every nonzero such block has rank six and image F6. This also proves that
there is no additional high-block direction hidden by the mixed gauge.

## 3. The full locus

A matrix of W' with rank at most six has zero scalar, g2, and g1 by the
source rank bound in Section 1. Only its final block row remains. Each
of its four blocks has rank at most six, so Section 2 puts the first block
in the displayed five-space and each other block in the four-space.

Conversely, every matrix in that 17-dimensional block space has image in
the six-dimensional final copy of F6. If it is nonzero, at least one block
has rank six by Section 2. Hence the entire matrix has rank six and image
exactly that copy of F6. Independent matrices in distinct input blocks are
independent, proving the dimension 5+4+4+4=17. Applying D^-1 proves parts
1 and 2 in the original coordinates.

## 4. Critical compressions lose at most one direction

Let U=im(C) and L=ker(P), so dim U=109 and dim L=3. Write H for the kernel
of the linear compression map W -> PWC. For any nonzero X in H, the
elementary rank-loss inequality gives

    rank X <= (112-rank P)+(112-rank C) = 6.

Part 1 forces X in Z and rank X=6. Restriction to U lowers rank by at most
three, while X(U) is contained in L. Thus rank(X|U)=3, X(U)=L, and
ker(X) is contained in U. Consequently

    L contained in E,       U=X^-1(L).

Conversely these conditions imply PXC=0.

It remains to bound dim H. Assume H is nonzero, so L is a subspace of E.
For every X in H, quotienting its output by L gives a well-defined map

    A_X : V/U -> E/L.

Both spaces have dimension three. For every nonzero X in H, its image is
all of E and its inverse image of L is exactly U, so A_X is an isomorphism.
The assignment X -> A_X is linear and injective: A_X=0 would put im X
inside L, contradicting rank X=6 for nonzero X.

If X,Y in H were independent, det(A_Y+t A_X) would be a polynomial in t
of degree three with nonzero leading coefficient. Over an algebraically
closed field it has a root. At that root Y+tX remains nonzero, but its
induced map is singular, a contradiction. Therefore dim H <= 1 and
dim PWC = 112-dim H >= 111. The same argument gives the claimed uniqueness.
This elementary determinant argument is a written proof, not a claim of
machine formalization or an inference from the finite control.

## 5. Explicit sharp compression

Work in the W' coordinates. Let L' be the span of coordinate vectors
105,106,107 (rows 21,22,23 of the final block). Let U be the coordinate
subspace obtained by deleting input coordinates 3,7,11. Let P' select the
109 other output coordinates, with a zero row appended, and let C inject
the 109 selected input coordinates, with a zero column appended. Set P=P'D.
Both P and C have rank 109 in every characteristic.

The matrix X' with only block (3,0)=T_0 is killed by P'X'C. Indeed its
remaining nonzero rows 0,7,14 in that block have their only nonzero entries
in the deleted columns 3,7,11. Thus X=D^-1 X' is a nonzero lost direction.

The verifier separately constructs all 112 basis matrices of W', deletes
the indicated rows and columns, and row-reduces their flattened images.
It obtains 111 pivots, each +1 or -1 before normalization, and one zero
generator after elimination. These integer operations certify dimension
111 over every field. They check the explicit example independently of
the algebraic-closure argument for arbitrary compressions.

## 6. Scope

This determines the rank-six locus of the fixed space W and its critical
constant-compression behavior. It does not classify all singular Laurent
trajectories or prove that a compressed space is a matrix-multiplication
tensor. The prior broader regular-long-leg exclusions remain in force.
No smaller exponent or new target construction follows from this result.
