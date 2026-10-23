# Ordered monomial search audit

Base: main `3008d704d1797da02f7bf3f29cc1dbd4c0e7fa93`.
Reviewed PR118 head: `019269fad70d78845627e91eafe10b4063e3890c`.
Owner branch: `research/continuation-01a16975`.

R6 question: do the saved exact monomial certificates replay under an
independently implemented support and block checker, and what happens in the
omitted ordered dimensions a>b? The historical exhaustive scopes impose
2<=a<=b. That restriction is explicit in the archive but absent from PR118's
scope table. Swapping inputs changes the shared sector axis, so symmetry of
the source profile does not justify treating both score searches as identical.

Deliver an exact finite census over all a,b>=2 at the existing binary and
ternary size cutoffs, with separate old/new counts, a literal asymmetric
witness, and independent replay of every retained PR118 certificate. Preserve
all archives. A finite nonviolation or successful audit does not prove an
all-weight inequality, a tensor character, or an exponent improvement.

Overlap checked against all open PRs on October 23, 2026. PR118 owns the
maintained ranking implementation; this package owns its independent audit
and the additional ordered finite scopes. It does not replace that branch.

Refresh at publication: concurrent PR187 and PR192 appeared during this
investigation and overlap the ordered census and recognition result. Retain
this package as independently implemented confirmation and the separate
60-record PR118 audit; do not count matching conclusions as new discoveries.
