# Integrated research coordination

The exponent-improvement goal is active; no bound below 9/4 is established.
The user requests frequent integration of completed work into main and cleanup
of fully merged task branches. Preserve proof status and source attribution
when merging; integration is not theorem acceptance.

The subsequent four-lane main integration at `a83bc24`, combined with the
graded-obstruction checkpoint `635bf48`, passes 162 tests. The new proofs
close two graded-weight regions but leave intermediate slopes and arbitrary
singular shared maps open. See `../docs/integration_2026-10-20.md` for pins.

The product/recoupling package entered main through PR #2 at `93f8f8a`.
PR #1 adds the Koszul/scaling/source-obstruction package and reconciles the
shared status and research-direction documents. Its combined local replay
with that main revision passes 106 tests. Both historical archives are
unchanged. Current package pointers:

- `ai/2026-10-20-koszul/ACTIVE.md`: singular shared-map and intermediate-weight
  questions; read the newly excluded constant-basis and graded regions first.
- `ai/2026-10-20-mixed-restrictions/README.md`: collision-capacity questions.
- `../docs/concurrent_research.md`: pinned results on the other active branches,
  including which proofs were inspected or adopted.

Do not delete a worker branch with unmerged commits. Fetch before starting
new work or publishing an integration, and test the combined tree.

## Product-filtration worker checkpoint retained from PR #2

Goal: continue until a rigorously supported matrix multiplication exponent
strictly below 9/4 is obtained. **ACTIVE / INCOMPLETE.** No such bound exists.
The user explicitly instructed not to stop at checkpoints and to merge
verified work into main frequently, cleaning up incorporated branches/PRs.

Checkout: `/home/cinna/matrix-mult-schur-20261020`.
Branch: `research/singular-shared-laurent-20261020`.
PR #2 merged into main at `93f8f8ab951e104cda041d3180f2401a4c0f81d3`.
Its tree equals the locally and remotely verified `20734a9` checkpoint.
PR #4 merged the quantitative capacity theorem at `34c2367` after the
required CI check passed. Its incorporated branch was removed as well.
The merged `research/product-filtration-20261020` branch was removed.
Preserve other workers' active branches and the first-pass archive.

Current results:

1. The two-sector inequality narrows the hypothetical critical amplitude to
   1/Gamma(4/3)<=K<=(16/9)^(1/3), a nonempty interval. P_* survives the
   whole family with cubed score at most 27/32. No unchanged grid is needed.
2. Full recoupling coefficients, scalar tight-support certificates, explicit
   affine direct sums, W/CW source certificates and exact finite screens are
   retained in their own packages. No scored profile violation was found.
3. Active-output disjointness and repetition capacity now give an asymptotic
   overhead lower bound 3/2-sqrt(3)/4 for coordinate input injections with
   arbitrary nonzero scalars, constant output mixing and diagonal weights.
   It permits arbitrary canonical target-copy counts and limsup A/m<=5/4.
   This exceeds the required approximately 1.020472. The proof is written
   and unreviewed. The joint-word extension now allows arbitrary Laurent
   output maps while retaining monomial input maps. Actual input mixing
   remains outside the proof.

Current queue:

1. Search a genuinely nondiagonal shared basis followed by nontrivial shared
   weights. A fixed shared basis with regular invertible limit is already
   excluded by concurrent 8e0a766. Shared weights are therefore essential.
   The selected exact discovery model fixes an integer shared basis, searches
   a Y coordinate injection and arbitrary rational output coefficients, and
   accepts only an independently replayed coefficient witness. Identity m=2
   is its positive control. The dense Hadamard m=4 pilot is UNSAT; an opposite Newton-basis pilot
   adds nondiagonal input mixing. Its m=2 control is SAT and independently
   replayed. Its m=4 query is also UNSAT; the result is finite and does not
   exclude general nondiagonal shared maps.
2. If a finite witness appears, extract its structural pattern, quantify all
   source overhead and prove the required unbounded family. A single finite
   matching-profile violation does not establish an exponent.
3. If this ansatz is also obstructed, move to general Laurent shared maps or
   a different source-wide mechanism. Do not repeat unchanged closed grids.

Latest local extension validation: 179 tests pass in
results/mixed-restrictions-2026-10-20/tests-laurent-extension.txt.
Latest merged validation: 174 combined tests after integrating 424dd92;
the earlier standalone capacity checkpoint passed 73 tests and the full
five-part archive replay
under Python 3.12.3 / SymPy 1.14.0. Logs are in
results/mixed-restrictions-2026-10-20/. Hosted run 39505129621 executed both
unittest and archive-replay steps successfully at 20734a9. An earlier billing
failure was historical infrastructure unavailability, not a test failure.

Concurrent overlaps are credited in package notes and sources.json. In
particular, canonical exact-restriction and equivariant-flattening arguments
independently overlapped d2d505c and 6bdab15. The quantitative capacity bound
is complementary to 8e0a766, retaining distinct hypotheses.
