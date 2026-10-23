# Ordered-input monomial score census

Question R6: does the historical `a <= b` inventory cover both shared-input
roles, and what changes when the missing ordered dimensions are searched?

It does not cover them. The [all-size support argument](proof.md) gives
weights of lengths `3,2m` whose target score rises from `max(3,m)+1` to
`2m+1` when swapped, for every `m >= 2`. This disproves pointwise dominance
of the chosen orientation. It does not disprove equality of global maxima.

The completed census visits every ordered `a,b >= 2` with the stated sum
limit, using weights in the stated alphabet and minimum zero in each input.
Every ordering and acceptance decision uses exact rational arithmetic.

| Alphabet and limit | Historical `a <= b` | Added `a > b` | Ordered total | Maximum ratio |
| --- | ---: | ---: | ---: | ---: |
| `{0,1}`, `a+b <= 11` | 12,976 | 11,732 | 24,708 | 1 |
| `{0,1,2}`, `a+b <= 10` | 209,692 | 160,560 | 370,252 | 1 |

No score exceeds the source profile. Among unequal-length swaps:

| Alphabet | Historical orientation better | Added orientation better | Equal |
| --- | ---: | ---: | ---: |
| Binary | 7,932 | 810 | 2,990 |
| Ternary | 107,629 | 10,975 | 41,956 |

The additional cases are 172,292 candidate visits across the two nested
alphabets, not a count of distinct supports or tensor isomorphism classes.
The results retain five leaders per orientation class and the first exact
witness of each strict swap direction. Reports also contain counts, maxima
and violation counts for each ordered dimension pair.

## Evidence and reproduction

`search.py` reuses only the unchanged, hash-pinned historical support and
block-discovery functions. PR118 retains credit for the maintained exact
ranking search and its prior input-role warning; this package neither
imports its unmerged code nor changes its historical-scope results.

`verify.py` imports no discovery code. It rebuilds diagonal minima, finds
components by graph traversal, compares whole Cartesian convolution
supports, and evaluates the profile with a direct rational product formula.
It checks all 28 retained records and the closed count formula

    sum (q^a-(q-1)^a) (q^b-(q-1)^b)

over the declared ordered dimensions. The count identity alone does not
certify the executed census or global maxima; those require the completed
search replay. The verifier explicitly reports that boundary. The tests
also compare all 190 binary candidates with `a+b <= 6`, reject corrupted
support/partition/block/score and coverage records, and check the all-size
family at `m=2,...,12`.

Run from the repository root, using Python 3.10 or later:

```sh
python research/ai/2026-10-23-ordered-monomial-search/search.py --alphabet-size 2 --max-sum 11 --output results/ordered-monomial-search-2026-10-23/binary.json
python research/ai/2026-10-23-ordered-monomial-search/search.py --alphabet-size 3 --max-sum 10 --output results/ordered-monomial-search-2026-10-23/ternary.json
python research/ai/2026-10-23-ordered-monomial-search/verify.py results/ordered-monomial-search-2026-10-23/binary.json results/ordered-monomial-search-2026-10-23/ternary.json
python -m unittest discover -s tests -p test_ordered_monomial_search.py -v
```

The full regression and historical replay are additional repository merge
gates. The initial focused run before the ternary report finished failed
only because that report was not yet present; it is not a passed run.

## Scope and next question

`AI-ORDERED-SCORE-ASYMMETRY-001` is a written unreviewed score calculation;
`EXP-ORDERED-MONOMIAL-CENSUS-001` is a finite experiment. Separate code is
not independent mathematical review. No exponent improvement is claimed.
The alphabets, dimensions and current fallback score remain finite/restricted.
This package does not exhaust arbitrary integer weights, output-shared
partitions, arbitrary bases, tensor powers or stronger block estimates.

Do not repeat these exact inventories as new research. A useful next step
would change the recognition bound or examine a shared-axis class absent
from both input orientations, with separate scope and acceptance evidence.
