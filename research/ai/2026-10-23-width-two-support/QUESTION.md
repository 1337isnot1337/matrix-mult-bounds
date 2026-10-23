# Width-two support scoring

Owner: this continuation, branch `research/continuation-01a1697b`.
Research base: main `3008d704d1797da02f7bf3f29cc1dbd4c0e7fa93`.

R3/R6 question: can the historical monomial search's matched-component
score exceed P*(2,b), at arbitrary b and arbitrary input weights, when
either input leg has dimension two?

Investigate the stronger combinatorial question for every coefficient-one
support subset of C(2,b) and C(b,2), whether or not a weight degeneration
realizes that subset. Retain the historical convolution recognizer and
single-slice fallback score. Prove an all-size statement and verify it
against exhaustive finite support subsets and the archived recognizer.

Coordination: open PR118 owns exact rational ordering and finite-weight
certificate replay. This package supplies a separate all-size proof and
does not change that branch or the historical archives. Main and the open
PR titles and PR118 description were inspected before selecting this task.
No subagents are used. No exponent improvement is claimed.

Subsequent concurrency check: PR189 at
`5f1a90680ed288d04829428d443c009156df128a` independently presents the
overlapping monomial theorem. PR191's maintained distinction is arbitrary
support deletions, and its PR description discloses the overlap. The
next owned question is the width-three weight-coherence argument on
`research/width-three-support-01a1697b`.
