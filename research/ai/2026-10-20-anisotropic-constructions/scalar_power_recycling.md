# Exact reuse of the scalar correction in tensor powers

October 21, 2026. This note gives a constructive telescoping identity,
a complete rational two-copy witness, and the cost of the retained
correction. No smaller matrix multiplication exponent is established.

Let `T=A(2,2)` and write `M=M3`. The previously checked
[spin1 maps](parity_balancing_spin1.md) give an ordinary restriction

\[
 T\longrightarrow S:=M+\rho,\qquad
 \rho(A,B,C)=\operatorname{tr}(A)\operatorname{tr}(B)\operatorname{tr}(C).
 \tag{1}
\]

The two tensors on the right use the same nine variables on each leg.
Their addition is not a direct sum. The explicit source extension
`T direct_sum one scalar` cancels the second term.

## 1. An exact telescoping construction

For every positive integer `k`, there is a rational ordinary restriction

\[
 T^{\otimes k}\ \oplus\!
 \bigoplus_{j=0}^{k-1}
 \left(T^{\otimes j}\otimes M_{3^{k-1-j}}\right)
 \longrightarrow M_{3^k}.
 \tag{2}
\]

Here a zero tensor power is the scalar tensor. All the auxiliary
summands in (2) are included in the source.

To prove (2), use the identity

\[
 S^{\otimes k}-M^{\otimes k}
 =\sum_{j=0}^{k-1}
 S^{\otimes j}\otimes\rho\otimes M^{\otimes(k-1-j)}.
 \tag{3}
\]

Consecutive terms telescope after substituting `rho=S-M`. Each term
on the right is a restriction of the corresponding auxiliary source
in (2): apply (1) to its first `j` factors, insert the trace functional
in the omitted factor, and use the remaining matrix tensor directly.
Negate one leg of each auxiliary map. Adding their images to the
image of the main source cancels every term of (3). Grouping matrix
vertices identifies `M3` to tensor power `k` with `M_(3^k)`.

Thus correction tensors can be reused without expanding all the
binomial summands of `(T direct_sum one scalar)` to tensor power `k`.
The common source-leg dimension in (2) is exactly

\[
 12^k+\sum_{j=0}^{k-1}12^j9^{k-1-j}
 =\frac{4\cdot12^k-9^k}{3}.
 \tag{4}
\]

| Power | Matrix target | Source dimension in (2) | Naive scalar-extended power |
| ---: | ---: | ---: | ---: |
| 1 | M3 | 13 | 13 |
| 2 | M9 | 165 | 169 |
| 3 | M27 | 2,061 | 2,197 |
| 4 | M81 | 25,461 | 28,561 |

These are exact source-dimension savings. They do not remove the
auxiliary tensors or embed the resulting source into a smaller
univariate convolution source.

## 2. The complete two-copy witness

The saved maps realize

\[
 A(2,2)^{\otimes2}\oplus A(2,2)\oplus M_3
 \longrightarrow M_9.
 \tag{5}
\]

The common source coordinate blocks have dimensions `144,12,9`.
Every map has shape `81 by 165`, with common denominator four and
331 nonzero entries. The first block is the Kronecker product of
the original spin1 maps. The second block uses those maps on the
first matrix factor and takes the trace of the second. The last
block takes the trace of the first factor and uses the second
matrix factor. The third leg of each auxiliary block is negated.

For target vertices `I=3*i0+i1` and `J=3*j0+j1`, use target row
`9*I+J`. If `J0` denotes the original nine-by-twelve map with
denominator two, the three block row maps are

\[
\begin{aligned}
 &J_0(i_0,j_0)\otimes J_0(i_1,j_1),\\
 &J_0(i_0,j_0)\,\delta_{i_1,j_1},\\
 &\delta_{i_0,j_0}\,E_{i_1,j_1}.
\end{aligned}
\tag{6}
\]

The original source-coordinate permutations are applied separately
on the three legs, exactly as in the spin1 certificate.

The standard-library verifier reconstructs all 4,187 source terms:
`64^2` from the main block, 64 from the second block, and 27 from
the third. It accumulates their images with integer arithmetic and
checks all 531,441 target coefficients, including zeros. The result
has precisely the 729 coefficients of M9. It also checks the main
block before cancellation: that image has 2,601 nonzero coefficients,
and the complete residual has 2,025. Both auxiliary blocks together
are checked to be the negative of that entire residual.

This is a complete ordinary construction over the rationals. In
particular, it does not infer success from a numerical residual or
from the formal source dimensions.

## 3. The exact tensor-power residual

The residual in (3) is large even though the one-copy defect has
rank one. There is a useful exact statement for every integer `n>=2`.
Let

\[
 S_n(A,B,C)=\operatorname{tr}(ABC)
    +\operatorname{tr}(A)\operatorname{tr}(B)\operatorname{tr}(C),
 \qquad R_{n,k}=S_n^{\otimes k}-M_n^{\otimes k}.
\]

View the variables as matrices on `(C^n)` to tensor power `k`.
For a set `I` of tensor positions, let `Tr_I` denote the unnormalized
partial trace. Expansion of the tensor product gives

\[
 R_{n,k}(A,B,C)=
 \sum_{\varnothing\ne I\subseteq\{1,\ldots,k\}}
 \operatorname{tr}\!\left(
  (\operatorname{Tr}_I A)
  (\operatorname{Tr}_I B)
  (\operatorname{Tr}_I C)\right).
 \tag{7}
\]

For the full set `I`, the three partial traces are scalars. Formula
(7) follows on decomposable matrix inputs and then on all inputs by
trilinearity. It keeps the matrix order and requires no commutativity.

### Exact flattening rank

Over the complex numbers, every one of the three flattenings of
`R_(n,k)` has rank

\[
 \boxed{\ n^{2k}-(n^2-1)^k\ }.
 \tag{8}
\]

Indeed, every nonempty partial trace kills
`sl_n` to tensor power `k`. Formula (7) therefore places this
`(n^2-1)^k`-dimensional space in each flattening kernel, giving the
upper bound in (8).

For the reverse bound, specialize the second input to `I_n` to tensor
power `k`. On one factor,

\[
 S_n(A,I_n,C)=\operatorname{tr}(L(A)C),\qquad
 L(A)=A+n\operatorname{tr}(A)I_n.
\]

The trace pairing is nondegenerate. On `C*I_n direct_sum sl_n`, the
operator `L` has eigenvalues `1+n^2` and `1`. Consequently the
specialized residual is the trace pairing composed with
`L` to tensor power `k` minus the identity. On a tensor component with
exactly `j` scalar factors its eigenvalue is

\[
 (1+n^2)^j-1,
\]

with multiplicity `binom(k,j)*(n^2-1)^(k-j)`. In characteristic zero,
these eigenvalues vanish exactly when `j=0`. The specialized slice
has rank (8), so the flattening has at least that rank. The cyclic
symmetry gives the same conclusion on the other legs.

For the spin1 construction, the complete flattening kernel is thus
`sl_3` to tensor power `k`, and the residual rank is `9^k-8^k`.

| Power | Residual flattening rank | Minimum number of separate scalar corrections | Minimum size of an independent square matrix correction |
| ---: | ---: | ---: | ---: |
| 1 | 1 | 1 | 1 |
| 2 | 17 | 17 | 5 |
| 3 | 217 | 217 | 15 |
| 4 | 2,465 | 2,465 | 50 |

The last column is the ceiling of the square root of the second.
It is a necessary lower bound, not an asserted correction map.
Flattening rank cannot increase under restriction or degeneration,
so these lower bounds apply when a separate auxiliary source supplies
the whole residual (7), including when the auxiliary maps use the
same target variables as the main image. Polynomially many scalar
summands cannot supply this unchanged residual for unbounded `k`.

The statement fixes the original spin1 tensor-product image. It does
not exclude changing those maps, inserting cross-factor terms, or
cancelling errors together with additional source directions before
the residual (7) is formed.

## 4. Exact source-cost accounting at the current finite gate

The [existing finite-amplitude comparison](README.md#conditional-exponent-implication)
gives `6*P(2,2) <= 10^(1/t)`. Since A(2,2) is cyclic and invariant
under reflection, its character value is `P(2,2)^(3t)`. Set `p=3t`.
The source budget supplied by that comparison is therefore

\[
 \lambda(T)\le U_p:=\frac{1000}{6^p}.
 \tag{9}
\]

The matrix value is `lambda(M3)=3^p`. At the critical value `p=9/4`,
we have `U_p>3^p`, certified by the integer comparison

\[
 18^9<1000^4.
 \tag{10}
\]

The full source budget for (2) is

\[
 U_p^k+\sum_{j=0}^{k-1}U_p^j(3^p)^{k-1-j}.
 \tag{11}
\]

Already its first term exceeds the target value `3^(pk)` at `p=9/4`.
Thus the exact telescoping construction does not pass this finite
gate, even before charging its auxiliary summands.

There is a stronger dimension check for pure powers of A(2,2) under
the same comparison. If such a power restricts or degenerates to a
direct sum of square matrices of sizes `n_j`, conciseness implies

\[
 \sum_j n_j^2\le12^k.
\]

Since `p/2=9/8>1`,

\[
 \sum_j n_j^p\le
 \left(\sum_j n_j^2\right)^{p/2}\le12^{kp/2}.
\]

This is strictly less than `U_p^k`; raising the one-copy comparison
to the eighth power gives the exact certificate

\[
 6^{18}12^9<1000^8.
 \tag{12}
\]

Consequently no square direct-sum target from a pure A(2,2) tensor
power can cross the existing sixfold finite gate. This dimension
argument covers ordinary maps and singular degenerations. It is
scoped to this source budget and these targets. It does not exclude
another character inequality, a compression of the product source
into a differently priced convolution source, or general tensor-power
research.

## 5. Reproduction and verification boundary

The complete sparse witness, exact residual ranks, and integer cost
comparisons are stored in
`results/anisotropic-constructions-2026-10-20/scalar-power-recycling.json`.
The saved witness is independently replayed from its map entries;
the verifier does not regenerate them from the spin1 formula.

```sh
python -S research/ai/2026-10-20-anisotropic-constructions/scalar_power_recycling.py
python -S -m unittest discover -s tests -p test_scalar_power_recycling.py -v
```

The rank controls calculate the specialized residual matrices by
Kronecker products and exact rational elimination, for `n=2,k<=3`
and `n=3,k<=2`. They agree with (8). A tampered auxiliary sign fails
the full M9 coefficient replay. The all-size claims rely on the
written tensor identity and rank argument above, not on those finite
controls. This is work checked in the generating session; no external
independent review, historical priority, or formalization is claimed.
