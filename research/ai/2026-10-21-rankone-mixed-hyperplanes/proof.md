# A mixed hyperplane already forces the full rank-one frame equations

Written proof, unreviewed, October 21, 2026. The matrix-multiplication
exponent remains 9/4.

At the canonical four-row flags, suppose both first mixed projections are
rank-one partner lines, one effective first space has dimension seven,
and the other has dimension at least six. Arbitrary complex subspaces,
boundary graph lifts, higher regular output maps, delayed unequal first
orders, and a Laurent first map are allowed. These data cannot yield the
100-by-110-by-110 matrix target.

The complete normal kernel is again only the four common-plane directions.
The new step is that six opposite first rows with a nonzero mixed
projection force all seven opposite normal equations. Consequently the
necessary ordinary first-rank sum with both mixed projections nonzero
is at most twelve. This is a local first-space constraint, not an exponent
improvement or a general degeneration exclusion.

## 1. Reduce the first spaces to a mixed hyperplane

Adopt the complete partner classification and maximal seven-frame
description. On the chart v3 nonzero, normalize the partner lines as

    v=(a*b,b,a,1),       u=(a*b,-a,-b,1).

Write W_B,W_C for the maximal compatible seven-dimensional quotient
spaces, in the preceding basis with six boundary vectors followed by
one mixed vector. The B first space is all of W_B. The C first space
contains a six-dimensional subspace V with nonzero mixed projection.
It lies in W_C: the full B boundary annihilator and its mixed row force
any C mixed graph term into the full six-dimensional C annihilator.
Thus V is a hyperplane of W_C and is not its pure-boundary hyperplane.
This includes all possible graph lifts of V.

Imposing the B off-diagonal equations on the canonical 228-dimensional
normal space leaves a uniform 88-dimensional space. On it, let

    Psi_D: W_C -> Q_C,       dim Q_C=200,

be the remaining correction obstruction, arranged as a 200-by-7 matrix.
The actual C equations say Psi_D(V)=0, hence rank Psi_D is at most one.
We will prove the stronger structural statement

    rank Psi_D<=1  implies  Psi_D vanishes on the six boundary vectors.
                                                               (1)

The assertion is not that every nonzero obstruction has rank at least
two. Nonzero rank-one obstructions supported on the seventh column exist
and are explicitly retained as controls.

## 2. Uniform polynomial kernels and repeated two-by-two minors

The 1400-by-228 B constraint matrix has rank 140 at every a,b. Its fixed
rank-140 minor at a=b=0 becomes identity plus a strictly triangular
polynomial matrix after a constant invertible row transformation. The
normalized off-diagonal part has 158 nonzero entries. Polynomial backward
substitution gives a complete 228-by-88 kernel with a fixed identity
minor. The verifier checks both the triangular determinant identity and
the entire matrix-kernel product over Q[a,b].

Restrict the C obstruction to this kernel. Its entries are linear forms
in the 88 normal parameters, with coefficients in Q[a,b]. The certificate
lists two-by-two triangular submatrices whose two diagonal entries are
nonzero rational multiples of the same linear form L. Their determinants
are c*L^2 with constant c nonzero. If rank Psi_D<=1, each L must vanish
over C, at every a,b. No parameter-dependent factor is divided away.

There are three rounds on this chart:

| Normal parameters before | Independent forced forms | Parameters after | Recorded minors |
| --- | --- | --- | --- |
| 88 | 56 | 32 | 112 |
| 32 | 14 | 18 | 28 |
| 18 | 2 | 16 | 4 |

After every round, a full polynomial kernel is verified using a fixed
nonzero minor and an identity free-coordinate block. Thus the substitution
retains every complex solution, including special values of a,b. After
the last round, all six boundary columns of Psi_D vanish identically;
only column seven can be nonzero. This proves (1) on the full chart.

The exceptional endpoint v=e1 is checked separately. Its B normal space
also has dimension 88; two rounds force ranks 56 and 16, leaving sixteen
parameters and only the seventh obstruction column. Source reversal covers
the v0 nonzero chart and the remaining endpoint e2. As in the preceding
package, these cases cover every nonzero complex rank-one mixed line.
The matrices and the polynomial kernel/minor witnesses are exported in
the complete report and recomputed from the canonical correction maps.

## 3. The mixed component kills the final column

Since V has a nonzero mixed projection, it contains some vector z whose
seventh coordinate z7 is nonzero. After (1),

    0=Psi_D(z)=z7 * (seventh column of Psi_D).

Therefore the last column vanishes too. All seven C equations hold,
so the preceding uniform seven-frame theorem gives exactly the four
common-plane directions. This argument handles every mixed hyperplane;
it does not replace arbitrary hyperplanes by coordinate deletions.

The same conclusion holds with the legs exchanged, by the exact source
automorphism exchanging output legs and transposing the short indices.

## 4. All orders and the new first-rank bound

Use the delayed compatibility and moving-boundary induction already
spelled out in the seven-frame proof. At each first normal error order N,
the actual B and C first frames give the shifted off-diagonal equations
at N+s_B and N+s_C. These precede the first possible double-new-output
error order N+s_B+s_C. The rank-eight old cross forces the necessary
source corrections in W0. Sections 1-3 apply to the same next normal
error and reduce it to common-plane motion. Absorb that motion into the
formal polynomial plane and continue.

Both regular output maps remain in rank-56 moving boundary spaces over
C((t)). The target is concise on 110 coordinates of each output leg,
which neither a Laurent first map nor a regular limit can supply from
these ranks. This is the required contradiction. The proof does not
need a further terminal third-block estimate.

For ordinary derivatives with both mixed projections nonzero, the complete
classification gives either invertible lines of dimensions 1,1 or rank-one
lines with individual effective dimensions at most seven. A sum above
twelve in the latter case would require dimensions 7,6 or 7,7 in some
order. Both are excluded here. Hence the sum is at most twelve.

## 5. Controls and limits

The pure-boundary hyperplane has zero mixed projection, so Section 3
does not apply. Its normal space has dimension sixteen; nonzero rank-one
obstructions supported on the mixed column show why that hypothesis is
needed. The report retains an exact such matrix for each chart case.

A mixed five-dimensional C space at a=b=0, obtained by retaining columns
1,3,4,5,6 of the maximal frame (zero-based), has a twelve-dimensional
normal space. It still has a mixed component. Thus the present argument
does not extend to all five-dimensional mixed spaces merely by repeating
its first-equation conclusion. This control is not a higher lift or a
matrix target. Seven-by-five and six-by-six first spaces remain open.

The partner/frame classification, canonical correction maps, triangular
minor-search method, and moving-plane induction retain their earlier
attribution. The new contribution is the uniform conditioned obstruction
structure (1) and its arbitrary mixed-hyperplane consequence. These are
generating-session exact checks and written research, with no independent
review, formalization, or improved exponent.
