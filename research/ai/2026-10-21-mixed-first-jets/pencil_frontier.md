# All maximal mixed first pencils are trapped

Written proof, unreviewed, October 21, 2026. No exponent improvement.

For the canonical rank-four leading maps, **first quotient ranks 14 and 6,
in either order, are impossible for a limit M(10,10,11)**. Consequently a
compatible first derivative with any mixed component must have quotient
rank sum at most **19**, improving the earlier necessary bound of 20.
If both mixed projections are nonzero, the elementary block argument
below already gives a rank-sum bound of 16.

All higher regular coefficients and an arbitrary Laurent first-leg map
are allowed. The result does not exclude smaller or delayed first
extensions, other leading flags, or general tensor degenerations.

## 1. The only maximal mixed pairs form a projective line

Use the canonical extensions E_B/G,E_C/G, each a direct sum of a
12-dimensional boundary quotient and a four-dimensional mixed space.
The concurrent [second-jet theorem](../2026-10-21-second-jet-rank-one/rank_one.md)
proves H_actual=0 for any target. Its [block identity](../2026-10-21-second-jet-rank-one/boundary_spanning.md)
identifies the mixed-by-boundary contraction, after fixed invertible
coordinate changes, with X(v) tensor I6, where

    X(v) = [[v3,v1],[v2,v0]].                         (1)

Suppose r_B=14 and r_C=6. The previous rank-deficit argument shows that
the C space is pure boundary: if both sides had mixed projections, each
quotient rank would be at most 10. Let U be the mixed projection of the
B space. No X(v), v in U, can have rank two, since such a vector would
annihilate no nonzero opposite boundary covector. A linear subspace of
Mat2 consisting of matrices of rank at most one has dimension at most
two. Therefore U has dimension two, and the B space contains the entire
12-dimensional boundary quotient.

Every two-dimensional rank-one matrix space has either a common kernel
or a common image. In the common-image case its two independent row
factors have zero common kernel; (1) then gives zero opposite boundary
annihilator, contradicting r_C=6. Hence U is a common-kernel plane.

Write

    m_(j,z)=e_(0,j,z)+e_(3,j,z-3), j in {1,2}, z in {4,5}.

In the canonical mixed coordinates, all common-kernel planes are

    U_lambda = span(m_(1,4)+lambda*m_(2,4),
                    m_(1,5)+lambda*m_(2,5)),          (2)

including U_infinity=span(m_(2,4),m_(2,5)). The opposite boundary
annihilator has dimension six and is unique. Thus the original first
spaces, after removing G components and changing output row bases, are
exactly the pairs V_B(lambda),V_C(lambda) described by (2). There are no
remaining boundary graph parameters: B already contains all boundary
directions, and C is pure boundary.

For completeness, the rank-one matrix-space fact is elementary. Fix a
nonzero u*v^T in the space. Any other rank-one element must share its
column line or its row line, or their sum has rank two. If there were
elements sharing opposite factors but not both, their sum would again
have rank two. Thus one factor is common to the whole space.

## 2. Two source-symmetry representatives

For t nonzero, scale every source covector e_(i,j,z) by

    t^(i+j+z-6).

Every source term has total exponent zero, so this is an exact tensor
automorphism. It scales G_z by t^(z-3), preserving the leading flag after
invertible output row rescaling. Both terms of m_(j,z) have weight
j+z-6, so it sends lambda to t*lambda in (2). Consequently all finite
nonzero lambda are equivalent to lambda=1.

The simultaneous reversal

    (i,j,z) -> (3-i,3-j,6-z)

also preserves every source term, sends G_z to -G_(6-z), and interchanges
the endpoint pencils lambda=0 and infinity. The maintained verifier
checks both source identities on all 4096 terms and the mixed weights.
Thus only lambda=0 and lambda=1 need to be treated. The endpoint case
is the [preceding third-order theorem](third_order.md).

## 3. A stronger constraint on a projected target subspace

Let R be the first-slice space of M(10,10,11). Up to invertible row and
column coordinates it is

    R = {A tensor I11 : A in Mat10}.

Let pi discard four leading rows and four leading columns. Suppose a
linear subspace R' of R has projected image supported in a fixed
14-by-6 rectangle. Then

    dim pi(R') <= 2.                                 (3)

First, pi is injective on R: its kernel consists of old-cross matrices
of rank at most eight, whereas every nonzero element of R has rank at
least eleven. For r in R', its projection has rank at most six, whence

    rank(r) <= 6+8 = 14 < 22.

Ranks in R are multiples of eleven. Therefore the corresponding
10-by-10 matrices all have rank at most one. The elementary common-factor
argument just given applies in arbitrary dimensions too. Let k=dim R'.

If the right factor is common, the column projection of codimension
four preserves at least seven of its eleven internal directions.
As the left factor ranges over a k-dimensional space, their collective
column image before the row projection has dimension at least 7k.
The row projection removes at most four dimensions in total. The
projected rectangle therefore requires

    7k-4 <= 14,   hence k <= 2.

If the left factor is common, the transposed argument gives

    7k-4 <= 6,    hence k <= 1.

This proves (3). More generally, for rank-one underlying slices and
projection losses e_B,e_C, supports r_B,r_C give

    k <= max(floor((r_B+e_B)/(n-e_C)),
             floor((r_C+e_C)/(n-e_B))).

Only n=11, e_B=e_C=4, r_B=14, r_C=6 is used here. The argument relies
on the target's repeated identity factor; minimum rank alone would not
give this dimension bound.

## 4. The generic pencil's normal space and cubic minors

The lambda=1 seed is stored in `generic-pencil-seed.json`. Its B space
is exactly the boundary quotient plus the two rows in (2), and its C
space is the full six-dimensional opposite boundary annihilator.
The saved `generic-pencil-twojet.json` is rebuilt by the existing rational
constructor and verified by the complete coefficient replay.

As in the endpoint proof, the first normal equations leave dimension
228, and the mixed off-diagonal equations have rank 212. The resulting
sixteen normal directions are exactly the independent directions in
the generic seed. All their linear and quadratic combinations have
explicit second-order corrections.

On x in K_inf, the correction-independent projected third coefficient is

    J_D(x)[b,c] = T(x,b'_D,c)+T(x,b,c'_D)-T(y_x,b,c).   (4)

The invariance under arbitrary later corrections is the same as in
`third_order.md`, Section 2: differences of new-row corrections belong
to F_B,F_C, and their pairings with V_C,V_B vanish on K_inf. Rows outside
the fourteen and six first directions contribute zero to this projection.

Flatten (4) as a 64-by-84 matrix linear in the sixteen normal parameters.
The certificate retains **twelve 3-by-3 triangular minors**. Each has
three nonzero scalar multiples of a single linear form on its diagonal.
Its determinant is therefore a nonzero constant times that form cubed.
If the flattening has rank at most two, all twelve forms must vanish.
They are independent. Their four-dimensional common kernel annihilates
the entire flattening and is exactly the common-plane tangent space.

`pencil_frontier.py` reconstructs all coefficients, checks the diagonal
forms and every claimed triangular zero, replays the rank-twelve
certificate, and compares the final direction space with the explicit
plane tangents. It verifies retained witnesses rather than rerunning
the discovery search. Thus every nonzero third obstruction has first
flattening rank at least three, for every complex parameter value.

## 5. All-order consequence

Apply the moving-plane induction from `third_order.md`. At the first
normal departure order N, its first two coefficient equations place D
in the complete sixteen-dimensional normal space above. Regularize a
moving K_inf row through order N+1 and divide by t^(N+2). The constant
rows lie in L0=R direct-sum W0; their projected block is exactly (4).

Projecting away W0 identifies their R components with the space J_D(K_inf),
supported in the fixed 14-by-6 rectangle. Equation (3) forces this space
to have dimension at most two. The cubic minors then force J_D=0 and
D to be common-plane motion. Absorb that motion into the formal plane
at order N and continue the induction.

Both generic maps remain in moving boundary spaces of rank 56, which
cannot have a regular limit concise in 110 coordinates. This excludes
lambda=1, and the symmetries and endpoint theorem exclude every pencil
in (2). Interchanging the two output legs gives the reversed 6-by-14
case as well; source short-index transposition realizes the corresponding
exchange of the extension blocks.

## 6. The improved necessary rank sum

If only one mixed projection is nonzero and the other space is nonzero,
the previous block bound gives r_B<=14,r_C<=6, up to exchange. Sum 20
would require the excluded maximal pair, so the sum is at most 19.
If the other space is zero, the sum is at most 16 directly.

If both mixed projections are nonzero and one contains a rank-two X(v),
the opposite pure-boundary intersection is zero. That side has dimension
at most four; the first side has pure-boundary dimension at most six
and mixed dimension at most four, giving sum at most fourteen. If
neither mixed projection contains a rank-two element, each has dimension
at most two, and both pure-boundary intersections have dimension at most
six, giving sum at most sixteen. This proves the asserted bounds.

## Attribution and remaining work

This proof adopts the concurrent no-second-growth theorem and its complete
matrix block identity, the earlier moving-boundary induction, and the
endpoint third-order result. The new argument uses rank divisibility and
common-factor matrix spaces to bound the projected target dimension,
then twelve cubic minors for the generic pencil. It does not supply a
matrix target. The written proof and exact finite checks have no
independent review or formalization. The next construction question must
use smaller or delayed first extensions, or different leading flags.

After writing this argument, the concurrent quantum worker's
`research/ai/2026-10-21-third-boundary-trap/proof.md`, Section 5, was
inspected at commit `1068ce94f58466cb553d138b82540a8b128f6097`.
It independently uses the same rank-divisibility and common-factor
principle, together with a broader joint-support estimate, to prove
projected third first rank at most two for every admissible ordinary
first pair. That result subsumes the target-side bound in Section 3;
we retain its direct special-case proof and credit the overlap. The
new generic-pencil minors and maximal-pair classification here remain
separate source calculations. This inspection is not independent review.
