# A second universal maximal invertible quadratic three-plane

October 25, 2026. Claim `AI-QUADRATIC-CHAIN-THREE-001` is
**proof-written-unreviewed**. Exact integer certificates and a separate
same-session reconstruction support this proof; they are not independent
mathematical review or formalization. No historical priority is claimed.

## Statement

For every field K, including finite and nonperfect fields, the coefficient
family

    N(t,x,y)=[[t,x,0],[0,t,x],[0,y,0]]

has dimension three, coefficient determinant -txy, and geometric source
rank at most fourteen for the complete quadratic source. Its source rank
is exactly fourteen whenever txy is nonzero. It is inclusion maximal among
linear families satisfying that geometric source-rank bound. It is not
equivalent, under permitted binary changes and optional transposition, to
the earlier universal plane

    P(x,y,z)=[[x,x,0],[0,y,0],[0,z,z]].

Consequently characteristic two has at least two inequivalent attaining
three-spaces over every ground field. In other characteristics these are
two inequivalent inclusion-maximal three-spaces, while the global maximum
is four. This does not classify all three-spaces or supply a compatible
three-leg tensor map. No matrix-multiplication exponent improvement follows.

The rank condition is polynomial vanishing, rather than only a condition
on rational points. All parameters are independent polynomial coordinates.
Dependencies and original attribution are pinned in sources.json.

## 1. Full source and integer certificate

Use precisely the pinned literal source, with lexicographic pair orders:

    R(M)[(j,L),(H,r)]=M[H-j,L-r],
    j,r=0,1,2, L,H=0,...,4,

and out-of-range coefficients zero. The entries N00,N01,N21 recover
(t,x,y), so the family has dimension three over every field. Integer
expansion gives detN=-txy. In zero-based source column order the vector

    v=(0,0,-y^2,0,y^2,0,0,0,0,-ty,-xy,0,t^2,2tx,x^2)^t

satisfies R(N)v=0 over Z[t,x,y]. In particular the 2tx term must be retained
in the integer certificate even though it vanishes in characteristic two.
The coordinate -y^2 has a unit coefficient, so v remains a nonzero polynomial
vector over every field. Over K(t,x,y) it proves detR(N)=0; hence that
identity holds in K[t,x,y], including parameter values where v specializes
to zero.

Delete zero-based row0, pair(j,L)=(0,0), and column2, pair(H,r)=(0,2),
retaining the original order on the other rows and columns. Exact integer
determinant expansion gives

    det R(N)_(delete 0,2)=-t^2*x^7*y^5.

The maintained verifier and a separate pair-indexed regression reconstruct
this literal minor and expand it exactly. Its coefficient is a unit over
every field. Therefore rankR(N)>=14 whenever txy!=0, proving exact rank14
there. At t=x=y=1 both the coefficient determinant and this minor are -1;
no extension of the ground field is needed to obtain an invertible point.

For an independent invariant cross-check, the pinned integer invariants
are D=-txy, e=t, A2=-xy and T4=0. In particular D=e*A2 and

    P12=D^4+(eD+2T4)*(eD*T4+T4^2-A2*D^2)=0.

The pinned identity detR=D*P12 agrees with the direct kernel certificate.
No integer normalization is divided by before reducing characteristic.

## 2. A section invariant distinguishes the two planes

In characteristic different from two, every coefficient-invertible
geometric family has the intrinsic linear form

    m=e+2T4/D.

Its existence and relative covariance are proved in the pinned odd-attainer
package: if M'=A(g) M A(h)^t then m'=det(g)det(h)m, and transpose preserves
m. In characteristic two use e itself; the pinned ordinary binary action
gives e'=det(g)det(h)e, again preserved by transpose. Thus the section
U=ker(m) in odd characteristic, or U=ker(e) in characteristic two, is
intrinsic under the permitted equivalences. Both N and P have T4=0 and
D nonzero as polynomials, so their respective sections are simply e=0.

For a coefficient space U define its common right and left kernels by

    K_R(U)=intersection_(M in U) ker M,
    K_L(U)=intersection_(M in U) ker M^t.

Invertible left-right actions preserve their dimensions; transpose swaps
them. Thus the unordered pair of dimensions is an invariant of the
intrinsic section under all permitted equivalences.

For N, the section t=0 is spanned by

    B=[[0,1,0],[0,0,1],[0,0,0]],
    H=[[0,0,0],[0,0,0],[0,1,0]].

The equations B*u=H*u=0 give u1=u2=0, so K_R=K*(1,0,0).
The equations B^t*w=H^t*w=0 give w0=w1=w2=0, so K_L=0.
For P the section y=0 instead imposes u0+u1=u1+u2=0 on the
right and w0=w2=0 on the left. Thus K_R=K*(1,-1,1) and
K_L=K*(0,1,0). These calculations work in every characteristic.
The unordered pairs {1,0} and {1,1} differ. Therefore N and P are
inequivalent, even after extension of scalars and optional transposition.

## 3. Inclusion maximality in every characteristic

Suppose a larger linear geometric rank-at-most-fourteen family contains N.
Choose one additional direction; together with N it gives a four-space W.
Its coefficient determinant is nonzero because its restriction to N is
-txy. In characteristic two, this contradicts the pinned sharp cap three.

In characteristic different from two, the pinned four-dimensional
attainer classification implies the intrinsic identity 16D=m^3 on W.
Its integral linear form ell obeys T4=D*ell. Restricting this identity
to N gives 0=(-txy)*ell|N in the polynomial domain K[t,x,y], so ell|N=0.
Consequently m|N=e|N=t. Restricting 16D=m^3 then gives

    -16txy=t^3.

This is impossible as a polynomial identity: the coefficient of t^3
in t^3+16txy is one in every field. This also handles characteristic three
without dividing by three. Thus no larger W exists over any ground field.

## Discovery and evidence boundary

A finite GF2 polynomial census in the normalized common-evaluation-kernel
chart found this witness while investigating characteristic-two attainers.
It checked155 two-planes and8 complement cosets in each of two first-column
charts, finding4 square-chart and2 nonsingular-chart families. This finite
chart calculation is discovery evidence only, not a classification over
other fields or an exhaustion of all attainers. The proposed exclusion of
square first-column directions was falsified and abandoned. The first
witness has the integer certificates above, which establish its universal
scope independently of that finite census.

The previous packages retain full-source, determinant, cap and classification
credit. The new contribution is this explicit second family, its integer
kernel/minor, the section-kernel distinction and the maximality consequence.
Exact controls corroborate these statements and include mutation guards for
the characteristic-two-only omission of 2tx. All source pins and discovery
records are preserved. Independent review and tensor-map construction remain
open; the exponent has not changed.
