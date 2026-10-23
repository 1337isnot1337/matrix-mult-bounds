# Saturation below full Hankel rank

Base main: `1c04903`, October 23, 2026. Owner-directed Codex research.
Open issues and PRs were inspected before starting. The earlier rectangular
integration PR76 contains full-symbol-rank equality counterexamples and a
crossed-flattening equality theorem; those retain their credit.

Question: if a source slice attains `rank M_F = ab r` and its scalar
Hankel rank satisfies `r < min(a,b)`, must all its coefficient sequences
share one constant length-r scheme? The maintained proof treats r=2.
The completed written, unreviewed continuation uses both coefficient-map equalities and the
gcds of the two homogeneous Hankel kernels, without choosing a leading
minor or extending the statement to full symbol rank. Integer intermediate
ranks extend the result to the strict strip `rank M_F<ab*r+min(a,b)`.
The moving-support family in proof.md attains the strip boundary for all
r>=2, so no larger universal strict strip follows from this conclusion.

The application question is separate: does this pointwise constraint
help exclude the A9 square-sum candidate (32,6,3)? A common scheme for
an entire lifted Segre variety has not been established. No target
exclusion or smaller exponent follows merely from pointwise saturation.
