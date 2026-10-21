# Mixed hyperplanes recover the complete seven-frame normal equations

Written proof, unreviewed, October 21, 2026. The matrix-multiplication
exponent remains 9/4.

At the canonical four-row flags, suppose both first mixed projections
are rank-one partner lines and both effective first dimensions are at
least six. Arbitrary complex first subspaces, boundary graph lifts,
higher regular output maps, delayed unequal first orders, and a Laurent
first map are allowed. These data cannot yield M(10,10,11).

The key statement applies to either output leg independently: its six
first equations, with a nonzero mixed projection, imply its complete
maximal seven-frame normal equations. Applying it on both legs leaves
only the four common-plane directions. The ordinary first-rank sum when
both mixed projections are nonzero is at most twelve; its remaining
rank-one frontier consists of seven-by-five pairs in either order.
These are necessary local restrictions, not a smaller exponent.

## 1. Every compatible first space lies in its maximal frame

Adopt the complete partner classification. On the chart v3 nonzero,
normalize the two mixed lines as

    v=(a*b,b,a,1),       u=(a*b,-a,-b,1).

Their maximal compatible quotient frames W_B,W_C have dimension seven.
In the maintained bases each consists of six boundary vectors followed
by one mixed vector. The pure mixed product H(m_B(u),m_C(v)) is zero.
For arbitrary graph lifts, compatibility therefore gives

    H(beta,m_C(v))+H(m_B(u),gamma)=0.

The two summands have disjoint source supports, so each vanishes. Thus
beta and gamma belong to the respective full six-dimensional boundary
annihilators. The pure-boundary parts of the first spaces belong to those
annihilators as well. Consequently every compatible first space with these
partner lines, even a nonmaximal one, is contained in W_B or W_C.

If an effective first dimension is at least six, choose a six-dimensional
subspace V of it with nonzero mixed projection. It is a hyperplane of the
corresponding maximal frame and is not its pure-boundary hyperplane.
All boundary graphs of V are included by this reduction.

## 2. An unconditioned obstruction lemma on all 228 normal parameters

Use the canonical first normal equations, whose solution space has
dimension 228. For one leg, let

    Psi_D: W_B -> Q_B,       dim Q_B=200,

be its off-diagonal correction obstruction. It is a 200-by-7 matrix,
linear in the normal parameter D. No equations on the opposite leg are
imposed in this section. The actual first-space equations say
Psi_D(V)=0, so rank Psi_D is at most one.

We prove, uniformly over all partner lines,

    rank Psi_D<=1  implies  Psi_D vanishes on the six boundary vectors.
                                                               (1)

The entries of Psi_D are linear forms in the 228 normal parameters,
with coefficients in Q[a,b]. The report records two-by-two triangular
submatrices whose diagonal entries are nonzero rational multiples of
one linear form L. Each determinant is c*L^2, with c a nonzero constant.
Under rank at most one, L must vanish at every complex a,b. In particular,
no factor depending on a or b is divided away.

The complete chart has these three rounds:

| Parameters before | Independent forced forms | Parameters after | Recorded minors |
| --- | --- | --- | --- |
| 228 | 96 | 132 | 140 |
| 132 | 24 | 108 | 46 |
| 108 | 2 | 106 | 4 |

After each round, the verifier constructs a complete polynomial kernel.
A fixed nonzero minor becomes identity plus a strictly triangular
polynomial matrix after multiplication by a constant invertible matrix.
Backward substitution gives the kernel, with a fixed identity block in
its free coordinates; the full matrix-kernel product is zero identically.
These checks establish both the constant rank and the completeness of
the substitution at every a,b. No complex solution is lost at a special
parameter value.

After the last round, all six boundary columns of Psi_D vanish
identically. Only its seventh, mixed column can be nonzero. This proves
(1) on the entire chart.

For the endpoint v=e1, three exact rounds force ranks 98,22,2 and again
leave 106 parameters supported only in column seven. Source reversal
covers the v0 nonzero chart and the remaining endpoint e2. The preceding
frame package verifies that these charts exhaust all nonzero rank-one
mixed lines. Exchanging output legs and transposing short indices is
also an exact source automorphism, so the same assertion applies to C.

Nonzero rank-one matrices supported on column seven actually occur.
Thus (1) is a support statement, not a minimum-nonzero-rank-two assertion.
The report retains exact countercontrols to that stronger, false assertion.

## 3. The mixed component kills the remaining column

The hyperplane V contains a vector z whose seventh coordinate z7 is
nonzero. After (1),

    0=Psi_D(z)=z7 * (seventh column of Psi_D).

Hence the last column is zero as well. All seven equations on this leg
hold, independently of the first space or correction equations on the
other leg. The complete one-leg seven-frame system has a uniform
88-dimensional kernel, also certified in the report by a fixed rank-140
minor and a complete polynomial kernel.

Apply the same argument to the other leg. Both complete seven-frame
systems now hold. The adopted uniform seven-frame theorem says their
common kernel consists exactly of the four common-plane directions.
This handles arbitrary six-by-six first spaces, as well as six-by-seven,
seven-by-six and seven-by-seven, without replacing them by coordinate
hyperplanes.

## 4. All orders and the first-rank bound

Use the delayed compatibility and moving-boundary induction spelled out
in the seven-frame proof. At each first normal error order N, the actual
B and C first spaces give the shifted off-diagonal equations at N+s_B
and N+s_C. These precede the first possible double-new-output error
order N+s_B+s_C. The rank-eight old cross forces the required source
corrections into W0.

Sections 1-3 apply to this normal error and force common-plane motion.
Absorb that motion into the formal polynomial plane and iterate. Although
the actual first spaces may have dimension six, the implication to their
virtual seventh equations is used only to identify the normal kernel;
no extra output row or unproved tensor correction is inserted.

Both output maps remain in rank-56 moving boundary spaces over C((t)).
The target is concise on 110 coordinates of each output leg. Neither a
Laurent first map nor a regular limit can raise these output flattening
ranks to 110. This contradiction proves the all-order exclusion.

For ordinary derivatives with both mixed projections nonzero, the full
classification gives invertible lines of dimensions 1,1 or rank-one
partners with each effective dimension at most seven. In the rank-one
case at least one dimension must now be at most five. The total is at
most twelve, with only 7,5 or 5,7 remaining at that threshold. The separate
five-frame proof excludes the invertible-line stratum entirely.

## 5. Controls, attribution and remaining scope

The pure-boundary hyperplane has zero mixed projection, so Section 3
does not apply. On one leg it leaves 106 normal parameters, with eighteen
independent possible mixed-column coefficients and an 88-dimensional
complete-seven-frame kernel. Exact nonzero rank-one matrices in the report
show why the mixed hypothesis is needed.

The report additionally checks the more restricted case in which the
opposite seven-frame equations already hold. That leaves 88 parameters;
its rank-one minor rounds reduce them to sixteen, again supported only
on the mixed column. These compatible additional controls are not needed
to assume the opposite equations in Section 2.

A mixed five-dimensional C space at a=b=0, retaining maximal-frame
columns 1,3,4,5,6 (zero-based), has twelve normal directions even when the
B first space is the full seven-frame. Thus the first-equation conclusion
does not extend to all mixed five-spaces. This finite control is not a
higher lift or target. General seven-by-five pairs, smaller first spaces,
one-sided mixed projections, and other flags remain open.

Canonical correction maps, the complete partner/frame description,
triangular-minor discovery method and moving-plane induction retain their
earlier source credits. The new contribution is the unconditioned support
lemma (1), its complete polynomial witnesses and its arbitrary mixed-
hyperplane consequence. These are generating-session checks and written
research, with no independent review, formalization or exponent gain.
