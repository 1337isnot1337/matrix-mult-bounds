# Exact acceptance test for a fixed-seed target-stabilizer limit

October 21, 2026. The proposed experiment was to reduce the residual
of the full A(3,3)->M5 numerical map by a singular target stabilizer.
An invariant gives a decisive check before spending time on scaling.
For the saved seed the check fails exactly. The construction search
therefore continues by changing the source maps.

## Reshuffling into an operator

For a tensor T on three n-by-n matrix legs, define the n^3-by-n^3
operator

\[
\mathcal R(T)_{(i,j',k'),(i',j,k)}
=T_{(i,j),(j',k),(k',i')}.
\tag{1}
\]

The matrix multiplication tensor is sent to the identity operator.
Let the three target vertices be changed by P,Q,R. On coefficient
maps, the edge actions are P on the first index and Q inverse on
the second index of the first leg, and cyclically. Equation (1)
changes by

\[
\mathcal R(T)\longmapsto
(P\otimes Q\otimes R)\mathcal R(T)
(P\otimes Q\otimes R)^{-1}.
\tag{2}
\]

Thus every spectral invariant of the reshuffled operator is
unchanged by a target stabilizer, including when the three matrices
become unbounded along a limiting sequence.

For a fixed seed to approach M_n under (2), its residual operator
\(\mathcal R(T)-I\) must be nilpotent. This is a necessary condition,
not a sufficient one: local similarities are a smaller group than
all similarities.

## Allowing an overall scalar normalization

Write O=R(T) and N=n^3. Even if the seed may also be multiplied by
a scalar, a necessary condition is

\[
\boxed{\quad N\operatorname{tr}(O^2)
-\operatorname{tr}(O)^2=0.\quad}
\tag{3}
\]

Indeed, if a sequence of scalar multiples of matrices similar to O
converges to I_N, its trace forces the scalars to converge to
N/tr(O), with tr(O) nonzero. The trace of the square then forces (3).
Equivalently, after this trace normalization, (3) states that the
residual has zero trace of its square. Higher powers would also have
to vanish, but a nonzero value in (3) already rejects the seed.

## Exact certificate for the saved A33 seed

Four full complex ALS runs, initialized by the three-quotient
construction and then allowed to leave that family, reached a best
full relative residual 0.16994800681886255. This is a numerical
discovery result, not a tensor identity. The original coefficient
file is

`results/anisotropic-constructions-2026-10-20/parity_balancing_three_quotients_a33_als_complex/best.npz`.

The exact certificate interprets each stored real and imaginary
binary64 component as its dyadic rational value. It reduces those
numbers into F_p[i], with p=65519 and i^2=-1, and recomputes the full
729-term source contraction with integer arithmetic. This prime is
3 modulo4, so the indicated quadratic extension is a field. All
dyadic denominators are invertible. A nonzero reduction of (3)
therefore proves that the rational-complex value of (3) is nonzero.

The separate exact A23->M4 control is also passed through this
contraction and reshuffling: its operator is exactly I_64 modulo the
same prime. The script checks integer accumulation bounds before
using int64 matrix multiplication. No floating point multiplication
is used in the finite-field contraction.

Consequently the stored seed, with arbitrary overall scalar
normalization, cannot be converted to M5 solely through its target
GL5^3 stabilizer. This conclusion applies to those fixed dyadic maps.
It does not exclude changing their coefficients, using a different
seed, or any general degeneration from A33.

`parity_balancing_stabilizer.py` saves the input SHA-256, prime,
exact reduced traces, and nonzero polynomial value in
`results/anisotropic-constructions-2026-10-20/parity_balancing_stabilizer_a33_seed.json`.

## Dependency-free replay

The best seed alone is exported in
`parity_balancing_stabilizer_a33_seed_coordinates.json`, in the same
results directory. Each real and imaginary coordinate is represented
by its exact `float.hex` value. The file records both the original NPZ
SHA-256 and the SHA-256 of the canonical coordinate payload.

`parity_balancing_stabilizer_verify.py` requires only the Python
standard library. It converts each hexadecimal dyadic to a numerator
and denominator, reduces it modulo 65519, and recomputes all 729
source terms and all 15625 entries of the reshuffled operator using
Python integers. It separately recomputes the entire A23->M4 positive
control. The results agree with the initial array-based checker:

\[
\operatorname{tr}O=(18547,23372),\qquad
\operatorname{tr}(O^2)=(41652,28362),\qquad
125\operatorname{tr}(O^2)-(\operatorname{tr}O)^2=(32521,59183).
\]

The ordered pairs denote coefficients of 1 and i in F_65519[i].
The standard-library replay is saved in
`parity_balancing_stabilizer_a33_stdlib_replay.json`. Run it with
site packages disabled:

```
python -S research/ai/2026-10-20-anisotropic-constructions/parity_balancing_stabilizer_verify.py
```

The three focused tests replay the full seed and positive control,
reject a changed map even after its payload hash is recomputed, and
reject an altered coordinate hash. The optional `--npz` argument
checks the original NPZ file hash without loading any arrays.

Review status: the similarity argument, trace-normalized invariant,
and initial finite-field implementation were checked by a second
agent in this generating session. The subsequent standard-library
replay agrees with that implementation. No external independent
review or formalization is claimed.
