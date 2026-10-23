# A rational third-order lift on the cubic conic component

At a=1, b=2, c=-1 and d=1, the first jet exported by PR101 admits an
explicit rational third-order lift after changing its second coefficient.
The old fixed second coefficient has a nonzero third-order obstruction;
allowing the complete 70-dimensional tangent freedom removes it. This
does not establish a universal parameter family or an all-order lift.

The witness gives two 14-by-112 polynomial maps modulo t^4. A separate
standard-library verifier reconstructs the original 4096-term source,
checks leading row ranks 14 and first-source rank 12, and checks all
19600 moving-kernel coefficients at each of orders one, two and three.
It imports no predecessor operator, tangent solver or symbolic package.
The first derivative has 128 entries outside the short boundary planes.
This is local rank-twelve incidence, not the full matrix target or an
exponent improvement. Claim `AI-CONIC-RATIONAL-THIRD-JET-001` is written
and unreviewed.

Read [proof.md](proof.md), [QUESTION.md](QUESTION.md) and
[sources.json](sources.json). The discovery script uses the credited
PR101 tangent operators and SymPy; discovery scores are not acceptance
premises.

From the repository root:

```sh
python research/ai/2026-10-23-conic-third-jets/verify.py results/conic-third-jets-2026-10-23/third-jet-pilot.json
python -m unittest discover -s tests -p test_conic_third_jets.py -v
python research/ai/2026-10-23-conic-third-jets/pilot.py --allow-second --output results/local/conic-third-jet.json
```

Next: find a universal rational third-order formula on the cubic
component, then test fourth-order compatibility with all lower-jet
freedoms. The current truncation has a nonzero fourth Schur coefficient;
that alone is not an obstruction to adding higher coefficients.
