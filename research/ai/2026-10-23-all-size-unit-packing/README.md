# Disjoint source units and sharp singular-space caps for every size

For every a>=1, the balanced cyclic source of dimension
`N=a^2(2a-1)` has a^2 disjoint coordinate supports each carrying a
unimodular matrix slice. The [written proof](proof.md) works over every
field, including characteristics dividing a, using a polynomial kernel
recurrence and degree bounds. It requires no roots of unity or division
by a.

Over C the resulting sharp cap is

```
max dim{linear W: every source slice in W is singular} = a^2(2a-2).
```

The elementary distinct-weight limit from the A4 predecessor transfers
the coordinate packing to every dense complex linear subspace. A zero-row
kernel attains the cap. This closes the all-size source packing question;
larger finite packing searches are unnecessary for this source family.

The theorem is **written and unreviewed**. It does not supply regularity
or partial frames for arbitrary target degenerations. No target map,
independent review, formalization or exponent improvement is claimed.
The original cyclic source, earlier unit and A4 packing proofs retain
their credit and exact pins. The recurrence and all-size continuation
are owner-directed OpenAI Codex work, with no new external theorem.

```sh
python research/ai/2026-10-23-all-size-unit-packing/verify.py
python -m unittest discover -s tests -p test_all_size_unit_packing.py -v
```

Use root requirements from the repository root. The finite replay checks
21 exact short-matrix integer determinants througha6,63 independent
modular determinants overF2,F3,F5,70 formal successive-equation identities
and packing/sharp-kernel bookkeeping througha12. It also replays the A4
predecessor. These are finite proof-data controls. The all-size,
all-field and all-complex-subspace quantifiers come from the written
polynomial and diagonal-limit arguments, not extrapolation of the table.

Claims: `AI-ALL-SIZE-RESIDUE-UNITS-001` and
`AI-ALL-SIZE-SINGULAR-CAP-002`.
