# Nonmonic balanced flags through the target diagonal orbit

October 20, 2026. AI-derived written reduction with exact finite controls.
The reduction is unreviewed. No tensor degeneration or smaller matrix
multiplication exponent has been established.

## Construction question

Can the balanced polynomial flags realize `C(4,10) -> T4` when their leading
coefficients may be arbitrary nonzero numbers?

The predecessor fixes every leading coefficient to one and every desired
target coefficient to one. Those two normalizations cannot both be assumed
without justification. This package removes the first restriction within the
same degree flags and weight order. The later chamber extension below uses
the same flag construction with a different weight order. Neither covers
arbitrary Laurent input maps.

The source and target, the balanced order
`beta=100, eta=(0,201,403,607)`, and the polynomial flag model are adopted
from the existing [balanced coefficient package](../2026-10-20-balanced-coefficients/elimination.md).
Its 121 entries of nonpositive parameter weight consist of 101 required
zeros and 20 desired coefficients. It has 125 monic polynomial coefficients
after the source-translation anchor. An exact solution is still missing.

## 1. Replacing leading coefficients by target row scalings

Write the nonzero leading coefficients of the three families of flag
polynomials as `g_p`, `b_y`, and `c_z`. Dividing each polynomial by its
leading coefficient makes it monic. This changes a desired unit tensor
coefficient to

`t_(p,y,z) = 1/(g_p b_y c_z)`.

Conversely, suppose monic flag polynomials give the correct zero pattern and
their twenty desired coefficients have the form

`t_(p,y,z) = alpha_p beta_y gamma_z`,

with all row scalars nonzero. Dividing the three polynomial rows by these
scalars gives the desired unit coefficients. This division preserves every
zero, degree flag, and parameter weight. Thus membership in the target's
diagonal orbit is exactly the remaining normalization requirement.

The source-translation anchor remains valid: the degree-one shared
polynomial can be made `t` by an affine substitution, followed by row
normalization. Polynomial multiplication respects the same substitution on
all three spaces. The degree-zero shared polynomial then normalizes to one.

## 2. Only two multiplicative relations remain

Index the ten Y and Z coordinates in the existing order

`(0,0), (0,1), (1,0), (0,2), (1,1), (2,0), (0,3), (1,2), (2,1), (3,0)`.

List the twenty desired triples `(p,y,z)` in lexicographic order; the list
is exported in `structure.json`. Let `t_0,...,t_19` denote their nonzero
coefficients. Then the coefficients are diagonally equivalent to `T4` if
and only if

```
t_2 t_5 t_6 t_13  = t_1 t_7 t_8 t_12,
t_2 t_6 t_11 t_18 = t_1 t_7 t_14 t_17.
```

This statement holds over every field, including fields of characteristic
two and three. The coefficients must all be nonzero.

Here is an integer certificate and proof. Form the `20 x 24` incidence
matrix `E`, putting ones in columns `p`, `4+y`, and `14+z` of row
`(p,y,z)`. Each of the two displayed relations is an integer vector in
the kernel of `E^T`. Necessity follows by substituting row scalars.

For sufficiency, select all rows except 13 and 18, and select the eighteen
columns

`0,1,2,3,4,5,6,7,8,9,10,11,12,15,17,18,20,21`.

The resulting square matrix `D` has determinant `-1`. Its inverse is
integral; `structure.json` contains every entry. Set the six unselected
row scalars to one. For selected scalar `s_j`, use the Laurent monomial

`s_j = product_(i=1)^18 t_(selected row i)^((D^-1)_(j,i))`.

The selected eighteen coefficients are then reproduced exactly, over any
field. The first displayed relation uniquely determines `t_13`, and the
second uniquely determines `t_18`, because all coefficients are nonzero.
They therefore reproduce the other two coefficients as well. No roots,
field extensions, or logarithms are used in this exact normalization.

The target diagonal orbit consequently has dimension 18. The twenty
desired unit equations may be replaced by two binomial equations and twenty
nonvanishing conditions. Together with the 101 zero equations this gives
103 polynomial equations in the 125 monic coefficients, on an explicitly
specified open set. The binomials have degree at most twelve in those
coefficients. This is a reformulation of the stated nonmonic flag class,
not an existence result inferred from the variable count.

The same reduction now has a uniform form for every `m>=2` in
[uniform_normalization.md](uniform_normalization.md). It selects
`m^2+m-2` independent target coefficients and gives an explicit Laurent
inverse, leaving `(m-3)(m-2)(m+2)/6` binomial relations. The selected
incidence minor is unimodular in every degree. This statement has a written
all-degree proof; finite exact controls are included as implementation checks.

## 3. A finite characteristic-zero existence certificate

`torus_exact.py` checks the 101 zero equations, the two binomials, the
twenty nonvanishing conditions, and the `103 x 125` Jacobian over `F3` or
`F4`. It evaluates coefficients by a direct sparse polynomial expression.
The regression suite compares these values with separate polynomial
multiplications in the original source coordinates.

If a point satisfies all these conditions and the Jacobian has row rank
103, select a nonzero `103 x 103` minor and fix the other 22 variables.
The multivariable Hensel theorem used in the predecessor lifts that square
system over `Z_3`, or over the unramified degree-two extension of `Z_2`
with residue field `F4`. Every desired coefficient stays a unit. The
integer Laurent-monomial normalization above therefore gives a unit-target
degeneration over the fraction field.

The predecessor's proper-ideal and weak-Nullstellensatz argument then
produces a complex algebraic solution. Apply it to the augmented ideal
including `v * product(t_0,...,t_19) - 1`; the lifted point extends to this
equation because all target coefficients are units. This retains the open
nonzero condition in the resulting algebraic point. This use of Hensel's lemma has the
same hypotheses as its cited Keith Conrad reference: polynomial equations
over a complete valuation ring, zero residue, and invertible Jacobian
determinant. A random point with a large Jacobian rank is not sufficient;
it must also solve the equations and satisfy all nonvanishing conditions.

No qualifying finite-field point is supplied by this package.

## 4. Discovery and limits

The optional `pivot_torus.py` numerical program reuses the predecessor's
68 linear eliminations. It retains 57 monic free coefficients and adds
18 target row scalars, represented numerically by exponentials. Thus it
solves 53 residual equations in 75 complex parameters. Numerical residuals
are divided by the target row products before optimization; this prevents
small target coefficients alone from making the reported error look small.
A separate convolution calculation checks all 121 normalized coefficients
of nonpositive parameter weight.

This program uses NumPy and SciPy only for discovery. Neither floating
point residuals nor untraced solver failures prove existence or exclusion.
The exact verifier and its regression tests require only the repository's
maintained SymPy dependency. Z3 is optional discovery software.

The [completed search record](search_outcomes.md) distinguishes normalized
coefficient errors from certificates. Four finite-field runs returned
`unknown` at their 180-second limits. Numerical runs found small errors with
nearly singular Jacobians, but no exact solution. The exact pure-power
shared-polynomial limit is excluded by reduction to an existing repository
obstruction; this observation prevents further work in that closed stratum.

The [two additional finite formulations](finite_formulations.md) retain the
same exact construction question. One applies the 68 known unit pivots first,
leaving 75 residue-field parameters and 53 equations. The other imposes a
symmetric polynomial pairing, with 53 parameters, 57 zero equations, and ten
nonzero target conditions. Their four bounded searches also timed out without
models. The smaller variable counts are not claimed as solver improvements.

The [new compatible chamber](chamber_search.md) changes the offsets to
`eta=(0,301,628,844)`. It has 95 required zero coefficients and the same
two target-orbit relations, giving 97 equations in 125 monic coefficients.
The new chamber was found in a reproducible sample of 20,000 integer weight
triples. Its full finite-field queries and bounded numerical run produced
no exact solution. Thirteen exact tests now cover the coefficient systems, including the new
chamber's 65 unit pivots and 50 residual coefficient equations.

Even an exact size-four degeneration would not itself lower `9/4`.
Its source-to-target implication is the earlier finite construction
question. Replication with controlled source overhead, or another complete
growth argument, would still be required. That implication is not claimed
from the dimension count or the new target-orbit reduction.

## Reproduction

```
python research/ai/2026-10-20-new-source-constructions/torus_exact.py --structure-only --output results/new-source-constructions-2026-10-20/structure.json
python research/ai/2026-10-20-new-source-constructions/general_target_orbit.py --maximum-m 7 --output results/new-source-constructions-2026-10-20/general-structure.json
python -m unittest discover -s tests -p test_nonmonic_target_orbit.py -v
```

The optional discovery programs save seeds, bounds, completed iterations,
source hashes, and outcomes. See the reports for their actual scope.

## Attribution

This package starts from repository commit
`9a4ee3d05939d88730045877a6945165845f0398`. The target, weights, flag
normal form, monic polynomial representation, triangular elimination, and
characteristic-zero lifting argument come from the existing singular-flag
and balanced-coefficient packages. The new contribution is the exact target
diagonal-orbit reduction, its unimodular normalization, and the corresponding
nonmonic discovery/checking formulation. No historical priority or
independent mathematical review is claimed.

The external `9/4` theorem remains OpenAI's result. This construction
question does not establish a new arithmetic exponent.
