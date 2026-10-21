# The capacity bound permits arbitrary Laurent output maps

AI-derived written extension, 2026-10-20; unreviewed. No smaller matrix
exponent is established. This strengthens the scope of
[asymptotic_capacity.md](asymptotic_capacity.md) without changing its constant.

For unbounded m, arbitrary positive integers k_m and N=m(m+1)/2, suppose
C(A_m,B_m) degenerates to canonical T_(m,k_m). On each of the two inputs,
require every target coordinate to select one distinct source coordinate,
multiplied by an arbitrary nonzero Laurent scalar. Allow an arbitrary
Laurent matrix on the output. If limsup A_m/m<=5/4, then

    liminf B_m/(k_m N) >= 3/2-sqrt(3)/4.                (1)

Thus an arbitrary Laurent output map does not rescue the monomial-input
class. At least one input needs actual linear mixing to escape this result.
This is not a proof that arbitrary tensor degenerations are obstructed.

## 1. Disjointness uses valuations, not output-row weights

Write x_p and y_i for the source indices of target inputs p and i, and a_p,
b_i for their Laurent scalars. Set w_p=val(a_p), v_i=val(b_i). Let C_(z,t)
be the Laurent entry mapping source output t to target output z. Every target
input pair receives exactly one source contribution, at t=x_p+y_i. Its
coefficient is

    a_p b_i C_(z,x_p+y_i).                              (2)

There is no summation or cancellation in (2). Every desired coefficient has
valuation zero and nonzero leading coefficient. Every nonzero undesired
coefficient must have strictly positive valuation.

For each target output row z let S_z be the set of source indices used by
its desired input pairs. Suppose t belongs to S_z and S_z' with z!=z'. Take
desired pairs with input valuation sums g and g'. If n=val(C_(z,t)) and
n'=val(C_(z',t)), then g+n=g'+n'=0. The two crossed outputs are undesired
because each target input pair has only one desired output. Equation (2)
forces g+n'>0 and g'+n>0. These assert both g>g' and g'>g, a contradiction.
The active sets remain disjoint, so

    E=sum_z(|S_z|-1) <= A+B-1-kN.                       (3)

For desired pairs in the same row using the same source index, their input
valuation sums must be equal, since they use the same output entry.

## 2. Record index and weight differences together

For target sector u, with input coordinate a and output coordinate c, a
singleton active set implies both

    x_(a+c)+y_(u,a) = a constant in a,
    w_(a+c)+v_(u,a) = a constant in a.

Introduce the word of ordered pairs

    d_p=(x_(p+1)-x_p, w_(p+1)-w_p),  0<=p<m-1.

A singleton output row forces its length-(u-1) window in this joint word to
be the fixed negative differences of (y_(u,a),v_(u,a)). The repetition bound
therefore applies to this joint word, not only its index component:

    E >= k R(d).

If L is the longest constant run of d, the same nonadjacent-window argument
gives R(d)>=floor((m-1-L)^2/4). Consequently there is a common interval of
ell=L+1 shared target coordinates on which **both** x_p and w_p are
arithmetic, and

    ell > m-2sqrt(E/k+1).                               (4)

Using a separate run for each component would lose this conclusion; the
joint-word condition is essential.

## 3. The projected flattening still applies

Assume for contradiction B/(kN)<=rho<3/2-sqrt(3)/4 along a subsequence.
Equations (3)-(4) give liminf ell/m>=1-sqrt(2(rho-1))>5/8. Since all x_p
lie in [0,A-1] and limsup A/m<=5/4, its nonzero integer step on this interval
must eventually be +1 or -1, exactly as in the earlier quantitative proof.
The weight step is arbitrary, including zero.

Write a_p=epsilon^(w_p) u_p(epsilon), with u_p regular and u_p(0)!=0. Apply
diag(u_p^(-1)) to the projected first leg. This is regular and invertible
at zero. The limiting target is rescaled there by nonzero constants. On
the common interval, the remaining first map is an arithmetic diagonal
weight on a consecutive source interval, hence a polynomial-variable
scaling of C(ell,B). Its structured flattening has rank B+q. Arbitrary
Laurent maps on the other two legs cannot increase this rank at their
tensor limit.

The projected target still has rank at least

    k*((ell+p0)*(m-p0)-[h(h+1)+q(q+1)]/2),
    h=ell-1-q.

The constant first-leg rescaling changes only nonzero entries inside the
disjoint matrix groups. Each such group retains rank at least one. Choose
q=floor((ell-1)/2), obtaining

    B >= k*(ell*m-floor(ell^2/4))-floor((ell-1)/2).

The limiting scalar calculation is unchanged and proves (1). Thus the
stronger scope does not require global arithmetic shared weights or a common
parameter weight on all entries of an output row.

## Exact control and limits

The saved m=3 control has input X weights (0,0,4). One output row is
`source_Z_4 + epsilon^(-4) source_Z_7`. Its shared weights are nonarithmetic
and its two output-entry valuations differ. Direct coefficient replay checks
all 108 coefficients, giving T_3. This is an extended-model control, not a
new existence result: T_3 already had other verified constructions.

If an input row mixes several source coordinates, equation (2) becomes a sum;
cancellation can invalidate both the disjointness and joint-word steps.
The extension deliberately leaves that problem open. It also retains the
canonical target identifications and the stated relative short-input bound.
