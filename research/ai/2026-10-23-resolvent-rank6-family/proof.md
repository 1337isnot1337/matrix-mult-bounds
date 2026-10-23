# A sixteen-dimensional linear family of rank-six matrices

October 23, 2026. Written and unreviewed. This does not construct a tensor
degeneration or improve the matrix multiplication exponent.

Claim `AI-RESOLVENT-RANK6-FAMILY-001` refines, but does not classify, the
rank-six locus of the 112-dimensional fixed-resolvent space `W` from
`AI-RESOLVENT-SHARP-MINRANK-001`. Retain the source formulas, field
conventions, and attribution in the pinned predecessor package
`research/ai/2026-10-23-resolvent-minrank/`.

Let `e_(i,s)` be the coordinate vector in the 16-dimensional outer parameter
space, let `G(f)=K^-1 S(f)`, and put `Q(f)=G(e_(0,0))G(f)`. For each
`k=3,4,5,6` and `i=0,1,2,3`, let `X_(k,i)` be the element of `W` with the
single nonzero block `(3,k-3)` equal to `Q(e_(i,0))`. These sixteen matrices
are linearly independent: the four block positions use distinct parameters,
and within each block the four Q generators are among the independent
generators of the mixed 31-dimensional space. Their span `L_6` therefore has
dimension sixteen.

The outer factors reused in each block are

\[
Q(e_{(0,0)}),\quad Q(e_{(1,0)}),\quad
Q(e_{(2,0)}),\quad Q(e_{(3,0)})
\]

These four matrices are linearly independent over every field by the
predecessor's unit-pivot minor certificate. Each occurs as a block in `W` for
every one of the four specified `k` values.

Let `K=S(f_*)`, where `f_*[(i,s)]=1` exactly when `i+s=3`. The source
normalization gives `K G(e_(0,0))=S(e_(0,0))`; hence

\[
KQ(e_{(i,0)})=S(e_{(0,0)})G(e_{(i,0)}),\qquad 0\le i\le3.
\]

The exact integer reconstruction places each right-hand matrix on the same
six rows, with zero-based indices `{0,7,14,21,22,23}`. Left multiplication by
`K` preserves rank over every field because the predecessor verifier supplies
an integer inverse of `K`. Apply `K` on the output side of each of the four
outer blocks. Every linear combination in `L_6` then has image supported on
at most these six row coordinates, so its rank is at most six. If its
parameter vector is nonzero, block separation and the four-generator
independence make the full matrix nonzero. It belongs to `W`, whose minimum
nonzero rank is six over every field. Thus every nonzero element of `L_6` has
rank exactly six. The projective rank-six locus contains the linear
`P^15 = P(L_6)`.

## Realizing the rank-loss-six alignment

Fix a nonzero `X` in the embedded `L_6`. Its rank is six. For any
three-dimensional subspace `L` of `im(X)`, let

\[
U=X^{-1}(L).
\]

Since `L` is contained in `im(X)`, rank-nullity gives
`dim(U)=dim(ker X)+dim(L)=106+3=109`, and `X(U)=L`. Choose a linear map
`C:F^110 -> F^112` of rank 109 with image `U`, and a linear map
`P:F^112 -> F^110` of rank 109 with kernel `L`. Such maps exist by choosing
bases and extending them. Then

\[
PXC=0,\qquad \ker(X)\subseteq U,\qquad U=X^{-1}(\ker P),
\]

so the equality conditions in the preceding compression argument are
attained by this family. The total rank-loss budget is six. The product `PC`
has rank at most 109, so it cannot equal `I_110`; this construction does not
meet the normalized-compression premise used by the fixed-resolvent
application.

The result shows that the rank-loss-six equality geometry is algebraically
realizable inside `W`. It does not show that the maps arise as leading terms
of a complete tensor degeneration. It neither classifies every rank-six
matrix in `W` nor excludes or constructs a matrix target.
