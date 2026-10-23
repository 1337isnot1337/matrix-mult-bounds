# An all-order gap for the two singular A4 leading flags

October23,2026. Written, unreviewed owner-directed OpenAI Codex work.
No independent review, formalization, full target or exponent improvement.

## 1. Statement and normalization

Suppose a complete complex formal degeneration satisfies

    B M(F(X)) C = X tensor I_11+O(t), X in Mat_10(C).          (1)

Here M is the literal112-by112 A4 source slice map, F is a Laurent
linear first map, and B,C have formats110-by112 and112-by110. Balance
both long maps by their minimum entry valuations b,c:

    B_hat=t^(-b)B,  C_hat=t^(-c)C,  F_hat=t^(b+c)F.

The identity is unchanged and both balanced long maps are regular.
Let r_B,r_C be their leading ranks, q_B=112-r_B, q_C=112-r_C, and

    d=q_B+q_C=224-r_B-r_C.

Then every such degeneration must satisfy

    d>=20, equivalently r_B+r_C<=204.                       (2)

If20<=d<=27, the leading polar coefficient of F_hat has rank between
10 and16 as a linear map from Mat_10 to the source parameter space.
Its image has one fixed coherent middle Hankel factor. If28<=d<=31,
the fixed-factor and upper-rank16 conclusion still hold. No conclusion
about a completed target follows from passing these necessary tests.
Every finite pole order is allowed throughout the exclusion (2).

The [one-regular-long-leg theorem](../2026-10-23-one-regular-leg/proof.md)
first gives r_B,r_C<=109. If F_hat were regular, the unit equation at
zero would instead require both ranks at least110. Thus F_hat has a
pole of some order h>0. Put L=F_hat_(-h), a nonzero linear map. The
leading negative coefficient of (1) gives

    B_hat(0) M(L(X)) C_hat(0)=0 for every X.                 (3)

## 2. The regular kernel correction with a singular column limit

The following argument does not require C_hat(0) to have full rank.
Assume ker L contains an invertible matrix X_0. Replace F_hat by
F'=t^h F_hat and B_hat by B'=t^(-h) B_hat. Then F' is regular with
F'_0=L, while C_hat remains regular and (1) is preserved.

For any invertible U in Mat_10, set

    Y_X=M(F'(X)) C_hat,       D=Y_U,       G=B'D.

Both Y_X and D are regular. The unit output is G=U tensor I_11+O(t),
so G is regular invertible. Normalize B''=G^(-1)B'. Then B''D=I_110
exactly, and Z_X=B''Y_X is regular with

    Z_X(0)=(U^(-1)X) tensor I_11.

Over C((t)), P=I_112-D B'' projects onto the two-dimensional kernel
of B''. Consequently W_X=P Y_X=Y_X-D Z_X has rank at most2.
The latter expression proves W_X is regular before specialization;
therefore rank W_X(0)<=2. This is the credited regular right-inverse
correction used in PR113, now applied with a singular column limit.

Since L(X_0)=0, Y_(X_0)(0)=0, and hence

    W_(X_0)(0)=-M(L(U)) C_hat(0) ((U^(-1)X_0) tensor I_11).

The last factor is invertible. It follows that
rank(M(L(U)) C_hat(0))<=2 for every invertible U. Such matrices form
a dense open subset of Mat_10. The rank-at-most2 condition is closed
and depends polynomially on U, so it holds for every U. Deleting q_C
source columns can lose at most q_C in rank. Transpose the same
argument to obtain the other side as well. For every f in im L,

    rank M(f)<=2+min(q_B,q_C).                              (4)

The target parameter is transposed in that argument, and invertibility
of X_0 is preserved. Thus an invertible matrix in ker L requires
min(q_B,q_C)>=14, by the source minimum16. In particular,

    d<=27 implies ker L contains no invertible matrix.      (5)

No unit-lift regularity or rank condition was imposed on the original
maps. Regularity of the scalar-balanced F' is automatic.

## 3. A lower bound for the leading first-map rank

A complex linear space of10-by10 singular matrices has dimension at
most90. We use the dimension inequality of Flanders, with the arbitrary-
field statement in [de Seguins Pazzis, arXiv:1507.05375v2, Theorem1.1](https://arxiv.org/pdf/1507.05375v2).
Its hypotheses are a linear matrix space with every rank at most r;
for n=p=10 and r=9 it gives dim<=10*9. The paper retains Flanders's
original credit and Meshulam's field extension credit. The theorem
is external work; no equality classification is used.

If rank L<=9, then dim ker L>=91, so ker L contains an invertible
matrix. Combining with (5) proves

    d<=27 implies rank L>=10.                              (6)

This is a rank of a linear coefficient map, not a matrix slice rank
or the tensor slice-rank invariant.

## 4. The source gap excludes all total defects below20

Equation (3) gives rank M(f)<=q_B+q_C=d for every f in im L. The
prior source minimum16 excludes d<16. If d<20, the complete prior
[rank-gap theorem](../2026-10-20-anisotropic-constructions/slice_rank_gap.md)
for a=b=4 makes every nonzero f in im L a rank16 slice. Its complete
minimum-rank classification is

    f_(i,k,s)=u_i h_k v_s,

where the4-by4 Hankel matrix of h has rank one. The pinned
[minimum-rank proof](../2026-10-20-koszul/cyclic_finite_target.md), Section4,
supplies the same classification by an elementary multiplication argument.
The gap above16 uses the credited vector-bundle splitting theorem in
[Grothendieck1957, Theorem2.1, printed page126](https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG/AG-25.pdf),
through the maintained predecessor proof. Its hypothesis is a complex
vector bundle on P^1; the relevant kernel bundle and its splitting
degrees are given explicitly there. Neither imported result is claimed
as a new theorem of this continuation.

Every linear space in this minimum locus has one fixed h: a line with
different h factors either ceases to be decomposable or would lie in
the degree-six rational normal curve, which contains no line. With h
fixed, a linear space of decomposable u tensor v has either a fixed u
or a fixed v. To see this, sum two independent tensors. Decomposability
of their sum requires one pair of factors proportional. If two u
factors are independent, comparison with both tensors fixes every v;
otherwise every u was already proportional. Thus

    d<20 implies rank L<=4.                                (7)

Equations (6) and (7) contradict each other. This proves (2), at every
finite Laurent order, including the formerly open equality d=16.

For d<32, the prior [polynomial-rank-locus theorem](../2026-10-20-anisotropic-constructions/polynomial_rank_locus.md)
makes im L lie in a single space {g_(i,s) h_k} with fixed rank-one
Hankel h. Its dimension is16. This gives the stated upper bound and,
together with (6), the interval10<=rank L<=16 for20<=d<=27.

## 5. Exact leading controls and the remaining gap

The literal source coordinate f_(0,0,0)=1 has16 distinct row/column
pivots. For each3<=q_B<=13, kill q_B pivot rows and the remaining
q_C=16-q_B pivot columns. This gives both leading ranks at most109,
total defect16 and B_0 M(f) C_0=0. Restore all but two deleted rows
and columns at degree one to make both long maps have rank110 over
the Laurent field. The t^(-1)f lift has no negative output coefficient,
but its constant output is a rank12 partial permutation, not a unit.
These controls attain only the leading equation, which the all-order
argument proves cannot extend to the target.

For L(X)=tr(X)f, the cyclic permutation matrix is invertible in ker L.
The prospective unit U=I_10 gives rank(M(L(U)) C_0)=q_B>=3, violating
the correction bound2. These exact witnesses isolate the new obstruction.
Additional literal source controls calibrate ranks16 and20; dimension
controls record Flanders's strict margin and its singular-kernel equality
example, without claiming a target at equality.

Predecessor source minimum, gap, coherent locus and PR113 kernel argument
retain exact byte pins and original credit. All new proofs and controls
are owner-directed OpenAI Codex work, written and unreviewed. Finite
controls do not formalize arbitrary series or provide independent review.
Defects at least20 remain open, subject to the stated leading-rank bounds.
There is no full A4 exclusion, constructed matrix target or exponent
improvement below9/4.
