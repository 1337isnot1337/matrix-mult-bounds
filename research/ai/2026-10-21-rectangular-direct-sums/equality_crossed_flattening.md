# Equality forces a low-rank crossed coefficient flattening

October 21, 2026. Written proof, unreviewed. This is a necessary condition
for source slices and supplies no tensor restriction or exponent improvement.

Use the source conventions of `polynomial_rank_locus.md` in the maintained
anisotropic package. For the polynomial Hankel symbol B_F(x,z), let its
rational-function rank be r. Define the crossed coefficient flattening

    T_F[(p,s),(q,i)] = F_(i,p+q,s),
    p<a, s<b, q<b, i<a.

**Claim.** If rank(M_F)=ab r, then rank(T_F)=r.
This holds also at full symbol rank r=min(a,b). It does not assert that
all long-coordinate coefficients share a fixed length-r scheme.

## Proof

Write K(x)^T for the inner full coefficient map in z. The maintained
polynomial injections give rank(M_F)>=b rank(K)>=ab r. Equality forces
rank(K)=ar and equality in the outer coefficient map for K(x).
The coefficient-map equality lemma in `parity_structure_equality.md`
implies that all columns of K(x) are constant linear combinations of ar
independent columns. Hence its row space, equivalently the image of
K(x)^T, is a fixed ar-dimensional coefficient subspace E, independent of x.
Here coefficient vectors in E are vector polynomials in z, with a entries.

Choose a constant x_0 at which rank(K(x_0))=ar and rank(B_F(x_0,z))=r.
Such constants exist by nonvanishing of finitely many polynomial minors.
Choose r columns C_1(z),...,C_r(z) of B_F(x_0,z) independent over C(z).
Their products z^j C_l, 0<=j<a, are linearly independent and belong to E.
There are ar of them, so they form a basis of E.

Consider the core

    E^- = {v(z) : z^j v(z) is in E for every 0<=j<a}.

Every v in this core expands uniquely as sum_l C_l(z) p_l(z), deg p_l<a.
The same is true for z^(a-1)v. Independence of the C_l over C(z) forces
z^(a-1)p_l to have degree below a, hence every p_l is constant. Therefore
E^- is precisely the r-dimensional constant span of the C_l. This proof
also works after extending constants from C to C(x).

Every column of B_F(x,z), together with all its shifts of order below a,
lies in E over C(x), since these shifts are columns of K(x)^T. Consequently

    B_F(x,z) = C(z) R(x)

for a fixed a-by-r polynomial matrix C(z) and an r-by-b matrix R(x).
The coefficients of R can be recovered by a constant left inverse of the
coefficient matrix of C, so R is polynomial in x with the original degree
bound. Expanding coefficients gives rank(T_F)<=r. Conversely, specializing
the two polynomial variables contracts T_F to B_F, so its rank is at least
r. This proves the claim. The zero case is immediate.

## Application to the unresolved A(8,9) target

For M30 plus M3, the rank-at-most-three parameters of the large block lift
to source rank at most576. If their generic symbol rank is eight, the claim
forces crossed rank at most eight on that dense open set, hence on the
whole rank-at-most-three parameter variety by closedness of minors.
If their generic symbol rank is at most seven, the strengthened projection
argument in `saturation.md` instead forces the entire900-dimensional block
into the certified cap504, which is impossible. Thus every proposed ordinary
map for this target must send rank-at-most-three parameters to crossed
flattenings of rank at most eight.

This is not yet an exclusion: injective linear maps from Mat30 into Mat72
can satisfy this rank condition in isolation, for example ordinary padded
identity embeddings. Their compatibility with the source Hankel structure
and all three target legs is a separate unresolved problem.
