# Finer full-source S5 cube covers

The [written, unreviewed proof](proof.md) improves the characteristic-two
cube bounds to 6638912 for S5 x C2 and 41159136 for S5 x C2^2. The one-copy
single-target volume caps are 2576 and 6415. Five additional shapes are
excluded in the second source; M(13,14,14) in the first remains open.

The full rank 120 binary basis and all 1728000 original group-trace
coefficients are replayed. The improved covers use two finer principal
degree assignments. A separately verified 26-coordinate common cover is
retained, but is not needed for the new bounds. These are restrictions
on the maintained coordinate/potential construction class over C;
arbitrary complex maps and an exponent improvement are not established.

```sh
python research/ai/2026-10-23-s5-peirce-covers/source.py --output results/s5-peirce-covers-2026-10-23/source.json --verification results/s5-peirce-covers-2026-10-23/source-replay.json
python research/ai/2026-10-23-s5-peirce-covers/export_covers.py --output results/s5-peirce-covers-2026-10-23/certificate.json
python research/ai/2026-10-23-s5-peirce-covers/verify_covers.py --source results/s5-peirce-covers-2026-10-23/source.json --certificate results/s5-peirce-covers-2026-10-23/certificate.json --output results/s5-peirce-covers-2026-10-23/verification.json
python -m unittest discover -s tests -p test_s5_peirce_covers.py -v
```

The optional C++ search under discovery is not an acceptance dependency.
The producer, verifier and focused tests require only the maintained root
Python environment. Reproduction is entirely local.
