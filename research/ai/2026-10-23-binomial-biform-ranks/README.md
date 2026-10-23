# Exact binomial biform ranks

For either orientation of a two-monomial biform, nonzero coefficients
over any field, and positive offsets u,v<a, the [written proof](proof.md)
gives

    rank R_a=a^2+sum_(i,j) min(n_i,m_j),

where n_i and m_j are the input residue lengths modulo u and v. For
u=v=d and a=q*d+r this becomes

    rank R_a=a^2+a*d-r*(d-r).

An elementary path-matrix argument proves every rectangular block has
rank bc+min(b,c). No splitting or classification theorem is imported.
The bound rank R_a>=a^2+a can replace the binomial input to PR148's
divisor proof; any dependency amendment to that package is separate and
must preserve the broader biform theorem's original credit.

Claims `AI-BINOMIAL-BIFORM-RANK-001` and
`AI-BINOMIAL-ELEMENTARY-GAP-002` are written and unreviewed. No independent
review, formalization, historical priority, source-space cap at nondivisor
widths, matrix construction or exponent improvement is claimed.

```sh
python research/ai/2026-10-23-binomial-biform-ranks/verify.py
python -m unittest discover -s tests -p 'test_binomial_biform_ranks.py' -v
```

The report exports114 full-rank unimodular minors with row/column covers:
both orientations for every offset at a=2,...,6, plus the a7 equal-offset
cases d=2,3. Acceptance directly checks each determinant and every
literal covered entry. Exact row reduction only discovers the lower
minor. Arithmetic controls check8555 lower-gap cases and435 quotient/
remainder identities through a30, separately from matrix certificates.
Tests additionally inspect weighted rational matrices, prime fields2,3,5,
symbolic weighted minor monomials, tampering and exact source pins.
These are finite controls for the all-size unreviewed proof.
