# Characteristic-three closure of the invertible quadratic stratum

October 25, 2026. Claim `AI-CHAR3-QUADRATIC-INVERTIBLE-001` is
**proof-written-unreviewed**. A separate same-session algebra audit found no
remaining gap in the radical, fixed-frame, cubic-coefficient and Frobenius
arguments. This is not independent review or formalization. No compatible
tensor target or exponent improvement is claimed. Dependencies are pinned in
[sources.json](sources.json): PR228 supplies the normalization and integral
linear form, and PR227 supplies the full tangent quadratic. Their earlier
determinant source retains its attribution. No new external theorem is imported.

## Theorem and literal source

Let K have characteristic three. For M in Mat_3(K) use the full source

    R(M)[(j,L),(H,r)]=M[H-j,L-r],
    0<=j,r<=2, 0<=L,H<=4,

with row pairs (j,L) and column pairs (H,r) in lexicographic order and
out-of-range coefficients zero. If a K-linear family W has source rank at
most fourteen after algebraic closure and contains an invertible coefficient
point after algebraic closure, then **dim_K W<=4**. Combined with the pinned
PR228 result, this proves the cap four over every field of characteristic
different from two, including characteristic zero.

The hypothesis is geometric polynomial vanishing of det R; finite-field
point checks do not replace it. Characteristic two remains unresolved here.
No cap-four sharpness witness is asserted. The [two-plane](two-plane.md) gives
a lower bound two when the field contains a square root of -1. Neither the
upper nor lower bound supplies a compatible tensor map.

Extend scalars to the algebraic closure k; this preserves dimension. A family
of larger dimension contains a five-space through an invertible member, so it
suffices to exclude such a five-space. Use the pinned invertible coordinate
change M=P N P^t. The universal source determinant factor and the domain
property of k[W] force the normalized residual determinant to vanish on W.

Assume W is this normalized five-space, with p=det N
not identically zero and residual determinant zero. Put H=N^tN, q=tr H,
A=s2(H), Q=H^-1. The monic-integrality argument from PR228 supplies a global
linear form h on W such that p=q*h-h^3 and A=2*p*h. On every invertible
point, Q has orthogonal blocks diag(mu,B), trB=mu!=0, d=detB!=0. Since
trQ=A/p²=2h/p, one has h=p*mu and p²*mu*d=1.

## Radical direction

Work in characteristic three. The four-variable off-block tangent form q4
is nondegenerate: its Schur numerator has determinant d³!=0. For
B=[[u,v],[v,w]], C=[[a,b],[c,e]], the other tangent form reduces to

    qC=(b-c)*(v*(a-e)-u*b+w*c).

If B is nonscalar these two linear factors are independent, so qC has
rank two. Its radical consists exactly of symmetric C commuting with B:
C is in span(I,B). The commutant assertion is elementary: a nonscalar
2-by-2 matrix has a cyclic vector z (z,Bz independent), so a commuting
matrix is determined by its value on z and is a linear combination of
I,B. Both I and B are symmetric.

Thus the full eight-variable tangent form has rank six and radical dimension
two. Since the residual vanishes on W, its five-dimensional direction space
lies in the tangent hyperplane and the quadratic term vanishes on it.
Polarization makes W totally isotropic. Such a five-space contains the whole radical: its
image in the nondegenerate six-dimensional quotient has dimension at most
three, forcing intersection with the radical to have dimension at least two.

Apply the pinned left-Gram calculation to N^t, then transpose back; tangent
radical perturbations are N F with symmetric block-diagonal F. The scalar
C=I gives F=I. The second direction C=B gives

    F2=diag(tr(B²)/mu,B)
      =Q+(d/mu)E=(Q²+dI)/mu,
    E=(Q²-mu*Q+dI)/d.

Here E is the distinguished first-coordinate projector; the formula follows
from Cayley-Hamilton on B and holds without diagonalizing B. The equality
for F2 is in characteristic three. Since W contains N and N F2, it contains

    V=N Q².

The formula is invariant under the fixed orthogonal basis change at N, so
there is no moving-frame differentiation in this conclusion.

## The forced line makes d=mu²

Because h is a linear form on W, h(N+tV)=h(N)+t*h(V). Compute h(V) by
its invariant expression p*mu at N. With V=NQ² one has

    dH=2Q,  dQ=-2Q³=Q³,
    dmu=tr(Q³)/2=(trQ)³/2=mu³,
    dp=p*tr(Q²)=p*(2mu²+d).

The trace-cube equality holds in characteristic three, without a spectral
assumption. Hence dh=p*mu*d=h*d, so h on this line is h*(1+d*t).
The direct determinant and norm expansions are

    q_t=q+mu*t+2mu³*t²,
    p_t/p=1+(2mu²+d)t+(mu⁴+mu²d+d²)t²+mu²d²t³.

These follow from H_t=H+2tQ+t²Q³ and
p_t=p det(I+tQ²). Along this line the polynomial identity
p_t=q_t*h_t-h_t³ holds. In characteristic three, h_t³=h³(1+d³t³).
Using h=p*mu and p²*mu*d=1, its t³ coefficient gives

    0=2*p*mu²*d*(d-mu²).

Thus d=mu² at every point with nonscalar B. If B is scalar instead,
B=(mu/2)I already gives d=mu²/4=mu² in characteristic three. Therefore
rho=d/mu²=1 at every invertible point of W.

## Constant-ratio contradiction in characteristic three

The invariant relations now imply p²=2*q³ with q!=0. Unique factorization
and homogeneity yield q=c*ell², p=e*ell³, with ell a nonzero linear form.
Polarization in characteristic three is valid because two is invertible.
For U=ker(ell|W), dimU=4 and U is perpendicular to W for the nondegenerate
Frobenius pairing, so W-perp=U.

Since p|W=e*ell³, its differential on W is identically zero. Thus
G=grad p=p N^-t belongs to W-perp=U. Along N+tG the determinant is constant,
because ell is constant. But the first coefficient of

    det(I+t N^-1 G)=det(I+t p Q)

is p*trQ=2*p*mu!=0, a contradiction. This proves the proposed cap four
in characteristic three, as a written argument awaiting independent review.

The maintained verifier checks the qC factorization, F2 identity, directional
derivatives, trace/squared-second invariants and cubic coefficient reduction
modulo three, with denominators checked before reduction. Two finite controls
exercise scalar and nonscalar B. These checks corroborate algebra; the radical
containment, integrality and Frobenius arguments remain written proofs.
This is not a generic-rank-seven argument: that rank statement is false in
characteristic three. The exact original scratch hashes are retained as
discovery provenance, not treated as independent review.
