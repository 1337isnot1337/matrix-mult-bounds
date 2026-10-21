# A rational six-sector construction from C(7,28)

October 21, 2026. Explicit rational finite construction, checked within
the same AI research session. External mathematical review and
formalization remain outstanding. No smaller exponent is established.

## Statement and complete certificate

With the matched-sector convention of the [five-sector note](README.md),
there is an explicit rational degeneration

\[
C(7,28)\unrhd\widetilde T_6
=\sum_{p=0}^5\sum_{a=0}^p\sum_{c=0}^{5-p}\sum_{i=0}^5
(H_p)_{i,a+c}X_iY_{a,p-a}Z_{c,5-p-c},
\]

with each `H_p` invertible. This certifies actual matched convolution
sectors, not an identification of the whole tensor with canonical `T6`.

The source is `sum_(d=0)^6 sum_(j=0)^27 A_d Y_j Z_(d+j)`.
The three constant maps have shapes `6 by 7`, `21 by 28`, and `21 by 34`.
The shared rows are `1,t,t^3,t^4,t^5,t^6`. Input rows of target degree `p`
have weight `p`; output rows of degree `q` have weight `q-5`. Thus a
coefficient has exponent `p+q-5`.

The [witness](../../../results/selfadjoint-sectors-2026-10-21/m6-witness.json)
specifies every rational entry. The separate standard-library verifier
expands all 196 source monomials into all 2,646 coefficient positions.
It checks 420 negative zeros and 336 required constants. There are 210
nonzero constant coefficients and 1,083 nonzero positive remainder
coefficients, with degrees one through five. The map ranks are `6,21,21`.
The six sector determinants are

\[
1,\quad 1/3220480,\quad -4,\quad -4,\quad 1/3220480,\quad 1.
\]

The certificate proves the degeneration over every characteristic-zero
field. It has source length `28=21+7` at this finite size. No unbounded
cost bound follows from that equality.

## Two moment bands and an exact central block

Use the symmetric forms `B_d(f,g)=L(t^d f g)`, for
`d in {0,1,3,4,5,6}`, on polynomials through degree 27. Put `h=t^22`.
The only nonzero moments are the top moment `L(t^43)=1` and the following
band:

\[
(L(t^{11}),\ldots,L(t^{21}))
=(-1,-1,1,0,-1,1,-1,-1,1,1,1).
\]

The three low polynomials are `h f_0,h f_1,h f_2`, where the coefficient
rows of the `f_i`, in degrees zero through five, are

\[
\begin{pmatrix}
0&-1&0&1&-1&-1\\
1&-1&0&1&-1&1\\
-1&-1&-1&0&0&-1
\end{pmatrix}.
\]

They have target degrees zero, one, one. Their pairwise products are
annihilated by every form because they are divisible by `t^44`.
Their products with the shared space span `t^22 P_11`, of dimension 12.

Choose the degree-two rows `1,t,t^2` and degree-three rows
`t^6,t^7,t^8,t^9`. All seven lie in the common annihilator of the low
rows. Indeed, the top moment cannot be reached by multiplying any of
these monomials with `t^22 P_11`, and the lower band lies below degree 22.
The three degree-two rows pair to zero because their products with any
shared monomial have degree at most ten. The `3 by 4` cross-pairing is
Hankel, with the six anti-diagonal vectors

\[
H_2=H_3=\begin{pmatrix}
0&0&0&0&0&-1\\
0&0&0&0&-1&-1\\
0&0&-1&-1&1&0\\
0&-1&-1&1&0&-1\\
-1&-1&1&0&-1&1\\
-1&1&0&-1&1&-1
\end{pmatrix}.
\]

Its determinant is `-4`. This gives the `C(3,4)` and `C(4,3)` sectors
under invertible shared maps.

For the degree-four rows, use the same cofactor-pencil method as in the
five-sector construction. The annihilator of `U h f_0` has dimension
22. Modulo the 16-dimensional annihilator of all three low rows, it has
dimension six. The saved five representatives give a full `5 by 6`
pencil whose degree-five kernel coefficients are independent. Exact
normalization gives `H_1=H_4` with determinant `1/3220480`.
The top six rows are a right inverse for the six functionals
`B_d(h f_0,-)`, so `H_0=H_5=I`.

The output row associated with any input polynomial `g` is
`Z_g(t^k)=L(g t^k)` for `k=0,...,33`. This converts the moment pairing
into actual convolution maps. The saved coefficient identity checks all
vanishing and target equations, including those between different parts
of this construction.

The degree-two rows are ordinary low-degree monomials and do not lie in
the high ideal `(t^22)`. Consequently the
[common-ideal bound](common_ideal_bound.md), when applied to every
strictly lower target degree, does not cover this mixed construction.
This observation permits further experiments; it is not an asymptotic
recursion theorem.

## Reproduction

Run from the repository root:

```sh
python research/ai/2026-10-21-selfadjoint-sectors/verify_witness.py results/selfadjoint-sectors-2026-10-21/m6-witness.json
python -m unittest discover -s tests -p test_selfadjoint_sectors.py -v
```

Optional reconstruction uses SymPy 1.14 and recorded seed 7:

```sh
python research/ai/2026-10-21-selfadjoint-sectors/construct_m6.py --seed 7 --output /tmp/selfadjoint-m6-reconstructed.json
```

This extends the five-sector moment method developed in the same research
session. The existing character criterion applies to actual sectors with
independent invertible shared bases; its sources and conditional status
are recorded in the linked notes.
