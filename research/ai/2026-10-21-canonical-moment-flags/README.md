# Integer canonical moment flags

October 21, 2026. This package records exact finite constructions. It does
not establish an exponent below 9/4 or an unbounded source-cost estimate.

## A canonical four-sector construction over every field

There are integer Laurent maps giving

\[
C(5,10)\unrhd T_4,\qquad
T_4=\sum_{a+b+c+d=3} X_{a+c}Y_{a,b}Z_{c,d}.
\]

Every map entry has absolute value at most six. The identity therefore
specializes to every field. It strengthens the earlier
[rational T4 construction](../2026-10-21-rectangular-t4-certificate/rational_flag_construction.md)
by giving integer maps; it is a construction of the same finite target.

Use the original source convention
\(C(a,b)=\sum_{i<a,j<b}x_i y_j z_{i+j}\).
Rows on each nonshared target leg are ordered by total degree p and then
by the first index k=0,...,p. The four source polynomials on the shared
leg are

\[
t^4,\quad t^3-t^4,\quad -1+t,\quad 1.
\]

The Y rows in degree p are \(t^k g_p\), where

\[
g_0=t^8(1-t),\quad
g_1=1-t^5-t^8,\quad
g_2=t^3(1-t),\quad
g_3=1-t^3-t^6.
\]

For each p, the Z row k is the length-14 window beginning at position k
of the integer moment sequence exported in the witness. All those
sequences are also displayed literally in `construct_t4.py`.
No inverse, root choice, or numerical solve is needed to reconstruct
the maps.

Give every shared row weight -3, and every Y and Z row in degree p
weight p. Thus a coefficient at degrees p,q has Laurent exponent
p+q-3. Direct substitution of all fifty original source monomials gives:

| Coefficient class | Positions checked | Result |
| --- | ---: | --- |
| Negative powers | 60 | All zero |
| Degree zero | 80 | Exactly the twenty monomials of T4 |
| Positive powers | 260 | 139 nonzero terms, at degrees 1, 2, or 3 |

Consequently the constant term is exactly T4 and the entire negative
part vanishes. This proves the displayed degeneration. All identities
are in the integer polynomial ring, so characteristic-zero lifting is
unnecessary. The rational map ranks are 4,10,10; conciseness of the
specialized target also forces the needed map ranks over every field.

## Independent verification

`verify_witness.py` uses only integer arithmetic for the coefficient
expansion and the standard-library Fraction type for an auxiliary rank
check. It does not use the block-factor equations, moment identities,
or a solver from the discovery process. It recomputes every source
contraction in all 400 target coefficient positions.

From the repository root:

```sh
python research/ai/2026-10-21-canonical-moment-flags/construct_t4.py --output results/local/t4-integer.json
python research/ai/2026-10-21-canonical-moment-flags/verify_witness.py results/canonical-moment-flags-2026-10-21/m4-integer-witness.json
python -m unittest discover -s tests -p test_canonical_moment_flags.py -v
```

Create `results/local/` first if it does not already exist. The
[frozen witness](../../../results/canonical-moment-flags-2026-10-21/m4-integer-witness.json)
and [exact replay](../../../results/canonical-moment-flags-2026-10-21/m4-integer-verification.json)
are sufficient for the finite claim.

The first discovery used finite-field block equations, followed by an
integer sign reconstruction. The published certificate is the integer
identity itself. Python and a separately written JavaScript expansion
agree on every coefficient and all remainder counts.

## Scope and provenance

Claim `AI-CANONICAL-INTEGER-FLAGS-001` is written and externally unreviewed.
The construction and its checks are AI-derived work within the same
owner-directed research session. They supply no independent mathematical
review or formalization and carry no historical priority claim.

The [matched-sector character criterion](../2026-10-20-construction-sprint/independent_sector_bases.md)
still requires an unbounded family with the stated asymptotic source
dimensions. This finite witness does not supply that premise.
