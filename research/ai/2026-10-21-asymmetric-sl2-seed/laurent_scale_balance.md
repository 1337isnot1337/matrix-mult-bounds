# Remove Laurent-variable scaling from the numerical objective

October 21, 2026. Numerical search correction, not an exact construction.

If each coefficient map is M(t)=sum_h M_h t^h, replacing t by c*t sends
M_h to c^h M_h. The resulting tensor coefficient N_k is multiplied by
c^k. The constant coefficient is unchanged. Therefore a raw joint norm
of the positive coefficient errors is scale-dependent: shrinking c can
suppress positive-power errors while enlarging negative-power maps.
Small raw residuals alone are especially inadequate evidence of a Laurent
identity. Historical results remain labeled numerical and are not rewritten.

For positive c=exp(s), minimize the combined squared coefficient norm

    Q(s)=sum_h q_h exp(2h*s),  q_h=sum_legs ||M_h||_F^2.

With nonzero coefficients of both signs this is strictly convex, tends
to infinity in both directions, and has a unique minimum satisfying
sum_h h*q_h*exp(2h*s)=0. The script finds this scalar minimum by bisection.
Its differential is

    ds = -sum_h h*exp(2h*s)*Re< M_h, dM_h >
             / sum_h h^2*q_h*exp(2h*s).

The solver's optional --balance-laurent-scale objective evaluates the
constant and positive tensor coefficients after this normalization.
Under another raw scale change by kappa, the balancing scale changes
from c to c/kappa; hence the normalized objective is invariant under
that scaling freedom. Saved best maps are the normalized maps themselves,
so the reported error corresponds to the saved coefficient convention.

The Jacobian includes both the ordinary coefficient derivative, weighted
by c^k, and the rank-one correction k*c^k*N_k*ds. Its adjoint includes
the matching term. Two unit tests check the scalar derivative, invariance
of the normalized maps, and the unchanged scalar constant coefficient.
A one-evaluation solver smoke run passes the adjoint assertion and has
Richardson directional error about1.10e-8. It is a derivative check, not
an optimization result.

A snapshot of the preceding degree-three run has coefficient norm143.718.
Variable balancing uses c about2.93 and reduces it to77.394. Its normalized
joint residual is about5.95e-4, rather than the much smaller unnormalized
value. This change is a convention/conditioning effect, not a new failure
or improvement of the polynomial identities. The constant error is unchanged.
The normalized input checkpoint and reports are retained for replay.

This fixes only one gauge freedom. It does not prove boundedness of all
future iterates, convergence, exactness, or a smaller matrix multiplication
exponent. A genuine result still needs exact coefficient identities and
the full target-to-exponent implication.

A subsequent attempt with the smaller preconditioner floor1e-12 failed
the unchanged directional-derivative gate (minimum error1.127e-7 against
a required1e-7) and stopped before optimization. The retry uses the
smoke-tested1e-10 floor and must pass the same gate. This failed attempt
is retained as a validation result, not counted as optimization progress.
