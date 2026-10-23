# A4 unit-image exclusion down to rank107

The [written proof](proof.md) extends the prior regular-unit-image
exclusion from rank109 to rank107. One long map must be regular with
rank110 limit, and the source lift of the target identity must be regular.
All finite pole orders of the other maps are allowed. Regular source
unit slices of corank at most three are included.

The argument uses the existing source locus below rank32 after proving
first-map regularity. A varying-retraction lemma gives injectivity of
the limiting first map, and target Segre rulings force100 dimensions
into a fixed16-dimensional source space if the other long map has a
pole. Ordinary specialization then gives the existing12>11 contradiction.

Claims `AI-CYCLIC-RANK-LOCUS-REGULARITY-001` and
`AI-A4-UNIT-IMAGE-RANK107-002` are written and unreviewed. There is no
independent mathematical review, formalization, constructed target or
exponent improvement. Rank106, singular long-leg limits and polar unit
lifts remain unresolved by this argument.

From the repository root, using the maintained requirements:

```sh
python research/ai/2026-10-23-unit-image-rank-gap/verify.py
python -m unittest discover -s tests -p 'test_unit_image_rank_gap.py' -v
```

The saved finite controls contain56 exact rational retractions, a fixed
projection losing rank5 versus recovered rank8, nine literal cyclic source
matrices at a=2,3,4, five A4 boundary cases and three source byte pins.
The test suite independently compares the retraction construction to
an exhaustive small integer search. These calculations support the
written proof and do not formalize arbitrary Laurent series.

`QUESTION.md` records the starting question and its acceptance criteria.
`sources.json` identifies prior local results without changing their
credits or evidence status. No new external theorem is imported.
