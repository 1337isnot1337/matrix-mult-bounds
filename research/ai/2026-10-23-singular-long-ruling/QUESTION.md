# A singular long-leg limit and the shared kernel correction

Base: main `1c04903`. Concurrent PR113 at `08ac3e9` excludes the A4
target when one scalar-balanced long map has rank110 at zero. It leaves
singular limits open. PR112 independently studies general regularity from
the same regular-right-inverse projector; its rank102 unit-image corollary
is subsumed by PR113 and is not the new question here.

Question: if the regular long map C instead has rank c<110 at zero,
can the shared column space of the rank-two kernel corrections combine
with the existing source rank gap to exclude c>=106?

For every rank-one target parameter, the scalar-balanced first source
slice would have rank at most `11+2+(112-c)`. At c106 this is19, below
the next possible source rank20. A ten-dimensional rank-one target ruling
cannot map injectively into a linear space of minimum-rank source slices,
whose maximum vector dimension is four. The shared correction space is
needed to force such injectivity or make the leading first map vanish.

Intended evidence: written all-order proof, exact source pins including
the existing gap theorem's external splitting dependency, explicit shared
correction and target-ruling matrices, actual source rank16/20 controls,
and the c105 boundary. No complete singular degeneration exclusion,
independent review, formalization, constructed target or exponent gain.
