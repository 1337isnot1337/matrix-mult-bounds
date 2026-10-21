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
