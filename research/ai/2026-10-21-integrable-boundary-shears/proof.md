# An exact non-plane two-parameter boundary shear

Written AI-assisted construction, unreviewed, October21,2026.
No matrix-multiplication exponent improvement is established.

## 1. Construction and exact identity

Adopt the canonical A4 source T and the boundary bases D_B,D_C from PR45.
For z in(1,2,4,5), their raw sixteen rows are the coordinate covectors
with both short indices in{0,3}. C is the short-index swap of B.
Omit the B and C covectors e_(0,0,1),e_(0,0,2), leaving fourteen each.
Let v=a e1+b e2, with a,b arbitrary complex parameters. Modify only

    B_z=e_(3,0,z)-e_(v,3,z+3),
    C_z=e_(0,3,z)+e_(3,v,z+3),        z=1,2.              (1)

All other twelve retained rows stay fixed. Write B(a,b),C(a,b) for the
resulting14-by112 maps. Then, as a full112-by14-by14 tensor,

    T(id,B(a,b),C(a,b))=T(id,B(0,0),C(0,0)).             (2)

This is a polynomial identity on all C^2. Both maps have rank14 for every
parameter: projecting to their original fourteen boundary coordinates is
the identity matrix. Their added terms are outside that boundary space.

Here is an explicit coefficient proof of(2). For k=1,2 and z,w=1,2,

    T(-,e_(k,3,z+3),e_(0,3,w))
      =T(-,e_(3,0,z),e_(3,k,w+3))
      =e_(3-w,3-z,3-k).                                (3)

Their signs in(1) are opposite, so they cancel. A normal term has zero
product with every other retained boundary row. The only potentially
additional low e_(0,0,z) rows were omitted. All normal-by-normal products
vanish, because their C first short index is3 while the B long index is4
or5; the source relation r+s=6-z_B cannot then hold. This accounts for
every linear and quadratic term in a,b and proves(2).

The fixed tensor has first rank12, supported on the twelve canonical A0
source coordinates. A saved twelve-by-twelve nonzero determinant certifies
the rank. The construction moves the two source rowspaces, while their
contracted tensor stays exactly fixed.

## 2. Each deformed pair is maximal away from the origin

Let K be the100-dimensional span of source first covectors outside A0.
For a given C(a,b), consider all B covectors u with T(K,u,C(a,b))=0.
This annihilator is exactly the14-dimensional span of B(a,b) whenever
(a,b)!=(0,0). The exchanged assertion holds.

The constraint matrices have shape1400-by112. Their kernels contain the
explicit fourteen independent rows by(2), so rank is at most98. On the
chart a!=0 a saved98-by98 determinant is -a^2 on B and -a^4 on C.
On b!=0 the corresponding determinants are -b^2 and -b^4. Thus the
rank is98 on both charts and the displayed14-dimensional kernels are
complete. At the origin both annihilators have dimension16; exact rank96
minors and the canonical16-dimensional boundary kernels certify that case.
These statements cover every complex parameter, not a numerical sample.

## 3. All-order jets with effective first ranks ten and ten

This exact family integrates the two extra normal directions found at the
10-by10 first-extension threshold. To make that statement precise, let t
be the degeneration parameter and use B(ta,tb),C(ta,tb) in(1). Form local
maps P(t),Q(t) with four leading rows plus fourteen new rows:

    P_lead,z=G_z+t e_(v,3,z+3),
    Q_lead,z=G_z+t e_(3,v,z+3),           z=1,2,

while the leading rows at z=4,5 stay G_z. Their new rows are respectively
t B(ta,tb),t C(ta,tb). These maps are polynomial of degree at most2.
Every leading row belongs to the generic span of the new rows; for example
P_lead,z is the difference between the retained e_(0,3,z) row and B_z.
Thus their row ranks over C(t) are14. At t=0 their leading ranks are4;
the first new-row spaces have effective dimensions14-4=10 on each side.

Their entire contracted tensor annihilates K identically, by(2) and the
leading-row relations. Its first rank is12 at every t, including0.
All regularized first coefficients have no growth beyond W0; the source-row
corrections may be taken zero at every order. For (a,b)!=(0,0), the first
leading normal derivative is outside the four common polynomial-plane
motions: it occurs only in the two low-long leading rows, whereas a
nonzero common plane derivative has corresponding high-long entries.
The two new normal derivatives together with the four plane directions
are independent, as an exact rank6 certificate also checks.

This is an integrable non-plane family at effective first ranks10,10.
Consequently an extension of the earlier common-plane trap to that whole
class would be false. The first14-rowspaces are the complete mutual
annihilators for nonzero parameters, by Section2.

## 4. Scope of the construction

These maps do not reach the100-by110-by110 matrix target. Their generic
output row ranks are14 and their contracted first rank is12. No Laurent
first-leg map or regular specialization can raise those ranks to the
required dimensions. The example supplies a source-level integrable
family and a boundary on the preceding obstruction, not an improved
algorithm or an improving degeneration.

Adding later full-rank output coefficients changes the exact tensor
identity. Whether such coefficients can produce the required saturated
matrix slice space remains an open construction question. This family
must not be recorded as a full-rank matrix-target lift merely because
its polynomial coefficient equations hold at every order.
