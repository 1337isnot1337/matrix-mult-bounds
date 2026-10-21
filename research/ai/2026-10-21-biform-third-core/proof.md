# The third normal block is a biform syzygy tensor

AI-assisted written proof, unreviewed, October21,2026. No exponent gain.
The source, canonical flags and moving-plane induction retain the credits
in PR45/46/47/48/55/57. This note identifies the full tensor structure,
proves sharper projection bounds and extends the boundary trap to arbitrary
first dimensions at least11 and9, in either order.

## 1. Exact polynomial structure

Use the28-dimensional boundary-compatible normal space of PR55. After
passing from the16 boundary rows to their12-dimensional quotients, its
third block has first dimension16. Index these first coordinates by
(i,s,k), where i,s=0,1 are the two middle short indices and k=0,...,3
indexes the long coordinates1,2,4,5. Order each12-dimensional boundary
quotient as six consecutive pairs. The exact source coefficients give

    J_D(i,s,k)[(b,epsilon),(c,eta)]
      = delta_(epsilon,1-s) delta_(eta,1-i) K_D(k)[b,c],       (1)

with b,c=0,...,5. Thus J_D is the tensor product of the outer-product tensor
of dimensions4,2,2 and a core K_D of dimensions4,6,6. Every coefficient
in(1) is checked, for all28 parameters. In particular its first-slice
space is Mat2 tensor Z_D, where Z_D is the matrix span of the four core
slices. The coefficient image of K_D has dimension24 and kernel4, the
common polynomial-plane directions.

Let S0 be the span of all core matrices as D and k vary. The preceding
80-dimensional matrix-span certificate gives dim S0=20. It now has a short
polynomial description. On the affine chart of P1 times P1 use variables
x,y and the bases

    A=(1,-y,y-x,-y^2+xy,-xy,xy^2),
    B=(1,x,y-x,xy-x^2,-xy,-x^2y).                          (2)

After bihomogenization these are bases of sections of degrees(1,2) and
(2,1). Their changes from the standard monomial bases both have determinant1.
Their products span all sixteen monomials of degrees at most(3,3).
The exact coefficient map

    mu:Mat6x6 -> H0(O(3,3)),
    mu(M)=sum M_bc A_b B_c                                (3)

has rank16 and kernel exactly S0, as checked against every previous span
basis vector. This is ordinary biform multiplication in explicit bases.

If M=u tensor v has rank1, then mu(M)=(sum u_b A_b)(sum v_c B_c).
The polynomial ring is an integral domain and both displayed families
are independent. Thus no nonzero rank-one matrix belongs to S0.
This proof explains the earlier six determinant certificates; it does not
assume that their finite checks supply the integral-domain argument.

The core has minimum nonzero first-flattening rank2. An independent small
certificate gives triangular two-by-two determinants c*L^2. Rank at most1
forces24 independent linear forms on the28 parameters. The final core is
zero and the parameter kernel has dimension4. A rational parameter gives
first rank2, so this auxiliary bound is sharp. Consequently any non-plane
D has r=dim Z_D>=2, and every nonzero matrix in Z_D has rank at least2.

## 2. The exact two-hyperplane loss is three

The general lemma in PR57 bounded the loss by5 for S0 tensor Mat2.
For this particular polynomial kernel the correct bound is3, and is sharp.

For nonzero biforms u of degree(1,2) and v of degree(2,1), consider pairs
(a,b) of the same respective degrees satisfying

    a v+u b=0.                                           (4)

Let g=gcd(u,v), u=g u', v=g v'. Unique factorization gives

    a=u' h,       b=-v' h,

where h has the bidegree of g. Since that bidegree is coordinatewise
at most(1,1), the solution space in(4) has dimension at most4.

For one-dimensional quotient kernels on the two12-dimensional matrix
legs, write their generators as u=(u_0,u_1),v=(v_0,v_1) in the respective
six-dimensional biform spaces tensored with dimension2. A matrix killed
by both quotients is represented as a tensor v+u tensor b. Membership
in S0 tensor Mat2 means a_i v_j+u_i b_j=0 for all i,j. Choose nonzero
u_i0 and v_j0. The complete pair(a,b) is determined by(a_i0,b_j0), since
multiplication by a nonzero biform is injective. By(4) its space has
dimension at most4. The representation has the one-dimensional kernel
(a,b)=(lambda*u,-lambda*v). Therefore the killed matrix space has
dimension at most3.

The saved corner control attains3: u and v are the first basis vectors
in(2). Their homogeneous gcd has degree(1,1), so(4) has dimension4 and
its matrix images have dimension3. The tensor factor can be a single
matrix unit. This is sharp for the actual80-dimensional space, unlike
the earlier sharp5 control for the more general lemma.

## 3. A puncture lemma with losses one and three

Here is a second, independent projection consequence of(1).
Let Z be any matrix space with dimension r>=2 and no nonzero rank-one
matrix. In Mat2 tensor Z, remove at most one dimension from the matrix
row leg and at most three from its column leg. The projected matrix
space still has dimension at least3. The exchanged statement also holds.

First remove the column kernel K, of dimension at most3. A single
auxiliary row block of Mat2 tensor Z consists of pairs(Z0,Z1) in Z direct
sum Z. Let W be its projected image, with dimension w. Set

    K_j=K intersect (V tensor e_j),      j=0,1.

The dimensions of K0 and K1 sum to at most3; at least one is at most1.
If a pair in the projection kernel has the other matrix component zero,
its remaining matrix has rowspace in that K_j and hence rank at most1.
It must be zero. Projection onto the other Z component is therefore
injective on the kernel. Its dimension is at most r, giving w>=r>=2.
The full projected matrix space consists of two independent auxiliary
row blocks and has dimension2w.

Now remove the possible row line spanned by p=(p0,p1). A killed matrix
has the form p tensor f, with p0 tensor f and p1 tensor f both in W.
Its space has dimension at most w. If w>=3, the remaining first dimension
is at least2w-w>=3. The only possible failure would be w=2 and a killed
space of dimension2. In that case p0,p1 must be proportional: otherwise
W would contain the direct sum of two copies of the same2-dimensional
space. It follows that W has a fixed common column line, say span(u).

We show that this last case cannot have w=2. Project Z away from u on
the row leg. The projection is injective on Z because a nonzero kernel
matrix would have rank1. Let Q be the joint rowspace of this image.
Because W has column line u, both auxiliary copies of Q lie in K. Thus
2 dim Q<=3. Since Z is nonzero, Q is a line, say span(v), and K contains
v tensor C^2. Every matrix in Z now belongs to

    U tensor v + u tensor V.

Projecting the column leg away from v is also injective on Z, for the
same rank-one reason. Its image has column line u and dimension r.
The two auxiliary column copies consequently span2r dimensions after
quotienting by v tensor C^2. The remaining part of K has dimension at
most1 and can lose at most one further dimension from this space.
Therefore w>=2r-1>=3, a contradiction. This proves the lemma.

The bound3 is sharp. Take Z spanned by E01-E10 and E02-E20 in Mat3.
Every nonzero member has rank2. In Z tensor Mat2, remove row0 and columns
0,1,2 of the6-by6 matrices. The original matrix-space dimension is8 and
the projected dimension is3. The report verifies the complete matrices.
This is a control for the general lemma, not a target degeneration.

The same Z also marks a limit of this argument: removing two row dimensions
and two column dimensions, the two auxiliary copies of the common row
and column direction, kills its entire tensor product. The report verifies
this counterexample as well. A general assertion for losses(2,2) would be
false; reaching that frontier needs additional structure of the actual K_D.

## 4. Conditioned boundary obstructions have minimum nonzero rank four

On the228-dimensional canonical normal space, write Psi_B,Psi_C for the
200-by12 boundary obstruction matrices from PR57. Each separately has
minimum nonzero rank2. Setting Psi_B=0 leaves100 parameters. On this
entire kernel, every nonzero Psi_C has rank at least4. The exchanged
statement holds as well. Exact triangular four-by-four minor identities
force56,14,2 independent forms in three rounds, leaving28 parameters
on which both boundary matrices vanish. Both auxiliary minimum bounds
have sharp rational controls.

Suppose the first boundary subspaces have dimensions at least11 on B
and at least9 on C. Their correction equations require Psi_B and Psi_C
to annihilate those subspaces. Psi_B has rank at most1, hence is zero.
The conditioned Psi_C then has rank at most3, hence is also zero.
The normal variation belongs to the complete28-dimensional boundary
normal family, irrespective of which complex subspaces were chosen.

## 5. Arbitrary first dimensions eleven and nine are trapped

Use the canonical G leading rows and target with first-slice space
{X tensor I11:X in Mat10x10}, of leg dimensions100,110,110. Assume the
first new-row spans lie in the boundary quotients, have dimensions at
least11 and9 in either order, and first occur at arbitrary positive
orders s_B,s_C. Allow all higher regular coefficients and an arbitrary
Laurent map on the first leg.

At each moving-boundary induction step, the shifted off-diagonal equations
put the next normal error in the28-dimensional family by Section4.
The full virtual third block is(1). Its restriction to the actual first
spans is a projection losing at most one dimension on one matrix leg and
at most three on the other. If the error is not a plane motion, Sections1
and3 force first rank at least3.

The matrix target forces first rank at most2 for that same terminal
residue. Indeed its projected joint supports are at most12 on each leg;
each matrix has rank at most12 and differs from its target component by
the old rank-at-most8 cross. The target component has rank at most20 and
therefore has parameter matrix X of rank at most1. PR55's joint-support
estimate forces parameter joint row and column dimensions at most2.
The linear rank-one space consequently has dimension at most2, and
double projection is injective on the target. This proves the ceiling2.

The contradiction forces the error to be a common polynomial-plane motion.
Absorb it into U(t) and continue the induction exactly as in PR55/57.
The first spans need not be enlarged: Section4 supplies virtual full-frame
corrections, whose restrictions equal the actual corrections modulo F_B,F_C,
which cannot change this third block. Both regular local maps remain in
moving rank56 boundary spaces at every order. They cannot have a concise
110-dimensional target leg.

For ordinary first derivatives, mixed spaces already have rank sum at
most20 by PR47, and at most19 by the stronger PR53 result. Pure boundary
spaces have individual ranks at most12. A sum above20 would force one
rank at least11 and the other at least9, now excluded. Thus the global
necessary ordinary first-rank sum at these canonical flags is at most20.
The pure boundary possibilities12,8 and10,10 remain at this threshold.
Other leading flags and general degenerations remain open. No smaller
matrix-multiplication exponent follows from these necessary constraints.
