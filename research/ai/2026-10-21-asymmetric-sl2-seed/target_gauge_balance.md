# Target-vertex balancing for numerical Laurent searches

October 21, 2026. Numerical conditioning only; no exact certificate.

For target coordinates A_(i,j), B_(j,k), C_(k,i), applying G to one
occurrence of a vertex and G^(-transpose) to its other occurrence
preserves the matrix-multiplication tensor. The implementation checks
this identity numerically for the accumulated three leg gauges and
checks that the saved coefficient maps equal the gauged inputs.

For the two coefficient Gram matrices Q and R (the second is transposed
because its action is contragredient), minimizing the sum of squared
coefficient norms reduces to minimizing

    trace(Q X) + trace(R X^(-1)),  X=G G^* positive definite.

The stationary solution satisfies X Q X=R, giving
X=Q^(-1/2) (Q^(1/2) R Q^(1/2))^(1/2) Q^(-1/2).
The script cycles through the three vertices. Small spectral floors are
numerical safeguards; each step checks that the actual norm did not
increase. This is standard matrix balancing, not a new tensor identity.

For the saved degree-two checkpoint, the coefficient norm decreases
from149.3781744725804 to135.28667938936178. The accumulated target
invariance error is about1.93e-15. The leg gauge condition numbers are
about4.22,3.06,2.87. These values do not establish convergence or a new
bound. Nonunitary gauges change the residual norm, so residual values
from different gauges must not be treated as directly comparable progress.

The Laurent solver now accepts --padding-noise. The first degree-three
balanced restart used the former1e-4 padding and was interrupted after
it substantially perturbed the initial residual. A new restart uses zero
padding, preserving the prior polynomial maps before optimization while
opening the extra Laurent coefficient directions. Both remain numerical
searches. The original unbalanced continuation is kept separately.
