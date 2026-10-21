# Exact identity through order two

Finite exact polynomial certificate, unreviewed, October 21, 2026.
The construction is over Q and its identities hold after extension to C.
No complete degeneration or exponent improvement is asserted.

## First spaces

Use G,E_B,E_C and the 4096-term source convention from the first-extension
package. Each source leg has dimension 112. The leading tensor has twelve
independent first rows on A0={(i,s,z):i,s in {1,2},z in {0,3,6}}.
Let K be the other 100 coordinate covectors.

Each effective extension E/G has boundary dimension 12 and mixed dimension 4.
On B take all twelve boundary directions and the mixed rows

    e_(0,1,4)+e_(3,1,1),
    e_(0,1,5)+e_(3,1,2).

They form a common-kernel rank-one pencil in the concurrent worker's
2-by-2 mixed block. Its opposite pure-boundary annihilator has dimension 6.
The seed saves bases V_B,V_C with quotient dimensions 14,6 and

    (K,V_B,V_C)T=0.

The verifier checks this identity and both dimensions directly. The mixed
block interpretation and rank-sum boundary are credited to the concurrent
second-jet package, not claimed as new here.

## Polynomial maps and correction

For a=(a0,...,a15), the certificate specifies

    P(t,a)=P0+t P1(a)+t^2 P2(a),
    Q(t,a)=Q0+t Q1(a)+t^2 Q2(a),

with 18 and 10 active output rows. P0,Q0 have G in their first four rows
and zero elsewhere. The new rows of P1,Q1 are the fixed V_B,V_C bases;
the first four rows depend linearly on a in sixteen independent directions.
P2,Q2 are linear in a and supported only on new output rows. Their
coefficient lists contain 64 and 50 nonzero entries, respectively.

The first-leg matrices Y(a),Z(a), linear and quadratic in a, are supported
on row K and column A0. Set

    U(t,a)=I-t Y(a)-t^2 Z(a).

Every product of two matrices in that block is zero, so U has the exact
regular inverse I+tY+t^2Z. The accepted identity is

    pi_K U(t,a) (1,P(t,a),Q(t,a))T = O(t^3).             (1)

Here pi_K selects the 100 rows outside A0. Thus the first two corrected
partial spaces remain the leading space. Equation (1) is checked as a
polynomial in all sixteen parameters, including every quadratic monomial.

The constructor solves two rank-92 systems for the new second rows.
For the retained directions, the complete quadratic top-block residual
already lies in the leading twelve-row space. Its coordinates supply Z;
no top second derivative is needed. This accounts for P1 Q1, both second
derivatives, and the first-leg row correction.

## Acceptance and limits

The separate verifier checks 171 identities on the 100-by-18-by-10 output
universe: 3,078,000 coefficient cells. Complete source contraction and
complete monomial enumeration cover zero coefficients as well. This is
not a count of sampled parameter choices. Tests also reconstruct the
family from its seed and evaluate it in the original cyclic coordinates.

The active formats are smaller than the target's two 110-dimensional legs.
They can be padded with zero rows through order two, but later nonzero
coefficients and a suitable Laurent first-leg map have not been constructed.
No 100-dimensional matrix slice space is exhibited in the saturated limit.

At a0=1 and all other parameters zero, setting unlisted higher coefficients
to zero leaves a third corrected coefficient of first flattening rank 8.
The test retains this exact nonzero coefficient. It is not an obstruction
to adding higher derivatives, and it does not prove useful target growth.
Those higher equations are the next construction problem.
