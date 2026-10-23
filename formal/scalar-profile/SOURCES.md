# Source map

The checked lemma is an auxiliary result for the local scalar-profile argument
in [`research_note.md`](../../research/ai/2026-10-20/research_note.md).

| Lean declaration | Source statement | Scope |
| --- | --- | --- |
| `DiscreteConcave` | (S2), lines 47–50 | One fixed row, rewritten as nonincreasing consecutive increments. |
| `TriplingAt` | (S3), lines 52–54 | One fixed row and one positive starting index. |
| `finite_tripling_slope_bound` | Section 2.2, lines 190–203 | Finite cross-multiplied slope bound; it replaces the limit step only. |

The source note remains unchanged. This Lean project does not formalize the
remaining recurrence, pointwise-minimality argument, or tensor consequences.
