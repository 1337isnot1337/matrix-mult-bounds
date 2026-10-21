# Leading-map obstructions for varying quantum families

AI-assisted research, October 20, 2026. Written proofs are unreviewed.
**No exponent improvement or qualifying tensor degeneration is constructed.**

The [saturation argument](saturation.md) applies to any tensor with a
first leg of dimension a. Fix regular maps on its other two legs, of
constant ranks b0,c0, and let r be the first-leg flattening rank after
those constant maps. Every regular tensor limit obtained with an arbitrary
Laurent first-leg map has slice rank at most

    a-r+min(b0,c0).

There is no bound on the orders of the higher jets. If r=a, the Laurent
first-leg map must itself be regular. This is a general leading-map test,
not a claim of historical priority for saturated lattices or slice rank.

For the prescribed quantum root maps at orders 4,8,12,16,24, exact
number-field row support and nonzero modular minors give respective
ceilings 62,44,64,68,86. These are below the slice rank 100 of M10, so
they exclude the selected size-four matrix target in those families.

The ungraded ceilings at orders three and six are only 104. The separate
[central-weight argument](graded_obstruction.md) excludes their sixteen
prescribed phase pairs when the final maps and projections preserve the
Cartan grading. The proof uses a nonzero matrix of rank at most four
in a forced 16-dimensional central space, whereas every nonzero first
slice of the matrix target has rank at least eleven.

The unique Cartan target profile is adopted from the concurrent worker's
canonical claim **EXP-CYCLIC-CARTAN-FRONTIER-051**, merged in PR23. See
[COORDINATION.md](COORDINATION.md). The independent integer recursion in
profiles.py replays that classification; it is not a new result. Two
prose coefficients in the canonical note are corrected without changing
its search or surviving profile.

## Reproduction

Use root requirements.txt. The certificate generator uses SymPy for
exact rational functions; the contraction and modular minor routines use
integer arithmetic. No NumPy or floating arithmetic is used for acceptance.

```sh
python research/ai/2026-10-20-graded-quantum-flags/one_leg.py --output /tmp/one-leg-certificates.json
python research/ai/2026-10-20-graded-quantum-flags/profiles.py --output /tmp/profile-replay.json
python -m unittest discover -s tests -p test_graded_quantum_flags.py -v
```

The source normalizations come from the quantum package merged in PR25.
The square matrix slice-rank fact is external, from Blasiak et al.,
arXiv:1605.06702v4, Remark 4.9. Sources are pinned in sources.json.
Different leading flags, symmetry-breaking projections and tensor powers
remain open. Slice rank is not submultiplicative, so the finite ceilings
are not asymptotic method barriers.
