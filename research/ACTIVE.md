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

1. Expand truncated-algebra source searches to products W_a tensor W_b,
   using nonseparable digit-pair weights and exact source rank ab.
2. Strengthen interior transvectant lower values with explicit restrictions
   and matched decompositions; avoid assigning convolution values from
   dimensions alone.
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
The earlier full archive replay passed locally. The current 49-test suite also passed; its log is in results/clebsch-gordan-2026-10-20/tests.txt.
Hosted job 118867495049 at `89ebb78` ran zero steps: GitHub reported failed
account payments or a spending limit. That is unavailable CI infrastructure,
not evidence that tests ran and failed. No billing changes were attempted.
