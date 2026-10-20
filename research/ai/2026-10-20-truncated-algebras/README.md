# Active source family: truncated polynomial multiplication

2026-10-20. AI-derived investigation; no exponent below 9/4 established.
This changes the source and its upper bound, rather than extending a completed
convolution-product screen.

Let

    W_r = sum_(i+j+k=r-1) x_i y_j z_k,  0<=i,j,k<r.

It has border rank exactly r over C. Here is the elementary upper certificate.
Choose a primitive r-th root of unity zeta. The cyclic tensor with support
i+j+k congruent to r-1 modulo r equals

    (1/r) sum_(ell=0)^(r-1) zeta^((r-1)ell)
      (sum_i zeta^(-i ell) x_i)
      (sum_j zeta^(-j ell) y_j)
      (sum_k zeta^(-k ell) z_k).

It has rank at most r. Weight each variable by its index, subtracting r-1
on the first leg. The minimum supported total weight is zero, and its tensor
is W_r. Output flattening gives the matching lower bound r. The Fourier
construction and degeneration/interpolation passage are standard tools;
the argument is included to make the source cost explicit.

Every leg permutation preserves W_r. Thus for a character with parameter t,

    P(W_r)=lambda(W_r)^(1/t) <= r^(1/t).

At the critical value t=3/4 an exact scored degeneration above r^(4/3) would
exclude that value directly. A uniform bound below 3/4 would still require
quantifying the strict margin and its dependence on t before claiming an
arithmetic exponent. The tests here compare cubes with r^4 exactly.

The search normalizes input weight arrays to minimum zero, chooses the
minimum-compatible weight on every output, and scores exact zero-weight
supports. Recognized convolution pieces use exact coordinate/factor
certificates. Unrecognized pieces use a dot-product slice: each slice is a
partial permutation matrix because i+j+k is fixed. Recursive components
use the same proved shared-leg and full-direct-sum inequalities as the
recoupling search. The stronger run also allows recursive output-coordinate
deletions. Those deletions recover the six-unit Strassen-sector score for
W_4, which is missed by the weaker score without output deletion.

Binary normalized arrays have been tested for r=2..7. No strict critical
violation was found. The output-deletion run covers r=3..7, also without a
strict violation. The exact reports preserve counts, witnesses and interval
bounds. This is finite evidence, not a general obstruction.

An important next extension is a product W_a tensor W_b. It also has source
border rank ab and is itself a degeneration of W_ab: write each index in
base b and weight by its low digit. In the support of W_ab the lowest
possible low-digit sum is b-1; retaining it also forces high-digit sum a-1.
The resulting support is exactly W_a tensor W_b. Nonseparable weights on
the digit pairs are outside the completed one-dimensional binary runs.

## Reproduction

```sh
python research/ai/2026-10-20-truncated-algebras/truncated_search.py --max-size 7 --output /tmp/truncated-binary.json
python research/ai/2026-10-20-truncated-algebras/truncated_search.py --min-size 3 --max-size 7 --delete-outputs --output /tmp/truncated-output-restrictions.json
python -m unittest discover -s tests -p test_truncated_algebras.py -v
```

The character framework, dot-product normalization and shared-leg entropy
inequality are external dependencies from OpenAI's October 2 proof,
revision fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb. The comparison lower
profile is the local first-pass result. No historical priority, independent
review, or formal verification is claimed for this investigation.
