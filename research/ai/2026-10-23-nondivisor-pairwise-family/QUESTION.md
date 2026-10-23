# A uniform failure of pairwise source-rank screening

October23,2026. Branch `research/nondivisor-pairwise-family-20261023`.
Base main`3008d704d1797da02f7bf3f29cc1dbd4c0e7fa93`.

PR148 leaves nondivisor widths unclassified; PR171 explains their exact
two-monomial rank deficit. Can a support pass every coordinate-pair
rank test but fail the same rank ceiling at a higher-support slice?
The live inventory has no such family; PR157's locally Toeplitz repair
and PR185's saved-target screen have separate scopes.

Proposed family: d>=2,a=2d+1,T=a(a+d). Let S have the ad coordinates
x^i z^s for i<d,s<a and the extra coordinate x^d z^d. Every coordinate
pair has a source entry cover of size at most T-1, yet S contains
(1+xz)^d, whose active biform matrix should have full rank T over C.

Prove the binomial Toeplitz determinant product and its literal source
block decomposition. Verify all pair covers, include a positive-
characteristic negative control, and distinguish failure of a pairwise
method from a counterexample to any dimension-cap formula. This is
independent of PR148's running validation and supplies no matrix target
or exponent improvement.
