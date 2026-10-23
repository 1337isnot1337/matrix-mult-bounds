# Next question: full-window variable coefficients

The written proper-shift-window theorem in `proof.md` excludes one variable bulk long-leg map with common channel-window span of dimension below m, while the other map is Toeplitz. Polynomial degrees at most m-2, shared constant-coefficient recurrences of order below m, and low-total-multiplicity exponential polynomials all fall into this class. The result is only about ordinary restrictions and is unreviewed.

**Next precise construction target:** for Q(6,4), exhibit exact B bulk coefficients whose four-shift windows have full span K^4, keep the C bulk Toeplitz (or explicitly justify a second variable leg), and solve the full coefficient equations for a correction to M(5,4,5). Record the correction's actual tensor/border rank, then determine whether an unbounded fixed-width family has total correction cost o(n^(3/2)). Passing this necessary window-span test is not sufficient. PR #145 (diagonal shift) and PR #147 (product-long-map residual) own separate charts; do not duplicate them.

A separate theorem target is to allow a moving basis W_q and derive a lower bound from its rate of variation, without incorrectly replacing a collection of rank-(m-1) local matrices by one globally rank-(m-1) sum. Singular Laurent maps remain outside this ordinary theorem. There is no exponent improvement.
