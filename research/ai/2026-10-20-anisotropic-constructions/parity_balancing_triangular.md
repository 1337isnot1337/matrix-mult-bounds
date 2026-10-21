# Exact triangular lifts for every full A(a,b)

October 21, 2026. All vector spaces and maps in this note are over the
rational numbers. Put

\[
n=a+b-1,\qquad r=(a-1)(b-1),\qquad a,b\ge2.
\]

We construct linear maps J and K with

\[
A(a,b)\longrightarrow
\bigl[(A,B,C)\mapsto\operatorname{tr}(ABC)
+\operatorname{tr}(K(A)K(B)K(C))\bigr],
\tag{1}
\]

where A,B,C are n-by-n matrices and K(A) is r-by-r. The two terms
in (1) use the same target variables. They are a sum of trilinear
forms, not a direct sum of tensors on disjoint spaces.

Consequently there is an exact ordinary restriction

\[
A(a,b)\oplus M_r\longrightarrow M_n.
\tag{2}
\]

The second source summand cancels the explicitly retained residual.
It cannot be discarded from this conclusion. At a=b=2, (2) is the
[scalar-corrected M3 construction](parity_balancing_spin1.md).
These constructions do not establish a smaller matrix multiplication
exponent.

## 1. The source and its physical matrices

Let W be the space of ab-by-ab matrices of the form

\[
W(F)_{(i,q),(p,s)}=F_{i,p+q,s},
\quad 0\le i,p<a,\quad 0\le q,s<b.
\]

Here F has a choices of i, n choices of its middle index, and b
choices of s. Thus W has dimension abn. As in the small construction,
expanding a trace of three such matrices gives exactly the full source
A(a,b). Its original coordinates are

\[
X=(i,p+q,s),\quad Y=(j,p,r+s),\quad Z=(i+j,q,r),
\]

where i,p,r have a choices and j,q,s have b choices. The common
functional orders on the three legs are (i,k,s), (p,k,j), and (r,k,q).

Write d=b-1. Define a surjective linear map
\(\pi:\mathbb Q^{ab}\to\mathbb Q^n\) by

\[
\pi(v)_t=
\sum_{i+d-q=t}(-1)^q\binom dq\,v_{i,q},
\qquad 0\le t<n.
\tag{3}
\]

Every output coordinate has a nonzero input coefficient, and each
input coordinate contributes to just one output coordinate. This
proves surjectivity directly. Its kernel therefore has dimension r.

## 2. An invertible map from the source matrix space

**Lemma.** The linear map

\[
L:W\longrightarrow\operatorname{Hom}(\mathbb Q^{ab},\mathbb Q^n),
\qquad W(F)\longmapsto\pi W(F)
\tag{4}
\]

is an isomorphism.

Both spaces have dimension abn. It remains to prove injectivity. For
fixed s, the entry of L(F) with row t and column (p,s) is

\[
\sum_{i+d-q=t}(-1)^q\binom dq F_{i,p+q,s}.
\]

Put k=p+q and c=i-k=t-d-p. The equations split into square blocks
indexed by c. Their input and output indices are

\[
\begin{aligned}
\max(0,-c)&\le k\le\min(n-1,a-1-c),\\
\max(0,-c-d)&\le p\le\min(a-1,a-1-c).
\end{aligned}
\]

In each block the matrix entry is

\[
(-1)^{k-p}\binom d{k-p},
\tag{5}
\]

where the binomial coefficient is zero outside 0 through d. Row and
column sign changes remove the sign in (5).

For c>0 the block is upper triangular with diagonal one. For c<-d
it is lower triangular with diagonal one after the sign changes. In
the central range -d<=c<=0, write h=-c. The block has rows
p=0,...,a-1 and columns k=h,...,h+a-1, with 0<=h<=d.

To show that this central determinant is positive, let B be the finite
upper bidiagonal matrix with ones on its diagonal and first upper
diagonal, on indices 0 through a+d-1. Then

\[
(B^d)_{p,k}=\binom d{k-p}.
\]

Every minor of B is zero or one. Indeed, any nonzero determinant
matching must preserve the order of the row and column indices:
an inversion would require a later row to reach an earlier column
while an earlier row reaches a later column using only steps zero
and one, which is impossible.

Apply Cauchy--Binet repeatedly to the minor of B^d with initial index
set \(\{0,\ldots,a-1\}\) and final set
\(\{h,\ldots,h+a-1\}\). Every summand is nonnegative. There is a
summand equal to one: shift the whole index set by one at h stages
and keep it fixed at the other d-h stages. Every intermediate index
lies in the finite range, and every associated minor of B is one.
Thus the determinant is positive. Every block is invertible, proving
the lemma.

This proof also gives an exact construction algorithm: invert the
small binomial blocks (5), separately for each s. No genericity
assumption or numerical matrix inversion is used.

## 3. Constructing the quotient action and retaining its kernel

For each n-by-n matrix A, define J(A) to be the unique matrix in W
such that

\[
\pi J(A)=A\pi.
\tag{6}
\]

It exists by the lemma, and depends rationally and linearly on A.
Equation (6) implies that J(A) preserves R=ker pi and acts as A on
the quotient. Choose any rational complement to R on which pi is an
isomorphism. In a basis formed from that complement followed by a
basis of R, one has

\[
J(A)=\begin{pmatrix}A&0\\ *&K(A)\end{pmatrix}.
\tag{7}
\]

The map K is linear and its matrices have size r. Multiplying three
matrices in (7) and taking their trace proves (1). Applying the
restriction maps \(-K\) on all three legs of an added M_r source
contributes minus the residual, proving (2).

An explicit rational basis of R is available. For 0<=u<a-1 and
0<=v<b-1, put

\[
Qe_{u,v}=
\frac{d-v}{d}\,e_{u,v}
+\frac{v+1}{d}\,e_{u+1,v+1}.
\tag{8}
\]

The two contributions cancel under (3), by the adjacent-binomial
identity. These vectors are independent: ordering by their leading
row coordinate makes the nonzero leading coefficients triangular.
There are r vectors, so their image is precisely R. The executable
constructs K from

\[
J(A)Q=QK(A)
\tag{9}
\]

and checks this exact identity on every target matrix unit.

## 4. Exact finite examples and limits of a recursion

The saved construction contains every rational map and residual
matrix for the following cases:

| Source | Quotient M_n | Residual matrix size r | Residual block at A=I |
| --- | ---: | ---: | --- |
| A(2,2) | M3 | 1 | 3 |
| A(2,3) | M4 | 2 | 4 with multiplicity 2 |
| A(3,3) | M5 | 4 | 5 with multiplicity 3; 10 with multiplicity 1 |
| A(4,4) | M7 | 9 | 7 with multiplicity 5; 21 with multiplicity 3; 35 with multiplicity 1 |

These eigenvalues are exact finite calculations. The construction and
proof do not require an all-size formula for them. At a=2 the lower
physical space is the full matrix space of size b-1, so the residual
is also a restriction of A(1,b-1), which is M_(b-1).

For A(3,3) and A(4,4), the residual matrices in the basis (8) do not
belong to the ordinary lower Hankel spaces W_(a-1,a-1). More
strongly, the natural next kernel flag is not preserved. In the
A(3,3) example, take A=E00 in the five-dimensional quotient basis.
Its residual is

\[
K(E_{00})=\begin{pmatrix}
0&0&0&1\\
0&2&0&0\\
0&0&0&0\\
0&0&0&3
\end{pmatrix}.
\]

It sends the next scalar kernel vector (1,0,0,1) to (1,0,0,3).
The lower top projection gives (0,-2,0), so this vector leaves that
kernel. This exact example rules out discarding off-diagonal blocks
in a proposed recursion along this particular natural flag. It does
not exclude a different residual construction or basis.

The reported residual correction is consequently retained in full.
No direct sum of the smaller odd-size matrix tensors, no ordinary
lower A source, and no vanishing residual is inferred from the
eigenvalue patterns.

## 5. Reproduction and review status

The exact generator uses SymPy:

```sh
python research/ai/2026-10-20-anisotropic-constructions/parity_balancing_triangular.py --pair 2 2 --pair 2 3 --pair 3 3 --pair 4 4 --output results/anisotropic-constructions-2026-10-20/parity_balancing_triangular.json
```

A separate replay requires only the Python standard library:

```sh
python research/ai/2026-10-20-anisotropic-constructions/parity_balancing_triangular_verify.py results/anisotropic-constructions-2026-10-20/parity_balancing_triangular.json
```

It reconstructs pi, Q, and every physical source matrix from the saved
map, and checks (6) and (9) with `Fraction` arithmetic on every target
matrix unit. The CI tests also reject a changed residual entry and a
report that attempts to discard the residual correction.

For each recorded source it exports the complete common source map,
every residual matrix, every binomial-block determinant, and the
first failure of the natural next flag when one occurs. Each target
matrix unit passes (6) and (9) exactly. The note's proof establishes
the construction for every pair a,b>=2; the finite controls check
the implementation and explicit examples.

Review status: the proof was checked by a second agent in this
generating session. The author also completed the exact finite
replay. No external independent review or formalization is claimed.
