# Quantitative crossed-rank bound

October 21, 2026. Written proof, unreviewed. No exponent improvement.

For a source slice F, let r be the rational-function rank of its polynomial
Hankel symbol B_F, and let d be the rank of its crossed coefficient flattening
T_F. Then

    rank(M_F) >= (ab-1) r + d.                         (1)

Consequently rank(M_F)<=ab r+delta implies d<=r+delta. The equality lemma
is the special case delta=0. The exact A89 rank577/crossed-rank9 example
shows that the coefficient of delta cannot be improved merely by asserting
a missing one-unit rank stratum.

## A polynomial-span growth lemma

Let S be a finite-dimensional space of vector polynomials over an infinite
field K, with dimension d_0 and rank r_0 over K(t). Put
W_T=S+tS+...+t^(T-1)S. Then

    dim_K W_T >= d_0+(T-1)r_0.

Choose a constant c where evaluation of S has rank r_0. For every T>=2,
(t-c)W_(T-1) is a dimension-preserving subspace of W_T in the evaluation
kernel, while the evaluation image of W_T contains that of S. Hence
 dim W_T>=dim W_(T-1)+r_0. Induction proves the claim. No discarded output
coefficients or generic-polynomial-as-unit assumption is used.

## Apply it twice

Use the maintained K(x) from `polynomial_rank_locus.md`. Its rank over C(x)
is rho>=ar. Its degree-b input coefficient map is exactly M_F^T. If D is
the dimension of the constant span of the polynomial columns of K, the
growth lemma gives

    rank(M_F) >= D+(b-1)rho.                           (2)

Write B_F(x,z)=sum_i x^i B_i(z). Transposing the coefficient matrix whose
column span defines D identifies its image with the span of

    z^j times every column of every B_i(z),  0<=j<a.

Before adjoining the shifts, those columns span a vector-polynomial space
S of dimension exactly d=rank(T_F). Its rank R over C(z) is at least r:
extending scalars and taking their x-weighted sums recovers all columns of
B_F. The same growth lemma therefore gives

    D >= d+(a-1)R >= d+(a-1)r.                        (3)

Combining (2), (3), and rho>=ar yields
 d+(a-1)r+(b-1)ar = d+(ab-1)r, proving (1).

## Current limitation

For a full-symbol-rank A89 slice with rank at most578, (1) gives crossed
rank at most10. The proved block-Hankel dimension theorem only covers ranks
up to the smaller block-window size, eight. It cannot currently convert this
rank-ten bound into a dimension obstruction. A dimension bound for higher
rank block-Hankel strata would be a genuinely new required input, and the
finite frontier does not assume one. The analogous issue occurs one unit
above the full-symbol equality threshold for A810.
