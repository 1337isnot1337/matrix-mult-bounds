# Unequal common-divisor source-space caps

Base: main `3008d704d1797da02f7bf3f29cc1dbd4c0e7fa93`.
Branch: `research/rectangular-divisor-cap-01a16975`.

Question: for `2<=a<=b` and a positive common divisor `d` of `a,b`, is
the maximum dimension of an arbitrary complex linear source-slice space
of rank at most `q` exactly `bd` throughout
`a(b+d-1)<=q<a(b+d)`?

PR148 gives the balanced proper-divisor statement. PR171 studies individual
binomial ranks; PR186 studies an elementary general biform gap; PR190
studies nondivisor widths. This question instead extends the dimension
cap to unequal source sizes, using the existing complex biform lemma on
main. It does not depend on those other branches' proposed new lemmas.

Intended output: an all-size proof, an explicit rectangular coordinate
partition, exact residue-block and strip controls, and a stated regular-
long-leg corollary. No target construction or exponent gain is expected
from a source-space cap alone.
