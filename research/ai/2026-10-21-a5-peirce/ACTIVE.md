# A5 principal-block modular refinement

Base: `b3e36fd4b627a7f00532ce25a21d78da6620c99f` (PR93). Topic branch:
`research/a5-peirce-20261021`. No delegated workers.

Question: does an exact Peirce/corner refinement of the published A5
radical pilot lower the modular source bound for A5 x C2 below 100,
thereby excluding its coordinate/potential M10 target? The complete
subgroup-coset catalog leaves that target open, and a separate eager
600-second search found no pair-injective model.

PR93's discovery README explicitly leaves blockwise alternate-source
filtrations open. Reuse its source data and bit-algebra helpers with
credit. The S5 and F8 investigations remain owned by their current
workers; do not change their worktrees. First construct orthogonal
idempotents and exact corner/radical dimensions for A5. Numerical weight
optimization is discovery only. Any accepted bound needs a separately
replayed algebra certificate, feasible rational/exact weights and the
credited modular field-transfer/slice argument with all hypotheses.

A bound at least 100 does not exclude the M10 target. A smaller numerical
score alone is not an exact exclusion, source map or exponent improvement.

## Accepted witness and current objective

The F2 and F4 corner pilots both gave approximately 104.443, above the
needed threshold. A loop basis change over F4 instead produced a tight
277-term leading tensor, with a rational entropy lower certificate.
The independent standard-library verifier checks all 216,000 source
coefficients, the rank 60 basis, integer weights, all 14,400 cover products,
and a large-integer inequality. Five corruption/control tests pass.

The written consequence is a lower barrier for eventual characteristic-two
source-power slice-rank costs: above 517/5 for both order 120 central covers,
and above 976613/5000 for the order 240 product source. It is not a finite-power
test exclusion or a construction. The proof imports the credited CVZ19
and AVZ20 tight-support entropy theorem with its field hypotheses.

The worktree is refreshed to `ef76802`, where PR95 has merged after all
hosted checks passed. Remaining work: update status and claim metadata,
run full regression/replay, inspect current overlap/main, and submit the
focused method-barrier PR through normal rules.
