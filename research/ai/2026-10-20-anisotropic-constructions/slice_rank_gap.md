# A gap above minimum slice rank

October 20, 2026. Written proof checked by a second agent in this session.
No external independent review or formal verification is claimed. This is an ordinary-
restriction obstruction. It does not obstruct degeneration by singular
parameter-dependent maps, and it proves no improved exponent.

Work over C and let 2 <= a <= b. Put m=a+b-1 and N=abm. Use the source
coordinates from the [construction note](README.md): a first-leg slice F
has matrix entries F_(H-j,p+q,L-r), with out-of-range coefficients zero.

## Claim

Every nonzero slice of A(a,b) has rank ab or rank at least ab+a. The
projective locus with rank ab consists exactly of

    F_(i,k,s) = u_i h_k v_s,

where u and v are nonzero and the a-by-b Hankel matrix (h_(p+q)) has rank
one. This locus has dimension a+b-1.

In particular, a nonzero A(4,5) slice has rank 20 or rank at least 24. Its
minimum-rank locus has projective dimension eight.

## 1. The biform block

For f=(f_(i,s)), define R(f), with rows (j,L) and columns (H,r), by

    R(f)_((j,L),(H,r)) = f_(H-j,L-r).

Here 0<=i,r<a, 0<=s,j<b and 0<=H,L<m. Thus R(f) has bm rows and am
columns. Regard f as the biform sum f_(i,s) x^i z^s.

**Block lemma.** For f nonzero, R(f) has rank ab when f=u(x)v(z), and
rank at least ab+a otherwise.

Homogenize the coefficient polynomials f_s(x) to common x-degree a-1.
Divide all of them by their greatest common homogeneous factor. The
resulting primitive coefficient forms have degree d and no common zero
on P^1. The case d=0 is exactly the separable case f=u(x)v(z).

Make the a-by-m polynomial matrix H(x) whose r-th row is the coefficient
vector, in z, of z^r times the primitive biform. At every point of P^1,
this primitive biform is a nonzero polynomial in z. Its first a shifts
are linearly independent. Consequently H defines a surjective map of
vector bundles

    O^m -> O(d)^a.

Equivalently, this is the degree-d twist of O(-d)^m -> O^a.

Its kernel E has rank b-1 and degree -ad. The splitting theorem for
vector bundles on P^1 gives

    E = direct sum_(j=1)^(b-1) O(-mu_j),
    mu_j >= 0,    sum_j mu_j = ad.                       (1)

The nonnegativity follows from E being a subbundle of O^m: a summand of
positive degree has no nonzero homomorphism to O. The splitting theorem
is the only external structural input in this proof. See Grothendieck,
Theorem 2.1, printed page 126, in the primary source linked below.

The transpose R(f)^T is the coefficient map of H applied to vectors of
polynomials of degree at most b-1. Indeed, its output at (H,r) is

    sum_(j,L) f_(H-j,L-r) y_(j,L),

which is the coefficient of x^H in sum_L f_(L-r)(x)y_L(x). Restoring the
removed common factor multiplies every output polynomial injectively,
so it does not change the kernel. The kernel dimension is therefore

    h^0(E(b-1)) = sum_j max(0,b-mu_j).

The domain has dimension mb. Hence

    rank R(f) = ab + sum_j min(b,mu_j).                  (2)

If d=0, all mu_j vanish and the rank is ab. If d>=1, then

    sum_j min(b,mu_j) >= min(b,sum_j mu_j)
                       = min(b,ad) >= a,

since a<=b. This proves the block lemma. It also recovers the lower
bound ab for every nonzero block without a genericity assumption.

For later use, in the separable case f=u v the two spaces are

    row R(f) = (u C[x]_(<b)) tensor C^a,
    col R(f) = C^b tensor (v C[z]_(<a)),                 (3)

inside the respective coefficient spaces. For two nonproportional
nonzero u, the spaces u C[x]_(<b) differ: equality would force both u
to divide the other, with equal degree. One can state the same argument
homogeneously, where both have degree a-1. Likewise, the spaces
v C[z]_(<a) differ for nonproportional v.

## 2. The full slice

After grouping rows by p and columns by q, the full slice is the a-by-b
block Hankel matrix

    B_(p,q) = R(F_(p+q)),

where F_k is the biform with coefficients F_(i,k,s). Assume

    0 < rank B < ab+a.                                 (4)

Every nonzero block has rank below ab+a, so the block lemma makes every
nonzero F_k separable. First make F_0 nonzero by a GL2 change of variables
on the middle convolution factor. This acts invertibly on all three
source spaces and preserves both the source tensor and slice rank. Such
a change exists because powers of linear forms span the degree m-1
binary forms. Thus a nonzero vector-valued form cannot vanish on every
point of the Veronese curve. The block lemma continues to apply after
this change.

Write F_0=u_0 v_0. Its block has rank ab. In the first block row, a block
whose v-factor is not proportional to v_0 would increase the column
space dimension to at least b(a+1)=ab+b, by (3). This contradicts (4).
Thus, for q<b, all nonzero F_q have the factor v_0.

In the first block column, a block whose u-factor is not proportional
to u_0 would increase the row-space dimension to at least a(b+1)=ab+a.
This too contradicts (4). Since a<=b, the first-column indices are
among the indices already covered by the first row. Therefore

    F_p = c_p F_0    for 0<=p<a,   with c_0=1.          (5)

Subtract c_p times the first block row from block row p. The first
block column becomes zero below its top block. The first block row
has rank exactly ab, since all its blocks have the same column space.
Restriction of this row space to the first block column is injective,
because that top block also has rank ab. The remaining block rows
therefore contribute rank independently of the first row. Each block
in them consequently has rank less than a, by (4). Such a block is

    R(F_(p+q) - c_p F_q).

The block lemma gives rank at least ab for every nonzero such block.
Since ab>=a, all these blocks vanish. Injectivity of f -> R(f) gives

    F_(p+q) = c_p F_q    (0<=p<a, 0<=q<b).             (6)

Using p=1 gives F_q=c_1^q F_0 for 0<=q<=b. The other p then cover all
indices through a+b-2. Thus

    F_k = c_1^k F_0,

and B has rank ab. Undoing the GL2 change retains a rank-one Hankel
factor. Conversely, a product of two nonzero biform factors and a
rank-one Hankel factor gives rank ab directly. This proves the claim.

The projective minimum-rank locus is the Segre image of

    P^(a-1) x P^1 x P^(b-1),

where the middle factor is embedded as the degree m-1 rational normal
curve. Its dimension is (a-1)+1+(b-1)=a+b-1.

## 3. Consequence for the selected ordinary restriction

Suppose constant linear maps sent A(4,5) exactly to M(12,12,13). All
three maps would be surjective because the target is concise. The
first dual map would inject the projective rank-one matrix variety

    P^11 x P^11

into the source slice space. A rank-one target parameter gives a slice
of rank 13. The maps on its other two legs have kernels of dimension
160-156=4 each. Its lifted source slice would consequently have rank at
most 13+4+4=21.

The rank gap forces every such lift to have rank 20. This would embed
the dimension-22 rank-one matrix variety into the dimension-eight
minimum-rank locus, which is impossible. Thus there is no ordinary
restriction A(4,5) -> M(12,12,13).

More generally, if l+h-2>a+b-1, the existence of an ordinary restriction
A(a,b) -> M(l,h,n) requires

    n(l+h-1) <= 2N-ab-a.                               (7)

The two cyclic versions hold when their corresponding dimension
conditions hold. Equality in (7) is not excluded: lifts can then reach
the first possible rank above the minimum.

This argument does not supply the rank estimates needed for singular
limits. A parameter-dependent sequence of nonzero slices can approach
the minimum locus with diverging coordinates in other maps. No claim
about such degenerations follows from the ordinary-map proof.

## Source

A. Grothendieck, *Sur la classification des fibres holomorphes sur la
sphere de Riemann*, American Journal of Mathematics 79(1), 1957,
121-138, Theorem 2.1, printed page 126. DOI: 10.2307/2372388.
[Primary article scan](https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG/AG-25.pdf).

A second agent in the same session checked the coefficient-map rank formula, removal
of the common homogeneous factor including the point at infinity, the
row and column spaces, the rank contribution after block row subtraction,
the GL2 normalization, and the dimension inequality. That review found no
required repair. Finite exact controls accompany the note; finite tests
and AI review do not constitute formal verification.
