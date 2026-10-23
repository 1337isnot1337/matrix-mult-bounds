# A closed flip component and an explicit split escape

This investigation changes the pinned external rank-76 M(4,5,5)
decomposition before attempting a Q(6,4) grid assignment.

The [component proof](component_proof.md) closes all finite standard
shared-factor flips and term gauges of that exact seed: none enables
rank reduction or deletion of a nonempty subset by the physical
matrix-multiplication stabilizer. The certificate checks 3306 unit minors
and the scalar trace pairing of every proportional-W class.

Rank-increasing splits fall outside this theorem. An explicit four-split
construction and complete Laurent replay are the positive continuation
described in `QUESTION.md`. The package does not establish a matrix
target from Q(6,4), a new rank record, or a smaller exponent.

## Reproduce the component certificate

```sh
python research/ai/2026-10-23-flip-escape/verify_component.py
python -m unittest discover -s tests -p test_flip_component.py -v
```

The command replays the stored certificate. To regenerate its selected
unit minors separately:

```sh
python research/ai/2026-10-23-flip-escape/verify_component.py --write-certificate /tmp/component_certificate.json
```

The external algorithm, conversion commit, and source theorem versions
are credited in `sources.json`. No historical archive is modified.
Both the written argument and its finite controls were developed in this
owner-directed AI session; they have no independent review.
