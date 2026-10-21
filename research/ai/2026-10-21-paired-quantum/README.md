# Exact calibration of paired quantum recoupling

**Status:** AI-derived finite calculations and written interpretation,
unreviewed, October 21, 2026. Claim `AI-PAIRED-QUANTUM-001`.
There is no exponent improvement and no construction of the proposed
paired matrix direct sum.

The prescribed quantum Clebsch--Gordan maps below give a concrete family
of bases for the paired source. At a primitive fourteenth root, the
rowwise regular first-leg map for `P_10` has rank **91**, below the full
first-leg dimension 100 of the proposed target. Small examples also show
why matching the three dimensions of a matrix tensor is insufficient:
the size-two limit has format `(4,4,4)` but is not `M(2,2,2)`.

These statements concern the specified normalization. Coupled Laurent
normalizations, cancellations at the tensor level, and different bases
remain open.

## 1. Exact source equivalence

Use the coproduct convention and the rational functions established in
[the quantum recoupling package](../2026-10-20-quantum-recoupling/family.md).
Its external convention is
[Arun Ram, Quantum SL2, September 25, 2012](https://soimeme.org/~arunram/Notes/QuantumSL2.html).
The formulas used here are those derived in the project package; no
semisimplicity statement at a root is assumed.

Put `D=a-1` and `h=2D`. Reverse the long coordinates of the usual paired
source, so its support is

\[
A_{p,q}B_{y,h-q-v}C_{h-p-y,v},\qquad 0\le p,q,y,v\le D.
\]

Over `Q(q)`, define

\[
A'_i=q^{-\binom i2},\qquad
B'_i=q^{-Di-\binom i2},\qquad
G_s=\frac{(-1)^s q^{\binom s2+s(h-s-1)}}{{h\brack s}_q}.
\]

Here the symmetric quantum binomial coefficient is the one used by the
dependency. The local diagonal factors are

\[
d_A(i,j)=A'_iA'_j,\qquad
d_B(i,z)=B'_iG_{h-z},\qquad
d_C(z,j)=G_{h-z}B'_j.                                      \tag{1}
\]

On each source support position their product is

\[
d_A(p,q)d_B(y,h-q-v)d_C(h-p-y,v)=f(p,y)f(q,v),               \tag{2}
\]

where `f` is the trilinear invariant coefficient from the dependency.
In particular this tensor is source-equivalent by explicit local diagonal
maps, independently of any claim about quantum intertwiners after
regrouping. The verifier checks (2) as an identity in `Q(q)` in all 353
positions for `a=2,3,4`.

Let `Q_(m,n)(q)` be the inverse of the generic Clebsch--Gordan basis
matrix from that package. Columns of the original basis are indexed by
`(k,l)`, where `0<=k<=min(m,n)` and `0<=l<=m+n-2k`. Every basis vector
lies in weight index `k+l`. The three local maps are

\[
M_A=Q_{D,D}\operatorname{diag}(d_A),\quad
M_B=Q_{D,h}\operatorname{diag}(d_B),\quad
M_C=Q_{h,D}\operatorname{diag}(d_C).                         \tag{3}
\]

Every map is invertible over `Q(q)`. Thus (3) specifies a legitimate
varying-basis family of the paired source. This statement does not use
an unproved quantum composition-factor decomposition of the tensor.

## 2. The prescribed regular normalization

Fix a cyclotomic polynomial `Phi_N(q)` and let `nu` be its valuation.
For each nonzero row `r` of a local map, set

\[
e_r=\min_j\nu(M_{rj}),\qquad
\widetilde M_{rj}=\Phi_N(q)^{-e_r}M_{rj}.
\]

All entries of `tilde M` are regular at every primitive `N`th root.
The verifier takes their residues exactly in
`Q[q]/(Phi_N(q))` and computes the rank separately on each weight block.
There are no floating-point rank decisions.

For `a=10`, `N=14`, the first map has dimension 100 and rank 91. Its
rank deficits at weight indices `7,8,9,10,11` are respectively
`1,2,3,2,1`; every other weight block has full rank. Thus the constant
tensor obtained from the three regular maps has first flattening rank at
most 91. It cannot be

\[
M(4,11,10)\oplus M(10,12,6),
\]

whose first flattening rank is `4*10+10*6=100`. Any subsequent constant
local maps also preserve this obstruction. An additional singular tensor
normalization is outside this statement.

The report also calculates all three maps for `a=2,3,4` at root orders
`3,4,6,8,10,12,14`. Some useful calibrations are:

| `a` | Root order | First map rank | Second map rank | Third map rank |
|---:|---:|---:|---:|---:|
| 2 | 3 | 4 | 4 | 4 |
| 2 | 4 | 3 | 6 | 6 |
| 3 | 8 | 6 | 12 | 12 |
| 3 | 10 | 9 | 12 | 12 |
| 3 | 12 | 9 | 10 | 10 |
| 4 | 14 | 16 | 18 | 18 |

## 3. A small limit with the right dimensions but the wrong tensor

Take `a=2`, let `zeta` be a primitive cube root, and apply the regular
maps. The exact constant tensor has flattening ranks `(4,4,4)` and 36
nonzero coefficients in the original recoupled coordinates. Projecting
onto coordinates `0,1,2,3` on each leg identifies its support with a
tensor in `Q(zeta)^4 tensor Q(zeta)^4 tensor Q(zeta)^4`.

Let its first-leg slices be the four `4`-by-`4` matrices
`S_0,S_1,S_2,S_3`, in the indexing order from (3). The calculation gives

\[
\det S_1=-\frac{7}{16}(\zeta+1)\ne0.
\]

Set `L_i=S_1^{-1}S_i`. Append the flattened matrix `L_0^2` to the four
flattened matrices `L_i`. On flattened column indices `0,1,2,4,5`, the
resulting `5`-by-`5` minor is

\[
\frac{\zeta+19}{343}\ne0.                                 \tag{4}
\]

Consequently the normalized four-dimensional slice space is not closed
under matrix multiplication.

For comparison, every first-leg slice space of a tensor isomorphic to
`M(r,b,r)` has the form `U (Mat_r tensor I_b) V` for invertible `U,V`.
Normalizing by any invertible slice conjugates it to the algebra
`Mat_r tensor I_b`, so closure under multiplication is necessary. Formula
(4) therefore proves that this particular limit is **not** `M(2,2,2)`.
It places no restriction on other restrictions or degenerations of `P_2`.

The same exact screen at `a=3`, root order 10, gives flattening ranks
`(9,12,12)` but a ten-dimensional span after appending one product to
the normalized nine-dimensional slice space. Hence that particular
limit is not `M(3,4,3)` either. The report contains the nonzero minor.

## 4. Reproduction and scope

From the repository root, with the root requirements installed:

```sh
python research/ai/2026-10-21-paired-quantum/screens.py \
  --output results/paired-quantum-2026-10-21/certificate.json
python -m unittest discover -s tests -p test_paired_quantum.py -v
```

The certificate consists of 64 local maps, 353 formal source-coefficient
identities, and two exact small tensor limits. The test suite includes an
independent SymPy determinant check and the full size-ten first-map
calculation. The exact Clebsch--Gordan formulas are imported from the
maintained quantum package, whose source and convention are identified
above.

The unconstructed direct sum remains a useful target because the paired
spectral calculation would convert it to a smaller exponent. The
calculations here reject only one natural leading-map choice and prevent
dimension coincidences from being mistaken for matrix multiplication.
