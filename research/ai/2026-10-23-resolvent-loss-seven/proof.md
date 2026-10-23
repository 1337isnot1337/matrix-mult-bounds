# Sharp two-direction bound at total compression loss seven

October 23, 2026. Written and unreviewed. No exponent improvement.

## 1. Statement

Let W be the same 112-dimensional fixed-resolvent matrix space as in
`AI-RESOLVENT-RANK-SIX-LOCUS-001`. Work over any field.
Let P have size 110-by-112 and C size 112-by-110. Define

    p = 112-rank P,    q = 112-rank C,    p+q <= 7.

Then

    dim ker(X -> PXC, X in W) <= max(0,p+q-5).

In particular, total loss seven gives dim PWC>=110. This is sharp:
there are integer factors of ranks 109 and 108 attaining dimension 110.
The same bound covers every split of total loss six, extending PR188's
rank109/rank109 case. The statements concern this fixed W only. Scalar extension and descent
allow the bound over every field, as explained below.

The proof reuses the all-field classification in PR188: every nonzero
matrix in W of rank at most seven has rank six and image equal to one
fixed six-dimensional E_full. No additional low-rank source search is
required. The sole external input is projective intersection, stated
with its field use in Section 2.

## 2. Classical full-row-rank space bound

If a d-dimensional linear space of m-by-n matrices over an algebraically
closed field consists of full-row-rank matrices and zero, where 1<=m<=n,
then d<=n-m+1.

Here is the reduction to the external projective-intersection theorem.
Choose a basis A1,...,Ad. Rank failure is equivalent to a nonzero row vector
v and nonzero t=(t1,...,td) satisfying

    v^T (sum_i ti Ai) = 0.

These are n bilinear equations on P^(m-1) x P^(d-1). Under the Segre
embedding they become n homogeneous linear equations in P^(md-1).
The Segre variety is closed, has dimension m+d-2, and its points are the
rank-one matrices (v_j ti). These facts follow directly from the two-by-two
minor equations and the standard coordinate charts, each an affine space
of dimension m+d-2.

If d>=n-m+2, its dimension is at least n. The linear equations cut a
projective linear subspace of codimension at most n. The Segre variety
must meet that subspace by the [Stacks Project, Lemma 33.34.3, tag 0B2R](https://stacks.math.columbia.edu/tag/0B2R). The intersection has a point
over the algebraically closed base field, giving nonzero v,t and a rank
failure. This contradiction proves the bound.

The imported lemma concerns nonempty closed subsets of projective space
whose dimensions sum to at least the ambient dimension. It is valid over
any field as a statement about closed subsets. Algebraic closedness here
is needed to obtain a base-field point. We do not infer this matrix-space
bound over arbitrary fields. No historical priority for this classical
bound or the Segre argument is claimed.

## 3. Application to the compression kernel

First suppose the field is algebraically closed. Set U=im C, L=ker P,
and Kc={X in W: PXC=0}. If p+q<=5, the predecessor's
minimum rank six and the elementary restriction inequality give Kc=0.
Assume Kc is nonzero and 6<=p+q<=7. Every nonzero X in Kc has rank at most
p+q, so the predecessor's rank-seven gap gives rank X=6 and im X=E_full.

Put ell=dim(L intersect E_full). Since p,q>=2 and p+q<=7, p<=5 and
ell<=5. For every X in Kc the quotient map factors as

    F^112/U -> E_full/(L intersect E_full).

Every nonzero such map is surjective, since X has image E_full. Its
source dimension is q and target dimension is m=6-ell>=1. The association
from Kc to these m-by-q matrices is injective: a nonzero X cannot have
image in a subspace of E_full of dimension at most five. Nonemptiness
therefore implies q>=6-ell.

Section 2 gives

    dim Kc <= q-(6-ell)+1 = q+ell-5 <= p+q-5.

This proves the theorem, including the alignment refinement with ell.
For total loss seven, two lost directions require ell=p: the entire
left kernel must lie in E_full. A one-dimensional kernel only forces
ell>=6-q. These conditions are necessary, not sufficient.

For an arbitrary field F, extend scalars to its algebraic closure. The
integer source identities and the predecessor's classification remain valid
there. Ranks of P and C, dim W, dim ker(X -> PXC), and dim(L intersect
E_full) are unchanged by field extension: each is the rank or nullity of
a matrix of linear equations over F. Apply the bound over the closure and
descend these dimensions to F. This proves the full theorem over every
field, including the refinement using ell. It also removes algebraic
closedness from the predecessor's critical-compression conclusion.

This descent does not assert the classical full-row-rank-space lemma over
arbitrary fields. A general matrix space can acquire lower-rank nonzero
members over an extension. Here the source's exact low-rank classification
controls those members over the closure as well.

## 4. Integer sharpness witness

Use the predecessor's middle-first ordering and multiply every output
block by K, its integral unimodular unit. Denote this output change by D.
In these coordinates E_full is supported on the final-block rows
R={0,7,14,21,22,23}.

Take X0 and X1 in W_6 with only block (3,0) nonzero, respectively Q(e_00)
and Q(e_10). After the output change their blocks are the predecessor's
high matrices S(e_00)K^-1 S(e_i0). On the first three rows of R their only
nonzero coefficients are

| Matrix | Nonzero (row,column) pairs in its outer block |
| --- | --- |
| D X0 | (0,3), (7,7), (14,11) |
| D X1 | (0,7), (7,11), (14,15) |

All displayed values are one. Outside R both matrices vanish.
The verifier checks these statements against the literal integer source.

Let P_tilde select all 112 output coordinates except final-block rows
21,22,23. It has 109 rows; append one zero row to give the required
110-by-112 size. Set P=P_tilde D, so its rank is 109.
Let C select all 112 input coordinates except block-zero columns
3,7,11,15, and append two zero columns to obtain size 112-by-110.
It has rank 108. The displayed support identities give PX0C=PX1C=0.
The two source parameters are independent, so dim Kc>=2. Section 3 gives
the reverse inequality over every field, hence dim Kc=2
and dim PWC=110.

All factor entries are integers and the selected unit inverse is integral.
This witness attains exactly two lost directions over every field, as do
the same rank and support identities combined with Section 3. There is no
characteristic-dependent determinant in the sharpness construction.

## 5. Evidence and boundary

The standard-library verifier checks the source pins, the predecessor's
complete low-rank certificate, the integer sharpness support, and the
rank budgets. Tests additionally reconstruct the entire 112-dimensional
space and find exactly 110 independent compressed generators over F2.
An integer minor nonzero modulo two certifies the same lower bound over Q;
the exact two-dimensional kernel gives the matching upper bound.

This proof closes the specific total-loss-seven question from PR188.
It does not classify losses of eight: rank-eight source matrices then
become eligible kernel directions outside W_6. Nor does the compressed
space result produce a target tensor or an improved exponent. The source
classification and this continuation remain written and unreviewed.
