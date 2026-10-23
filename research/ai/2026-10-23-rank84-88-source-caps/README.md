# Sharp rank84/88 source caps and a Laurent sum136 gate

The [written proof](proof.md) gives sharp complex A4 source-space
dimension caps56 below matrix rank84, and60 below rank88. It adopts the
prior characteristic-zero order-ideal reduction and retains credit for
the staircase spaces attaining the bounds. Applying the prior saturated
target-support inequality improves the necessary balanced long leading
rank sum from144 to136 for A4 to M(10,10,11).

The exact acceptance replay checks70 coherent lower-bound witnesses in
each certificate, all1404 remaining size57 ideals and118 remaining size61
ideals, with exported odd84/88 minors. It independently rebuilds4096
source terms,112 block factorizations, both complete inventories, three
sharpness/boundary spaces and644 newly excluded target rank pairs.
Discovery uses a different inventory algorithm and is never imported by
acceptance.

These are **written, unreviewed** computer-assisted proofs. They do not
construct a matrix target or improve the exponent. The prior64-dimensional
staircase of rank at most88 meets the two dimension/rank conditions at
balanced ranks68,68; a further improvement needs more than those two
inequalities alone. That space has not been realized as a compression
kernel or a degeneration.

From the repository root:

```sh
python research/ai/2026-10-23-rank84-88-source-caps/verify.py
python -m unittest discover -s tests -p test_rank84_88_source_caps.py -v
```

Regenerate discovery witnesses with `discover.py --rank 84` and
`discover.py --rank 88`, then run acceptance. Compressed certificates and
the frozen summary are in `results/rank84-88-source-caps-2026-10-23/`.
Exact prior versions and artifact digests are in [sources.json](sources.json).

Claims: `AI-A4-RANK84-SOURCE-CAP-001`,
`AI-A4-RANK88-SOURCE-CAP-002`, and
`AI-A4-BALANCED-LONG-SUM136-003`.

This continuation follows unmerged PR129's source-space and Laurent
arguments and PR155's staircase counterexamples. Their evidence status
and original credit are preserved. No new external structural theorem
or historical priority is claimed.
