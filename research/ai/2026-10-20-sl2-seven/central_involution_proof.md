# A central involution forces an injective quotient pair map

Written AI-derived argument, unreviewed; no general tensor-degeneration or
exponent conclusion. This concerns precisely the three-set, integer vertex
potential construction accepted by the pinned `group_exact.py`.

Let z be a central involution in a finite group G. Suppose sets S,T,U have
injective cyclic pair maps S^-1 T, T^-1 U, U^-1 S, and integer vertex
potentials make every unwanted supported group term strictly positive.

**Claim.** If S contains s0 and s1=z*s0, then

    T x U -> G/<z>,   (t,u) |-> [t^-1*u]

is injective. Consequently |T|*|U| <= |G|/2. The claim and consequence hold
cyclically for the other two sets.

Proof. An ordinary collision in G contradicts the given pair-map injectivity.
The only remaining possible collision in the quotient has

    t0^-1*u0 = z*t1^-1*u1,
    t1*t0^-1 = z*u1*u0^-1.

The following two cyclic triples of group labels both multiply to identity:

    (s0^-1*t0, t1^-1*u1, u0^-1*s1),
    (s1^-1*t1, t0^-1*u0, u1^-1*s0).

For the first, use t0*t1^-1=z*u0*u1^-1 and s1=z*s0. For the second use
the displayed equation directly. Centrality and z squared = 1 justify the
cancellations. Both terms are unwanted since their two S vertices differ.

If the S,T,U potentials are alpha,beta,gamma, their weights are respectively

    alpha(s0)-alpha(s1)+beta(t1)-beta(t0)+gamma(u0)-gamma(u1),
    alpha(s1)-alpha(s0)+beta(t0)-beta(t1)+gamma(u1)-gamma(u0).

These are negatives, so they cannot both be strictly positive. This proves
injectivity in the quotient and hence the counting bound.

For SL(2,7), z=-I and |G|/2=168. In shape (16,16,17), every product of the
other two set sizes is at least 256. Therefore none of S,T,U may contain
both g and z*g. These 504 binary clauses are sound consequences of the
intended witness conditions, added to the search independently of the
solver's general commuting-trade clauses. No completeness claim is inferred
from a time limit.

The argument also applies to the concurrent SL(2,5) target (10,10,10), since
100>60, but no other worker's files or runs are changed here.
