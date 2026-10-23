# Audit of the whole-filtration entropy certificate

**Claims:** `AI-FULL-ENTROPY-001` and the balanced continuation
`AI-BALANCED-ENTROPY-002`, Sections 2--4 of
[`research_note.md`](../ai/2026-10-20-full-filtration/research_note.md).

**Source pin:** repository commit `3008d704d1797da02f7bf3f29cc1dbd4c0e7fa93`;
the reviewed note is Git blob `3cd953da312bc3c8530cf0b8b0cd481ac8a9fbf3`,
and its certificate generator is Git blob `dd7e0f8413c705d65d09e2bccd54534967dbb86e`.

**Conclusion:** I found no gap in the proof that the defined optimistic entropy
score is bounded by the pointwise certificate for every distribution, nor in
the balanced all-size `39/40` bound. The conclusions concern that analytic
score and its stated sources. They do not establish a weighted tensor
extraction theorem, an actual character profile, an exponent improvement,
independent human review, or a Lean formalization. Both claims remain
`proof-written-unreviewed`.

## Every-distribution dual certificate

For positive probability vectors `u` and `v`, the pointwise condition
`f_ij^3 <= C^3 (u_i v_j)^2` implies
`log f_ij <= log C + (2/3)(log u_i + log v_j)`. Summing against `q` and using
`D(q_X || u) >= 0` and `D(q_Y || v) >= 0` gives
\[
\sum_{ij}q_{ij}\log f_{ij}\le \log C-\frac23(H(q_X)+H(q_Y)).
\]
The entropy minimum is at most `(H(q_X)+H(q_Y))/2`; the two terms cancel in
the logarithm of `E(q)`. This holds for zero entries of `q` by continuity and
the stated `0 log 0` convention. It uses no property of the output marginal
beyond its being part of the minimum, so it does bound the complete support.

For `R(x,y)=P_*(x,y)/(h_xh_y)`, when `x<=y` the formula is
`(y+(x-1)/2)/h_y`. It increases with `x` on that region. For fixed `x`, the
exact forward difference in `y` is
`(2y-(x-1)/2)/((3y+1)h_y)`, which is positive when `x<=y`. Symmetry supplies
the other region and the crossing at `x=y`; therefore `R` is coordinatewise
nondecreasing. Since `A_i<=a+c-1`, `B_j<=b+d-1`, this proves the blockwise
bound used in (3). The vectors proportional to `h_(A_i)^(3/2)` and
`h_(B_j)^(3/2)` are positive and normalized by the corresponding `W` sums;
the exponents in (2) match exactly after raising the blockwise bound to the
third power.

If one input marginal is a singleton, its entropy is zero and every score is
at most the largest block value. `P_*` is coordinatewise nondecreasing, so
this largest value is `P_*(a+c-1,b+d-1)`, as used by the direct branch in the
finite verifier. No entropy term is omitted in that case.

## Balanced all-size bound

For `n>=23`, the indices in `W(n,n)` are `1,3,...,2n-1`. The monotonicity of
`h_r^3/r` gives
`h_r^(3/2) <= h_(2n-1)^(3/2) sqrt(r/(2n-1))`; summing yields the stated
`S_n` bound. The integral bound for `S_n` is oriented correctly because
`sqrt(2x-1)` is increasing. The monotonicity of `h_r^3/(3r-1)` gives the
`h_(2n-1)/h_n` comparison in the required direction, while
`h_n^3/n >= h_2^3/2 = 32/27` supplies the remaining lower bound. Cubing (6)
then gives exactly the rational function (7). All canceled denominators are
positive for `n>=23`.

The cross-multiplied difference in (7) has positive coefficients after
substitution `n=x+23`. The integer-only generator constructs its coefficients
by polynomial convolution; the test independently expands the expression
with SymPy and checks equality of every coefficient. Thus coefficient
positivity covers all real `x>=0`, not just sample values.

For `2<=n<=22`, the certificate stores a rational positive probability vector
for each marginal and checks every pointwise inequality directly. The count
`sum(n^2 for n in 2..22)=3794` matches the complete block-position coverage.
The resulting dual certificate applies to every distribution, not only to a
grid of distributions. Root enclosures for the separate `U` comparison use
integer square roots and rational endpoints.

## Exact verification and scope

Using Python 3.14.8 with the maintained SymPy dependency, I ran:

```sh
python research/ai/2026-10-20-full-filtration/entropy_certificate.py \
  --max-size 12 --output results/local/full-entropy-review-2026-10-23.json
python -m unittest discover -s tests -p test_full_filtration_entropy.py -v
```

All 20,736 source tuples on the specified grid passed; 6,095 singleton cases
used the direct maximum-block certificate. The six focused tests passed,
including the complete source-grid replay, all 3,794 balanced pointwise
checks, the exact root enclosures, and independent tail-polynomial expansion.
The finite unequal-source grid is not an all-size theorem. The balanced proof
is all-size only for the specified `C(n,n)^2` score.

The external numerical recurrence remains attributed to OpenAI's pinned
October 2, 2026 paper, [commit
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/build/paper.tex).
The matching profile and determinant-filtration block family remain attributed
to the prior local notes. No tensor-extraction theorem is imported or claimed.
