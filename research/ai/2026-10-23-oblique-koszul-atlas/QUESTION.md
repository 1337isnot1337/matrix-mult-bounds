# Fixed-residual Koszul screening

October 23, 2026. Owner-directed Codex research, started from the exact
construction checkpoint `29a486ac622261c8b4854fc109fb8ab40dcf91a2`
in pending PR147. This is a separate finite-method investigation; the
construction and equalizer proof retain their original attribution.

Question: can a full-space Koszul flattening on any leg, in any degree,
raise the known border-rank lower bound of twelve for the actual
`Q(6,4)` product-oblique residual? If that screen fails, examine stronger
exterior flattenings before trying another full-space Koszul degree.

Deliver exact integer coefficient matrices and complete rank decisions.
Use unit elimination when possible to retain every-characteristic scope.
Compare matrix rank divided by the exact rank-one divisor, rounded up,
with the existing bound. A modular rank alone is a rational lower bound,
not an upper bound or an all-characteristic rank certificate.

Keep the fixed source maps and the full residual. No conclusion about
other source maps, general Laurent degenerations, optimal border rank,
or an improved matrix multiplication exponent follows from a failed
flattening screen.

The main branch is `3008d704d1797da02f7bf3f29cc1dbd4c0e7fa93` at
selection. No open issue owns this question. PR147 owns the construction,
ordinary rank and equalizer bound; its preceding note gives an analytic
ceiling for the first-leg middle Koszul map but no complete all-leg atlas.
This continuation must be integrated after its prerequisite or retain an
explicit pinned dependency.
