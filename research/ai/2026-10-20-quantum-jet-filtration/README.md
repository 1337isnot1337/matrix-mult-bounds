# Quantum first jets and partial saturation

AI-assisted research, October 20, 2026. Written proofs are unreviewed.
**No exponent improvement is established.**

The [proof](proof.md) gives the first-jet extension

    slice_rank(limit)<=a-r1+b0+c0,

where r1 is the dimension of the first partially saturated row space,
and b0,c0 are the two regular leading-map ranks. An exact minor can lower
bound r1 using one prescribed first derivative, independently of the
other first jet and all higher jets.

For the order-three/six quantum curves, 32 exact modular minors give
r1>=64 and a slice ceiling 56. Disjoint column supports make each minor
a nonzero monomial in the approach rate. The conclusion therefore covers
every nonzero rate, higher parameter term and ramification order. It
allows an arbitrary Laurent map on the third leg and subsequent ungraded
substitutions. This is stronger than the previous graded central-space
obstruction, and it explains the failed ungraded coefficient pilots.

The proof separately permits arbitrary constant output projections of
codimension at most two before the limit is taken. Four leading-map rank
minors and 128 coordinate-slice minors give a uniform nonzero-slice rank
lower bound 28; after projection this forces r1>=26 and a slice ceiling
94. Thus no regularity is assumed before those constant projections.
Parameter-dependent output projections are outside this corollary.

Use root requirements.txt:

```sh
python research/ai/2026-10-20-quantum-jet-filtration/jets.py --output /tmp/first-jet-certificates.json
python -m unittest discover -s tests -p test_quantum_jet_filtration.py -v
```

Acceptance uses exact rational functions, integer contractions and modular
minors with verified number-field residue denominators. No numerical
dependency is added. The proof adopts the source family from PR25, the
saturated-lattice argument from PR33, and the external square-matrix
slice-rank fact with its original credit.

The finite-field discovery pilot completed six relative rates using
three coefficients per local matrix. Its saturated tensors had ranks
112,72,72. A longer Fourier-interpolation calculation independently
checked the common-rate result. These are retained discovery results,
not characteristic-zero acceptance or a general rank classification.

Non-scalar weights on the varying quantum blocks and different leading
flags remain construction questions. Retiming the same parameter curve
does not escape this proof. No asymptotic method ceiling follows, since
slice rank is not submultiplicative.
