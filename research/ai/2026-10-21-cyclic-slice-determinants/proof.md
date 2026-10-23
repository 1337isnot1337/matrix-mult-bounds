# Unimodular slices and reduced cyclic convolution determinants

October 21, 2026. Claims `AI-CYCLIC-UNIMODULAR-001` and
`AI-CYCLIC-REDUCED-DETERMINANTS-002` are local written proofs with exact
certificates, without independent mathematical review or formalization.
No tensor degeneration is excluded and no smaller exponent is established.

The selected question was whether a common factor of the full source
slice minors could supply a global determinant-divisor obstruction for
the open A4 to M(10,10,11) singular target. The required source divisor
does not exist. This does not rule out factors created after restricting
the first leg or selecting a singular leading flag.

## Source and results

Use the existing cyclic product A_a of the three oriented C(a,a)
convolution tensors. Its leg dimension is N=a^2(2a-1). In the maintained
[source convention](../2026-10-20-koszul/cyclic_finite_target.md), the slice
matrix has rows(j,p,L), columns(H,q,r), and entries

    M_a(F)[(j,p,L),(H,q,r)] = F(H-j,p+q,L-r),            (1)

where j,p,q,r are in{0,...,a-1}, H,L in{0,...,2a-2}, and out-of-range
short indices give zero. No new source identification is claimed.

For every a>=1, take the integer slice

    F0(i,k,s)=1 if i+s=a-1 and k=a-1; zero otherwise.   (2)

Then det M_a(F0) is plus or minus one. This gives an explicit full-rank
slice over every field, with only a nonzero first-leg coefficients.
The all-size conclusion is proved below, rather than extrapolated from
the finite controls.

For a=2,3,4, the full homogeneous polynomial

    D_a(F)=det M_a(F)

is reduced over C. Consequently, for each 1<=r<N, the collection of all
r-by-r minors of the full source matrix M_a(F) has no nonconstant common
polynomial divisor. These statements concern exactly these three sizes;
reducedness in every size is not proved.

At the same three sizes, two further normalized source slices have a
commutator of full rank N. Thus a uniform smaller commutator-rank bound
for this full normalized source space is also unavailable. Restrictions
and specially chosen slice subspaces remain outside that conclusion.

## All-size integer block proof

In(1)-(2), the middle indices satisfy q=a-1-p. Reorder by p and its
matching q. Up to row and column permutations, M_a(F0) is the direct sum
of a copies of a matrix K of dimension a(2a-1), with rows(j,L) and
columns(H,r). Its entry is one precisely when

    H+L-j-r=a-1,       0<=L-r<=a-1.                    (3)

Put t=L-j and u=H-r. Condition(3) forces u=a-1-t. Thus K splits further
into square blocks indexed by

    1-a <= t <= 2a-2.

Their row labels are those j in[0,a-1] for which 0<=t+j<=2a-2, and their
column labels are those r in[0,a-1] for which 0<=a-1-t+r<=2a-2. The block
entry is

    B_t(j,r)=1 when 0<=t+j-r<=a-1; zero otherwise.       (4)

For t<0, reindex j'=j+t. The matrix is lower triangular with every
diagonal entry one. For t>=a, reindex r'=r-(t-a+1). The matrix is upper
triangular with every diagonal entry one. Both cases have determinant one.

For 0<=t<=a-1, both index ranges are 0,...,a-1. Keep row 0 and replace each
row j>=1 by the original row j minus the original row j-1. This is a
unimodular row operation. The new rows are

    +e_(t+j),      1<=j<=a-1-t,
    -e_(t+j-a),    a-t<=j<=a-1.

They give signed unit pivots at every column except t. The remaining
row 0 has coefficient one at column t. Clearing its other columns leaves
a signed permutation matrix. Therefore det B_t is plus or minus one.

The block dimensions sum to a(2a-1), and all blocks have determinant
plus or minus one. The same is true of K and M_a(F0). This proves the
integer statement for every a>=1, including a=1. Reduction modulo any
characteristic preserves invertibility.

## Three exact reducedness witnesses

Each exported witness uses the same F0 in(2), prime 1009, and one explicitly
saved coefficient vector F1. Its integer entries are interpreted modulo
1009. The slices have dimensions 12,45,112 for a=2,3,4 respectively.
Their original generation used the deterministic seed 20261021+a; the
verifier reads all coefficients and does not depend on that seed.

Over F_1009 form

    A=M_a(F0)^(-1)*M_a(F1).

The saved vector v=e_0 is cyclic: the Krylov matrix

    K=[v,Av,...,A^(N-1)v]

has rank N. The certificate supplies a monic degree-N polynomial f such
that f(A)v=0. In the Krylov basis, A is its companion matrix, so f is
the characteristic polynomial. The constant coefficient of f is nonzero.
Finally, two saved polynomials satisfy the exact identity

    u*f + w*f' = 1 in F_1009[z].                       (5)

Thus f is squarefree. The determinant polynomial of the pencil is a
nonzero scalar times the reciprocal of f, with a possible change of
sign in its variable. It therefore is squarefree and has full degree N.
The verifier checks the matrix inverses, full Krylov rank, cyclic relation,
nonzero constant coefficient, and every coefficient of(5). It uses only
integer finite-field arithmetic. Numerical eigenvalues and characteristic
polynomial interpolation are not acceptance evidence.

Here is why the finite-field line proves the characteristic-zero claim.
The source determinant is a homogeneous integer polynomial of degree N,
and its value at F0 is plus or minus one. If it had a repeated factor over
C, it would also have a repeated rational factor, since characteristic
zero is perfect. Gauss's lemma then gives a primitive integer repeated
factor. Restrict that factorization to the integer line F0+z*F1 and reduce
modulo 1009. The determinant on this line still has degree N. Every factor
must therefore retain its full positive degree: a degree drop in one
factor cannot be compensated by any other factor. A repeated factor
would remain repeated on the finite-field line, contradicting(5).

This establishes reducedness for a=2,3,4. It does not establish
irreducibility, a simple spectrum at every point, or reducedness at all a.

## No global common divisor of submaximal minors

Fix one of those three sizes. Suppose an irreducible nonconstant h divided
every r-by-r minor, for some 1<=r<N. Laplace expansion implies that h also
divides every(N-1)-by-(N-1) minor and D_a. Each partial derivative of D_a
with respect to a source coefficient is a linear combination of those
cofactor minors, because M_a(F) is linear in F. Thus h divides D_a and
all its partial derivatives.

Over characteristic zero, a reduced polynomial has no irreducible factor
dividing both the polynomial and every partial derivative. Writing
D_a=h*g with h not dividing g, differentiating would force h to divide
every partial derivative of h, which is impossible for a nonconstant h.
This contradiction proves the claimed gcd statement.

The full source therefore does not supply the common source factor needed
for this particular divisor test. A compression, a restricted first-leg
space, or a singular initial map can create common factors. None of those
classes is excluded by this calculation. The M(10,10,11) construction and
the exponent goal remain open.

## A full normalized commutator

The certificate also supplies F2. With the same unimodular F0, form

    A=M_a(F0)^(-1)*M_a(F1),
    B=M_a(F0)^(-1)*M_a(F2).

The verifier checks that AB-BA is invertible modulo 1009 in each of the
three sizes. Because M_a(F0) is unimodular, both normalized matrices
have integer entries before reducing the supplied coefficient vectors.
Their commutator determinant is therefore a nonzero integer, as its
reduction is nonzero. The characteristic-zero rank is exactly N.

Full rank holds on a nonempty Zariski-open set of slice pairs at this
fixed normalization. Consequently no claimed uniform bound less than N
on these full-source normalized commutators can hold in these sizes.
This is a calibration of the full source, not an obstruction to a target
obtained from a compressed or singularly transformed slice space.

## Reproduction and attribution

From the repository root:

```sh
python research/ai/2026-10-21-cyclic-slice-determinants/certify.py --verify results/cyclic-slice-determinants-2026-10-21/certificate.json
python -m unittest discover -s tests -p test_cyclic_slice_determinants.py -v
```

Use `--output` in place of `--verify` to regenerate the witness file. The
root requirements suffice; neither NumPy nor SciPy is used by acceptance.
The finite controls check the interval proof for a=1,...,10, compare every
matrix entry with the prior literal source at a=2,3,4, replay all three
pencils, and reject corrupted cyclic relations, Bezout identities and scope.

The cyclic convolution source, its target and the existing minimum-rank
proof retain their original attribution. The block proof and finite
reducedness application are local rederivations without a historical
priority claim. Standard interval row operations, cyclic-vector linear
algebra, Gauss's lemma and the derivative criterion for reducedness are
used with the hypotheses stated above. The earlier semisimple determinant-
factor investigation motivated the question; its square-target obstruction
does not prove a result for this convolution source.
