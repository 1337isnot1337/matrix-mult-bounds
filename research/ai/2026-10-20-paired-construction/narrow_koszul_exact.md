# All Koszul degrees for the narrow source Q(3,2)

**Finite exact result: all 25 comparisons pass.** This is a necessary-condition
screen, not a construction or an exponent improvement.

The source is

\[
Q_{n,m}=\sum_{0\le p,q<n\atop0\le y,v<m}
A_{p,q}B_{y,q+v}C_{p+y,v}.
\]

For `(n,m)=(3,2)`, its format is `(9,8,8)`. The proposed target

\[
M(3,2,3)=\sum_{i,k<3\atop j<2}a_{i,k}b_{i,j}c_{j,k}
\]

has format `(9,6,6)`. When the first Koszul factor is B or C, the target's
six-dimensional factor is embedded in the source's eight-dimensional factor.
The zero padding is included before each matrix is built.

## Complete rank table

| Exterior degree p | A source | A target | B source | B target | C source | C target |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 6 | 9 | 9 | 9 | 9 |
| 1 | 72 | 54 | 72 | 72 | 72 | 72 |
| 2 | 272 | 216 | 242 | 222 | 242 | 222 |
| 3 | 568 | 474 | 424 | 354 | 424 | 354 |
| 4 | 720 | 612 | 413 | 321 | 413 | 321 |
| 5 | 568 | 474 | 224 | 168 | 224 | 168 |
| 6 | 272 | 216 | 64 | 48 | 64 | 48 |
| 7 | 72 | 54 | 8 | 6 | 8 | 6 |
| 8 | 8 | 6 | — | — | — | — |

All ranks in this table were computed over the rational numbers from the
signed coefficient matrices. Every value also equals the independently
computed rank modulo 2. Neither the source nor target values are obtained
by assuming a symbolic rank formula.

The target ranks never exceed the source ranks. Since rational and complex
matrix rank agree for these integer matrices, these tests do not exclude a
complex degeneration. In particular, a low-degree pass is not being
extrapolated to untested degrees: both long legs were computed separately at
every degree p=0 through 7.

## Method and reproduction

For first factor V, the matrix implements

\[
K_p(T):\Lambda^pV\otimes W^*\longrightarrow
\Lambda^{p+1}V\otimes U,
\qquad (v_I,\beta)\mapsto
\sum_{a,b,c}T_{abc}(v_I\wedge v_a)\otimes\beta(w_b)u_c.
\]

The code retains the exterior signs. Additive tensor weights split the
matrix into disjoint blocks, and their compatibility is asserted for every
source term. Each block is eliminated independently with exact Fractions;
a second elimination uses integer bit vectors modulo 2.

The source uses the two-dimensional weights

\[
w_A(p,q)=(p,q),\quad w_B(y,j)=(y,-j),\quad w_C(z,v)=(-z,v).
\]

The target uses three-dimensional weights

\[
w_A(i,k)=(i,0,k),\quad w_B(i,j)=(-i,j,0),
\quad w_C(j,k)=(0,-j,-k).
\]

Unused padded coordinates may have arbitrary weights, since they occur in
no tensor term. The largest source matrix has 1008 rows and 1008 columns,
but the weight decomposition reduces the rational eliminations to much
smaller blocks. The report records the dimensions and ranks of every block.

From the repository root:

```sh
python research/ai/2026-10-20-paired-construction/narrow_koszul_exact.py --output research/ai/2026-10-20-paired-construction/narrow-koszul-exact.json
python -m unittest discover -s tests -p test_narrow_koszul_exact.py -v
```

Only the Python standard library is needed. There is no numerical tolerance
and no finite-field inference of an upper bound on complex rank.
