# Sharp onset of paired long-leg kernels

October 23, 2026. Written and unreviewed. This continues the bundle argument
in PR169, with its exact source pins in sources.json. No construction of
a matrix target or smaller exponent is claimed.

Put a>=2, D=a-1, m=aD, h=2a-1 and N=ah. Use

    P_a = sum A_(u,q) B_(y,q+v) C_(u+y,v),
          0<=u,q,y,v<a.

All claims below hold over every field, for the long-leg exterior map
with short input A*. The other long leg follows by the maintained
source symmetry.

## A fixed short direction

Fix q=q0 in {0,...,D}, and allow all u. This restricts the input to a
dimensions. The only B coordinates used are

    B_(y,q0+v),       0<=y,v<a.

They span a^2 dimensions. After relabeling them as E_(y,v), the tensor
is independent of q0:

    T_a = sum e_u E_(y,v) C_(u+y,v).

For its exterior map in first space E, at degree r, the kernel dimension
is exactly

    k(a,r) = binom(m,r-a)*max(r-m,0).                  (1)

As usual, an out-of-range binomial coefficient is zero.

Here is a direct proof using the explicit quotient already constructed
in PR169. At [s:t] in P^1, the a vectors

    b_v(s,t) = sum_y s^(D-y)t^y E_(y,v)

span S'=O(-D)^a inside E tensor O, with quotient Q'=O(1)^m. The
adjacent-row matrix t e_y-s e_(y+1) proves this quotient on both standard
charts; no splitting theorem is needed.

Evaluate C_(z,v) as s^(2D-z)t^z f_v. A domain vector becomes a section
X of wedge^r E tensor O(D), and the evaluated map is

    X |-> sum_v b_v(s,t) wedge X tensor f_v.

On the component with k exterior factors in S', its fiber operator is

    wedge^k F^a -> wedge^(k+1) F^a tensor F^a,
    w |-> sum_v e_v wedge w tensor f_v.

This operator is injective for k<a: any nonzero exterior coefficient
has some index v outside its support, isolated in the f_v output.
At k=a it is zero. Thus the kernel filtration has only one nonzero
piece, giving an actual bundle isomorphism

    kernel_bundle(D) = wedge^a S' tensor wedge^(r-a)Q' tensor O(D)
                    = O(r-m-1)^binom(m,r-a).

There are no other pieces or extension maps here. The original exterior
kernel equals its global sections, because the monomials of degree2D
identify the complete C output with these evaluated polynomials.
The arbitrary-field identity h^0(O(d))=max(d+1,0) proves (1).

## Padding and all short coordinate directions

In the full N-dimensional B space, a complement of this a^2-space has
dimension m. The first-space exterior decomposition by complement degree
is preserved by the map, since every tensor coefficient lies in the
a^2-space. The exact kernel dimension for this fixed input q0, with
the full B space, is therefore

    L_q(a,p) = sum_(r=0)^(a^2) binom(m,p-r)*k(a,r).     (2)

For different coordinate q0 these kernels lie in disjoint A* input
summands. They are independent even though their B spaces overlap.
Consequently the full source kernel satisfies

    dim ker K_p(P_a) >= L(a,p) := a*L_q(a,p),
    rank K_p(P_a) <= a^2*binom(N,p)-L(a,p).            (3)

The ordinary row-dimension bound can be intersected with (3). This is
a source rank upper bound, so it is a valid necessary screen, unlike
a modular source rank lower bound. Equality is not asserted: at a2,p3,
L=4 while the independently certified full kernel dimension is10.

## The first kernel degree is sharp at every size

At p=m+1 only r=m+1 contributes to (2). Thus

    dim ker K_(m+1)(P_a) >= a*binom(m,a-1) > 0.        (4)

For m+1<=p<=a^2 one can take r=p in (2); for a^2<p<=N one can take
r=a^2. In each case a positive term exists, so L(a,p)>0 throughout
m+1<=p<=N. Together with PR169's injectivity through p=m, this proves
that the full-column interval is exactly

    0<=p<=a(a-1).

The integer controls export the two restricted kernel vectors at a2
and 15 at a=3 in the first kernel degree. Translating them to all a
coordinate q0 values gives 4 and 45 independent literal-source kernel
vectors, respectively. Every signed output coefficient is checked over
the integers. These finite witnesses control the construction; they do
not formalize the universal bundle argument.

## Scope and attribution

PR169 supplies the credited projective-line source interpretation,
explicit adjacent-row quotient, long-leg symmetry and injectivity
interval. The maintained paired-source package supplies its original
tensor and frontier. This continuation fixes one short direction,
computes its complete kernel, pads it, and sums the independent input
directions. These are owner-directed Codex deductions without independent
review, formalization or a historical-priority claim. The standard
line-bundle global-section fact retains its Stacks attribution in PR169.

The bounds leave the coupled short-input kernel unresolved. They do not
construct any of the 28 matrix targets or establish an exponent gain.
