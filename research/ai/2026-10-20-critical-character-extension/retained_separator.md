# Retaining the convolution separator does not strengthen the power sum

October 20, 2026. Written deduction from an external construction. No new
degeneration or exponent improvement is claimed.

Let A be a sum of M matched blocks A_h with their first input shared.
Write v_h=lambda(A_h), and lambda(B_X(n))=n^p for 0<=p<=1.
The proof of Houxi Lü, *Polynomial Separation of a Shared Tensor Leg and
Matrix Multiplication in Arbitrary Characteristic*, arXiv:2610.18914v1,
Proposition 2.1, explicitly factors its construction through

    A tensor C(M,n)  degenerates to  direct_sum_h (A_h tensor B_X(n)).

This intermediate construction is already in the external proof, before
the auxiliary convolution is replaced by its rank M+n-1. Over an infinite
field, character monotonicity therefore gives

    lambda(A) lambda(C(M,n)) >= n^p sum_h v_h.           (1)

It is tempting to retain the exact convolution character in (1) in the
hope of improving the existing matched-sector power-sum bound. The
following control shows that this lower-bound method is always redundant.

Apply the same external construction to A=B_X(M), viewed as M scalar
blocks sharing a one-dimensional first space. Since lambda(A)=M^p and
every block has value one, it proves

    lambda(C(M,n)) >= M^(1-p) n^p.                     (2)

Thus the right side of (1), after dividing by its auxiliary value, is at
most M^(p-1) sum_h v_h. But, for 0<p<=1, the already established matched
power-sum inequality says

    lambda(A) >= (sum_h v_h^(1/p))^p
              >= M^(p-1) sum_h v_h.                   (3)

The last inequality is the power-mean inequality, or Jensen applied to
the convex function x^(1/p). Hence (3) is at least as strong as (1) for
every possible actual value of lambda(C(M,n)). This conclusion holds at
every finite M,n and for unequal block values as well as equal ones.

When p=0, the existing lower bound is max_h v_h. Equation (2) gives
lambda(C(M,n))>=M, so (1) gives at most the arithmetic mean of the v_h,
which is again weaker. The p=1 case is included in (3).

This argument excludes only the proposed use of this separator as a
stronger lower bound on lambda(A). It does not exclude exploiting a new
tensor identity, a stronger upper bound for a coupled source, or a
different auxiliary tensor. No numerical optimization is needed here.

Sources: [Lü v1](https://arxiv.org/html/2610.18914v1), Proposition 2.1 and
its displayed maps; [Uznański v2](https://arxiv.org/html/2610.10494v2),
Lemma 3.3 for the power-sum formulation. Both are external results.
