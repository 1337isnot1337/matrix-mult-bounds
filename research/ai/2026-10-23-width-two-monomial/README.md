# Width-two monomial score: all weights and all sizes

The [written proof](proof.md) closes both input orientations at minimum
size two for the original monomial-support scorer. On C(2,b), its exact
deficit from P_* is `[2(inactive y coordinates)+(y coordinates in
one-endpoint components)]/3`. It classifies and counts every equality
support. On C(b,2), equality requires the full original support and the
sharp proper-support deficit is `(b-1)/3`.

The standard-library verifier compares an independent path formula
against the pinned original minimum-support/component/recognition code.
Every sign word is realized by explicit integer weights. The finite
census therefore covers all supports in the stated sizes, with no
weight-magnitude cutoff, in both orientations.

```sh
python research/ai/2026-10-23-width-two-monomial/verify.py --max-b 10 --check results/width-two-monomial-2026-10-23/census.json
python -m unittest discover -s tests -p 'test_width_two_monomial.py' -v
```

The saved census has 59,046 orientation/support checks for 2<=b<=10.
Tests also check huge affine gauges, inactive coordinates, sharp gaps,
the orientation distinction and the equality-count recurrence to b=100.
These finite checks support the proof; they do not establish its
universal quantifiers by themselves.

Claim `AI-WIDTH-TWO-MONOMIAL-001` is written and unreviewed. No arbitrary
degeneration exclusion, tensor-character construction, independent
review, formalization or exponent improvement is claimed. PR118's
separate exact-ranking work retains its credit and is not a dependency.
The archived sources remain unchanged.
