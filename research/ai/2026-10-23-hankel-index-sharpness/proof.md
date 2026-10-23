# Every integer Hankel pencil degree budget is attained

October 23, 2026. Written proof, unreviewed. Owner-directed Codex work.
No independent mathematical review, formalization or priority is claimed.

The construction below works over **every field** F. All matrix and
polynomial identities are integral, including in characteristic two.
The external index sum theorem and the earlier local Hankel proof retain
their attribution. The construction and kernel proof here do not require
the index sum theorem.

## 1. Family and statement

Choose positive integers `epsilon`, `p`, `q`, and set

    s=p+q,  r=epsilon*s,  a=r+p,  b=r+q,  d=a+b-2.

For homogeneous pencil parameters `[u:v]`, let the moment vector of
length `d+1` have only the two nonzero entries

    h_(r-1)=u,       h_(r+s-1)=v.

Write `H(u,v)_(i,j)=h_(i+j)` for `0<=i<a`, `0<=j<b`. Both indicated
moments lie between zero and d. Define the degree-r binary form

    P(u,v;X,Y) = sum_(j=0)^epsilon
                    (-v)^(epsilon-j) u^j X^(s*j) Y^(r-s*j).       (1)

**Theorem.** Every nonzero projective member H(u,v) has rank exactly r.
On the affine chart `u=1`, write `t=v` and `P(t,z)=P(1,t;z,1)`.
The polynomial right kernel over F[t] has the basis

    P(t,z), z P(t,z), ..., z^(q-1) P(t,z),                       (2)

with coefficient vectors of length b. The left kernel has the analogous
basis through `z^(p-1) P(t,z)`, with vectors of length a. Every nonzero
polynomial kernel vector has t-degree at least epsilon. All left and
right minimal indices are epsilon, and

    (a+b-2r)*epsilon = (p+q)*epsilon = r.                       (3)

In particular every equality case of this numerical form, at every
positive integer epsilon and every positive left/right nullity, has an
explicit Hankel pencil realizing the complete degree budget.

## 2. Annihilation and constant rank, including both endpoints

Let `c_j=(-v)^(epsilon-j)u^j`. Then `u c_j+v c_(j+1)=0` for
`0<=j<epsilon`. Contracting (1) against the moments means checking

    sum_(j=0)^epsilon c_j h_(s*j+k)=0,
                  0<=k<=d-r=r+s-2.                           (4)

Whenever one nonzero contribution occurs, the other occurs at the next
index and cancels it. The two possible unmatched contributions would
require `k=r+s-1` or `k=-1`, outside the indicated range. This proves
(4) as polynomial identities over the integers.

The shifted forms in (2) give q independent right-kernel vectors at every
`[u:v]`: multiplication by a nonzero polynomial is injective over F[z].
The p analogous left vectors are independent as well. These imply
`rank H(u,v)<=r` at every point, without specializing a generic kernel
across a possible endpoint rank drop.

The leading r-by-r submatrix has antidiagonal u, with all entries on
one side of that antidiagonal zero. Its determinant is
`(-1)^(r(r-1)/2) u^r`. The trailing r-by-r submatrix has the same
property with v and determinant `(-1)^(r(r-1)/2) v^r`.
At every projective point at least one of these minors is nonzero.
This proves exact rank r at both endpoints and throughout the pencil.

## 3. Complete polynomial kernel and minimal degrees

Work on `u=1`. The polynomial P(t,z) is monic in z of degree r and
has t-degree epsilon, with leading t-coefficient the nonzero constant
`(-1)^epsilon`. Thus it is primitive as a vector of polynomials in t.
The q vectors in (2) are independent over F(t) and the kernel dimension
is q by Section 2, so they span the rational-function kernel.

Let f(t,z) be any polynomial right-kernel vector, encoded as a polynomial
in z of degree less than b. Over F(t), f is divisible by P. Division by
the monic polynomial P can also be performed over F[t], and uniqueness
of the remainder forces that remainder to be zero. Therefore

    f=P g,     g in F[t,z],     deg_z g < q.                  (5)

This proves that (2) is the entire F[t]-module kernel. Since F[z] is an
integral domain and the leading t-coefficient of P is nonzero,

    deg_t(P g)=epsilon+deg_t g   for every nonzero g.          (6)

No nonzero kernel vector has degree below epsilon. Every vector in (2)
has degree epsilon, and their leading t-coefficients are independent.
They consequently form a minimal polynomial basis: any rational kernel
basis with polynomial entries has q vectors each of degree at least
epsilon, while (2) attains that lower bound for every vector. The left
kernel proof is identical. This proves all assertions, including (3).

## 4. The A10 boundary and the precise consequence

For `epsilon=2`, `p=q=2`, the construction gives

    a=b=10, r=8, h_7=u, h_11=v,
    P=u^2 X^8-u v X^4 Y^4+v^2 Y^8.

On `u=1` the primitive annihilator is `z^8-t z^4+t^2`.
Both left and right minimal indices are `(2,2)`. The pencil has rank
eight at every point of P1. Here `5r=2(a+b)=40` exactly.

More generally epsilon=2 always gives `5r=2(a+b)`. Hence the earlier
argument that **every pencil has a linear parameter annihilator** cannot
replace its strict inequality by a weak one, even with constant projective
rank, rectangular dimensions, arbitrary field, or extra copies obtained
by increasing both nullities. An index-only argument cannot decrease the
degree bound at any of the equality cases in (3).

This is a limitation of that intermediate argument. It does **not**
disprove a Segre-image dimension bound at the boundary, construct the
large symbol image needed for a matrix block, or prove that the remaining
ordinary A10 formats are realizable. It does not change the finite
frontier, give a source degeneration, or improve the exponent 9/4.

## 5. Prior work, external source, and verification

The prior local [Hankel pencil proof](../2026-10-21-hankel-pencil-degree/proof.md)
derives `(a+b-2r)*epsilon<=r` from the external index sum theorem. Its
existing 8-by-8 rank-seven quadratic control already shows that linearity
fails without the hypotheses. The present all-degree family attains
equality, in particular at the exact first nonlinear A10 boundary; it
does not claim the earlier observation as new.

The external source is Fernando De Teran, Froilan M. Dopico and D. Steven
Mackey, *Spectral equivalence of matrix polynomials and the index sum
theorem*, MIMS EPrint 2013.47, August 22, 2013,
[Lemma 6.3 and Theorem 6.5, printed pages 37-38](https://eprints.maths.manchester.ac.uk/2017/01/covered/MIMS_ep2013_47.pdf).
Those results cover arbitrary fields and rectangular pencils. Their
statements and surrounding proofs were inspected in this session. No
historical priority for these elementary pencil constructions is claimed.

`verify.py` checks the full homogeneous annihilation identities and both
symbolic antidiagonal minors in the declared finite grid. The separate
test directly solves coefficient linear systems for polynomial kernel
vectors, without using P, and checks their complete dimension sequences
over Q and finite fields. These finite controls support this written
all-size proof; they do not prove its universal quantifiers by enumeration.
