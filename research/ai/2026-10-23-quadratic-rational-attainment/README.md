# Rational attainment of the quadratic rank defect

For every a>=3, nonzero quadratic-in-z slices over Q with coefficient
degrees below a have exactly the full crossed-source ranks

    {a^2, a^2+a, a^2+2a}
      union {a^2+2a-1 : gcd(a+1,210)>1}.

The [proof](proof.md) combines the merged quadratic kernel-index and
torsion criteria with Mazur's rational torsion theorem, handles singular
and doubled boundaries, and supplies explicit polynomial certificates
of orders 2, 3, 5 and 7. The necessity argument does not assume that a
genus-one curve has a rational point. The order-2, order-3 and order-5
certificates work over every field; the order-7 certificate works in
characteristic different from 2. Only the rational-field assertion is
an exact classification here.

This is written, unreviewed research with same-session checking. It is
not independent mathematical review, formalization, a full cyclic-source
classification for a>3, or a matrix-multiplication exponent improvement.
The merged prior results and external theorem versions are credited in
[sources.json](sources.json).

The companion [verifier](verify.py) reconstructs the full source and
recurrence matrices without importing a prior verifier. The saved
[report](../../../results/quadratic-rational-attainment-2026-10-23/controls.json)
contains four exact recurrence ranks, four nonzero integer kernel
tuples, thirteen polynomial recurrence identities, and ten complete
rational source-rank computations. A separate F2 source at a=3 checks
the excluded characteristic-two degeneration of q7. Orders 2 and 3 use small auxiliary T_2 and
T_3 matrices without asserting source ranks at sizes a=1 or a=2.
The original order-5 and order-7 discovery receipts are preserved in
the result directory and pinned. No discovery search is rerun.

From the repository root, reproduce the bounded report and eight
focused tests with:

```bash
python research/ai/2026-10-23-quadratic-rational-attainment/verify.py
python -m unittest discover -s tests -p 'test_quadratic_rational_attainment.py'
```

The tests replay the saved report, compare the supplied discovery
arrays, retain every recurrence endpoint, reject corrupted first and
last equations, enforce the small-matrix/source-size boundary, guard
exact rational arithmetic, check the characteristic-two boundary, and
verify the local source hashes. The
all-size conclusion comes from the written argument, not the bounded
profiles. This package has no dependency on the separate split-family
attainment draft.
