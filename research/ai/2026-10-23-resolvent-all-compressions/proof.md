# Every constant compression in the fixed singular-unit resolvent

October 23, 2026. `AI-CYCLIC-SINGULAR-RESOLVENT-ALL-002` is a written,
unreviewed proof with an exact polynomial coefficient certificate.
It excludes one fixed ansatz, not general A4 degenerations or a smaller
matrix multiplication exponent.

## Statement and adopted predecessor

Use the normalized literal cyclic convolution source A4 from the
[pinned predecessor](../2026-10-21-singular-unit-resolvent/proof.md).
Its source dimension is 112. Let H(f)=M(F0)^(-1)M(f), where F0 has
coefficient one precisely at i+s=3, k=3. Put N=H(e_(0,0,0)).
Then N has rank 16 and N^2=0.

For every pair of constant complex maps P:C^112 -> C^110 and
C:C^110 -> C^112 with PC=I110, the exact resolvent ansatz

    B(t)=P(tI112+N)^(-1)

cannot degenerate A4 to M(10,10,11), even with arbitrary finite Laurent
first maps and arbitrary constant target bases. This removes the
predecessor's candidate-rank hypothesis for every such constant pair.
Moving compressions, corrections to the exact resolvent and other source
identity trajectories remain outside the statement.

The predecessor proves the following implication. Let V0 be the span of

    NH(f),  k>=3;       H(g),  k<3;       I112.            (1)

If its compressed image P V0 C has dimension 112, that image is the
entire limiting first-leg matrix space, including every Laurent first-map
order. A grading gives a proper invariant subspace of dimension in
{14,15,16,27,28,55,56,83,84}, excluding any row/column equivalent target
Mat10 tensor I11 by matrix-unit divisibility. We adopt that written
argument and its existing credits. Its exact nonzero minor also proves
that V0 itself has dimension 112: it has 113 displayed generators, with
one relation given by N. Thus it suffices here to prove that the map
X -> PXC is injective on V0 for every constant split pair PC=I110.

## Outer blocks of the literal source

Separate the four middle grades q=0,1,2,3, each of dimension 28.
For a 4-by-4 coefficient array F=(F_i,s), define a 28-by-28 matrix

    M_F[(j,L),(H,r)]=F_(H-j,L-r),                         (2)

with coefficients outside 0,...,3 set to zero, j,r in 0,...,3 and
H,L in 0,...,6. Let D=M_F0 for the outer coefficients F0_i,s=1 at i+s=3,
and put T(F)=D^(-1)M_F and S=T(e_00).
The maintained integer unit proof gives D invertible. The new verifier
checks an integer inverse in both orders; the full-source factorization
is also checked against every one of the 112 maintained coefficient slices.

Let E_d be the 4-by-4 shift sending grade q to q+d when both are in range.
The literal relation p+q=k gives

    H(F at middle k)=E_(3-k) tensor T(F),
    N=E_3 tensor S.                                     (3)

In particular each high-middle generator NH(F at k), k=3,4,5,6,
has just its bottom block row nonzero, with block S T(F) in column k-3.
The low-middle terms at k=2,1,0 have T(G) on the first, second and third
strict lower block diagonals, respectively. The identity adds the same
scalar multiple of I28 to every diagonal block.

## Two outer rank facts

For every nonzero F,

    rank T(F)>=16,                                      (4)

with equality only if F_i,s=alpha_i beta_s is separable. Here is a
self-contained equality argument, also proving the bound. Write
F_i(y)=sum_s F_i,s y^s. Matrix (2) sends seven input polynomials u_H(y)
of degree at most three to the four polynomials

    sum_i F_i(y) u_(i+j)(y),        j=0,1,2,3.

Over C(y), the four rows are independent: they represent the four
polynomials x^j sum_i F_i(y)x^i, and polynomial multiplication has no
zero divisors. Their rational kernel has dimension three.
Let K_d be its polynomial vectors of degree at most d. The leading
coefficient map K_d/K_(d-1) has dimension at most three. Otherwise four
vectors with independent leading coefficients would be independent over
C(y), by comparing the highest degree in a cleared-denominator relation.
Consequently dim K_3<=12 and (4) follows by nullity.

If rank is 16, every one of the four degree increments is three, so
K_0 has dimension three. Each nonzero coefficient Toeplitz matrix has
rank four and must have exactly this constant kernel. Its row space is
f_s(x) times the polynomials of degree at most three, where
f_s(x)=sum_i F_i,s x^i. These row spaces are equal for every nonzero f_s.
Equality forces those polynomials proportional: each divides the other,
since each belongs to the other's row space. Thus F is separable.
Conversely a nonzero separable F has rank 4*4=16.

The second fact, needed for the high blocks, is

    rank(S T(F))>=5 for every nonzero F.                 (5)

Indeed rank S=16. If rank T(F)>=17, the elementary product rank bound
16+17-28 proves (5). In the remaining case F=alpha(x) beta(y), the
image of M_F is C^4 tensor beta(y) P_3, of dimension 16.
The kernel of S is the twelve-dimensional coordinate space K with H>=4,
since D is invertible and M_e00 selects H=j, L=r. If rank(S T(F))<=4,
the product rank bound is equality and K is contained in im T(F).
Equivalently D K is contained in im M_F.

The input coordinate (H,r)=(6,0) lies in K and D sends it to the single
output (j,L)=(3,0). Thus beta(y) divides 1 and is constant. But the
coordinate (H,r)=(5,3) is sent by D to the sum of (j,L)=(2,3) and (3,4).
This has a nonzero degree-four term, which is outside C^4 tensor P_3.
That contradiction proves (5). No rank classification is inferred from
sampled coefficient arrays.

## A split compression of a square-zero matrix

For any X with X^2=0 and PC=I on a codimension-k split compression,

    PXC=0  implies  rank X<=k.                          (6)

Write W=im C and K=ker P, so the source is W direct sum K. Put U=XW.
Then U is contained in K, and XU=0. Hence
rank(X restricted to K)<=k-dim U. Since im X=XW+XK,
rank X<=dim U+k-dim U=k. This argument uses the split identity PC=I.
It is stronger here than the unrestricted two-projection rank-loss bound.

## Reduction of a possible kernel to nineteen parameters

Suppose a nonzero X in V0 satisfies PXC=0. Deleting two dimensions on
each side gives rank X<=4. In its block form (3), the scalar identity
coefficient must vanish: its top diagonal block otherwise has rank 28.
The low k=2 coefficient must vanish by (4), using block (1,0), and then
the low k=1 coefficient vanishes by block (2,0). Thus X has only its
bottom block row left.

In columns 1,2,3, each remaining block is S T(F). Bound (5) forces all
three to vanish, because every submatrix has rank at most rank X<=4.
Only block (3,0) can remain. It has the form

    Z=T(G)+S T(F).                                      (7)

Now X^2=0, so (6) improves the bound to rank Z=rank X<=2.
Multiplying (7) by D gives M_G+M_e00 T(F). The second summand has no
output rows with L>=4. If some coefficient polynomial
G_d(x)=sum_i G_i,d x^i is nonzero for d>=1, choose the four rows
(j,L)=(j,3+d) and the seven columns (H,r)=(H,3). Their matrix is the
four-row Toeplitz matrix G_d(H-j), which has rank four. All those rows
are outside the second summand. This contradicts rank Z<=2.
Therefore G has only s=0 coefficients.

Since T(e_00)=S=S T(F0), its constant G coefficient can be absorbed into
F. The only remaining matrix space in (7) is

    S T(F)+g1 T(e_10)+g2 T(e_20)+g3 T(e_30),             (8)

with nineteen scalar parameters. The following exact certificate proves
that a nonzero member of (8) has rank at least three. It follows that
Z=0, hence X=0, a contradiction. Compression is injective on V0 for every
constant split pair, proving the statement via the predecessor.

## Exact cubic certificate over the complex numbers

Left multiply (8) by D and retain its sixteen possibly nonzero output
rows (j,L) with j,L in 0,...,3. This is a 16-by-28 matrix of integer
linear forms in nineteen parameters. Its homogeneous cubic polynomial
space has dimension binomial(21,3)=1330.

The certificate lists 1330 actual 3-by-3 minors. The standard-library
verifier reconstructs the integer source normalization and the specified
linear matrix, expands each determinant polynomial modulo two, and
checks that their coefficient vectors are independent in all 1330 cubic
monomials. It does not accept a recorded rank or a numerical tolerance.
This is an odd integer coefficient determinant. Thus the same minors span
all homogeneous cubics over Q and over C. If the matrix had rank at most
two, all those minors would vanish, and so would the cube of each of the
nineteen parameters. Over C every parameter would be zero. This proves
the claimed rank gap for arbitrary complex parameters, rather than
extrapolating from a finite field's set of rational points.

The seeded binary discovery pilot found the selected minors after 90,398
samples. Acceptance checks only the exported minors and their full
coefficient span. The earlier 6,216 coordinate-deletion witnesses are
preserved outside the repository as discovery; the present theorem
supersedes that restricted continuation.

The polynomial certificate does not formalize the written kernel,
compression, flat-limit or invariant-subspace arguments. Those arguments
remain unreviewed. Their conjunction excludes the exact fixed resolvent
for constant P,C only. No target construction or exponent gain is claimed.
