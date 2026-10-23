# Retain the full regular right inverse in the Laurent argument

Base: main `1c04903`, including PR105's partial-unit-image theorem.

Question: can the regular right inverse `T=M(F(unit)) C` supplied by the
normalized unit equation exclude first-map poles without compressing the
target, and extend the A4 regular-unit-image exclusion below rank109?

The proposed exact mechanism is `K=I-T B`, an idempotent of rank
`k=N-R` over C((t)). The identity

    K M(F(x)) C = M(F(x)) C - T (B M(F(x)) C)

regularizes the projector product using only regular T and target output.
Specialization bounds the leading first-pole slice by rank k after C,
hence by 2k before C. Once F is regular, a vector in ker F(0) makes
`rank(T(0) Xi(x))<=k`. If `rank T(0)>=r`, the sufficient injectivity
condition is `nu>N-r`. A leading row of B then meets the full-column
source contraction bound, with defect k rather than N-r.

Intended output: an all-order written proof and its exact A4 threshold,
small rational-function controls including singular right inverses and
corrupted-evidence rejection, updated claim/status records, complete local
regression and historical replay, and a focused pull request.

The source rank minimum and ordinary A4 obstruction retain their existing
credit. This is separate from the open conic-jet and fixed-resolvent work.
No arbitrary degeneration exclusion, independent review, formalization,
constructed matrix target or exponent improvement is intended.
