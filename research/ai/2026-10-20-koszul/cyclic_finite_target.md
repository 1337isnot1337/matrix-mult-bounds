# A smaller finite target and its constant-map obstruction

October 20, 2026. AI-derived conditional implication and written proof,
unreviewed. **No improved exponent or target degeneration is established.**
This follows the [finite profile criterion](finite_amplitude.md) and the
[coordinate and Laurent-output screens](finite_target_screens.md).

## 1. Reduce the construction to leg dimension 112

Let C=C(a,a), and define

    A_a = C tensor C^cyclic tensor C^(cyclic squared),
    d_a = a^2(2a-1).

Each leg has dimension d_a. Since C is invariant under exchanging its two
short legs, A_a is isomorphic to every permutation of its three legs,
S_a is isomorphic to A_a squared, and

    lambda(A_a)=P(a,a)^(3t).                              (1)

If A_a degenerates to M(l,h,n), its leg symmetry gives the same statement
for every permutation of the target. Multiply the character inequalities
and take their geometric mean. The matrix character parameters sum to 3t,
so even when the individual parameters are unequal,

    lambda(A_a) >= (l*h*n)^t,
    P(a,a) >= (l*h*n)^(1/3).                              (2)

Combined with the existing 6P(a,a)<=(6a-2)^(1/t), this would give

    omega <= 9 log(6a-2)/log(216*l*h*n).                   (3)

In particular consider the new finite premise

> A_4 degenerates over C to M(10,10,11).                  (H1100)

The source legs have dimension 112; the target legs have dimensions
100,110,110. The source has border rank at most 7^3=343. This premise
would imply the descriptive bound omega<=2.247423596, and the exact
rational bound omega<=281/125=2.248, certified by

    237600^281 > 22^1125,  where 237600=216*1100.          (4)

The target is unconstructed. H1100 is a different sufficient premise from
S_4 to M106; tensoring H1100 gives rectangular matrix products rather than
that exact square target. No equivalence of the two premises is claimed.

Among sorted shapes 2<=l<=h<=n with h*n<=112, the only shape for which
(3) beats 9/4 is (10,10,11). This is a small finite frontier: since h>=l,
l,h<=floor(sqrt(112))=10. If l<=9 then l*h*n<=9*112=1008,
whereas improvement requires 216*l*h*n>22^4=234256. Thus l=h=10;
n is either 10 or 11, and only 11 passes. The maintained code also
enumerates this frontier and all sorted candidates through a=6.

## 2. Exact minimum nonzero slice rank

For every a>=1, the minimum rank of a nonzero slice of A_a on any leg is

    minrank(A_a)=a^2.                                    (5)

Here this means ordinary matrix rank after contracting one tensor leg;
it is not the tensor's slice rank invariant. The same value on each leg
follows from the leg symmetry. The proof below works over any field.

Write the three factors as

    X_i Y_j Z_(i+j),  Y_p Z_q X_(p+q),  Z_r X_s Y_(r+s),

with i,j,p,q,r,s in {0,...,a-1}. A first-leg slice is specified by
F_(i,k,s), with 0<=k<=2a-2. Its matrix has rows (j,p,L), columns (H,q,r),
and coefficient

    F_(H-j,p+q,L-r),                                    (6)

where coefficients outside the two short index ranges are zero.
Choose k0 such that f_(i,s)=F_(i,k0,s) is not zero. Choose p0,q0 in
{0,...,a-1} with p0+q0=k0. Fix p=p0,q=q0 in the matrix. Let i0 be the
largest first index with a nonzero coefficient in f, and s0 the largest
second index with f_(i0,s0)!=0.

Take the a^2 rows (j,p0,r'+s0), with j,r' in {0,...,a-1}, and a^2
columns (j'+i0,q0,r), with j',r in that range. All indices are available.
The resulting entry is

    f_(i0+j'-j,s0+r'-r).

In increasing j,j' order this matrix is block lower triangular, since
j'>j makes the first argument exceed i0. Each diagonal block is upper
triangular in r',r, since r'>r makes its second argument exceed s0.
Every diagonal entry is f_(i0,s0). Its determinant is therefore
f_(i0,s0)^(a^2), proving the lower bound in (5). For equality take F
supported only at (i,k,s)=(0,0,0). Equation (6) then has exactly a^2
nonzero entries in distinct rows and columns, so its rank is a^2.

This is an elementary structured-matrix calculation, with no priority
claim. It does not invoke a numerical minimum-rank search.

## 3. Constant linear maps cannot supply H1100

For a constant linear restriction A_a to M(l,h,n), all target legs are
concise, so each leg map has full row rank. Contract a rank-one matrix
parameter on the target leg of dimension l*h. The target slice rank is n.
Its lifted source parameter is nonzero; its source slice has rank at
least a^2. The other two maps lose at most their kernel dimensions
d_a-h*n and d_a-n*l. Consequently

    n >= a^2-(d_a-h*n)-(d_a-n*l),
    n(l+h-1) <= 2d_a-a^2.                               (7)

Cycling the target legs gives the other two necessary inequalities.
For H1100, a=4 and d_a=112, while

    11(10+10-1)=209 > 2*112-16=208.

Thus H1100 is impossible by arbitrary constant linear maps, including
dense input mixing. Equivalently, the two 110-dimensional maps each lose
at most rank two, leaving every nonzero source slice with rank at least
12; the target has rank-11 slices. This is a one-rank-unit contradiction.

This is **not** an obstruction to arbitrary degeneration: matrix rank can
drop at a singular limit. It directs a search for H1100 toward genuinely
parameter-dependent maps. The earlier Laurent-output theorem also excludes
coordinate inputs with arbitrary Laurent output, since

    10*(3*110-2*112)=1060 > 7^3=343.

At a=5, five of the seven improving sorted shapes pass (7), including
(13,13,17). The next section excludes that equality case as well. Four
shapes still pass these screens; passing is not a construction.

## 4. Classify the minimum-rank slices and remove one equality case

Over C, for a>=2 the affine cone of slices of rank at most a^2 is exactly

    F_(i,k,s)=u_i h_k v_s, with rank(H(h))<=1,
    H(h)_(p,q)=h_(p+q),  0<=p,q<a.                     (8)

Its dimension is 2a; its projectivization has dimension 2a-1. Zero is
included in the cone. The rank-one Hankel factors form the rational normal
curve h_k=alpha^(2a-2-k)*beta^k, with arbitrary scalar absorbed into u.
We prove the classification rather than infer it from finite ranks.

First, for a nonzero biform f_(i,s), let R(f) be the matrix with rows
(H,r), columns (j,L), and entry f_(H-j,L-r). This is the transpose, up to
ordering, of the fixed-p,q submatrix in Section 2. Set D=a-1 and
f_i(z)=sum_s f_(i,s) z^s. Let H_i be the a by (2a-1) matrix whose rows
are the coefficient vectors of z^r f_i(z), r=0,...,D. The matrix R(f)
is the degree-D polynomial multiplication map associated with
H(x)=sum_i H_i x^i. Its kernel consists of vector polynomials y(x) of
degree at most D satisfying H(x)y(x)=0 identically.

For all but finitely many x, H(x) has rank a: its rows are the multiples
of one nonzero polynomial by 1,z,...,z^D, and are independent. Choose a
distinct such x-values. Evaluation injects ker R(f) into the direct sum
of their a nullspaces, each of dimension D. If rank R(f)=a^2, both spaces
have dimension aD, so evaluation is surjective. Fix a vector v in one
node's nullspace and prescribe zero at the other nodes. Its unique
interpolating vector polynomial is L(x)v for a scalar Lagrange polynomial.
Since H(x)L(x)v=0 identically, H(x)v=0 identically. Hence H(x) has a common
D-dimensional kernel, and all nonzero H_i have the same row space.

That row space is f_i(z) times the space of polynomials of degree at most
D. Equality of two such spaces implies their polynomial gcds agree up to
scalar, so all nonzero f_i are proportional. Thus

    rank R(f)=a^2 if and only if f_(i,s)=u_i v_s.         (9)

The converse also follows directly as a tensor product of two full-rank
polynomial-multiplication matrices.

Now arrange the full slice as the a by a block Hankel matrix with blocks
R(F_k), where (F_k)_(i,s)=F_(i,k,s). We may arrange F_0!=0: a GL2 change
of variables in the convolution factor supplying the long first-leg
coordinate preserves full slice rank and acts on that factor by its
degree-2D representation. The pure powers span this representation, so
some such change gives a nonzero extreme-coordinate slice. This is the
usual change of variables for binary polynomial multiplication, not an
arbitrary change of the Hankel structure.

If the full matrix has rank a^2, its block R(F_0) already has that rank.
For p<=D, both the first block row and the first block column contain
R(F_p); their ranks cannot exceed a^2. Each nonzero F_p is separable by
(9). Its row and column spaces must equal those of R(F_0). For a separable
f=u v, these spaces are, respectively, a full a-dimensional factor times
v*S_D and u*S_D times a full factor. Their equality forces both polynomial
factors to be proportional. Consequently R(F_p)=c_p R(F_0), with c_0=1.

Choose a generalized inverse G of R(F_0). Since the whole block matrix
has rank a^2, every Schur residual vanishes, giving

    R(F_(p+q))=R(F_p) G R(F_q)=c_p c_q R(F_0).

Injectivity of f to R(f) makes all F_k scalar multiples of F_0 and their
scalar Hankel matrix rank one. Undoing the GL2 change preserves that
rank-one Hankel property. This proves (8). Its projective variety is
the product P^(a-1) times P^1 times P^(a-1), embedded by a Segre map with
a degree-2D Veronese on the middle factor, giving the stated dimension.

Apply this to a hypothetical constant restriction A_5 to M(13,13,17).
The other two leg maps have target dimension 221 and kernel dimension
four each. Every target rank-one first-leg parameter has slice rank 17,
so its lifted source slice has rank at most 17+4+4=25. The first dual map
is injective by conciseness. It therefore embeds the rank-one parameter
variety P^12 times P^12, of dimension 24, into the projective minimum-rank
locus of A_5, of dimension 9. This is impossible. This additional
constant-restriction obstruction still does not exclude degeneration.

## Exact controls and limitations

`cyclic_finite_target.py` implements (6), the exhibited triangular minor,
the finite sorted-shape frontier, and the integer exponent certificate.
It independently computes the ranks of all 4095 nonzero slices at a=2
over F2 and checks the proposed minor for each. Its 27 minimum-rank slices
are exactly the 27 products in (8) over F2, checked as sets. Seeded integer slices at
a=3,...,8 also check the zero pattern and diagonal of the exhibited minor.
The F2 run is a finite characteristic-two control of the algebraic rank
formula, not a characteristic-zero degeneration search. No existence
claim, complete Laurent search, independent review or formalization follows.
