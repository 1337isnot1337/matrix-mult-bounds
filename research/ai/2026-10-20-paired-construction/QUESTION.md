# Construct a graded degeneration for the new paired target

Owner: the source-verification and construction worker, October 20, 2026.
Base inspected: `75bf6a3`. No smaller exponent is established.

**Constructive checkpoint, October 21.** A separate unrestricted search
yielded an exact `P_2 -> M(2,2,2)` restriction. Its quotient proof extends
to `P_a -> M(a,2,a)` for all `a >= 2`, with explicit integer maps and
telescoping cancellation. See `README.md`, `chain_family.py`, and the
full coefficient certificates. This family does not cross the exponent
gate. The original paired target below remains unconstructed.

The concurrent paired-direct-sums worker found that

    P_10 -> M(4,11,10) direct_sum M(10,12,6)

passes every first-leg Koszul rank comparison. Its coefficient identity is
unconstructed. The source and conditional exponent implication belong to
that worker's package and the earlier paired-sources package.

This lane investigates an explicit Cartan-graded basis search for that
target. A grading allocation alone is insufficient: all tensor coefficients
and their vanishing orders must eventually be checked. Numerical fits are
discovery records, never accepted degeneration certificates.

The source has coordinates A_(p,q), B_(y,j), C_(z,v), and terms
A_(p,q) B_(y,q+v) C_(p+y,v), with p,q,y,v in {0,...,a-1}.
Use weights p+q, y+2a-2-j, and 2a-2-z+v respectively. Every term has
total weight 4a-4. The target uses vertex weights alpha,beta,gamma and
leg weights alpha+gamma, beta-alpha, 4a-4-beta-gamma.

The finite allocation in `graded_search.py` uses the entire first source
space and fits both long-leg multiplicity profiles. It permits a numerical
search using only matrices within equal-weight subspaces. A successful
fit would still need exact recovery of a Laurent family and independent
coefficient verification.
