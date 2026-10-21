# Exact multiplication controls inside the parity source

October 21, 2026. These are explicit, coefficient-verified constructions.
They do not establish a smaller matrix multiplication exponent or a
restriction of the full source to M14 plus M3. A separate pairwise
annihilator argument excludes the formerly proposed parity-source target
M14 plus M4; the exact controls below remain valid.

## An integral mixed-basis M9 restriction

Let P4 denote the polynomials of degree at most four. Choose ordered bases

    U = (1, x^4, x),
    V = (x^2, 1+x^4, x+x^3).

The nine products U_alpha V_beta, ordered by 3*alpha+beta, form an integral
basis of P8. Their coefficient matrix M has determinant -1. The integer
matrix R printed in `parity_structure_certificate.json` is its exact inverse;
the executable checks both R M = I and M R = I over the integers.

Consequently the two short-leg maps U,V and the long-leg map R restrict the
convolution tensor C(5,5) to the outer-product tensor of dimensions (3,3,9).
Applying these maps on the three cyclic convolution factors gives

    A(5,5) -> M(9,9,9).

This is an ordinary restriction with entries in {0,1,-1}. It uses genuine
coordinate mixing: a monomial-only control below gives M8.

Here are the complete map formulas. The source coordinates are

    X=(i,t,s), Y=(j,p,u), Z=(v,q,r),

where i,j,p,q,r,s range from 0 to 4 and t,u,v from 0 to 8. The source has
coefficient one at t=p+q, u=r+s, v=i+j. Label the nine target vertices by
pairs in {0,1,2} squared, using index 3*alpha+beta. Write

    I=(alpha1,beta2), J=(alpha2,beta3), K=(alpha3,beta1).

The three restriction matrices are

    A[(I,J),(i,t,s)] = U[alpha1,i] R[(alpha2,beta2),t] V[beta3,s],
    B[(J,K),(j,p,u)] = V[beta1,j] U[alpha2,p] R[(alpha3,beta3),u],
    C[(K,I),(v,q,r)] = R[(alpha1,beta1),v] V[beta2,q] U[alpha3,r].

The source contractions separate into three identities R M = I. Therefore
the image coefficient is one exactly for a matching target triangle and
zero for every other coefficient. The executable also verifies that claim
by accumulating the complete transformed tensor in exact integer arithmetic.
The image has exactly the expected 729 nonzero coefficients.

## Restricting the parity degeneration

The source weights are

    wX=t-i-s, wY=u-j-p, wZ=v-q-r.

The degeneration D removes precisely the parity pattern (1,1,0) and retains
the patterns (0,0,0), (0,1,1), and (1,0,1). It has 11,725 terms.

Each U and V polynomial is parity homogeneous, with grades (0,0,1).
Every nonzero entry of row R[(alpha,beta),:] has degree parity
grade(alpha)+grade(beta) modulo two. Thus the maps preserve parity.
Define each target vertex grade by

    g(alpha,beta) = grade(alpha)+grade(beta) mod 2.

There are five vertices of grade zero and four of grade one. The image
of D is exactly the parity face of M9 that removes triangles whose three
edge grades are (1,1,0). Those edge grades are

    (g(I)+g(J), g(J)+g(K), g(K)+g(I)) mod 2.

This image has 549 terms: M9 has 729, while the omitted triangles number
5*5*4+4*4*5=180. The executable verifies the complete parity-face image,
including absence of every extraneous coefficient.

This produces several ordinary multiplication controls. Keeping only
equal-grade X entries leaves the independent direct sum

    M(5,5,9) plus M(4,4,9),

with formats summing to (41,81,81) and with 225+144=369 terms. Keeping only
unequal-grade Z entries instead gives

    M(5,9,4) plus M(4,9,5),

with formats summing to (81,81,40) and 360 terms. The separation into direct
sums is exact: the first construction separates by the common grades of I,J,
and the second by the ordered unequal grades of I,K. Their coordinate
supports on all three tensor legs are disjoint.

## Saved matrices and a full-source larger-target seed

`parity_structure_m9_maps.npz` contains A,B,C, each an integer array with
shape (81,225), target coordinates first. The aliases x,y,z contain the
same arrays. U,V,R and the target vertex grades are also included.
Each matrix has 300 nonzero entries.

Source flattening orders, all zero based, are

    X: (i*9+t)*5+s,
    Y: (j*5+p)*9+u,
    Z: (v*5+q)*5+r.

Target flattening orders are 9*I+J, 9*J+K, 9*K+I. Target vertex grades in
this order are (0,0,1,0,0,1,1,1,0).

To embed the full-source seed in the first nine vertices of an M14 block,
move target row 9*i+j to row 14*i+j on each leg and set other rows to zero.
Appending the nine rows of a separate M3 block as zeros gives matrices of
shape (205,225). On the full source, the resulting image consists of exactly
729 desired coefficients of the 2,771-term M14-plus-M3 target, so its
relative Frobenius residual is sqrt(2042/2771), approximately 0.85844,
before perturbation. This is only a partial-target seed.

Every missing target triangle uses at least two new edge rows. The exact
seed is consequently a stationary point of the squared residual objective:
one-leg first derivatives cannot fill those entries. Finite perturbations
or a second-order construction are needed to start a local extension.

There is also no extension that fixes the two other core maps exactly while
adding a nonzero new row on one leg. Contraction with those two core maps
is injective on the remaining 225-dimensional source leg. It factors as
three injective maps of ranks 5,9,5: multiplication by a nonzero polynomial
on each end and the invertible nine-product matrix in the middle. Thus a
successful extension must adjust the existing core maps as well.

## A monomial M8 family

For scalar sets A,C,F,D,G,L with uniquely represented sums A+C, F+D, G+L,
take vertices I=A cross F, J=D cross L, K=C cross G and maps

    X(I,J)=(A,F+D,L),
    Y(J,K)=(C,D,G+L),
    Z(K,I)=(A+C,F,G).

Whenever these coordinates lie in the source ranges, uniqueness of the
three scalar sums proves that every retained source term is a matching
matrix-multiplication triangle. Injectivity also holds separately on each
edge coordinate map. The choice

    A=D=G={0,4}, C=F=L={0,1,2,3}

gives an induced M8 in A(5,5). Its parity face has vertex split four plus
four. The executable checks both the full and parity-face restrictions.

## Reproduction

Run from the repository root:

    python research/ai/2026-10-20-anisotropic-constructions/parity_structure.py

This uses NumPy, recomputes both tensors, checks every image coefficient,
and rewrites the certificate and compressed matrices. The larger-source
restriction maps are composed from three exact nine-dimensional identities;
no numerical optimization is needed to obtain or validate these controls.
