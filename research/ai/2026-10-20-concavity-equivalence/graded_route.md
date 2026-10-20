# Graded coefficient identities for singular degenerations

The intended certificate has constant rational matrices P, Q, G and integer
weights. For the source `C(a,B)`, let S_i be its `(B+a-1)`-by-B shift matrices.
The transformed coefficients are

    M_i = Q (sum_h G[i,h] S_h) P.

Let target Y and Z coordinates have degrees 0,...,a-1, with degree d occurring
d+1 times. Require M_i[z,y] to be zero when `deg(y)+deg(z)<a-1`, and to equal
the canonical T_a coefficient when equality holds. Entries with larger total
degree are free. Weights `deg(y)` on Y and `deg(z)-(a-1)` on Z then give a
genuine degeneration with constant term T_a and no negative powers. The
coefficient matrices and all required zeros must be checked exactly.

The initial programs fixed G=I. That restricted class is now closed at the
desired cost by the concurrent catalecticant obstruction. The next selected
experiment makes G arbitrary and requires it invertible. This is distinct from
the other worker's full orbit-distance fitting: only the entries that survive
the grading are prescribed here.

## Evidence already obtained

`graded_certificate.py` verifies explicit exact coordinate controls for a=2
and a=3 and rejects a deliberate bad coefficient. These controls certify small
degenerations only; they do not establish a growing family.

The first alternating least-squares run used a=2,...,8, 500 iterations and
seeds 20261020+a. Only the a=2 residual was small; the a=3 run missed a known
exact solution and became ill conditioned. This is not exclusion evidence.
A trust-region run with an analytic Jacobian found a floating a=3 control
with residual about 3.3e-15, and a=4 stalled around 1.8e-4. It was interrupted
during a=5 after the fixed-shared obstruction was applied. Both runs used
NumPy 2.5.4 and SciPy 1.18.1; their temporary candidate files were not available
after continuation. No exact candidate is retained from them.

The subsequent a=6,B=24 run was also unavailable after continuation. The
stronger concurrent obstruction rejects that fixed-G case, so it will not be
rerun. Future discovery data is saved under this worktree's results directory.

Floating residuals and condition numbers are discovery diagnostics. No
floating run is a construction certificate or an exponent bound.

The maintained discovery and exact verifier now also allow integer directions
`(alpha,beta)`. For a monomial coordinate let e denote the exponent of s.
The tested power is

    alpha*(deg(y)+deg(z)-(a-1)) + beta*(i-e(y)-e(z)).

This is induced by weights beta*i on X, alpha*deg(y)-beta*e(y) on Y, and
alpha*deg(z)-beta*e(z)-alpha*(a-1) on Z. All target terms have power zero.
The exact verifier rejects any nonzero negative coefficient, incorrect
constant coefficient, or floating input entry. It permits an arbitrary
constant shared matrix G. A successful exact target would itself force the
necessary shared rank because the target is concise.

Completed a=4,B=10 runs use directions (1,0), (1,-1), (1,1), and (1,2).
Their final descriptive residuals are approximately 5.43e-5, 1.86e-4,
3.68e-4, and 6.94e-4. Their matrices, diagnostics, seeds, and stopping budgets
are retained under `results/concavity-equivalence-2026-10-20/graded-shared-a4*`.
None is an exact certificate. Small partial residuals are especially weak
evidence here: for the first fit, the best full scaled tensor error in a
separate epsilon sweep remained about 1.03 relative to the target norm.
