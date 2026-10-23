# Two moving supporting variables: additive cost or counterexample

Base c0bf463, October 23, 2026. The mathematical sources of PR134 are
frozen while its final hosted checks run. This continuation uses a new
branch and does not change that auto-merge candidate.

Question: for deficient scalar Hankel rank r and primitive supporting
degrees (1,1), must full source rank be at least

    ab*r+a(a-r)+b(b-r)?

The preceding theorem proves only the maximum of the two extra costs.
Its forty-case pilot used constant initial moments. The next discovery
step varies the initial moments themselves, while checking the literal
source degrees and preserving exact arithmetic. A counterexample needs
an independently replayable characteristic-zero upper rank. Finite
nonviolations do not prove the inequality.

First bounded class: A(3,3), r=2, support V^2-xz U^2, with
f_0=g0, f_1=g1, f_2=xz*g0, f_3=xz*g1, f_4=x^2*z^2*g0.
Take g0 in {0,1} and g1=c0+cx*x+cz*z+cxz*xz with ternary coefficients,
excluding the all-zero slice. This gives 161 cases. Rank modulo32003
provides a rigorous characteristic-zero lower bound; any putative
violation is replayed over Q. The general complex four-parameter class
is a separate algebraic question.

The ordinary A9 square sums were already excluded by the credited
Wronskian application. This source-structure question does not reopen
those targets or imply a smaller exponent.

Completed here, as a written unreviewed theorem: the exact full-source
rank minimum over the entire binomial recurrence chart, including all
polynomial initial moments and every field. The residue/key formula and
torus degeneration are in proof.md. The primitive-degree-(1,1) problem
for arbitrary other supporting forms remains open.

Attempt ledger: the 161-case grid has zero modular violations and is
retained as finite discovery. A lexicographic constant-pivot trial in
the four-parameter g0=1 chart found only sixteen constant pivots, which
does not prove the required rank twenty-four. Its partial certificate
is retained as discovery-only data; no generic exclusion is inferred.
The proof instead uses the exact residue components and monomial limits.
