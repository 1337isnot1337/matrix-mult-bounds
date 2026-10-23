# Independent ordered monomial audit

This R6 continuation independently checks the exact support certificates in
[PR118](https://github.com/1337isnot1337/matrix-mult-bounds/pull/118) at
`019269fad70d78845627e91eafe10b4063e3890c` and extends the historical exhaustive
searches to both orders of the input dimensions. The historical archives and
PR118's producer are unchanged. This is a finite computational audit, not an
independent review of the underlying spectral inequalities.

## Why the omitted orientation matters

The archived note explicitly restricts exhaustive weights to `2<=a<=b`.
PR118 retains that generator, although its README scope table omits `a<=b`.
The source profile is symmetric, but the score groups terms by their second
and third coordinates, retaining the first coordinate as the shared leg.
Consequently input exchange need not preserve this score.

For example, `x=(0,0), y=(0,1,1,0)` gives three recognized convolution sectors,
each worth 2, with source score 6 and ratio 1. Exchanging the arrays gives a
single unrecognized sector whose slice lower bound is 3, hence ratio 1/2.
This is a difference between the implemented lower bounds; it does not assert
that the tensors have unequal intrinsic spectral values.

The [recognition lemma](recognition.md) proves that sorting and axis reversals
already detect every exact convolution obtainable by arbitrary coordinate
relabeling inside the integer addition support. Its elementary proof covers
all sizes, including nonuniform singleton-axis labels. A separate brute-force
check tests every coordinate bijection for all 511 nonempty subsets of C(3,3).
The written proof is unreviewed. A stronger bound on a rejected sector must
use something beyond relabeling it as one complete convolution.

## Independent certificate replay

`check.py` reconstructs diagonals, flood-fills adjacency of the zero terms,
tests literal set equality with each candidate convolution support, and
computes the profile from its exact product formula. It imports neither the
archive search nor PR118's implementation. All 20 retained records in each
of PR118's binary, ternary and random reports match this implementation.

`results/ordered-monomial-audit-2026-10-23/reviewed-records.json` retains the
original report hashes, each record's normalized weights, and SHA-256 of
its canonical JSON (`sort_keys=True, separators=(",", ":")`). The regression
test reconstructs all 60 records and compares these digests. The commit,
source blobs and source file hashes are recorded in `sources.json`.

This replay checks retained witnesses, not every candidate or the reported
maxima of the random search. The new exhaustive censuses below separately
recompute every candidate within their declared scopes.

## Ordered exhaustive scopes

For alphabet size q and ordered dimensions `(a,b)`, the exact number of
normalized weight pairs is

`(q^a-(q-1)^a) * (q^b-(q-1)^b)`.

The census uses every `a,b>=2` with `a+b<=N`; it does not quotient by input
exchange. Each dimension pair is checked against that count. The report
records separate historical `a<=b` and additional `a>b` counts, violation
counts, and exact best and best nontrivial witnesses for every dimension.
Here nontrivial means more than one sector, as in the historical search.

Both censuses completed with no scored violation. The best ratio and best
nontrivial ratio are exactly 1 in each full scope.

| Alphabet | N | Historical a<=b | Additional a>b | Complete ordered scope |
| --- | ---: | ---: | ---: | ---: |
| Binary | 11 | 12,976 | 11,732 | 24,708 |
| Ternary | 10 | 209,692 | 160,560 | 370,252 |

The combined scope is 394,960 candidate cases, including 172,292 additional
cases. These are candidate counts, not distinct tensor-isomorphism classes.
The exact reports are in `results/ordered-monomial-audit-2026-10-23/`.

## Reproduction

From the repository root, using Python 3.10 or later:

```sh
python research/ai/2026-10-23-ordered-monomial-audit/check.py --alphabet-size 2 --max-sum 11 --output results/local/ordered-binary.json
python research/ai/2026-10-23-ordered-monomial-audit/check.py --alphabet-size 3 --max-sum 10 --output results/local/ordered-ternary.json
python -m unittest discover -s tests -p test_ordered_monomial_audit.py -v
```

The standalone `--report PATH` mode also checks the retained records in an
original PR118 report. Obtain that report from the exact commit recorded
above, not a moving branch. The package and routine tests do not need that
unmerged branch to be installed.

Routine tests verify retained record digests, tampering rejection, explicit
orientation asymmetry, full small-scope enumeration, saved coverage counts,
every saved per-dimension maximum witness, and recognition against all
coordinate bijections on 511 supports. All eight focused tests pass.
Reproducing the *maximality*
claims requires the two exhaustive commands; witness replay alone does not
establish maximality.

The profile and sector model retain the archive's attribution. This audit
does not exhaust arbitrary integer weights, stronger lower bounds on the
unrecognized sectors, general basis changes, tensor powers, or cancellation
methods. It does not produce a tensor character or improve the exponent.
