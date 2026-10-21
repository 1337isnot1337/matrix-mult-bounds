# An exact flatness gate for finite block-Hankel realizations

October 21, 2026. Written proof, unreviewed. This is a standard
finite-realization mechanism written explicitly for our conventions,
not a new general realization theorem or an exponent improvement.

Let M_0,...,M_(r+c-2) be d-by-e complex matrices and H_(r,c) their
block-Hankel matrix. If

    rank H_(r,c) = rank H_(r-1,c-1) = n,                 (1)

then there are C of size d-by-n, A of size n-by-n, and B of size n-by-e
with M_k=C A^k B for every supplied moment.

Factor H=OR minimally. Write O in block rows O_p and R in block columns
R_q. Inner flatness says O_low (p<r-1) has full column rank and R_low
(q<c-1) has full row rank. The Hankel equalities say

    O_shift R_low = O_low R_shift.

Choose a right inverse of R_low, define A=R_shift R_low^right, and obtain
O_shift=O_low A. Substitute this equality back and cancel the full-column
rank O_low to obtain R_shift=A R_low. Induction gives O_p=O_0 A^p and
R_q=A^q R_0, proving the assertion including the last moment.

The implementation chooses nonsingular minor indices inside the inner
block, constructs a rational factorization, and verifies every supplied
moment exactly. It never reports realization from rank alone. A failed
test means only that this sufficient test did not apply.

For the A(8,10) crossed matrix, take d=10,e=8,r=8,c=10 and
M_k[s,i]=F_(i,k,s). Three controls are included:

- A fully observed noncyclic nine-state sequence passes and all 17 moments
  are reconstructed exactly.
- F_(0,0,0)=F_(1,7,1)=1 has a genuine J_8 direct-sum J_1 realization,
  but inner rank 8 versus full rank 9. Thus failing the gate does not
  exclude a nine-state representation.
- F_(0,8,0)=1 has inner rank 7 versus full rank 8 and needs at least nine
  states by the moment-Hankel counterexample in outer_compression.md.

## What remains missing

The crossed-rank-nine critical stratum is not classified by (1).
For a minimal n-state representation, output rank at least three and
n<=9 ensure an observability index at most seven: before stabilization,
each observation step increases dimension by at least one, starting at
least three. The same argument applies to controllability. Consequently,
a minimal realization with n<=9 and both outer coefficient flattenings
of rank at least three satisfies this inner-flatness gate.

This observation has only one direction. It does not establish that
failure of flatness forces an outer compression, since it assumes the
small realization in the first place. Using it to manufacture that
realization would be circular. A proof of that missing alternative, or
an explicit counterexample to it, remains a concrete next problem.

Background consulted (not used as an unproved extra premise): classical
partial-realization literature, including Sontag, *Mathematical Control
Theory*, second edition, section 6.6, author-hosted text:
https://www.sontaglab.org/FTPDIR/sontag_mathematical_control_theory_springer98.pdf
The short sufficient-criterion proof above is self-contained.

### Subsequent same-day development

`generic_flatness.md` now gives a written, unreviewed graded-module proof of the missing generic-chart alternative for crossed rank at most nine. The earlier warning against assuming realization from a single rank remains valid; the new argument uses both outer ranks and a coordinate change. Finite-state critical strata still require analysis.
