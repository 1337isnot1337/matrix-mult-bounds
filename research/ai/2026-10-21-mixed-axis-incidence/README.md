# Uniform mixed-axis closure

Claim `AI-MIXED-AXIS-CLOSURE-092` closes the ten-dimensional normal family
left by claim091. An auxiliary projection over C(ell), a uniform13-minor,
and two rank-one relation minors reduce it to two coordinates. Two cubic
minors then leave only the four common-plane normals. The written proof
excludes M(10,10,11) for the specified axis, with arbitrary boundary
four-space and higher maps. It has no independent review or exponent gain.

- [Proof and exact quantifiers](proof.md)
- [Question and continuation](QUESTION.md)
- [Pinned dependencies](sources.json)
- [Polynomial and minor witnesses](certificate.json)
- [Reconstructed report](../../../../results/mixed-axis-incidence-2026-10-21/report.json)

From the repository root, with the maintained requirements installed:

```sh
python research/ai/2026-10-21-mixed-axis-incidence/verify.py --output results/local/mixed-axis-incidence.json
python -m unittest discover -s tests -p test_mixed_axis_incidence.py -v
```

The checker reconstructs the source and all prior axis reductions. It
does not require Singular, which was used only to discover a polynomial
relation basis. General graph charts and the sub-9/4 goal remain open.
