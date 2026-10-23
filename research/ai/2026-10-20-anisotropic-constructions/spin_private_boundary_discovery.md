# Two finite attempts to change the spin boundary

October 21, 2026. These are bounded discovery calculations over the
prime field of order 65521. They do not export characteristic-zero
matrix maps, exclude all choices of subspaces, or lower the matrix
multiplication exponent.

The motivation is constructive. The first saved spin core had an
injective deleted-channel convolution map. A useful replacement should
preserve many middle channels while leaving a response direction
available to a new matrix unit. Both attempts below keep the explicit
spin first map from [the rational construction](spin_module14.md).

## 1. An undoubled larger convolution

The reduced source is the cyclic product with parameters (2,8,8),
with leg dimensions (12,144,144). Its transfer maps are

\[
J_s e_{a,j}=e_{a+s,j},\qquad (K_i z)_{a,j}=z_{a,j+i},
\qquad a,j<8,\quad i,s<2.
\]

The program builds a 26-dimensional subspace U from four polynomial
chains. It tests nine length profiles, two generator densities,
and six seeds per choice: 108 completed trials. A candidate for
28 channels needs a 60-dimensional ignored space and a full
144-dimensional join after choosing 28 endpoint pairs.

The largest complete join found has rank 134. It occurs for profile
(8,7,6,5), density 5, trial 3, seed 851503. At that point U has
dimension 26, the ignored space has dimension 60, and the endpoint-pair
space has dimension 31. No candidate was found. This does not bound
the optimum over other subspaces or other first maps.

The saved [complete records](../../../results/anisotropic-constructions-2026-10-20/undoubled-spin-discovery.json)
include every tested seed and rank. The optional generator is
[undoubled_spin_discovery.py](undoubled_spin_discovery.py).

## 2. A distinguished boundary pair

The second attempt makes a channel special by design. First use
parameters (2,3,8), chain lengths (3,3,2,2), and a ten-dimensional U.
The second trial, seed 932001, gives

\[
\dim W=28,\qquad \dim D=12,\qquad
\operatorname{rank}[W,L'_0V,L'_1V,L'_2V]=64.
\]

All statements in this note concern the saved finite-field bases.
This rank calculation is not an accepted rational tensor witness.

Embed U into the (2,4,8) source by shifting its first polynomial
coordinate from r to r+1. Add the vector at r=0 with coefficients
\(e_{j=0}-e_{j=7}\), and add the explicit pair

\[
z^+=e_{r=0,H=0},\qquad z^-=e_{r=0,H=8}.
\]

The pair equations hold: \(K_1z^+=K_0z^-=0\), and
\(K_0z^+-K_1z^-=e_{r=0,j=0}-e_{r=0,j=7}\) belongs to the
enlarged U. The other twelve pairs are supported at r at least one.
Thus deleting this distinguished pair leaves a common first-variable
factor in their last-map polynomials.

The enlarged dimensions are U=11, W=32, and D=13. However, the
prescribed 71-column join has rank 68. Three dimensions are missing,
so this recipe does not give the desired thirteen-channel module.

## 3. The specified first-map repair also fails over the saved field

Keep those thirteen-channel last-leg rows fixed. With the original
spin first map, enumerate every coefficient of a freely varying
second vector on the 80 original second coordinates. The resulting
matrix M has shape \(351\) by \(80\) and rank 68. Let T be the
351-by-39 matrix of the desired M(3,3,13) coefficients and let Q
annihilate the image of M. The target quotient has

\[
\operatorname{rank}(QT)=3.
\]

The proposed repair adds three first coordinates \(F(i,3,0)\), for
i=0,1,2, with arbitrary linear forms in all nine target first entries.
It allows three additional second coordinates:
\((p,L,j)=(2,0,0),(2,0,7),(2,0,6)\). Each extra coefficient column
is an affine function of nine repair coefficients.

A solution would require the images of these three extra columns
modulo M to span the three-dimensional target quotient. In particular
each must lie in that quotient. The program eliminates the quotient
coordinates and solves each membership condition by exact modular
row reduction. The first two affine conditions are inconsistent.
The third has a one-dimensional solution space. Consequently this
specific three-coordinate repair cannot complete the saved finite-field
thirteen-channel tensor.

This is a finite-field conclusion for the explicit saved basis and
repair chart. It does not exclude a different boundary pair, another
first map, additional source coordinates, or a rational construction
whose reduction is outside this chart.

The [candidate basis](../../../results/anisotropic-constructions-2026-10-20/spin-private-boundary-candidate.json),
[discovery coverage](../../../results/anisotropic-constructions-2026-10-20/spin-private-boundary-discovery.json),
and [quotient calculation](../../../results/anisotropic-constructions-2026-10-20/spin-private-boundary-quotient.json)
preserve the actual inputs and outcomes.

## Reproduction

The optional discovery programs use NumPy and the finite-field toolkit
in the earlier spin discovery script. They are separate from the
standard-library rational acceptance verifiers.

    python research/ai/2026-10-20-anisotropic-constructions/undoubled_spin_discovery.py --trials 6
    python research/ai/2026-10-20-anisotropic-constructions/spin_private_boundary_discovery.py

The boundary program stops at the first qualifying base point, after
two trials in the first profile, and then performs the complete
quotient calculation. The two discovery programs do not claim a
full square assembly or a smaller exponent.

