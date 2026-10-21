# Higher jets and sixteen quantum block flags

AI-assisted research, October 20, 2026. Written proofs are unreviewed.
**No exponent improvement is established.**

The [higher-jet lemma](higher_jets.md) counts primitive saturated rows
using Smith orders and a first nonzero projected coefficient. For the
prescribed order-three/six quantum curves, it gives slice ceiling 98 even
after moving 112-to-110 output maps that stay surjective at the limit.
Their kernels may meet the original four-dimensional leading images.
Singular leading output maps remain open.

The separate [block calculation](blocks.md) supplies a nonzero minor for
every one of 256 ordered two-layer single-leading-block choices. Exactly
131 use the leading-map bound and 125 use a first-jet bound, with ceiling
97 in every case. This conclusion requires a regular full-output limit;
output projections before that limit and arbitrary block hierarchies are
outside the finite block calculation.

The size-four target has leg dimensions 100,110,110 and requires slice
rank at least 100 by its restriction to square M10. The new ceilings close
the stated families. They do not close general singular degenerations,
provide a tensor-power barrier or improve the exponent.

Use root requirements.txt:

```sh
python research/ai/2026-10-20-higher-jet-quantum-flags/blocks.py --output /tmp/block-certificates.json
python research/ai/2026-10-20-higher-jet-quantum-flags/controls.py --output /tmp/moving-controls.json
python -m unittest discover -s tests -p test_higher_jet_quantum_flags.py -v
```

Acceptance uses exact Q(q) arithmetic and integer contractions reduced at
a good cyclotomic prime. A saved nonzero minor proves number-field
nonvanishing. Independent dual-number tests check all selected-block
normalizations and the remaining-block case. The rate test replays every
jet minor at rate -1. Thirty-two explicit moving-surjection controls
support the general written proof; they do not replace it. A Smith-minor
control verifies the coefficient-count hypothesis and a counterexample
shows why arbitrary coefficient rank would be insufficient.

The source family and prior saturation arguments are credited in
`sources.json`. The external square-matrix slice-rank theorem retains its
original attribution. All code and proofs were generated and checked in
the same Codex session; no independent mathematical review is claimed.
