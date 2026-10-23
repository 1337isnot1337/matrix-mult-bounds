# Audit of the unequal-filtration entropy certificate

**Claim:** `AI-UNEQUAL-ENTROPY-001`, the bound for the explicitly defined
certificate `U(a,b,c,d)` in
[`research_note.md`](../ai/2026-10-20-unequal-entropy/research_note.md).

**Source pin:** repository commit `1c04903c215f396150605c0778024e856ec0b0d4`;
the reviewed note is Git blob `8e27b73d47a0d729dc1c47a1f579ff3b28012770`,
and its verifier is Git blob `43b78098f54e08950ac3ea134a34fdaff56a0307`.

**Conclusion:** I found no gap in the all-size proof that
\[
\frac{U(a,b,c,d)}{P_*(a,b)P_*(c,d)}\le
\frac{81}{350}\left(1+\frac{14\sqrt{14}}{27}\right)^{4/3}
\]
for `a,b,c,d >= 2`, with equality only at `(2,2,2,2)`. The proof controls
the stated analytic certificate `U`; it is not a bound on the exact entropy
optimum, a weighted extraction theorem, a tensor construction, or an exponent
improvement. This first-party Codex audit is not independent human review or a
Lean formalization. The claim stays `proof-written-unreviewed`.

## Audit of the all-size reduction

The symmetries used to place a minimum length at `a` are valid: exchanging the
two source tensors preserves the two `W` factors up to order, while exchanging
both input pairs swaps those `W` factors and the symmetric arguments of `R`.
Together these operations act transitively on the four lengths.

For `a` minimal, the two source denominators are exactly
`P_*(a,b)=h_a X/2` and `P_*(c,d)=h_ell Y/2`, with the notation in the proof.
The index set in `W(a,c)` has `a` terms with mean index `c`; the terms in
`W(b,d)` have `m` terms with mean index `M`. The recurrence calculation in
Section 2 gives decreasing forward differences for `w_n=h_n^(3/2)`, so its
piecewise-linear interpolation is concave. Jensen therefore gives
`W(a,c) <= a h_c^(3/2)` and `W(b,d) <= m h_M^(3/2)`.

The substitutions from (4) are applied in the correct directions. If
`N=max(c,M)` and `e=min(c,M)`, then `N<=v` because
`b+d-1>=M` and `a+c-1>=c`; also `e>=ell` because `M>=d`. Hence
\[
\frac{h_N^3}{h_v^3}\le\frac Nv,\qquad
\frac{h_e^3}{h_\ell^3}\le\frac{3e-1}{3\ell-1}.
\]
Cubing the Jensen-based bound and using these inequalities yields exactly (7).
All cross-multiplied factors are positive for the stated positive lengths,
so (8) is equivalent to the required `97/100` bound for this upper
certificate.

For the discrete-concavity step, write
`r_n=(1+1/(3n))^(3/2)` and `d_n=w_(n+1)-w_n`. Convexity gives
`r_n-1 >= 1/(2n)`, and the mean value theorem gives the stated upper bound
for `r_(n+1)-1`. Substitution gives (5); its denominator minus numerator is
`54n^3+108n^2+42n-4`, positive for every `n>=1`. The term indices in `W`
are an arithmetic progression with mean `max(a,c)`, including when one
length is one, so the Jensen application has no endpoint exception.

## Audit of the tail certificates

The six weak ordering cases for `b,c,d` are represented by their nonnegative
successive gaps; ties lie on shared boundaries. In the two cases with `c`
largest, the maps `(x,z)=(x'+z',z')` and `(x,z)=(x',x'+z')` cover the
respective regions `z<=x` and `z>=x`, including equality. They also fix which
of `a+c-1` and `b+d-1` is `u` or `v`. Thus the eight polynomial cones cover
all cases after placing a minimum at `a`.

For `a>=11`, `h_a^3/a` is increasing, so replacing it by `h_11^3/11` makes
the left side of the desired inequality smaller. The eight resulting
polynomials have degree eight and strictly positive coefficients. For each
minimum `2,...,10`, a shifted polynomial with nonnegative coefficients proves
the tail whenever its corresponding gap reaches the listed threshold.
The three tails cover the union where any gap reaches threshold; the remaining
box has all gaps below threshold. Therefore the 37 tuples are the complete
residual set, not sampled representatives.

The standard-library verifier constructs the coefficient lists from (8) and
(9), removes zero coefficients, rejects any negative coefficient, and hashes
the normalized lists only after those sign checks. Its exact residual bounds
use rational square-root enclosures with denominator `10^15`; monotonicity of
the positive formula in each `W` gives valid lower and upper enclosures for
the cubed ratio. The exceptional radical is separately expanded in
`Q(sqrt(14))`. Every nonexceptional residual has upper endpoint below
`(97/100)^3`; the exceptional interval lies strictly between the stated
rational decimal cubes. The proof's conclusion for every size follows from
the coefficient and cone arguments, not from the finite test box.

## Verification and limits

Using Python 3.14.8, I regenerated the exact certificate and ran:

```sh
python research/ai/2026-10-20-unequal-entropy/unequal_entropy.py \
  --output results/local/unequal-entropy-review-2026-10-23.json
python -m unittest discover -s tests -p test_unequal_entropy.py -v
```

The replay produced eight large cones with 3,614 positive coefficients,
72 small-minimum cases with 216 shifted certificates and 29,943 nonzero
coefficients, and all 37 residuals (largest coordinate 10). The five focused
tests passed, including cone recovery, scalar-polynomial agreement, radical
enclosures, and negative-coefficient rejection. These checks validate the
finite certificate construction; they do not independently review the
mathematical proof or upgrade the claim status.

The external dependency is the recurrence and exponent framework in OpenAI's
pinned October 2, 2026 paper, [commit
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/build/paper.tex).
The matching profile and earlier score `U` remain attributed to the local
notes identified by `sources.json`; no theorem or priority is reattributed.
