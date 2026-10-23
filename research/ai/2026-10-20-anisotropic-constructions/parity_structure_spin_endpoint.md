# An exact endpoint repair of the spin module

Research construction, October 21, 2026. Changing the existing $Y$ map
of the rational spin module gives an exact ordinary restriction

\[
A(8,8)\longrightarrow M(3,3,27)
\tag{1}
\]

whose full first-leg response has rank **191**. The complete response
at $F(7,0,7)$ vanishes. This removes the single excess response
direction in the saved 192-response construction and reaches the
necessary dimension allowance for embedding this core in
$M_{27}\oplus M_7$. The full square/direct-sum target remains
unconstructed, and no smaller exponent is established.

## 1. Fixed input and coordinate conventions

Use common source coordinates $F(i,k,s)$, numbered $(15i+k)8+s$, on
all three legs. The source coefficients are one at

\[
X(i,p+q,s)Y(p,r+s,j)Z(r,i+j,q),
\qquad i,p,r,j,q,s\in\{0,\ldots,7\}.
\tag{2}
\]

Start from the actual $A(8,8)\to M(3,3,28)$ maps in
`spin-module14-full-maps.json`. Delete middle channel 27 on both the
$Y$ and $Z$ legs. The resulting target coordinate orders are

\[
X_{I,J}:3I+J,\qquad Y_{J,\alpha}:27J+\alpha,
\qquad Z_{\alpha,I}:27I+\alpha.
\]

Retain these nine first-map images and all 81 $Z$ images exactly.
Only the existing 81 $Y$ images are changed. In particular the new
construction does not add a channel while keeping the former maps
fixed. The old saved-map response obstruction keeps its original
scope.

The new map denominators are $2,181776,20$. The actual sparse maps
have respectively 16, 4,853, and 1,608 nonzero entries. All are stored
in `parity_structure_spin_endpoint_maps.json`.

## 2. The exact linear correction

Let $D_X$ be the $729\times960$ matrix obtained by contracting the
original source with the fixed first map and fixed $Z$ map. Its row
index is a pair consisting of a first target unit and a $Z$ target
unit. For each target $Y$ unit, its row of source coefficients must
solve the corresponding column of the matrix multiplication identity.

Let $D_f$ be the $81\times960$ matrix obtained by fixing the first
source coordinate to

\[
f=F(7,0,7)
\tag{3}
\]

and contracting with the fixed $Z$ map. If $Y^0$ denotes the old
$81\times960$ coefficient matrix, the correction is a matrix
$\Delta Y$ satisfying

\[
D_X(\Delta Y)^T=0,
\qquad
D_f(\Delta Y)^T=-D_f(Y^0)^T.
\tag{4}
\]

These equations preserve **all** required module coefficients,
including the zeros, and annihilate **all** coefficients of the
response at (3).

The old $Y$ support is contained in the 160 coordinates

\[
F(p,e+2L,j),\qquad
p,e\in\{0,1\},\quad0\le L<5,\quad0\le j<8.
\tag{5}
\]

On these coordinates, the kernel calculation for $D_X$ splits by
the source parity $e$. The two exact constraint ranks are 78 and 75,
leaving seven kernel directions after channel 27 is deleted. No new
source-coordinate columns are required.

The seven-dimensional correction space has a six-dimensional image
under $D_f$. The right side of (4) lies in that image. The
optional generator solves (4) over $\mathbb Q$, checks both equalities
exactly, and exports the new actual $Y$ map. The new common denominator
is 181776 after rational coefficients are reduced.

The proof of the final restriction does not depend on stored rank
metadata or on the discovery computation: the standard-library
verifier independently contracts the exported maps against (2).

## 3. Complete identity and full response rank

Let $\Psi$ contract the entire first source space against the new
$Y$ map and fixed $Z$ map. Every nonzero $Y$ coordinate still has
first short index $p\in\{0,1\}$; every nonzero $Z$ coordinate has
last short index $q\in\{0,1\}$. Thus the first long coordinate is
$k=p+q\in\{0,1,2\}$. The response is supported on at most
$3\cdot8\cdot8=192$ source coordinates.

Equation (4) makes the complete response at (3) zero. Consequently

\[
\operatorname{rank}\Psi\le191.
\tag{7}
\]

The replay rebuilds every response coefficient from the actual
integer map numerators. Exactly 191 source-coordinate rows are
nonzero. A stored list of 191 output columns specifies a square
minor on those rows. Its regenerated determinant is

\[
33245\pmod{65521},
\]

which is nonzero. Therefore

\[
\operatorname{rank}_{\mathbb Q}\Psi=191,
\qquad\dim\ker\Psi=769.
\tag{8}
\]

The same original-source contraction checks all 59,049 target
coefficients. Exactly 243 coefficients equal one, namely

\[
X_{I,J}Y_{J,\alpha}Z_{\alpha,I},
\qquad0\le I,J<3,\quad0\le\alpha<27,
\]

and every other coefficient is zero. This proves (1).

## 4. The exact first-space allowance for assembly

The 191 nonzero response rows are independent. Its kernel is therefore
the following explicit coordinate space:

\[
K=\operatorname{span}\{F(i,k,s):3\le k\le14\}
\ \oplus\ \mathbb Q F(7,0,7).
\tag{9}
\]

The first summand has dimension 768. Let $E_0$ be the span of the
nine actual first-map images. Their response images are independent
because (1) is the concise $M(3,3,27)$ tensor. Hence the inverse image
of the nine-dimensional first target response space is exactly

\[
K\oplus E_0,
\qquad\dim(K\oplus E_0)=769+9=778.
\tag{10}
\]

For an ordinary extension that retains these two non-first maps, all
first-leg units outside the nine units of this core must lie in $K$.
The proposed target has common leg dimension $27^2+7^2=778$.
Thus its allowance $778-9=769$ now equals the available kernel
dimension. Moreover, any such full extension must use precisely the
first-image space (10). This is a concrete assembly constraint, not
a construction of its other maps.

## 5. Replay and controls

```bash
python -S research/ai/2026-10-20-anisotropic-constructions/parity_structure_spin_endpoint.py
python -S -m unittest discover -s tests -p test_parity_structure_spin_endpoint.py
```

The complete verifier uses only the standard library. Its inputs are
the actual map export and the minor's coordinate lists. NumPy and
SymPy are confined to the optional rational generator.

One tamper control doubles the correction on one target $Y$ row, so
that its row becomes $2Y-Y^0$. Both $Y$ and $Y^0$ satisfy the old module
identity, and hence this modified row does as well; it breaks the new
endpoint cancellation. The verifier rejects it for that reason. A
separate nonzero first-map coefficient tamper checks the full
multiplication identity.
