# No ordinary restriction from Q(3,2) to M(3,2,3)

**Status: written proof, with a same-session audit by a second agent and
exact local coefficient controls; no external mathematical review.** This
concerns ordinary linear restrictions over the complex numbers. It does not
exclude a Laurent degeneration with singular changes of basis and does not
improve an exponent.

## Statement

Let

\[
Q_{3,2}=\sum_{p,q=0}^{2}\sum_{y,v=0}^{1}
A_{p,q}B_{y,q+v}C_{p+y,v},
\]

of format `(9,8,8)`. There are no three ordinary linear maps taking this
tensor to

\[
M(3,2,3)=\sum_{i,k=0}^{2}\sum_{j=0}^{1}a_{i,k}b_{i,j}c_{j,k},
\]

of format `(9,6,6)`.

The argument has two parts. A kernel meeting a polynomial divisor subspace
is forced into one of two explicit forms, each incompatible with matrix
multiplication. If both kernels avoid these subspaces, projective
intersection gives the contradiction instead.

## 1. Reduction to two two-dimensional kernels

Suppose such maps existed. The target is concise in all three factors, so
the A-side map is invertible and the B- and C-side maps are surjective.
Consequently the latter have kernels `K_B` and `K_C` of dimension two.
After taking these quotients, the nine-dimensional slice space would be
equivalent under invertible left and right matrix transformations to

\[
\{X\otimes I_2:X\in\operatorname{Mat}_3(\mathbb C)\}.
\tag{1}
\]

In particular every slice rank would be even. The induced identification of
slice parameters is an invertible linear map
`L:Mat3→Mat3`; a quotient slice of rank `2r` corresponds to a matrix `L(a)`
of rank `r`.

Use homogeneous binary polynomials to include roots at infinity. Put
`V=Sym¹(C²)` and `P_d=Sym^d(C²)`. The two long source factors have the forms
`U⊗P_3` and `P_3⊗U'`, with `dim U=dim U'=2`.

For nonzero quadratics `f,g∈P_2`, contraction by the pure A-parameter
`f⊗g` has B-image and C-image

\[
E_g=U\otimes gV,\qquad F_f=fV\otimes U'.
\tag{2}
\]

Both have dimension four. More explicitly, if `f_p,g_q` are their
coefficients, this slice is

\[
\sum_{y,v=0}^{1}
\left(\sum_{q=0}^{2}g_qB_{y,q+v}\right)
\left(\sum_{p=0}^{2}f_pC_{p+y,v}\right).
\tag{3}
\]

Each displayed family of four vectors is linearly independent because
multiplication by a nonzero binary polynomial is injective. Thus the slice
has rank exactly four before either quotient.

## 2. A one-dimensional intersection would create an odd slice rank

For any fixed two-dimensional `K⊂U⊗P_3`, consider the incidence

\[
\mathcal I_K=\{([k],[g])\in\mathbf P(K)\times\mathbf P(P_2):
k\in U\otimes gV\}.
\]

For a fixed nonzero `k`, its two cubic components have only finitely many
common quadratic divisors, up to scalar. At least one component is nonzero,
and any such divisor divides that fixed nonzero cubic. It follows that
`dim I_K≤1`. Its image in the two-dimensional projective space `P(P_2)`
is therefore a proper closed subset. In particular `K∩E_g=0` for generic g.
The same conclusion holds on the C side for generic f.

Suppose now that `dim(K_B∩E_g)=1` for some g. Choose f with
`K_C∩F_f=0`. In (3), the quotient of the four B-vectors has rank three,
whereas the quotient of the four C-vectors still has rank four. The product
therefore has rank three. This contradicts (1). Interchanging B and C gives
the symmetric statement.

We have proved the following necessary condition for each kernel:

\[
\dim\bigl(K\cap(U\otimes gV)\bigr)\in\{0,2\}
\quad\text{for every nonzero }g\in P_2.
\tag{4}
\]

This is a statement about all complex quadratic divisors, including
multiple roots.

## 3. Classification when the kernel meets a divisor subspace

**Lemma.** If a two-dimensional `K⊂U⊗P_3` satisfies (4) and meets at least
one divisor subspace, it has one of the following forms after invertible
changes of bases in U and the binary variables:

\[
K=U\otimes\langle h\rangle
\quad\text{for a nonzero cubic }h,
\tag{5}
\]

or

\[
K=\langle u_0\ell^3,\ u_0\ell^2m+u_1\ell^3\rangle,
\tag{6}
\]

where `(u0,u1)` and `(ell,m)` are bases.

**Proof.** By (4), some quadratic g divides every element of K. Write
`K=gH` with a two-dimensional subspace `H⊂U⊗V`, viewed as a pencil of
two-by-two matrices. Its determinant is a homogeneous quadratic on `P(H)`;
over C it has a zero, so H contains a nonzero rank-one matrix `u⊗ell`.

The corresponding vector of K has both components proportional to the cubic
`h=g ell`. If h is not a cube of one linear form, it has a second quadratic
divisor `g'` not proportional to g. Condition (4) forces

\[
K\subseteq U\otimes(gV\cap g'V)=U\otimes\langle h\rangle.
\]

Both spaces have dimension two, proving (5).

For completeness, if the determinant vanishes identically on H, every
member has rank one. A two-dimensional rank-one matrix pencil has either
a common U-factor or a common V-factor: otherwise the sum of two members
with both pairs of factors independent has rank two. A common V-factor
gives `H=U⊗ell` and hence (5). A common U-factor gives `H=u⊗V`.
The two-dimensional space `gV` contains a cubic that is not a pure cube,
so the preceding alternative-divisor argument again forces (5),
contradicting a common U-factor. Thus the identically-zero case introduces
no additional kernel type.

Assume (5) does not occur. Every rank-one member of H must then give a pure
cube, so `g=ell²` for a fixed line ell and every rank-one member has its
V-factor on that line. Two independent such members would again give (5).
There is therefore exactly one projective rank-one member of H. The
determinant pencil is nonzero and has a double zero there.

Choose bases so that this member is `u0 ell`, represented by `E00`, and
write a second member as `[[a,b],[c,d]]`. The determinant of their pencil is
`alpha beta d + beta²(ad-bc)`. A double zero at `beta=0` forces `d=0` and
`bc≠0`. Subtracting a multiple of `E00` and rescaling the second basis
vectors puts H in the form
`span(u0 ell, u0 m+u1 ell)`. Multiplication by `ell²` gives (6). ∎

The allowed changes really are source symmetries. The source is the product
of the two binary multiplication tensors
`P_2⊗P_1→P_3`, with their output factors placed on opposite long legs.
The group `GL2×GL2` acts on these polynomial multiplication tensors. On B,
one group acts on the two-dimensional U factor and the other acts by the
cubic polynomial representation; the corresponding changes on A and C are
invertible as well. Thus putting one kernel into (5) or (6) does not impose
an extra restriction on the other kernel.

## 4. A fixed-image fibre in matrix multiplication

We use the following elementary property of (1).

**Fibre lemma.** Suppose a three-dimensional subspace of its slice
parameters has all images contained in a fixed two-dimensional subspace
`B0⊂B`. Then its nonzero slices have rank two, its combined C-span is six,
and it can be written

\[
S_p=b_0c_{p,0}+b_1c_{p,1},\qquad p=0,1,2,
\tag{7}
\]

where the six C-vectors form a basis. For every other slice S, restriction
of its map `C*→B` to each paired dual subspace
`span(c_(p,0)*,c_(p,1)*)` has rank either zero or two.

**Proof.** In (1), slice images are `im(X)⊗C²`. Nonzero slices with image
inside B0 therefore correspond to rank-one matrices with the same image
line. The three-dimensional parameter space is exactly all rank-one
matrices on that fixed line and an arbitrary three-dimensional row vector.
It is a full matrix row or column fibre, according to conventions. Its
C-vectors span `C³⊗C²`, giving (7). A general slice on one paired dual
subspace is a single matrix column tensored with `I2`, and so has rank zero
or two. This conclusion is unchanged by the common invertible changes of
B and C bases. ∎

Equivalently, the elementary rank-one-space fact used here follows from
`rank(uvᵀ+u'v'ᵀ)=2` whenever both pairs of factors are independent.

## 5. Uniform cubic kernels are impossible

Suppose `K_B=U⊗h`. Choose a linear divisor ell of h and set `g=h/ell`.
Then `K_B⊂E_g`, and the quotient of E_g has dimension two. For every
nonzero f the quotient slice has image in this fixed two-dimensional
B-subspace. Under the assumed matrix-multiplication equivalence, the
three-dimensional f-fibre satisfies the fibre lemma and must have combined
C-span six.

However `E_g/K_B` is

\[
U\otimes(gV/\langle h\rangle)\cong U\otimes(V/\langle\ell\rangle).
\]

The second factor is one-dimensional. In (3), the v-dependence on B is
therefore a single covector, independent of f and y. The combined C-span
before the C quotient is contained in

\[
P_3\otimes\langle v_0\rangle
\]

for a fixed vector `v0∈U'`, and has dimension at most four. A C quotient
cannot increase this dimension. This contradicts the fibre lemma.

The same argument excludes a uniform cubic kernel on C.

## 6. Tangent-jet kernels are impossible

By the source symmetries, a kernel of the second type on B can be written

\[
K_B=\langle B_{0,0},\ B_{0,1}+B_{1,0}\rangle.
\tag{8}
\]

In the quotient write

\[
b_0=B_{0,1},\ b_1=B_{1,1},\ b_2=B_{0,2},\ b_3=B_{1,2},
\ b_4=B_{0,3},\ b_5=B_{1,3}.
\]

These are a basis, with `B00=0` and `B10=-b0`. Define the following C-vectors
after the arbitrary C quotient:

\[
c_{p,0}=C_{p,1}-C_{p+1,0},\qquad
c_{p,1}=C_{p+1,1}\qquad(0\le p\le2).
\tag{9}
\]

The q=0 slices are exactly

\[
S(A_{p,0})=b_0c_{p,0}+b_1c_{p,1}.
\]

Under the assumed equivalence, the fibre lemma implies that the six vectors
in (9) are a basis of C. In particular no unspecified C quotient or A
change of basis may destroy their pairing structure.

Now expand one further source slice, without making any choice for the
other kernel:

\[
\begin{aligned}
S(A_{2,1})
 &=b_0C_{2,0}+b_2C_{2,1}+b_1C_{3,0}+b_3C_{3,1}\\
 &=b_0(c_{0,1}-c_{1,0})+b_2c_{1,1}
   +b_1(c_{1,1}-c_{2,0})+b_3c_{2,1}.
\end{aligned}
\tag{10}
\]

Its two columns on the paired dual subspace
`span(c_(0,0)*,c_(0,1)*)` are precisely

\[
\begin{pmatrix}0&1\\0&0\\0&0\\0&0\\0&0\\0&0\end{pmatrix},
\]

of rank one. The fibre lemma requires rank zero or two. This contradiction
is independent of every coefficient of the C quotient. By transposing the
source, a tangent-jet kernel on C is also impossible.

## 7. The case where both kernels avoid the divisor subspaces

The preceding steps exclude every kernel satisfying (4) that meets any
divisor subspace. Hence the hypothetical ordinary restriction would have
to satisfy

\[
K_B\cap E_g=0,\qquad K_C\cap F_f=0
\quad\text{for every nonzero }f,g\in P_2.
\]

Every pure A-slice in (3) would then retain rank exactly four. Under the
invertible parameter map L, all matrices `L(f⊗g)` would have rank exactly
two.

The projective pure-parameter locus is the Segre variety

\[
\Sigma=\mathbf P^2\times\mathbf P^2\subset\mathbf P^8,
\qquad\dim\Sigma=4.
\]

Its image `L(Sigma)` is a closed projective fourfold, as is the target
rank-one Segre variety. Two nonempty closed projective varieties of
dimensions 4 and 4 in `P8` must intersect. The precise external result is
[Stacks Project, Lemma 33.34.3, tag 0B2R](https://stacks.math.columbia.edu/tag/0B2R),
whose hypotheses are closed nonempty subsets of projective space and
`dim X+dim Y≥dim P`. Applying it gives a nonzero pure parameter with
`rank L(f⊗g)=1`, contradicting the rank-exactly-two conclusion.

All possible kernels have now been excluded. This proves the statement. ∎

## Verification and limits

The companion `narrow_kernel_controls.py` checks the small integer matrices
in the uniform-cubic and tangent-jet arguments. The latter check makes an
invertible coordinate change on the entire original C space, retaining two
extra free coordinates. Equation (10) has no coefficient on either extra
coordinate, so the rank-one block is independent of their eventual images
under a C quotient. The exact controls also verify the same local jet
contradiction for n=3 through 8; the theorem above is stated only for n=3.

```sh
python research/ai/2026-10-20-paired-construction/narrow_kernel_controls.py --output research/ai/2026-10-20-paired-construction/narrow-kernel-controls.json
python -m unittest discover -s tests -p test_narrow_kernel_controls.py -v
```

The finite checks do not replace the incidence-dimension, pencil
classification, or projective-intersection arguments. The final Segre
dimension comparison is specific to n=3. No exclusion of singular Laurent
degenerations follows from this proof: a singular A-side limit need not
induce the invertible parameter map L used throughout.
