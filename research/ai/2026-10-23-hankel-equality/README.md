# Deficient Hankel symbols near saturation

The [written unreviewed proof](proof.md) extends the earlier rank-two
equality containment to every scalar Hankel rank `r<min(a,b)`. In fact
`rank M_F < ab*r+min(a,b)` already forces one constant length-r supporting
scheme for all coefficient sequences of F. An explicit family has a
moving scheme at the first excluded rank `ab*r+min(a,b)` for every r>=2.

This is a pointwise source-slice constraint. It does not make the scheme
constant over an entire matrix-parameter family, supply a new matrix-target
exclusion, or improve the exponent. The [question](QUESTION.md)
records that remaining family problem. The historical ordinary A9 square
sums are already excluded by the credited Wronskian application.

The proof adopts the earlier full-output coefficient-map lemma and
two-variable injections, then descends the homogeneous kernel gcd from
both rational function fields. The prior rank-two theorem, classical
Hankel description and concurrent PR76 counterexamples retain their
credit in [sources.json](sources.json).

Exact controls check saturated ranks one through eight, three genuine
excess-one cases inside the strip, reduced and nonreduced schemes,
both projective endpoints, and the sharp moving-support family at ranks
two through eight. A full-symbol counterexample protects the strict
rank hypothesis. These checks are finite evidence, not the general proof.

From the repository root, with the maintained requirements installed:

```sh
python research/ai/2026-10-23-hankel-equality/verify.py --output results/hankel-equality-2026-10-23/controls.json
python -m unittest discover -s tests -p test_hankel_equality_descent.py -v
```

The independent test reconstructs each homogeneous kernel and its gcd
over an exact rational function field. It also checks that a common
scheme alone does not imply saturation. No independent mathematical
review or formalization is claimed.
