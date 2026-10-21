# Rank strata and an exceptional mixed graph

Written proof, unreviewed, October 21, 2026. Claim
`AI-MIXED-TWO-COORDINATE-STRATA-093`. Work over C with the canonical A4
leading flags, partner a=b=1, full B seven-frame, and a C five-space
containing m+t*d0+h*d1. The two parameters t,h are arbitrary complex
constants. The boundary four-space inside C is arbitrary. They are not
the formal parameter of a degeneration, which is denoted epsilon below.

The complete necessary normal dimension is32 except at (t,h)=(0,0),
where it is36, and (t,h)=(1,1), where it is34. A polynomial88-by32 frame
is complete away from these two points. At the second point, the full
34-dimensional normal system, including directions missed by specializing
that frame, reduces to the four common-plane motions. The shifted
induction excludes M(10,10,11) at this exceptional graph. The pure-row
origin is already covered by claim089. Target exclusion for the whole
two-coordinate chart is not established here.

## 1. Actual mixed-row equations

Adopt the full-B normal kernel of dimension88, its virtual C correction,
and the sixteen adapted low-rank source slices from claim088. As in
claims090/091, every row of their stacked obstruction Z annihilates the
actual C five-space. Write its seven column blocks as Z0,...,Z6, each
with312 rows and88 normal parameters. The mixed-row constraints are

    M(t,h) = Z6+t*Z0+h*Z1,            M(t,h)*normal=0.

This is the actual row m+t*d0+h*d1; no pure-row containment is imposed.
The maintained verifier reconstructs all seven blocks from the source
tensor. M is a polynomial312-by88 matrix over Q[t,h]. The four plane
directions are in its kernel and annihilate the full virtual tensor.

## 2. Complete rank stratification

The saved polynomial matrix N has88 rows,32 columns and degree at most4.
The exact identity M*N=0 is checked in Q[t,h]. Its specialization at
(1,2) has rank32. Thus M has rank at most56 over Q(t,h). Every57-minor
of M is consequently the zero polynomial, so this upper bound holds at
every complex pair, not just generically.

A saved56-minor is exactly

    t^10*(h-1)^2*(h+t)^4*(t-h^2)^4.                    (1)

Outside its zero set the rank is56. Its zero set consists of four curves.
The following additional56-minors cover their generic points:

| Curve | Parameter | Exact minor |
| --- | --- | --- |
| h=1 | t | t^10*(t-1)^6*(t+1)^2 |
| h=-t | t | -4*t^16*(t^2+3)^2 |
| t=h^2 | h | -4*h^30*(h-1)^4 |
| t=0 | h | 4*h^12 |

Every root of every displayed univariate polynomial is retained. The
remaining controls are t=-1,0,1 on h=1; t=0,+i*sqrt(3),-i*sqrt(3) on
h=-t; h=0,1 on the parabola; and h=0 on t=0. Exact minors give rank56
at each of these points except the origin and (1,1). Complete exact
row reductions give ranks52 and54 at those two points respectively.
Algebraic controls use the exact number field, including the two
nonreal roots. The verifier checks that the root lists factor each
univariate polynomial completely, rather than checking only real roots.

Together with the global upper bound this proves

    dim ker M = 36 at (0,0), 34 at (1,1), and32 elsewhere.

## 3. A polynomial frame with a precise specialization boundary

N contains the four plane motions through an explicitly checked constant
32-by4 embedding. For each56-minor above, a matched32-minor of N equals
that minor times a nonzero rational constant. The constant has absolute
value6164217593856; its sign is stored and checked separately for each
minor. At the finitely many residual points of rank56, N is also checked
to have rank32. These identities show that N is a complete normal frame
at every pair except the two rank-jump points.

At the origin N has rank28, and at (1,1) it has rank30. Specializing the
generic frame therefore misses respectively eight and four dimensions
of the actual normal kernels. Neither special fiber is analyzed by
assuming that a generic kernel basis remains complete there. The next
section recomputes the complete34-dimensional kernel at (1,1).

Singular polynomial syzygies suggested N. Its acceptance uses only the
maintained SymPy dependencies: polynomial identities, exact determinants
and complete finite field-extension calculations. No assertion about
Singular's module-generation algorithm is needed for the proof.

## 4. Split the exceptional target conditions into two families

At (1,1), remove the four plane directions from the complete34-dimensional
kernel by a constant complement. Let d have the remaining30 coordinates.
Apply the actual mixed-row shear to both the obstruction and the virtual
third tensor. Its mixed column vanishes. The joint row basis S(d) has
56 rows and six boundary columns (E0,O0,E1,O1,E2,O2). Since its rows
annihilate the C five-space, rank S(d)<=2.

Project these columns by

    Q(d) = (O0-E0,O1-E1,O2-E2).

Ten row combinations W of S lie in the kernel of this column projection.
Their coefficient kernel has dimension16. Hence

    rank S(d) >= rank Q(d)+rank W(d).

If W=0, d belongs to this16-dimensional linear family. If W!=0, rank S<=2
forces rank Q<=1. Repeated triangular two-minors of Q have determinants
equal to nonzero rational multiples of squares of linear forms in d.
Setting those forms to zero gives complete successive kernel dimensions

    30 -> 18 -> 16 -> 12 -> 10 -> 8 -> 6.

Every diagonal identity, triangular zero, determinant ratio and complete
linear kernel is replayed. Thus the second case belongs to a specified
six-dimensional linear family. The projection need not vanish there;
its coefficient rank is six. No stronger projection claim is used.

## 5. Eliminate both families with the full target conditions

For each family, reconstruct the virtual third tensor in the same adapted
64-source basis used in claim090. Modulo rows already known to annihilate
the C five-space, the listed additional source slices have either support
covered by at most two B/C vertices or joint B rank at most two. The
prior saturated target rank gap forces each such projected slice to
vanish on C. These give further mixed-row equations and obstruction rows.

For the16-dimensional stable family, the first added source positions are

    16,17,18,19,24,25,26,27,28,29,30,31.

The mixed-row equations reduce16 to8. Triangular cubic minors of the
extended obstruction then reduce8->6->4->2. Source positions22,23 become
available, and further cubic minors reduce2 to0.

For the six-dimensional projection family, source positions22,23,28,29
become available first, then30,31. Their mixed-row equations reduce6 to4,
and cubic minors reduce4 to0.

These are zero-based positions in the fixed adapted source basis, not
indices of raw tensor coordinates; the certificate stores both. Each
rank bound is checked on the reconstructed residual source slice. The
cubic witnesses are actual triangular minors with three repeated linear
diagonal forms and nonzero rational scales. Rank at most two forces the
forms to vanish over C. No numerical approximation or generic parameter
specialization enters either terminal elimination.

The resulting complete dimensions, after restoring the four planes, end
at4 in both cases. This covers every boundary four-space in the C
five-space containing m+d0+d1.

## 6. All-order implication and remaining question

Adopt the shifted moving-plane induction of the cited third-boundary and
mixed-five-space proofs. If the first normal error from moving boundary
modules is at epsilon^N and the first new output orders are s_B,s_C,
the off-diagonal corrections appear at N+s_B and N+s_C. Corrected earlier
residues lie in the old cross and cancel in W0. The double-new-output
residue at N+s_B+s_C is precisely the virtual tensor used above. Higher
source corrections and boundary terms have zero double projection there.

The normal result forces a common-plane error at each step. Absorb it
into the moving plane and increase N. Both output maps stay in rank56
boundary modules over C((epsilon)), so cannot reach the two110-dimensional
target legs. This excludes the exceptional graph for arbitrary higher
maps, delayed unequal growth, and a Laurent map on the first leg under
the stated canonical leading normalization.

The rank stratification and frame cover the whole two-coordinate chart;
the new target exclusion covers only (1,1). The origin and previously
closed axes retain their earlier proofs. The generic target incidence,
other graph charts and partner strata remain open. This is not a matrix
multiplication algorithm or an exponent improvement, and the written
proof has no independent mathematical review.
