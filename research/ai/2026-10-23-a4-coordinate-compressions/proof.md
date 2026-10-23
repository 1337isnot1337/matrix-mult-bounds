# Independent coordinate compressions have sharp minimum dimension forty

October 23, 2026. Claim `AI-A4-INDEPENDENT-COORDINATE-004`.
Written and unreviewed; finite computer-assisted proof.

Use the exact 46-dimensional space

\[
\mathcal E=\mathcal G+[\mathcal G,F]+F\mathcal G F
\subseteq\operatorname{Mat}_{28},\qquad F=G_{00},
\]

from [the preceding reduction](../2026-10-23-conjugation-limit/LOW_RANK_REDUCTION.md).
Its source convention and complete block-basis certificate are unchanged.
All imported versions are pinned in [sources.json](sources.json).

## 1. Complete finite lower bound

Let R and C be independent two-element subsets of the 28 output and
input coordinates. Deleting rows R and columns C gives a 26 by 26
matrix space. The complete finite calculation covers

\[
\binom{28}{2}^{2}=142884
\]

pairs. It reconstructs all 46 coefficient matrices and computes the
dimension of every projected space modulo the prime 1009. The histogram is:

| Dimension modulo 1009 | Number of pairs |
| --- | ---: |
| 40 | 2 |
| 41 | 59 |
| 42 | 1,482 |
| 43 | 2,168 |
| 44 | 19,151 |
| 45 | 15,096 |
| 46 | 104,926 |

A nonzero minor modulo 1009 is a nonzero integer minor. Each modular
dimension is therefore a lower bound for the complex dimension.
Consequently every pair has complex image dimension at least 40.
No equality of modular and complex ranks is assumed in this argument.

## 2. Exact sharpness

Write S(i,s)=F G(i,s) F. For deleted rows (20,25) and deleted columns
(3,7), the six independent matrices

\[
S(0,0),S(0,1),S(0,2),S(1,0),S(1,1),
3S(0,3)+2S(1,2)+S(2,1)
\]

have zero projection, entry by entry over the integers. For deleted rows
(24,25) and deleted columns (2,7), six independent killed matrices are

\[
S(0,0),S(0,1),S(1,0),S(1,1),S(2,0),
S(1,2)+2S(2,1)+3S(3,0).
\]

Independence follows from their distinct coefficient pivots in the
already independent 46-generator basis; the verifier checks it as well.
Thus each displayed projection has dimension at most 46-6=40 over C.
The modular lower bound proves equality. These are the only two pairs
of complex dimension 40, since every other pair has modular dimension
at least 41.

The sharp minimum over all independent coordinate pairs is therefore
40, and the maximum compression-kernel dimension is six.

## 3. Consequence for the complete conjugation family

Consider the original 112-dimensional saturated limit L and constant
long maps that independently delete any two output coordinates and any
two input coordinates. The preceding low-rank reduction proves that
every killed matrix is supported in block (3,0), with its outer matrix
in E. The induced outer maps delete at most two coordinates on each
side. If fewer are deleted in that block, delete additional coordinates
to reach two. This can only enlarge the kernel.

Section 1 bounds the enlarged kernel by six, so the original full
coordinate compression also loses at most six leading slice directions:

\[
\dim(PLC)\ge112-6=106.
\]

The full M(10,10,11) target requires at least nine lost directions by
`AI-A4-TWOSIDED-RANKLOSS-001`. Hence every such independent coordinate
compression is excluded, including arbitrary Laurent first-map
cancellations and the true re-saturation after compression.

The two pairs in Section 2 lift to independent deletions in the last
output block and first input block and give kernel dimension six in L.
Thus the coordinate bound is sharp within this fixed conjugation family.

## 4. Scope

This completes the independent coordinate class in the stated basis.
It does not settle arbitrary complex rank-26 outer maps. Noncoordinate
flags remain the separate [algebra question](../2026-10-23-a4-compression-algebra/QUESTION.md).
In particular, the finite calculation is not an argument that an
arbitrary bad flag can be changed into a coordinate flag.

The source, original limit, low-rank-locus reduction and rank-loss
criterion retain their previous credits. Exact finite replay and
same-session reasoning checks are not independent mathematical review.
No full target, improved exponent or formalization is claimed.
