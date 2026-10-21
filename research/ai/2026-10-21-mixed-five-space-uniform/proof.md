# Uniform adapted source slices

Written proof, unreviewed, October21,2026. Claim
`AI-MIXED-FIVE-SPACE-LOW-SLICES-088`. All vector spaces are over C.

Use the rank-one partner chart and complete seven-frames of claim085:

    u=(ab,-a,-b,1),  v=(ab,b,a,1),
    B_j=d_(2j+1)-b*d_(2j), C_j=d_(2j+1)+a*d_(2j), j=0,...,5,
    B_6=m_B(u), C_6=m_C(v).

Assume the B first space is the full seven-frame. Let V be any actual C
first space in its compatible maximal seven-frame, and let D be a
matrix-target admissible normal error. The statement below applies in
particular to arbitrary mixed five-spaces V.

## 1. Uniform virtual tensor and its correction certificate

The adopted complete B equations have a polynomial 228-by-88 kernel
basis K(a,b). Its fixed identity free-coordinate block and constant
nonzero rank140 minor prove completeness at every point, including a=0
or b=0. The earlier uniform-kernel routine reconstructs that certificate.

The C obstruction Psi(D) has seven columns and200 rows, linear in D.
Form its joint coefficient matrix in the616 columns indexed by a C
coordinate and one of88 normal parameters. It has a uniform row basis:
select the fixed full-rank minor F at a=b=0, multiply by F(0,0)^(-1),
and verify that the difference from the identity is strictly triangular
after a fixed permutation. Consequently det F is the same nonzero
constant at every a,b. Polynomial back substitution gives the row basis
R, and the full identity M=M[:,pivots]R is checked. This establishes
equality of rowspaces at every point, without division by a or b.

As in the point package, use exact B corrections and fixed partial
inverses for virtual C corrections. Their complete joint error factors
through R by an explicit polynomial matrix. The C corrections thus
become valid on V contained in ker Psi(D). The coefficient tensor

    J_D(x,b,c)=T(x,b',c)+T(x,b,c')-T(y_x,b,c)

is reconstructed symbolically from the source. Subtract the indicated
polynomial combinations of R from each joint B row. This does not change
J_D on V; all combinations are independent of the normal parameters D.

## 2. Sixteen uniform rank-one slices

For s=0,1,2,3 and z=1,2,4,5 define

    x_(s,z)(a)=e_(2,s,z)-a*e_(1,s,z).

These vectors belong to K_inf. Their projection onto the sixteen
e_(2,s,z) coordinates is the identity, proving independence for every a.
Contracting the reduced virtual tensor with each x_(s,z) gives a7-by7
matrix whose first six B rows vanish identically as polynomials in a,b
and D. The remaining row is the mixed B row. The report exports the
entire16-by7-by7-by88 coefficient array in sparse joint form, and the
verifier checks every asserted zero. Hence each slice has rank at most
one, also after restriction to any actual V.

In a target lift, the corresponding terminal source residue belongs to
R_target+W0. Its double projection is this slice; the complementary old
four-row/four-column cross has maximum rank eight. Its target component
therefore has rank at most nine, whereas a nonzero slice of
R_target=Mat10 tensor I11 has rank at least eleven. That component is zero,
and double projection makes J_D(x_(s,z),B7,V)=0. These are sixteen
uniform necessary source-slice vanishing equations.

The same conclusion applies at shifted terminal order N+s_B+s_C under
the adopted moving-boundary order argument. No induction closure is
claimed here: the remaining normal directions have not all been removed.

## 3. Scope

At a=b=0 this recovers the first sixteen source slices used by claim087.
The new calculation proves that step uniformly over the entire v3 chart.
Source reversal transports it to v0 nonzero. The two exceptional partner
points with v0=v3=0 are not covered by this certificate.

The coordinate-partner proof eventually forces the four plane normals.
That later elimination has not been extended here. Passing these
necessary equations supplies no higher-rank output maps, matrix target,
new global first-rank bound, or exponent improvement. Independent
mathematical review remains open.
