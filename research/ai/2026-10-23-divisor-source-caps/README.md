# Sharp divisor-strip source-space caps

Let d<a divide a, with a>=2. The [written proof](proof.md) shows that for
every integer ceiling q in

    a(a+d-1)<=q<a(a+d),

the largest dimension of an arbitrary complex linear space of A_a source
slices of rank at most q is exactly ad. A divisor-cycle partition gives
the upper bound after rank-preserving torus specialization. Literal
residue blocks reduce each forbidden coordinate pair to d^2 copies of
the credited smaller biform block gap. A d-row strip attains the cap.

This extends PR129's A4 cap8 to all balanced sizes and proper divisors.
The active-ruling corollary recovers the credited A4 rank102 exclusion;
it claims no new A4 cutoff. Claims `AI-DIVISOR-SOURCE-CAP-001` and
`AI-DIVISOR-LONG-EXCLUSION-002` are written and unreviewed. The block
lemma retains its inherited P1 bundle-splitting dependency. No independent
review, formalization, historical priority, target construction or
exponent improvement is claimed.

```sh
python research/ai/2026-10-23-divisor-source-caps/verify.py
python -m unittest discover -s tests -p 'test_divisor_source_caps.py' -v
```

The finite controls contain110 determinant-one minors for every
nonseparable two-monomial biform at p=2,...,6, all330 residue identities
for those cases and d=1,2,3, all60 divisor/strip cases for a=2,...,24,
ten inherited A4 corollary cases and three local source pins. Acceptance
checks the exported minors using exact integer Bareiss determinants;
unit-pivot elimination is discovery only. Tests use a separate exact
backend for determinants and literal dense ranks, including crossed
and wrapped coordinate pairs. These finite ranges support rather than
replace the all-integer written argument.
