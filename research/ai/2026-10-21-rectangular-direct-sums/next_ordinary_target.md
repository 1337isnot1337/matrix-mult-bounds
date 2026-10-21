# The first remaining ordinary target through dimension1500

October21,2026. Open construction problem after necessary tests.
No target maps or improved exponent are claimed.

The updated scan covers86 formats A(a,b),2<=a<=b, with source leg dimension
at most1500. Among2184 strictly improving sorted single rectangular shapes,
2183 are excluded by the maintained written lemmas. The only survivor is

    A(8,10) -> M(32,33,33).

Its source legs have dimension1360 and its target legs have dimensions
1056,1089,1056. The previous A89 to M30 target is now excluded by the
two-ruling theorem. The same shape from A99 is excluded by its three-ruling
variant. This is the first *not excluded* ordinary source size in this scan;
it is not a claim that a restriction exists at this size.

If the missing restriction were constructed, the existing cyclic-source
spectral implication would give

    omega <= 9 log(52)/log(7527168), approximately2.2458713757.

Here7527168=216*(32*33*33), and the strict rational consequence
omega<2246/1000 has the integer certificate52^9000<7527168^2246.
The whole tensor restriction is missing. This conditional arithmetic is
not an attained improvement.

## Why the new gate stops one rank short

On the1056-dimensional first target parameter leg, a rank-two input lifts
to source slice rank at most

    2*33+(1360-1089)+(1360-1056)=641.

The full scalar-symbol rank threshold is8*80=640. Thus the new argument
cannot force scalar Hankel rank at most7. If it could, its dimension bound
would be12*80=960<1056, a contradiction.

This one-rank gap cannot be rounded away. The already recorded one-step
slice counterexample for A(8,10) has source slice rank641, full scalar
symbol rank8 and crossed coefficient rank9. It is a slice, not a target
construction, but it invalidates that tempting shortcut.

Any proposed ordinary restriction must therefore have full scalar-symbol
rank8 on a generic rank-two parameter. The quantitative crossed bound
then gives crossed rank at most9. The all-rank bundle dimension bound is
9*(8+10)+1=163, while the rank-two parameter variety has dimension
2*(32+33-2)=126. This dimension test alone does not exclude the target.
A stronger structural argument or actual cancellation maps are still needed.

## Replay scope

`single-frontier-1500.json` records all2184 shapes and gate witnesses.
The five needed top-Hankel cap formats have74360 integer coordinate minor
certificates. Their general torus and dimension arguments remain written
and unreviewed. Singular degenerations and multiple-block targets are not
closed by this single ordinary scan.

## Restricted distinct-atom continuation

The new `distinct_atoms.md` proves a sharp650 lower bound when a slice
has crossed rank9 and consists of nine distinct finite rank-one spectral
atoms. Such a slice misses the641 ceiling. This narrows that ansatz only:
crossed rank8, repeated/infinite support and general slices are untouched.
The existing641 counterexample remains valid.

The subsequent `cyclic_state_gap.md` extends the650 obstruction to
observable cyclic finite-state realizations of dimension9, including
repeated eigenvalues with one Jordan block each. Its proof forces source
rank divisible by10. General noncyclic states and boundary support remain
open; the existing641 example has state J8 direct_sum J1 and is noncyclic.

The one-unit case also forces two degree-one primitive polynomial relations
by `one_unit_syzygies.md`: inner span dimension9/rank8 and outer span
dimension65/rank64. The actual641 slice realizes these relations. This
provides exact structure to use in a construction or a further exclusion;
it does not settle the remaining ordinary target.

The factor criterion in `one_unit_pairing.md` makes those constraints
explicit: the two primitive kernel pencils must have separable nonzero
bilinear pairing. At the known sparse641 example, fixing these pencils
leaves exact tangent-image dimension149 after the Hankel linearization.
This exceeds126 and does not exclude the target; integrating useful
deformations and realizing the target's full tensor remain open.

An explicit integrated family now appears in `one_unit_convolution_family.md`.
It has image dimension134 and generic source slice rank641. Its separate
one-factor spaces have dimensions79 and63, so the straightforward
separate-factor target parameterization is one coordinate short on the
smaller side. This is a source-slice construction, not the missing full
tensor restriction.

The fixed convolution family's exact linear span is622, below the required
1056. The common ninth-power-divisor pencil argument also closes the union
of its long-GL2 translates as a possible image of all rank-two parameters:
linearity would force one common support point and ambient dimension640.
Multiple long-support points and general slices remain outside this argument.

The broader `multiple_support_family.md` now supplies a141-dimensional
nonlinear family of generic rank641 slices with full ambient span1360.
It uses one double and six simple long-support points. This escapes the
fixed-fat-point span obstruction; constructing the required linear target
parameter map and complete tensor restriction remains open.
