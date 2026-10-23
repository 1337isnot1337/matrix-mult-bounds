# Boundary of the two-equal-leg staircase cover method

Selected October 23, 2026 from the finite S5 cube continuation in PR111,
at parent commit 043fb271d566747367662ab2faa6d8b81cb5875f.
Branch: research/s5-staircase-cover-boundary-20261023.

The weighted covers exclude M19 but do not exclude M(13,14,14).
Question: does allowing nonlinear monotone degree thresholds, with the
first two legs equal and the third leg independent, improve any of the
eight cube block-word covers? Exhaust the finite class with exact integer
costs, retain a best cover, and test the reduction against literal small
support enumeration. Do not infer optimality for three unequal legs,
nonmonotone covers, another basis or another source power.

An initial exhaustive pilot of 891888 first-leg staircases found the same
eight costs as PR111. The next work is reproducible independent validation
of the finite-class completeness argument and certificates.

Completed continuation: the separate Python and C++ r=1 enumerations agree
on all four three-unequal-leg minima. The77,392,758-pair universe and
5,207,743 evaluated pairs are recorded in three_leg_boundary.md. Seven
focused tests passed; no broader cover optimality or exponent gain.
