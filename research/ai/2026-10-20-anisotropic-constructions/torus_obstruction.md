# The diagonal-torus construction class is excluded

October 20, 2026. Written argument with exact finite controls. No claim of
independent mathematical review, arbitrary-degeneration exclusion, or
improvement in the exponent is made.

The numerical torus runs preceded this obstruction. Their residuals were
large, and they supplied no construction. The argument below explains why
ordinary maps in the specified class cannot solve the selected target.

## 1. The source and the target action

Use the source coordinates in the package README. Give its three legs
weights

    k-i-s,  L-j-p,  H-q-r.

Every source term has total weight zero. For A(4,5), each source leg has
weight multiplicities

    (1,3,6,10,14,17,19,20,19,17,14,10,6,3,1)

at the integer weights -7 through 7. On M(12,12,13), use vertex weights
u_i,v_j,w_k and the induced weights u_i-v_j,v_j-w_k,w_k-u_i.
The construction class consists of constant maps preserving these spaces,
for any integer choices of the vertex weights. It permits dense mixing
inside each weight space. It does not permit mixing different weights or
a parameter-dependent singular limit.

The two target legs of dimension 156 leave total dimension defect four.
For either such leg, its difference-character polynomial must equal the
source-character polynomial minus four monomials, with repetitions allowed.
`general_weight_assignments.py` factors all such nonnegative polynomials.
The separate integer recursion in `audit_torus_weights.py` reconstructs
their factors without a polynomial factorization library. It confirms:

- 2,819 nonnegative defect polynomials;
- 73 compatible pairs with vertex dimensions 12 and 13;
- 68 normalized profiles for the 13-dimensional vertex;
- exactly two complete triples, up to swapping the two size-12 vertices.

The complete triples use every one of the 20 source coordinates at weight
zero on every leg. Both target central tensors have a nonzero rank-one
slice. This last fact follows directly from a common vertex weight with
multiplicities one on all three vertices. The saved profiles provide
the finite arithmetic evidence. No finite search over coefficient maps
is involved in this enumeration.

## 2. Exact minimum slice rank of the central source block

The weight-zero coordinates are X=(i,i+s,s), Y=(j,p,j+p), and
Z=(q+r,q,r). Thus the central source has dimension ab on every leg.
For a first-leg slice f=(f_(i,s)), its matrix, with rows (j,p) and
columns (q,r), has entries

    f_(q+r-j, j+p-r),

where out-of-range coefficients are zero. Assume 1<=a<=b. The minimum
rank of a nonzero such matrix is exactly a, over every field.

Choose a degree k with a nonzero coefficient f_(i,k-i). Let i0 be the
largest such first index and put s0=k-i0. Set

    p0=min(s0,a-1),  d=s0-p0,  q0=i0+d.

These satisfy 0<=d<=b-a and 0<=q0<b. Select the a rows (r+d,p0) and
the a columns (q0,r'), for 0<=r,r'<a. Their entries are

    f_(i0+r'-r, s0+r-r').

If r'>r, the first index exceeds i0 while the total degree stays k,
so that entry vanishes. Every diagonal entry is f_(i0,s0), which is
nonzero. The selected determinant is therefore f_(i0,s0)^a. This proves
the lower bound. The slice supported only at (0,0) has exactly a unit
entries in different rows and columns, proving attainment.

Cyclic symmetry gives the same value on the other two central legs.
In particular the A(4,5) central block has minimum nonzero slice rank four.
The earlier discovery code computed the minimum degree of a coordinate
slice; that number alone was insufficient. The triangular minor proves
the required bound for arbitrary linear combinations of slices.

## 3. Consequence for the two possible weight profiles

A weight-preserving ordinary restriction would restrict at weight zero
to three 20-by-20 maps. The central target is concise: it is a direct sum
of nonzero matrix products, one for each common vertex weight. Hence all
three central maps are invertible. Invertible maps preserve the minimum
rank of a nonzero slice. The source minimum is four and the target minimum
is one, a contradiction.

Therefore no ordinary restriction A(4,5) to M(12,12,13) exists in the
entire specified diagonal-torus class. This rules out continuing the
eight recorded ALS starts in that class. It does not rule out arbitrary
ordinary maps or singular degenerations, and the conditional exponent
2.244 remains conditional.

## 4. Reproduction and attribution

The source convention and full-source triangular-minor idea come from the
existing balanced cyclic target note and their unequal-length extension
in this package. The new content is the central-block minor and its use
with the complete torus profile enumeration. The integer enumeration was
written independently by the critical-character worker in this session;
it agrees with the factorization enumerator. These are two implementations
of a finite arithmetic screen, not independent proof review.

`central_minrank.py` verifies every nonzero binary central slice for
(a,b)=(1,3),(2,2),(2,3),(3,3), and explicitly constructs the triangular
minor. These finite controls support the implementation; the all-field,
all-size lower bound is the argument in Section 2.
