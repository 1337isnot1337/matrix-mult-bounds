# The rank-two cubic sharpens the A(3,3) ordinary cap

October 21, 2026. Written proof, unreviewed. No exponent improvement.

Let X be the cone of five coefficient sequences whose3-by3 Hankel matrix
has rank at most two. If a linear map Phi:U tensor V -> C^5 sends decomposable
inputs into X, then dim im(Phi)<=2.

## Proof

Every linear subspace in X has dimension at most two. The same torus-limit
argument used in `saturation.md` reduces this to the ten coordinate
three-spaces; `hankel-a3-b3.json` gives exact determinant witnesses for all ten.
This is a certified special case of that argument, not an assumption that
all pointwise low-rank sequences share one fixed recurrence.

Let p,q be the generic dimensions of the two bilinear rulings. Both are at
most two by the linear-space cap. The elementary bilinear span bound gives
W=im Phi dimension at most pq<=4: choose q fixed u_i whose images span the
opposite ruling for generic v, then use polynomial continuation.

If dim W=3, both ruling dimensions are two. The projective image closure Y
is irreducible and spans P(W)=P2. It contains a projective line from every
generic first ruling. If it had dimension one it would equal such a line,
contrary to its span. Therefore it is all of P2. This would put a three-
dimensional linear space in X, a contradiction.

If dim W=4, choose u_1,u_2 as in the bilinear span bound. Their ruling
spaces must be two-dimensional and disjoint. Choose v_1,v_2 whose images
span both spaces. The restriction to span(u_1,u_2) tensor span(v_1,v_2) is
then a linear isomorphism onto W. Its decomposable image is a smooth quadric
Q in P3, which lies in X.

The cubic Hankel determinant restricted to W is nonzero; otherwise W itself
would contradict the linear-space cap. It vanishes on Q, so it is the product
of Q's irreducible quadratic equation and a nonzero linear form. The latter
factor gives a three-dimensional linear hyperplane in W lying in X, again
contradicting the cap. Both larger dimensions are impossible, proving the claim.

## Source consequence

For A(3,3), N=45 and ab=9. An ordinary M6 target has output kernels of
dimension9. Every lifted rank-one parameter slice has source rank at most
6+9+9=24<27, so its scalar Hankel symbol has rank at most two. The preceding
claim applies over the algebraic closure of C(x,z). Choosing two independent
coefficient coordinates injects the full target block into at most2ab=18
dimensions, whereas Mat6 has dimension36. Thus A(3,3) cannot ordinarily
restrict to M6. Larger squares already exceed the source leg dimension.

This does not exclude M5: its corresponding lifted bound is45, outside this
argument. A saved numerical A33-to-M5 fit elsewhere in the repository remains
a numerical fit, not an exact starting map. It must not be used as though it
were a completed restriction when attempting to add a sixth vertex.

No arbitrary singular degeneration is excluded. The current small ordinary
square ceiling is five, without a claim that an exact M5 restriction exists.
