# A nonempty open set of arbitrary mixed graphs

Claim `AI-GENERIC-MIXED-GRAPHS-094` gives a written, unreviewed exclusion
of M(10,10,11) on an explicitly defined nonempty open set of all six
mixed-graph coefficients and the partner parameter a at b=1. It extends
to an open set on b!=0 by the checked source torus.

The certificate uses56 necessary normal equations, a constant plane
complement and two fourteen-variable source blocks. At its rational
witness,559 cubic minors in each block generate all2380 quartic forms
after multiplication by the normal variables. Exact modular rank lifts
this to a nonempty Zariski-open condition in characteristic zero.

- [Proof and the exact open-set definition](proof.md)
- [Remaining exceptional geometry](QUESTION.md)
- [Witnesses](certificate.json) and [pinned sources](sources.json)
- [Replayed report](../../../results/generic-mixed-graphs-2026-10-21/report.json)

From the repository root with the maintained dependencies installed:

```sh
python research/ai/2026-10-21-generic-mixed-graphs/verify.py --output results/local/generic-mixed-graphs.json
python -m unittest discover -s tests -p test_generic_mixed_graphs.py -v
```

The checker reconstructs the symbolic source, its block partition and the
rational witness. It replays the selected cubic minors and their exact
quartic consequences, and verifies the frame torus covariance. No random
search, Singular or numerical tolerance is used by maintained acceptance.
The exceptional complement and the smaller-exponent goal remain open.
