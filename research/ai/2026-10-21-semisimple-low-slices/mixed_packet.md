# Exact mixed maps for one punctured torus packet

October21,2026. AI-SL2-F8-MIXED-LOCAL-025. Written, unreviewed.
This constructs a local Laurent degeneration, not a joint target.

Use the first non-TPP cyclic-nine parent(A,B,C) whose unique extra relation
(a,b,c) has a of order9; its exact torus indices are(0,1,4). Index its full
input arrays by X_(s,t),Y_(t,u),Z_(u,s). Let A0,B0,C0 be the permutation
matrices for left translation by a,b,c. The selected group tensor is

    tr(X*Y*Z) + tr(A0*X*B0*Y*C0*Z).                       (1)

Indeed its group support has precisely the identity relation and the one
extra relation; this is checked with the actual504-element multiplication
table. All three pair maps are injective.

Put F=I+A0. Since A0^9=I,

    F^-1 = (I-A0+A0^2-...+A0^8)/2.                       (2)

The substitutions X=F*X', Z=Z'*F^-1 preserve both terms in(1): trace is
cyclic and F commutes with A0. This is a parent-tensor automorphism and
must not be counted as a new or larger multiplication packet.

Delete one point of the a-translation cycle. Let S be the eight retained
labels and alpha_i the decreasing path potentials from claim021. Set

    X'_(i,t)=epsilon^(alpha_i)*x_(i,t),     i in S,
    Z'_(u,j)=epsilon^(-alpha_j)*z_(u,j),    j in S,

and zero elsewhere. Leave Y unchanged. Composing with(2) gives explicit
9-by8 and8-by9 mixed maps. The backward map has denominator2; every
forward matrix column has two nonzero entries. All81 parent group basis
labels occur in each of the first and third source legs. Negative powers
are allowed in the input maps, as in a Laurent border degeneration.

The complete coefficient replay sums20736 integer numerator contributions.
Of these,9072 have negative exponent before cancellation. All such negative
terms cancel exactly. The surviving coefficients have numerator2 and
denominator2:648 intended matrix terms at exponent0 and567 extra terms
at exponent1. Thus the full selected source tensor equals

    T_matrix + epsilon*T_extra,

with no uninspected support or numerical cancellation. The report exports
the matrices, exponents and selected labels. The verifier accepts these
as data and rejects modified coefficients or exponents.

This supplies nonmonomial local maps with an exact Laurent identity.
It is equivalent to the earlier punctured packet under a parent symmetry;
it does not increase its volume or address cross terms between packets.
Applying different maps to several overlapping parents does not by itself
produce a simultaneous source degeneration. In particular the missing
joint map in claim022 is still missing. The ordinary low-rank span
obstruction in claim024 shows that any successful joint map for that target
must be singular. General packetwise mixing and compatible cross-term
cancellation remain open.
