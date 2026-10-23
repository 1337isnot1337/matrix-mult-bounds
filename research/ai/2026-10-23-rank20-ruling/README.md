# Rank20 source linear spaces and the singular rank105 chart

The [written, unreviewed proof](proof.md) classifies the canonical A4
source locus of rank at most20 and proves that its largest vector linear
spaces have dimension eight. After fixing the coherent middle factor,
the biform has a quadratic divisor in x or in z. A generic-pencil argument
controls linear spaces whose divisor initially appears able to vary.
The dimension-eight bound is attained by fixing either quadratic divisor.

The [all-size continuation](all_sizes.md) proves the corresponding source
classification at rank cap a^2+a for every integer a>=2, with a binary
divisor of degree a-2 and sharp vector linear-space dimension2a. It also
gives a uniform Laurent ruling criterion and explicit A5 target margins.
Claim `AI-FIRST-GAP-LINEAR-SPACES-003` remains written and unreviewed.

PR125's shared-correction ruling criterion then excludes an A4 to
M(10,10,11) formal degeneration if either scalar-balanced long-map limit
has rank at least105. Both other maps, including the original unit lift,
may have arbitrary finite poles. Remaining candidates must have balanced
long-map leading ranks at most104 on both sides. Rank caps above20 and
the corresponding lower long-map ranks are outside this proof.

The source rank formula and its external Grothendieck splitting theorem,
the fixed coherent-factor classification and the shared-correction
criterion retain their previous attribution and exact pins. See
[the question](QUESTION.md) and [source records](sources.json).

Reproduce from the repository root with its maintained dependencies:

```sh
python research/ai/2026-10-23-rank20-ruling/verify.py
python -m unittest discover -s tests -p test_rank20_ruling.py -v
```

The exact report at `results/rank20-ruling-2026-10-23/controls.json`
contains eight dimension-eight fixed-divisor source spaces,24 actual
source rank calculations, all22 permitted kernel splitting-degree triples,
four independent generic pencils and eight long-limit ranks. It includes
repeated quadratic roots, roots at infinity and conjugate nonreal roots.
An independent pencil loses the quadratic divisor when the joint gcd is
zero; a dependent pencil retains degree two despite joint gcd zero. The
latter checks the independence hypothesis in the proof's pencil lemma.

Additional selected-size controls enumerate331 admissible splitting tuples
at a2 through6, exhibit sharp fixed-divisor spaces with actual source ranks
at a2,3,5, and check four A4/A5 target thresholds. These finite controls
are separate from the universal proof and do not establish its quantifiers.

Use `verify.py --write` only to regenerate controls, followed by replay
without that flag. The [validation receipt](../../../results/rank20-ruling-2026-10-23/validation.json)
records all869 tests on each of Python3.10 and3.14 at610f2a9:866 passed
and3 optional controls skipped per version. All five historical archive
replays passed. At integrated commit e57e144,34 focused tests passed,
covering this package, its parent, incoming fixed-resolvent tests and
repository metadata. The research code and controls are byte-unchanged
between those full-suite and integration checks. The receipt retains
compressed hosted/focused logs and exact commit/tree and code hashes.

The earlier local full runs were interrupted by a machine reboot and
are not counted as passing. PR142 includes the full PR125 package for
combined integration; final-head hosted CI must pass before merge. The
universal proofs remain unreviewed and unformalized. These checks do not
establish the universal classification, a matrix target or a smaller exponent.
