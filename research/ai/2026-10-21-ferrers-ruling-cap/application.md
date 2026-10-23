# Exact ordinary applications of the Ferrers dominance cap

October21,2026. Finite applications of written, unreviewed proofs.
No matrix tensor is constructed and no exponent gain is proved.

The application retains the source-lift inequalities, polynomial and
Hankel tests, quantitative crossed bound, proper-section refinement and
exact square-partition recurrence from the prior packages. Its only
new algebraic input is the closed-target cap in dominance.md, with the
uniform scalar Hankel linear-space cap as its hypothesis. The concurrent
rectangular worker's quantitative and bundle arguments retain their
credits at the exact sources.json pins. No archived file is changed.

For a scalar Hankel cone of rank at most r, every linear space has
dimension at most r when r<min(a,b). Over the algebraic closure of the
rational coefficient field, a bilinear parameter map sending every
rank-at-most-k matrix to that cone therefore has full image dimension
at most

    r                       if r<k(k+1),
    floor(r/k)^2+2(r mod k)   otherwise.

The usual independent scalar-coordinate injection then bounds the full
coefficient parameter dimension by this cap times ab. The lower-symbol
prerequisite for the crossed-locus test remains mandatory. No strict
source rank threshold is rounded to include equality.

## Balanced rectangular comparison

The saved PR83 comparison enumerates5139 improving sorted ordinary
rectangular shapes, for balanced sources a2..a12, and excludes4899.
This continuation preserves every previously excluded record byte-for-
byte as a JSON value and checks the240 remaining shapes. It excludes67
more, leaving173:5 at a10,38 at a11 and130 at a12. Every new inequality
and its coordinate order are retained in rectangular.json, and the tests
replay all67 using an independent complete-diagram dynamic program for
the cap. These are necessary-test survivors, not constructions. The
comparison is against PR83, not the full concurrent all-source frontier.

## Square direct sums

The existing exact recurrence checks every target dimension and every
square partition from A8 through A12. The score denominator is1000000;
acceptance uses integer interval bounds, not the display of a real power.

| a | Maximizing retained partition | Dimension | Score upper numerator | All improving sums excluded |
|---|---|---:|---:|---|
|8|27,1,1|731|93741340669|yes|
|9|32,5,3,1|1059|140053290292|yes|
|10|38,3,1,1,1|1456|202837340823|no|
|11|44,2,1|1941|281261289312|no|
|12|50,4,2,1,1|2522|376216828388|no|

At A8, an M27 block with total target dimension D>=732 has rank-two
lift upper54+2*(960-D)<512=8*64. Its scalar symbol has Hankel rank at
most7. The new cap at(r,k)=(7,2) is11, so its729 parameters would inject
into at most11*64=704 coefficients. Thus such a block cannot occur at
those dimensions. This sharpens the previous D743 score ceiling to D731.
The previous packages already excluded all improving A8 square sums;
this is a tighter ceiling, not another exponent result.

At A11 with an M44 block and total dimension1961, the rank-three lift
upper is3*44+2*(2541-1961)=1292<1331=11*121. Thus the scalar Hankel rank
is at most10. The former generic ruling cap16 gave1936=16*121, which
did not contradict the1936-dimensional block. The new closed-target
saturation gives cap10 because10<3*4, hence at most1210 coefficients,
a contradiction. The maximal retained square partition instead has
dimension1941. The A12 maximum decreases from2545 to2522.

The larger-source scores still exceed their critical thresholds, and
those retained partitions remain unconstructed. Other concurrent tests
may exclude them. No general singular degeneration, tensor-power
construction or complete exponent implication is supplied here.
