# Paired convolution sources

Owner: product-filtration worker, research/paired-source-kernel-20261020.
Base: main 9b2fcc3, after the balanced equations package merged in PR #15.
The exponent goal is active. No bound below 9/4 is established.

Group the six permutations of C(a,a) into three cyclic copies of
P_a=C(a,a)_(A,B,C) tensor C(a,a)_(A,C,B). Its format is
(a^2,a(2a-1),a(2a-1)). Investigate matrix-product extraction from these
smaller paired sources, rather than fitting the full six-factor tensor.

The first exact calculation gives a 3a-2 dimensional first Koszul kernel.
It rules out full-capacity M(a,2a-1,a) under arbitrary complex degeneration,
and excludes the promising full-format size-five direct sum below. A finite
integer budget certificate bounds all one-copy matrix-block extraction
scores at a=4. These are source and method obstructions, not exponent gains.

Selected open construction: P_6 degenerating to M(6,10,6), in formats
(36,66,66) to (36,60,60). It would imply omega<=2.235 by the existing
spectral and convolution inequalities. The source has border rank at most
121. Ordinary restrictions and the adopted coordinate-input ansatz are
excluded; a construction must use genuine input mixing and a singular
family. The first Koszul ranks do not exclude it. Stronger necessary tests
and an actual coefficient construction remain open.
