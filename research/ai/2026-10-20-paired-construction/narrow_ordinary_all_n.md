# Ordinary restrictions for all Q(n,2), and wider-kernel conditions

**Status: written proof with a same-session audit by a second agent; no
external mathematical review.** The conclusion is an obstruction to ordinary
linear restrictions over C. No singular degeneration is excluded and no
matrix multiplication exponent is improved.

## 1. The all-n ordinary obstruction

For every integer n at least 3, there is no ordinary restriction

\[
Q_{n,2}=\sum_{p,q=0}^{n-1}\sum_{y,v=0}^{1}
A_{p,q}B_{y,q+v}C_{p+y,v}
\quad\longrightarrow\quad M(n,2,n).
\tag{1}
\]

The source has format `(n²,2(n+1),2(n+1))` and the target has format
`(n²,2n,2n)`. Thus a hypothetical restriction again has an invertible A
map and two-dimensional kernels on each long leg.

The n=3 proof is written separately in `narrow_ordinary_obstruction.md`.
Here are the changes needed for every larger n.

### Divisor incidence and the kernel normal forms

Use `P_d=Sym^d(C²)`. A pure A parameter `f⊗g`, with both forms of degree
`n−1`, still gives a slice of rank four. Its two images are

\[
E_g=U\otimes gP_1,\qquad F_f=fP_1\otimes U',
\]

inside `U⊗P_n` and `P_n⊗U'`, respectively. For a fixed nonzero vector in a
kernel, its nonzero polynomial components have only finitely many divisors
of degree `n−1`. Hence the incidence over `P(K)=P¹` has dimension at most
one. Since `P(P_(n−1))` has dimension `n−1≥2`, a generic divisor space
avoids each kernel. The odd-rank argument therefore gives

\[
\dim(K\cap E_g)\in\{0,2\}\quad\hbox{for every }g\ne0.
\tag{2}
\]

If K meets a divisor space, write `K=gH`, where H is a two-dimensional
pencil of two-by-two matrices. A rank-one member gives a polynomial
`h=g ell` of degree n. Unless h is a pure n-th power, it has another divisor
of degree `n−1`. Equation (2) then forces

\[
K=U\otimes\langle h\rangle.
\tag{3}
\]

The only remaining pencil has a single double rank-one point. The same
two-by-two determinant calculation gives

\[
K=\langle u_0\ell^n,\ u_0\ell^{n-1}m+u_1\ell^n\rangle.
\tag{4}
\]

Pencils whose determinant vanishes identically are dealt with exactly as
in the n=3 proof: a common polynomial factor gives (3), while a common U
factor contains a polynomial that is not a pure power and triggers the
alternative-divisor argument. No new type occurs when n increases.

### Both normal forms remain impossible

For (3), choose a linear factor ell of h and set `g=h/ell`. The fixed-g
fibre is n-dimensional and its B image lies in a two-dimensional space.
In `Mat_n⊗I_2`, such a fibre must be a complete rank-one matrix fibre; its
combined C support has dimension `2n`. In the quotient of the source, its
C support has dimension at most `n+1`. Since `n+1<2n`, this is impossible.

For (4), the source symmetries normalize the kernel to
`span(B00,B01+B10)`. Put `b_(2(j−1)+y)=B_yj` for `j≥1`, with
`B00=0` and `B10=−b0`. The entire fixed-q=0 fibre is

\[
S(A_{p,0})=b_0c_{p,0}+b_1c_{p,1},\qquad
c_{p,0}=C_{p,1}-C_{p+1,0},\quad c_{p,1}=C_{p+1,1}.
\]

The fibre lemma now forces all `2n` C vectors to be a basis, with n paired
two-dimensional dual blocks. Because n is at least three, the slice A21
exists and retains the same exact identity

\[
S(A_{2,1})=b_0(c_{0,1}-c_{1,0})+b_2c_{1,1}
 +b_1(c_{1,1}-c_{2,0})+b_3c_{2,1}.
\]

Its restriction to the first dual block has rank one, whereas every
`Mat_n⊗I_2` slice has rank zero or two there. This excludes (4), on either
long leg. The control script `narrow_kernel_controls.py` verifies all the
integer identities for n=3 through 8, retaining both free C coordinates.
The formula itself supplies the proof for all n.

### The avoiding case and the constant-rank theorem

It remains to exclude two kernels that avoid every divisor space. Fix any
nonzero g. As f varies, the quotient slices form an n-dimensional linear
space whose every nonzero element has rank exactly four. Under the assumed
matrix multiplication equivalence, this would give an n-dimensional
linear subspace of `Mat_n(C)` of constant rank two.

The external theorem used here is
[Ellia–Menegatti, arXiv:1508.00209v1, Proposition 8](https://arxiv.org/html/1508.00209v1).
For an algebraically closed field of characteristic zero, let `l(r;a)` be
the largest dimension of an `a×a` linear matrix space whose every nonzero
element has rank r. The proposition proves

\[
l(r;a)\le\max\{r+1,a-r+1\},
\qquad l(r;a)=a-r+1\quad(a\ge2r).
\tag{5}
\]

With `r=2`, `a=n≥4`, it gives `l(2;n)=n−1`, a contradiction.
The n=3 avoiding case is already covered by projective intersection in
the separate proof. This establishes (1) for every n at least three. ∎

The external theorem is a proved result, not a uniform-bundle conjecture
appearing elsewhere in the same paper. Its field and dimension hypotheses
are satisfied here. The paper gives a proof of Proposition 8 and attributes
the original bound to Beasley.

## 2. Necessary conditions for wider sources

The following statements are partial conditions, not a claimed obstruction
for `m≥3`.

Take integers `m≥2` and n, and write

\[
Q_{n,m}=\sum_{p,q<n}\sum_{y,v<m}
A_{p,q}B_{y,q+v}C_{p+y,v}.
\]

An ordinary restriction to `M(n,m,n)` would have long-leg kernels of
dimension

\[
k=m(m-1).
\]

For degree-`n−1` binary forms f,g, a pure source slice has rank `m²`, with
images

\[
E_g=U_m\otimes gP_{m-1},\qquad F_f=fP_{m-1}\otimes U'_m.
\]

Assume `n>k`. The divisor-incidence argument bounds the defective parameter
locus for each kernel by `k−1<n−1`, so the other kernel can be avoided by
a generic opposite parameter. Since every matrix multiplication slice has
rank divisible by m, necessarily

\[
\dim(K_B\cap E_g)\equiv0\pmod m,
\qquad
\dim(K_C\cap F_f)\equiv0\pmod m
\quad\hbox{for all nonzero }f,g.
\tag{6}
\]

Neither kernel can avoid every divisor space if additionally `n≥m+2`.
For example, if K_C did, choose g with `K_B∩E_g=0`; the entire
n-dimensional f-fibre would become a constant-rank-m subspace of Mat_n.
Equation (5) bounds its dimension by
`max(m+1,n−m+1)<n`, a contradiction. The same argument applies with B and
C reversed. This strengthens the assertion that the two kernels cannot
both avoid every divisor space.

There is also a condition coupling the two nonzero intersections. Identify
the m²-dimensional pure-slice images with the two factors of the identity
matrix of order m² by using the y,v coordinates in the source formula.
Let `R_g` and `S_f` be the corresponding preimages of the two kernel
intersections, of dimensions d_B and d_C. Let `rho(f,g)` be the rank of the
identity bilinear pairing restricted to `R_g×S_f`. Direct linear algebra
gives the quotient-slice rank

\[
\operatorname{rank}S(f,g)=m^2-d_B-d_C+\rho(f,g).
\tag{7}
\]

Indeed, the surviving C-dual space is the annihilator of S_f. Its
intersection with R_g has dimension `d_B−rho`; quotienting its image on
B gives (7). By (6), another necessary condition is

\[
\rho(f,g)\equiv0\pmod m\quad\hbox{for every nonzero }f,g.
\tag{8}
\]

For the requested `m=4` regime, these conclusions apply whenever `n≥13`.
Both kernels have dimension twelve; both must meet some divisor space;
each intersection has dimension 0, 4, 8, or 12; and every induced pairing
in (8) has rank divisible by four. These are exact necessary conditions
that a proposed ordinary construction can be checked against. They do not
classify the twelve-dimensional kernels. In particular, the rank-one
pencil argument used for m=2 does not classify a higher-dimensional space
of four-by-four matrices.

## 3. Why a singular family is still open

The conditions above use ordinary quotients and an invertible identification
of all A slice parameters. A Laurent family can have long-leg kernels with
Grassmannian limits, while output changes of basis and the A map have
different powers of the parameter. Its nonzero limiting coefficient can
depend on higher terms of the quotient maps. It need not equal the tensor
obtained by applying the limiting quotient maps directly to Q.

Thus the proven ordinary exclusion is a reason to search for a truly
singular family. It is not a border-restriction obstruction. A useful
singular candidate must specify every Laurent coefficient and cancel all
negative powers before its full constant coefficient can be compared with
matrix multiplication.
