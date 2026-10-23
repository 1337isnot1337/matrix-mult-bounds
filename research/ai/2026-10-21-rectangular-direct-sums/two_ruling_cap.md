# A two-ruling dimension bound closes ordinary A89 to M30

October21,2026. Written proof, unreviewed. No historical-priority claim.
This is an ordinary-restriction obstruction, not an improved exponent.

## Bilinear dimension lemma

Let Phi:U tensor V -> W be surjective over an algebraically closed field.
Fix an integer r>=6. Suppose that

- dim Phi(U0 tensor V)<=r for every subspace U0 of dimension at most2;
- dim Phi(U tensor V0)<=r for every subspace V0 of dimension at most2.

Then dim W<=floor(r^2/4). In particular r=7 gives dimension at most12.
The argument applies over C and over the algebraic closure of C(x,z).
If either input has dimension at most one, the conclusion follows at once
from dim W<=r<=floor(r^2/4). Assume both inputs have dimension at least two.

Write p=dim Phi(u,V) and q=dim Phi(U,v) for generic u,v. Both lie between1
and r unless W=0. Let p_k be the generic dimension of
Phi(span(u1,...,uk),V). Generic submodularity gives

    p_(k+1)-p_k <= p_k-p_(k-1).

Indeed, the sum of the two spaces from u1,...,u_(k-1),uk and from
u1,...,u_(k-1),u_(k+1) is the space for all k+1 vectors. Their
intersection contains the space for the first k-1 vectors.

Also p_q=dim W. Choose q generic fixed u_i. For generic v, the vectors
Phi(u_i,v) span Phi(U,v). Thus all of Phi(U,v) lies in the fixed sum of
the q row spaces. Polynomial continuation gives that containment for
every v, so those row spaces span W. Interchanging the inputs gives the
corresponding column statement. This also proves the product bound d<=pq.
Concavity and p_2<=r give

    d <= min(pq, p+(q-1)(r-p), q+(p-1)(r-q)).             (1)

Assume p<=q by interchanging the inputs. If p<=2, the third expression
in (1) is at most r, so the result follows. If p>=3, it is

    rp-r+q(2-p) <= -p^2+(r+2)p-r.

The integer maximum of this quadratic is floor(r^2/4)+1. If q>p, the
first inequality loses at least one, giving the desired bound. Therefore
the only possible failure is d=floor(r^2/4)+1 with p=q and p an integer
nearest to (r+2)/2. For r>=6 these values have

    p>=4,  c=2p-r in {1,2,3},  and p'=r-p>=2.

Equality in the concavity bound forces p_2=r and p_3=2r-p; otherwise
p_q would be smaller than d. For three generic row spaces E1,E2,E3,
each of dimension p, every pair intersection has dimension c. Moreover

    dim(E3 intersect(E1+E2)) = p+r-(2r-p)=c.

This contains E3 intersect E1 and E3 intersect E2, both of dimension c.
They coincide and equal E1 intersect E2. Fixing generic E1,E2 gives a
fixed c-dimensional space L contained in every generic row space.

Pass to W/L. Its generic row rank is p'=p-c=r-p, and its generic column
rank q' is at most q=p. In the exceptional quadratic-equality cases,

    dim(W/L)=d-c=p' p.

The product bound therefore forces q'=p and equality in that bound.
Choose p generic u_i whose p'-dimensional row spaces span W/L. They form
a direct sum. Choose p' generic v_j that give a basis in every one of
these finitely many row spaces. The p*p' vectors Phi(u_i,v_j) modulo L
form a basis of W/L. Hence the restriction from span(u_i) tensor span(v_j)
is a linear isomorphism onto W/L. Independence of the images also proves
independence of the selected u_i and v_j.

Since p'>=2, select two of the v_j. With all p of the u_i, their images
have dimension2p>r. But quotienting cannot increase the assumed dimension
bound r for a two-dimensional second input space. This contradiction
excludes the exceptional value and proves d<=floor(r^2/4).

The restriction r>=6 matters. The map sending u,v in C4 to the seven
coordinates u1*v1,u1*v2,u1*v3,u1*v4,u2*v1,u3*v1,u4*v1 has two-ruling
bounds5 but full image dimension7>floor(25/4). It prevents an unjustified
extension to r=5. For even r=2h>=6, the full tensor-product map on
C^h tensor C^h has two-ruling bound2h and image dimensionh^2, so the
stated bound is sharp in those even cases. No odd-case sharpness is claimed.

## Three-ruling variant

More generally suppose every input subspace of dimension at most k, on
either side, has image dimension at most r, where k>=2. Keep p,q and p_j
as above. If p<=k or q<=k, then d<=r. Otherwise concavity gives

    p_k-p_(k-1) <= floor((r-p)/(k-1)),

because the k-1 increments from p_1 to p_k are nonincreasing. Therefore

    d <= min(pq,
             r+(q-k) floor((r-p)/(k-1)),
             r+(p-k) floor((r-q)/(k-1))).              (2)

This is valid also for p=k or q=k, with bound r. Maximizing over1<=p,q<=r
is a finite general bound. For r=8,k=3 it gives d<=11. For an explicit
check assume p<=q: p<=3 gives8; p=4 gives at most10; p=5 gives at most10;
p=6 gives at most11; p>=7 gives at most8. The eleven-coordinate cross map
on C6 tensor C6, taking its first row and first column, attains11: a
three-input ruling lies in a fixed five-dimensional space plus at most
three further directions. Thus this particular bound is sharp.

For A99 to M(32,33,33), a rank-three parameter on its1056-dimensional
first leg lifts to rank at most

    3*33+(1377-1089)+(1377-1056)=708<729=9*81.

Its9-by9 scalar Hankel symbol has rank at most8. The existing coordinate
certificates bound linear spaces in that cone by8. Applying (2) bounds
the scalar image by11, hence the full parameter space by11*81=891<1056.
This excludes that ordinary target as well, without a singular-limit claim.

## Application to the final dimension1152 ordinary target

For A(8,9), each source leg has dimensionN=1152. An ordinary M30 target
has900 coordinates per leg, so each of its two projected slice legs loses
252 dimensions. A rank-at-most-two matrix parameter therefore lifts to a
source slice of rank at most

    2*30+252+252=564<576=8*72.

By the maintained source slice bound, its scalar8-by9 Hankel symbol has
rank at most7. Over the algebraic closure of C(x,z), every image of a
linear parameter space U0 tensor V or U tensor V0 with dim U0 or dim V0
at most2 is a linear space in that rank-seven Hankel cone. The12870
existing integer minor witnesses and the torus argument bound every such
linear space by7 dimensions.

The bilinear lemma now bounds the entire scalar symbol image by12.
Select twelve independent scalar coefficient coordinates, or fewer if the
image is smaller. Each is a polynomial in x,z with at most8*9=72
coefficients. Their joint vanishing forces the whole symbol to vanish.
The full900-dimensional target parameter space would therefore inject
into a space of dimension at most12*72=864. This is impossible.

Hence A(8,9) cannot ordinarily restrict to M30. The proof allows arbitrary
ordinary linear maps, including cancellations. It does not exclude a
general singular degeneration. The formerly surviving ordinary target is
closed, and the single-target scan through source dimension1152 has no
remaining ordinary candidates under these written lemmas.

## Finite checks and limits

`two_ruling_cap.py` enumerates (1) for r=6,...,20, reconstructs every
exceptional equality case, and checks symmetric-product and excluded-r=5
controls by exact integer linear algebra. The k-ruling bound and the
sharp r=8,k=3 cross control are checked as well.
The A89 Hankel coordinate certificates are the previously verified ones.
These finite checks do not replace the general proof above, independent
review, or formalization. No target maps or smaller exponent are claimed.
