# Characteristic-two source-cost barrier

An explicit A5 basis has a tight leading tensor which certifies a lower
barrier for asymptotic slice-rank bounds in characteristic two. The two
order 120 central-cover sources have liminf source-power slice rank above
517/5. The order 240 product source has it above 976613/5000. These constants
exceed the comparison thresholds for the project's selected coordinate
targets. The [written proof](proof.md) states the exact scope and external
entropy dependency. It remains unreviewed; no target map or smaller
matrix multiplication exponent is established.

The accepted certificate is `tight-certificate.json` in
`results/a5-peirce-2026-10-21/`. Its verifier needs only Python's standard
library:

```sh
python research/ai/2026-10-21-a5-peirce/verify_tight.py \
  results/a5-peirce-2026-10-21/tight-certificate.json
```

It independently checks a rank 60 basis over F4, every one of 216,000 source
coefficients, all nonnegative parameter exponents, the complete 277-term
limit, injective tightness weights, rational marginal counts and an exact
large-integer entropy inequality. It also verifies the SL(2,F5) to A5
central-cover map on 14,400 products. Numerical ranks, optimizer success
and floating entropy estimates are not acceptance criteria.

The initial search tried to lower the modular source cost below 100.
Both F2 and F4 corner/support optimizations instead gave approximately
104.443. Splitting the two-dimensional loop with the vectors
`v1+w*v2` and `v1+(w+1)*v2` revealed a tight leading support and the lower
barrier. The resulting accepted witness does not depend on the unreviewed
radical pilots that guided discovery.

To reproduce the basis discovery, the first three commands additionally
need NumPy/SciPy. They were run in the existing discovery environment with
NumPy 2.5.4, SciPy 1.18.1 and SymPy 1.14.0. Maintained dependencies and both
historical archives are unchanged.

```sh
python research/ai/2026-10-21-a5-peirce/pilot.py \
  --output results/a5-peirce-2026-10-21/pilot.json
python research/ai/2026-10-21-a5-peirce/support_pilot.py \
  --input results/a5-peirce-2026-10-21/pilot.json \
  --output results/a5-peirce-2026-10-21/support-pilot.json
python research/ai/2026-10-21-a5-peirce/f4_pilot.py \
  --input results/a5-peirce-2026-10-21/pilot.json \
  --output results/a5-peirce-2026-10-21/f4-pilot.json
python research/ai/2026-10-21-a5-peirce/export_tight.py \
  --output results/local/a5-tight-certificate.json
```

The export command uses SymPy for discovery of integer weights; the
independent verifier does not. The producer and verifier use different
finite-field convolution implementations. Same-session replay is not
independent mathematical review. The initial pilot's representation-order
error is preserved in `initial-pilot.log`; the producer now measures the
two restricted image dimensions before choosing their roles.
