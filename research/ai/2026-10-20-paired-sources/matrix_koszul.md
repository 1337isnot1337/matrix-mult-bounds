# Matrix multiplication Koszul kernels from a Casimir calculation

Written local derivation over C, unreviewed, October 20, 2026. No exponent
improvement or historical priority is claimed. The Cauchy and Pieri rules
are standard imported representation theory. The kernel modules below
already appear as a proved inclusion in Landsberg--Ottaviani,
[New Lower Bounds for the Border Rank of Matrix Multiplication](https://theoryofcomputing.org/articles/v011a011/v011a011.pdf),
Theory of Computing 11(11), 2015, Lemma 4.2. Their Remark 4.3 anticipates
equality. The argument here computes the positive operator directly; it
does not assert that equality has remained open in subsequent literature.

Let U=C^l, V=C^r, A=U tensor V. Remove the independent b-dimensional
middle-index factor from M(l,b,r). Its Koszul map is

    delta: exterior^p(A) tensor U
              -> exterior^(p+1)(A) tensor V*,
    delta(w tensor u_i)=sum_j (u_i tensor v_j) wedge w tensor v_j*.

Equip the standard exterior bases with their usual orthonormal products.
Write e_(i,j)=u_i tensor v_j and let iota_(i,j) be contraction. The
creation-annihilation identity gives

    delta* delta = r I-T,
    T=sum_(i,k,j) (e_(i,j) wedge iota_(k,j)) tensor E_(k,i).

The first operator in parentheses is the gl(U) action rho(E_(i,k)) on
exterior^p(A). Thus T=sum_(i,k) rho(E_(i,k)) tensor E_(k,i), the tensor
Casimir coupling the exterior factor and the auxiliary U.

The exterior Cauchy rule and the one-box Pieri rule give the decomposition

    exterior^p(U tensor V) tensor U
      = direct_sum_(lambda,mu) S_mu(U) tensor S_(lambda')(V),

where lambda has p boxes and fits in the l-by-r rectangle, and mu is
obtained by adding one box to lambda, still with at most l rows. These
rules and notation are reviewed in Appendix A of the cited primary paper.
Different lambda have different V modules, and each one-box summand is
multiplicity one for a fixed lambda.

For completeness the quadratic Casimir sum_(i,k) E_(i,k)E_(k,i) acts
on S_lambda(U) by

    c(lambda)=sum_i lambda_i*(lambda_i+l+1-2i).

Apply it to a highest-weight vector: the diagonal terms give sum lambda_i^2,
and each raising/lowering pair contributes lambda_i-lambda_j for i<j.
This gives the displayed scalar. The coproduct of the Casimir is the sum
of the two individual Casimirs plus 2T. On the summand corresponding to a
box added in row i, T therefore has eigenvalue

    [c(mu)-c(lambda)-l]/2=lambda_i+1-i,

the content of the added box. Since lambda has at most r columns, this
content is at most r. It equals r exactly for a box added to the first
row when lambda_1=r. Every other eigenvalue of rI-T is positive. Positivity
of delta*delta now proves that the entire kernel, not just a submodule, is

    direct_sum_(lambda_1=r)
        S_(r+1,lambda_2,...) U tensor S_(lambda') V.

Restore the b independent middle indices. The exact rank is

    rank K_p(M(l,b,r))
      = b * [l binom(lr,p)
             -sum_(lambda_1=r) dim S_(r+1,lambda_2,...) C^l
                                  *dim S_(lambda') C^r].

All partitions in the sum fit the l-by-r rectangle and have size p. The
dimensions are evaluated by the exact Weyl product. If p<r the sum is
empty, recovering the injectivity argument used in the first checkpoint.

This proof uses complete reducibility and a positive Hermitian inner
product over C. The separate proof in [matrix_euler.md](matrix_euler.md)
now gives a shorter alternating formula and proves the same ranks over
every field. That stronger field statement follows from its cohomological
argument, not from the characteristic-zero representation theory here.
