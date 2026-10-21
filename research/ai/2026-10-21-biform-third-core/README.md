# Biform structure and arbitrary eleven-by-nine boundary spans

Written AI-assisted proof, unreviewed. No exponent improvement is established.

The [proof](proof.md) identifies the entire third normal block as a tensor
product with a4-by6-by6 core. The six-dimensional matrix factors are biforms
of degrees(1,2) and(2,1). Every core matrix lies in the20-dimensional kernel
of their polynomial multiplication map. The explicit basis changes both
have determinant1, and every tensor coefficient is verified.

This supplies a short integral-domain proof that the kernel has no rank-one
matrix. A bihomogeneous gcd argument sharpens the actual two-hyperplane
compression bound from5 to3, with a sharp rational control. A separate
puncture lemma retains at least three first directions when one matrix leg
loses at most one dimension and the other loses at most three. Its sharp
control also shows that a general extension to losses(2,2) would be false.

Conditioned boundary-obstruction matrices have sharp minimum nonzero rank4.
Together these facts exclude every boundary first pair with dimensions at
least11 and9, in either order, including arbitrary complex subspaces,
delayed unequal first-growth orders, arbitrary higher regular coefficients
and an arbitrary Laurent first leg. The same moving-plane induction traps
both maps in dimension56, below the concise target dimension110.

The necessary ordinary first-rank sum at these canonical flags is now at
most20. Pure boundary pairs12,8 and10,10 remain at that threshold. Other
leading flags and general degenerations remain open.

```sh
python research/ai/2026-10-21-biform-third-core/verify.py --output-dir /tmp/biform-third-core
python -m unittest discover -s tests -p test_biform_third_core.py -v
```

Use root requirements.txt. Frozen coefficients from PR55/57 are pinned
inputs; their original verifiers reconstruct them from the source. New
checks derive the biform multiplication and tensor identity, replay exact
minor chains, and verify sharp and failing projection controls. The
all-order and general projection assertions use the written proofs, not
finite sampling or a jet cutoff. No independent review or formalization
is claimed. Canonical data and prior induction/minor methods retain their
credits in sources.json.
