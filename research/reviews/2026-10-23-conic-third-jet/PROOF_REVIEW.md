# Internal proof audit: third-order lift on the mixed conic chart

**Target:** PR [#107](https://github.com/1337isnot1337/matrix-mult-bounds/pull/107),
head `86b514225414662933f88c6ed8270250b40a287d`.

**Source pins:** `proof.md` blob
`9f9fc2dc5eded3f92e8b320f55add4f1f6c52ac1`; rational verifier blob
`3d04824d5e2f9a97254cb4313247c51f35c75bf6`; symbolic verifier blob
`159858540e4c07bfbdc5008d4f9ce78d2c423923`; family data blob
`ba907b50a98696f09118dd2af5f5c908c30c6ed0`. The target commit is the
source for every path and result cited below.

**Conclusion:** I found no gap in the stated mixed-chart incidence-jet claim:
for each complex `a,b,d` with `d != 0` and `c=-d^3`, the exported matrices
give a rank-twelve third-order incidence jet with the prescribed constant and
first coefficients. The audit checks the coefficient identity and the
rank-to-incidence implication. It does not review PR101's underlying tangent
calculation, establish a curve beyond order three, or construct the full matrix
target. This is an internal Codex audit; the claim remains proof-written and
unreviewed pending independent mathematical review.

## Coefficient identity and rank implication

The source has dimensions `112 x 112 x 112`, indexed by
`index(u,v,z)=28u+7v+z`. Its 4096 coefficient-one terms are the Cartesian
product over the six indices in `{0,1,2,3}` given in `proof.md`. For sparse
`14 x 112` maps `B_i,C_j`, contracting the last two legs gives a
`112 x 196` matrix `T(-,B_i,C_j)`. The rational verifier rebuilds those terms
and places each coefficient at flattened output column `14*r+s`; its loop
over a source term and matching entries of `B_i,C_j` implements that
contraction.

Write
\[
F(t)=T(-,B(t),C(t))=\sum_{k=0}^3 t^kF_k\pmod {t^4},
\qquad W_k=F_k[A,:],
\]
where `A` is the specified set of twelve first-source coordinates and `K` is
its 100-coordinate complement. The checked equations are
\[
F_0[K,:]=0,\qquad
F_k[K,:]=\sum_{i=1}^kY_iW_{k-i}\quad(1\le k\le3).
\]
They imply `F(t)[K,:]=Y(t)F(t)[A,:]` modulo `t^4` for
`Y(t)=tY_1+t^2Y_2+t^3Y_3`. The selected `12 x 12` minor of `W_0` is the
constant `-1`, so the twelve rows in `A` remain independent over the
truncated coefficient ring. The equations therefore put every other row in
their span and give rank exactly twelve. The verifier checks all 100 by 196
entries at each positive order, so this step does not rely on the discovery
system's reported rank or completeness.

## Uniform parameter range

The symbolic verifier reads only integer constants, `a,b,d`, and rational
arithmetic from the family data. After exact cancellation, it rejects any
coefficient whose denominator is not a rational constant times `d^k` for
`0 <= k <= 2`. Thus each coefficient specializes at every complex point with
`d != 0`. The three leading minors are checked as nonzero rational constants
(`1`, `1`, `-1`), so no additional generic-parameter exclusion is needed.

The verifier compares `B_0,B_1,C_0,C_1` to the pinned PR101 cubic-component
two-jet, checks the displayed second-coefficient correction, contracts the
literal source for orders zero through three, and verifies every moving-kernel
identity over `Q(a,b,d)`. The correction preserves the first derivative and
therefore the projective normal class `[1:d]`. These are sufficient exact
checks for the claimed chart result; the fixed-second-coefficient obstruction
and discovery-system dimension are not used as proof premises.

The local validation receipt and hosted CI on the target PR are separate
evidence. This audit did not re-run the symbolic verifier; it checked its
coefficient expansion, denominator guard, pivots, and incidence implication.
The report does not upgrade the claim to independently reviewed.

## Limits

The chart excludes `d=0`. A third-order incidence jet is not an all-order
formal curve or a degeneration of the full matrix-multiplication tensor. No
exponent improvement follows. PR101 remains the credited source for the
canonical tensor, cubic conic base, and prescribed first jet; no external
theorem or priority claim is added here.
