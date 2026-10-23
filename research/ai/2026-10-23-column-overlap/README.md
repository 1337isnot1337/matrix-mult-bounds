# Paired-source maps with full channel rank

The [proof](proof.md) gives a repair-cost bound for fixed injective
polynomial-column routing. Each retained column may use an arbitrary
regular square channel matrix. The first map and auxiliary maps may have
Laurent poles of any order, and their contributions may cancel poles.

Let D be the target first dimension, N the number of source coefficient
positions covered by all retained windows, and G the corresponding count
from invertible leading blocks. If the two good-window graphs have c_B
and c_C components, the auxiliary first flattening has rank at least

\[
\max(0,D-N+G-c_Bc_C).
\]

At fixed width, near-full outer dimensions and only o(n) singular leading
channel blocks, this is n^2-o(n^2). Full channel rank is permitted. Mixing
different source polynomial columns remains outside the theorem.

The exact controls include two integer matrix-product restrictions,
a full-channel example attaining the connected `D-1` flattening bound,
boundary windows, genuine slice-rank loss, polar cancellation, and a
moving exact restriction showing why the saturation correction is needed.

```sh
python -S research/ai/2026-10-23-column-overlap/verify.py \
  --output results/local/column-overlap-controls.json
python -m unittest discover -s tests -p test_column_overlap.py -v
```

The retained report is
[controls.json](../../../results/column-overlap-2026-10-23/controls.json).
The [source pins](sources.json) identify imported conventions and the
earlier Laurent normalization argument. This is owner-directed OpenAI
Codex work, written and unreviewed. No improved exponent is claimed.
