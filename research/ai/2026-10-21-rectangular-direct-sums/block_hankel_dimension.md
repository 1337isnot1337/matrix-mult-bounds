# A dimension bound at the first block-Hankel boundary

October 21, 2026. Written proof, unreviewed. No independent audit, novelty,
or improved matrix-multiplication exponent is claimed.

Let H=(F_(i+j)) have L block rows, M block columns, and p-by-q blocks.
Its sequence has length m=L+M-1. Suppose L<=M. Over C, the variety of
such sequences with rank(H)<=L has dimension at most

    max( L(p+q), q(L+M-1)+p-1, p(L+M-1)+q-1 if L=M ).                       (1)

The two terms account for state-space realizations and a boundary component
with a common one-dimensional output space. The second component cannot
simply be discarded by assuming a flat extension.

## 1. A finite change-of-coordinates cover

First suppose rank r<=L and r<M; choose a full-rank factorization H=UV, with r intermediate
coordinates. Write U_i (p-by-r) and V_j (r-by-q) for the blocks.
A homogeneous change of the binary long coordinates acts on H by invertible
scalar block row and column matrices; the explicit Pascal identity is the
one proved in `parity_structure_equality.md` in the anisotropic package.
In particular, the row space of V transforms by the degree-(M-1) binary
representation on its block index.

There is one of M fixed distinct affine shears for which
V_-=[V_0 ... V_(M-2)] has rank r. If not, for each shear the original
r-dimensional row space W of V contains a nonzero vector in

    span(((-lambda)^(M-1),...,(-lambda),1)) tensor C^q.

Choose a nonzero vector for each of the M distinct lambda values. They are
independent: a scalar Vandermonde dual functional on the block index isolates
each vector, regardless of its nonzero C^q factor. This would give dim W>=M,
contrary to r<M. Thus these M fixed charts cover the whole rank-r locus.
A finite cover adds no parameter to a dimension bound.

For completeness, if S_M(lambda) has entries
binom(M-1-i,j-i) lambda^(j-i) for j>=i, the transformed factor is
V S_M(lambda)^T. A row vector whose transformed first M-1 blocks vanish is
an output vector times the last row of S_M(-lambda)^T, exactly the displayed
coherent vector. This also checks the location of the deleted block.

## 2. Factorization and the exceptional component

Work in a chart with V_- of full row rank. Let V_+=[V_1 ... V_(M-1)], and
let U_-,U_+ stack the first and last L-1 block rows. The Hankel identities give

    U_+ V_- = U_- V_+.

Choose a right inverse R of V_- and set A=V_+ R. Then U_+=U_- A, so
U_i=C A^i with C=U_0. The complete observability stack has rank r because U
does. Its rank increments are nonincreasing: multiplication by A surjects
from each successive row-space quotient onto the next. Therefore, if U_-
is not full rank, all L increments are positive. Since r<=L, this forces
r=L and every increment to equal one. In particular rank(C)=1.
Write C=c w. Every block F_(i+j)=c w A^i V_j then has the same output line.
All such sequences have dimension q m+p-1, by their direct parametrization
as c tensor an arbitrary length-m sequence of q-vectors.

Otherwise U_- has full column rank, and the same Hankel identities force
V_+=A V_-. Consequently V_j=A^j B and

    F_k=C A^k B, 0<=k<m.

For fixed r, the parameter space (A,B,C) has dimension r^2+rq+pr.
Each minimal realization has an r^2-dimensional change-of-state orbit in
its fiber. This action is free: a state change fixing A and C fixes every
C A^i, whose stack has rank r. The fiber dimension theorem therefore bounds
the image dimension by r(p+q). This suffices for an upper bound; uniqueness
of every finite realization is unnecessary.

For r<L the exceptional case cannot occur. Taking the finite union over
r<=L and over the fixed shears proves (1) when L<M, including zero. Changes of
long coordinates preserve the common-output property and variety dimension.

## 3. The square boundary L=M

Only r=L=M needs another case. Use M+1 distinct fixed shear parameters.
If none makes V_- full rank, W contains nonzero vectors w_j tensor v_j
for all M+1 coherent block vectors w_j. The first M of these form a basis
of W. Expand w_(M+1) in the basis w_1,...,w_M. Every coefficient is nonzero
by Vandermonde interpolation at distinct points. Comparing tensor components
in the expansion of w_(M+1) tensor v_(M+1) forces all v_j to be proportional.
Therefore W=Sym^(M-1)(C^2) tensor span(v), so every F_k has a common input
line. These sequences have dimension p m+q-1. Otherwise a good shear exists
and Section 2 applies unchanged. The finite M+1-chart cover together with
this common-input component proves (1) also at L=M.

For the source crossed flattening, p=b, q=a, L=a, M=b. In particular,
A(9,9)'s crossed rank-at-most-nine variety has dimension at most162.
The input/output exceptional families have dimension161 and must still be
included in the proof.

## 4. The A(8,9) application

The crossed flattening T_F has L=8, M=9, p=9, q=8, so (1) is 136.
Suppose ordinary maps produce M30 plus M3. Its large-block dual space is
900-dimensional, and its rank-at-most-three parameter variety has dimension
3(30+30-3)=171. The lift is injective by target concision.

The source rank upper bound on that parameter variety is576. If the generic
symbol rank were at most seven, projection saturation and the exact A89
Hankel cap would put the whole large block into dimension at most504,
contrary to900. Thus the generic symbol rank is eight. The crossed-equality
lemma then places a dense open set, hence the whole rank-at-most-three
variety, in crossed rank at most eight. The crossed flattening itself is an
injective linear rearrangement of the source coefficients. An injective image
of dimension171 cannot fit into the variety of dimension at most136.
This excludes that particular ordinary target.

The same comparison supplies a necessary screen for other rectangular blocks:
use the determinantal dimension k(u+v-k), the exact lifted-rank upper bound,
and a verified lower-symbol-rank exclusion before applying (1). It must not
be used when the lifted bound exceeds a^2 b. The leading A(8,10) candidate
has upper641 rather than640 and is not excluded by this argument.

## Sources and limits

This proof uses the maintained coefficient-map and Pascal identities and
standard rank factorizations, observability quotients, and fiber dimensions.
Feldmann and Heinig, *Vandermonde factorization and canonical representations
of block Hankel matrices* (1996), warns that scalar factorization statements
do not transfer unrestrictedly to larger blocks:
https://doi.org/10.1016/0024-3795(95)00501-3 . Only its abstract was inspected;
no theorem from the inaccessible full article is imported here. The argument
above explicitly handles its boundary exception rather than assuming a
Vandermonde factorization. It does not cover rank thresholds greater than min(L,M),
singular tensor degenerations, or construct any exponent-improving maps.
