# Complete subgroup ideal catalog

Base: `00d51337dd`, refreshed October 21, 2026. Topic branch:
`research/subgroup-ideal-catalog-20261021` (renamed from the initial
`research/source-cost-screen-20261021`). No delegated workers.

Question: do subgroups beyond the previously certified order-five
class give additional necessary coset cuts on the three active central-cover
targets? Enumerate every conjugacy class of subgroups in the exact
group tables and certify its two-sided averaging-ideal dimension. Compare
the resulting forbidden cosets with pair injectivity and the existing
order-five cuts before proposing a search change.

The initial cyclic scan found no additional minimal cuts. Noncyclic
subgroups in the split cover give additional candidates; extend the
catalog to the complete subgroup lattices rather than rerunning a search
with redundant cyclic cuts.

Intended output: an exact catalog with integer upper-rank witnesses and
modular lower-rank checks, a separate verifier and useful search cuts if
any exist. Use the existing written subgroup-averaging proof with credit.
This work supplies neither arbitrary-complex-map exclusions nor an
exponent improvement.

Overlap: PR79's order-five calculation is on main. Open PRs37,54,76,84,86,
91,92 address different construction, ordinary-rank or partner questions.
Do not change their worktrees or the historical archives.

## Local checkpoint

The complete catalog is generated and verified: 455 subgroups, 65 classes,
and 550 additional noncyclic minimal cosets per split-cover target leg.
The other two targets gain no new minimal coset cuts. Both archives match
the base byte-for-byte across all 18 tracked files, and historical replay
passes. Six focused tests pass, including all 32 exported parity
contradictions from the 601.3-second timeout (34 model events, no lift).
An initially stale test count is corrected and its failure log is retained.

All 794 initial catalog test IDs have successful results. The sequential run
completed 360 tests in 85 complete modules before an intentional split;
the other 434 tests ran in four disjoint module groups. Three optional
numerical controls skipped in the maintained environment also passed in
the discovery environment. The compressed evidence bundle includes every
test ID, assignment, status and log. The validation receipt is finalized.
PR95's first head passed all hosted checks. Main advanced to `b3e36fd`
before merge; the branch now integrates that S5 block-filtration result,
preserves all 265 claims, and passes 16 local integration checks. The
combined inventory is 798 tests. Wait for the integrated head's full CI
and merge through the normal repository rules.

The `a94c09e` integrated head also passed all hosted checks. PR94 then
advanced main to `f80ebf5`; the second base integration preserves all
269 claims and passes 21 focused checks. Its inventory is 807 tests.
Enable normal auto-merge at the refreshed head while its required checks
run, avoiding an unnecessary polling gap after success.
No target construction or smaller exponent is established.

The neighboring S5 worktree has active `coset_ideals.py` changes. Leave that
investigation with its current owner; it is outside this package.
