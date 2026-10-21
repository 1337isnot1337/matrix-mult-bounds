# Agent-board review and a correction to the finite-rank frontier

Checked October 20, 2026. [Source and post pins](../references/board_review_2026-10-20.json).

## Scope and attribution

The [matrix-multiplication board](https://board.bigospeedrun.com/matrix-multiplication)
contains four posts by **matmul-swarm, an agent of @fringewidth**, dated October
17. The JSON feed had four posts and `next: null`, so this review covered the
entire feed returned then. The posts report no exponent below 9/4. Their
supporting scripts were described as not public. Their labels such as
"Confirmed x3" are author-reported agent cross-checks, not this repository's
verification or a leaderboard review.

The [integer board](https://board.bigospeedrun.com/integer-multiplication) had
one launch announcement and the [Fourier board](https://board.bigospeedrun.com/exact-dft)
had no posts. No transferable mathematical result was found in those feeds.
This is not an exhaustive survey of private groups or other discussion sites.

## Findings worth carrying into the research plan

| Post | Reported finding | Consequence for this repository |
| --- | --- | --- |
| Part 1, `98dae387-0a9b-44a4-ad70-a57d8ef5879b` | Small exact schemes, random numerical tensor fitting, and certain symmetric ansatzes did not reach 9/4. The proposed first exact-rank size was 34. | Avoid interpreting a numerical plateau as an impossibility proof. Correct the size threshold below before allocating a search. |
| Part 2, `3a4edfaa-d6a8-44ec-9131-6ff0a66781d3` | Numerous group/TPP obstructions; three SL2(5) degeneration shapes remain open in their work. Counting statistics do not decide the needed integer-potential feasibility. | Keep SL2(5) shapes (9,9,12), (9,10,11), (10,10,10) as attributed leads requiring exact certificates, not verified open cases here. |
| Part 3, `e503331e-a40c-476a-9d7c-58ebe859197e` | STPP, aggregation and border-sum searches have substantial scoped obstructions. A claimed exclusion of some unequal matrix-tensor sums was withdrawn. | Preserve the withdrawal. Do not replace the per-summand asymptotic sum inequality by an invalid total-volume shortcut. |
| Part 4, `c22e71e1-45e5-4f44-bfb6-4f1701b9a5d7` | A single border-rank certificate for M16 with at most 511 terms would suffice. Their pinned Lean library has an equal-square interface but lacks the needed unequal-sum bridge. | The inequality 511^4 < 16^9 is locally checked. The Lean API and missing-dependency claims remain source reports until the exact library revision is inspected. |

The board's rank, border-rank and group-theoretic searches concern different
objects from our convolution shared-leg search. We retain their useful warnings
without treating those reported obstructions as a proof that our route is closed.

## Locally checked correction: exact schemes at sizes 34-37

The board correctly computes its thresholds from Bläser's bound, but misses a
stronger published lower bound relevant at these sizes. Massarenti and Raviolo,
[*On the rank of n x n matrix multiplication*, arXiv:1211.6320v2](https://arxiv.org/abs/1211.6320v2),
Remark 3.3, pages 9-10, give over the complex numbers

$$R(M_n)\ge\frac83n^2-7n.$$

We inspected the primary manuscript's statement and the surrounding derivation,
including the rendered page. We did not independently audit its full proof.
This is an **exact-rank** bound; applying it to border rank would be invalid.

A rank-R square scheme strictly beats 9/4 only if $R^4<n^9$. The following
consequences use integer powers and rational ceilings, without logarithm rounding.

| n | Published exact-rank lower bound, rounded up | Largest R with R^4 < n^9 | Consequence |
| ---: | ---: | ---: | --- |
| 34 | 2845 | 2791 | Excluded |
| 35 | 3022 | 2979 | Excluded |
| 36 | 3204 | 3174 | Excluded |
| 37 | 3392 | 3376 | Excluded |
| 38 | 3585 | 3585 | Only R = 3585 survives these bounds |
| 39 | 3783 | 3800 | These bounds leave a window |
| 40 | 3987 | 4023 | These bounds leave a window |

Thus n=38 is the first size not excluded in our scan of n=3 through 40 using
these two lower bounds. This is not a claim that all other known obstructions
have been checked, that rank 3585 at n=38 exists, or that a new exponent is proved.
The M16 border-rank question is unaffected.

[Exact report](../results/koszul-2026-10-20/board_thresholds.json), reproduced by:

```sh
python research/ai/2026-10-20-koszul/board_thresholds.py \
  --output results/koszul-2026-10-20/board_thresholds.json
```

## Integration decision

Continue the convolution route, now screening candidates with the exact Koszul
formulas. Keep the group's finite-object leads in this attributed map. A claim
can enter the local theorem ledger only after its hypotheses and proof artifacts
have been checked; board publication alone is not that check.

## Subsequent source refresh

After PR #32, the matrix board still returned the same four October 17
posts. The new [external-source comparison](external_followups.md) records
an earlier scalar-profile result found in a public research repository
and distinguishes its main-branch theorem from its open follow-up PR.
