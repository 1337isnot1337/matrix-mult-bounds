# Bounded unsuccessful discovery follow-ups

These records are separate from the two successful exact constructions.
They did not find 30 products on nine coordinates, a cheaper 29-product
correction pattern, or 39 correction-free products on twelve coordinates.
They prove no upper bound, nonexistence, or optimality statement.

`summary.json` records the completed budgets, seeds, inputs, source
files, optional solver versions and file hashes. Raw output and actual
reports are preserved. The versioned public origins of `ex14.masks`
and `ex38.masks` are pinned in the parent `sources.json`; these files
contain the same tripartition data in mask form. The 29-product input
is the successful local witness, serialized as masks. The pair {6,7} seed
removes product index 21 (zero-based) from it, killing the sole surviving
mixed triple with that replicated pair before the restricted search.

The C++ programs take the seed file, mode, iteration count and RNG seed
as in the successful construction commands. `search_broad.cpp` changes
only the destroy/rebuild population parameters. `search_no_pair.cpp`
adds the explicit replicated-pair {6,7} exclusion to the conflict-free test.
`optimize_corrections.cpp` instead takes seed file, iterations, RNG seed
and output path, and favors smaller correction counts among equally
large families. Their source files preserve the programs actually run.

The optional Python MILP experiment uses SciPy and NumPy; these are
**not** dependencies of mathematical acceptance or the maintained test
suite. Run `milp_search.py` from this directory to repeat its recorded
bounded experiment with the adjacent mask seed. It performs up to 300
neighborhood attempts, with a 120-second total budget and 3-second solver
limits. Exact coordinate tests reject invalid proposed families. Eight
of 291 solver calls ended at their time limits. No solver status or
floating objective supplies a mathematical nonexistence certificate.

For a tripartition t, the MILP has coefficient 2 on its own selected-product
variable and coefficient 1 on each different tripartition sharing one
part. The row bound is 2. A chosen t therefore excludes every repeated
part; an unchosen t excludes a mixed compatible triple of selected
parts. This is used only for candidate discovery in the recorded fixed
neighborhoods, never as an exhaustive global claim.
