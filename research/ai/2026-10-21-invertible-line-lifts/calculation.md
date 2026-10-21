# Normal filtering and a complete partial lifting system

Finite exact certificates over Q, valid after extension to C. No exponent
improvement or general degeneration exclusion is asserted.

## 1. The fixed seed and the zero-third requirement

Use the compatible invertible mixed lines from the preceding both-mixed
package. The effective first ranks are 1 and 1. Each output map has four
leading rows G and one first new row b or c; further output rows are not
part of the construction ansatz below.

The old-cross matrices have rank at most eight. The target slice space
R of M(10,10,11) has minimum nonzero rank eleven, and the saturated limit
is L0=R direct-sum W0. A corrected projected third coefficient on K_inf
has support in the single new-row/new-column entry. Adding back the old
cross gives rank at most nine, so its target component must vanish.
Thus the projected third coefficient must be zero. This is the
one-by-one instance of the concurrent general third-support theorem.

The canonical first normal equations leave 228 coordinates. For b,c,
the off-diagonal compatibility equations have rank 156 and leave 72.
Choose arbitrary correction rows b',c' and let

    J_D(x)=T(x,b',c)+T(x,b,c')-T(y_x,b,c), x in K_inf.

The boundary annihilator identities make this expression independent
of the choice of correction rows. It is linear in the 72 normal
parameters. Its coefficient map has rank 32, so its zero space has
dimension 40. `normal_space.py` reconstructs all maps, solves their
rational equations and exports nonzero modular rank minors.

The pure-B and pure-C parts each have dimension 16. Together with common
plane motion they span dimension 36. The exported four-vector complement
is a deterministic linear-algebra choice. No assertion identifies the
pure directions with removable nonlinear gauge parameters; their
interactions must be retained in later equations.

## 2. The construction ansatz

Select the 36-dimensional span of pure-B, pure-C and complementary
directions, omitting plane motion. Write a=(u0,...,u15,v0,...,v15,w0,...,w3)
for their coordinates and D_B(a),D_C(a) for the four leading-row
variations on each side. Use fixed first new rows b,c.

The exact first equations are satisfied. The complete second off-diagonal
equations permit the second new rows to be **zero** for every a in this
selected span; the verifier checks this before forming any quadratic
system. We fix that choice. Alternative second new rows and additional
output rows are outside the following ansatz, so failure of its equations
is not an obstruction to arbitrary higher maps.

Let E denote the 896 unknown coefficients of the second leading rows.
The raw second leading-block residual is

    r(a)=T(K,D_B(a),D_C(a)),

where K is the full 100-dimensional first kernel. The first-normal
derivatives have no support on the twelve leading first coordinates A0,
so there is no additional first-source-correction term in this block.
Require the derivative of E plus r(a) to lie in W0. Its unique A0
coordinates determine the second source-row correction z(E,a).

At the next order, the new-row/leading-column block is

    T(K,b,E_C)-T(z(E,a),b,G)+T(K,b3,G),

with the symmetric expression for the other block. Here b3,c3 are
arbitrary third new-row corrections. The second new rows are zero, so
their products do not contribute. Earlier source-row corrections have
zero A0 off-diagonal blocks in this ansatz, which is also checked.

Eliminate b3,c3 using the two exact rank-92 correction maps. Together
with the second leading-block equations this gives a constant linear
system

    M E = -F r(a),    M of shape 1016 by 896.          (1)

The matrix M has rank 632 and left cokernel dimension 384. If Z is the
complete left cokernel, (1) is solvable if and only if

    Z F r(a)=0.                                      (2)

This is ordinary linear image membership over Q or C; no numerical
tolerance or sampled parameter inference is involved.

## 3. Sixteen quadratic conditions

Expanding (2) on all 666 quadratic monomials in 36 variables gives a
coefficient row space of dimension sixteen. The report exports a reduced
basis of all sixteen quadratic forms and the complete monomial ordering.
Every form is bilinear between u and v. None contains a w parameter or
a product within a single pure parameter group.

For example, the coordinate assignment u0=v6=1, with all other parameters
zero, satisfies all sixteen equations. Direct exact source contraction
shows that its uncorrected linear maps have first flattening rank 13
at t=1. Thus the solvable correction system does not merely reproduce
an uncorrected rank-12 truncation. This rank-13 control remains far
from the matrix target and is not an improving degeneration.

The equivalence in (2) covers second leading rows and third new rows only.
It does not include third leading rows, later coefficients, or unused
output rows. Those are the next lifting equations. The 40-dimensional
normal filter and the 36-direction ansatz have different scopes and must
not be conflated with a complete classification of all possible curves.

## Attribution

The canonical source, normal equations and rational correction maps are
adopted from the earlier extension, moving-boundary and mixed-first-jet
packages. The both-mixed package supplies the exact invertible-line seed;
the concurrent third-support theorem justifies the zero-third condition.
The new work is the complete 72-to-40 normal filter and the specified
quadratic compatibility system. These written interpretations and exact
checks have no independent review or formalization.
