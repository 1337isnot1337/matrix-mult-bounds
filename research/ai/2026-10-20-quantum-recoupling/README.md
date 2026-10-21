# Quantum recoupling controls

AI-assisted research, October 20, 2026. **No exponent improvement or
qualifying matrix degeneration is constructed.** The identities and
control calculations have no independent mathematical review.

The [family note](family.md) fixes a quantum-group convention, proves a
local diagonal equivalence with convolution over Q(q), and defines varying
recoupling maps on paired and cyclic convolution sources. This supplies
a legitimate class of Laurent tensor transformations near roots of unity.
It does not identify an improving limit.

The retained controls check both intertwiner equations at 196 coefficient
positions, 360 trilinear invariant equations, and 30 small basis/root
configurations. Basis coalescence is measured by the determinant valuation
minus the sum of column minimum valuations. A positive value proves
dependence after those column normalizations. It does not imply that the
tensor has a useful limit.

At q=i, the cyclic source's rowwise-regular local maps have exact ranks
8,32,64 for a=2,3,4. This normalization produces ordinary restrictions;
the size-four map has insufficient rank for the M(10,10,11) target. This
is a calibration of one normalization, not an obstruction to arbitrary
quantum recoupling or singular Laurent input maps.

Use root requirements.txt. The maintained exact code uses SymPy and the
standard library. No numerical dependency is needed for these controls.

```sh
python research/ai/2026-10-20-quantum-recoupling/quantum.py --output /tmp/quantum-controls.json
python -m unittest discover -s tests -p test_quantum_recoupling.py -v
```

The quantum-group definitions are external; the notes cite Arun Ram's
explicit convention and derive the normalizations used here. The fixed
classical recoupling and cyclic-source conventions are adopted from the
adjacent project packages, with their original credit retained. No
historical priority is claimed for quantum Clebsch--Gordan coefficients,
root degenerations or the source identities.

The optional `discovery/cyclic_series.py` retains a finite-field Taylor
calculation at p=65537, with q=256+t, where 256^2=-1 mod p. It requires
NumPy in addition to SymPy; those dependencies are not added to maintained
requirements. Actual small reports and arrays are saved separately from
exact complex controls. To replay the discovery calculation:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/ai/2026-10-20-quantum-recoupling/discovery/cyclic_series.py --output-dir results/local/quantum-recoupling
```

That run uses four Taylor coefficients and finds a nonzero constant tensor
in every tested rowwise-regular normalization. It supplies no singular
tensor-level degeneration or complex tensor classification.
