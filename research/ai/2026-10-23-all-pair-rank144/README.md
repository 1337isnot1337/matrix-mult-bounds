# Every balanced leading-rank pair has total at most144

For every complete Laurent presentation of A4 to M(10,10,11), the
individually scalar-balanced leading ranks a,b,c satisfy

    a+b<=144, a+c<=144, b+c<=144, and a+b+c<=216.

Here a belongs to the100-dimensional target leg. If a=100, each long
leading rank is at most44. These are necessary conditions only.
Claim `AI-A4-ALL-PAIR-RANK144-001` is written and unreviewed externally,
with no formalization or exponent improvement.

The [proof](proof.md) combines the registered source-space caps with
the saturated support inequality. The only exceptional mixed pair is
(100,100). A compact Grassmannian incidence and lowering argument
reduces its arbitrary complex compression kernel to seven short
order ideals. Exported matchings and forced-cover certificates exclude
deletion budgets12+12. This rederives the needed case of the credited
PR151 compression theorem without importing its8,008-subset artifact.

## Reproduce

From the repository root with Python3.10 or later:

```sh
python -I -S research/ai/2026-10-23-all-pair-rank144/verify.py
python -m unittest discover -s tests -p 'test_all_pair_rank144.py' -v
```

Acceptance uses the standard library. It checks every matching edge
and forced-cover step without a matching search, both required tori,
the336 literal lowering identities, and all20,706 integer rank pairs.
The imported proof versions are pinned in [sources.json](sources.json).

Candidate certificate regeneration is separate:

```sh
python research/ai/2026-10-23-all-pair-rank144/discover.py --output results/local/all-pair-rank144-candidate.json
```

No regular target-unit lift, fixed coordinate kernel, or finite bound
on the remaining Laurent pole order is assumed. The source cap44 is
used only below rank80, and arithmetic pairs at sum144 remain open
to this argument. No surviving pair is asserted to be constructible.
