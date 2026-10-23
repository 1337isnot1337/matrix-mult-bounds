# A rational construction of the three-weight degeneration

Date: October 21, 2026.

This note constructs explicit rational maps for `C(5,10) -> T_4`.
It gives an algebraic construction of the finite degeneration whose
existence was first certified in this package by a rational contraction
argument. Neither finite result by itself improves the matrix
multiplication exponent.

The optional SymPy constructor is `construct_rational_flag.py`.
Its default seed is zero and all its calculations are exact. The saved
map coefficients are rational numbers, not rounded coordinates of the
earlier contraction certificate. A separate standard-library verifier
checks the final witness independently.

The complete [rational matrices and remainder](../../../results/rectangular-t4-certificate-2026-10-21/rational-witness.json)
and the [independent replay report](../../../results/rectangular-t4-certificate-2026-10-21/rational-verification.json)
are included. The identity holds over the rationals and hence over every
field of characteristic zero. To replay the final certificate, run:

```sh
python research/ai/2026-10-21-rectangular-t4-certificate/verify_explicit.py results/rectangular-t4-certificate-2026-10-21/rational-witness.json
```

The optional exact reconstruction uses SymPy 1.14:

```sh
python research/ai/2026-10-21-rectangular-t4-certificate/construct_rational_flag.py --seed 0 --output /tmp/rational-t4.json
```

## 1. First polynomial flag

Work in `P_9`, with output functionals on `P_13`. Begin with the shared
subspace

`U=span(1,t^4,t,t^3)`.

The displayed order is the initial shared basis. Take

`h=-t^2+t^4+t^5`,

`w_0=1+t^4-t^5+t^6-t^7-t^9`,

and `W=span(w_0,h t^4,h)`. Direct exact computation gives
`dim(UW)=11`. Its only product relation is
`1 tensor (h t^4)-t^4 tensor h`.
Consequently `E=ann(UW)` has dimension three.

These choices are the default constructor's explicit input, not a
genericity assertion. The general first-flag construction and its
independent integer controls are in the adjacent rectangular-module
package.

## 2. A residual matrix pencil

Choose the primitive integer nullspace basis `e_0,e_1,e_2` specified
by the constructor, and put

`z_0=e_0+e_1+e_2`, `z_y=e_0`, `z_x=e_1`.

Let `F_0:P_9 -> U*` send `f` to the values `z_0(u_i f)`.
The explicit matrix has rank four. Its kernel `W_mid` has dimension
six and contains `W`. Choose three representatives `M` for
`W_mid/W`. Pairing these representatives with `z_y,z_x` gives two
`3 by 4` matrices `L_0,L_1`.

The vector of signed maximal minors of `L_1-tL_0` is a polynomial
kernel vector. Remove its common polynomial factor and write it as

`C (1,t,t^2,t^3)^T`.

For the displayed input, `C` is invertible. Define
`D=L_0 C[:,0:3]`. The kernel identity gives

`L_0 C=[D 0]`, `L_1 C=[0 D]`,

and the exact calculation also gives `det(D)!=0`.

Replace the shared basis matrix `A` by `C^T A` and the middle input
representatives by `D^-1 M`. Their two output slices are now
`[I_3 0]` and `[0 I_3]`, exactly the degree-two-by-degree-one
catalecticant block of `T_4`.

This step uses elementary polynomial cofactors and matrix inversion.
The inverses and all nonzero rank claims are checked exactly for
the displayed data.

## 3. Aligning the first flag with the same shared coordinates

The new shared basis changes the coordinates of the original pencil
`span(1,t^4)`. Choose two forms `u,v` in that pencil whose new shared
coefficient vectors satisfy

`u_i=v_(i+1)`, for `i=0,1,2`.

This is a homogeneous system of three equations in the four
coefficients expressing `u,v` in the old pencil. The explicit
nullspace vector gives independent `u,v`. Set the degree-one input
rows to `h v,h u`; keep the degree-zero row `w_0`.

The only relation in `U tensor W` is now

`u tensor (h v)-v tensor (h u)`.

Its three recurrence identities are precisely the conditions for it
to be a relation of the target degree-one-by-degree-two block.
Therefore the seven high-output rows of total degrees two and three
can be prescribed by the target tensor on `UW`, and extended to
`P_13` by solving a consistent rational linear system.

Finally choose four input rows that are dual to the four independent
functionals `f -> z_0(u_i f)`. This gives the degree-three-by-degree-zero
identity block. The ten input rows are independent: three span `W`,
three complete `W_mid`, and four complete `P_9`. The output rows are
independent for the analogous annihilator and quotient reason.

## 4. Laurent weights and exact identity

Index target input and output monomials by total degree and then by
their first exponent. Give input degrees `0,1,2,3` the weights

`(0,0,1,2)`,

and output degrees `0,1,2,3` the weights

`(-2,-1,0,0)`.

The shared map has weight zero. The first-flag annihilator makes all
negative coefficients vanish. The cofactor identification, first-flag
relation, and dual top rows give every constant target block, including
the required zero off-block entries. Every other nonzero coefficient
has positive weight. Thus the three row-scaled rational maps give

`mapped C(5,10) = T_4 + positive powers of epsilon`.

The default witness has 48 checked negative coefficients, 124 checked
constant coefficients, and 228 nonzero positive remainder terms.
It has shared, input, and output ranks `4,10,10`.

The source shared kernel is exactly the coefficient of `t^2`.
The invertible rational shared change in the construction does not
alter that source hyperplane.

## 5. The remaining all-size question

The construction suggests taking a first product flag, passing to its
annihilator, and constructing the remaining target blocks on the
quotient. For `m=4`, the next block is a `3 by 4` matrix pencil, so
its full minimal-index condition gives an explicit cofactor basis.
For larger `m`, the next block has more than two output slices.
Its target catalecticant identities still need to be established.

Independent invertible shared identifications for different degree
blocks can remove the final common-coordinate alignment requirement
when only the block character inequality is needed. They do not remove
the need to construct each block's multiplication tensor or to cancel
every negative and constant off-block coefficient.
