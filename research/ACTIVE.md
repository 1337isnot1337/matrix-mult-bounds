# Active research checkpoint

Goal: continue until a rigorously supported matrix multiplication exponent
strictly below 9/4 is obtained. **ACTIVE / INCOMPLETE.** No such bound exists
in this branch. The user explicitly instructed not to stop at checkpoints.

Checkout: `/home/cinna/matrix-mult-schur-20261020`.
Branch: `research/product-filtration-20261020`.
Review: PR #2. Earlier pushed checkpoints: `712c91a`, `89ebb78`.

Completed owned work is documented in the affine-direct-sums and
Clebsch--Gordan packages. Coordinate paths differ from the other workers'.
The fixed-label proof independently overlaps their stronger result; it is
not counted twice. New recoupling searches retain k>i+j terms. No scored
profile violation has been found.

Current mathematical queue:

1. Products W_a tensor W_b and standard CW sources now have exact source-cost
   certificates and finite coupled-weight screens. Those screens found no
   violation. Move beyond unchanged sampled weight families.
2. Scalar tight-support uniform-marginal certificates now strengthen all 101
   recoupling blocks in six sources. Additional outer restrictions still find
   no violation. Investigate non-coordinate constructions and global endpoint
   constraints instead of repeating these supports.
3. Investigate whether critical-profile rigidity plus upper decompositions
   of W_r can conflict with its tight-support subrank bound. This is only a
   proposed bridge; no weighted extraction theorem or contradiction is proved.
4. If a strict source-rank violation appears, independently replay the
   coefficient witness and turn the strict margin into an explicit bound
   on every detecting character's t, then the stated arithmetic exponent.

Do not repeat unchanged completed grids as new research. Save the actual
coverage and exact next question at every commit. Keep other branches and
the first-pass archive unchanged; do not change repository visibility.

Validation environment: `/tmp/matrix-mult-research-venv/bin/python`, Python
3.12.3, SymPy 1.14.0. The host SymPy 1.12 does not satisfy archive replay.
The earlier full archive replay passed locally. The current 65-test suite also passed; its log is in results/mixed-restrictions-2026-10-20/tests.txt.
Hosted job 118867495049 at `89ebb78` ran zero steps: GitHub reported failed
account payments or a spending limit. That is unavailable CI infrastructure,
not evidence that tests ran and failed. No billing changes were attempted.

The all-size two-sector source-rank inequality narrows the hypothetical
critical amplitude to 1/Gamma(4/3)<=K<=(16/9)^(1/3). It does not close the
interval. P_* survives this family with cubed score at most 27/32 at every
size. Current follow-up: the mixed-target collision search permits arbitrary shared
coordinate permutations and output-coordinate sums. Exact witnesses pass for
m=2,3 and m=4 at B=11; the m=4,B=10 query is UNSAT, while m=5,B=15 timed
out. Allowing A=m+1 also gives UNSAT at m=4 and a timeout at m=5.
This has no asymptotic short-leg cost if an unbounded family can be found.
No such family is proved. Next: exploit the necessary disjointness of
source output sets belonging to distinct target output coordinates, then
move beyond this coordinate ansatz if its overhead remains too large. The independently rediscovered ordinary-restriction and shared-leg
flattening arguments overlap concurrent d2d505c and 6bdab15, respectively.
See research/ai/2026-10-20-mixed-restrictions/README.md for precise coverage.
