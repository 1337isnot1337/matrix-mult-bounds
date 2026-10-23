# Extend the balanced A4 rank frontier below rank 48

Selected October 23, 2026 after inspecting current pull requests through
PR135. PR122 at a284807699bc95e252087b3503b49da483116788 bounds the sum
of two regular long-map ranks by 192. Its compression-kernel argument
uses source slices below rank 32. The concurrent torus package at
c8c8246 bounds every linear source space of rank at most 23 by dimension
eight and excludes individual balanced long ranks of at least 102.

Can coordinate torus limits bound source spaces at ranks 32 through 47,
then strengthen the sum frontier through the saturated target-support
inequality? The output must include a proof for arbitrary complex source
subspaces, exact minor and block controls, and a finite integer rank-pair
screen. A numerical search or a coordinate-only obstruction is insufficient.

The question concerns necessary conditions on a missing degeneration.
It does not ask for, or claim, a smaller matrix multiplication exponent.
