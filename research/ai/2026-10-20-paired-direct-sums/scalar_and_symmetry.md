# Scalar corrections and finite symmetry for paired sources

October 21, 2026. These calculations supply exact obstructions to specified
ordinary equivariant maps. They do not exclude arbitrary maps or singular
degenerations and do not improve the matrix multiplication exponent.

The starting motivation was the independent exact identity
`A(2,2) + one scalar -> M3` in
[the anisotropic spin1 note](../2026-10-20-anisotropic-constructions/parity_balancing_spin1.md).
That identity uses a block triangular matrix embedding and has a rank-one
trace defect. This note investigates whether a comparable correction can
repair the paired sources. The source families are different.

## 1. Sources, fields, and numerical scalar pilot

Use the maintained orientation

\[
Q_{n,b}=\sum_{p,q<n,\;y,v<b}
A_{p,q}B_{y,q+v}C_{p+y,v},\qquad P_a=Q_{a,a}.
\]

The format is `(n^2,b(n+b-1),b(n+b-1))`. The narrow pilot target is
`M(n,b,n)`. An appended scalar means a new coordinate on every leg and
one new source term on those three coordinates. It is never silently
removed from a claimed source.

`narrow_scalar_search.py` tested `Q(3,2) + one scalar -> M(3,2,3)` using
four real ordinary-map ALS starts, each with 1000 iterations and ridge
`10^-12`. The source has format `(10,9,9)` and 37 terms. All 324 target
coefficient positions were included. There are 198 map parameters.

| Seed | Best relative full coefficient error |
| --- | ---: |
| 202610260 | 0.2376728522135205 |
| 202610261 | 0.33387238728897545 |
| 202610262 | 0.3339685624049732 |
| 202610263 | 0.47163614849090285 |

No map was found. These finite failures do not prove impossibility. The
exact control embeds the known integer `P2 -> M2` map, sends the scalar
to zero, and then deliberately activates its three coordinates to check
that the appended source term is counted.

All arguments below are over the complex numbers. Rational certificates
are used after the explicit changes of coordinates stated below.

## 2. A forced tetrahedral kernel for Q(3,2)

In the native binary-form coordinates, the source modules are

\[
A=S^2(\mathbb C^2)^*\otimes S^2(\mathbb C^2)^*,\quad
B=S^1(\mathbb C^2)^*\otimes S^3(\mathbb C^2),\quad
C=S^3(\mathbb C^2)\otimes S^1(\mathbb C^2)^*.
\]

Quaternion generators `i,j` act through commuting involutions because
each total degree is even. Their joint fixed spaces on B and C are

\[
K_B=\langle B_{0,1}-B_{1,2},\ B_{0,3}-B_{1,0}\rangle,
\quad
K_C=\langle C_{1,0}-C_{2,1},\ C_{3,0}-C_{0,1}\rangle.
\]

These are the two character components in the natural tetrahedral
decomposition `V2 + V4 = 3 + 3 + 1' + 1''`. The target with outer
tetrahedral module `3` and middle module `1' + 1''` has two copies of
`3` on each long leg. Thus an equivariant surjection must kill exactly
these two-dimensional source fixed spaces. The same conclusion holds
for the corresponding Klein-four model with a trivial middle module.

The verifier expands all 36 source terms under both signed-permutation
generators and checks covariance without numerical arithmetic. It
checks that each joint fixed space has dimension two.

In the quotient coordinate order recorded in `tetrahedral-kernel.json`,
the slice at first coordinate `A[0,1]` has nonzero entries

\[
(0,1),(1,2),(2,4),(3,1),
\]

all equal to one. Its columns 1, 2, and 4 are independent; all other
columns vanish. Its rank is exactly three. In `M(3,2,3)`, every first-leg
slice is a matrix tensored with `I2`, so every slice rank is even. An
invertible first-leg basis change preserves this property of the entire
slice space. Consequently this forced equivariant compression is
impossible. Arbitrary compression kernels are not covered by this
argument.

## 3. Full diagonal SL2 cannot be repaired by trivial scalars

Write `Vd=S^d(C^2)`. For P3 the source legs decompose as

\[
A=V_0\oplus V_2\oplus V_4,
\qquad B=C=V_2\oplus V_4\oplus V_6.
\]

The target M3, with each physical space equal to V2, has
`End(V2)=V0+V2+V4` on every tensor leg. These character identities are
checked exactly by the verifier.

Under equivariant maps, the target identity component on B can receive
nothing from the original source B, which has no V0. If all appended
scalar summands carry trivial SL2 actions, their A and C images also lie
in the one-dimensional identity components. Therefore contraction with
the target B identity has A-C rank at most one, regardless of the
number of appended trivial scalar summands. The identity slice of M3
has rank nine. This excludes the full diagonal-SL2 model with any
number of these trivial scalar summands.

Counting the scalar terms individually would give only the weaker
necessary inequality `r >= 9`; their collinear invariant images give
the stronger obstruction just proved. This argument does not apply to
nonsymmetric maps or to auxiliary tensors carrying nontrivial modules.

## 4. Exact Cartesian coordinates and the A4 fixed sector

The tetrahedral group gives a wider ordinary-map model. Put

\[
X=x^2-y^2,\qquad Y=\mathrm i(x^2+y^2),\qquad Z=2xy.
\]

Then `X^2+Y^2+Z^2=0`. The changes of basis from binary quadratics to
`(X,Y,Z)` and from binary quartics to

\[
(X^2,Y^2,XY,YZ,ZX)
\]

have determinants `-4i` and `-64`, respectively. They are invertible
over Q(i). Binary-form multiplication becomes the following exact map
`mu: U tensor U -> W`, where U has basis X,Y,Z and W has the displayed
five-element basis:

\[
\mu(X,X)=X^2,\quad \mu(Y,Y)=Y^2,\quad
\mu(Z,Z)=-X^2-Y^2,
\]

with the six off-diagonal products equal to their named basis elements.
The two-factor source has coefficients

\[
\widetilde P_3=
\sum_{p,q,y,v,z,j}
\mu_{p,y}^{z}\mu_{q,v}^{j}
A_{p,q}B_{y,j}C_{z,v}.
\]

This is P3 in the stated invertible coordinates and has 100 nonzero
terms. All subsequent Cartesian calculations use rational coefficients.

Generate A4 on U by the sign matrix `diag(1,-1,-1)` and the cyclic
permutation `X -> Y -> Z -> X`. Its action on W follows by multiplication.
The source modules are `U* tensor U*`, `U* tensor W`, and `W tensor U*`;
U is self-dual for these orthogonal generators. The target is the trace
tensor `sum Eij tensor Ejk tensor Eki`, with all three physical spaces U.

The Klein-four fixed coordinate spaces are, in cyclic order,

| Tensor leg | Source Cartesian coordinates | Target coordinates |
| --- | --- | --- |
| A | `A00,A11,A22` | `E00,E11,E22` |
| B | `B0,3; B1,4; B2,2` | `E00,E11,E22` |
| C | `C3,0; C4,1; C2,2` | `E00,E11,E22` |

Restricting all three legs to these spaces gives exactly

\[
N=\sum_{\{i,j,k\}=\{0,1,2\}} e_i\otimes e_j\otimes e_k.
\]

The target fixed-sector tensor is D3. Every slice of N is of the form

\[
\begin{pmatrix}0&a_2&a_1\\a_2&0&a_0\\a_1&a_0&0\end{pmatrix}.
\]

A nonzero symmetric rank-one matrix cannot have a zero diagonal over C:
writing it as a nonzero scalar times `u u^T` would force every coordinate
of u to vanish. Hence every nonzero slice of N has rank at least two.
D3 has rank-one slices. For an ordinary equivariant restriction without
auxiliary tensors, all three fixed-sector maps would have to be
invertible, because both fixed spaces have dimension three and the
target is concise. This proves that ordinary A4-equivariant
`P3 -> M3` is impossible.

## 5. Classifying every trivial-scalar correction of the fixed sector

Allow any number r of scalar summands, each with trivial A4 action.
Every such scalar can map only into the target A4 invariant line on
each leg. Their total image is therefore a single coefficient

\[
\kappa\,(1,1,1)^{\otimes3}.
\]

Each original fixed-sector map commutes with the cyclic permutation, so
it is circulant. Let its three Fourier eigenvalues be `A_s,B_s,C_s`,
where `s=0,1,2` and `w^2+w+1=0`. Using the unnormalized Fourier basis,
the only nonzero coefficients of N are

\[
\widehat N_{000}=\widehat N_{111}=\widehat N_{222}=6,
\quad \widehat N_{abc}=-3
\quad\text{for the six permutations of }(0,1,2).
\]

The corresponding nine coefficients of D3 all equal three. Every other
Fourier coefficient is zero. This entire table is checked exactly in
`Z[w]/(w^2+w+1)`.

The six mixed-sector equations imply that all nine eigenvalues are
nonzero. Comparing them shows that the ratios

\[
r_1=A_1/A_0=B_1/B_0=C_1/C_0,\qquad
r_2=A_2/A_0=B_2/B_0=C_2/C_0
\]

are common to the three legs. Put `g=A0 B0 C0`. The equations become

\[
g r_1r_2=-1,\qquad
g r_1^3=g r_2^3=1/2.
\]

Cubing the first equation and multiplying the latter two gives
`g=-4`. Consequently

\[
r_1=-\frac{w^t}{2},\qquad
r_2=-\frac{w^{-t}}{2},\qquad t\in\{0,1,2\}.
\]

The 000 equation is `6g+27 kappa=3`, which forces `kappa=1`.
The factor 27 is the Fourier coefficient of `(1,1,1)^tensor3`.

Let `L=(J-I)/2` and let P be the cyclic three-by-three permutation.
After independent leg scalings whose product is one, all possible
original fixed-sector maps are therefore

\[
P^tL,\qquad P^tL,\qquad -4P^tL.
\tag{1}
\]

Every phase is checked separately below. No assumption that a
diagonal-only cyclic permutation preserves the other sectors is used.

The phase-zero diagonal repair itself is exact:

\[
(L\otimes L\otimes(-4L))N
=D_3-(1,1,1)^{\otimes3}.
\]

It is the polarization identity

\[
6xyz=\frac{(x+y+z)^3-
(x+y+z-2x)^3-(x+y+z-2y)^3-(x+y+z-2z)^3}{4}.
\]

One scalar repairs this diagonal sector, but the next section proves
that the repair cannot extend to the full matrix tensor in this model.

## 6. A twelve-dimensional linear contradiction for every phase

Consider the nontrivial Klein-four character on the A coordinates
`A12,A21`, and the same target character on `E12,E21`. The first-leg
map on this two-dimensional character space must be invertible because
the target first flattening has full rank nine. Write its inverse as R.

The B source coordinates for this character are
`B0,0; B0,1; B1,2; B2,4`. Let the corresponding target map be an arbitrary
two-by-four matrix B. Allowing every such B only enlarges the model.
An appended trivial scalar contributes nothing to this character.

Contracting the original source against the phase-zero C diagonal map
in (1) gives the three two-by-four matrices

\[
S_0=\begin{pmatrix}2&2&0&0\\0&-2&0&0\end{pmatrix},\quad
S_1=\begin{pmatrix}2&2&0&-2\\0&0&-2&0\end{pmatrix},\quad
S_2=\begin{pmatrix}0&0&0&-2\\0&-2&-2&0\end{pmatrix}.
\]

The matching trace-tensor slices are

\[
T_0=0,\qquad T_1=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
T_2=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
\]

For phase t the necessary equations are

\[
S_{k-t\bmod3}B^T=R T_k,\qquad k=0,1,2.
\tag{2}
\]

These are twelve homogeneous linear equations in the eight entries of B
and four entries of R. In the row and column orders saved by the
certificate, their determinants are

| Phase t | Exact determinant |
| --- | ---: |
| 0 | 256 |
| 1 | -256 |
| 2 | -256 |

Thus (2) forces `B=R=0` in every phase, contradicting the invertibility
of R. This proves the following precisely scoped statement:

**There is no ordinary A4-equivariant restriction from P3 plus any
number of trivial A4 scalar summands to M3 with its three physical
spaces carrying the standard tetrahedral three-dimensional module.**

The proof does not exclude non-equivariant maps, scalar summands with
different group actions, other auxiliary tensors, other physical
representations, or singular degenerations.

The exact source matrices are regenerated from all Cartesian source
coefficients by `tetrahedral_scalar_obstruction.py`. It stores each full
twelve-by-twelve equation matrix. A second worker in the same generating
session separately checked the Fourier classification and all three
determinant values. That worker did not regenerate the source matrices.
This additional check is not independent mathematical review.

## 7. Completed finite searches and exact replay

`tetrahedral_search.py` builds the complete rational intertwiner spaces
by solving both generator equations. Their dimensions are `(7,11,11)`
without a scalar and `(8,12,12)` with one scalar. The 729 target
positions have 61 invariant coordinate orbits of size three; 546
positions are forced zero. Every reported residual is replayed on all
729 coefficients. An independent integer contraction checks that the
reduced objective represents the full coefficient equations.

| Model | Seeds | Iterations per seed | Best errors for the four seeds |
| --- | --- | ---: | --- |
| A4-equivariant P3 | 202610270–273 | 1200 | 0.614723, 0.577842, 0.658165, 0.650566 |
| A4-equivariant P3 plus one trivial scalar | 202610280–283 | 1200 | 0.494335, 0.581477, 0.692516, 0.494335 |
| Exact phase-zero diagonal repair fixed, 20 remaining parameters | 202610290–293 | 1600 | 0.700966, 0.700966, 0.641707, 0.634286 |

All three grids are complete. No construction was found. The exact
obstructions above supersede these numerical failures within their
stated models. Each grid used real coefficients and ridge `10^-12`.
The last grid kept all 27 diagonal-sector coefficients exactly correct.

The core exact obstruction and scalar-pilot tests use only the Python
standard library:

```sh
python research/ai/2026-10-20-paired-direct-sums/tetrahedral_kernel.py
python research/ai/2026-10-20-paired-direct-sums/scalar_symmetry_obstructions.py
python research/ai/2026-10-20-paired-direct-sums/tetrahedral_scalar_obstruction.py
python -m unittest discover -s tests -p test_paired_tetrahedral.py -v
```

The optional intertwiner discovery controls also use the maintained
SymPy dependency; numerical searches use NumPy. The saved checkpoints
are complete map matrices in their declared source coordinates.

Review status: exact author checks and the limited same-session check
described above. No external review, formal proof assistant check, or
smaller exponent is claimed.
