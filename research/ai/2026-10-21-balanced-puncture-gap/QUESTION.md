# Can a balanced projection leave first dimension one or two?

Base: e804f27, after the complete projective cancellation classification
submitted in PR 94. This is a separate discovery branch, not a new theorem.

Question: for the rank-one-free skew pencil Z=span(E01-E10,E02-E20),
can two-dimensional kernels on each six-dimensional amplified matrix leg
leave a nonzero image of dimension at most two in Z tensor Mat2?

Registered finite pilot: all 651 binary RREF two-spaces on each leg,
423801 ordered kernel pairs. Compute every image dimension over F2;
replay every pair of modular image dimension at most two over Q, using
the signed skew pencil and exact rational lifts of the binary RREF kernels.
Keep field-lifting false positives separate. A negative finite screen does
not prove the arbitrary-complex-subspace assertion.

Positive controls: the known complete-cancellation kernels, and a rank-one
pencil with a nonzero two-dimensional projected image. No random sample or
unrecorded seed is involved. Preserve all completed counts and exact maps
for any rational counterexample before moving to a proof attempt.

Completed: the registered finite pilot found one zero image and no
nonzero image below four for the skew-pencil model. A separate written
complex proof now gives zero-or-four for that model and zero-or-three
for every rank-one-free matrix space of dimension at least two. The
general proof imports the classical complex Kronecker canonical form;
its elementary rank cases and canonical quotient arguments are supplied.
Six focused tests pass, including sharpness and essential-hypothesis
controls. This is written and unreviewed, not formalized.

Completed in the companion coupled-boundary package: simultaneous left
and right boundary obstruction ranks at most two force both complete
matrices to vanish. The exact cubic certificate reduces 228 parameters to
the prior 28-dimensional family and identifies its basis coefficientwise.

Next: higher-order compatibility of the conic non-plane normal survivors
and the separate 12-by-8 case. A first-normal classification does not
establish a full matrix-target lift or a smaller exponent.
