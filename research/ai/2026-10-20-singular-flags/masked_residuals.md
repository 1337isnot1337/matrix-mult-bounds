# A masked residual can approach zero along a target stabilizer

AI-derived explanation and exact negative control, 2026-10-20. This is a
calibration result for numerical discovery, not a matrix-exponent claim.
The concurrent graded-route note already cautioned that its partial residuals
do not measure full scaled-tensor error. The argument here makes one source
of that problem explicit; no novelty is claimed for the elementary torus fact.

Let a diagonal weighting w preserve the wanted target T: every nonzero target
coefficient has weight zero. A common discovery objective measures only
coefficients of weight <=0, imposing the target at weight zero and zero at
negative weights. Coefficients of positive weight are unconstrained.

Suppose a constant tensor S already matches T at every weight-zero position.
Apply the same target diagonal action D(t), with t tending to infinity.
Every negative-weight error tends to zero, and the weight-zero entries remain
correct. The masked residual therefore tends to zero. Positive-weight errors
can diverge at the same time. This operation stays within the class of
constant trial matrices, because it rescales their target rows by constants
at every fixed t.

Consequently a sequence of tiny masked residuals does not, by itself, furnish
the polynomial family needed in the intended epsilon->0 direction. All
coefficient valuations and growth rates must be controlled. In particular,
the positive and negative directions cannot simply be interchanged.

## An exact control inside the convolution source family

Start with the saved C(2,3) to T_2 coordinate control. Its output row zero
uses source coordinates {0,3}. Add source coordinate 1 to that row, leaving
the other maps and weights unchanged. The resulting constant tensor S is an
ordinary restriction of C(2,3). It still has every weight-zero coefficient
correct. Its four unwanted terms have weights -3,1,1,4.

After D(t), direct exact coefficient calculation gives

    masked squared error = t^(-6),
    full squared error   = t^(-6)+2t^2+t^8.

The incomplete objective approaches zero while the full error diverges.
The original epsilon-weighted family still has a nonzero epsilon^(-3)
coefficient. `gauge_control.py` evaluates every coefficient with rational
arithmetic, rather than taking these two formulas as inputs.

## Fixing the diagonal freedom

For canonical T_m, the full positive diagonal stabilizer has logarithmic
weights

    wX(p)=gamma+beta*p,
    wY(u,a)=eta_u-beta*a,
    wZ(u,c)=-gamma-eta_u-beta*c.

The C(2,m-1) sector forces the shared arithmetic progression; every other
sector then supplies one eta_u. These m+2 parameters exhaust the diagonal
solutions. Exact linear-rank controls check that count at small m.

For real numerical trials with nonzero rows, one can fix this freedom by
normalizing the total shared-matrix norm, balancing its endpoint row norms,
and normalizing the norm of each Y sector. Any exact real solution can be
rescaled to meet these conditions. The later flag parametrization instead
uses nonzero pivot anchors, giving algebraic normalizations without adding
norm equations. Neither normalization alone makes a floating result exact.

In the retained run, a residual about 0.0005507 became about 1.9976 after
target-preserving balancing; desired entries changed by at most about
1.8e-13 from rounding. A balanced refinement reached about 0.00664, without
an exact witness. The earlier weight order is independently excluded by the
written flag obstruction, so further fitting in that chamber is unnecessary.
