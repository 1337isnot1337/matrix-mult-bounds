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


## Smaller canonical five-, six-, and seven-sector constructions

Literal integer block factors and moments now prove

\[
C(6,16)\unrhd T_5,\qquad
C(7,24)\unrhd T_6,\qquad
C(8,34)\unrhd T_7
\]

over every field. These reduce the long source dimension of the previous
five- and six-sector certificates from20 to16 and from28 to24, respectively.
They also identify all sectors in one canonical shared basis.

| Target | Source | All coefficient positions | Negative zeros | Constant positions | Target monomials | Largest map entry in absolute value |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| T4 | C(5,10) | 400 | 60 | 80 | 20 | 6 |
| T5 | C(6,16) | 1125 | 175 | 175 | 35 | 1 |
| T6 | C(7,24) | 2646 | 420 | 336 | 56 | 5 |
| T7 | C(8,34) | 5488 | 882 | 588 | 84 | 2 |

The source convention and degree weights are the same as above, with
shared weight1-m. For m=5,6,7 let J=(0,1,3,...,m) and
\(\nu_d=\mathbf1_{d=m-1}-\mathbf1_{d=m}\).
The displayed data in `construct_larger.py` give factors g_p and moments
z_q satisfying

\[
\sum_j g_p[j]z_q[j+\ell]=
\begin{cases}
0 & p+q<m-1,\
\nu_\ell & p+q=m-1
\end{cases}
\qquad (\ell\in J+\{0,\ldots,p+q\}).
\]

There are129,216,335 scalar equations at the respective sizes. The Y row
with first index k in degree p is \(t^k g_p\). The Z row with first
index k in degree q is the corresponding consecutive window of z_q.

Before normalization, each matched block has the common shared Hankel
matrix \(H_{i,r}=\nu_{J_i+r}\). Its determinant is-1,-1,1 at sizes5,6,7.
The shared source map has columns J equal to H inverse and its remaining
column zero. Thus the zero-degree block coefficients become exactly
\(\mathbf1_{i=a+c}\), and the negative-degree coefficients stay zero.
This is a direct proof of each canonical degeneration from the finite
integer equations. The constructor uses only unit pivots and integer
output coefficients.

The frozen maps are
[m5](../../../results/canonical-moment-flags-2026-10-21/m5-integer-witness.json),
[m6](../../../results/canonical-moment-flags-2026-10-21/m6-integer-witness.json), and
[m7](../../../results/canonical-moment-flags-2026-10-21/m7-integer-witness.json).
Their adjacent verification reports contain complete coefficient counts
and SHA-256 hashes. Reconstruct or verify a size by replacing the argument
in the following commands:

```sh
python research/ai/2026-10-21-canonical-moment-flags/construct_larger.py --m 6 --output results/local/t6-integer.json
python research/ai/2026-10-21-canonical-moment-flags/verify_witness.py results/canonical-moment-flags-2026-10-21/m6-integer-witness.json
```

A recovered prose list once shifted the last m6 moment by one position.
The independent source replay rejected that list. The frozen data contain
the corrected moment with entries+1 at index26 and-1 at index27, and the
complete integer replay passes. Source reconstruction and literal replay
are separate checks.

Across the four sizes, every one of9,659 coefficient positions is checked.
The finite lengths10,16,24,34 happen to fit m^2-3m+6. No continuation of that
pattern is asserted; even that quadratic pattern, if continued, would
have asymptotic long-leg cost2 and would not prove the required cost-one
family. These are finite constructive improvements, with no new exponent.

The restored m5,m6,m7 fixtures were regenerated from compact signed
polynomials and replayed independently in JavaScript with exact integer
arithmetic. After local execution was restored, the separate Python
constructors and full-source verifier reproduced all four frozen witnesses
and reports. All three regression tests passed, including both damaged-map
controls. The exact checkpoint and commands are recorded in the
[Python replay receipt](../../../results/canonical-moment-flags-2026-10-21/restored-python-replay.json).
The source maps, their proof, and all same-session checks remain externally
unreviewed.

The focused acceptance and corruption checks run with:

```sh
python -m unittest discover -s tests -p test_canonical_moment_flags.py -v
```

## Scope and provenance

Claim `AI-CANONICAL-INTEGER-FLAGS-001` is written and externally unreviewed.
The construction and its checks are AI-derived work within the same
owner-directed research session. They supply no independent mathematical
review or formalization and carry no historical priority claim.

The [matched-sector character criterion](../2026-10-20-construction-sprint/independent_sector_bases.md)
still requires an unbounded family with the stated asymptotic source
dimensions. This finite witness does not supply that premise.
