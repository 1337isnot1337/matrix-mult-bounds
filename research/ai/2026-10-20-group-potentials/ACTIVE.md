# Continued campaign checkpoint

Goal: prove a complete arithmetic exponent bound strictly below 9/4. The owner
explicitly requested continued work without ending at a partial checkpoint.
The active goal is not achieved. Do not mark it complete for a conditional
number, a finite profile violation, an exclusion, or successful verification.

Workspace: `/home/user/matrix-mult-bounds`, owned branch
`research/full-filtration-entropy-20261020`. Earlier pushed group checkpoint:
`dcfc1ef`. Read live git status and remote branches before editing; other
workers use their own branches. The archived passes stay byte-for-byte intact.

## Established in this branch, with actual status

- Earlier entropy work: unreviewed all-size balanced optimistic-score gap
  39/40; no weighted block-extraction theorem or exponent improvement.
- `research_note.md`: exact group-potential certificate format, general
  determinant-divisor obstruction, and abelian-coset ceiling lemma. Written
  proofs are unreviewed. The source SL(2,5) degrees were verified using all 81
  products of nine primitive central idempotents over Q(sqrt(5)).
- `rank_locus_proof.md`: arbitrary complex degeneration to M(a,b,c), a<=b<=c,
  requires N>=b*c+D(a-1), with D(r) computed from source degrees as an integer
  knapsack. Its explicit rank-eight, dimension-fourteen cone excludes SL(2,5)
  targets (9,9,12) and (9,10,11). Of all seven sorted shapes passing the exact
  9/4 degree-sum gate, only (10,10,10) survives this screen. This is a written,
  unreviewed argument, not a SAT proof or an exponent result.
- A successful SL(2,5) target degeneration would give omega<=2249/1000 by the
  exact conditional gate. None is constructed. The small (3,3,3) control
  succeeds with 27 intended terms and one killed extra term.
- Exactly 479 old Farkas cuts replay (20 SL2 control, 459 affine C5:C4).
  Larger SAT runs have no qualifying witness. Untraced UNSAT is not promoted
  to mathematical proof; many cases now have independent rank-locus exclusions.

## Current implementation and live work

- `search.py`: Glucose4 and budgeted CaDiCaL195 discovery, integer-only
  acceptance via `group_exact.py` and `verify_reports.py`.
- Affine groups use largest-coset normalization, exact integer max-fiber
  product constraints and complete cyclic-subgroup tables in
  `abelian_tables.py`. The canonical C29 normal (3,3,3) table has 162 rows.
- The latest SL(2,5) search uses the order-20 upper-triangular Borel subgroup
  (index six). Independent right translations give at least two Borel points
  in each size-ten set. A finite conjugation/inversion certificate covers all
  nineteen nonidentity Borel quotients with four canonical anchors. This is
  an exact search normalization, not a new target construction.
- Inspect `results/group-potentials-2026-10-20/*borel-cadical.json` and process
  status for the continuing SL2 (10,10,10) run. A report marked `running` is
  an initial or intermediate checkpoint, not completed coverage.
- Source rank-locus screens should precede any new affine search. They remove
  the tested C13:C3, C17:C4 and C19:C3 targets, plus C31:C5 (12,12,12) and
  C31:C6 (13,13,13). C29:C4 (10,10,10), C31:C6 (12,13,13), and larger suitable
  shapes remain candidates; their degeneration is unconstructed.

## Commands and constraints

Use `/tmp/matrix-entropy-venv/bin/python`. Optional discovery dependencies are
installed there (NumPy, SciPy, python-sat, SymPy). Exact certificates use the
standard library; repository tests use its existing SymPy dependency.
There are four CPU cores and limited free disk (check live space). Bound each
discovery run, retain actual parameters, verify every accepted witness, and
commit/push coherent checkpoints. Do not repeat unchanged timed-out searches.

Run the focused suite with `python -m unittest discover -s tests -p
test_group_potentials.py -v`; run the full suite before a substantial checkpoint.
Archive replay was passed unchanged. GitHub Actions previously could not start
because of account billing/spending restrictions; no hosted pass is implied.

Other agents' latest fetched branches at the time of this note:
`research/koszul-and-scaling-20261020` (292ba18),
`research/filtration-compatibility-20261020` (cf79709), and
`research/product-filtration-20261020` (b7cfb60). Their conditional fat-point
construction threshold is about 1.020472 source overhead; the source
degenerations remain unconstructed. The last branch owns off-leading
recoupling work; do not duplicate it without inspecting its current state.

## Later checkpoint: normal-subgroup Fourier screen

`ternary_fourier_proof.md` proves, with an integer Fourier certificate, that
C3^4 has no three four-point sets with an injective sum map. The elementary
lower bound is 1232 against the required 1088; an independent 64-inequality
certificate gives 1682. It excludes coordinate-potential (16,16,16) searches
in every group containing this subgroup with index four. It is a written,
unreviewed proof and does not exclude arbitrary tensor degeneration.

`candidate_frontier.py` screens all 45 affine C_p:C_r groups with p<=61 and
order<=250: 22,178 sorted shapes, 428 strict degree-sum gates, 58 survivors
after the coset and rank-locus screens. Three scheduled batches finished
34 cases with no pair model; one additional case was interrupted after a
CaDiCaL conflict-budget call substantially overran its requested time. The
manifests retain that distinction. Time limits are cooperative, not hard
wall-clock guarantees. No untraced negative is a theorem.

`quaternary_group.py` defines F4^3:C3 of order 192. The restricted offset
searches for (12,12,12) found 167 and 259 pair-injective models, respectively;
all 426 have exact positive Farkas circuits. `verify_reports.py` replays the
group products and verifies that each learned offset clause preserves its
whole circuit. No successful target exists in these reports. A cyclic-shear
direction screen is new discovery work, not a general group exclusion.

Latest fetched other-worker tips: Koszul `6bdab15`, product-filtration
`f6f307c`, filtration-compatibility `cf79709`. Their unrestricted source
degeneration gap remains open. The target exponent is still unbeaten.

`crossed_means_proof.md` now supplies necessary strict inequalities on nine
fiber-mean potentials. A positive integer zero dependence excludes the
chosen directions for every offset. The coordinate-base run reached 2000
models, all with exactly replayed mean circuits. A separate written argument
excludes this whole base family whenever two complementary four-spaces are
F4-scalar invariant. Other cyclic/random bases returned untraced SAT UNSAT;
those outcomes remain experiments. `verify_mean_reports.py` checks the two
bijections and every integer circuit with no SAT/LP dependencies.

## F8 checkpoint

Read `octal_research.md` for the new source and normalization arguments.
The exact local F8^2:C7 frontier has 6720 normalized pair cases, 126 local
survivors, 3942 complementary direction triples and 342 normalized classes.
Two global cases have untraced negative SAT outcomes; no qualifying witness.
F8^3:C7 has an explicit pair-injective 56-point parent. Deleting eight per
family produced 87 exactly replayed Farkas cuts, with no positive witness.
The feasible 20000-row prefix was not a witness and was superseded by that
full-constraint discovery. All 10752 symmetry-transformed copies of the
smallest circuit verify exactly; their hole-hitting SAT run timed out.

`test_group_streams.py` adds six passing local tests (integer backtracking
against small brute force, field/group laws, sparse-circuit replay, full
stream verification, actual group-operation normalization and frontier
controls). The expanded full suite passes all 55 tests. The first 30
normalized direction classes returned untraced SAT UNSAT; eleven discovered
models have exact circuits. These are experiments, not certified all-class
exclusions. No hosted CI pass is implied.

Latest fetched other-worker tips: Koszul `8e0a766`, compatibility `0108d62`,
product filtration `2c76b59`. The live leaderboard still shows 9/4. Continue
construction work; the user's target remains unachieved.
