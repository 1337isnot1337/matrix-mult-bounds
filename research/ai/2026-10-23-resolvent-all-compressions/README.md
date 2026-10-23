Preservation note, October23: before submission, main advanced to PR139
(`3008d70`), whose written theorem proves minimum rank exactly six over
every field and supersedes this narrower complex cubic certificate.
This package is preserved as an alternative proof artifact. It is not a
new frontier result, and no new global claim or PR is proposed for it.
The broad exclusion and moving-frame consequence should be cited to PR139.

# All constant compressions in the fixed singular-unit resolvent

The [written proof](proof.md) removes the predecessor's rank hypothesis:
every constant complex pair PC=I110 is excluded for the exact ansatz
B(t)=P(tI+N)^(-1), with arbitrary finite Laurent first maps.
A nineteen-parameter rank gap is certified by 1,330 cubic coefficient
vectors independent modulo two. Their integer determinant is nonzero,
so they span every cubic over C. This is a polynomial identity argument,
not a test of finitely many complex parameter values.

Run from the repository root:

```sh
python research/ai/2026-10-23-resolvent-all-compressions/certify.py --verify results/resolvent-all-compressions-2026-10-23/certificate.json
python -m unittest discover -s tests -p test_resolvent_all_compressions.py -v
```

The verifier uses the standard library. The full argument is written and
unreviewed; the certificate does not formalize its Laurent or module
arguments. Moving compressions, resolvent corrections, other unit
trajectories and the general A4 target remain open. No exponent improvement.
