# The remaining H1100 Cartan character pattern

October 20, 2026. EXP-CYCLIC-CARTAN-FRONTIER-051, exact finite
classification and numerical experiments; unreviewed.
**The surviving character pattern is not a tensor construction.**

Keep only the diagonal torus of the SL2 action in [the main note](README.md).
Normalize its source weights to k-i-s on X=(i,k,s), L-j-p on
Y=(j,p,L), and H-q-r on Z=(H,q,r). Their sum is zero at every source
coefficient. At a=4, the common leg character is

    S(t)=t^-6 P(t), P(t)=(1+t+t^2+t^3)^2(1+t+...+t^6).

Its coefficients at weights -6,...,6 are

    1,3,6,10,13,15,16,15,13,10,6,3,1.

We allow arbitrary torus vertex representations U,V,W of dimensions
10,10,11, with integer weights, and intertwining leg maps into
U tensor V*, V tensor W*, W tensor U*. Source weights under the
unrescaled SL2 torus are twice the displayed weights. A common parity
of vertex weights can be removed by translation before this rescaling.
Basis changes within weight spaces are unrestricted.

## Exhaust the necessary characters

Conciseness of a limiting matrix tensor requires a surjective leg map
at generic parameter values. Therefore all three target characters
must be coefficientwise at most S(t). Write U,V,W also for their
nonnegative Laurent character polynomials, and use star for t -> t^-1.
Since S=S*, the two 110-dimensional leg conditions give

    U W* = S-D,  V W* = S-E,

where D,E have nonnegative integer coefficients summing to two.
Thus t^6 D is t^i+t^j with 0<=i<=j<=12, subject to nonnegative
remaining coefficients. Exactly 89 of the 91 pairs are permitted;
subtracting twice at either endpoint is invalid.

For each Q=P-t^i-t^j, remove its leading and trailing zero
coefficients, recording the monomial shift. Exhaust all factorizations
Q_red=f g with nonnegative integer coefficients, f(1)=10, g(1)=11,
and nonzero endpoints. Recover U=f and W=reverse(g), with the relative
shift determined by the removed monomial and deg(g).

The maintained search uses integer coefficient equations, without
assuming an irreducible factorization returned by a computer algebra
system. For each split of the total degree and each positive divisor
f0 of Q_red(0), g0 is fixed. At step k, enumerate every nonnegative
f_k within the remaining sum budget. The coefficient equation then
fixes

    g_k=(Q_k-f_k g0-sum_(1<=i<k) f_i g_(k-i))/f0.

Reject a negative, nonintegral or over-budget value, or a nonzero
coefficient outside the chosen degree. Check the leading coefficients,
both total sums and the entire final product. This is exhaustive by
induction on k. The finite search visits 124162 nodes.

There are four ordered (U,W) candidates, with coefficients listed from
their minimum weight upward. W is normalized to have minimum weight 0.

| Removed exponents | U coefficients | W coefficients | Minimum U weight |
| --- | --- | --- | ---: |
| 2,10 | 1,2,1,2,1,2,1 | 1,1,2,3,2,1,1 | 0 |
| 3,4 | 1,2,2,2,2,1 | 1,1,2,2,1,2,1,1 | 1 |
| 3,9 | 1,1,2,2,2,1,1 | 1,2,2,1,2,2,1 | 0 |
| 8,9 | 1,2,2,2,2,1 | 1,1,2,1,2,2,1,1 | 1 |

Pair candidates with the same W, and check the remaining condition
U V* <= S coefficient by coefficient. Exactly one triple survives,
up to a common translation of all vertex weights:

    U=V=(1,1,2,2,2,1,1), W=(1,2,2,1,2,2,1)

at weights 0,...,6. Here U W*=S-t^-3-t^3. The U V* coefficients at
weights -6,...,6 are 1,2,5,8,11,14,16,14,11,8,5,2,1, all at most S.
An independent SymPy rational factorization discovery calculation
gave the same four pairs; acceptance uses the exhaustive integer search.

This result classifies necessary characters for this torus action. It
does not give any leg maps or imply that the surviving tensor exists.
It does not cover arbitrary symmetry-breaking constructions.

The product-filtration worker's concurrent
[quantum recoupling family at the inspected revision](https://github.com/1337isnot1337/matrix-mult-bounds/blob/46e02801a03aadcdb9573a5ee09ea38e9762fe8f/research/ai/2026-10-20-quantum-recoupling/family.md)
already supplies legitimate parameter-dependent local bases and studies
coupled singular normalizations. That route is attributed to its worker;
it is not introduced by this character screen. Centering the surviving
characters and reverting to standard SL2 weights gives the formal identities

    U=V=chi(V6)+chi(V2), W=chi(V6)+chi(V4)-chi(V0).

The negative V0 term explains why W is not a classical SL2 representation.
It also gives a concrete character target for that varying-basis lane.
No quantum-module realization, tensor-level cancellation, or usable root
limit is asserted here.

## Completed construction pilots

Two optional NumPy programs retain actual completed attempts. No floating
residual is an acceptance certificate.

At a=2, Cartan-intertwining maps to M3 have 26 allowed entries on each
leg. An exact embedded M2 restriction initializes 32 ALS starts: 16
real and 16 complex, seeds 202610420 through 202610451, each at most
1000 sweeps. Noise scales .03,.1,.3,1 repeat. Every target coefficient
is checked; other-weight coefficients vanish identically by the ansatz.
The best full relative residual was 0.19572114671489324. No exact map
or degeneration was found, and the finite pilot proves no exclusion.

For H1100, use the unique character pattern above, with all vertex
weights negated to match the chosen embedded M4 control. The maps have
1222,1316,1316 allowed entries. Four real and two complex starts used
seeds 202610461 through 202610466, 200 ALS sweeps each, and repeating
noise scales .03,.1,.3,1. Each run samples distinct secondary vertex
weights from [-20,20] and imposes zero coefficients at negative
secondary degree, and the M(10,10,11) coefficients at degree zero.
Positive secondary degrees are omitted. Global map norms are equalized
and a diagonal target-stabilizer balancing pass uses at most 20 sweeps.

Contractions are assembled in source-weight blocks. Before optimization,
the program checks the exact embedded M4 tensor and compares all
three block-contraction assemblies with a direct full contraction of
a seeded perturbation. Every retained source coefficient is accounted
for by weight conservation; this is a computational reduction, not
an extra discarded-coefficient assumption.

All six runs completed. The best masked residual was
0.8198673783546997. Several runs escaped to large norms and large
unweighted coefficients; the largest final map norms exceeded 1e9.
These failures do not exclude the character survivor, this secondary
grading class, or any general degeneration. The earlier
[masked-residual warning](../2026-10-20-cyclic-singular-search/README.md)
applies. Reports, best iterates and the H1100 progress log are retained.

## Reproduction

The exact frontier uses only the Python standard library:

```sh
python research/ai/2026-10-20-cyclic-equivariant/torus.py
python -m unittest discover -s tests -p test_cyclic_torus.py -v
```

The tests replay all 89 deficit cases and independently compare the
positive-factor search with brute-force coefficient vectors on small
products. Optional discovery used NumPy 2.5.4, and writes to ignored
`results/local/`:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python research/ai/2026-10-20-cyclic-equivariant/discovery/cartan_m3.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 CARTAN_STARTS=6 CARTAN_ITERATIONS=200 python research/ai/2026-10-20-cyclic-equivariant/discovery/cartan_h1100.py
```

Numerical trajectories can vary with BLAS and library versions. There
is no independent mathematical review, formalization or exponent gain.
