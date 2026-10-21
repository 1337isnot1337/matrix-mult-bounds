# Exact boundary-chain restrictions of the paired source

**Result.** For every integer \(a\ge2\), there is an explicit restriction

\[
P_a\longrightarrow M(a,2,a)
\]

with coefficients in \(\{0,1,-1\}\). This is a proved tensor identity over
the integers, valid over every field. It provides a positive construction
and calibration for the concurrent search. **It does not improve the
matrix multiplication exponent.** The larger paired direct-sum target
remains unconstructed.

## 1. Source, target, and maps

The source is

\[
P_a=\sum_{p,q,y,v=0}^{a-1}
 A_{p,q}B_{y,q+v}C_{p+y,v},
\]

of format \((a^2,a(2a-1),a(2a-1))\). The matrix multiplication convention is

\[
M(a,2,a)=\sum_{i,k=0}^{a-1}\sum_{j=0}^1
 a_{i,k}b_{i,j}c_{j,k},
\]

of format \((a^2,2a,2a)\). Thus its ordinary bilinear evaluation multiplies
an \(a\)-by-2 matrix by a 2-by-\(a\) matrix, in that order.

Send \(A_{p,q}\mapsto a_{q,p}\). On the second source space, use

\[
B_{0,j}\mapsto
\begin{cases}
b_{j+1,1},&0\le j<a-1,\\
b_{j-a+1,0},&a-1\le j\le2a-2,
\end{cases}
\]

\[
B_{1,j}\mapsto
\begin{cases}
b_{j,1},&0\le j<a,\\
b_{j-a,0},&a\le j\le2a-2,
\end{cases}
\qquad B_{y,j}\mapsto0\quad(y\ge2).
\]

On the third source space, write \(\gamma_{z,v}\) for the image of
\(C_{z,v}\), and set

\[
\gamma_{z,v}=
\begin{cases}
(-1)^{a-1-v}c_{0,z-v+a-1},&0\le z\le v,\\
(-1)^v c_{1,z-v-1},&v<z\le a,\\
0,&z>a.
\end{cases}                                                     \tag{1}
\]

Every displayed target index lies in its indicated range. These are
constant linear maps; no limiting parameter or numerical approximation
is needed.

## 2. Telescoping proof

The third-space maps satisfy the exact adjacent relations

\[
\gamma_{p,v}+\gamma_{p+1,v+1}=0
\quad(0\le p<a,\ 0\le v<a-1),                         \tag{2}
\]

and the two boundary conditions

\[
\gamma_{p,a-1}=c_{0,p},\qquad
\gamma_{p+1,0}=c_{1,p}.                                 \tag{3}
\]

To check the coefficient of \(A_{p,q}\), first follow a target variable
\(b_{i,0}\). Its possible source occurrences are \(B_{0,a-1+i}\)
and \(B_{1,a+i}\); the latter is absent when \(i=a-1\). In the slice
indexed by \(q\):

- If \(i>q\), neither occurrence has an allowed index \(v\).
- If \(i=q\), only \(B_{0,a-1+i}\) occurs, yielding
  \(\gamma_{p,a-1}=c_{0,p}\).
- If \(i<q\), both occur and yield
  \(\gamma_{p,a-1+i-q}+\gamma_{p+1,a+i-q}=0\), by (2).

Next follow \(b_{i,1}\). Its possible occurrences are \(B_{0,i-1}\)
and \(B_{1,i}\); the former is absent when \(i=0\).

- If \(i<q\), neither occurrence has an allowed index \(v\).
- If \(i=q\), only \(B_{1,i}\) occurs, yielding
  \(\gamma_{p+1,0}=c_{1,p}\).
- If \(i>q\), the two occurrences yield
  \(\gamma_{p,i-1-q}+\gamma_{p+1,i-q}=0\).

Consequently the source slice becomes

\[
\sum_{y,v}B_{y,q+v}C_{p+y,v}
\longmapsto b_{q,0}c_{0,p}+b_{q,1}c_{1,p}.
\]

Combining this with \(A_{p,q}\mapsto a_{q,p}\) proves the claimed
matrix multiplication identity. The proof is an identity in a polynomial
ring over \(\mathbb Z\), so it also applies in characteristic two.

## 3. The explicit \(a=2\) witness

The first discovered instance has the particularly short form

\[
B\mapsto
\begin{pmatrix}b_{11}&b_{00}&b_{10}\\
                b_{01}&b_{11}&b_{00}\end{pmatrix},\qquad
C\mapsto
\begin{pmatrix}-c_{01}&c_{00}\\
                 c_{10}&c_{01}\\
                 c_{11}&-c_{10}\end{pmatrix}.
\]

The complete expansion has 16 source contributions, 12 distinct target
monomials touched, eight matrix multiplication terms with coefficient
one, and four off-support monomials canceled by opposite signs.
[`exact-p2.json`](exact-p2.json) records every contribution, including the
four cancellations. [`exact_p2.py`](exact_p2.py) reconstructs that record.

The witness was discovered by unrestricted numerical fitting, followed
by an exact quotient derivation. Numerical fitting is not part of its
acceptance: the maps above and the full integer coefficient check are.

## 4. Exact continuation and its limit

Represent third-space coordinates as monomials \(u^z v^j\). Relations
(2) correspond to quotienting by the subspace

\[
K_a=(1+uv)\operatorname{span}
 \{u^y v^j:0\le y<a,\ 0\le j<a-1\}.
\]

This is a subspace quotient, not a claim that this truncated space is an
algebra quotient. Its dimension is \(a(a-1)\), leaving a quotient of
dimension \(a^2\). The two boundary chains used in (3) are independent.

We also tested whether this same quotient, with the specified transpose
map on the first space, could realize \(M(a,a,a)\). For one candidate
middle mode, write \(b_q\) for its second-space vector in target row
\(q\). All wrong first-space slices must vanish, and all correct slices
must have the same output for each \(p\). These are linear equations in
the \(a^2(2a-1)\) entries of the vectors \(b_q\).

[`quotient_search.py`](quotient_search.py) solves those equations using
exact rational row reduction. [`quotient-continuation.json`](quotient-continuation.json)
contains the reproducible results:

| \(a\) | Unknowns | Exact rank | Middle-mode dimension | Combined output span |
|---:|---:|---:|---:|---:|
| 2 | 12 | 9 | 3 | 4 |
| 3 | 45 | 43 | 2 | 6 |
| 4 | 112 | 110 | 2 | 8 |
| 5 | 225 | 223 | 2 | 10 |

For \(a=3,4,5\), this particular quotient and first-space map cannot
realize \(M(a,a,a)\): they have fewer than \(a\) independent middle
modes and less than \(a^2\) output span. This is an ansatz-specific
failure. It places no restriction on other quotients or singular families.

## 5. Exponent gate and unresolved target

The [paired direct-sum character calculation](../2026-10-20-paired-direct-sums/README.md)
gives the finite gate

\[
\sum_j(36l_jb_jr_j)^t\le(6a-2)^2,\qquad t=\omega/3.
\]

For this one-block family it becomes

\[
(72a^2)^t\le(6a-2)^2.
\]

It does not force \(t<3/4\). In fact \(6a-2\ge5a\) for \(a\ge2\),
so

\[
(6a-2)^8\ge5^8a^8\ge4\cdot5^8a^6>72^3a^6=(72a^2)^3.
\]

Thus this inequality has strict slack at \(t=3/4\) for every member of
the family. Even its \(a=2\) consequence alone is only
\(\omega\le3\log(100)/\log(288)\approx2.439627\).

The separate target
\(P_{10}\to M(4,11,10)\oplus M(10,12,6)\) would cross a smaller gate,
but its degeneration remains unconstructed. The exact grading allocation
in [`grading.json`](grading.json) only sets up that search. Three completed
constant-map fits at 200 iterations have relative residuals approximately
0.85405, 0.86533, and 0.85595. Their files are exploratory numerical
records, and neither the residuals nor grading capacities prove a
degeneration or rule one out.

## 6. Reproduction and independent checks

The exact tools need only Python's standard library:

```bash
python research/ai/2026-10-20-paired-construction/exact_p2.py
python research/ai/2026-10-20-paired-construction/chain_family.py
python research/ai/2026-10-20-paired-construction/quotient_search.py --sizes 2 3 4 5
python -m unittest discover -s tests -p test_paired_construction.py -v
```

[`chain_family.py`](chain_family.py) supplies the maps, integer coefficient
checker, and ordinary multiplication evaluator. For every \(a=2,\ldots,8\),
[`chain-family.json`](chain-family.json) records checks of all \(a^4\)
source terms and all \(4a^4\) target coefficient positions. Precisely
\(2a^3\) source contributions survive the zero maps; these give
\(2a^2\) desired terms and \(a^2(a-1)\) off-support cancellation pairs.
The test suite also evaluates every ordinary bilinear basis input pair,
so output order and transposition are checked independently of the saved
coefficient certificates.
