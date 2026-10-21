# Heisenberg continuation and modular obstruction

Question: can a coordinate/potential construction in the next Heisenberg
source, H_7, realize M(16,16,17) and pass the conditional 2.247 comparison?
The maintained H_5 source proof supplies the source degrees. Two bounded
general searches, normalized with first size16 or17, each ended after600
seconds with no model. They are discovery history, not nonexistence proofs.
They require optional python-sat/NumPy/SciPy discovery dependencies.

The [modular proof](modular_proof.md) now gives a stronger reason to leave
that source: applying Petrov's external defining-characteristic filtration,
with a characteristic-transfer argument and cyclic symmetrization, excludes
the usual degree gate for rectangular coordinate targets, including finite
direct sums, in **every tensor power** of H_p, for all odd primes p<=47.
It leaves arbitrary complex degenerations open. The proof is written and
unreviewed, and no matrix multiplication exponent was improved.

The exact report gives rational certificates for fourteen primes and a
non-exclusion control at53. All acceptance arithmetic is rational/integer.
Finite controls verify the PBW change of basis and actual group-algebra
right-generator products over F_3, F_5, F_7. The external filtration and
tight-support theorem retain their authors' attribution.

```sh
python research/ai/2026-10-20-heisenberg-seven/modular_bound.py \
  --output results/local/heisenberg-modular-bound.json
python -m unittest discover -s tests -p test_heisenberg_modular.py -v
```

The former minimum-leg modular pilot is superseded by the cyclic volume
argument and retained only in ignored `results/local/` for provenance.
Neither a failed SAT search nor a preliminary unproved modular premise is
used in the written conclusion.
