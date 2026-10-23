# Critical finite states and the remaining ordinary single target

October 21, 2026. Written proof under audit; not independently reviewed.
No smaller exponent or matrix-target construction is asserted.

This note combines the generic-flatness reduction with a uniform analysis
of finite support strata. Its intended conclusion is exclusion of an
ordinary restriction A(8,10) -> M(32,33,33). The argument and each input
must be reviewed before regarding this as an independently certified
closure of the last ordinary single-target case through source size1500.

## 1. Reduction to minimal eight- or nine-state sequences

Suppose the restriction exists. Its first target leg gives an injective
linear map Phi:Mat_(32,33) -> C^1360. The rank-two parameter variety has
dimension126. The source slice lift is at most641. The earlier two-ruling
argument excludes the possibility that its generic scalar Hankel rank is
at most7, so the generic scalar rank is8. The quantitative source bound
then gives crossed rank at most9 and at least8.

Neither outer coefficient flattening can have generic rank at most2,
by outer_compression.md. Thus both have generic rank at least3. Choose
one homogeneous long-coordinate chart that works on a nonempty open
subset by generic_flatness.md. This change is fixed for the whole map;
it acts invertibly on the long coefficient space and on the p and q
Hankel factors, so it preserves the source, scalar and crossed ranks.
In that chart there is a minimal realization

    f_k(x,z)=v(z)^t A^k u(x),

of dimension n=8 or9, with deg_x u<8 and deg_z v<10. Minimality follows
from crossed rank n. A rational realization on a fixed minor chart is
provided by flat_realization.py.

If n=8, scalar rank8 forces the minimal polynomial of A to have degree8;
A is cyclic. If n=9, cyclicity is impossible by cyclic_state_gap.md:
source rank is divisible by10 and at least641 by the crossed-rank bound,
hence at least650. A noncyclic nine-state A with scalar rank8 has minimal
polynomial degree exactly8. Its Jordan form therefore consists of one
Jordan block at each support point, except for one extra size-one block
at a single point. The sum of the largest block sizes is8.

Fix the generic Jordan partition and pass locally to an algebraic cover
labeling its distinct support points. A generic scalar evaluation has minimal recurrence order eight, so its first seventeen moments determine that recurrence and hence the support scheme. All dimension and differential
arguments below are on this generic stratum; no assumption of distinct
simple eigenvalues is imposed on the whole state matrix.

## 2. The exceptional block and the one-unit condition

Let the largest block at the exceptional point have size e. The state
there is J_e plus J_1. Denote by u_0(x),v_0(z) the endpoint polynomials
whose product is its highest jet residue, and by u_*(x),v_*(z) those of
the extra block. Minimality makes each pair (u_0,u_*) and (v_0,v_*)
linearly independent as polynomial vectors.

In the scalar Hankel factorization U(z)V(x), the one-dimensional right
kernel of U and left kernel of V are supported on these two eigenspaces.
Up to fixed state-basis factors, their two nonzero coefficients are the
pairs (v_*, -v_0) and (u_*, -u_0), divided by their polynomial gcds.
The one-unit criterion in one_unit_pairing.md forces both primitive
kernel vectors to have degree one.

For e=1 the long-block left and right eigenvectors pair nontrivially,
as do those of the extra block. The resulting kernel pairing is a
nondegenerate bilinear form in two independent linear-polynomial pairs.
It has separation rank two. This contradicts the separable pairing
required by source rank641. Therefore e>=2.

For e>=2, the left and right eigenvectors of the long Jordan block pair
to zero. Only the extra-block pairing remains, a product of one linear
factor in x and one in z. The required separation condition is automatic.
The remaining condition is exactly that both independent polynomial
pairs have primitive quotients of degree at most one. In particular,
for fixed nonzero u_0, the allowable u_* lie in a finite union of
linear spaces of dimension at most2. Indeed their gcd is u_0 divided
by either a constant or one linear factor; the latter has only finitely
many choices among the roots of u_0. The same holds for v_*.

This description includes arbitrary linear-factor roots and amplitudes;
it is larger than the earlier explicit family with fixed factors x,z.
There are at most seven distinct support points in this nine-state case.

## 3. Uniform fibers over the highest residues

A simple state block of size e has coefficient parameters u_0,...,u_(e-1)
and v_0,...,v_(e-1), each with8 and10 coefficients respectively. Its top
residue R=u_0 v_0 is a nonzero rank-one8-by10 matrix. Fixing R leaves
one scalar factorization freedom and18(e-1) remaining coefficients.
The centralizer of a single Jordan block has dimension e and acts freely
on minimal input/output pairs. Thus the image fiber over R has dimension
at most17(e-1).

For the exceptional J_e plus J_1 block, fixing the nonzero top residue
again leaves one scalar freedom and18(e-1) ordinary coefficients. The
preceding gcd argument allows at most two additional parameters for each
of u_* and v_*. The centralizer has dimension e+3, and again acts freely
on minimal pairs. Therefore the image fiber has dimension at most

    1+18(e-1)+4-(e+3)=17(e-1)+1.

The free action assertion follows directly from minimality: an invertible
state map commuting with A and fixing both input and output maps fixes
all A^j input vectors, which span the state space, and is the identity.
Centralizer dimensions follow from dim Hom(J_i,J_j)=min(i,j).
All these actions preserve the highest residues. Quotienting their free
orbits supplies an upper bound even without invoking uniqueness of a
finite realization.

Let rho be the number of distinct support points, whose largest blocks
sum to8. Over any nonzero tuple of top residues, the total fiber dimension
is at most17(8-rho) in the eight-state case and17(8-rho)+1 in the
nine-state case. These bounds are uniform, including lower-degree endpoint
polynomials and repeated roots in the gcd factors.

## 4. Bad residue dependencies cannot contain the parameter image

A rank-one8-by10 matrix cone has dimension17. For rho<=8 nonzero top
residues, call a tuple good if it is independent or has precisely one
proportional pair and no other relation. For rho>=3 the nongood locus
has dimension at most17*rho-22. To see this, a minimal circuit of k>=3
rank-one matrices has dimension at most

    max_(1<=l<k) [l(8+k-l)+10(k-l)-1].

Adding the rho-k free residues gives codimension at least22 for every
3<=k<=rho<=8. If all minimal circuits have size two, two independent
dependencies impose codimension at least32. For rho<=2 every tuple is
good. This is the same incidence argument as multiple_support_linearity.md,
now checked through eight residues.

Add the uniform fiber bounds and rho support parameters. The nongood
family dimension is at most136+rho-22 in the eight-state case, hence at
most122, and137+rho-22 in the nine-state case, hence at most122 since
rho<=7. Both are below126. Thus the generic rank-two image has good
highest residues.

## 5. Support velocities and the eight-simple-point exception

For a support scheme Z of length8 and reduced length rho, quotient the
17-dimensional long space by the jets on Z+Z_red, of length8+rho.
Along any straight line of slices in a fixed generic stratum, the second
derivative is zero. Modulo these discarded jets its equation is

    sum_i R_i tensor q_i * (lambda_i')^2 = 0,

up to nonzero factorial constants. Here q_i is the next jet after the
discarded ones at point i. Terms involving residue derivatives or lower
jets are in the discarded space. For rho<=7, every two q_i are linearly
independent by Hermite interpolation: adding their two jets has length
at most17. Good residues therefore force every support velocity to vanish.

The tangent space to the rank-two parameter variety at UV is generated
by straight-line directions delta(U)V and U delta(V). Thus the support
map has zero differential on its entire generic tangent space and is
constant in characteristic zero. All rank-two images, and hence their
linear span, then lie in a fixed length-eight long space tensored with
the80-dimensional outer coefficient space. This gives dimension at most
640, contradicting injectivity from dimension1056.

The only remaining case is n=8,rho=8, all simple points. The jet quotient
has dimension one and each q_i is nonzero. Independent residues still
force stationary support. If there is one proportional pair, the other
six velocities vanish by isolating their six independent residue
directions. Those six support points are therefore fixed globally on
the generic parameter stratum.

Project the long space by their fixed six-dimensional evaluation span.
On the generic rank-two image the projected tensor is the sum of the
remaining pair with proportional outer residues, hence is decomposable
in C^80 tensor C^11. This rank-one condition extends to every rank-at-most-
two input by closedness. In particular, images of any two rank-one inputs
and their sum are decomposable. Such a pairwise compatible collection
of decomposable tensors has a common factor: if two independent members
share one factor, any third must share that factor as well. Since
rank-one inputs span Mat_(32,33), the entire projected linear image has
dimension at most max(80,11)=80. Restoring the fixed six support spaces
gives total dimension at most6*80+80=560, again below1056.

## Conclusion and limitations

Every generic stratum described by the finite-realization reduction is
excluded. Subject to the written lemmas and this argument, the remaining
ordinary A(8,10) -> M(32,33,33) restriction is impossible. This does not
exclude singular tensor degenerations, multiple target blocks, larger
sources, or other approaches to a smaller exponent. The result is a
written obstruction under audit, not an independently certified theorem.

Exact arithmetic controls will cover the incidence dimensions, every
partition of8 and its Hermite jet counts, and the exceptional Jordan
pairings. They are checks of the argument's algebra, not substitutes for
review of the uniform fiber and generic-stratum steps.

## Corollary for a large block inside a direct sum

The proof uses only these properties of the target parameter space
Mat_(p,q), not the exact values32 and33:

- p,q>=2 and pq>960, for the scalar-rank-seven ruling contradiction;
- 2(p+q-2)>122, for exclusion of the nongood finite-state strata;
- the two outer-compression bounds from outer_compression.md are below pq;
- every rank-two parameter lifts to a source slice of rank at most641.

Under these conditions the same contradiction applies. In a direct sum,
set all other blocks to zero on the parameter leg. If its three total
leg dimensions are D_0,D_1,D_2, a selected block M(p,q,w) on leg i has
rank-two lift at most

    2w + 2*1360 - sum_(j != i) D_j.

This allows a further necessary-condition filter on the historical
two-block survivor list. It does not assume the other block is absent
when computing the deleted source dimensions.
