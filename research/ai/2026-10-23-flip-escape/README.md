# A closed flip component and an explicit split escape

This investigation changes the pinned external rank-76 M(4,5,5)
decomposition before attempting a Q(6,4) grid assignment.

The [component proof](component_proof.md) closes all finite standard
shared-factor flips and term gauges of that exact seed: none enables
rank reduction or deletion of a nonempty subset by the physical
matrix-multiplication stabilizer. The certificate checks 3306 unit minors
and the scalar trace pairing of every proportional-W class.

Rank-increasing splits fall outside this theorem. The
[split construction](split_proof.md) raises the term count to 80, then
uses one common physical stabilizer transformation to delete four terms.
A [five-split continuation](five_split.md) gives a second exact witness.
Both use 76 terms, have no negative-degree tensor coefficients, and give the complete
matrix multiplication tensor at degree zero.

| Witness | Exact intermediate terms | Distinct U directions | Positive-degree remainder coefficients |
| --- | ---: | ---: | ---: |
| Four splits | 80 | 72 | 51 |
| Five splits | 81 | 71 | 172 |

Both changed seeds remain subject to stronger incidence conditions;
neither fits the proposed termwise Q(6,4) grid. Their new shared-U pairs
permit further flips that can change some W directions. The later
[fixed-component certificate](../2026-10-23-fixed-flip-components/README.md)
shows that every such finite continuation still retains 50 W directions
requiring ten rank-four groups. Its separate trace argument also closes
further subset deletion in the five-split component. See
[the continuation checkpoint](ACTIVE.md) for the remaining questions.
No rank record or smaller exponent is established.

## Reproduce the component certificate

```sh
python research/ai/2026-10-23-flip-escape/verify_component.py
python research/ai/2026-10-23-flip-escape/verify_split.py
python research/ai/2026-10-23-flip-escape/verify_split.py --variant five
python -m unittest discover -s tests -p test_flip_component.py -v
python -m unittest discover -s tests -p test_split_border_seed.py -v
```

These commands replay all three stored certificates and run ten focused
tests. They use only the Python standard library. The tests include
changed and missing witnesses, a rational shared-factor flip, complete
split identities at two nonzero rational parameters, and a negative
control where individual nilpotence fails to imply joint nilpotence.
Changed schema, scope and variant metadata are rejected as well.
To regenerate the certificates separately:

```sh
python research/ai/2026-10-23-flip-escape/verify_component.py --write-certificate /tmp/component_certificate.json
python research/ai/2026-10-23-flip-escape/verify_split.py --write-certificate /tmp/split_certificate.json
python research/ai/2026-10-23-flip-escape/verify_split.py --variant five --write-certificate /tmp/five_split_certificate.json
```

The external algorithm, conversion commit, and source theorem versions
are credited in `sources.json`. No historical archive is modified.
Both the written argument and its finite controls were developed in this
owner-directed AI session; they have no independent review.
