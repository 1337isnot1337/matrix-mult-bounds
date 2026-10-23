# Quadratic invariants of the complete discarded error

**Claim:** `AI-EXTERNAL-QUADRATIC-ERROR-010`

**Status:** written-unreviewed

**Field:** any characteristic-zero extension of the rational numbers

This package gives an exact, reusable obstruction to a proposed physical
stabilizer degeneration. It checks the **complete error tensor**, including
all original discarded terms. A trace-zero term with a nilpotent cyclic
matrix product can still fail this test.

There are two applications:

1. In the accepted ten-split seed, no single term can be deleted from any
   exact minimum five-term refactorization of the block
   `{36,56,61,62,75}` by a subsequent common physical degeneration. The
   refactorization and physical matrices may depend on a Laurent parameter
   and may have poles. The original ten discarded terms remain in the error.
2. Two specified polynomial refactorization families, obtained after the
   additional V replacements `69 -> 63` and `69 -> 64` on the six-split seed,
   also fail this deletion test for every Laurent-dependent value of their
   free parameter.

The exact obstruction is quadratic. All three explicit families below have
full error invariant `2`, although the selected term has trace zero and its
cyclic matrix product has square zero. Their proposed 75-term survivors
therefore do not yield a physical degeneration to `M(4,5,5)`.

This does not exclude arbitrary 75-term algorithms, simultaneous deletion
of several terms, nonminimal block refactorizations, or refactorizations
mixing this block with other terms. It gives no matrix multiplication rank
record, general border-rank lower bound, source map, or exponent improvement.

## A tensor reshaping makes the physical action a conjugation

Let

\[
\mathcal T=\operatorname{Mat}_{r,s}(K)\otimes
\operatorname{Mat}_{s,t}(K)\otimes\operatorname{Mat}_{t,r}(K),
\qquad N=rst.
\]

Define a linear reshaping `rho: T -> Mat_N(K)` by

\[
\rho(F)_{(i,\ell,k),(n,j,m)}
   =F_{(i,j),(\ell,m),(k,n)}.
\]

Every index ranges over its corresponding physical space. Thus rows and
columns both have size `r*s*t`, and the reshaping is a coordinate bijection.
For the literal matrix multiplication tensor

\[
M=\sum_{i,j,k} E_{ij}\otimes E_{jk}\otimes E_{ki},
\]

the reshaping is `rho(M)=I_N`.

The physical action on a rank-one tensor is

\[
\Phi_{R,P,T}(U,V,W)
 =(R^{-1}UP,\ P^{-1}VT,\ T^{-1}WR).
\]

Left matrix indices contribute `R^-1,P^-1,T^-1`; the reordered right
indices contribute `R,P,T`. Therefore

\[
\rho(\Phi_{R,P,T}F)
 =(R^{-1}\otimes P^{-1}\otimes T^{-1})
   \rho(F)(R\otimes P\otimes T).
\]

This is an identity over any extension field where the physical matrices
are invertible. In particular it allows arbitrary matrices over a Laurent
field. It also explains directly why the action fixes `M`.

Consequently all power traces `tr(rho(F)^a)` are physical invariants.
The first two are

\[
L(F)=\operatorname{tr}\rho(F),\qquad
q(F)=\operatorname{tr}(\rho(F)^2).
\]

Write their symmetric bilinear polarization as

\[
C(F,G)=\operatorname{tr}(\rho(F)\rho(G)),\qquad q(F)=C(F,F).
\]

For rank-one tensors this is the explicit contraction

\[
C(U\otimes V\otimes W,\ U'\otimes V'\otimes W')
 =\operatorname{tr}(U V' W U' V W').
\]

Each factor of each tensor appears once, so this formula extends bilinearly
to arbitrary tensors. It depends on the tensors themselves, not on their
decompositions. A factor gauge uses three nonzero scalars with product one;
it leaves the whole tensor term, and hence these invariants, unchanged.

### Coordinate involution and target calibration

In row-major flat coordinates put

\[
a=is+j,\qquad b=\ell t+m,\qquad c=kr+n.
\]

The involution

\[
\pi(a,b,c)=(ns+\ell,\ jt+k,\ mr+i)
\]

gives

\[
C(F,G)=\sum_{a,b,c}F_{a,b,c}G_{\pi(a,b,c)}.
\]

The verifier implements this formula independently of the matrix-product
formula. It also implements the sparse reshaping and arbitrary positive
integer power traces. These three descriptions agree in the exact controls.

Since `rho(M)=I_N`,

\[
C(M,F)=L(F),\qquad C(M,M)=N.
\]

For `M(4,5,5)`, `N=100`. A complete error `E=M-S` therefore satisfies

\[
q(S)=100-2L(E)+q(E).
\]

When `L(E)=0` and `q(E)=2`, the candidate survivor has invariant `102`.
Both forms of this calculation are checked for the explicit families.

## Necessary conditions for contraction

Let `epsilon` be a formal parameter. Convergence to zero means that every
coordinate has positive valuation in `K((epsilon))`. If a common physical
action sends an error `E(epsilon)` to zero, every positive-degree invariant
polynomial of that error must also tend to zero. In particular,

\[
L(E(\epsilon))\longrightarrow0,\qquad
q(E(\epsilon))\longrightarrow0.
\]

This applies to the sum of all discarded terms. It permits cancellation
between those terms. It does not impose separate convergence on each term.

For a **fixed constant** error `E`, contraction forces
`tr(rho(E)^a)=0` for `1 <= a <= N`. Newton identities in characteristic zero
then give characteristic polynomial `x^N`, so `rho(E)` is nilpotent.
Equivalently, all coefficients of that characteristic polynomial are
conjugation invariants and must equal their values at zero. Nilpotence is
only a necessary condition: the available conjugations have the special
form `R tensor P tensor T`.

For a parameter-dependent error, the condition is that its power traces
tend to zero. It is not a claim that every nonzero-parameter reshaping must
already be nilpotent. The test suite includes a Laurent-dependent example
whose linear invariant tends to zero while its quadratic invariant tends
to two.

## Every minimal refactorization of the named ten-split block

The [ten-split certificate](../2026-10-23-large-gauged-batches/README.md)
gives an exact constant identity `M=S+D`, where `D` includes all ten original
discarded terms. Let

\[
B=(36,56,61,62,75),\qquad Z_i=U_i\otimes W_i.
\]

The exact certificate in this directory checks

\[
\operatorname{rank}[Z_i]_{i\in B}
 =\operatorname{rank}[V_i]_{i\in B}=5.
\]

Thus the block tensor has V-flattening rank five. Any exact five-term
refactorization has independent new columns on both sides of this
flattening. Their spans are its intrinsic column and row images. Writing
the original column matrices as `Z,V`, there is an invertible `G` such that

\[
Z'=ZG,\qquad V'=VG^{-\mathsf T}.
\]

This also holds over `K((epsilon))`, with no bound on poles in `G`.
For one selected term `A=U' tensor V' tensor W'`, let `x` and `y` be the
corresponding columns of `G` and `G^-T`. Then

\[
x^{\mathsf T}y=1.
\]

Define matrices indexed in the displayed order of `B` by

\[
H_{ij}=L(U_i\otimes V_j\otimes W_i),\qquad
J_{ij}=C(D,U_i\otimes V_j\otimes W_i).
\]

Using the **full** original `D`, exact coordinate contraction and an
independent matrix-trace contraction give

\[
H=I_5+3E_{61,62},\qquad J=-3E_{61,62}=I_5-H,
\qquad L(D)=q(D)=0.
\]

Here `E_61,62` denotes the matrix unit labeled by those source term indices,
the third row and fourth column in the displayed block order. If
`tau=L(A)`, then

\[
\tau=x^{\mathsf T}Hy,\qquad C(D,A)=x^{\mathsf T}Jy=1-\tau.
\]

Every original U factor in this block has the common left column

\[
p=(1,-1,0,0)^{\mathsf T}.
\]

The certificate exports all five right rows and checks `U_i=p a_i^T`.
Consequently every matrix in their U span has rank at most one.
The new nonzero decomposable column `U' tensor W'` lies in the original
Z span, hence in `span{U_i} tensor span{W_i}`. Apply a linear functional
that is nonzero on `W'` to conclude `U' in span{U_i}`.
Thus `U'V'W'` has rank at most one. For such a square matrix,
`tr(A^2)=tr(A)^2`, so

\[
q(A)=\tau^2,
\qquad\boxed{q(D+A)=2-2\tau+\tau^2}.
\]

If a subsequent physical action contracted `D+A`, its linear invariant
`L(D+A)=tau` would tend to zero. The displayed quadratic identity would
then tend to two. This contradicts contraction. It also covers a
Laurent-dependent refactorization whose selected term has trace tending
to zero without being identically zero.

This proves the one-term deletion obstruction for every exact minimum
five-term refactorization of this named block. It does not classify
nonminimal decompositions or refactorizations involving other blocks.

## Three explicit polynomial families

All following indices are zero-based. A factor marked by a term index is
the surviving constant factor in its stated starting seed.

### Ten-split shared-W pair

For terms 61 and 62 of the ten-split seed, `W_62=-W_61`. Define

\[
\begin{aligned}
A(z)&=(U_{61}-zU_{62})\otimes
       ((1+z/3)V_{61}-V_{62}/3)\otimes W_{61},\\
K(z)&=(U_{61}/3-(1+z/3)U_{62})\otimes
       (V_{62}-zV_{61})\otimes W_{61}.
\end{aligned}
\]

Their sum is exactly the original two terms. Replacing that pair by
`A(z),K(z)` preserves the 76-term tensor. Deleting `A(z)` leaves 75 terms
and full error `E(z)=D+A(z)`. This explicit family illustrates the stronger
block theorem above.

### Six-split seed followed by V69 replacement

Start from the [six-split constant seed](../2026-10-23-gauged-splits/README.md).
For `j=63` or `j=64`, split term 69 on its V factor:

\[
U_{69}\otimes V_{69}\otimes W_{69}
 =U_{69}\otimes V_j\otimes W_{69}
  +U_{69}\otimes(V_{69}-V_j)\otimes W_{69}.
\]

Include this new difference in `D`, together with all six earlier errors.
Its factor minima in the pinned physical family are `(8,-5,-2)`, with
positive total one. The verifier regenerates all seven differences and
checks their positive total valuations. The resulting 76-term seed is
therefore another border family with limit `M`.

The new pair 69 and `j` shares `V_j`. Define

\[
\begin{aligned}
A_j(z)&=(U_{69}+zU_j)\otimes V_j\otimes((1-z)W_{69}+W_j),\\
K_j(z)&=(U_{69}+(z-1)U_j)\otimes V_j\otimes(zW_{69}-W_j).
\end{aligned}
\]

Again, `A_j(z)+K_j(z)` equals the original pair exactly. Keeping `K_j(z)`
and the other 74 terms gives a 75-term candidate with full error
`E_j(z)=D+A_j(z)`.

### Identities checked for every parameter

For each of the three registered families, exact polynomial contraction
checks

\[
L(A(z))=0,\qquad (U(z)V(z)W(z))^2=0,
\]

and

\[
q(D)=q(A(z))=0,\qquad C(D,A(z))=1,
\qquad q(E(z))=2.
\]

The full surviving-plus-error tensor is `M` in every parameter degree.
The proposed survivor has invariant `102`, while the target has `100`.

| Family | Original errors in D | Full error terms | Survivor terms | Nonzero error coefficients across all z degrees |
| --- | ---: | ---: | ---: | ---: |
| Ten, pair 61/62 | 10 | 11 | 75 | 303 |
| Six plus V69 to 63 | 7 | 8 | 75 | 153 |
| Six plus V69 to 64 | 7 | 8 | 75 | 351 |

These are identities over `Q[z]`, not checks at finitely many values.
Substituting any `z(epsilon)` in a characteristic-zero Laurent field
preserves the identity `q(E)=2`, including substitutions with poles.
An arbitrary common invertible physical action also preserves it. Thus
the full error cannot tend to zero. Possible cancellations among its
original and newly deleted terms are already included.

## Reproduction and acceptance boundaries

From the repository root:

```sh
python research/ai/2026-10-23-quadratic-error/verify.py
python -m unittest tests.test_quadratic_error -v
```

Acceptance uses only the Python standard library. It byte-checks the
external factors and both predecessor certificates. It reconstructs the
constant splits, all saved factor polynomials, and the complete original
discarded remainders. No scratch search output is an acceptance dependency.

For the full identities it checks 10,000 source coordinates and all 10,000
coordinates in each of degrees zero, one, and two for each family:
90,000 family coefficient positions. Every quadratic coefficient is then
contracted exactly in two ways. The block check independently certifies
both flattening ranks, the common U column, and all entries of `H` and `J`.

Eight focused tests cover the complete replay, all 10,000 involution
coordinates, target reshaping, a rational physical conjugation, product-one
gauges, exact coefficient and shape controls, and corrupted source/scope,
factor, and block certificates. A Laurent-pole refactorization has linear
error invariant `3*epsilon` but quadratic `2-6*epsilon+9*epsilon^2`.
A separate three-cycle control has zero linear and quadratic invariants
and nonzero cubic, illustrating the necessary-only nature of these tests.

The reusable `invariant.py` exposes `tensor_from_factors`, `pairing`,
`quadratic`, `reshape`, `trace_power`, and exact polynomial contraction.
Its scalar inputs are integers or `Fraction` objects. Saved coefficients
use canonical rational strings; no expression evaluation is performed.

The initial algorithm retains the external AlphaTensor attribution and
license notice in the [original source package](../2026-10-21-external-grid-seed/README.md).
The split seeds retain their prior local attribution. The reshaping proof,
block calculation, family certificates, and exact replay here are local
AI-derived continuation; no historical priority or independent mathematical
review is asserted. Detailed source pins are in `sources.json`.
