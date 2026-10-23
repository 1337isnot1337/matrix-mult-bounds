# Sharp kernel onset and source-rank bounds

The [written proof](proof.md) shows that the paired source's long-leg
Koszul maps, with short input, are injective exactly for
0<=p<=a(a-1), over every field. Fixing one short coordinate gives an
explicit family of kernels in every larger degree, with an all-degree
dimension lower bound. Combined with PR169, this gives both upper and
lower bounds on the source ranks. Neither bound is asserted to be exact
in the remaining intermediate degrees.

Exact controls check every exterior degree of the restricted source at
a2 and a3, with modular lower ranks and independent integer kernels.
The first-kernel witnesses embed into 4 and 45 independent full-source
integer kernels, respectively. All signed output coefficients are checked.

The saved screen makes 25,254 exact comparisons for all 28 maintained
short-leg survivors through a16 and both long-leg orientations. The
bounds settle 2,970 intermediate comparisons beyond the two full-rank
intervals as incapable of excluding the target. They give no target
exclusion. Every remaining comparison is explicitly undecided. This is
a bounded screen of the pinned frontier, not an all-size dominance result.

Run from the repository root:

```sh
python research/ai/2026-10-23-paired-kernel-onset/verify.py --verify results/paired-kernel-onset-2026-10-23/certificate.json
python research/ai/2026-10-23-paired-kernel-onset/verify.py --screen --verify results/paired-kernel-onset-2026-10-23/target-screen.json
python -m unittest discover -s tests -p 'test_paired_kernel_onset.py' -v
```

The all-size argument is written and unreviewed. This package depends
on the explicitly pinned PR169 bundle result and the maintained matrix
rank formula. No independent review, formalization, historical priority,
target construction or exponent improvement is claimed.
