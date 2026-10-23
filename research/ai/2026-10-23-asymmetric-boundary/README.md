# Asymmetric boundary reductions

This package addresses the separate canonical A4 first-boundary case
12-by8. The full case remains open. The [proof](proof.md) establishes:

* A universal splitting of the other-side obstruction on the complete
  100-dimensional full-side kernel as J(M tensor I2), with J injective
  and M a 42-by6 linear matrix. A nonzero compatible obstruction has rank
  four and forces the smaller first span to be a product H tensor C2.
* Every non-plane core in the preceding complete 28-dimensional
  joint-zero family has joint row and column support at least three.
  Two exact 364-by364 cubic coefficient determinants certify this globally.
* A sharp one-sided projection gap, zero or at least four, under losses
  at most four. Together these exclude non-plane normals in the
  joint-zero family from the asymmetric target's third first-rank bound.

The nonzero rank-four branch, its third tensor, later compatibility and
the full matrix target remain unresolved. No exponent improvement,
independent review or formalization is claimed. All work was prepared
with OpenAI Codex under owner direction. Predecessors retain credit and
exact source pins in [sources.json](sources.json).

Run from the repository root with root requirements installed:

```sh
python research/ai/2026-10-23-asymmetric-boundary/verify.py
python -m unittest discover -s tests -p test_asymmetric_boundary.py -v
```

The verifier reconstructs both obstruction maps and the biform core from
the credited source builders. It uses exact rational identities and
nonzero integer coefficient determinants modulo 32003. It does not use
ignored discovery scripts, parameter sampling, floating point or an
unrecorded Groebner calculation. The compressed report under
`results/asymmetric-boundary-2026-10-23/` is deterministic.

Focused tests independently reconstruct all selected cubic determinants
symbolically, check their coefficient matrix and determinant through the
SymPy finite-field implementation, verify the complete auxiliary identity
and the sharp product kernel, and reject corrupted minor and first-span
controls. These checks verify the stated algebra; they do not constitute
independent mathematical review.
