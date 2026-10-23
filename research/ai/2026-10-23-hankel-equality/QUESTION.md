# Saturation below full Hankel rank

Base main: `1c04903`, October 23, 2026. Owner-directed Codex research.
Open issues and PRs were inspected before starting. The earlier rectangular
integration PR76 contains full-symbol-rank equality counterexamples and a
crossed-flattening equality theorem; those retain their credit.

Question: if a source slice attains `rank M_F = ab r` and its scalar
Hankel rank satisfies `r < min(a,b)`, must all its coefficient sequences
share one constant length-r scheme? The maintained proof treats r=2.
The written, unreviewed continuation uses both coefficient-map equalities and the
gcds of the two homogeneous Hankel kernels, without choosing a leading
minor or extending the statement to full symbol rank. Integer intermediate
ranks extend the result to the strict strip `rank M_F<ab*r+min(a,b)`.
The moving-support family in proof.md attains the strip boundary for all
r>=2, so no larger universal strict strip follows from this conclusion.

The application question is separate: when does this pointwise constraint
force a common scheme for an entire lifted Segre variety? This has not
been established. The historical A9 square-sum candidate (32,6,3) is
already excluded by the maintained Wronskian application and its credited
three-ruling bound; it is not an open target or a new exclusion here.
No target exclusion or smaller exponent follows merely from pointwise
saturation.
