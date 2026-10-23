# Explicit rational three-jet, with its finite scope

October 23, 2026. Written, unreviewed, owner-directed Codex work.

Let T be the canonical integer 112-cubed tensor with coordinates
index(u,v,z)=28u+7v+z and the following 4096 coefficient-one terms:

    (index(i,s,6-p-q), index(p,j,6-r-s), index(r,q,6-i-j)),
    for i,j,p,q,r,s in {0,1,2,3}.

This is the credited source of PR101 and its predecessors. Let A0 be the
twelve first-source coordinates index(i,j,z) with i,j in {1,2} and
z in {0,3,6}; let K contain the other 100 first-source coordinates.

The exported witness specifies rational matrices B_i,C_i of size
14-by-112 for 0<=i<=3, and Y_i of size 100-by-12 for 1<=i<=3.
Write F_k=sum_{i+j=k} T(-,B_i,C_j), with each F_k flattened into
112-by-196, and W_k=F_k[A0,:]. Independent exact replay verifies

    F_0[K,:]=0,
    rank(B_0)=rank(C_0)=14,  rank(W_0)=12,
    F_k[K,:]=sum_{i=1}^k Y_i W_{k-i},  k=1,2,3.       (1)

All 100*196 coefficients of each equality are checked. Over Q[t]/(t^4),
equation (1) expresses the remaining source rows in the span of the
twelve rows W(t). The leading ranks give unit minors, so this is a
rank-twelve incidence three-jet with two rank-fourteen maps. Extension
of scalars gives the same three-jet over C.

The constant and first coefficients are the specialization of PR101's
cubic-component witness at a=1,b=2,d=1,c=-d^3=-1. Both a-c=2 and b+c=1
are nonzero, so the point is outside the two already-integrable linear
components. The first derivative contains 128 nonzero entries outside
the short boundary planes. The second and third coefficients are new.
Their numbers of nonzero entries are (38,32) and (88,68) for (B,C).
The source corrections Y_1 and Y_2 vanish; Y_3 has 32 nonzero entries.

Discovery first tested arbitrary third coefficients with the fixed old
second coefficient. Its complete reduced third system is inconsistent
in the second middle sector at this point. It then allowed all 70
second-coefficient tangent fields, producing a consistent exact
379-equation system of rank 50. With its free variables zero, only seven
tangent weights are nonzero. The corresponding corrected maps are
exported explicitly and accepted by (1); their acceptance does not
depend on completeness of the discovery operator or its reported rank.

The old fixed-jet obstruction and the numerical ranks of the discovery
systems are retained as discovery evidence, not as universal
nonexistence claims. The exported maps at this single rational point
are the positive result. The independent verifier rebuilds the literal
source, uses rational arithmetic, checks leading ranks, and checks (1)
without importing the discovery script or predecessor elimination.
Corruption controls alter a third map, a moving-kernel coefficient,
the leading rank and the parameter label.

No fourth coefficient is supplied. The chosen truncation has 520
nonzero entries in its fourth Schur coefficient, as a discovery control;
allowing fourth map coefficients and varying earlier choices remains
open. This is neither an all-order formal curve nor a full matrix-target
degeneration. There is no exponent improvement, independent
mathematical review, formalization or historical-priority claim.
