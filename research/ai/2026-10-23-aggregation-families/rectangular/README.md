# Rectangular targets and the complete aggregation grid

October 23, 2026. Owner-directed OpenAI Codex research. Written and unreviewed.

The question is whether unequal matrix shapes or coordinate-dependent
target dimensions can overcome the complete-grid cost gate. The
[proof](proof.md) gives two precise restrictions on that approach.

1. For a conflict-free family with one fixed ordered cardinality shape
   `(a,b,c)`, every complete-grid budget fails the direct 9/4 comparison
   when `a+b+c<=32`. Target dimensions may differ between coordinates
   and between products. The exact certificate checks every shape,
   including empty parts, and includes dimension 33 as a non-exclusion
   control.
2. If one retained target fills the centered coordinate spaces of
   dimensions `q_r-1>=2`, the fixed leading grid forms are linearly
   independent after projection to that target. Reweighting those same
   forms and the same correction forms cannot remove a leading position.

These statements concern the specified cost certificates and forms.
They are not lower bounds on tensor rank. Mixed ordered cardinality
shapes, smaller targets with a pruned grid, and new rank-one forms are
separate possibilities. In particular, the unequal-shape examples in
Appendix D of the external paper use scalar gradings and are outside the
first result's induced-edge hypothesis.

## Reproduce

```sh
python research/ai/2026-10-23-aggregation-families/rectangular/verify.py
python -m unittest discover -s tests -p test_aggregation_rectangular.py -v
```

The standard-library verifier rebuilds the complete integer shape table,
checks the saved certificate, and checks exact rational local matrices
for the second result. These finite controls accompany the all-dimension
proof. They are not independent mathematical review or formalization.

The [validation receipt](validation/report.json) and
[focused log](validation/focused.log) account for all 914 discovered
tests: 907 unchanged prior successes, five new tests, and the two rerun
claim-ledger and relative-link checks. Existing implementations and
witnesses are unchanged; the prior five archive replays are retained.
This is combined coverage, not a new uninterrupted full-suite run.

## Sources and continuation

The imported framework is Solomonik and Blaeser,
[arXiv:2610.26563v2](https://arxiv.org/html/2610.26563v2), revised
October 22, 2026: Sections 5.3 and 5.6 for centering and corrections,
Definition 7 for conflict freedom, Section 6 and Appendix D for graded
unequal-shape constructions. The uniform exact identity is rederived in
the [parent proof](../proof.md). The induced-edge argument extends the
[balanced cost gate](../cost_floor.md).

Every complete tripartition on d coordinates has target volume n^d
when its coordinate dimensions are all n, even when its three matrix
dimensions differ. With coordinate sizes n_r the volume is their
product. Thus simply changing the three part sizes does not change
the volume term in the asymptotic sum theorem. Appendix D's additional
products rely on a broader graded combinatorial model; their reported
costs are not evidence of a 9/4 improvement.

The next constructive question removes the full-target hypothesis:
restrict different products to smaller coordinate spaces, omit exactly
zero leading and correction forms, and compare that actual budget with
the sum of the target volumes to the power 3/4. A successful cost must
include every surviving correction position. A failed finite search
will be recorded as a finite experiment, not a nonexistence theorem.
