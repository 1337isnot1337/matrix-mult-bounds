# A4 long-map leading ranks

The [new equality-case proof](corank_one.md) excludes every complete
complex Laurent degeneration A4 to M(10,10,11) with either long map
regular and of rank at least109 at zero. The other maps may have
arbitrary finite Laurent poles. No source-unit rank assumption remains.

At rank109, the source minimum16 is attained by every nonzero leading
lift of a target rank-one matrix. Its kernel lies in the fixed source
column image. The prior minimum-rank classification and one common row
vector then force all lifts into a four-dimensional source ruling. The
leading first-map kernel contains an invertible matrix, contradicting
the regular kernel residual's rank bound of two.

The [normalized leading-rank bound](proof.md#simultaneously-normalized-long-map-ranks)
also requires r_B+r_C<=208 after independently dividing each long map
by its minimum entry valuation. Together the results leave only
r_B<=108, r_C<=108 and r_B+r_C<=208. These are necessary conditions,
not constructions of the remaining cases. A general A4 degeneration and
an exponent below9/4 remain unproved.

The full-rank regular-kernel argument is credited to concurrent
[PR113](https://github.com/1337isnot1337/matrix-mult-bounds/pull/113), at
`08ac3e983e270cf3df4e26d960ceb16415f7ef31`. Its A4 claim is not duplicated
as a new result here. [The self-contained proof](proof.md) states the
rectangular version used by this continuation. Source minima and the
minimum-rank variety retain their original credit and [byte pins](sources.json).

Claims `AI-A4-CORANK-ONE-LONG-001` and
`AI-A4-NORMALIZED-LONG-RANK-SUM-002` are **written and unreviewed**.
Parent and peer agents checked the arguments in the generating session;
this is not independent external mathematical review or formalization.
All continuation work is owner-directed OpenAI Codex work.

With the root requirements installed, run from the repository root:

```sh
python research/ai/2026-10-23-long-leg-rank-obstruction/verify.py
python -m unittest discover -s tests -p test_long_leg_rank_obstruction.py -v
```

The frozen report is
`results/long-leg-rank-obstruction-2026-10-23/controls.json`. It checks
12 polar residual families,15 sharp rank-loss matrices, five scalar
normalizations,100 target generators, three literal source factorizations,
three row-space intersections,20 cubic divisors of one sextic, three
bounded-rank matrix-space controls, and12,100 normalized rank pairs.
The latter count concerns integer rank budgets, not constructed maps.
Finite controls check the proof's linear algebra; they do not formalize
its all-order, irreducibility or universal classification arguments.

Use `verify.py --write` to regenerate the report, then replay without
that flag. Tests reject changed source pins, missing predecessor credit,
altered rank boundaries and overstated proof status.
