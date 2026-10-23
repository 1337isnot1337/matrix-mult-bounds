# Exact two-monomial biform ranks

October23,2026. Branch `research/binomial-biform-ranks-20261023`.
Base main`3008d704d1797da02f7bf3f29cc1dbd4c0e7fa93`.

PR148's divisor theorem and exact a5,d2 boundary motivate this question:
determine rank R_a(g) for g=alpha+beta*x^u*z^v and
g=alpha*x^u+beta*z^v, with1<=u,v<a and nonzero coefficients, uniformly
over all fields. The live open-PR inventory has no separate binomial-rank
investigation. Keep the published divisor theorem's validation head fixed.

Proposed formula: partition the a input indices modulo u and v into
lengths n_i and m_j. The rank is a^2+sum_(i,j) min(n_i,m_j). For u=v=d,
writing a=q*d+r gives a^2+a*d-r*(d-r). Unequal residue lengths explain
the nondivisor deficit without refuting a source-space dimension cap.

Prove the rectangular path-matrix ranks, including all characteristics,
and export exact lower minors plus row/column covers. The formula would
replace the bundle-splitting input for the binomial step in PR148;
that dependency amendment must be explicit rather than silently changing
its status. No matrix target or smaller exponent is supplied.
