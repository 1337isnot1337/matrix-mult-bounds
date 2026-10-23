# The rank-seven gap and every six-loss compression boundary

Claim `AI-RESOLVENT-RANK-GAP-001` is written and unreviewed. It extends
[the rank-six classification](proof.md), using the same fixed space W,
rank-six locus Z, and common six-dimensional image Ehat. All statements
in this note hold over every field. They concern ordinary matrix rank.

## 1. Rank seven is absent

The new certificate has 26 triangular eight-by-eight minors in the same
31-dimensional mixed outer space Y. Each determinant is plus or minus
ell^8, where ell has a unit coefficient. Their successive unit
substitutions again leave exactly the five displayed generators of V
from the preceding proof. All these final matrices have rank at most
six. Hence the rank-at-most-seven locus of Y is V: rank seven never
occurs. Conversely the previously checked six-minors show that every
nonzero member of V has rank six.

In W, rank at most seven still forces the scalar, g1, and g2 to vanish,
because their nonzero blocks have rank at least 16. Each remaining
block has rank at most seven, hence is in the same rank-six space as
before. These blocks share a six-dimensional image. Their concatenation
therefore has rank at most six, so the rank-at-most-seven locus of W
is exactly Z. Thus the least nonzero rank is six, and the next possible
rank is at least eight.

Rank eight is attained by the matrix with sole block (3,1)=Q(e01).
In transformed output coordinates its eight nonzero rows are
{0,1,7,8,14,15,22,23}. The verifier checks their support and an
eight-by-eight minor of determinant 1 or -1. This is sharp over every
field, rather than just a rational sample.

The acceptance program verifies every eight-minor entry and substitution,
the complete final parameter transformation, and the rank-eight witness.
It also replays the previous certificate. This is a polynomial identity
certificate, not a finite search over field elements.

## 2. Every allocation of six lost dimensions

Let P and C have output-side and input-side coranks a and b in the
112-dimensional ambient spaces, respectively. Thus L=ker P has dimension
a and U=im C has dimension 112-b. Write H={X in W:PXC=0}.

**Theorem.** If a+b=6 and b>=1, then dim H<=1 over every field.
This bound is attained for every pair (a,b)=(0,6),...,(5,1).
If (a,b)=(6,0), then H=Z when L=Ehat, and H=0 otherwise.
The maximum loss in this last case is therefore 17, not one.
For a+b<=5, the predecessor's injectivity theorem applies.

For a nonzero X in H, the rank-loss inequality gives rank X<=6.
The rank-six classification then gives rank X=6 and im X=Ehat.
Restriction to U has rank at least 6-b=a. Its image lies in L,
so X(U)=L and L is contained in Ehat. The induced map

\[
 \overline X:\mathbb F^{112}/U\longrightarrow\widehat E/L
\]

is an isomorphism between b-dimensional spaces. The linear map
X -> Xbar on H is injective: if Xbar=0 then im X is contained in L,
of dimension a<6, contrary to rank X=6.

First suppose the field is algebraically closed. If H contained two
independent matrices, the associated invertible b-by-b matrices A,B
would make det(A+tB) a degree-b polynomial. It has a root. The resulting
nonzero member of H would induce a singular map, a contradiction.

For an arbitrary field, extend all source formulas and the fixed maps
P,C to an algebraic closure. Matrix ranks and dimensions of kernels of
linear systems are preserved by field extension. The rank-six
classification remains valid there because it was proved over every
field by integer polynomial identities. The preceding argument bounds
the extended compression kernel by one, and hence bounds the original
kernel by one. This step extends the algebraically closed conclusion
stated in the first proof; no unproved property of constant-rank spaces
over nonclosed fields is being assumed.

When b=0, C is surjective, so a killed nonzero X requires im X=Ehat
to be contained in L. Both spaces have dimension six; thus L=Ehat.
In that case every member of Z is killed, and no matrix outside Z
can be killed because its rank exceeds six. This proves the dichotomy.

## 3. Explicit sharp examples

Work in output coordinates transformed by I4 tensor K. Take the same
nonzero witness with sole block (3,1)=Q(e00). Its six nonzero outer rows
are E0={0,7,14,21,22,23}. Delete the last a rows of 84+E0 and the following
input columns in the second middle-coordinate block:

| a | b | Deleted local input columns (add 28) | Dimension of compressed W |
|---|---|---|---|
| 0 | 6 | 0,1,2,3,7,11 | 111 |
| 1 | 5 | 0,1,3,7,11 | 111 |
| 2 | 4 | 0,3,7,11 | 111 |
| 3 | 3 | 3,7,11 | 111 |
| 4 | 2 | 3,7 | 111 |
| 5 | 1 | 3 | 111 |
| 6 | 0 | none | 95 |

The actual entries of the witness show it is killed in every row of the
table. The maps have the indicated ranks over every field. For a<6 the
theorem forces the nonzero kernel to be one-dimensional. For a=6 the
deleted output space is precisely Ehat in these transformed coordinates,
and the kernel is Z of dimension 17. These are therefore all-field
conclusions. As a separate finite control, the verifier reconstructs all
112 generators and independently obtains the table by exact rational
row reduction.

## 4. Limits and next question

The rank gap also implies that any compression with total loss seven
can kill only directions in Z. The dimension of such a kernel is not
classified here. Different resolvents and general singular Laurent
trajectories are outside scope. Neither the rank gap nor the complete
six-loss boundary supplies a matrix target or a smaller exponent.
The generating session's verification is not independent review.
