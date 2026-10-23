# Complete rank-six locus of the fixed-resolvent space

The rank-at-most-six locus in the fixed 112-dimensional space W is a
17-dimensional linear subspace. Every nonzero member has rank six and
the same six-dimensional image. For two rank109 compression maps, the
compression kernel has dimension at most one; both compressed dimensions
111 and 112 occur. The proof describes every nontrivial kernel/image pair.

These are written, computer-assisted and unreviewed matrix-space results
over every field. They do not establish a smaller exponent or a new
arbitrary-singular-degeneration exclusion.

## Reproduce

From the repository root, using only the Python standard library:

```sh
python research/ai/2026-10-23-resolvent-rank-six-locus/verify.py
python -m unittest discover -s tests -p test_resolvent_rank_six_locus.py -v
```

`proof.md` supplies the all-field classification and compression argument.
The standalone acceptance program reconstructs the source and verifies
26 integer triangular seven-minor identities, the original-coordinate
eliminations and the five-generator polynomial normal form. It checks
sharp compression examples over Q, F2, F3 and F1009. Those four controls
do not replace the all-field written proof.

`sources.json` pins the predecessor formulas and preserves attribution.
`claims.json` mirrors the two new root-ledger claims. `manifest.json`
hashes the certificate and recorded report under
`results/resolvent-rank-six-locus-2026-10-23/`.
The initial question remains in `QUESTION.md` as a discovery checkpoint;
its four-parameter guess is superseded by the complete five-parameter
mixed-block classification, including the exceptional cancellation.

Prepared with OpenAI Codex under owner direction. PR139 supplies the
fixed space and previous minimum-rank result; PR103 and the earlier
cyclic-source packages retain their original credits. No historical
priority, independent review or formalization is claimed.
