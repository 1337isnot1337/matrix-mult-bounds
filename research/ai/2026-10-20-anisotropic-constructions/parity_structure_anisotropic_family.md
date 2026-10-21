# An integral direct-sum family for A(a,a+1)

October 21, 2026. Exact constructive family, with complete coefficient
replays at a=5,6,7. No improved exponent is claimed.

For every a>=5,

\[
A(a,a+1)\longrightarrow
M_{2a-2}\oplus M_{2\lfloor(a-1)/2\rfloor}.
\tag{1}
\]

This generalizes the M8 plus M4 construction. At the current larger
source it gives A(7,8) to M12 plus M6. Cropping the latter block gives
an exact M12 plus M5 seed, with 1,853 target coefficients. It does not
construct the proposed M25 plus M5 target.

## Local bases

Put d=a-1 and c=floor(d/2). The first short space has degree at most d,
the second has degree at most d+1, and the long space has degree at
most 2d+1. Set

\[
U=(1,x^d),\qquad
V_1=x-x^d,\quad V_j=x^j\ (2\le j<d),\quad V_*=1+x^{d+1}.
\tag{2}
\]

Thus V has d basis vectors, in the order 1,...,d-1,*. The 2d products
U_alpha V_beta are independent. Their dual functionals are

\[
\begin{aligned}
R_{0,j}&=e_j\quad(1\le j<d),& R_{0,*}&=e_0,\\
R_{1,1}&=-e_0+e_{d+1},& R_{1,*}&=e_1+e_d,\\
R_{1,j}&=e_{d+j}\quad(2\le j<d).
\end{aligned}
\]

The complementary functionals are

\[
h_0=-e_0+e_{d+1}+e_{2d},\qquad
h_1=-e_1-e_d+e_{2d+1}.
\tag{3}
\]

In particular, h_0 and h_1 annihilate U times V. The full list of
products followed by x^(2d),x^(2d+1) has inverse with rows (R,h_0,h_1).
This is an integer inverse on both sides, so no interpolation
denominators enter the construction.

Choose c first-short vectors

\[
P_0=x,\qquad P_\mu=x^{2\mu}\quad(1\le\mu<c).
\]

Choose 2c second-short vectors, all in span(V):

\[
\begin{aligned}
Q_{0,0}&=-V_1,&Q_{0,1}&=-V_*,\\
Q_{\mu,0}&=V_{d+1-2\mu}-\delta_{\mu,1}V_*,&
Q_{\mu,1}&=-V_{d-2\mu}\quad(1\le\mu<c).
\end{aligned}
\tag{4}
\]

The index ranges in (4) are valid for d>=4. Coefficient extraction
using (3) gives

\[
h_\lambda(P_\mu Q_{\nu,\kappa})
=\delta_{\mu,\nu}\delta_{\lambda,\kappa}.
\tag{5}
\]

For positive mu, the selected even degrees pair with monomials whose
sum is d+1 for h_0 and d for h_1. All other relevant sums avoid the
supports of h. The only extra pairing at mu=0 is
h_1(x V_(d-1))=-1; subtracting V_* in Q_(1,0) cancels it. The choices
Q_(0,0)=-V_1 and Q_(0,1)=-V_* give the two remaining unit pairings.
This proves (5) for both parities of d.

## Cyclic products and vanishing mixed terms

The identity on U,V,R is an outer product of dimensions 2 and d.
Its cyclic product is M_(2d), using the core-map formula in
`parity_structure_a56.md`. Identity (5) is an outer product of
dimensions c and 2, with the 2c-dimensional factor in the second
short space. Its cyclic product is M_(2c), using the extra-map
formula from the same note, with the first vertex label ranging
from 0 to c-1.

The two blocks form a direct sum. With one extra row, its long h
pairs core U and V and vanishes. With two extra rows, a long h
pairs a core U and an extra Q; this also vanishes because Q belongs
to span(V). Every mixed cyclic placement has one of these factors.
This proves (1).

Every map entry is 0, 1, or -1. There are
4a(a+1)+12c(c+2) nonzero entries on each leg. These counts refer
to the explicitly supplied maps and do not assert any optimality.

## Exact controls and exported seed

| Source | Target | Common target dimension | Target terms |
|---|---|---:|---:|
| A(5,6) | M8 plus M4 | 80 | 576 |
| A(6,7) | M10 plus M4 | 116 | 1,064 |
| A(7,8) | M12 plus M6 | 180 | 1,944 |

The verifier checks both local inverse identities, every entry of (5),
and the complete image of every original source coefficient in these
three cases. It separately checks the cropped M12 plus M5 image.

Files:

- `parity_structure_anisotropic_family.py`: the all-a construction and exact replay.
- `parity_structure_anisotropic_family_certificate.json`: exact finite checks and counts.
- `parity_structure_anisotropic_family_a78_maps.npz`: integer A,B,C maps of shape (180,784), x,y,z aliases, local bases, and A_cropped,B_cropped,C_cropped arrays of shape (169,784).

The full A78 maps have the M12 block in rows 0 through 143 and M6
in rows 144 through 179. The cropped maps retain those first 144
rows and use five vertices of M6 for a final M5 block. All blocks
use standard matrix-index order.

Run from the repository root:

```
python research/ai/2026-10-20-anisotropic-constructions/parity_structure_anisotropic_family.py
```

These are actual smaller tensor restrictions. A larger target needed
for an exponent improvement remains unconstructed.
