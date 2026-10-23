# Diagonal-polynomial biform blocks and exact quadratic rank

October 23, 2026. Owner-directed AI-assisted work. Written, unreviewed proofs. Neither a matrix-tensor degeneration nor an exponent improvement is claimed.

## 1. Statement

Work over any field K. Fix integers a>=2 and 0<=d<a, and a polynomial

    f(t)=c_0+c_1*t+...+c_d*t^d,  c_0*c_d != 0.

Define g(x,z)=f(xz). The maintained cyclic-source coefficient matrix has rows (j,L), columns (H,r), where 0<=j,r<a and 0<=H,L<2a-1, and

    R_a(g)[(j,L),(H,r)] = coefficient of x^(H-j) z^(L-r) in g.

This matrix is square, of size a(2a-1). The source convention is pinned in sources.json.

**Theorem A (all-degree reduction).** Let T_(a,h) be the a-by-a banded Toeplitz matrix

    T_(a,h)[u,v]=c_(h+1+v-u),  0<=u,v<a,

with out-of-range coefficients understood to be zero. Then

    rank_K R_a(f(xz)) = a^2 + sum_(h=0)^(d-1) rank_K T_(a,h).     (1)

This identity is exact over every field, without assuming intermediate coefficients are nonzero.

**Theorem B (quadratic rank).** Suppose a>=3, d=2 and c_0*c_2 != 0. Define

    D_0=1, D_1=c_1,
    D_n=c_1*D_(n-1)-c_0*c_2*D_(n-2) for n>=2.

Then

    rank_K R_a(c_0+c_1*xz+c_2*x^2*z^2)
       = a^2+2a-1 if D_a=0, else a^2+2a.                   (2)

In particular every polynomial in this family has rank at least a^2+2a-1. The corresponding two-monomial and arbitrary-biform results have different scope and remain credited separately.

For c_0=c_1=c_2=1, D_n is the integral six-periodic sequence 1,1,0,-1,-1,0, repeated. Therefore

    rank_K R_a(1+xz+x^2*z^2)
      = a^2+2a-1 precisely when a=2 modulo 3,
      = a^2+2a otherwise,                                 (3)

in every characteristic. For c_0=c_2=1, c_1=2, the recurrence gives D_n=n+1; the rank drop in (2) occurs exactly when char(K) divides a+1.

## 2. All-degree proof

An entry of R_a(g) vanishes unless H-j=L-r, equivalently j+L=H+r. Sort rows and columns by this conserved index s, 0<=s<=3a-3. For each s, the admissible indices j and r are the same interval

    I_s=[max(0,s-2a+2),min(a-1,s)] intersect Z.

The s-block is the square matrix

    B_s[i,r]=c_(s-i-r),  i,r in I_s.                        (4)

The whole matrix is a direct sum of these B_s after row and column permutations.

For s=0,...,a-1, I_s=[0,s]. Reversing the columns, r'=s-r, makes the entry c_(r'-i). This is triangular with diagonal c_0; hence rank(B_s)=s+1.

For s=a+d,...,2a+d-2 put

    J_s=[s-d-a+1,a-1] intersect Z.

Because d<=a-1, J_s is contained in I_s. Rows and columns of B_s indexed below J_s are zero, since even the maximum possible other index a-1 gives s-i-r>d. On J_s by J_s reverse columns using r'=s-d-r. The entry becomes c_(d+r'-i), a triangular matrix with diagonal c_d. Thus

    rank(B_s)=|J_s|=2a+d-1-s.

For s>2a+d-2 every entry vanishes because s-i-r>d for all i,r<a. The first and last nonzero ranges contribute respectively a(a+1)/2 and a(a-1)/2, totaling a^2.

Exactly the d blocks s=a,...,a+d-1 remain. Each has I_s=[0,a-1] because d<a. Write s=a+h and reverse columns r'=a-1-r. Formula (4) becomes c_(h+1+r'-i), precisely T_(a,h). Adding all block ranks proves (1). For d=0 the central sum is empty and the same calculation gives a^2.

## 3. Quadratic proof

When d=2, the first central T_(a,0) is tridiagonal with diagonal c_1, upper diagonal c_2 and lower diagonal c_0. Expanding its determinant along the first row gives D_n as stated. The second central T_(a,1) is triangular with diagonal c_2, and therefore has rank a.

If D_a!=0, T_(a,0) is invertible. If D_a=0, its submatrix on rows 1,...,a-1 and columns 0,...,a-2 is triangular with diagonal c_0 and determinant c_0^(a-1) !=0. Its rank is therefore exactly a-1. Formula (1) now proves (2), uniformly in K.

For c_0=c_1=c_2=1, D_0=1, D_1=1, D_2=0, D_3=-1, D_4=-1, D_5=0. The recurrence implies D_(n+3)=-D_n for all n>=0, first at n=0,1 and then by induction. Thus zeros occur exactly at n=2 mod 3 even after reduction into any field. For c_0=c_2=1,c_1=2, induction gives D_n=n+1.

## 4. Acceptance, provenance and limits

Run from the repository root:

    python research/ai/2026-10-23-diagonal-biform-ranks/verify.py --output results/local/diagonal-biform-controls.json
    python -m unittest tests.test_diagonal_biform_ranks -v

The finite acceptance independently reconstructs literal coefficient matrices, their conserved-index blocks, the central Toeplitz matrices, triangular rank intervals, and the quadratic determinant recurrence over F2,F3,F5,F7,F101. The saved output records 312 block-formula cases, 112 literal full-matrix cases, 144 quadratic instances, 5016 triangular-block checks and 290 periodic-recurrence cases. These are finite controls and do not replace the proofs above.

The original cyclic source and arbitrary-biform results retain their attribution, exact source pins and limitations in sources.json. PR171's binomial-biform formula and PR186's arbitrary-biform proof work were inspected for overlap but are not premises. The new calculation classifies individual diagonal-polynomial slices, not linear spaces of slices, general biforms, full matrix targets or singular limits. No smaller exponent follows.

**Next precise question.** For d>=3, classify simultaneous rank defects of the d central banded Toeplitz matrices, particularly shared determinantal conditions in arbitrary positive characteristic. A target construction would additionally require all three leg maps and an exact source-to-target implication.
