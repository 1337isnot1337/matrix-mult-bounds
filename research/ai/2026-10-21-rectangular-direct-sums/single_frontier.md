# Ordinary single-target frontier through source dimension1152

October21,2026. Finite application of the maintained written lemmas.
Their general proofs remain unreviewed. No new construction or exponent.

The complete scan of71 source formats A(a,b), with2<=a<=b and
N=ab(a+b-1)<=1152, contains1200 sorted rectangular target shapes with
leg dimensions at mostN and strict9/4 score gain. The baseline tests
exclude1181. Rank-three saturation excludes15 more, and the second
Hankel boundary excludes3. Only A(8,9) -> M(30,30,30) survives.

The score test is the exact integer inequality

    216 u v w > [3(a+b)-2]^4.

Sorted shapes u<=v<=w are exhausted by v<=floor(sqrt(N)) and w<=N/v.
Cyclic permutations and reversing the source orientation cover the target
axis orders and the interchange of a,b. The a=1 case cannot improve this
score at any size: leg dimensions imply uvw<=b^3, and, writing b=t+1,

    (3b+1)^4-216b^3 =81t^4+216t^3+216t^2+120t+40>0.

This is a finite ordinary-restriction frontier. It does not exclude
singular degenerations, tensor powers, multiple summands or larger sources.

## Closing the balanced size-eight candidate

The earlier balanced-source scan retained M(27,28,28) from A(8,8)
under its weaker tests. Its target leg dimensions are756,784,756, while
N=960 and ab=64. A rank-at-most-three parameter on the first target leg
lifts to source slice rank at most

    3*28+(960-784)+(960-756)=464<512=8*64.

Its scalar8-by8 Hankel symbol therefore has rank at most7. The cone of
such length15 scalar Hankel sequences has dimension14. Since14<3(3+2),
the projection-saturation lemma extends this containment from rank-three
parameters to the whole linear parameter image.

Every linear space in this scalar Hankel cone has vector dimension at
most7, by the maintained torus argument and all6435 integer coordinate
minor certificates for A88. Choosing seven independent coefficient
coordinates bounds the full parameter dimension by7*64=448. But its
actual dimension is27*28=756. This contradiction excludes the ordinary
restriction. It applies to arbitrary maps, not just coordinate selections.
No general singular degeneration is excluded by this argument.

## Exact finite evidence

`single_frontier.py` saves every score-eligible shape and its gate or
witness in `single-frontier-1152.json`. Saturation is used only for
A79,A88,A89. The6435+6435+12870 existing coordinate certificates were
replayed with integer determinants. The second-boundary uses A710 and
the previously recorded rank-six controls. All imported proofs retain
their stated assumptions and review status.

The surviving ordinary M30 target is described in
`single_matrix_target.md`, including its conditional exponent implication.
Passing every gate does not supply a tensor restriction. Its maps remain
missing, so the displayed conditional improvement is not attained.
