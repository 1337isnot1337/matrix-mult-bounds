# Exact marginal feasibility for the shifted parity source

October 21, 2026. This is an AI-derived support calculation and a written
consequence of the Tao--Sawin antichain theorem. Its tightness, interpolation,
entropy-duality and score-cover arguments were checked by a second agent
in this generating session; there is no external independent review or
formalization. That check did not re-prove the external antichain theorem
or replay the exact certificates. **No matrix multiplication restriction
or exponent improvement is established.**

The subsequent [pairwise-annihilator argument](parity_annihilator.md) excludes
the one-copy target M(14) direct sum M(4), despite the sharp support
entropy value proved here. The balancing theorem remains valid. It
illustrates a strict separation between this entropy screen and actual
matrix multiplication degenerations.

## Result and construction relevance

Let S be the `parity110` degeneration of A(5,5) defined in
[`singular_support.py`](singular_support.py). There is a strictly positive
probability distribution on every one of its 11,725 support entries whose
coordinate marginals are

\[
q_X(x)=\frac{z^{\rho_X(x)}}{112+113z},\quad
q_Y(y)=\frac{z^{\rho_Y(y)}}{112+113z},\quad
q_Z(z')=\frac{z^{\rho_Z(z')}}{113+112z},                 \tag{1}
\]

where rho is the shifted parity and the positive scalar z is the positive
root of

\[
113z^2-112z-226=0.
\]

The scalar is about 1.9941061017702744. Thus the elementary parity capacity
bound is feasible on the actual source support. It is not invalidated by
an additional support constraint inside the parity blocks.

Strict feasibility also implies that positive diagonal coordinate scalings
of S attain the marginals in (1) as squared-coefficient marginals. A saved
floating approximation provides such a scaling to approximately 1.1e-16
absolute marginal error. This is a numerical preconditioner, not a
restriction to the excluded M(14) direct sum M(4) target.

Write H=S tensor S^cyclic tensor S^(cyclic squared). The exact consequence is

\[
\lim_{n\to\infty}\operatorname{sr}(H^{\otimes n})^{1/n}
=\frac{(112+113z)^2(113+112z)}{z^2}.                   \tag{2}
\]

The cube root of the right side is about 212.7162573664768. Therefore this
asymptotic slice-rank screen alone does not exclude a target with leg
dimension 212. The separate annihilator argument does exclude it.

## Support, parity, and reflection reduction

Use the coordinates

\[
X=(i,p+q,s),\quad Y=(j,p,r+s),\quad Z=(i+j,q,r),
\]

with all six input indices from 0 through 4. The original weights are

\[
w_X=p+q-i-s,\quad w_Y=r+s-j-p,\quad w_Z=i+j-q-r.
\]

They sum to zero. Set rho=(w_X+1,w_Y+1,w_Z) modulo 2, and keep exactly
the terms with rho_X+rho_Y+rho_Z=2. Equivalently, delete original parity
pattern 110. There are 225 coordinates on each leg. Shifted even and odd
class dimensions are respectively

\[
(e_X,e_Y,e_Z)=(112,112,113),\qquad
(o_X,o_Y,o_Z)=(113,113,112).
\]

Three commuting symmetries reverse the input pairs (i,j), (p,q), and
(r,s), replacing both entries of the chosen pair by their complement to 4.
The support and all shifted parities are preserved. The resulting group
has 1,650 support orbits and 45 coordinate orbits on each leg. A uniform
distribution inside each support orbit has uniform marginals inside each
of its coordinate orbits.

This quotient is used only for discovery. The exact verifier expands the
support orbits and checks every one of the 675 original coordinate
marginal equations.

## Two exact certificates and interpolation

For a rational parameter p, prescribe shifted odd class masses

\[
(p_X,p_Y,p_Z)=(p,p,2-2p)
\]

and require uniform coordinate mass inside each class. Two saved
certificates use p=2/3 and p=67/100:

| Parameter | Support orbits | Positive residual orbit masses | Original marginal equations |
| --- | ---: | ---: | ---: |
| 2/3 | 1,650 | 132 | 675 |
| 67/100 | 1,650 | 132 | 675 |

Each certificate assigns a base mass 1/10^10 to **every** retained support
term. It then adds each listed rational orbit mass, divided uniformly
among the terms in that orbit. Every residual mass is positive, all
equations hold as identities of rational numbers, and total mass is one.

The files are

- [`parity_balancing_p_2_3.json`](../../../results/anisotropic-constructions-2026-10-20/parity_balancing_p_2_3.json)
- [`parity_balancing_p_67_100.json`](../../../results/anisotropic-constructions-2026-10-20/parity_balancing_p_67_100.json)

The common X and Y odd mass in (1) is

\[
p_* = \frac{113z}{112+113z}
     \simeq0.667984835545348.
\]

Eliminating z gives

\[
f(p_*)=0,\qquad f(p)=225p^2-19266p+12769.
\]

The polynomial is strictly decreasing throughout [2/3,67/100], and

\[
f(2/3)=25,\qquad f(67/100)=-15287/400.
\]

Thus p_* is strictly between the certificate parameters. Interpolating
their distributions with the same convex coefficient as their parameters
gives an exact distribution with the desired algebraic marginals. Every
term still has mass at least 1/10^10. The Z odd mass is 2-2p_*; the
stationary equation for z makes this exactly 112z/(113+112z).

The distributions are explicit algebraic support witnesses. Their square
roots need not themselves factor as three coordinate scalings. The next
argument establishes the existence of a factored witness separately.

## Why a positive diagonal scaling exists

Consider the compact set of support distributions with the prescribed
marginals (1), and maximize Shannon entropy on this set. Strict
feasibility implies that the maximizer has no zero entry: mixing a
distribution with a zero entry toward a strictly positive feasible point
increases entropy for a sufficiently small positive mixing parameter.
The positive contribution at a newly filled entry has order minus
epsilon log epsilon and dominates the finite first-order changes at
already positive entries.

At this interior maximum, the entropy gradient annihilates the kernel of
the linear marginal map. It therefore lies in that map's row space,
even though some marginal equations are redundant. Consequently, there
are real coordinate multipliers lambda_X, lambda_Y, and lambda_Z with

\[
P(x,y,z')=\exp(\lambda_X(x)+\lambda_Y(y)+\lambda_Z(z'))
\]

on the support; an additive constant is absorbed into the multipliers.
Multiplying the three tensor coordinate bases by exp(lambda_i/2) gives
squared coefficients P. All scalings are positive and invertible.

Any two source legs determine the third on this support. Therefore the
reduced Gram matrices have zero off-diagonal entries, and their diagonal
entries are precisely these marginals. This observation is useful for
numerical conditioning. Equation (2) below needs only the support
distribution, not the diagonal-scaling argument.

## Sharpness of the cyclic slice-rank screen

First, the source support is an antichain after ordering each leg by its
following integer coordinate weight:

\[
u_X(i,k,s)=-i+9k-81s,\quad
u_Y(j,p,l)=-j-9p+81l,\quad
u_Z(h,q,r)=h-9q-81r.                                  \tag{3}
\]

Each weight is injective on its 225 coordinates. For example, equality
of two X weights, first modulo 9 and then after division by 9, forces
the three indices to agree. The input ranges are shorter than the base
9. The same argument applies on Y and Z. On every support term the
sum in (3) is zero, by h=i+j, k=p+q and l=r+s. Two different support
terms therefore cannot be weakly increasing on all three legs.

The cyclic product H is also tight and hence an antichain: combine the
three independent-copy weights in a sufficiently large integer base.
All its support coefficients are nonzero. Tao and Sawin's Proposition 6
then identifies its asymptotic slice rank with the exponential of the
maximum, over support distributions, of the minimum of the three
marginal entropies. Its assumptions are satisfied here over C.

Let h_i be the entropy of (1). The product of the exact support
distribution with its two cyclic permutations is supported on H. Each
of H's three marginals has entropy h_X+h_Y+h_Z. Also,

\[
h_i=\log(e_i+o_i z)-p_i\log z,\qquad
p_X+p_Y+p_Z=2.
\]

This proves the lower bound in (2).

For completeness, the upper bound has an elementary slice cover. Give
each source coordinate score z^rho. The product of the three scores is
K=z^2 on every support term. The partition sums are
Z_X=Z_Y=112+113z and Z_Z=113+112z. In H each leg has partition sum
Z_X Z_Y Z_Z, while the product of all three leg scores is K^3.
In H tensor-powered n times, some coordinate in every support term has
score at least K^n. Each leg has at most (Z_X Z_Y Z_Z/K)^n such
coordinates, by summing their positive scores. They form a slice cover,
so

\[
\operatorname{sr}(H^{\otimes n})
\le3\left(\frac{Z_X Z_Y Z_Z}{K}\right)^n.
\]

Taking nth roots proves the matching upper bound. Optimizing the right
side over z gives 113z^2-112z-226=0: the logarithmic derivative is zero
exactly when the three shifted odd probabilities sum to two.

The target leg dimension 212 passes this screen by an integer comparison
alone. At p=2/3 the sum of marginal entropies exponentiates to
(27/4) 112^(4/3) 113^(5/3). Its cube exceeds 212^9 because

\[
19683\cdot112^4\cdot113^5
=57063131430009387024384
>55360846528600214601728
=64\cdot212^9.
\]

## Saved numerical preconditioner

The NPZ file
[`parity_balancing_preconditioner.npz`](../../../results/anisotropic-constructions-2026-10-20/parity_balancing_preconditioner.npz)
contains:

- `points`: the 11,725 support triples in i,j,p,q,r,s loop order, matching
  `singular_support.source_terms(5,5)` filtered to parity110;
- `masses` and `coefficients=sqrt(masses)`;
- `log_probability_factors`, a 3 by 225 array, with each mass equal to
  exp of the sum of its three coordinate entries, to floating precision;
- `A`, `B`, and `C`: exp of half those log factors, so
  A[x] B[y] C[z] reconstructs the stored coefficient;
- the original unnormalized iterative logs and the combined diagonal
  multiplier array.

Starting from uniform support mass, iterative proportional fitting took
200 full sweeps. The largest coordinate marginal residual was
1.033e-16; the least support mass was approximately 5.253e-9. The
three-factor coefficient reconstruction residual was below 4.7e-16.
These are floating discovery diagnostics. The existence and entropy
statements rest on the exact endpoint certificates and the arguments
above.

## Reproduction and scope

The exact replay uses only the Python standard library:

```sh
python research/ai/2026-10-20-anisotropic-constructions/parity_balancing.py --verify results/anisotropic-constructions-2026-10-20/parity_balancing_p_2_3.json
python research/ai/2026-10-20-anisotropic-constructions/parity_balancing.py --verify results/anisotropic-constructions-2026-10-20/parity_balancing_p_67_100.json
python -m unittest discover -s tests -p test_parity_balancing.py -v
```

Discovery uses NumPy, SciPy linear programming and SymPy exact linear
solving. Run the script with `--discover --p 2/3` or `--discover --p 67/100`.
The solver only selects a candidate support basis. The program then
solves the full marginal equations exactly, rejects negative values,
and runs the separate expansion verifier. Numerical preconditioning
uses `--ipfp --arrays PATH --output PATH`.

All five focused tests passed. They replay the two exact endpoint
certificates, check the root bracket and injective tight weights, and
reject a changed mass, a duplicated orbit, and a negative base mass.
The [verification report](../../../results/anisotropic-constructions-2026-10-20/parity_balancing_verification.json)
records both certificate hashes, all 1,350 marginal equations, the
11,725 tight-weight identities, and the exact integer comparison.

The exact checks establish support feasibility and the stated sharp
asymptotic slice-rank screen. They do not construct M(14) direct sum
M(4), do not give a general tensor-restriction criterion, and do not
improve the matrix multiplication exponent.

## External dependency

Terence Tao and Will Sawin, [*Notes on the “slice rank” of tensors*](https://terrytao.wordpress.com/2016/08/24/notes-on-the-slice-rank-of-tensors/),
August 24, 2016, Proposition 6, accessed October 21, 2026. The lower-bound
use requires nonzero support coefficients and an antichain under
coordinate total orders; both are verified above. Proposition 4 gives
the finite antichain slice-cover characterization, and Corollary 2 gives
lower semicontinuity over an algebraically closed field. The elementary
score upper bound itself does not require the antichain hypothesis.
