# Arbitrary boundary hyperplanes are trapped at every order

AI-assisted written proof, unreviewed, October21,2026. No exponent improvement.
The canonical source, G flags, boundary spaces, normal equations and formal
moving-plane induction retain the credits in PR45/46/47/48/49/55.

## Statement

The source is A4 with leg dimensions112. The target has dimensions100,110,110,
with first-slice space {X tensor I11:X in Mat10x10}. Fix the leading G rows.
Suppose the first new-row spans are subspaces of the canonical boundary
quotients D_B/G,D_C/G, each of dimension at least11. The first-growth orders
may be delayed, positive and unequal. Then no regular higher coefficients
and no Laurent first-leg map can reach the target.

This concerns arbitrary hyperplanes, not coordinate omissions or a finite
set of sampled subspaces. At ordinary first order it implies that at least
one effective first rank is at most10, since the previous mixed-component
sum bound already excludes two ranks at least11 with a mixed component.
The global ordinary rank sum is at most22: without mixed components the
only sum above22 is12+11 or12+12, now excluded. This does not close all
pairs of sum22:12+10 and its exchange remain open.

## 1. Boundary obstruction matrices have minimum nonzero rank two

Use the228-dimensional normal parameter space from PR46 and restrict each
200-by16 obstruction Psi_B(D),Psi_C(D) to the12-dimensional boundary
quotient. Every nonzero resulting200-by12 matrix has rank at least2 over C.
An exact repeated-minor certificate proves this: two rounds force124 and4
independent linear forms to vanish if every two-by-two minor vanishes.
Afterwards every matrix coefficient is zero. The remaining parameter
dimension is100. The auxiliary bound is sharp, with rational controls.

A matrix annihilating an arbitrary boundary subspace of dimension11 has
rank at most1. Thus both boundary obstruction matrices vanish identically.
The complete boundary normal constraints leave the same28-dimensional
normal space as PR55. Its third block J_D has coefficient kernel equal
to the four common plane directions, and every nonzero J_D has first
flattening rank at least8.

## 2. The full matrix span of the third block

Pass from the16 boundary frame coordinates to their12-dimensional quotient
using the four fixed radical identities in PR55. Let S be the linear span
of every matrix slice J_D(x), allowing both x and D to vary. It has dimension80
and, after a fixed coordinate ordering, is

    S=S0 tensor Mat2,       S0 subset Mat6x6, dim S0=20.       (1)

The exact span basis and sixteen linear equations for S0 are exported.
Every parity block belongs to S0, and dimension80 proves equality in(1).
The space S0 has no nonzero rank-one matrix over C.

To certify the last assertion, substitute u_i v_j into its sixteen linear
equations. Successively assuming u0,u5,u1,u4,u2,u3 is the next nonzero
coordinate, six linear combinations of these equations have coefficient
determinant c*u_i^6 in v, after the preceding u coordinates vanish. The
six constants c are nonzero rational numbers. Thus each assumption forces
v=0. All u coordinates must vanish if v is nonzero, proving the assertion
for every complex pair. This is a finite polynomial-identity certificate,
not sampling or a numerical rank inference.

It follows that S itself has no rank-one matrix: any nonzero rank-one
matrix in S would have a nonzero rank-one6-by6 parity block in S0.

## 3. A general two-hyperplane compression lemma

Let U,V have dimension h, let H subset U tensor V contain no nonzero
rank-one tensor, and put S=H tensor Mat_d, regarded as matrices from
V* tensor C^d to U tensor C^d. Let a quotient remove one dimension on each
matrix leg. Its kernel on S has dimension at most h-1. If either quotient
removes no dimension, the kernel on S is zero.

Here is a proof without a generic-position assumption. Write N for the
quotient map (U tensor V)->(U tensor V)/H. The absence of rank-one tensors
means that for every nonzero u or v the maps N(u,-) and N(-,v) are injective.
Let the two one-dimensional kernels be spanned by u=(u_i) and v=(v_j).
Every matrix in the compression kernel is represented as

    M=a tensor v+u tensor b.                              (2)

The representation has a one-dimensional kernel (a,b)=(lambda*u,-lambda*v).
The condition M in S is equivalent, for all i,j, to

    N(a_i,v_j)+N(u_i,b_j)=0.                              (3)

Choose i0,j0 with u_i0 and v_j0 nonzero. The space of pairs(a,b)
satisfying(3) injects into U by (a,b)->a_i0: if a_i0=0, (3) first gives
b_j=0 for every j, then gives a_i=0 for every i. Its dimension is therefore
at most h. Dividing by the one-dimensional kernel in(2) gives h-1.
If only one leg is projected, a nonzero matrix in the kernel would have
rank1, which S excludes.

With h=6,d=2 in(1), at most5 dimensions of any first-slice space can be
lost by arbitrary hyperplanes on both boundary quotients.

## 4. Target contradiction and all formal orders

The actual first boundary spans have codimension at most1 in each
12-dimensional quotient. Their corrected third block is the corresponding
compression of the full J_D. Section1 ensures the required virtual
corrections exist for every full boundary row. Their restriction equals
the actual corrections modulo F_B,F_C, which cannot change this third block.
No missing boundary row is added to an actual output map.

If D is not a common plane direction, its full third block has first rank
at least8. Section3 leaves first rank at least8-5=3 after the two arbitrary
hyperplane compressions. The target instead forces first rank at most2,
by PR55's joint-support argument. Hence D is a plane direction.

At every formal induction step the first leading normal error satisfies
the same228-dimensional leading equation. At the shifted off-diagonal
orders its boundary obstruction matrices annihilate the fixed first spans.
Section1 extends those equations to the full boundary quotients. At the
shifted new-new order the actual third block is the compression just
considered. Section4 forces plane motion, which is absorbed into U(t).
The order argument, arbitrary boundary choices, delayed unequal growth,
source-row corrections and zero first rows are exactly as in PR55.
Thus both leg maps remain in moving rank56 boundary spaces at every order,
contradicting target conciseness110.

The proof does not show that smaller first spaces or different leading
flags can produce the target. Those construction questions remain open.
