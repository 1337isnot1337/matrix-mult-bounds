# A singular-unit resolvent obstruction on an open compression chart

October 21, 2026. Claim `AI-CYCLIC-SINGULAR-RESOLVENT-001` is a written,
unreviewed argument with an exact finite rank witness. The general A4
degeneration and the exponent question remain open.

## Source and fixed ansatz

Use the literal A4 source from the maintained
[cyclic source convention](../2026-10-20-koszul/cyclic_finite_target.md),
Sections 2-3, and the explicit
[unimodular source unit](../2026-10-21-cyclic-slice-determinants/proof.md).
Both are pinned at main 39378de5. Source legs have dimension 112 and
minimum nonzero ordinary matrix-slice rank 16 over every field.

Let M(F) be the source slice, let F0(i,k,s) be one exactly when i+s=3 and
k=3, and put

    H(F)=M(F0)^(-1)M(F),       N=H(e_(0,0,0)).

Then H(F0)=I112, rank N=16, and N^2=0. Fix any constant complex matrices

    P: C^112 -> C^110,      C: C^110 -> C^112,      PC=I110.

Consider the resolvent ansatz

    B(t)=P(tI112+N)^(-1)=t^(-1)P-t^(-2)PN.             (1)

The first-leg map is any linear map with finite Laurent coefficients.
The other long map is the constant C. The regular source unit lift
e_(0,0,0)+tF0 has a singular limiting slice of rank 16, and (1) sends its
slice to I110 exactly. Thus the regular-invertible-unit hypothesis of
the earlier all-order chart obstruction is not satisfied.

Define the 48-dimensional source coefficient space L+ by k<3 and the
64-dimensional space L0- by k>=3. Let V(P,C) be the matrix space spanned by

    PN H(f) C,       f in L0-,
    P H(g) C,        g in L+,
    I110.                                               (2)

**Statement.** If dim V(P,C)=112, the ansatz (1) cannot degenerate A4 to
M(10,10,11), even with arbitrary Laurent first-leg maps and constant
changes of target bases. The rank condition holds on a nonempty Zariski
open subset of the variety PC=I110. It therefore excludes an open dense
set of constant compression pairs in this specific ansatz.

Pairs with dim V<112 are not excluded by this argument. Neither are
moving P(t), C(t), higher corrections to (1), or other singular unit
trajectories. No construction is supplied in those remaining cases.

## The source grading

In normalized source column order (H,q,r), with H in 0,...,6 and q,r in
0,...,3, put

    J_d = span of the coordinates with q>=d.

Thus dim J_d=28(4-d), J_0=C^112 and J_4=0. The source formula has middle
indices p+q=k. The unit F0 pairs p with q'=3-p. Multiplying by its inverse
therefore makes a middle-k coefficient send q to q'=q+3-k. In particular,

    H(L+) J_d is contained in J_(d+1),
    im N is contained in J_3,        N J_1=0.             (3)

These give N^2=0. Its rank is 16 because it is an invertible left
multiple of the coordinate source slice attaining the known minimum.
The verifier also checks the grade shift on every nonzero entry of all
112 normalized coefficient matrices, over the integers.

## The complete limiting matrix space under the rank hypothesis

Absorb the invertible Laurent scalar -t^(-2) from (1) into the unrestricted
first map. It suffices to consider

    A_t(f)=P(N-tI)H(f)C.                                 (4)

Every generator in (2) is the limit of a regular matrix curve in the
Laurent span of (4). For f in L0-, use A_t(f). For g in L+, (3) gives
NH(g)=0, so use -t^(-1)A_t(g)=PH(g)C. Finally,

    A_t(e_(0,0,0)+tF0)=-t^2 I110,                        (5)

which supplies the identity curve after division by -t^2.

The Laurent-field span of (4) has dimension at most 112. It has exactly
112: N-tI is invertible, and the two codimension-two maps lose at most
four from the minimum source slice rank 16. Thus no nonzero source
coefficient over C((t)) is killed. The minimum-rank proof holds over this
field as well.

If dim V=112, choose 112 of the regular curves above with independent
constant coefficients. They form a basis of the Laurent span of (4).
Any regular matrix curve in that span is a Laurent linear combination
of them. Its coefficients cannot have a pole: the leading coefficient
of a pole would give a nontrivial relation between their independent
constant matrices. All coefficients are therefore regular, and the
limit belongs to V. Conversely each generator of V is attained. Thus V
is the entire limiting first-leg slice space, including all finite
Laurent orders in the first map.

There are 113 displayed generators in (2), but at least one relation.
The nonzero matrix PNC is both a high generator combination H(F0)=I and
a low generator H(e_(0,0,0))=N. It is nonzero because its rank is at least
16-2-2=12. Hence dim V<=112 for every pair PC=I.

## An invariant subspace of forbidden dimension

Let K=ker P, of dimension two. Choose the largest m with K contained in
J_m. This exists and lies in {0,1,2,3}.

For m<=2 set U=PJ_(m+1). Since K is not contained in J_(m+1),

    dim U = 28(3-m)-dim(K intersect J_(m+1)),
    dim(K intersect J_(m+1)) is 0 or 1.                  (6)

The possible dimensions are 83,84,55,56,27,28. Each high generator in
(2) has image in Pim N, which is contained in PJ_3 and hence in U. For
z in J_(m+1), CPz-z belongs to K, so CPz belongs to J_m. By (3), every
low generator sends Pz into PJ_(m+1)=U. The identity also preserves U.
Thus all of V preserves U.

If m=3, take U=Pim N. Its dimension is 16-dim(K intersect im N), so it
is 14,15 or 16. Now CP(im N) is contained in im N+K, which lies in J_3.
Every H(g), g in L+, kills J_3. Low generators therefore kill U; high
generators have image in U, and the identity preserves it.

In all cases V has a nonzero proper invariant subspace of dimension in

    {14,15,16,27,28,55,56,83,84}.                        (7)

None of these dimensions is divisible by 10.

## Why this excludes the target space

Suppose V contained a row/column equivalent copy T of the slice space
Mat10 tensor I11. It has an invertible member G corresponding to the
identity matrix. Both T and G preserve U, and G invertible implies
G(U)=U and G^(-1)(U)=U. Hence G^(-1)T preserves U. This normalized space
is an algebra conjugate to Mat10 tensor I11.

For any unital Mat10 action on U, the ten diagonal matrix units split U
as the direct sum of their images. The off-diagonal matrix units give
isomorphisms between these ten images. Their dimensions are equal, so
dim U is divisible by 10. This contradicts (7). This elementary module
argument requires no choice of canonical leading flag or target basis.

Together with the complete limiting-space argument, this proves the
stated all-order first-map obstruction under dim V=112.

## Exact witness and openness

For one explicit pair, let C include all source coordinate columns
except positions 4 and 5 (zero based) and let P be the matching row
projection. They satisfy PC=I. The source-coordinate order is (H,q,r).
The verifier builds all normalized source coefficient matrices over Z,
checks the inverse over Z in both orders, and forms the 113 generators.

The saved certificate selects 112 generators and 112 flattened matrix
entries. The resulting square minor has rank 112 modulo 1009. Its
integer determinant is therefore nonzero, proving dim V>=112 over C.
The preceding upper bound proves equality. The explicit pair also
preserves Pim N of dimension 16; this is replayed over Z with unit-pivot
elimination. The universal invariant argument above supplies the other
pairs and their possible dimensions, rather than extrapolating from the
single finite witness.

Entries of (2) are polynomial in P,C, so rank 112 is open on PC=I. It is
nonempty by the witness. This parameter variety is irreducible: GL112
acts transitively by (P,C)=(P0 Q^(-1),Q C0), since a basis of ker P can
complete the columns of C to Q. As an image of irreducible GL112 it is
irreducible. The nonempty open set is therefore dense.

The certificate proves one nonvanishing minor and verifies finite source
identities. It does not formalize the limiting-space or universal
invariant-subspace proof. Those are written arguments without independent
review. The source convention, minimum rank and unimodular unit are
imported maintained results; standard linear algebra and matrix-unit
module theory are not claimed as historical novelties. No tensor map or
improved exponent is established.
