# Exact obstruction for the asymmetric SL2 action on M5

October 21, 2026. Written proof, unreviewed. No exponent improvement.

The source is full A(3,3). Preserve its diagonal SL2 action, with each source
leg decomposing as V0+2V2+3V4+2V6+V8. Let the three matrix vertices carry
U=V4, U=V4, and W=V2+2V0. This is the remaining representation-compatible
five-dimensional vertex pattern after the all-V4 case excluded in the
maintained cyclic-equivariant package.

Allow independent intertwiners on all three legs and their arbitrary limits.
We show that they cannot produce the M5 tensor. Numerical failures are not
used in the proof.

## Two coefficient matrices

The U-to-U target leg has one copy each of V0 and V8, as does the source.
Its maps on these components are scalars x0,x8. Each other target leg has
three copies of V4, matching the three source copies. Call their multiplicity
maps B,C, of size3 by3. Restrict the output tensor to the chosen V0 or V8
vector on the first leg and the V4 components on the other two legs.

Choose highest-weight V4 vectors and lower the third-leg vectors four times,
dividing by4!. For V8 on the first leg use its weight-zero vector obtained
by four lowerings, again divided by4!. The exact source and target coefficient
matrices G0,G8 are recorded in `pencil-certificate.json`. The reconstruction
uses the physical W trace description, checked against all729 original
source terms. Its source matrix G0 has determinant -7/6912; the target G0
has determinant -3/4.

Every equivariant output has

    G0_out=x0 B^T G0_source C,
    G8_out=x8 B^T G8_source C.

When G0_out is invertible, H_out=G0_out^-1 G8_out is therefore a scalar
multiple of a conjugate of H_source=G0_source^-1 G8_source. Direct rational
calculation gives

    tr(H_source)=726/7,
    tr(H_source^2)=518592/49,
    tr(H_source^2)/tr(H_source)^2=43216/43923.

For the target the corresponding ratio is11/8: its pencil has eigenvalues
1,1,-2/3. The source and target pencils cannot be scalar-similar.

## A polynomial certificate covers singular limits too

Set Q=adj(G0)G8. Every equivariant image satisfies the polynomial identity

    43923 tr(Q^2)-43216 tr(Q)^2=0.                    (1)

The derivation above holds on the nonempty open set where G0 is invertible,
so it extends polynomially to all intertwiner parameters and to the closure
of their images. At the target the left side is exactly137425/8, nonzero.
Thus even parameter-dependent intertwiners with poles cannot yield this M5
in a limit. No assumptions of bounded parameters or equal leg maps are made.

## Exhausting five-dimensional vertex representations for this action

The source has trivial central parity. Each matrix vertex must have pure
central parity, the same on all three vertices. Dimension five forces the
positive parity, so its irreducible-dimension partitions are5,3+1+1,1+1+1+1+1.
The last choice cannot pair with any other choice: it gives multiplicity at
least five somewhere, above every source multiplicity. Two3+1+1 vertices
also fail, giving five singlets and five V2 copies. Hence at most one vertex
can be3+1+1. All three irreducible V4 vertices are already excluded by the
credited five-coefficient invariant. A single3+1+1 vertex leaves the pattern
above, up to a cyclic rotation. This closes all diagonal-SL2 matrix-vertex
actions of dimension five on this source, including equivariant degenerations.

General symmetry-breaking maps and different subgroup actions are not covered.
The separate new cubic argument excludes ordinary M6 from A33, but does not
exclude arbitrary M5 restrictions.

## Discovery record

The complete exact intertwiner bases have dimensions9,13,13. Eight complex
ALS starts of300 sweeps each had best full relative residual approximately
0.6324597378. The best fit suppresses the two trivial W directions and nearly
retains an M(5,5,3) block. This prompted a separate rectangular search, whose
outcome must be assessed on its own. Failed fitting is not a proof of (1).
The numerical core compression is a search device; the exact invariant above
is reconstructed independently from the source and target representations.
