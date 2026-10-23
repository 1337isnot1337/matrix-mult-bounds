# Exact convolution sectors from self-adjoint moment constructions

October 21, 2026. Explicit rational finite construction, checked in the same
AI research session. External mathematical review and formalization are
outstanding. **No smaller matrix multiplication exponent is established.**

This package contains complete rational witnesses at two sizes:

| Target degree sectors | Source | Target dimensions | Independent coefficient checks |
| --- | --- | --- | --- |
| Five sectors, described below | `C(6,20)` | `5,15,15` | 1,125 |
| [Six sectors](m6_construction.md) | `C(7,28)` | `6,21,21` | 2,646 |

The [common-ideal rank bound](common_ideal_bound.md) explains why putting
every lower sector in a single isotropic polynomial ideal cannot give an
asymptotic cost-one extension. It does not exclude mixed recursive flags.

## Certified statement

There are explicit rational maps giving

\[
C(6,20)\unrhd\widetilde T_5,
\qquad
\widetilde T_5=
\sum_{p=0}^4\sum_{a=0}^p\sum_{c=0}^{4-p}\sum_{i=0}^4
(H_p)_{i,a+c}X_iY_{a,p-a}Z_{c,4-p-c},
\]

where every `H_p` is invertible. Thus the five matched blocks are actual
copies of `C(1,5), C(2,4), C(3,3), C(4,2), C(5,1)`, with the convolution
output as their common shared factor. Their shared identifications may differ.
This is the broader target allowed by the
[conditional growth criterion](../2026-10-20-construction-sprint/independent_sector_bases.md).
It is not asserted to be isomorphic to the canonical fat-point tensor `T5`.

The source convention is

\[
C(6,20)=\sum_{j=0}^{19}\sum_{d=0}^5 A_dY_jZ_{d+j}.
\]

The target maps have shapes `5 by 6`, `15 by 20`, and `15 by 25`.
Target rows are ordered by total degree `p=0,...,4`, then by the first
index `a=0,...,p`. The shared map has constant rows
`1,t,t^3,t^4,t^5`. Both nonshared maps multiply every degree-`p` row by
`epsilon^(p-2)`. Consequently a target coefficient has Laurent exponent
`p+q-4`.

The [frozen witness](../../../results/selfadjoint-sectors-2026-10-21/m5-witness.json)
specifies every rational entry. Independent direct substitution into the
120 source monomials checks all 1,125 target coefficient positions:

| Coefficient class | Exact result |
| --- | --- |
| 175 negative-weight positions | All vanish |
| 175 constant positions | Equal their prescribed `H_p` entries |
| Nonzero constant positions | 135 |
| 775 positive-weight positions | All nonzero, with degrees 1 through 4 |
| Ranks of the three constant maps | 5, 15, 15 |

The determinants of the five shared maps are

\[
1,\quad -\frac1{4667578047266447687912},\quad
-71944362,\quad -\frac1{4667578047266447687912},\quad 1.
\]

These finite identities prove the stated degeneration over the rationals,
and therefore over every characteristic-zero field.

## Construction by a symmetric moment pairing

All details below are discovery and reconstruction tools. The independent
verifier needs only the three final maps, the sector maps, and the weights.

Let `U=span(1,t,t^3,t^4,t^5)`, set `h=t^14`, and work with polynomials
of degree at most 19 on each nonshared input to a symmetric pairing. Choose
a rational functional `L` with `L(t^27)=1` and `L(t^k)=0` for `k>=28`.
The saved witness records all moments, including those below degree 27.
The five forms are

\[
B_i(f,g)=L(u_i f g),\qquad (u_0,\ldots,u_4)=(1,t,t^3,t^4,t^5).
\]

The output map associated with a polynomial `g` is the functional
`Z_g(t^k)=L(g t^k)`, for `k=0,...,24`. This realizes these symmetric forms
as actual maps from the displayed convolution source.

### First isotropic flag

Take the following three polynomials, in coefficient order `1,t,...,t^5`:

\[
F=\begin{pmatrix}
-1&-1&-1&0&-1&1\\
1&0&0&1&-1&1\\
-1&1&1&-1&0&1
\end{pmatrix}.
\]

Use `h f_0` for the degree-zero row and `h f_1,h f_2` for the degree-one
rows. Products of any two such rows lie in `(t^28)`, so every `B_i` pairs
them to zero. The product space `U span(f_0,f_1,f_2)` is all polynomials
through degree 10, of dimension 11. The common annihilator of the three
low rows in the 20-dimensional input polynomial space therefore has
dimension 9.

### Hankel central block

Set

\[
R(t)=\sum_{j=0}^{13}L(t^{27-j})t^j,\qquad
k_i=t^i/R(t)\pmod {t^{14}}\quad(i=0,1,2).
\]

Its constant coefficient is one, so the inverse is defined over the
rationals. These three polynomials belong to the common annihilator just
described. Since `t k_i-k_(i+1)` lies in `t^14 P_5`, and that space is
orthogonal to the annihilator for each `B_i`, the matrices
`(B_i(k_a,k_c))_(a,c=0)^2` are Hankel: their entries depend only on `a+c`.
Their five anti-diagonal vectors form

\[
H_2=\begin{pmatrix}
1978&-1925&1097&-949&425\\
-1925&1097&-949&425&-338\\
-949&425&-338&58&-41\\
425&-338&58&-41&-85\\
-338&58&-41&-85&61
\end{pmatrix},
\]

whose determinant is `-71944362`. Thus the central sector is exactly
`C(3,3)` under an invertible shared identification. These are the
degree-two rows.

### Outer pencil and endpoint

The common kernel of the five functionals `B_i(h f_0,-)` has dimension
15. Its quotient by the preceding nine-dimensional annihilator has
dimension 6. Select four representatives in this quotient. Pairing them
with `h f_1,h f_2` gives two `4 by 5` matrices `L0,L1`.

The saved rational selection has a maximal-minor kernel polynomial for
`L1-t L0` of degree four whose five coefficient vectors form an invertible
matrix `C`. If `D=L0 C[:,:4]`, the exact identities are

\[
L_0 C=[D\mid0],\qquad L_1 C=[0\mid D],\qquad \det D\ne0.
\]

Replacing the four rows by `D^-1` times those representatives gives the
degree-three rows and shared identification `H_1=H_3=C^-T`.
The remaining degree-four rows are a right inverse of the map
`f -> (B_i(h f_0,f))_i`, giving `H_0=H_4=I`.
The common-annihilator and kernel choices give every lower-degree
vanishing condition. Symmetry gives both orientations of each matched
block. The independent coefficient replay confirms the whole system.

## Reproduction and scope

Run from the repository root:

```sh
python research/ai/2026-10-21-selfadjoint-sectors/verify_witness.py results/selfadjoint-sectors-2026-10-21/m5-witness.json
python -m unittest discover -s tests -p test_selfadjoint_sectors.py -v
```

The verifier uses Python's standard-library rational arithmetic. Optional
reconstruction uses SymPy 1.14 and the recorded seed 2:

```sh
python research/ai/2026-10-21-selfadjoint-sectors/construct_m5.py --seed 2 --output /tmp/selfadjoint-m5-reconstructed.json
```

The generator and replay are different implementations: the generator
works with moments, nullspaces, and polynomial cofactors; the replay
expands each original convolution monomial using only the final matrices.
Neither constitutes external mathematical review.

The five-sector target nonshared dimension is `N=15`; the source has `B=20=N+5`
and shared dimension `a=6=m+1`. These are finite ratios. An unbounded
family with `B=N+O(m)` and `a=m+O(1)` would meet the previously stated
conditional growth premise, but this example does not construct such a
family. In particular, later low-degree blocks cannot simply all be
placed in the same high polynomial ideal at asymptotic cost one; that
restricted extension has a separate rank constraint.

The construction is AI-derived work of this research session. The target
class and exponent implications are attributed to the linked existing
criterion; no external exponent theorem is claimed as this repository's
work.
