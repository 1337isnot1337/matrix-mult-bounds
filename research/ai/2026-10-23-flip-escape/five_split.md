# A second exact seed from five simultaneous splits

This is a second witness under claim
`AI-EXTERNAL-SPLIT-BORDER-SEED-002`. It applies the construction proved
in [the four-split note](split_proof.md) to five terms. The original
four-split certificate is retained byte-for-byte.

Use these zero-based replacements, with the same rule
U_i = c U_j + (U_i-c U_j):

| Changed index i | Retained direction j | Coefficient c |
| ---: | ---: | ---: |
| 16 | 57 | 1 |
| 47 | 52 | -1 |
| 31 | 48 | -1 |
| 26 | 32 | 1 |
| 54 | 60 | -1 |

The exact intermediate decomposition has 81 terms. The common descending
image flag of the five discarded triples has dimensions

\[
(4,5,5),\ (4,4,4),\ (2,4,4),\ (2,4,1),\ (2,1,1),
\ (1,1,1),\ (1,1,0),\ (1,0,0),\ (0,0,0).
\]

The rational adapted-basis construction gives unimodular physical bases
with determinants (1,1,-1). All basis entries and surviving factors are
exported in `five_split_certificate.json`. Their column weights are

\[
r=(-7,-4,-1,-1),\quad
s=(-6,-3,-3,-3,0),\quad
t=(-5,-2,-2,-2,0).
\]

Every entry of every discarded factor has positive valuation. The
same physical-action argument therefore gives a 76-term Laurent
decomposition whose limit is M(4,5,5). It has 71 distinct first-leg
directions over Q(epsilon), since five directions were replaced by
directions that remain present.

The complete contraction has no negative-degree coefficients. Its
constant part has exactly the 100 required unit coefficients, and all
other 9900 constant positions are zero. Its positive remainder has
172 nonzero coefficients:

| Degree | Nonzero tensor coefficients |
| ---: | ---: |
| 3 | 44 |
| 5 | 23 |
| 6 | 42 |
| 8 | 17 |
| 9 | 23 |
| 11 | 11 |
| 12 | 7 |
| 14 | 4 |
| 15 | 1 |

The verifier also checks that this remainder is the negative of the
complete discarded tensor. No numerical fit is an acceptance premise.

## Reproduction

```sh
python research/ai/2026-10-23-flip-escape/verify_split.py --variant five
python -m unittest discover -s tests -p test_split_border_seed.py -v
```

The same standard-library verifier accepts only the two named variants,
their stated schema, source hash, and fixed conservative scope. Seven
focused tests cover both variants, exact finite-parameter split identities,
coefficient and valuation mutations, and schema/scope/variant mutations.

## Consequence and scope

The five replacements create different shared-U pairs from the earlier
four-split seed. Further exact flips may use those pairs to change W
directions while preserving the complete approximate tensor family.
The full Laurent remainder must continue to be accounted for.

This seed keeps all the original W directions. The
[weighted grid certificate](../2026-10-23-grid-escape/README.md)
therefore still excludes its termwise assignment to the specified
Q(6,4) evaluation grid. Fewer first-leg directions do not establish the
simultaneous incidence conditions.

The witness was selected by a finite candidate and compatibility search.
This note makes no maximum-batch or search-optimality claim. The exact
five-term witness is verified directly and does not depend on the
search's modular filters or branch pruning. The external algorithm and
nilpotent-factor deletion method retain the attribution in `sources.json`.
There is no new rank record, Q(6,4) map, exponent improvement, independent
review, or formalization.
