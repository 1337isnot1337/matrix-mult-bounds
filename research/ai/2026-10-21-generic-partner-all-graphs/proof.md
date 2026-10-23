# Every graph closes outside finitely many partner values

Written proof, unreviewed, October21,2026. Claim
`AI-GENERIC-PARTNER-ALL-GRAPHS-098`. No smaller exponent is established.

Work over C at the canonical A4 leading flags and rank-one partner chart
b=1. Let B have its full maximal seven-frame, and let C be any mixed
five-space in its maximal seven-frame. Its boundary four-space and all
six graph coefficients h are arbitrary.

**Result.** There is a precisely defined nonempty Zariski-open set U in
the single partner parameter a, containing2, such that every graph at
every a in U has only the four common-plane normals. The adopted shifted
induction excludes M(10,10,11) there for arbitrary higher maps, delayed
unequal orders and a Laurent first leg. Since U is open in the affine
line, only finitely many partner values remain outside this result.
Those exceptions are not classified here. The source torus extends the
statement to b nonzero and a/b in U.

This differs from094's open set in(a,h): the present set U depends only
on a, and every graph is excluded at each a in U. The proof uses no
division by any expression in h.

## 1. An initial polynomial enclosure for every a

Adopt the complete88-dimensional normal family and sixteen necessary
source slices from088. Reconstruct the seven312-by88 blocks Z0(a),...,Z6(a)
from the source tensor. The four plane columns are constant and annihilate
both these blocks and the virtual third tensor. A fixed constant
complement has84 coordinates.

Retain094's56 source rows and take a complete polynomial coefficient-row
basis, using the fixed nonzero minor and triangular inverse certificate
from088. This construction is valid at every complex a. Write its six
boundary columns as(E0,O0,E1,O1,E2,O2), and project by

    Q=(O0-a^3*E0,O1-a^3*E1,O2-a^3*E2).

Ten polynomial row combinations W lie in the kernel of this projection.
Their complete stable-boundary coefficient kernel has dimension54 for
every a, certified by a polynomial frame with an identity free block.
The source rows annihilate the actual C five-space, so their evaluated
boundary matrix S has rank at most two. As before,

    rank S >= rank Q + rank W.

Thus W=0 or rank Q<=1. In the second case, specified triangular two-minors
force squares of normal linear forms to vanish. Two complete polynomial
kernel steps give84->64->48, with no exceptional a. Every necessary
normal therefore lies in one of two explicitly constructed polynomial
families of dimensions54 and48, modulo the four planes.

## 2. Guard rational operations by a nonempty open parameter set

Do the subsequent calculations over K=Q(a). Every matrix coefficient
belongs to K and is independent of h. The verifier checks each rational
row basis R of a matrix M using

    M=M[:,P]*R,       R[:,P]=I,

and each rational kernel N using M*N=0 and its identity free-coordinate
block. At a specialization where the coefficients are finite and M keeps
its generic rank, these identities certify complete rowspaces and kernels.
In particular, no exceptional normal direction is lost by specializing
a generic kernel as if it were automatically complete.

Let M_i be the finitely many matrices passed to the verifier's rank
guards, and r_i their exact ranks over K. Let D be the finite collection
of nonconstant coefficient denominators encountered in these identities
and the cubic-span calculations below. Define

    U={a: every d(a)!=0 for d in D, and rank M_i(a)=r_i for every i}.

The current certificate has79 such rank guards. Clearing denominators,
all(r_i+1)-minors vanish identically, so rank at least r_i is an open
condition. Every coefficient is checked to be finite at a=2. At that
point the verifier recomputes every rank over Q and checks the specialized
row bases against complete numeric row reductions. All match r_i.
Thus2 belongs to U; U is nonempty and Zariski open. Its complement is
finite, since a nonzero polynomial in one variable has finitely many roots.

The coefficient poles recorded here involve a and a^3-1. The additional
rank conditions must not be discarded: this proof does not identify the
exceptional set with the poles alone. The matrices defining U are
reconstructed from the source and named in the machine-readable report.

## 3. Uniform graph-independent source operations

Keep all seven C columns throughout. A combination of known source rows
with zero boundary columns is a normal linear form times the mixed
covector. Since the actual C space contains m+sum h_j*d_j, its mixed
coordinate is one and that form must vanish for every h. These are the
complete `mixed_only` kernels in the certificate.

For each adapted virtual third-source slice, subtract its part in the
known coefficient rowspace. The saved residual has either a cover by at
most two B/C vertices or joint B coefficient rank at most two over K.
The latter upper bound persists throughout U by vanishing polynomial
three-minors. The prior saturated target rank gap forces the slice to
annihilate C. Its rows can therefore be added. Every source identity,
cover and rank bound is checked. The adapted source change is polynomial
and unitriangular, with the coefficient -a in its first short-index change.

Saved triangular three-minors give further linear forms whose cubes
vanish. Using complete guarded kernels, these operations reduce the54
stable coordinates to16, and the48 rank-one-projection coordinates to6.
All operations are in a alone; graph coefficients never enter a denominator.

## 4. Cubic spans reduce the two small families

The stable family splits into two eight-variable blocks. In each,
115 actual three-minors span the cubes of five independent linear forms
over K. The verifier checks membership in all120 cubic monomials by the
complete rowspace identities of Section2. At every a in U these forms
therefore vanish, reducing16 coordinates to6.

The other family splits into two three-variable blocks. Six actual
three-minors in each block span the cube of one linear form. Taking the
complete kernels reduces6 to4. Four further low-rank source slices and
triangular cubic minors reduce4 to0. This closes the rank-one branch.

For the stable remainder, write the three variables in either block as
(u,v,w). Five actual three-minors span the two cubic forms

    (v-a^3*w)*(u+v)^2,       (v-a^3*w)*(w-u)^2.

Hence either A: v=a^3*w, or B: u=w and v=-u. This is an exhaustive
complex case split. Combining both source blocks gives four linear
branches with dimensions4,3,3,2. Four more low-rank source slices and
the checked mixed-column/cubic constraints give

    AA:4->0,    AB:3->2->0,    BA:3->2->0,    BB:2->0.

The branch memberships and all reductions are guarded at2 as in Section2.
Thus every quotient normal vanishes at each a in U. Only the four planes
remain, for every actual graph and boundary four-space at that partner.

## 5. Consequence and scope

Apply the credited mixed-space shifted moving-plane induction of089--094.
It permits the stated arbitrary later maps and Laurent first leg, so it
excludes the saturated matrix target for every a in U. The checked source
torus normalizes(a,b) to(a/b,1) and transforms the six graph coefficients
invertibly when b is nonzero. This gives the claimed ratio extension.

Claim097 separately closes the equal nonzero partner, including a=1,
which this rational calculation need not cover. The finitely many other
partner values, boundary charts and different leading flags remain open.
This is a local exclusion, not an improving algorithm or a general lower
bound. Exact replay and CI do not independently review the written proof.
