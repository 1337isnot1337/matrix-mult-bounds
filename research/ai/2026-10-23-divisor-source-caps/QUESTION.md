# Sharp bounded-rank caps for divisor strips

October23,2026. Branch `research/divisor-source-caps-20261023`.
Base: PR129 at `9eca895e3618ad1f560e0565dc30134478e88da8`.

The A4 torus proof gives the sharp source-space cap8 below slice rank24.
This investigation generalizes that method across balanced source sizes;
it does not claim another A4 cutoff. The active A4 rank24, joint-rank,
conic and asymmetric-boundary questions retain their existing ownership.

Proposed all-size statement: let d be a proper positive divisor of a,
with p=a/d>=2. The maximum dimension of a linear subspace of A_a source
parameters whose every slice has rank at most a(a+d)-1 is exactly ad.
The same maximum holds throughout the interval

    a(a+d-1) <= rank ceiling < a(a+d).

Route: extend the rank-preserving torus and coordinate specialization.
At one middle extreme partition the a-by-a parameter grid into p-cycles
under simultaneous translation by(d,d). Any two coordinates of one cycle
give d^2 copies of a nonseparable two-monomial p-by-p biform, so their
sum has rank at least a^2+ad by the credited block-rank gap. At most one
coordinate per cycle remains. A d-row strip of dimension ad attains the
cap. Prove the residue decomposition, including wraparound and opposite
orientations, and export exact minors/scaling controls.

An active-ruling corollary may recover the credited A4 rank102 exclusion
and give a reusable all-size sufficient exclusion criterion. No new A4
cutoff, source target construction or exponent improvement is asserted.
