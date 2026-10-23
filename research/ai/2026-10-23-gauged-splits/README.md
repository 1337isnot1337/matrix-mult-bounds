# Six split deletions using positive tensor valuations

**Claim `AI-EXTERNAL-GAUGED-SPLIT-SEED-006`. Written proof, unreviewed.**

The pinned external rank-76 M(4,5,5) algorithm admits six simultaneous
split deletions under one physical stabilizer family. Two discarded
terms have poles in individual factors, but their rank-one tensors tend
to zero. The resulting 76-term border seed has 70 distinct first-leg
directions. Its full Laurent contraction is exact.

This construction demonstrates a strict advantage over the prior test
that required every discarded arrow to contract under a common physical
change without term gauges. A nonzero mixed trace rules out that stronger
condition for these six discarded triples. No rank record, Q(6,4) map,
or exponent improvement is supplied.

## 1. What must vanish

For a nonzero Laurent vector or matrix A, let v(A) be the minimum
exponent of its nonzero coordinate entries. For a nonzero rank-one
tensor A tensor B tensor C,

\[
v(A\otimes B\otimes C)=v(A)+v(B)+v(C).
\]

Each coefficient is a product of three factor coordinates. Choosing a
minimum-valuation coordinate on each leg attains the sum, so there is
no cancellation within this rank-one term. Thus a discarded term tends
to zero whenever the sum is positive, even if a factor has a pole.

This condition also has a factor-gauge interpretation. A term gauge
multiplies its three factors by powers whose exponent sum is zero; it
preserves the tensor term exactly. If integer factor valuations are
(a,b,c) with a+b+c>0, replace epsilon by t^3 and apply gauge exponents

\[
(1-3a,\ 1-3b,\ 3a+3b-2).
\]

They sum to zero. The new minimum valuations are
(1,1,3(a+b+c)-2), all positive. The gauge can differ from term to term.
This is more general than a single physical change applied to the
unscaled collection of all discarded arrows.

## 2. Six exact replacements

Start from the external integer factorization retained in
`../2026-10-21-external-grid-seed/factors.json`. Its conversion, authorship,
and license notice remain unchanged. Use the following zero-based rows:

| Changed term i | Retained U direction j | Coefficient c |
| ---: | ---: | ---: |
| 0 | 18 | -1 |
| 17 | 8 | 1 |
| 48 | 2 | -1 |
| 56 | 22 | -1 |
| 43 | 59 | -1 |
| 47 | 73 | 1 |

For each row use the exact identity

\[
U_i\otimes V_i\otimes W_i
=(cU_j)\otimes V_i\otimes W_i
 +(U_i-cU_j)\otimes V_i\otimes W_i.
\]

This gives 82 exact terms. Let S be the sum of the 76 retained terms and
D the sum of the six discarded terms. Then M=S+D. The six removed
directions are distinct and none is a destination j, so S has exactly
70 distinct U directions.

## 3. One physical family, with separate factor gauges

Use precisely the three unimodular physical bases and weights in the
[four-split construction](../2026-10-23-flip-escape/split_proof.md).
The retained base certificate is pinned by SHA-256 in `sources.json`.
For R=B_R diag(epsilon^r), and similarly S and T, the action is

\[
(U,V,W)\longmapsto(R^{-1}US,S^{-1}VT,T^{-1}WR).
\]

It fixes M(4,5,5). The minimum valuations of the discarded factors are:

| Original term index | v(U difference) | v(V) | v(W) | Tensor valuation |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 1 | 1 | 1 | 3 |
| 17 | 1 | 1 | 1 | 3 |
| 48 | 1 | 4 | 1 | 6 |
| 56 | 1 | 1 | 2 | 4 |
| 43 | -2 | 1 | 2 | 1 |
| 47 | 4 | -2 | 1 | 3 |

Every tensor valuation is positive. Therefore

\[
S(\epsilon)=M(4,5,5)-D(\epsilon)\longrightarrow M(4,5,5).
\]

For an explicit all-positive factor presentation after epsilon=t^3,
leave the first four term gauges equal to zero. The term at index 43
uses gauge exponents (7,-2,-5), giving factor valuations (1,1,1).
The term at index 47 uses (-11,7,4), giving (1,1,7). Both gauge triples
sum to zero, so they change no tensor coefficient.

## 4. Why the common unscaled arrow test misses this witness

Index the discarded terms in the order of the table, from zero to five.
The first U difference is U_0+U_18. Direct integer multiplication gives

\[
\operatorname{tr}\big((U_0+U_{18})\,V_{47}\,W_0\big)=1.
\]

This mixes the first discarded U and W arrows with the sixth discarded
V arrow. A common physical change preserves this trace. If every
unscaled arrow entry had positive valuation, the trace would tend to
zero, contradicting its value one. The simultaneous unscaled-arrow
contraction condition is therefore impossible for this exact batch.

Separate term gauges need not preserve this mixed trace because its
three factors come from different terms. They preserve each individual
rank-one tensor, which is exactly what the split identity requires.
The nonzero mixed trace thus proves that the new criterion is strictly
more permissive in this concrete example.

## 5. Complete certificate and reproduction

`certificate.json` contains all 76 surviving and six discarded Laurent
terms. Each factor coordinate is stored as a coordinate, a rational
coefficient string, and an integer exponent. The verifier reconstructs
the factors from the pinned source and physical matrices before checking
their contraction.

It verifies every one of the 10,000 constant tensor positions. Exactly
100 equal one and the other 9900 equal zero. There are no negative-degree
coefficients. The 73 nonzero positive-degree coefficients equal the negative
of the complete discarded tensor:

| Degree | Nonzero tensor coefficients |
| ---: | ---: |
| 1 | 4 |
| 3 | 9 |
| 4 | 6 |
| 5 | 2 |
| 6 | 13 |
| 7 | 8 |
| 8 | 1 |
| 9 | 14 |
| 10 | 7 |
| 12 | 6 |
| 13 | 2 |
| 15 | 1 |

Run from the repository root:

```sh
python research/ai/2026-10-23-gauged-splits/verify.py
python -m unittest discover -s tests -p test_gauged_split_seed.py -v
```

To regenerate the complete certificate separately:

```sh
python research/ai/2026-10-23-gauged-splits/verify.py --write-certificate /tmp/gauged_split_certificate.json
```

Only the Python standard library is needed. The exact small-matrix
helpers come from the preceding split package; the new verifier checks
the tensor-valuation condition and directly collects all Laurent
coefficients. The original four- and five-split acceptance fixtures
are not modified.

## 6. Scope and attribution

The external rank-76 exact algorithm already gives the same rank upper
bound. This is an explicit changed border seed. Its generic nonzero
parameter tensor has a nonzero remainder; it must not be treated as an
exact M(4,5,5) decomposition before the limit.

The unchanged W directions still exclude direct reuse without further
changes. The earlier fixed-direction certificates for standard flips
of the four- and five-split variants do not automatically apply to this
new component. Actual nine-group covers, simultaneous grid incidence,
and Q(6,4) maps are separate unresolved construction requirements.

Fawzi et al. retain credit for the matrix multiplication algorithm.
Dumitriu et al., arXiv:2610.13905v1, retain credit for the physical
nilpotent-factor deletion viewpoint. The six selected replacements,
their tensor-valuation replay, and the explicit separation from the
unscaled-arrow criterion are local owner-directed AI work. The
valuation and factor-gauge facts are elementary and are not claimed as
historically new. There is no independent review, formalization, rank
record, or exponent improvement.
