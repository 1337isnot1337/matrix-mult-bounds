# The adopted torus cap forces normalized long-rank sum at most 200

October 23, 2026. Owner-directed OpenAI Codex continuation.
Written and unreviewed; no independent mathematical review or formalization.

Claim `AI-A4-TORUS-LONG-RANK-SUM-005`.

## 1. Statement and exact predecessor

Consider any complex formal Laurent degeneration A4 to M(10,10,11).
Independently divide each long map by the smallest valuation of its
nonzero entries, and compensate for both scalar factors in the first
map. Let r_B,r_C be the two nonzero constant ranks. Then

    r_B+r_C<=200.                                      (1)

The source-space theorem adopted here is due to the concurrent
[PR129 at 9eca895e3618ad1f560e0565dc30134478e88da8](https://github.com/1337isnot1337/matrix-mult-bounds/blob/9eca895e3618ad1f560e0565dc30134478e88da8/research/ai/2026-10-23-torus-low-rank/proof.md):

    Every complex linear space of A4 source slices with all ranks
    at most 23 has vector dimension at most eight.       (2)

Its exact proof bytes are preserved in
[the adopted source copy](adopted/pr129_torus_low_rank_proof.md.txt), with
SHA-256 `36a9b1a2e1e79c342087bd424ad462200154508b2743b2477f5121afd96930ad`
and Git blob SHA `0143933a0ab7ae4259a5be62653fd1465d7c107e`.
The source theorem, its rank-preserving torus action, its matching minors,
and its individual rank102 exclusion remain credited to PR129.

The new deduction is (1), obtained by applying (2) to the whole leading
polar first-map image. It strengthens the rank-sum mechanism of this
package. The regular kernel residual retains PR113 attribution, and the
canonical source minimum rank16 retains its original credit. The argument
uses elementary linear algebra and polynomial minors. It introduces no
external theorem. Concurrent overlapping work is recorded separately in
[CONCURRENT_WORK.md](CONCURRENT_WORK.md).

## 2. The first map has a pole

Write the scalar-normalized identity as

    B(t) M(F(t)(X)) C(t)=Xi(X)+O(t),
    Xi(X)=X tensor I_11,       X in Mat_10(C).

Here B is 110-by-112, C is 112-by-110, both are regular, and M is the
canonical A4 map from its 112-dimensional parameter space into
112-by-112 matrices. Suppose for contradiction that

    r_B+r_C>=201.                                      (3)

The first map F has a pole. If it were regular, taking constant terms
would give an ordinary restriction. The target unit would force B0 and
C0 to have full ranks110. Target conciseness would force F0 to be
injective. Any target matrix unit would then have a nonzero source lift
of rank at most11+2+2=15, contrary to source minimum16. This also gives
the ordinary obstruction directly in the only case needed here.

Let h>0 be the pole order, and put F_hat=t^h F. Then F_hat is regular
and its leading map F0 is nonzero. The coefficient of t^(-h) in the
complete identity gives

    B0 M(F0(X)) C0=0       for every X.

The two-sided rank-loss estimate therefore gives

    rank M(F0(X)) <= (112-r_B)+(112-r_C) <=23.           (4)

The entire linear space im F0 satisfies (2), so

    rank F0<=8,
    dim ker F0>=100-8=92.                              (5)

## 3. A kernel element can be chosen invertible

A linear subspace of Mat_m with maximum matrix rank r has dimension at
most m*r over C. The needed proof is included in
[corank_one.md, Section 3](corank_one.md).

Briefly, choose a maximum-rank member and change constant bases to make
it diag(I_r,0). For any other member X=[P A;B C], the Schur complement
of diag(I_r,0)+tX vanishes. Its first two coefficients give C=0 and
B A=0. Polarization makes the image under X -> (A,B) totally isotropic
for the nondegenerate pairing tr(B A'+B' A), so that image has dimension
at most r(m-r). The projection kernel has dimension at most r^2. Adding
the bounds gives m*r.

For a singular subspace of Mat_10, this bound is90. Equation (5) thus
implies that ker F0 contains an invertible target matrix X.

## 4. The regular residual contradicts that invertible kernel element

Exchange the two long legs, transposing target matrices and permuting
the canonical source coordinates, if necessary. We may arrange

    r_C>=ceil((r_B+r_C)/2)>=101.                        (6)

Replace F by F_hat and B by t^(-h)B; their scalar factors cancel and C
remains regular. Choose an invertible V with F0(V) nonzero. A nonzero
linear map cannot vanish on the dense open set of invertible matrices,
so such a V exists. Set

    H=Xi(V)^(-1),       S=M(F_hat(V)),       D=S C H.

The matrices S,D are regular. The complete identity makes G=B D=I+O(t)
regular and invertible over C[[t]]. Replace B by G^(-1)B, so B D=I
exactly, while every target constant term remains Xi(X). Put

    T_X=B M(F_hat(X)) C,
    W_X=M(F_hat(X)) C-D T_X.

The residual W_X is regular. Since B W_X=0 and B has full row rank110
over C((t)), all columns of W_X lie in its two-dimensional kernel.
Specializing its vanishing three-by-three minors gives

    rank W_X(0)<=2,
    M(F0(X)) C0=D0 Xi(X)+W_X(0).                        (7)

This is the credited regular kernel residual. Regularity of the two
terms defining W_X is the reason its rank bound can be specialized.

Because F0(V) is nonzero, its source matrix has rank at least16.
Restriction by C0 loses at most112-r_C ranks. Thus

    rank D0>=16-(112-r_C)=r_C-96>=5.                   (8)

For the invertible X in ker F0, equation (7) gives

    D0 Xi(X)=-W_X(0).

Its left side has rank rank D0, since Xi(X) is invertible, and its right
side has rank at most two. This contradicts (8), proving (1).

## 5. Local verification of the adopted finite source controls

The universal source-space assertion (2) rests on PR129's written proof.
Its finite ingredients are reconstructed locally by verify_torus_sum.py,
without fetching a source or importing another verifier.

The canonical coefficient rule is

    M(F)_((j,p,L),(H,q,r))=F_(H-j,p+q,L-r).

The verifier checks all4096 nonzero source terms against the diagonal
action with parameter weight i+4k+28s, row weight -j+4p+28L, and column
weight H+4q-28r. The 112 parameter weights are distinct. It checks all
112 coordinate ranks16,32,48,64,48,32,16 according to the middle index.

For one coordinate at each extreme k=0,6, the two pieces have disjoint
row and column blocks and rank32. All256 such pairs are reconstructed.
Within one extreme, the sixteen outer coordinates are paired by
(i,s) -> (i+2 mod4,s+2 mod4). Each of the eight pair sums has a 24-by-24
minor with determinant one at each extreme, giving sixteen exact minors.

The verifier also records an eight-dimensional coordinate family with
at most20 supported matrix columns, and a twelve-dimensional family
with at most24 supported columns. The latter demonstrates the stopping
point of this particular source-space bound.

Run from the repository root:

```sh
python research/ai/2026-10-23-long-leg-rank-obstruction/verify_torus_sum.py
python -m unittest discover -s tests -p test_long_leg_torus_sum.py -v
```

The result is
`results/long-leg-torus-sum-2026-10-23/controls.json`. Use `--write` to
regenerate it. Finite controls check the source arithmetic, rank budgets,
source pins, and precise scope. They do not enumerate all Laurent maps,
prove the torus specialization for every subspace, or formalize the
written deduction.

## 6. Scope and next boundary

Together with PR129's individual rank bound, a remaining scalar-normalized
chart must satisfy

    1<=r_B,r_C<=101,       r_B+r_C<=200.

The new sum condition additionally removes (101,101), (101,100), and
(100,101) from the pairs left by that individual bound. The pairs
(99,101), (100,100), and (101,99) meet the sum200 boundary and are not
excluded by this argument. They are not asserted to be realizable.

At sum200 the polar source-rank budget is24. A twelve-dimensional source
space at that cap exists, so the dimension-eight premise cannot simply
be carried to that boundary. The argument does not assume singular
matrix changes of basis preserve the two scalar-normalized leading
ranks. It gives no complete degeneration exclusion or improved exponent.

