# Two finite-field construction formulations

October 20, 2026. Exact algebraic reductions with finite discovery records.
No new degeneration or matrix multiplication exponent is established.

## 1. Eliminate the known linear variables before solving

The predecessor's 68 elimination pivots are units in the integers. Their
inverses therefore remain valid over both residue fields used here, F3 and
F4. Apply those same pivots to the nonmonic formulation, replacing each
desired coefficient by its product of three target row scalars.

This leaves 57 free monic coefficients, 18 nonzero target scalars, and 53
polynomial equations. For every assignment to these 75 parameters, the
68 eliminated coefficients are uniquely determined. The original 121
coefficient equations hold exactly when the remaining 53 equations hold.
This is an alternative encoding of the preceding target-orbit formulation,
before any additional discovery filters. It does not prove solvability.

`eliminated_torus.py` implements the recurrences directly over each field.
The exact controls reconstruct every original coefficient independently.
They check that all 68 selected equations vanish and that every other
equation agrees with its retained residual. The integer coefficient map in
F4 uses characteristic two; it does not identify the field element encoded
as 2 with the integer two.

The recorded discovery runs additionally required at least one of the five
lower shared-polynomial coefficients to be nonzero in the residue field.
This is a search restriction, not a necessary condition for characteristic
zero lifting. A point with pure-power shared polynomials modulo a prime
could lift to a non-pure characteristic-zero point. The earlier pure-power
obstruction concerns exact characteristic-zero shared maps.

Both 120-second searches, one over F3 and one over F4, returned `unknown`
with reason `timeout`. Neither produced a model. Eliminating variables made
the expressions more complicated: the saved compressed queries are larger
than those from the cubic formulation. No search-speed improvement is
claimed from the reduction in variable count.

## 2. A symmetric polynomial-pairing subfamily

Retain the same monic shared polynomials G_p, input polynomials P_y, and
degree flags. Let H be one additional monic cubic and set

\[
 Q_z(f)=[t^{12}]H(t)P_z(t)f(t).
\]

The degree of H P_z is 12-rankZ(z), since this balanced order has
rankY(z)=rankZ(z). Thus Q_z has precisely the required nonzero pivot and
annihilates every smaller source degree. The Q rows are independent because
multiplication by nonzero H is injective and the P rows are independent.

The transformed tensor coefficient becomes

\[
 Q_z(G_pP_y)=[t^{12}]H G_p P_y P_z.
\]

It is symmetric in y and z. There are 53 free coefficients: five in G,
45 in P, and three in H. This is an extra restriction on the output maps,
not a normal form for all nonmonic flags.

The 121 entries of nonpositive weight are closed under exchanging y and z.
After identifying such pairs, the source needs 57 zero equations and ten
nonzero target conditions. Its two target-orbit binomials hold automatically:
each positive factor pairs with an equal negative factor after exchanging
y and z. The exact normalization in the main note therefore restores all
twenty desired target coefficients to one whenever these 67 conditions
hold. No additional binomial equation is needed in this subfamily.

`symmetric_pairing.py` reconstructs the full 125-variable source vector
from G, P, and H. Independent finite-field controls compare all 121
coefficients with direct four-polynomial multiplication and check the
target-orbit relations. The two recorded searches also excluded the
all-zero shared residue tuple, with the same limitation stated above.

Each search used a 60-second budget over F3 or F4. Both returned `unknown`
with reason `timeout`, without a model. They do not exclude this subfamily
over either residue field or over the complex numbers.

## 3. Verification boundary

These two formulations brought the package to ten exact tests. Their added
tests cover sixteen
symmetric-pairing reconstructions and sixteen elimination reconstructions
across F3 and F4. Each reconstruction checks all 121 original coefficients.
These tests establish the implemented equivalences at the checked inputs;
the algebraic arguments above establish their general form.

The finite queries, seeds, source hashes, budgets, and actual outcomes are
retained with the reports. The query hashes refer to uncompressed SMT text.
None of these four runs found a characteristic-zero lifting certificate.
An exact size-four degeneration would still need the separate growth
construction described in the predecessor before it could improve 9/4.

The later [compatible-chamber extension](chamber_search.md) adds two more
exact tests and changes the polynomial flags and nonpositive-weight mask.
Its equations and discovery runs are recorded separately.
