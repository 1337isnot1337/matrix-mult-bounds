# Exact pure-fiber curves and the complete third-order criterion

At c=d=0, PR101's exported polynomial two-jet is already an exact
polynomial incidence curve for every complex a,b. The maps have degrees
at most two and one. Literal-source replay checks their entire product,
not a truncated Schur series: all source rows in the fixed
100-dimensional kernel vanish identically as polynomials in a,b,t.
Leading unit minors give fourteen-row maps and first-source rank twelve
near t=0.

Together with PR107's mixed d-nonzero three-jets and PR101's exact linear
components, this proves that the projective normal-class existence
criterion through order three is exactly

```text
(a-c)*(b+c)*(c*lambda^3+mu^3)=0.
```

The criterion allows a suitable boundary tangent and higher coefficients;
it does not say that every representative extends. The mixed component's
fourth-order and all-order lifting remain open. These are local
rank-twelve incidence statements, not the full matrix target or an
exponent improvement. Both new claims remain written and unreviewed.

Read [proof.md](proof.md), [QUESTION.md](QUESTION.md) and
[source pins](sources.json). The polynomial maps themselves are credited
to PR101; this continuation certifies their exact pure-fiber consequence
and the resulting third-order classification.

From the repository root with root requirements installed:

```sh
python research/ai/2026-10-23-conic-pure-criterion/verify.py
python research/ai/2026-10-23-conic-pure-criterion/verify.py --certificate results/conic-pure-criterion-2026-10-23/curve.json
python -m unittest discover -s tests -p test_conic_pure_criterion.py -v
```
