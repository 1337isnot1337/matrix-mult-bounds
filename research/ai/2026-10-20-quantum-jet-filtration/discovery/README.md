# Retained finite-field coefficient calculations

These are discovery programs, separate from the exact characteristic-zero
obstruction in `../proof.md`. They require NumPy, which is optional and is
not added to root verification dependencies. The retained environment was
Python 3.12.3, SymPy 1.12, NumPy 1.26.4.

Both programs use a=4, p=786433, q0=10^((p-1)/6) modulo p, and all
112-dimensional source legs. All thirteen weight blocks are retained.
The direct calculation uses three coefficients and relative rates
1,2,3,-1,-2,-3. The Fourier calculation uses twelve coefficients and
32 evaluations of the truncated local polynomial matrix at the common
rate. The product polynomial has degree at most 22, so 32 samples recover
every requested coefficient without aliasing.

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/ai/2026-10-20-quantum-jet-filtration/discovery/matrixspace_rates.py --output-dir /tmp/quantum-rate-replay
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/ai/2026-10-20-quantum-jet-filtration/discovery/matrixspace_fourier.py --output-dir /tmp/quantum-fourier-replay
```

Modular products are accumulated using binary64 only when their integer
sum is below 2^53: the largest contraction has at most 112 terms, each at
most (p-1)^2. Multiplications and sums therefore remain exactly
representable; integer modular elimination is used afterward. The Fourier
program also checks its constant and linear coefficients against separate
direct contractions.

At each saturation round the exact modular row reduction is applied to
all available coefficients. Zero constant rows are divided by the
parameter, consuming one coefficient of precision. Completion means every
weight block attains full first-row rank before precision runs out. It
does not mean the resulting tensor is a matrix tensor. All six saved
tensors have flattening ranks 112,72,72.

The replay compared all 8,429,568 saved entries across the six rate arrays.
The common-rate tensor also agrees with the longer Fourier calculation.
`results/quantum-jet-filtration-2026-10-20/discovery-comparison.json` records
those comparisons. No finite-field candidate is promoted to a complex
degeneration or an exponent improvement.
