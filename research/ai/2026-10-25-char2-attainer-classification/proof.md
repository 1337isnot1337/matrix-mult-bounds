# Three geometric characteristic-two quadratic attainers

October 25, 2026. Claim `AI-CHAR2-QUADRATIC-ATTAINERS-001` is
**proof-written-unreviewed**. Exact algebra and separate same-session audits
support the argument; they are not independent review or formalization.

## Statement

Let k be an algebraically closed field of characteristic two. Let W be a
three-dimensional k-linear space of 3-by-3 coefficient matrices for the
complete quadratic source R, with det R identically zero on W and
D=det M not identically zero. Then W is equivalent to exactly one of

    P(t,x,y)=[[x,x,0],[0,t,0],[0,y,y]],
    N(t,x,y)=[[t,x,0],[0,t,x],[0,y,0]],
    V(t,x,y)=[[x,0,0],[y,t,x],[0,0,y]],

under permitted independent binary coefficient changes and optional
transpose. The source condition is geometric rank at most fourteen.
The previously proved sharp cap is three, so these are precisely its
geometric attainers. All three representatives have exact source rank
fourteen wherever their coefficient determinant is nonzero.

The same conclusion applies after extending any characteristic-two ground
field K to its algebraic closure. It is not a classification of K-forms
or a descent theorem. Section 7 gives two inequivalent forms over GF2
that become equivalent over its algebraic closure. No compatible three-leg
tensor map, historical priority or matrix-multiplication exponent
improvement is claimed.

## 1. Pinned premises and permitted actions

Use the complete literal source, including every endpoint,

    R(M)[(j,L),(H,r)]=M[H-j,L-r],
    j,r=0,1,2, L,H=0,...,4,

with lexicographic pair orders and zero outside the coefficient range.
All imported statements and conventions are pinned in sources.json.

For g=[[a,b],[c,d]] define the characteristic-two binary coefficient action

    A(g)=[[a^2,ac,c^2],[0,ad+bc,0],[b^2,bd,d^2]].

The permitted transformations M -> A(g) M A(h)^t and M -> M^t preserve
source rank. They give det A(g)=det(g)^3 and
e'=delta*e, D'=delta^3*D, where e=M11 and delta=det(g)det(h).
Thus U=ker(e) is an intrinsic section. Common right kernels transform by
A(h)^(-t), common left kernels by A(g)^(-t); transpose swaps the sides.
These are dual actions, not ordinary A(g) actions on kernel vectors.

The pinned integral-linear-form lemma gives a k-linear ell with

    T4=D*ell, D=e*(A2+e*ell+ell^2), A2=bh+df,

for M=[[a,b,c],[d,e,f],[g,h,i]]. Since D is nonzero, e is nonzero and
U has dimension two with D|U=T4|U=0. The pinned singular-pencil lemma
then gives a nonzero common right or left kernel of U. After transpose
if necessary, choose a common right kernel line.

The permitted dual binary action has three projective kernel-vector orbits
over k, represented by e0=(1,0,0), eta=(0,1,0), and e0+eta.
The conic Q(z)=z1^2+z0*z2=0 is the evaluation orbit. The eta line is fixed
because A(g)^t*eta=det(g)*eta; the third orbit consists of all other
non-evaluation lines. The pinned evaluation-kernel classification proves
that any W whose U has an evaluation right or left kernel is P or N.
Only eta and e0+eta remain to be treated.

We also use the original-coordinate adjugate identities

    S(adj M)=T4+eD, S(u*v^t)=Q(u)Q(v),
    S(B)=B11^2+B10*B12+B01*B21+B00*B22,

and the pinned fact that no primitive homogeneous linear vector in k[x,y]^3
can satisfy Q=0. The latter follows by two explicit Plucker identities.
We never assume an arbitrary GL3 coefficient change preserves the source.

## 2. The eta section: remove the evaluation cases

Assume U*eta=0, so its middle column is zero. If U has generic rank at most
one, the rank-one pencil lemma gives a fixed image line or a fixed row
functional. A fixed image gives a common left kernel of dimension at least
two; a fixed row gives a common right kernel of dimension at least two.
Every projective line meets the conic Q=0 over the algebraically closed
field k. Hence either case lies in the prior evaluation-kernel locus.

Suppose U has generic rank two and has a common left kernel lambda.
Choose a rank-two member B. Its common right and left kernels are then
the full one-dimensional kernels of B, so
adj(B)=c*eta*lambda^t with c nonzero. The adjugate identity gives

    0=S(adj B)=c^2*Q(eta)*Q(lambda)=c^2*Q(lambda).

Thus lambda is an evaluation vector and this case also lies in the prior
classification. Among P and N, only P can have a common eta kernel on
one side: N has one evaluation kernel and zero kernel on the other side.
The eta case inside the evaluation locus is therefore P, up to transpose.

It remains to treat generic-rank-two U with no common left kernel.

## 3. Normalize the moving section by permitted actions

Choose homogeneous parameters x,y on U. Because the middle column is zero,
only the middle row of adj M can be nonzero, so

    adj M=eta*v(x,y)^t

for a nonzero homogeneous quadratic vector v. Since T4=D=0 on U,
Q(v)=0. Let gamma be the homogeneous gcd of its entries and w=v/gamma.
A degree-two gamma would leave constant w, giving a common left kernel.
A degree-one gamma would leave a primitive linear w with Q(w)=0, which
the pinned linear-vector lemma forbids. Consequently gamma has degree
zero and v is primitive quadratic.

Write v=(v0,v1,v2). Neither v0 nor v2 can vanish: Q(v)=0 would then make
v1=0, leaving a single homogeneous quadratic entry, contrary to primitivity.
Also v0,v2 are coprime; a prime dividing both would divide v1 as well.
From v1^2=v0*v2, unique factorization now makes each of v0,v2 a nonzero
constant times the square of a homogeneous linear form. The constants
have square roots in k. Renaming these forms gives exactly

    v=(y^2,xy,x^2).

They are independent, since dependence would give a common factor in v.
This only changes the parameter basis of U; no arbitrary GL3 source
transformation has been used.

The degree-one column syzygies of (y^2,xy,x^2) are precisely the span of

    (x,y,0)^t, (0,x,y)^t.

Indeed, for a vector (a0*x+b0*y,a1*x+b1*y,a2*x+b2*y), coefficient comparison
in its pairing with (y^2,xy,x^2) gives
a2=b0=0, a1=b2, a0=b1. The two outer columns of M are therefore K(x,y)C,
where

    K(x,y)=[[x,0],[y,x],[0,y]]

and C is a constant 2-by-2 matrix. Generic rank two forces C invertible.
The permitted right action on these outer columns is entrywise-square h,
denoted h^[2]. Over k choose h with h^[2]=C^(-1). This normalizes U to the
full three-column pencil [[x,0,0],[y,0,x],[0,0,y]].

## 4. Exhaust the extension of the moving section

Let t=e. Absorb the t-components of entries M00 and M10 into x,y.
Every extension of the normalized section is then

    M=[[x,b*t,c*t],[y,t,x+f*t],[g*t,h*t,y+i*t]],
    ell=L*x+J*y+B*t,

where b,c,f,g,h,i,L,J,B are scalars. Direct coefficient comparison in
D/t=A2+t*ell+ell^2 first gives

    h=L^2, b=J^2, i=L+J^2*g+f*L^2,

and leaves the equations

    J+b*i+c*h+f=0,
    B^2+B+b*f*g+b*h+c*g=0.

After these three substitutions, the x^3*t, y^3*t and x*y^2*t coefficients
of T4-D*ell give respectively

    g=L^3, c=J^3, f=L*J^2+J.

The x*y*t^2 coefficient then forces B=L^2*J^2. Substitution makes every
remaining coefficient of both equations vanish. Thus the entire normalized
moving-section chart is the two-parameter family

    M_LJ=[[x,J^2*t,J^3*t],
          [y,t,x+(L*J^2+J)*t],
          [L^3*t,L^2*t,y+(L+L^2*J)*t]],
    ell=L*x+J*y+L^2*J^2*t.

No division by L, J, or their products was used, so zero and exceptional
parameter values are included. D has the term t*x*y with coefficient one,
and is not the zero polynomial. Conversely the two displayed integral-form
equations imply the source determinant identity in characteristic two,
so every M_LJ has geometric source rank at most fourteen.

The section quadratic is

    q_U=(D/e)|U=x*y+L^2*x^2+J^2*y^2.

The full D/e becomes this binary quadratic after the shifts
x'=x+L*J^2*t, y'=y+L*t. This shift identity is an additional check, not
needed for the geometric normalization below.

## 5. Remove L,J by a permitted section stabilizer

For G=[[a,b],[c,d]], direct multiplication gives

    A(G)K(x,y)=K(a*x+c*y,b*x+d*y)*G^t.

Choose H so that H^[2]=(G^t)^(-1), which is possible over k. The permitted
pair A(G) M A(H)^t then preserves the normalized moving section, with
parameter change (x,y)^t -> G^t*(x,y)^t. Set delta=det(G)det(H).
Since det(H)^2=det(G)^(-1), one has delta^2=det(G).

The polynomial D/e transforms by delta^2. Written in the new section
parameters z, its restriction is therefore

    q'_U(z)=det(G)*q_U((G^t)^(-1)z).

The inverse parameter substitution multiplies the polar xy coefficient
by det(G)^(-1), so the displayed scalar restores that coefficient to one.
This scalar cannot be discarded.

The binary quadratic q_U has xy coefficient one and hence nonzero polar
form. Over k it factors into two distinct linear forms. Choose G carrying
these two factor lines to the coordinate axes. Then q'_U is exactly xy,
rather than merely an uncontrolled scalar multiple of xy.

Normalize the new e coordinate to t and subtract section directions from
the new complement as in Section 4. The normalized extension again has the
classified form M_(L',J'), now with
q'_U=xy+(L')^2*x^2+(J')^2*y^2. Hence L'=J'=0, and the entire family is V.
This proves that the eta case outside the evaluation-kernel locus is V.

## 6. Exclude the mixed kernel e0+eta

Suppose U has common right kernel (1,1,0). Since e=0, its matrices have form

    [[a,a,c],[0,0,f],[g,g,i]],
    T4=(ai+cg)^2+ag*f^2=0,

where the five entries are linear forms on U.

If f is nonzero, unique factorization implies that the nonzero linear
forms a,g are proportional unless one vanishes: distinct prime linear
forms would have odd multiplicity in ag*f^2 but even multiplicity in
(ai+cg)^2. If a=g=0, U is third-column-only and has a two-dimensional
common right kernel; it therefore has an evaluation kernel over k.
Otherwise (a,0,g) has a fixed nonzero coefficient direction. The permitted
left action on the two outer coordinates is entrywise-square GL2, so it
can send this direction to e0 over k. This preserves the common right
kernel and scales e. Reapply the integral lemma to the transformed W:
T4=0 on its U. Now g=0 and a is nonzero, so a^2*i^2=0 implies i=0.
Every section matrix has bottom row zero, giving evaluation left kernel e2.

If f=0, the middle row is zero and the outer block [[a,c],[g,i]] is an
injective representation of the two-dimensional U with identically zero
determinant. The rank-one pencil lemma gives a common image line or a
common row functional. In the full 3-by-3 space these yield a common left
or right kernel of dimension at least two, respectively. Again its
projective line meets Q=0 over k.

Every mixed case thus belongs to the evaluation-kernel locus and must be
P or N. But P has only an evaluation kernel line and the eta line, while
N has only one evaluation kernel line. Neither has a mixed kernel line.
The dual binary action preserves the conic and the eta line; transpose
merely exchanges the sides. This contradiction excludes the mixed case.
The three cases now exhaust all possibilities by Section 1.

## 7. Converse, inequivalence, and the ground-field boundary

The pinned universal-plane packages provide integer certificates for P,N,V:
each has geometric source rank at most fourteen and exact rank fourteen
at coefficient-invertible points. Their intrinsic-section common right/left
kernel dimensions, with these chosen orientations, are

    P: (1,1), right span(1,1,1), left span(0,1,0);
    N: (1,0), right span(1,0,0);
    V: (1,0), right span(0,1,0).

These dimensions are invariant up to swapping. The sole line for N lies on
Q=0, whereas the sole line for V is eta and Q(eta)=1. Thus the three
representatives are pairwise inequivalent under all permitted actions,
including transpose, proving “exactly one” in the statement.

The field hypothesis in the classification cannot simply be dropped.
Both V=M_00 and

    M_11=[[x,t,t],[y,t,x],[t,t,y]]

are defined over GF2 and satisfy the source identities. V has only one
coefficient-invertible GF2 matrix, whereas M_11 has three: t must be one,
and direct enumeration of its four (x,y) choices gives three nonzero
determinants. Any invertible left-right action, parameter-basis change,
or transpose preserves this count. They are therefore inequivalent over
GF2, although Section 5 makes them equivalent over the algebraic closure.
For M_11 the shifted binary quadratic x^2+xy+y^2 is irreducible over GF2.
This is a concrete nontrivial ground-field form, not a classification of
all such forms.

## Discovery corrections and evidence limits

The entire eta locus is not just V: its evaluation branch is P up to
transpose. A fixed-kernel witness initially treated as a possible new orbit
is instead exactly P(t,x,t+x+y)^t A([[1,0],[1,1]])^t in characteristic two.
It is preserved as a regression guard.

An initial finite orbit-search script used the wrong coefficient matrix
and an incorrect row-elimination routine. Its outputs are discarded.
Both defects, the corrected script and an independent exact shear identity
are retained in the discovery pins. The geometric proof above does not
depend on that search or on a finite census.

The new contribution is exhaustion of the remaining eta and mixed cases,
the permitted stabilizer and scalar normalization, and the ground-field
boundary example. Earlier packages retain all source, integral-form,
pencil-lemma, evaluation-case and representative attribution. Exact controls
check polynomial identities and witnesses; they do not certify UFD
factorization, geometric exhaustion, or descent. The proof remains written
and unreviewed. Compatible tensor maps and exponent improvement remain open.
