# Exact rational rectangular seed

The reduced search yields an ordinary restriction A(3,3) -> M(5,5,3).
This is a concrete small module, not an exponent improvement or a claim of
historical novelty. The full M5 target remains obstructed in this SL2 ansatz.

Use the complete integer intertwiner bases in
`results/asymmetric-sl2-seed-20261021/rectangular-bases.json`, in their saved
order. The three coefficient vectors are

- A: (-1/192, 0, 1/96, 0, 0, 0, -1/384, -1/384, -1/96)
- B: (1, 0, -1/3, 0, 1/3, 0, 0)
- C: (1, -2, -4, -3, 0, 0, 0).

Some basis entries cancel denominators, so the assembled maps have common
leg denominators (192,1,1). The vertex representations are V4,V4,V2.
All 5625 coefficients of the physical trace contraction were checked as
rational numbers. A separate verifier uses only Python exact integers and
Fractions, expanding all 729 original source terms, and checks all 5625
output coefficients, including the 75 required ones. It does not use the
numerical compressed equations or assume equivariance implies correctness.

The initial complex alternating least-squares discovery reached relative
error 0.0002402. Analytic-Jacobian least squares reached 7.8e-15. Dividing
within each leg exposed rational ratios; the unnormalized exact contraction
was -192 times the target, giving the displayed A normalization. Neither
numerical residual is used in the exact verification.

The source conventions are W(F)[(i,q),(p,s)] = F[i,p+q,s]. Accordingly the
original cyclic trace terms are F[i,p+q,s] G[p,r+s,j] H[r,i+j,q]. These are
written explicitly to avoid a cyclic-index mismatch in independent replays.

## Next use and limitation

The module can be tensored or embedded into larger sources using verified
source maps. It is not enough to insert a rectangular block into a desired
square target: all cross-block products and mixed coefficients must match.
A single volume75 block at A33 has no improved-exponent implication from
the maintained score criterion. Any assembly or generalization remains open.
