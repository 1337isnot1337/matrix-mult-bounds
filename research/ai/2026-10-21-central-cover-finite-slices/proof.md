# A finite cube bounds split-cover coordinate target volume

October 21, 2026. Claim `AI-SPLIT-COVER-CUBE-EXCLUSION-001` is a written,
AI-derived proof with exact finite certificates. It has no independent
mathematical review or Lean formalization and gives no smaller exponent.

## 1. Statement

Let G=A5 x C2 and let T_G be its trilinear group tensor: the coefficient of
the identity in xyz. Over F4=F2[w]/(w^2+w+1), the full source satisfies

    slice_rank(T_G^tensor(3)) <= 973422 < 1000000.        (1)

Consequently every degeneration from T_G to a single M(a,b,c) over any
characteristic-two field satisfies abc<=986. In particular M(10,10,10)
and M(9,10,11) are excluded. The same excludes the maintained one-copy
coefficient-one injective-coordinate/strict-potential construction of
that target over C, since such a construction reduces to characteristic
two without changing its surviving coefficients.

This is not an exclusion of arbitrary complex degenerations, which need
not have good reduction. It does not exclude targets in SL(2,F5) or
SL(2,F5) x C2, nor constructions from arbitrary higher source powers.
An upper bound for a degeneration of a source is not an upper bound for
the source itself.

## 2. Exact full-source basis certificate

The certificate reuses the 60-vector F4 basis of
`AI-CENTRAL-COVER-SLICE-BARRIER-001`, pinned by its file SHA256. Acceptance
checks full rank and all 60^3 coefficients of the original A5 group trace.
It does not infer full-source properties from that claim's leading limit.

In this basis the full tensor is a direct sum P + M4, with leg dimensions
44 and 16. Assign degrees 0,1,2,3,4 to P's basis vectors with dimensions

    F(t) = 9 + 8t + 10t^2 + 8t^3 + 9t^4.              (2)

Every nonzero P term has total degree at most four. The exact counts by
total degree are 13 at degree zero, 36 at degree two, and 213 at degree
four. The other block is exactly the 64 coefficient-one matrix triangle
terms on 16 coordinates. There are no cross-block terms. These are checks
of the full 326-term source, not just the preceding 277-term limit.

For the central C2 factor use the invertible basis (1,epsilon), where
epsilon=1+z and epsilon^2=0. The identity-coefficient trace is one on both
1 and epsilon. Its full tensor has precisely the four terms

    (0,0,0), (1,0,0), (0,1,0), (0,0,1).               (3)

Their total epsilon-degree is at most one. In particular the zero-degree
term is retained; replacing the source by the three-term W limit would
not justify a source upper bound.

## 3. Explicit slice cover of each block word

Expand T_G^tensor(n) by the P/M4 block choice at each of its n positions.
This is a direct sum over binary words. In a word containing j P factors,
the degree generating polynomial of one leg is

    16^(n-j) F(t)^j (1+t)^n,                          (4)

and every nonzero triple has total degree at most D=4j+n. For integer
cutoffs (c1,c2,c3) with c1+c2+c3=D-2, cover each leg's coordinates of
degree at most its cutoff. If a nonzero term avoided all three sets, its
total degree would be at least c1+c2+c3+3=D+1, a contradiction.
Allocate each term to the first covering leg/coordinate in a fixed order.
This is a slice decomposition with at most the total size of these sets.
We can also use the entire first leg, taking the smaller cost. No
submultiplicativity assumption about slice rank is used.

Writing D=3q+r with 0<=r<3, choose r+1 cutoffs q and 2-r cutoffs q-1.
If a_d denotes the coefficient of t^d in F(t)^j(1+t)^n, the per-word bound is

    min(44^j 16^(n-j) 2^n,
        16^(n-j) [(r+1) sum_(d<=q) a_d
                   +(2-r) sum_(d<=q-1) a_d]).         (5)

There are binomial(n,j) such words; concatenate their decompositions.
For n=3 the exact cover is:

| P factors j | Words | Cutoffs | Slices per word | Contribution |
| --- | ---: | --- | ---: | ---: |
| 0 | 1 | (1,0,0) | 24576 | 24576 |
| 1 | 3 | (2,2,1) | 65024 | 195072 |
| 2 | 3 | (3,3,3) | 140928 | 422784 |
| 3 | 1 | (5,4,4) | 330990 | 330990 |
| Total | 8 | | | 973422 |

The producer multiplies integer polynomials. The verifier instead
enumerates all 120^3=1728000 one-leg coordinates, checks every block-word
degree count, and tests every degree triple of total at most D against
the cover. It also replays n=1 and n=2, obtaining bounds 110 and 10120.
Those two bounds do not exclude their targets; the cube is the first of
these three tested powers that does.

## 4. Finite matrix multiplication slice rank in characteristic two

We need the finite statement SR(M_m)=m^2 over every field, including when
the characteristic divides m. We give a direct reduction to the external
bounded-rank matrix-space theorem, avoiding a characteristic-zero
semistability argument.

The external theorem is the linear-space case of
[de Seguins Pazzis, arXiv:1507.05375v2, Theorem 1.1](https://arxiv.org/pdf/1507.05375v2),
which states Flanders's dimension bound over an arbitrary field: if a
linear subspace U of m-by-m matrices has every rank at most r, then
dim U <= mr. The paper credits Flanders for the original theorem and
Meshulam for removing the field restriction. We use only the dimension
inequality, not the classification of equality cases. The r=0 case is
immediate. This theorem is external work, not a local discovery.

Suppose tr(ABC) is a sum of p slices on A, q on B, and s on C, with
p+q+s<m^2. Let U be the common kernel of the p A-linear forms. Then
dim U >=m^2-p. For each A in U the resulting bilinear form on B,C is a
sum of at most q+s rank-one matrices, hence has matrix rank at most q+s.
Its rank is exactly m*rank(A): the trace pairing on matrices is
nondegenerate over every field, and left multiplication by A has rank
m*rank(A). Thus every A in U has rank at most r=floor((q+s)/m)<m.
The imported theorem gives

    m^2-p <= dim U <= mr <= q+s,

contradicting the assumed slice count. The reverse bound m^2 follows
by expanding along one leg. This proves the finite target value in every
characteristic. In particular SR(M1000)=1000000 in characteristic two.

## 5. Degeneration and field transfer

Over an algebraically closed field, slice-rank-at-most-R is closed.
For each triple p+q+s=R choose p-, q-, and s-dimensional spaces of slices
in the three legs. The incidence condition that the tensor lie in the sum
of their three slice subspaces is closed. Projecting from the product of
Grassmannians is proper, so the finite union of its images is closed.
Slice rank also cannot increase under linear maps. Thus degenerations
cannot increase slice rank. This is the same standard proper-incidence
argument used in the preceding modular packages.

Suppose T_G degenerates to M(a,b,c) in a characteristic-two field, and
extend to an algebraic closure K. It contains F4, so (1) still supplies an
explicit upper bound. The group trace is cyclic: T_G(x,y,z)=T_G(y,z,x).
Cyclically permuting the alleged maps therefore gives degenerations to
M(b,c,a) and M(c,a,b) from the same source. Taking their tensor product
gives a degeneration from T_G^tensor(3) to M(abc,abc,abc). Closedness and
section 4 imply

    (abc)^2 <= 973422,
    986^2 = 972196 <= 973422 < 974169 = 987^2.         (6)

Since abc is an integer, abc<=986. The volumes 1000 and 990 of M10 and
M(9,10,11) exceed this bound. Only the cube upper bound is used here;
slice-rank submultiplicativity is neither needed nor asserted.

In the maintained complex coordinate/potential model each variable maps
to a distinct group coordinate times an integer Laurent monomial, every
intended triangle has exponent zero and coefficient one, and every
unintended term has positive exponent. The same combinatorial identities
hold over F2; no cancellation or division is needed. This would give the
forbidden characteristic-two degeneration whenever abc>=987. Hence
this whole one-copy construction class is excluded in the split cover
for every such single rectangular target.

## 6. Relation to the asymptotic lower barrier

The prior claim proves a liminf of source-power slice-rank roots greater
than 103.4. It explicitly leaves finite-power tests open. Equation (1)
has cube root below 100, yet causes no contradiction: slice rank is not
submultiplicative. Concatenating slice decompositions on tensor powers
does not multiply their slice counts. We do not turn this finite cover
into an exponential rate or an all-power exclusion.

The nonsplit-cover degeneration toward the split source transfers the
prior lower bound in the required direction, but cannot transfer this
upper bound back to the nonsplit source. Further work there needs a
certificate for the actual full nonsplit tensor or a different argument.
