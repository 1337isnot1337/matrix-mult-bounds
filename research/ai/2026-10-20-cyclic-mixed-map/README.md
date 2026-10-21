# An exact small mixed-map restriction

**AI-CYCLIC-MIXED-RESTRICTION-046.** Over every field, the cyclic product A_2
of three C(2,2) tensors has an ordinary linear restriction to M(2,3,4).
The explicit integer maps give a
finite algebraic certificate. This result has no independent mathematical
review or Lean formalization, and no historical priority is claimed.

This is a construction, rather than a small floating residual. It does
**not** improve the matrix multiplication exponent or the known scalar
profile lower bound. It is a small example for investigating input mixing
and cancellation at larger cyclic sources.

## Tensor identity and certificate

Use the cyclic source convention of
[AI-CYCLIC-FINITE-TARGET-041](../2026-10-20-koszul/cyclic_finite_target.md).
In zero-based coordinates its 64 nonzero coefficients are one at

    X = (i, p+q, s),  index (3*i+p+q)*2+s,
    Y = (j, p, r+s),  index (2*j+p)*3+r+s,
    Z = (i+j, q, r),  index ((i+j)*2+q)*2+r,

for all i,j,p,q,r,s in {0,1}. Each source leg has dimension 12.
The target's 24 nonzero coefficients are one at

    (3*i+j, 4*j+k, 2*k+i),  0<=i<2, 0<=j<3, 0<=k<4.

The three matrices in
[witness.json](../../../results/cyclic-mixed-map-2026-10-20/witness.json)
have shapes 6-by-12, 12-by-12 and 8-by-12. Each entry is stored as
`[row, column, integer coefficient]`; absent entries are zero.
They have respectively 12, 16 and 12 nonzero entries, all equal to +/-1. Thus there is no parameter limit or numerical
tolerance in the claimed identity:

    sum_{a,b,c} T[a,b,c] A[i,a] B[j,b] C[k,c] = M(2,3,4)[i,j,k].

`verify.py` constructs the source and computes the complete contraction
with Python rational arithmetic. All 576 coefficients agree, including
the 552 coefficients required to vanish. Since the entries are integers,
this identity over Z reduces to the same identity over every field,
including characteristic two. The full-rank assertion also follows over
every field from the conciseness of the resulting matrix tensor.

The regression tests also check full row ranks, reject a changed
coefficient, and verify the natural A_a to M(a,a,a) coordinate restrictions
at a=2,3 as controls on the source and target indexing.

## Discovery and exact reconstruction

The retained discovery code and reports are separate from acceptance.
Sixteen seeded real alternating-least-squares starts, each with at most
1000 iterations, were run for each of M(3,3,3) and M(2,3,3). The former
had best full relative error about 0.19571 and produced no witness; this
does not exclude that target. For M(2,3,3), seed 202610224 reached about
0.00014957. Analytic-Jacobian Levenberg--Marquardt refinement reduced the
full relative error to about 3.88e-16. Numerical Jacobian rank was 193 in
252 variables; that floating rank was a discovery diagnostic only.

Greedy zero fixing followed by greedy fixing of selected entries to signs
revealed entries of the form +/-2^(e/4). Exact arithmetic modulo q^4-2
verified the reconstructed algebraic identity. Diagonal source and target
symmetries then removed all fourth roots. These earlier rational matrices are retained under
`discovery/earlier-m233-rational-witness.json`; their identity is replayed
as a regression control. The later construction below strengthens it.

For completeness the source diagonal exponents are

    alpha*i - beta*k + gamma*s + cx,
    alpha*j + beta*p - gamma*L + cy,
    -alpha*H + beta*q + gamma*r - cx - cy.

Their sum vanishes on every source term. The target diagonal exponents
are u_i+v_j, -v_j+w_k, and -w_k-u_i; their sum vanishes on every target
term. The parameter vector retained in the earlier rational witness is ordered
(alpha,beta,gamma,cx,cy,u0,u1,v0,v1,v2,w0,w1,w2).
For every map entry, adding its row and column exponents to the recognized
q-exponent gives a multiple of four, hence a rational power of two.

Starting from that exact M(2,3,3) witness, another 32 seeded real ALS
starts were run for each of M(3,3,3) and M(2,3,4), at Gaussian noise scales
0.01, 0.1, 0.3 and 1.0. The square target again produced no certificate. A further 32 complex
starts with the same four noise scales, seeds 202610300 through 202610331,
also found no certificate; their best full relative error was about
0.19575. These failures do not prove nonexistence.
The M(2,3,4) search reached about 2.47e-13 at seed 202610280; refinement
reached about 3.22e-16. Greedy zero and sign fixing then produced exactly
40 entries in {+1,-1}, with all other entries zero. Direct rational
contraction verified the full integer identity. This last exact check is
the acceptance criterion; solver residuals are not used as certificates.

The actual numerical reports and best/intermediate arrays are retained in
`results/cyclic-mixed-map-2026-10-20/discovery/`. Their original
`exact_certificate: false` or `exact_witness_found: false` fields describe
those numerical stages and are preserved. The exact final certificate is
the separate `certificate.json`. The 229-test first checkpoint and its
rational witness are followed by the strengthened integer certificate;
the final verification receipt records the updated test coverage.

## Consequence and remaining work

Spectral monotonicity and the leg-permutation argument in claim 041 give
P(2,2)>=24^(1/3). This is weaker than the already proved matching-profile
lower bound P_*(2,2)=10/3, since 24 < (10/3)^3. Tensor powers give the
corresponding restrictions to M(2^r,3^r,4^r), but no stronger profile or
exponent follows from that repetition. The earlier dimension screen
already excludes crossing the endpoint ceiling using only independent
matrix products extracted from the a=2 symmetrized source.

The useful next question is whether these cancellations have a structural
description that scales to a=4 or larger. The exponent-improving
A_4 to M(10,10,11) target is still unconstructed; ordinary restrictions
to it are excluded by claim 042, so a construction there must be singular.
This small ordinary restriction does not supply that missing degeneration.

## Reproduction and attribution

From the repository root, using root requirements.txt:

```sh
python research/ai/2026-10-20-cyclic-mixed-map/verify.py
python -m unittest discover -s tests -p test_cyclic_mixed_map.py -v
```

The verifier uses only the standard library; the row-rank regression uses
the existing SymPy dependency. Optional discovery scripts were run with
Python 3.14.8, NumPy 2.5.4 and SciPy 1.18.1, with
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1`. They now write intermediate
files under `results/local/cyclic-mixed-map/`; execute the scripts in this
order to repeat the successful discovery pipeline:

1. `cyclic_als_233.py`
2. `refine_cyclic_233.py`
3. `sparsify_cyclic_233.py`
4. `normalize_cyclic_233.py`
5. `exact_cyclic_233.py`
6. `rationalize_cyclic_233_small.py`
7. `extend_cyclic.py`
8. `refine_cyclic_234.py`
9. `sparsify_cyclic_234.py`
10. `normalize_cyclic_234.py`

The final normalized arrays are integers. The maintained verifier replays
the saved integer maps directly; rerunning the numerical discovery is not
needed to reproduce the certificate.

The separate `cyclic_als.py` retains the unsuccessful M(3,3,3) experiment.
Numerical trajectories may depend on numerical-library versions. These
optional dependencies are not needed for verification and have not been
added to maintained requirements. The new maps and searches were generated
by the continuing Codex research session directed by the repository owner.
The 9/4 theorem and spectral framework remain external work; the cyclic
source indexing and target criterion reuse the cited local claims.
