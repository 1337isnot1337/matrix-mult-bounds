# All graphs at generic partner values

Written AI-assisted exclusion, unreviewed. No exponent improvement.

The [proof](proof.md) excludes every mixed graph and boundary four-space
at each a in a nonempty open subset U of the partner line b=1. The set
contains2 and has finite complement. The checked source torus extends
to b nonzero with a/b in U. Exceptional partners are not classified.

The certificate uses polynomial54/48 initial enclosures, source-rank
constraints and exact cubic spans over Q(a). All79 rational rank guards
are verified at the reference a=2. The permitted set depends only on
the partner; every graph is excluded there, rather than only a generic
graph. No expression in graph coefficients is inverted.

```sh
python research/ai/2026-10-21-generic-partner-all-graphs/verify.py --output /tmp/generic-partner.json
python -m unittest discover -s tests -p test_generic_partner_all_graphs.py -v
```

Use root requirements.txt. See [QUESTION.md](QUESTION.md) for the finite
exceptional-parameter problem and the limits of current discovery data.
