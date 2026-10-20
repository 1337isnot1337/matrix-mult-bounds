# Exact source cost and the missing tensor witness

This is a finite source calculation and a conditional implication. There is
currently no degeneration to the selected target and no smaller exponent.

## Recovering the complex blocks without a character table

`source_certificate.py` enumerates the determinant-one matrices over F7 and
their products. There are 336 elements and eleven conjugacy classes. Products
of class sums give the rational center of Q[G]. The element whose class-sum
coefficients are 0,1,...,10 generates this center: its first eleven powers
have the nonzero determinant recorded in the certificate.

Its minimal polynomial is squarefree, with five linear and three quadratic
irreducible rational factors. Exact polynomial CRT gives eight orthogonal
central idempotents summing to the identity. For each factor f of degree r,
the corresponding rational block splits over C into r simple matrix blocks
of the same dimension d squared. The equality follows from Galois conjugacy;
it does not assume a rational realization of the irreducible representation.
Maschke semisimplicity applies in characteristic zero.

Left multiplication by an element e of Q[G] has regular trace 336 times
the identity coefficient of e. An idempotent has trace equal to rank, hence

    d squared = 336 * e[identity] / r.

Every result is an integer square. The derived complex matrix degrees are

    1, 3, 3, 4, 4, 6, 6, 6, 7, 8, 8.

Their squares sum to 336. The derivation verifies the polynomial identity,
irreducibility, cyclicity, all idempotent identities, and the dimension sum
using exact SymPy integer and rational arithmetic. No floating character
values or imported character table enter this calculation. The general
semisimple-algebra facts used to interpret it are a written argument, without
independent review or Lean formalization.

## Conditional exponent comparison

Suppose the group algebra multiplication tensor degenerates to M(a,b,c).
Write V=abc. The standard group algebra method, including border conversion,
gives

    V^(omega/3) <= sum_j d_j^omega.

For completeness, take the tensor product of the three cyclic orientations
of the target, obtaining M(V,V,V). The source has the corresponding product
of three copies of its matrix blocks. Taking n-th tensor powers and using
algorithms with exponent omega+epsilon bounds their total rank by a constant
times `(sum d_j^(omega+epsilon))^(3n)`. A fixed polynomial degeneration costs
only a polynomial factor under interpolation of tensor powers. Taking n-th
roots, then epsilon to zero, gives the displayed inequality. These are the
standard tensor-power and border-conversion steps, not a new external
matrix multiplication theorem. The group algebra framework is due to
[Cohn and Umans](https://arxiv.org/abs/math/0307321).

For V=16*16*17=4352, the exact root-interval calculation verifies

    sum_j d_j^(2247/1000) < V^(749/1000).

All intervals have denominator 10^10. The source upper numerator is
5,309,704,615,926 and the target lower numerator is 5,313,466,858,712.
Each endpoint is checked by raising integers to the relevant power. Because
each d_j < V^(1/3), the ratio `sum (d_j/V^(1/3))^s` is strictly decreasing in s.
Thus the hypothetical degeneration would imply omega < 2247/1000.

**The required degeneration has not been found.** A passing cost comparison
does not establish one. The SAT search is a bounded discovery experiment;
only an accepted integer potential certificate would supply its intended
construction. A timeout or an untraced solver status is no impossibility proof.

## Search normalization

The upper triangular Borel subgroup H has order 42 and index 8. Any set of
size k has at least ceil(k/8) points in one right coset Hx. An independent
right translation moves those points into H and a selected member to the
identity. Independent translations preserve the three cyclic pair labels
and all group-product equations by cancellation.

The first set has at least two points in H. Normalize their quotient, up to
pair reversal, by conjugation with an upper triangular invertible matrix.
This conjugation preserves H. `borel-certificate.json` enumerates witnesses
for all 41 nonidentity quotients and covers five anchor orbits. Thus the
extra Borel cardinality and anchor clauses preserve the intended search.
This is a written justification plus finite exact coverage, not a certified
complete SAT refutation.
