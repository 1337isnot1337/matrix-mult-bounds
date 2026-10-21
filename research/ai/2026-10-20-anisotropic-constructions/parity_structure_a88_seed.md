# A compact integral M15 seed in A88

October 21, 2026. Exact mixed-basis restriction and complete coefficient
replay. This constructs A(8,8) to M15. It does not construct the
larger M27 plus M7 target or improve the matrix multiplication exponent.

Let the two short polynomial spaces consist of degrees at most seven,
and the long space of degrees at most fourteen. Choose

\[
U=(1,x^4,x^7),\qquad
V=(1+x^5,x,x^2,x^3+x^6,x^7).
\tag{1}
\]

The fifteen products, ordered first by U and then by V, are

\[
\begin{array}{ccccc}
1+x^5&x&x^2&x^3+x^6&x^7\\
x^4+x^9&x^5&x^6&x^7+x^{10}&x^{11}\\
x^7+x^{12}&x^8&x^9&x^{10}+x^{13}&x^{14}.
\end{array}
\]

Write e_j for coefficient extraction at degree j. The dual basis is

\[
\begin{array}{ccccc}
e_0&e_1&e_2&e_3&e_7-e_{10}-e_{12}+e_{13}\\
e_4&e_5-e_0&e_6-e_3&e_{10}-e_{13}&e_{11}\\
e_{12}&e_8&e_9-e_4&e_{13}&e_{14}.
\end{array}
\tag{2}
\]

Evaluation on the displayed products proves that (2) is an integer
inverse on both sides. Hence the multiplication basis is unimodular.
No interpolation denominator or floating-point coefficient is used.

Take the cyclic product of the three local outer-product identities.
If vertices are I=(alpha_I,beta_I), with alpha in {0,1,2} and beta
in {0,...,4}, the restriction rows are

\[
\begin{aligned}
X_{I,J}(i,t,s)&=U_{\alpha_I}(i)R_{\alpha_J,\beta_I}(t)V_{\beta_J}(s),\\
Y_{J,K}(j,p,u)&=V_{\beta_K}(j)U_{\alpha_J}(p)R_{\alpha_K,\beta_J}(u),\\
Z_{K,I}(v,q,r)&=R_{\alpha_I,\beta_K}(v)V_{\beta_I}(q)U_{\alpha_K}(r).
\end{aligned}
\tag{3}
\]

Applying (2) to each local pair in the source formula gives exactly
sum_(I,J,K) X_(I,J)Y_(J,K)Z_(K,I), namely M15.

Source coordinates are lexicographic (i,t,s), (j,p,u), and (v,q,r),
with short lengths eight and long length fifteen. Target coordinates
use standard matrix-index order. The three maps therefore have shape
(225,960). There are three nonzero entries in U, seven in V, and
twenty-two in R. Each map has 3 times 7 times 22 = 462 nonzero
entries, all 1 or -1.

## Exact witness and replay

The standard-library verifier checks both inverse identities and the
complete contraction of all 262,144 source coefficients. Its output
has exactly the 3,375 unit coefficients of M15 and no extra terms.

- `parity_structure_a88_seed.py`: integer construction and complete replay.
- `parity_structure_a88_seed_sparse.json`: all three sparse integer maps, with local bases and coordinate conventions.
- `parity_structure_a88_seed_certificate.json`: exact completed coverage.
- `parity_structure_a88_seed_maps.npz`: optional dense A,B,C and x,y,z aliases, plus U,V,R, for numerical initialization. The sparse JSON is sufficient for exact verification.

Reproduce without site packages from the repository root:

```
python -S research/ai/2026-10-20-anisotropic-constructions/parity_structure_a88_seed.py
```

The witness supplies a compact exact starting point for the new source.
The larger target remains unconstructed; no exponent claim follows
from this seed alone. The formula and replay were generated within
this research session, with no external independent review or
formalization claimed.
