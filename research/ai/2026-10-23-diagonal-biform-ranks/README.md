# Diagonal polynomial biform ranks

Written, unreviewed all-field proofs. Finite exact acceptance passed. No exponent gain.

The all-degree source slice R_a(f(xz)), with deg f=d<a and nonzero
endpoint coefficients, has exact rank

    a^2 + sum_(h=0)^(d-1) rank T_(a,h),

where T_(a,h)[u,v]=c_(h+1+v-u) is explicit Toeplitz.
For a>=3 and f(t)=c0+c1*t+c2*t^2 with c0*c2!=0,
rank equals a^2+2a, except a determinant recurrence can lower it by one.

Read proof.md for the proof and QUESTION.md for the remaining constructive
question. Run from the repository root:

    python research/ai/2026-10-23-diagonal-biform-ranks/verify.py --output results/local/diagonal-biform-controls.json
    python -m unittest tests.test_diagonal_biform_ranks -v

Finite report: results/diagonal-biform-ranks-2026-10-23/controls.json.
