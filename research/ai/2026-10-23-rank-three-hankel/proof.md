# Rank-three inputs exclude the two nonsquare A(8,9) survivors

October 23, 2026. Owner-directed OpenAI Codex continuation. Written proof,
unreviewed. No independent mathematical review, formalization, historical
priority, general singular exclusion or exponent improvement is claimed.

Work over an algebraically closed field F of characteristic zero. In
the source application use the algebraic closure of C(u,v). The imported
source-rank inequality, classical scalar Hankel kernels and coefficient
injection retain their earlier attribution and exact pins in sources.json.

## 1. A dimension budget for projections of low-rank matrices

Let pi:Mat_(m,n) -> W be surjective and d=dim W. Fix
1<=k<min(m,n), and let Y be the Zariski closure in W of the image of
matrices of rank at most k. Then

    codim_W Y >= 1  implies  d >= (k+1)^2,
    codim_W Y >= 2  implies  d >= (k+1)(k+2).             (1)

Here pi is arbitrary; no generic-projection assumption is made.

Identify the dual image L=im(pi*) with a d-dimensional subspace of
E tensor G, where dim E=m and dim G=n. At a generic rank-k matrix,
the annihilator of the determinantal tangent space is A tensor B,
where A,B are independent generic subspaces of dimensions m-k,n-k.
For example, in bases putting the matrix into diag(I_k,0), a tangent
matrix has arbitrary entries except its bottom-right (m-k)-by-(n-k)
block, which must vanish. Basis changes give the assertion at every
rank-k point. In characteristic zero, the generic differential rank of
pi on this smooth irreducible rank-k stratum equals dim Y. This is the
usual generic Jacobian rank statement: a transcendence basis of the
image function field has independent differentials in a separable
extension. Therefore

    codim_W Y = dim(L intersect (A tensor B)) generically. (2)

For a fixed integer c, the condition

    dim(L intersect (A tensor B)) >= c for every A,B      (3)

is closed on the Grassmannian of d-subspaces of E tensor G. For each
fixed A,B it is a determinantal closed condition, and an intersection
of closed sets is closed. It is invariant under GL(E) x GL(G).
The generic intersection dimension in (2) is its minimum, by upper
semicontinuity on the irreducible product of Grassmannians. Thus if
the left side of (2) is at least c, (3) holds on the entire orbit
closure of L in the Grassmannian.

This orbit closure is nonempty and projective. Apply the classical
Borel fixed-point theorem to the product of the two upper-triangular
groups acting on it. These groups are smooth, connected and solvable.
There is a fixed d-subspace L0 still satisfying (3). Diagonal torus
weights on E tensor G are distinct, so L0 is spanned by matrix units.
The upper unipotents force its support to be a top-left Ferrers diagram:
if (i,j) occurs, every (i',j') with i'<=i and j'<=j occurs.

The upper-triangular group has an open orbit on the Grassmannian
containing A0=span(e_(k+1),...,e_m), and similarly for B0. This is the
usual open cell of subspaces projecting isomorphically onto the last
m-k coordinates. Since L0 is fixed, its generic intersection dimension
equals its intersection dimension for A0,B0. This is exactly the number
of Ferrers boxes outside the first k rows and first k columns.

One remaining box forces the whole (k+1)-by-(k+1) rectangle. Two
remaining boxes force either (k+1,k+2) or (k+2,k+1), in addition to
(k+1,k+1). They therefore force a (k+1)-by-(k+2) rectangle or its
transpose. This proves (1). If the ambient rectangle is too small for
those boxes, the corresponding codimension condition is impossible.

The fixed-point input is Milne, *Algebraic Groups*, corrected
October 5, 2021 version published by CUP in2022, Corollary17.3, printed
page353 (PDF page364), with its standing smooth/connected hypotheses on
printed page352. We read that statement, its hypotheses and proof.
The tangent, closed-condition, Ferrers and dimension deductions above
are supplied here, without a historical priority claim.

## 2. Large sections of the rank-seven Hankel variety have codimension two

Let V=S_15^* be the 16-dimensional moment space, and let X_r be the
cone of 8-by-9 Hankel matrices of rank at most r. For every vector
subspace W of V with dim W>=13,

    codim_W (X_7 intersect W) >= 2.                      (4)

We supply the argument for arbitrary W, including special sections.
The classical scalar Hankel annihilator description identifies a
rank-r moment sequence, for r<=7, with a unique minimal binary
annihilator q of degree r. For fixed q its moment sequences form an
r-dimensional vector space: they annihilate q S_(15-r). The incidence
over P(S_r) is a projective bundle with fiber P^(r-1), and its image is
P(X_r). Uniqueness at rank r gives irreducibility and dimension2r-1.
In particular P(X_7) has dimension13; P(X_6) is irreducible of dimension11.
Every X_r contains the rational normal moment curve, which spans V,
as is also seen from sixteen distinct evaluation points and Vandermonde.

At a rank-seven point h, the left kernel of its Hankel matrix is the
line q, and its right kernel is q S_1. Differentiating maximal minors
gives conormal equations from products of a left and a right kernel
vector. On the Hankel coordinate space their span is

    N_h^* P(X_7) = q^2 S_1.                             (5)

The two products q^2 x and q^2 y are independent. Thus the tangent
space has the expected codimension two, proving smoothness at every
rank-seven point. This also treats nonreduced schemes and infinity;
no distinct-root assumption is used.

For dim W=16, (4) follows from dim X_7=14. Otherwise put
c=16-dim W, so1<=c<=3. Suppose an irreducible component Z of the
projective intersection has codimension at most one in P(W). Then

    dim Z >= 14-c.                                     (6)

Z cannot lie in P(X_6). For c<3, (6) exceeds11. For c=3, equality
would force Z=P(X_6), since that variety is irreducible of dimension11;
this would put its full linear span V inside the proper subspace W.

At a generic rank-seven point of Z, at most one of the two independent
conormal equations can remain independent on W. This follows by
restricting them to the tangent space of the smooth generic point of Z.
Consequently (5) meets W-perp nontrivially. For its minimal q, there is
a nonzero linear binary form l with

    [q^2 l] in P(W-perp).                               (7)

The morphism ([q],[l]) -> [q^2 l] has finite fibers: a fixed nonzero
binary form has only finitely many degree-seven divisors up to scalar.
Thus the locus of pairs satisfying (7), and hence their q images, has
dimension at most c-1. For each q, h varies in at most P^6. This bounds

    dim Z <= (c-1)+6=c+5 <=8,

contrary to (6), which is at least11. This proves (4). The argument
does not assume that W is general or that the whole section is smooth.

## 3. Applying both bounds to the original source

Assume an ordinary complex restriction from A(8,9) to M(x,y,31), with
(x,y)=(28,31) or (29,30). The source has common leg dimension1152.
Conciseness of the matrix target makes its first parameter lift
injective, and the other maps have full target leg ranks31x,31y.
For a parameter matrix of rank at most k, its target slice is, up to
basis order, that matrix tensor I_31, so its rank is at most31k.
The ordinary lifted source slice therefore has rank at most

    31k + (1152-31x) + (1152-31y) = 31k+475.

For k=3 this is568<576=8*72. The adopted polynomial source inequality

    rank(M_F) >= 72 rank_(C(u,v)) H_F

forces H_F to have rank at most seven for every rank-at-most-three
parameter matrix. This remains true over the algebraic closure of
C(u,v): substitute a general product of an x-by-3 and a3-by-y matrix,
and the vanishing Hankel minors are polynomial identities in those
parameters and in the two short polynomial variables. Their validity
over C makes the identities valid over the extended field.

Let W be the full image of this linear Hankel-symbol map over that
extended field, and d=dim W. The source has only16 long coordinates,
so d<=16. Choose d coordinate projections injective on W. They inject
the entire complex lifted parameter space into d copies of the
72-dimensional biform coefficient space, exactly as in the prior
source-to-symbol application. Thus

    xy <= 72d.

Both xy=868 and xy=870 exceed12*72=864; hence d>=13. By (4), the image
closure of rank-at-most-three parameters has codimension at least two
in W. But (1), with k=3, then requires d>=4*5=20. This contradicts
d<=16. Neither ordinary restriction exists.

## 4. Scope and the remaining square target

The separate PR138 finite inventory supplies context: these are its
two nonsquare survivors. Their exclusion is proved above without
assuming the inventory's completeness. Its historical report and
necessary-test classifications remain unchanged. On integration, the
two exclusions leave M30 alone among that inventory's three formats.

For A(8,9) to M30 the total long-leg loss is504. Rank-two parameters
give a source rank upper bound564<576, but rank-three parameters give594.
The rank-two version of (1) requires only d>=12 for image codimension
two, compatible with13<=d<=16. The same proof does not exclude M30.
The sharp3-by-4 rank-two projection control emphasizes that limitation.

All claims here concern ordinary restrictions of the stated full source
and targets over C. General singular degenerations, rectangular direct
sums, other sources and the exponent below9/4 remain open. Finite
controls verify explicit rank, Ferrers, conormal and integer-budget
identities; they do not formalize the geometric proof or constitute
independent mathematical review.

External fixed-point source:
https://www.jmilne.org/math/Books/iAG2022.pdf
