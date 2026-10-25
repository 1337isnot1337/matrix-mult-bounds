# Sharp invertible quadratic dimension four outside characteristic two

October25, 2026. Claim `AI-ODD-QUADRATIC-SHARP-FOUR-001` is
**proof-written-unreviewed**. Exact integer certificates and a separate
same-session algebra audit corroborate this proof; neither is independent
review or formalization. No historical priority or exponent gain is claimed.

## Statement and source convention

Let K be any field of characteristic different from two, including zero.
For M in Mat3(K), retain the full fifteen-by-fifteen source

    R(M)[(j,L),(H,r)]=M[H-j,L-r],
    0<=j,r<=2, 0<=L,H<=4,

with out-of-range entries zero and both pair orders lexicographic. Among
K-linear coefficient families on which detR vanishes geometrically and
detM is not identically zero, the maximum dimension is **four**. The
following family attains it over K itself:

    W={M(t,b,c,f)=[[8t,b,c],[0,4t,f],[0,0,t]] : t,b,c,f in K}.

The existing cap-four proof in characteristic different from two and three,
and its characteristic-three continuation, supply the upper bound. Their
exact proof and dependency records are pinned in sources.json; their
hypotheses are precisely geometric source rank at most14 and coefficient
determinant not identically zero. The construction below supplies sharpness.

## Four independent coefficient directions

The entries M22,M01,M02,M12 recover t,b,c,f respectively, so the family is
four-dimensional over every K. Its determinant is 32t^3. When two is
invertible, coefficient invertibility is exactly t!=0. In particular
(t,b,c,f)=(1,0,0,0) is an invertible coefficient point over the ground field;
no root extraction or field extension is needed.

## Polynomial source kernel

With zero-based source column indices0,...,14, put

    v5=t^3, v7=-4t^3, v8=-f*t^2, v9=8t^3,
    v10=(-b+8f)*t^2, v11=-c*t^2+f^2*t,
    v12=(8b-32f)*t^2,
    v13=2bft+8ct^2-12f^2t, v14=2cft-f^3,

and set all other coordinates to zero. Direct multiplication in
Z[t,b,c,f] gives R(M)v=0. The coordinate v5 has coefficient one, so v is
nonzero over K(t,b,c,f) for every field K. Thus detR=0 in this fraction
field and hence as a polynomial in K[t,b,c,f]. It stays zero after scalar
extension, proving the geometric rank cap, including t=0 specializations
where this particular kernel may vanish. This argument is a polynomial
identity, not a finite-point census.

## Uniform exact rank fourteen

Delete source row11=(j,L)=(2,1) and column5=(H,r)=(1,2), keeping natural
order on the remaining rows and columns. Exact integer determinant
expansion gives

    det R_minor=-262144*t^14=-2^18*t^14.

Here is a short hand calculation of the minor. Give row (j,L) weight
j+L and column (H,r) weight H+r. An upper-triangular coefficient entry
requires H-j<=L-r, so a nonzero source entry has column weight at most
row weight. Sort the retained rows and columns by increasing weight,
keeping their original order within a weight. The minor is block lower
triangular with block sizes1,2,3,2,3,2,1. At equal weights H-j=L-r,
only the three diagonal coefficients8t,4t,t occur. After removing a
factor t from each row, the seven blocks, by rows, are

    [8]; [[8,4],[0,8]]; [[8,4,1],[0,8,4],[0,0,8]];
    [[1,0],[4,1]]; [[1,0,0],[4,1,0],[8,4,1]];
    [[1,0],[4,1]]; [1].

Their determinants are8,64,512,1,1,1,1. The row sorting permutation has
sign+1 and the column sorting permutation sign-1, giving -2^18*t^14
in the original order. All free parameters lie below these diagonal
blocks. The verifier also computes the whole literal minor directly;
a separate pair-indexed regression reconstructs it. Therefore rankR is
exactly14 at every coefficient-invertible point over every field of
characteristic different from two. At (1,0,0,0) the minor is -2^18. Its
only exceptional residue characteristic is two, already excluded by the
coefficient-invertibility hypothesis of this construction.

As an additional integer cross-check, the pinned determinant invariants
satisfy D=32t^3, A2=16t^2, T4=64t^4. With e=4t, ell=2t one gets
T4=D*ell and D=(e+2ell)(A2-e*ell-ell^2), so the pinned P12 is zero.
The kernel and minor above prove the new construction without relying on
an evaluation of the factor formula at finitely many points.

## Scope, discovery and remaining questions

Together with the separate characteristic-two sharp-three proof, the
maximum invertible-family dimension is now three in characteristic two
and four in every other characteristic. All these claims retain written,
unreviewed status. The singular six-dimensional families remain possible.
The PR230 universal three-plane remains inclusion maximal: this new
upper-triangular four-space does not contain it, since its nonzero
bottom-middle direction is absent here. In characteristic two our
coefficient determinant vanishes identically, so this witness does not
contradict the sharp-three result for the invertible stratum.

Discovery used the odd-characteristic linear form m=e+2T4/D and its
singular evaluation-kernel section. In a triangular candidate with
M00=t,m=t, the diagonal equations admit e=t/2,i=t/8, with b,c,f free.
Replacing t by8t gives the integral family. No exclusion of all odd
four-spaces survives this explicit witness. An earlier scratch assertion
that the mixed-compression container [[a,b,c],[0,e,0],[0,h,0]] has T4=0
failed exact replay: T4=a*c*h^2. It was corrected before this package;
that failed route is not a premise of the construction.

The same-session auditor independently rebuilt the literal source and
checked a different minor at (1,-2,-2,-2): deletion of row11 and column14
gives +2^22. This is separate computation within the generating session,
not independent mathematical review. Discovery and audit files are pinned
for provenance, not required at runtime. Classification of all attaining
families and compatible three-leg tensor maps remain open. This one-block
result supplies no matrix-multiplication exponent improvement.
