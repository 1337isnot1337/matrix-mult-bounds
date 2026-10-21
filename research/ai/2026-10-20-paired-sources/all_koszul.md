# Every first-leg Koszul rank of the paired source

AI-derived written proof, unreviewed, October 20, 2026. This extends the
explicit first kernel in research_note.md. It proves a rank obstruction,
not a smaller matrix multiplication exponent. No historical priority is
claimed for the cohomological method or the resulting formula.

Let a>=2, D=a-1, v=a^2 and N=a(2a-1). Let K_p(P_a) denote the map

    exterior^p(A) tensor B* -> exterior^(p+1)(A) tensor C.

With binomial coefficients outside their range equal to zero, the formula is

    rank K_p(P_a) = N binom(v-1,p)
                    +2D^2 binom(v-3,p-1).                 (1)

It holds over every field for 0<=p<=v. The argument below gives the full
rank, rather than extrapolating from small modular matrices.

## 1. A multiplication map on two projective lines

On X=P^1 times P^1 set L=O(D,D) and F=O(D,-2D-2). Choose the standard
monomial basis s_(i,j) of H^0(L), and let e_(i,j) be the corresponding
first-leg basis of A. The universal vector section is

    s=sum_(i,j) e_(i,j) tensor s_(i,j).

The two-chart calculation on P^1 gives h^0(O(d))=d+1 for d>=0 and
h^1(O(d))=-d-1 for d<=-2, with all other cases zero. Tensoring the two
chart complexes gives the corresponding cohomology on X. For a primary
reference to the projective-space calculation see the Stacks Project,
[Lemma 30.8.1, tag 01XT](https://stacks.math.columbia.edu/tag/01XT).

In particular H^1(F) and H^1(F+L) both have dimension N. On an affine
coordinate in each factor, choose basis u^y v^(-j-1) for H^1(F), with
0<=y<=D and 0<=j<=2D. Multiplication by s_(p,q) gives u^(p+y)
v^(-(j-q)-1). Its cohomology class is zero unless 0<=j-q<=D. When
j=q+t it is the output basis vector indexed by (p+y,t). Thus

    H^0(L) tensor H^1(F) -> H^1(F+L)

has exactly the paired-source coefficients, after identifying H^0(L)'s
dual coordinate labels with A. Exterior multiplication by s induces K_p.

## 2. An exact bounded double complex

Fix p and form the complex of line bundles

    C^k=exterior^(p+k)(A) tensor (F+kL),

with differential s wedge. Exterior powers outside 0,...,v vanish. On each
standard product chart one monomial section of L is a unit in its local
trivialization. Contraction at that coordinate contracts the Koszul
complex. Thus C is exact on every chart and every chart intersection.
The total complex of its product Čech complex is exact.

Taking the Čech cohomology first yields a bounded spectral sequence

    E_1^(k,q)=exterior^(p+k)(A) tensor H^q(F+kL) => 0,
    d_r:(k,q)->(k+r,q-r+1).

This is the standard bounded double-complex construction in the Stacks
Project, [Section 12.25, tag 012X](https://stacks.math.columbia.edu/tag/012X).
Its boundedness is enough for convergence here; the Čech terms themselves
need not be finite dimensional.

The nonzero cohomology rows have this pattern:

- q=2 only at k<=-2;
- q=1 only at k=-1,0,1,2;
- q=0 only at k>=3 (possibly starting later in the smallest case).

The q=1 dimensions at k=-1,0,1,2 are 3D+1,N,N,3D+1, respectively,
before the exterior factor. At k=-j, j>=2, the q=2 dimension is

    h_j=((j-1)D-1)((j+2)D+1).                       (2)

All possible d_r with r>=3 vanish: the only remaining case would go from
q=2,k<=-2 to q=0,k+3<=1, where the latter group is zero. On the E_2
page the only possible maps involving the left side are

    E_2^(-3,2) -> E_2^(-1,1),
    E_2^(-2,2) -> E_2^(0,1).

They must be isomorphisms because E_3=E_infinity=0. All other E_2 groups
in the q=2 row are zero.

## 3. Recover the desired kernel dimension by Euler characteristic

Write u=binom(v,p-1)(3D+1), the dimension of E_1^(-1,1), and let r be
the rank of its d_1 map to E_1^(0,1). If k_p=dim ker K_p, then

    dim E_2^(-1,1)=u-r,
    dim E_2^(0,1)=k_p-r.

Euler characteristic in the q=2 row and the two isomorphisms above give

    sum_(j=2)^p (-1)^j binom(v,p-j) h_j = k_p-u.

Hence

    k_p=binom(v,p-1)(3D+1)
         +sum_(j=2)^p (-1)^j binom(v,p-j) h_j.       (3)

This does not assume that any individual d_1 or d_2 has maximal rank.
Only exactness of the total complex and the displayed zero positions were
used. Subtract (3) from the domain dimension N binom(v,p).

For the simplification, the quadratic polynomial (2) is

    h_j=D^2*j*(j+1)-N.

At j=0 it is -N, and at j=1 it is -(3D+1). Therefore the generating
function of the ranks is

    -(1+z)^v sum_(j>=0) (-1)^j h_j z^j
       = N(1+z)^(v-1)+2D^2 z(1+z)^(v-3).

Taking its pth coefficient proves (1). At p=1, its kernel is 3a-2,
agreeing with the earlier direct classification. The formula is symmetric
under p->v-p-1, as transpose duality requires.

## 4. Consequence for the proposed size-six target

The independent matrix-rank formula in matrix_koszul.md gives, at p=7,

    rank K_7(P_6)=499196720,
    rank K_7(M(6,10,6))=500652900.

Both use the same 36-dimensional first leg. Padding the other two target
legs from 60 to 66 adds zero columns or rows and does not change this
rank. Rank cannot increase in a complex tensor degeneration. Consequently
the proposed P_6 -> M(6,10,6) degeneration is impossible.

The former conditional 2.235 implication remains a valid implication with
an excluded premise. It is not an exponent improvement. The earlier first
Koszul and coarse grading screens did leave it open; (1) supplies the
stronger source rank needed to close it.
