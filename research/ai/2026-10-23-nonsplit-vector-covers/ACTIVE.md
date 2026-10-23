# Nonsplit multidegree cube covers

Question, October 23, 2026: can coordinate covers of the separate principal,
matrix-central and extra-central degree bounds improve the scalar weighted
cube certificate for SL(2,F5) x C2? The intended output is an exact finite
cover or a scoped bounded discovery report. No asymptotic cost or exponent
gain follows from either outcome.

Base: d833eb0265a3e107636e8a0678c14fc07df812c2. The prior nonsplit package
is being finished in another local session; this investigation leaves it
untouched and uses its saved basis degrees as discovery input. Open PRs
and local worktree/process ownership were checked before selection.

For a cube block with j principal factors, keep three degree coordinates
(p,b,e), with source bounds sum p <= 8j, sum b <= 3-j and sum e <= 3.
A safe cover hits every triple satisfying all three bounds. Its class
multiplicities come from the integer polynomial
P(u)^j [16(1+v)]^(3-j) (1+w)^3. A numerical optimizer may propose class
sets; acceptance must count them exactly and check all admissible triples,
and must retain the original full-source basis verification as a premise.

Completed discovery: all seven vector-degree runs returned the old costs;
the source parity condition was checked densely against the pinned PR102
source. The complete 3372-vector integer census combining degree with the
saved cover also gives 6155844. Four focused tests and exact standalone
replay pass. The complete four-group regression ran 854 tests: 851 passed
and three optional controls skipped. All five archive replays pass; all
18 protected archive files match the base byte-for-byte. Prerequisite
PR102 merged as dcd209a and is integrated here. Four focused and 18
metadata tests pass after integration. CI passed at 9f177b0; the final
integration/receipt head still needs its current checks.

No new source-bound gain, class-wide cover optimum or exponent improvement
is claimed. Next: retain finer Peirce-corner information or change basis/
power; do not repeat this unchanged scalar/vector degree census.
