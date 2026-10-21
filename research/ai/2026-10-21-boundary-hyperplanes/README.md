# Arbitrary boundary hyperplanes

Written AI-assisted proof, unreviewed. No matrix-multiplication exponent gain.

The [proof](proof.md) excludes the canonical A4 target of leg dimensions
100,110,110 whenever both first boundary quotient spans have dimension at
least11. The spans are arbitrary complex subspaces; their first-growth
orders may be delayed and unequal. Higher coefficients and the Laurent
first leg are unrestricted.

Three ingredients extend PR55 beyond its complete12-by12 frames:

- The boundary obstruction matrices have sharp minimum nonzero rank2.
  Annihilating any11-dimensional boundary hyperplane forces the entire
  boundary obstruction to vanish.
- Every third-block matrix belongs to a fixed80-dimensional space equal
  to S0 tensor Mat2, where S0 is20-dimensional in Mat6x6 and contains no
  nonzero rank-one matrix. Six polynomial determinant identities prove
  that exclusion over C.
- Projecting away an arbitrary direction on each12-dimensional leg loses
  at most5 dimensions of any slice space in S0 tensor Mat2. First rank8
  therefore leaves at least3, exceeding the matrix target's ceiling2.

The general two-hyperplane lemma is sharp; a separate skew-matrix control
loses exactly5 dimensions. Formal induction then traps both local maps in
moving56-dimensional boundary spaces.

At ordinary first order, at least one effective first rank is at most10,
and the total is at most22. The pair12,10 and its exchange are not excluded
by this argument. Mixed first spaces retain their separate stronger bounds.

```sh
python research/ai/2026-10-21-boundary-hyperplanes/verify.py --output-dir /tmp/boundary-hyperplanes
python -m unittest discover -s tests -p test_boundary_hyperplanes.py -v
```

Use root requirements.txt. Frozen third coefficients come from PR55,
whose verifier independently reconstructs them from all source terms.
This package derives and verifies the new linear spaces, polynomial
identities and compression control exactly. Its all-order statement is
a written induction, not a finite jet cutoff. Attribution and dependency
hashes are in sources.json.
