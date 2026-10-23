# Rank20 source linear spaces and the singular rank105 chart

The [written, unreviewed proof](proof.md) classifies the canonical A4
source locus of rank at most20 and proves that its largest vector linear
spaces have dimension eight. After fixing the coherent middle factor,
the biform has a quadratic divisor in x or in z. A generic-pencil argument
controls linear spaces whose divisor initially appears able to vary.
The dimension-eight bound is attained by fixing either quadratic divisor.

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

Use `verify.py --write` only to regenerate controls, followed by replay
without that flag. The package's full validation remains in progress,
and its parent PR125 is not yet merged. The universal proof has no
independent mathematical review or formalization. Finite controls do not
establish the universal classification, a matrix target or a smaller exponent.
