# A third-order obstruction forces a moving boundary at every order

Written local proof, unreviewed, October 21, 2026. No matrix-multiplication
exponent improvement or historical priority is claimed. The source and
canonical extension spaces are adopted from PR45. The moving polynomial
boundary and the formal-induction framework are credited to PR46. The
new third-order block and matrix-target support argument below reduce
that theorem's first-extension hypothesis to boundary-spanning jets.

## 1. Statement and normalization

The source is the canonical cyclic A4 tensor, with all legs dimension112.
Take two regular maps P(t),Q(t) to dimension110 and an arbitrary Laurent
map on the remaining leg. Normalize their four nonzero leading rows to

    G_z=e_(0,3,z)-e_(3,0,z),     z=1,2,4,5.

The canonical leading first-row space W0 has dimension12. The target has
first-slice space R isomorphic to {X tensor I11 : X in Mat_(10x10)}, so
its first dimension is100 and its minimum nonzero matrix rank is11.
Let D_B,D_C be the canonical sixteen-dimensional boundary first-extension
spaces, each containing G. Their effective quotients D_B/G,D_C/G have
dimension12.

Assume the first nonzero new-row coefficients on both sides span those
full boundary quotients, possibly at different positive orders s_B,s_C.
After regular output-row changes, all new rows vanish below those orders.
The conclusion is that no such maps yield the matrix target, for any
higher coefficients, without a grading assumption. At ordinary first
order the spans may merely contain the boundary quotients: the preceding
second-jet theorem then excludes any additional mixed component.

Constant changes among the106 new output rows, and regular row operations
adding t^s_B or t^s_C times leading rows, put the first new rows in a fixed form:
sixteen rows give D_B,D_C at orders s_B,s_C, and every remaining row
coefficient at those orders is zero. To see
that the radical causes no difficulty, first select twelve independent
quotient rows, clear the G components in the others, and use four spare
rows to add the four radical directions at the appropriate order. These operations preserve the limiting
target up to constant invertible leg maps. We use this normalization below.

## 2. Saturation and the old cross

Let S(t) be the first flattening after P,Q and L0 its saturated limiting
rowspace. It has dimension at most112 and contains W0. The target space
R is also contained in L0. Let C0 consist of matrices supported on the
first four rows or first four columns. Its matrices have rank at most8.
Since W0 subset C0 and every nonzero target matrix has rank at least11,

    L0=R direct_sum W0,       L0 intersect C0=W0.         (1)

Every regular Laurent source-row combination has its residue in L0.
In particular a residue in C0 must belong to W0 and has a unique expression
using the twelve canonical source rows A0.

## 3. A normal lemma with boundary first rows

Put F_B=span{e_(p,j,z):p=0,3}, F_C=span{e_(r,q,z):q=0,3} and

    K_inf=span{e_(i,s,z): z=1,2,4,5}.

The omitted short and long indices have their full source ranges. Their
dimensions are56,56,64. The canonical source gives

    T(K_inf,F_B,F_C)=0,
    ann T(K_inf,-,G)=F_B,     ann T(K_inf,G,-)=F_C.       (2)

These facts and their exact rank56 certificates are adopted from PR45/46.
Take leading-row normal errors D=(D_Blead,D_Clead), modulo F_B,F_C.
There are448 scalar normal coordinates. Require, on K_inf,

    T(x,D_Blead,G)+T(x,G,D_Clead)=y_x S0,               (3)

where y_x is supported on A0. These are the old rank220 constraints,
leaving228 parameters.

Require also the off-diagonal correction equations for every b in D_B
and c in D_C:

    T(x,b',G)+T(x,b,D_Clead)-T(y_x,b,G)=0,              (4)

and its symmetric counterpart. It is enough to impose twelve quotient
basis rows on each side; the four G directions follow from (3).
The rank56 maps in (2) have cokernel dimension200. The resulting4800
linear equations on228 parameters have rank200, leaving28 parameters.
The report includes an exact kernel and a nonzero rank200 minor.

Choose any solutions b',c' of (4), and restrict the following tensor to
sixteen first covectors

    K_new={e_(i,s,z): i,s=1,2; z=1,2,4,5} subset K_inf:

    J_D(x,b,c)=T(x,b',c)+T(x,b,c')-T(y_x,b,c).          (5)

Here b,c range over the sixteen boundary frame rows. Changing b' by F_B
or c' by F_C changes nothing in (5), by (2). Thus J_D is well-defined.
It depends linearly on the28 parameters in D. Its coefficient image has
dimension24. The coefficient kernel has dimension4 and consists exactly
of the common polynomial-plane directions

    (D_Blead)_z=-e_(k,j,z),  (D_Clead)_z=e_(j,k,z),
    j=0,3; k=1,2; z=1,2,4,5.                          (6)

The verifier reconstructs (3)-(5) from all4096 source terms, checks all
correction equations, and verifies this kernel against the four explicit
directions. No numerical sampling supplies an upper-rank inference.

## 4. Two exact features of the third block

First, J_D has four fixed radical directions on each boundary output
factor. In the canonical ordering these are the differences of rows4+j
and8+j, j=0,...,3, and the analogous column differences. Every coefficient
of these identities is checked exactly. Hence the joint column and row
spaces of all matrices in J_D have dimensions at most12.

Second, if J_D is nonzero, its first flattening has rank at least8. Choose
24 independent coefficient columns to parametrize its whole coefficient
space. The certificate lists eight-by-eight upper triangular minors whose
entries above the diagonal vanish identically and whose diagonal entries
are nonzero rational multiples of a common linear form L. Each determinant
is cL^8 with c nonzero. Rank at most7 forces every recorded L to vanish.
The forced forms have rank24, so the entire block is zero. All kernels
and coefficient identities are over Q and therefore preserve every complex
solution. A saved coefficient assignment has first rank8, making this
auxiliary bound sharp.

## 5. The matrix target instead forces first rank at most two

We use an elementary joint-support estimate. Let Z be a linear subspace
of Mat_(10x10), with joint column and row dimensions p,q. Remove at most
four matrix rows and four matrix columns from {X tensor I11:X in Z} by
arbitrary linear quotient maps. If the projected joint column dimension
is at most b and the projected joint row dimension at most c, then

    7p-4<=b,       7q-4<=c.                            (7)

For the first inequality, write U for the joint p-dimensional column
space and regard each X as a map into U. Choose at most p such matrices
whose dual maps have trivial common kernel on U*. Their stacked dual
maps, tensored with I11, are injective. A functional annihilating the
joint column space after the C quotient maps into at most p copies of
that quotient's four-dimensional kernel. Thus this annihilator has
dimension at most4p: at most4p dimensions are lost from the original11p.
The B quotient then loses at most four more.
The other inequality is symmetric.

Suppose a linear family of regular source-row residues in L0 has double
projection J_D, away from the two leading four-dimensional output images.
Its target component differs from J_D by C0. Each J_D matrix has rank at
most12 by Section4, so the target component has rank at most20. Its
matrix parameter X therefore has rank at most1, since rank(X tensor I11)
is eleven times rank X.

Equation (7), with b,c<=12, gives p,q<=2. A linear rank-at-most-one matrix
space with such joint dimensions has dimension at most2: all its elements
share a left factor or all share a right factor, because two independent
left and right factors would give a rank-two sum.

Double projection is injective on the target space: its kernel is C0,
whose nonzero matrices have rank at most8. Consequently

    rank first-flattening(J_D)<=2.                     (8)

This bound is sharp as a target-subspace statement. The small control
in the report takes two matrices of original rank11; after the two
four-dimensional projections their first rank is2 and their joint supports
are10 and7. It is not a source degeneration.

There is also a consequence for **every admissible ordinary first-extension
pair** at these flags. Let its effective dimensions be r_B,r_C. PR47 gives
r_B,r_C<=16, r_B+r_C<=24 and W1=W2=W0. Normalize the first new rows to
independent quotient frames. Restrict source covectors to K_inf. The double
projection of the corrected third coefficient then has joint supports at
most r_B,r_C: a row with zero
first coefficient has second coefficient in F_B (respectively F_C), by
the annihilator equations (2), and contributes zero to the new-new block.
All first extension rows lie in those boundary spaces. Consequently each
matrix in this third block has rank at most min(r_B,r_C)<=12. Its target
component has rank at most20 and its parameter X has rank at most1.
Equation (7), now with b,c<=16, still gives p,q<=2. Hence the first
flattening of this projected third coefficient has rank at most2 for any
such pair. This necessary condition does not require the full boundary
frames or the special block (5). It imposes no positive lower rank on
arbitrary mixed or smaller first spaces.

Two further consequences require no new source calculation. If both
r_B,r_C<=9, this first rank is at most1. Indeed a rank-two parameter
space of matrices of rank at most1 has joint dimensions (2,1) or (1,2);
(7) would require one projected support to have dimension at least10.
If min(r_B,r_C)<=2, the entire projected block is zero: every projected
matrix then has rank at most2, and adding the old cross gives target rank
at most10, below11. These assertions concern the same K_inf restriction.

Combining (8) with Section4 forces J_D=0. Thus every normal error supplied
by the target and equations (3)-(4) must be one of the four plane motions.

## 6. Why the same block appears at every formal order

Follow the moving-plane construction of PR46. Let U(t) be a formal plane
of cubic forms reducing to span{e0,e3}, and set

    F_B(t)=U(t) tensor C^4 tensor C^7,
    F_C(t)=C^4 tensor U(t) tensor C^7.

The three products of a basis of U(t) remain independent. Their long
annihilator, tensored with the sixteen short first coordinates, gives a
regular rank64 module K_inf(t), with

    T(K_inf(t),F_B(t),F_C(t))=0                         (9)

identically. This uses polynomial products, not a claim that arbitrary
short-space changes are source automorphisms.

Inductively suppose every row of P,Q belongs to the corresponding moving
boundary modulo t^N. Project them onto that boundary and write their normal
errors as t^N D+O(t^(N+1)). For any regular basis row x(t) of K_inf(t), the
row x(t)S(t) vanishes below order N. Its coefficient at order N lies in C0.
By (1) it equals y_0 S0. The off-diagonal blocks and (2) force every new-row
normal error at this order to vanish; only the leading rows can depart.

Successively subtract t^(N+j) y_j S(t) to cancel residues in W0. Until
order N+s_B+s_C, every resulting residue is in C0. Here is the needed
order argument. A B new-row normal error before order N+s_B has no term
from a leading C normal error, since the B new rows start at s_B. The
source-row corrections cannot contribute to that off-diagonal block
earlier either. Thus (2) forces each such B error into the boundary.
The same statement holds for C before N+s_C. A double-new-output error
could therefore start only at N+s_B+s_C. This is an induction on the
intermediate coefficient order: any earlier double-output contribution
would use a new-row error already forced to vanish normally. Products
of leading normal errors have a leading output factor and remain in C0.
Consequently (1) supplies every required y_j before the terminal order.

At order N+s_B, the B off-diagonal equation is exactly (4), with correction
b' given by the new-row normal error at that order. Only y_0 contributes:
the B new rows vanish below s_B. At order N+s_C the symmetric equation
holds. The same leading normal D therefore belongs to the28-dimensional
space of Section3 even when the two first-growth orders differ.

Now divide the corrected source row by t^(N+s_B+s_C) and take its residue
in L0. Project both factors away from the leading images and restrict
x(0) to K_new. The resulting tensor is exactly (5): the order-(N+s_B)
new B error pairs with the C coefficient at s_C, the B coefficient at
s_B pairs with the order-(N+s_C) new C error, and the y_0 correction pairs
with the boundary-by-boundary coefficient at s_B+s_C. Every y_j with j>0
has zero double projection at this terminal order, because the double-new
block of S(t) starts at s_B+s_C. Higher boundary terms vanish by (9).
Products of two new normal errors occur strictly later, and leading
normal errors are removed by the double projection. Derivatives of x(t)
affect it only at later orders as well.

For new output rows whose coefficient at s_B or s_C is zero, their version
of (4) puts the relevant normal error in F_B or F_C, so their contribution
vanishes by (2). Thus the sixteen-frame calculation has omitted no output
coordinate. The same observation removes every choice of boundary terms
in b',c'. When s_B=s_C=1, the two initial row corrections are the y,z
corrections of the ordinary third-order calculation.

Sections4-5 force this block to vanish and D to be a plane motion (6).
Adjust U(t) at order N to absorb it. New output rows have zero constant
coefficient, so this preserves their boundary membership at the required
order and leaves their first nonzero frames unchanged. Every row now
belongs to the updated boundary modulo t^(N+1), completing the induction.

The resulting formal leg maps have row rank at most56 over C((t)). No
Laurent first-leg map can raise the other flattening ranks, and a regular
limit cannot raise them. The target is concise in110 coordinates on both
of these legs. This contradiction proves the exclusion at every order.

## 7. Consequences and remaining scope

A target with these leading flags cannot have both first quotient spans
contain the full canonical boundary quotients. Together with PR47's
rank-sum constraints, this improves the necessary total effective first
rank from24 to23: without a mixed component each rank is at most12,
and equality24 is the boundary-spanning case just excluded; with a mixed
component the earlier bound is already20.

Smaller or different first subspaces, leading-rank loss and other leading
flags remain open. Delaying the same full boundary frames, even to
different orders on the two sides, does not evade this theorem. In particular this is not an
arbitrary-degeneration exclusion and gives no exponent improvement. The
complete second jets in PR49 remain correct finite-order data; they cannot
lift to this matrix target under the stated boundary-spanning hypothesis.
