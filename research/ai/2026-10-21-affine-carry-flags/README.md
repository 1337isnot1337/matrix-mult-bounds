# Affine carry first flags and a finite six-sector control

This package proves a first-flag identity for every m >= 4 and records
a complete finite-field construction at m=6. It does not prove an
exponent improvement or a characteristic-zero six-sector construction.

## Results and scope

The [first-flag proof](first_flag_proof.md) uses an m-dimensional shared
polynomial space inside the first m+3 source coordinates. Its six labelled
input rows have product-space dimension at most 3m+6. This is an exact
polynomial identity over every field. It does not include the later
input or output sectors.

The [finite witness](../../../results/affine-carry-flags-2026-10-21/m6-f2-witness.json)
gives a torus degeneration from C(9,23) over F2 to the six matched sectors

    C(1,6), C(2,5), C(3,4), C(4,3), C(5,2), C(6,1),

with one common six-dimensional shared space and an independently
invertible shared change of basis in each sector. There are 21 target
coordinates on each nonshared leg. The construction uses natural
degree weights X=-5, Y_p=p, Z_q=q.

The standalone verifier checks all 2,646 source coefficients. Of these,
420 have negative degree and vanish, and 336 have degree zero and equal
the prescribed matched sectors. The other 1,890 positions have positive
degree. All three maps have ranks 6,21,21 and every shared sector matrix
has rank 6. The verifier also rejects a changed source-output coefficient.

A [finite lift](../../../results/affine-carry-flags-2026-10-21/m6-finite-lift-1025.json)
satisfies 540 defining congruences modulo 2^1025. Its variable order is
stored with the data. This is a finite congruence experiment. It does not
by itself imply the existence of a characteristic-zero point. The
unrestricted 540-equation Jacobian has rank 483 modulo 2 at the stored
residue point. The smaller affine incidence chart likewise has
dependent equations. No smoothness or algebraic dependency certificate
has been completed for either system.

## Exact tensor convention

The source is

    C(a,B) = sum_(0<=i<a, 0<=j<B) x_i y_j z_(i+j).

A binary integer stores a polynomial or a moment functional: bit j is
the coefficient of t^j or the value on t^j, respectively. The source
shared map has six rows U[i]. Input and output rows are grouped by
degree p or q and then by ascending position a or c within the block.

For p+q=5 the required coefficient is

    bit_(a+c)(H[p][i]).

Every H[p] is invertible over F2. This convention permits different
shared identifications in different sectors; it does not assert that
all six H[p] are one common matrix.

## Discovery route

The existing [integer m6 control](../2026-10-21-canonical-moment-flags/README.md)
starts from C(7,24). Applying the linear input operation
y(t) -> (y(t)-y(0))/t compresses its input window. Replacing the
degree-zero row by 1 exposes the affine first flag

    (1; h,th; g,1+tg,t+t^2g).

The shared space was then changed, and the next two input blocks were
found by exact finite-field subspace searches. Those searches were
discovery tools; the stored literal maps are the acceptance artifact.

## Reproduction

From the repository root:

    python research/ai/2026-10-21-affine-carry-flags/verify_first_flag.py
    python research/ai/2026-10-21-affine-carry-flags/verify_m6_f2.py
    python research/ai/2026-10-21-affine-carry-flags/verify_finite_lift.py
    python -m unittest discover -s tests -p test_affine_carry_flags.py -v

Only the Python standard library is needed. The first command checks
142653 integer relation coefficients for m=4,...,24. Modular rank
checks reach the proved upper bound in every one of those controls.

This is same-session AI-derived work under the repository owner's
direction. Existing source, target and exponent criteria retain their
original provenance. These finite controls are construction seeds;
an all-size completion and characteristic-zero transfer remain open.

