# A ceiling for correlated matrix extraction from the finite targets

Date: 2026-10-21.

This section strengthens the scalar audit for one concrete way of using the
actual finite targets. Take arbitrary tensor products of the accepted
targets, including mixed values of m and arbitrary leg permutations.
Afterwards allow an arbitrary degeneration to a direct sum of rectangular
matrix-multiplication tensors.

The character lower bound obtained this way cannot exceed the uniform
endpoint assignment P_* on the corresponding convolution sources.
Correlated choices of sectors and unrestricted linear maps in the final
extraction are allowed. This is a ceiling on this extraction method,
not an upper bound on the character of a target tensor.

## 1. A format-only inequality

At an endpoint character every dot-product exponent is 3/4. This equality
is proved from Uznański v2, Proposition 5.2, in the existing
[finite amplitude note](../2026-10-20-koszul/finite_amplitude.md).
A rectangular matrix tensor with leg dimensions A=lh, B=hn, C=nl has character

    (lhn)^(3/4)=(ABC)^(3/8).

Suppose a tensor of format (D_1,D_2,D_3) degenerates to a direct sum of
such tensors, indexed by j. Flattening ranks give
sum_j A_j<=D_1, sum_j B_j<=D_2, sum_j C_j<=D_3.
Holder and sum_j x_j^(9/8)<=(sum_j x_j)^(9/8) imply

    sum_j (A_j B_j C_j)^(3/8)
    <= product_(i=1)^3 (sum_j D_(i,j)^(9/8))^(1/3)
    <= (D_1 D_2 D_3)^(3/8).                         (1)

This argument applies to arbitrary degenerations, not only coordinate maps.

For a matched target of format (m,N,N), N=m(m+1)/2, the right side is
(mN^2)^(3/8). The uniform formal endpoint assignment on its source
C(a,B) is P_*(a,B)^(3/4). Thus the extraction route is bounded by that
assignment whenever

    mN^2 <= P_*(a,B)^2.                              (2)

Every accepted finite target satisfies (2) strictly:

| m | a | B | mN^2/P_*(a,B)^2 |
| ---: | ---: | ---: | ---: |
| 4 | 5 | 10 | 6561/8281 |
| 5 | 6 | 16 | 597871125/725548096 |
| 6 | 7 | 24 | 1594323/1952288 |
| 7 | 8 | 34 | 14765025303/18455222500 |
| 5 | 7 | 15 | 597871125/765296896 |
| 8, hypothetical | 9 | 46 | 2259436291848/2883628515625 |

The m=8 row remains hypothetical because its certificate was not recovered.

## 2. Arbitrary powers, mixtures and permutations

For a product of targets indexed by i, the product of its three format
dimensions is

    product_i m_i N_i^2,

regardless of the leg permutations. Multiplying (2) therefore bounds (1)
by

    product_i P_*(a_i,B_i)^(3/4).

This is exactly the value assigned to the corresponding product of
convolution sources by the uniform endpoint model. There is no assumption
that an extracted matrix block comes from a single sector, a single
factor, or an independent choice of local labels. Correlations and mixed
rectangular shapes are already included in the format bound.

Dot-product auxiliary tensors may also be included: their product of
format dimensions is k^2 and their endpoint character is k^(3/4), so
their factors cancel exactly from this comparison.

Arbitrary additional auxiliary tensors, new source compressions, or
non-matrix target tensors are outside this statement. In particular,
the bound does not constrain all possible information contained in the
finite maps.

## 3. Oriented entropy by itself

At the endpoint all shared power exponents are equal to 4/3. Assigning
each oriented powered convolution value the same symmetric P_* satisfies
each of the six individual finite shared-leg inequalities, not merely
their symmetrized product. Thus keeping those six inequalities separate
does not remove the feasible assignment.

For powers with the same common shared leg, applying only the existing
shared-sector entropy inequality also gives no correlation gain. For
positive sector weights v_r, its optimum is

    (sum_r v_r^(4/3))^(3/4).

On tensor products the sum over all sector tuples factors. Equivalently,
the Gibbs entropy maximum is attained by the product distribution;
subadditivity of entropy bounds any correlated distribution by the same
value. This last observation concerns that entropy inequality alone.
Crossed partitions or a new tensor comparison may contain information
not captured by it.

## 4. Consequence and verification

The surviving possibilities need a rule outside this matrix-extraction
ceiling, for example a stronger comparison with a non-matrix tensor, or
a different source construction. A claim that the finite targets improve
the exponent merely by taking large powers and extracting matrix products
would need to overcome (1)-(2).

The exact ratios are replayed by the companion verify.py. The proof is
the all-size Holder argument, not the finite list of arithmetic checks.
Same-session AI review is not external independent certification.
