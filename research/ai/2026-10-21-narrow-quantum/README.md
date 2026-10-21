# Unequal paired quantum maps and exact root-eight faces

Claim identifier: `AI-NARROW-QUANTUM-001`.

Status: exact source identities, explicit intermediate degenerations, and
written exclusion arguments; unreviewed. **No smaller matrix multiplication
exponent is claimed.**

This package extends the paired quantum source equivalence to unequal
lengths. It constructs 23 explicit Laurent limits of `Q_(3,2)` over
`Q(zeta_8)` and excludes `M(3,2,3)` from every one of these fixed limits.
The strongest two faces pass every first-leg Koszul test, but a long-leg
test rejects each by one rank. The original `Q_(3,2)` target remains open.

## 1. An exact generic source equivalence for all lengths

For integers `n,m >= 2`, put `D=n-1`, `E=m-1`, and `h=D+E`. Our source is

\[
Q_{n,m}=\sum_{p,r=0}^{D}\sum_{y,v=0}^{E}
A_{p,r}B_{y,r+v}C_{p+y,v}.
\]

Its format is `(n^2,m(n+m-1),m(n+m-1))`. Reverse the long coordinate in
the second and third legs. A source term then has positions

\[
A_{p,r}B_{y,h-r-v}C_{h-p-y,v}.                         \tag{1}
\]

Write `[h choose s]_q` for the symmetric quantum binomial coefficient,
as implemented in the maintained
[quantum core](../2026-10-20-quantum-recoupling/quantum.py). Define

\[
\alpha_i=q^{-\binom i2},\qquad
\beta_j=q^{-Dj-\binom j2},\qquad
\gamma_s=\frac{(-1)^s q^{\binom s2+s(h-s-1)}}{[h\mathbin{\mathrm{choose}}s]_q}.
\]

The three invertible diagonal substitutions are

\[
d_A(i,j)=\alpha_i\alpha_j,\qquad
d_B(i,z)=\beta_i\gamma_{h-z},\qquad
d_C(z,j)=\gamma_{h-z}\beta_j.                         \tag{2}
\]

For the generic invariant coefficient

\[
f_{D,E}(i,j)=
\frac{(-1)^{i+j}
q^{j(i-D)+(i+j)(h-i-j-1)}}{[h\mathbin{\mathrm{choose}}(i+j)]_q},
\]

these substitutions satisfy the coefficient identity

\[
d_A(p,r)d_B(y,h-r-v)d_C(h-p-y,v)
=f_{D,E}(p,y)f_{D,E}(r,v).                           \tag{3}
\]

Indeed, `binom(i+j,2)-binom(i,2)-binom(j,2)=ij` proves the equality of
exponents, and the signs and quantum binomial denominators agree term
by term. This proves (3) for all `n,m`; the verifier also exhausts all
841 source terms across `2<=n,m<=4` as finite controls.

Let `G_(u,v)` denote the inverse generic Clebsch--Gordan basis matrix in
the core. One possible set of local maps is

\[
M_A=G_{D,D}\operatorname{diag}d_A,\quad
M_B=G_{E,h}\operatorname{diag}d_B,\quad
M_C=G_{h,E}\operatorname{diag}d_C.                    \tag{4}
\]

Every map is invertible over `Q(q)`. For the coupled families below,
we instead set `M_A=diag d_A`, preserving the original first-leg basis.
Equation (3) proves the source equivalence directly. No claim about
arbitrary regroupings of quantum invariant tensors is needed.

The quantum conventions come from the existing core and its
[Arun Ram source](https://soimeme.org/~arunram/Notes/QuantumSL2.html).
The source equivalence and finite faces here are repository-derived
calculations, not assertions from that source.

## 2. The ordinary local limit loses too many coordinates

For `n=3,m=2`, specialize at a primitive eighth root `zeta`. The
uniformizer is `Phi_8(q)=q^4+1`. Divide each local-map row by its minimum
uniformizer valuation and take its residue. Exact contraction of the
original source gives these tensor concisions:

| First-leg basis | Regular limit concision |
|---|---|
| All three Clebsch--Gordan maps | `(6,5,5)` |
| First leg kept diagonal | `(9,5,5)` |

The target has format `(9,6,6)`, so neither ordinary limit supplies it.
These statements concern the prescribed row normalization only.

## 3. The coupled Laurent limits are actual source degenerations

Keep the first leg diagonal, and let `r_j` be the minimum valuation of
row `j` of its local map. The generic transformed tensor has exactly 83
nonzero rational-function coefficients `R_(i,j,k)(q)`. After subtracting
the three row minima, their valuations are 0 on 50 positions and 1 on
33 positions. Every other position in the full `(9,8,8)` box vanishes
identically over `Q(q)` after contraction.

The file [families.json](families.json) supplies 23 fixed pairs `(D_0,W)`.
Here `D_0` is a positive integer unrelated to the length parameter `D`
above. Set

\[
q(t)=\zeta\left(1-\frac{t^{D_0}}4\right),\qquad
L_X(t)=\operatorname{diag}
\left(t^{W_j-D_0r_j}\right)M_X(q(t)).                 \tag{5}
\]

Since

\[
q(t)^4+1=t^{D_0}-\frac38t^{2D_0}
+\frac1{16}t^{3D_0}-\frac1{256}t^{4D_0},
\]

the exponent of a nonzero transformed coefficient is

\[
D_0\bigl(\nu(R_{i,j,k})-r_i-r_j-r_k\bigr)
+W_i+W_j+W_k.                                      \tag{6}
\]

The verifier checks (6) is nonnegative for every one of the 83 generic
coefficients of every fixed family. Its leading coefficient is the
exact cyclotomic residue when (6) equals zero. Thus the complete tensor
has no negative Laurent coefficient. The maps in (5) are generically
invertible, and their limits are genuine degenerations of `Q_(3,2)`.
Rational local maps can also be truncated to sufficiently long finite
Laurent polynomials without changing the constant tensor coefficient.

The certificate gives all row minima, integer local exponents, generic
coefficient functions, leading tensors, and constant coordinate
projections to concise formats. Its cyclotomic coefficient lists are
polynomials in `zeta`, in descending powers.

The proposals originated from 1,000 numerical LP objectives. Replay
uses the fixed integer vectors and exact arithmetic; it does not use
an LP solver or any numerical rank decision. The 23 stored faces are
not asserted to exhaust every possible choice of weights or bases.

## 4. Why none of the fixed faces yields the target

Nine faces lose first-leg concision, falling below the target's nine
dimensions. Ten further faces retain first-leg concision nine but
have an explicit basis slice of rank one. Every nonzero first slice of
`M(3,2,3)` is two copies of a nonzero `3 x 3` matrix, and therefore has
rank at least two.

The existence of a nonzero first covector with slice rank at most one
is a closed condition on tensors with a fixed first-leg space. The
incidence of such pairs is determinantal and closed in the product
with the projective covector space. Projection is closed because
projective morphisms are proper and hence universally closed; see
[Stacks, Tag 01W7](https://stacks.math.columbia.edu/tag/01W7) and
[Tag 01W0](https://stacks.math.columbia.edu/tag/01W0).
First-leg changes are generically invertible when a degeneration
retains all nine concise first coordinates. Changes on the other legs
cannot increase slice rank. Consequently, the rank-one witnesses
exclude all further degenerations to this target, not just ordinary
restrictions of these ten faces.

For the remaining four faces, the verifier computes every exterior
degree of the Koszul flattening along each of the three legs. A useful
first obstruction for each is:

| Fixed family | Concise format | Tested leg and power | Face rank | Target rank |
|---|---:|---|---:|---:|
| `face0` | `(9,8,7)` | third leg, power 1 | 62 | 63 |
| `face1` | `(9,7,8)` | second leg, power 1 | 62 | 63 |
| `face3` | `(9,6,8)` | first leg, power 1 | 53 | 54 |
| `face12` | `(9,8,6)` | first leg, power 7 | 53 | 54 |

The first two faces pass every first-leg test. The long-leg obstruction
is therefore essential. A Koszul rank cannot increase under a tensor
degeneration because its matrix entries are linear in the tensor.

The comparison also accounts for unused first-leg dimensions. If the
target's intrinsic ranks are `k_p` and it is embedded into a first leg
with `d` extra zero coordinates, its rank is

\[
\sum_{j=0}^{d}\binom dj k_{p-j}.                    \tag{7}
\]

This follows by decomposing the exterior power by the number of zero
coordinates. In particular, the target's intrinsic long-leg ranks are
`[9,54,105,90,36,6]`, while in dimension seven they are
`[9,63,159,195,126,42,6]`. Comparing a seven-dimensional source directly
with the unpadded six-dimensional list would miss the rank-62 defect.

## 5. Replay and remaining scope

Run from the repository root with the root requirements installed:

```sh
python research/ai/2026-10-21-narrow-quantum/faces.py --output results/narrow-quantum-2026-10-21/certificate.json
python -m unittest discover -s tests -p 'test_narrow_quantum.py' -v
```

The tests cover all formal source controls, complete valuation
inequalities, every recorded exact tensor and obstruction, independent
matrix-target rank formulas, and a deliberately invalid pole-producing
weight vector. The original `Q_(3,2) -> M(3,2,3)` problem remains open.
Other quantum bases, row combinations, and coupled weights are outside
this finite certificate.
