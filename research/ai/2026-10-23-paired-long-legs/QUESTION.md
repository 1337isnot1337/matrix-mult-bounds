# Long-leg Koszul ranks of the paired convolution source

Selected October 23, 2026 from main 539b539 after checking the active
branches and PRs. This investigation is separate from the central-cover,
singular-unit and boundary-incidence continuations.

For P_a with format (a^2,a(2a-1),a(2a-1)), determine the ranks of

    wedge^p B tensor A* -> wedge^(p+1) B tensor C.

The maintained all-power formula covers the short A leg. Its finite
single-target frontier has 28 surviving formats through a=16, first at
a=14. Passing that test supplies no degeneration. Can the long-leg maps
exclude any of them, or can a proved dominance statement close this
particular screening route?

Intended output: an all-size proved rank bound or formula, exact finite
coefficient checks in the original source convention, and a target
comparison with explicit scope. Discovery ranks over a finite field are
lower bounds on complex source ranks, not usable source upper bounds for
excluding a complex degeneration. A field-specific rank comparison alone
will not be promoted to a complex obstruction.

The analytic proof now reaches the first support threshold, `p=a`, using a
full-spark interpolation basis and a two-block compatibility argument. The
same basis gives an all-degree rank floor by forcing kernel coordinates to
use at least `a` blocks. At `p=a+1` this floor dominates both long-leg target
ranks for four `a=15` and six `a=16` survivors. Exact ranks or a stronger
bound for `p>=a+1` remain the main question. No claim of a smaller exponent
is made.

## Checkpoint: through `p=a`

The [proof through the support threshold](long_leg_low_degrees.md) establishes
full column rank on both long legs for `0<=p<=a`. This range cannot exclude
any of the 28 saved targets through `a=16`: their target ranks are bounded
by the same source-domain dimensions. For every `p`, a separate support
argument proves `rank K_p >= a^2 L_(a,p)`, where `L_(a,p)` counts wedges
supported on at most `a-1` interpolation blocks. At `p=a+1`, its exact
comparison closes both long-leg rank tests for four `a=15` and six `a=16`
survivors. The other target shapes remain open. Next, strengthen the
all-degree rank floor or determine the `p=a+1` source rank.

The original coefficient matrix has rational rank `70<80` at `(a,p)=(2,3)`.
An exact bidegree-blocked rank atlas gives full column rank through `p=6`
when `a=3`, then rank `57185<57915` at `p=7`, with a 730-dimensional
kernel. The atlas uses the original signed wedge matrix and exact rational
elimination on the blocks not already certified full modulo `2`. These
finite ranks do not settle the all-size range; the next task is to explain
the longer injective range at `a=3` and determine its general boundary.
The script and replayed report are
`rank_atlas.py` and
`results/paired-long-legs-2026-10-23/graded-rank-atlas-a3.json`.

A further finite control at `(a,p)=(4,5)` has full rank `1,572,480` modulo
two across 524 original bidegree blocks, certifying full rational rank. This
is one more finite injectivity point; it does not establish an all-size
boundary or a general formula. The replayed report is
`results/paired-long-legs-2026-10-23/graded-rank-atlas-a4-p5.json` and can be
recomputed with
`python research/ai/2026-10-23-paired-long-legs/rank_atlas.py --a 4 --powers 5 --output results/paired-long-legs-2026-10-23/graded-rank-atlas-a4-p5.json`.

An equivariant weight analysis resolves the first two finite defects: at
`(a,p)=(2,3)` the kernel is
`Sym^0(U) tensor (Sym^3(V) + Sym^5(V))`, of dimension 10; at `(3,7)` it
decomposes into 20 `SL2 x SL2` irreducible types, of total dimension 730.
At `(3,8)` the kernel dimension is 3,780 and its decomposition has 30 types.
The defect degrees `3` and `7` fit the conjecture `p=a(a-1)+1`, but the
`a=4` boundary is not checked; the nonzero `p=8` kernel is a larger
post-boundary defect. The exact `a=3` atlas now extends through `p=14`:
the ranks at `p=9,...,14` are `37464, 18819, 6660, 1575, 225, 15`, with
kernel dimensions `7581, 8208, 5625, 2520, 720, 120`. See
`kernel_module_types.md` and
`results/paired-long-legs-2026-10-23/kernel-decomposition-a2-p3-a3-p7-p14.json`.
