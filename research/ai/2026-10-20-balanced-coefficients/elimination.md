# An exact monic coefficient system at the balanced order

AI-derived argument, written and unreviewed, October 20, 2026. No finite
degeneration or exponent improvement has been proved. This note gives an
exact algebraic construction problem, with fewer variables and a proposed
acceptance certificate.

Use the polynomial flags of ../2026-10-20-singular-flags/normal_form.md at
m=4, B=10, beta=100, eta=(0,201,403,607). Impose the additional restriction
that every leading/pivot coefficient is one. This is an ansatz, not a
lossless reduction of arbitrary constant matrices. The source translation
anchor fixes G_2=t, G_3=1. There are 125 remaining complex coefficients.

## Coefficients grouped by degree

Let r_y and r_z be the increasing weight ranks on Y and Z. Put
d_p=3-p, e_y=9-r_y. Reverse the coefficients of G_p and P_y, and list the
functional Q_z from its first nonzero monomial onward:

    A_p(s)=sum_i a_(p,i) s^i,
    B_y(s)=sum_j b_(y,j) s^j,
    C_z(s)=sum_k c_(z,k) s^k.

Each constant coefficient is one. Direct polynomial multiplication gives

    Q_z(G_p P_y) = [s^delta] A_p(s) B_y(s) C_z(s),
    delta=d_p+e_y-r_z.

There are exactly 121 entries of nonpositive parameter weight. Their
distances delta range from 3 to 12, and all twenty wanted terms occur among
them. The equations set the wanted entries to one and the other entries to
zero. Every other tensor coefficient has positive weight, so an exact
solution of these 121 equations gives the required limit in this ansatz.

At distance delta, new unknowns occur linearly: a term containing one
distance-delta coefficient has two constant coefficients equal to one.
Every other term uses only smaller distances. Thus the new linear matrix
has constant integer entries independent of all parameters. Selecting
independent rows and pivot columns gives the following elimination:

| Distance | New unknowns | Equations | Eliminated | Free | Conditions |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 21 | 0 | 0 | 21 | 0 |
| 2 | 20 | 0 | 0 | 20 | 0 |
| 3 | 18 | 6 | 5 | 13 | 1 |
| 4 | 15 | 16 | 12 | 3 | 4 |
| 5 | 13 | 25 | 13 | 0 | 12 |
| 6 | 11 | 22 | 11 | 0 | 11 |
| 7 | 9 | 18 | 9 | 0 | 9 |
| 8 | 7 | 14 | 7 | 0 | 7 |
| 9 | 5 | 10 | 5 | 0 | 5 |
| 10 | 3 | 6 | 3 | 0 | 3 |
| 11 | 2 | 3 | 2 | 0 | 1 |
| 12 | 1 | 1 | 1 | 0 | 0 |

The selected pivot matrices have integer inverses, checked exactly. Their
determinants are therefore units in Z. Recursively solving the 68 pivot
coefficients gives integer polynomials in 57 free parameters. The remaining
53 equations are integer polynomials of degree at most 12. For the degree
bound, give a free distance-j parameter weight j. A solved distance-j
coefficient has weighted degree at most j, by induction on the product
formula; constants on wanted equations do not increase that bound.

This proves equivalence, within the monic ansatz, to the vanishing of those
53 polynomials. It is valid over any field, since the only inverses used
are integer units. `coefficient_system.py` retains the recurrences rather
than expanding their potentially large polynomials. Exact controls compare
every constraint with a separate polynomial multiplication routine, and
recover arbitrary monic maps when fed their actual coefficients. These
controls validate the parametrization; they do not exhibit a T_4 solution.

## A finite certificate that would establish complex existence

The original 121 equations define an integer polynomial map F in 125
variables. Suppose a prime p and a point v over F_p satisfy F(v)=0 and
the 121-by-125 Jacobian has row rank 121. Select 121 columns with nonzero
minor and fix the other four variables at integer representatives. The
square system then has residual divisible by p and Jacobian determinant a
p-adic unit. Multivariable Hensel's lemma gives a solution over Z_p.

The imported lifting theorem is Keith Conrad,
[A multivariable Hensel's lemma](https://kconrad.math.uconn.edu/blurbs/gradnumthy/multivarhensel.pdf),
Theorems 3.3 and 3.8, accessed October 20, 2026. Its hypotheses here are
polynomials over the complete valuation ring Z_p, residual norm less than
one, and determinant norm one after the square subsystem is selected.

This also implies a solution over the algebraic closure of Q: evaluation at
the p-adic point makes the equation ideal proper over Q. If it contained
one after extending to an algebraically closed field of characteristic
zero, the finite linear identity witnessing that fact could be solved over
Q already, a contradiction. The weak Nullstellensatz then supplies an
algebraic point. Since all pivots were fixed at one, no open rank conditions
are lost. The resulting complex matrices would give an exact degeneration.

The finite certificate would consist of the residue-field coefficients,
all 121 exact coefficient checks, and a nonzero Jacobian minor. No such
certificate is currently available. A solver's UNSAT answer without a
checked trace is not promoted to a mathematical nonexistence proof.
A failure over one finite field also does not exclude complex solutions.
The same sufficient certificate can use F4: take the complete valuation
ring Z_2[zeta] with zeta^2+zeta+1=0. Its residue field is F4, and an
invertible residue-field minor is a unit determinant. Apply the same
lifting theorem there. The verifier represents residue-field elements by
their two coefficients in the basis 1,zeta. This extension changes the
certificate's residue field; it does not remove the rank requirement.

Finally, even a size-four construction would not by itself beat 9/4.
Replication into sources with increasing B, or a different complete growth
implication, would still be required. That step remains an open question.
