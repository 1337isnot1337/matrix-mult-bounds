# Pruning smaller centered targets

October 23, 2026. Owner-directed OpenAI Codex research. Written and unreviewed.

The [proof](proof.md) gives a concrete pruned rectangular construction
and a broader reason that this family of modifications cannot reach
the repository's exponent target.

**Construction.** A product-dependent restriction of the credited
external general22 family gives 22 independent products, each of volume
n^5, with border-rank budget

\[
4n^5+32n^4+102n^3+158n^2+118n+34\qquad(n\ge2).
\]

The ordered matrix shapes and the complete [witness](witness.json) are
explicit. This budget is below the classical upper bound 22n^5 for all
n>=4, by an exact positive-coefficient identity after n=4+u. Both leading
and correction positions are counted after zero forms are omitted.
The statement concerns border rank over characteristic-zero fields;
it does not promise a finite-precision running time.

**Limitation.** If every target coordinate of dimension m has at least
m+1 rows where both active factor maps are nonzero, even a pruned leading
grid costs at least

\[
(4/3^{3/4})^d\max_t(A_tB_tC_t)^{3/4}.
\]

This exceeds the whole 9/4 target mass whenever
`p^4*3^(3d)<4^(4d)`. It covers arbitrary product-dependent dimensions,
support positions, mixed ordered shapes, and scalar gradings. It applies
to the external 10-, 13-, and 22-product examples and the local 29- and
106-product families. The precise cost model deletes zero forms before
counting positions. Reweighting, cancellation between nonzero positions,
or a new rank decomposition are outside this result.

The explicitly tested alternative `[I;-1;0]`, `[I;0;-1]` has only m common
rows and escapes that premise. Six small modular discovery systems for
that alternative did not produce a competitive cost. They do not prove
characteristic-zero nonexistence or optimization. That finite search is
stopped here.

## Exact acceptance

```sh
python research/ai/2026-10-23-aggregation-families/pruned/verify.py
python -m unittest discover -s tests -p test_aggregation_pruned.py -v
```

The standard-library verifier checks raw source hashes, all 13,845 mixed
triples in the three external examples, every supplied scalar grade and
correction, all high-coordinate types for five saved profiles, and the
strict integer cost floors. Direct small-grid enumeration independently
checks the position counts. All-n formulas follow from the written
coordinate factorization and the complete finite source certificate.
Neither numerical optimization nor a sampled tensor residual is an
acceptance premise.

The [validation receipt](validation/report.json) and
[focused log](validation/focused.log) combine 912 unchanged prior test
successes with six new tests and the two rerun ledger/link checks,
covering all 920 discovered IDs. Existing code, witnesses and archives
are unchanged. The earlier five passed archive replays are retained.
This is baseline-plus-delta coverage, not a new full-suite run.

The [report](report.json) records exact all-n polynomials, target shapes,
and rational intervals for the critical mass. The
[discovery record](discovery/README.md) keeps attempted searches separate
from that acceptance. Sources and raw-byte pins are in
[sources.json](sources.json). Solomonik and Blaeser,
[arXiv:2610.26563v2](https://arxiv.org/html/2610.26563v2), retain credit
for the aggregation mechanism and the three graded families.

The prior [rectangular complete-grid result](../rectangular/README.md)
has narrower shape hypotheses. The new common-support argument permits
mixed graded shapes and genuinely smaller leading grids, while retaining
its explicit local-support and position-count restrictions. No lower
bound on actual tensor rank, historical priority, independent review,
formalization, or smaller matrix multiplication exponent is claimed.
