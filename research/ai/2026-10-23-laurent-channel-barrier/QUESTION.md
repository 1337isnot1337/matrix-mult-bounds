# Can Laurent cancellation escape a low channel-rank paired source?

October 23, 2026. Owner-directed research continuation on
`research/laurent-stencil-20261023-ab94`, based on main `bd03b9d`.

The ordinary-map arguments in PR157, PR173 and PR179 explicitly leave
singular Laurent cancellation open. Their common input is a subspace of
first-leg contractions on which the complete channel-polynomial matrix
has rank smaller than the target middle width.

The question is whether an arbitrary auxiliary tensor with small first
flattening rank can cancel poles and remove this obstruction. The
intended output is an all-order formal lemma, its precise near-full
paired-source application, and exact controls that retain pole terms.

The proposed mechanism takes a common kernel of the auxiliary image and
the excluded source slices over the Laurent field. A nonzero vector in
that kernel can be scaled to have a nonzero regular leading vector. The
total degeneration then makes its source contraction regular, so the
channel-rank equations can safely specialize. The argument must not
specialize the raw constant coefficient of a tensor that still has poles.

This is distinct from the predecessors' ordinary residual bounds. Their
source formulas, good-slice counts and channel factorizations retain
credit. The intended result is scoped to a uniform low channel-rank
factorization over the Laurent field. General full-profile maps and a
construction of a better matrix multiplication exponent remain open.

After this question, the constructive direction is a full-rank periodic
or nonlocal encoding outside those hypotheses. No finite numerical fit
will be treated as an exact tensor identity.
