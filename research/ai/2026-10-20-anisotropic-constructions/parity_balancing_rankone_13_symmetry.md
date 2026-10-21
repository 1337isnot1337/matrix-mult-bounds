# Symmetric versions of the degree-13 rank-one obstruction

This note transfers `parity_balancing_rankone_13_chain.md` to the other
three extreme rank-one types. It adds no general torus exclusion.

## Transpose with a swap of the short physical factors

The source matrix space need not be stable under ordinary transposition.
It is stable under the following anti-automorphism. Let S exchange the
two factors of the 8 by 8 physical space:

\[
 S e_{(i,q)}=e_{(q,i)},\qquad \tau(W)=S W^T S.
\]

For the source convention `W(F)_((i,q),(p,s))=F(i,p+q,s)`, direct indexing
gives

\[
 \tau(W(F))=W(F'),\qquad F'(i,k,s)=F(s,k,i).
\]

Thus tau preserves the source space and its torus weights. It reverses
products and preserves trace. In particular it fixes the positive
extreme `F(7,0,7)` and exchanges `F(6,0,7)` with `F(7,0,6)`.

On each target matrix block let R reverse the vertex order and put

\[
 \sigma(A)=R A^T R.
\]

The target charge profile is symmetric under reversal. Consequently
sigma also preserves weights and reverses products. It fixes the
positive extreme unit `E_(26,0)` and exchanges `E_(25,0)` with
`E_(26,1)`.

Apply tau to the source maps and sigma to their target inputs, and
reverse the three leg order. The two trace reversals preserve the
tensor identity. Two cyclically adjacent prescribed legs remain
adjacent after this reversal. Therefore the rank-chain theorem for
`E_(25,0) -> F(6,0,7)` proves the same ordinary-restriction obstruction
for `E_(26,1) -> F(7,0,6)` on two adjacent legs, with their positive
extreme partners prescribed as before.

## Charge reflection

Physical reflection `e_(i,q) -> e_(7-i,7-q)` acts on source coordinates as

\[
 \rho:F(i,k,s)\longmapsto F(7-i,14-k,7-s).
\]

It is a matrix conjugation and reverses torus weights. Target vertex
reversal `kappa(A)=R A R` is also a conjugation and reverses weights.
Applying both preserves the tensor identity and sends the two positive
rank-one types to their negative counterparts.

## Four precise exclusions

Each row below specifies one source image and the corresponding extreme
image on two adjacent legs. All coefficients may be arbitrary nonzero
scalar multiples of those displayed. The other maps and coefficients
remain unrestricted subject to the source space and torus profile.

| Type | Prescribed target unit | Prescribed source coordinate | Extreme partner |
| --- | --- | --- | --- |
| Positive R | `E_(25,0)` | `F(6,0,7)` | `E_(26,0) -> F(7,0,7)` |
| Positive Q | `E_(26,1)` | `F(7,0,6)` | `E_(26,0) -> F(7,0,7)` |
| Negative R | `E_(1,26)` | `F(1,14,0)` | `E_(0,26) -> F(0,14,0)` |
| Negative Q | `E_(0,25)` | `F(0,14,1)` | `E_(0,26) -> F(0,14,0)` |

For each individual type, two such legs are impossible. Equivalently,
each type can occur on at most one of the three legs of an ordinary
restriction with the stated profile. This does not yet rule out mixed
patterns or pencils whose relevant images have physical rank two.
No global torus restriction exclusion or exponent improvement follows
from this statement alone.

The symmetry was derived by the generating worker and checked by the
parent as a second agent in this generating session; no external
independent review or formalization has occurred.

`parity_balancing_rankone_13_symmetry.py` verifies source-space
preservation on all 960 coordinate matrices, checks all 4,096 nonzero
physical entries of that basis, and checks target multiplication for
all pairs of matrix units in both blocks. The exact report is saved at
`results/anisotropic-constructions-2026-10-20/parity_balancing_rankone_13_symmetry.json`.

```bash
python -S research/ai/2026-10-20-anisotropic-constructions/parity_balancing_rankone_13_symmetry.py
```
