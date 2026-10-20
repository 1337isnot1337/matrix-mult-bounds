# Product-filtration investigation

Date: October 20, 2026. AI-derived research by Codex at the owner's request.
Base: `5d831b4`; owned branch: `research/filtration-compatibility-20261020`.

## Question selected before investigation

R2: Does the explicit matching profile satisfy all three two-source
determinant-filtration inequality families for every positive integer
`a,b,c,d`, rather than only on the previously checked grid through 12?

An exact violation would give a missing constraint to study. An all-size
compatibility proof would close this proposed escape from the scalar barrier
and identify which stronger tensor construction is needed. Neither outcome
alone implies an exponent bound.

## Coordination and scope

At selection, GitHub returned no open issues or pull requests. The fetched
research branch `research/koszul-and-scaling-20261020` contains a separate
Koszul-packing obstruction. This investigation uses its latest commit as its
base without changing that worker's checkout or branch. No new agents are
launched. The archived first and second passes are preserved.

The shared-leg entropy and determinant-filtration machinery is external work
of OpenAI and classical polynomial algebra, as attributed in the source
registry. The matching profile is the earlier local analysis. New results will
be labeled by their actual proof and verification status.

## Completed first milestone

[Research note](research_note.md): an all-size proof characterizes the three
filtration families as precisely separate concavity including the zero boundary.
It proves compatibility of the matching profile for all sizes. The written
argument is unreviewed; no exponent improvement is established.

```sh
python research/ai/2026-10-20-concavity-equivalence/verify.py \
  --output results/concavity-equivalence-2026-10-20/verification.json
```

The result closes R2 for these families and is tracked as AI-FILTRATION-007.

## Follow-up question

After the first milestone, investigate the analytic gap in the second-pass
R4 draft: do replication, the rank bound and separate concavity automatically
give the homogeneous limit used by its rigidity and curvature criteria, and
can differentiability be removed? Uznański v2 already proves rescaling for
oriented profiles (Lemma 4.1); this pass will attribute that prior result and
give a self-contained scalar argument tied to the local hypotheses. A positive
curvature gain remains a separate, unproved tensor question.

The follow-up is written in [homogeneous_rigidity.md](homogeneous_rigidity.md).
It supplies a direct scalar limit proof, one-sided derivatives, the critical
shape and conditional curvature bound. A compactness argument explains why
excluding all endpoint characters would imply some strict improvement. No
positive gain or endpoint exclusion is proved.

## Concurrent work and integration

A later fetch found `research/product-filtration-20261020` at `712c91a` and
the updated Koszul branch at `30219d0`, with overlapping compatibility and
rigidity conclusions. The notes cite these commits and distinguish the extra
equivalence, boundary counterexample, scalar limit proof, and compactness
argument. The full-filtration entropy branch at `f5b42e1` studies a different
analytic score and reports an additional balanced-family barrier. These are
concurrent AI-derived reports, not independent reviews.

This directory and its results were renamed to avoid colliding with the other
filtration worker's files. Shared status/ledger edits still need ordinary
integration when the branches are combined. No other worker's checkout was
modified.

## Active construction route

[fatpoint_growth_route.md](fatpoint_growth_route.md) extends the other
worker's degree-three target to all degrees and derives an explicit cost
threshold for a sufficient degeneration. The required construction remains
open. The exact report in `fatpoint-route.json` records necessary Koszul
screens and the conditional rational root certificate. It is not a new bound.

The next experiment investigates matrix-space bases and possible degenerations
of `C(a,B)` to these targets. Coordinate/diagonal-weight packing alone is
already obstructed; interpolation from a diagonal tensor is insufficient.
