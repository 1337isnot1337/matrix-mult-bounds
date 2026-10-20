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
