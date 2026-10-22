# A gap between zero and three under balanced two-dimensional punctures

October 21, 2026. Owner-directed Codex work. Written and unreviewed.
No formalization, independent review, historical priority, matrix target,
or exponent improvement is claimed.

**Theorem.** Let Z be a complex matrix space of dimension at least two,
with no nonzero matrix of rank one. Amplify it by the full auxiliary
space Mat2. Apply quotient maps to its two matrix legs, whose kernels
have dimensions at most two. The projected matrix space either is zero
or has dimension at least three.

The dimension condition, rank-one exclusion and complex field all matter.
Exact controls below show that dimension three is attainable and give
counterexamples when either of the first two assumptions is removed.
This is a statement about first-flattening dimension, not the minimum
ordinary rank of an individual projected matrix.

## 1. Reduction to exact two-dimensional kernels

Restrict to the joint row and column supports of any chosen subspace of Z.
The intersections with the original quotient kernels have dimensions at
most two. If a nonzero projected matrix survives, both kernel intersections
can be extended to dimension two while preserving that matrix: choose a
pair of covectors with nonzero evaluation on it, and place the extra kernel
directions in their annihilators. All support sizes used below are at least
four after amplification, so the needed extensions exist. Thus a nonzero
image of dimension at most two would persist with exact kernels of size
two on the relevant support. We use that reduction when applying the
small canonical pencil arguments.

Write K,L for exact two-dimensional kernels. A matrix of rank R can
lose at most four ranks under these two quotients. A subspace of Mat2
consisting entirely of matrices of rank at most one has dimension at
most two. If it has dimension two, it has one common row line or one
common column line: for two decomposable matrices, independence on both
sides would make their sum have rank two. This is elementary and holds
over C.

## 2. A slice of rank at least four already gives a sufficient gap

Fix M in Z of rank R and consider its four-dimensional auxiliary space
M tensor Mat2. If R>=5, every nonzero auxiliary matrix gives ordinary rank
at least five, and therefore cannot be killed. Its projected dimension
is four.

Suppose R=4 and its projected dimension were at most two. The auxiliary
kernel has dimension at least two and contains no invertible matrix:
M tensor X would then have rank eight, exceeding the possible loss four.
It is consequently a two-dimensional common-row or common-column
rank-one space. In the common-row case it contains e tensor f0 and
e tensor f1 for independent f0,f1. Each associated rank-four matrix
is completely killed with equality in the rank loss. Equality forces
K inside im(M) tensor e and L inside row(M) tensor fj. The latter two
containments have zero intersection, contradicting dim L=2. Transposition
handles the common-column case. The projected dimension is at least three.

## 3. A rank-three slice excludes a low-dimensional image of a larger Z

Assume that the whole projected space has dimension at most two and
M has rank three. Its auxiliary kernel contains no invertible matrix,
so the preceding rank-one-space observation forces a two-dimensional
common-row or common-column kernel. Its projected dimension is exactly
two. Exchange the matrix legs if necessary and write the kernel as
e tensor F, where F is the two-dimensional auxiliary column space.

For every nonzero f in F the matrix M tensor e tensor f, of rank three,
is killed. Put

    a=dim(K intersect (im M tensor e)),
    b_f=dim(L intersect (row M tensor f)).

Rank loss gives a+b_f>=3. Since both are at most two, a<=1 would force
L to contain two different two-dimensional subspaces in disjoint f fibers.
Hence a=2 and K lies in im M tensor e. Each f fiber meets L nontrivially.
It follows that L=v tensor F for a line v in row M: choose vectors from
the f0 and f1 fibers and then their f0+f1 fiber; their base factors must
be proportional. No classification theorem is needed for this step.

Let Mbar be M after quotienting its column leg by v. It has rank two.
Complete cancellation in auxiliary row e now forces

    K=U2 tensor e,  U2=im Mbar.

Choose a complementary auxiliary row e'. The projected image of
M tensor Mat2 is precisely Mbar tensor e' tensor F, of dimension two.
For any N in Z let Nbar be the same column quotient. Its auxiliary
row-e outputs lie, modulo K, in (U/U2) tensor e. These row directions
are disjoint from U2 tensor e', so they must vanish if the whole image
has dimension at most two. Thus im Nbar is contained in U2.

The remaining auxiliary row-e' outputs span

    span(Mbar,Nbar) tensor F.

Dimension at most two forces Nbar to be a scalar multiple alpha*Mbar.
Therefore N-alpha*M lies in U tensor v and has rank at most one. Choosing
N independent of M contradicts the rank-one exclusion. A space Z of
dimension at least two containing a rank-three slice cannot have projected
dimension one or two (or zero, since a rank-six amplified slice survives
at least two ordinary ranks).

## 4. The remaining constant-rank-two pencils

We may now suppose every nonzero matrix in Z has rank exactly two.
Choose any two-dimensional pencil W inside Z and discard common zero
rows and columns. We use the classical complex Kronecker canonical form:
a pencil is a direct sum of regular blocks and singular blocks L_j or
their transposes, where L_j has size j by j+1 and constant projective
rank j. Every nonzero regular block loses rank at some complex projective
parameter. The source is the Netlib book chapter
[Kronecker Canonical Form](https://netlib.org/utk/people/JackDongarra/etemplates/node309.html),
whose complex-matrix hypotheses and regular/singular block definitions
were inspected and whose fetched bytes are pinned in sources.json.

Constant projective rank two excludes every regular block. Removing
zero rows and columns removes L_0 blocks. Summing the positive singular
indices to two leaves just

    L2, L2^T, L1 direct_sum L1, L1^T direct_sum L1^T,
    L1 direct_sum L1^T.                                  (1)

These classical normal forms are external input. The gap arguments for
their amplified quotients follow below. The mixed last form is equivalent,
by row/column permutations and signs, to the skew pencil

    [[0,s,t],[-s,0,0],[-t,0,0]].                          (2)

## 5. The unbalanced pencil cases leave dimension at least three

For L2 take [[s,t,0],[0,s,t]]. After amplification and a row quotient
with two-dimensional kernel, write its full-rank two-by-four map as
[P0 P1], with P0,P1 of size two. The projected matrices before the
column quotient are

    [P0 S, P0 T+P1 S, P1 T],  S,T in Mat2.               (3)

If det(P0+z P1) is not identically zero, (3) depends injectively on
the eight coefficients of S,T. Indeed each column satisfies the
polynomial identity (P0+zP1)(s+zt)=0 if (3) vanishes, forcing s=t=0.
Any matrix killed by the subsequent two-dimensional column kernel has
both rows in that fixed kernel. Such matrices form a space of dimension
at most four. The remaining first dimension is at least 8-4=4.

If that determinant is identically zero, the rank-one pencil observation
and full row rank of [P0 P1] give P0=u*alpha, P1=v*alpha with independent
u,v and a nonzero row alpha. Thus (3) is a four-dimensional space whose
two rows, after a change of output basis, are

    [s,t,0], [0,s,t],   s,t in C^(1 by 2).

Every nonzero such matrix has rank two. A killed subspace of dimension
two would give a two-dimensional space of invertible two-by-two matrices
after identifying the fixed column kernel with C2. Its homogeneous
determinant has a nontrivial complex zero, a contradiction. At most one
first direction is killed, leaving dimension at least three.

For L1 direct_sum L1 the analogous expression is

    [P0 S,P0 T,P1 S,P1 T].                               (4)

If the stack of P0,P1 has rank two, this depends injectively on S,T and
the 8-4 bound applies. Otherwise P0=u*alpha,P1=v*alpha as above; (4)
is four-dimensional and all its nonzero matrices have rank two, giving
the same 4-1 bound. Transposition proves both opposite formats in (1).
These cases never have projected dimension at most two, including zero.

## 6. The skew-pencil case leaves zero or at least four dimensions

For (2), write the quotient maps as P=[P0 P1 P2] and Q=[Q0 Q1 Q2],
each full rank four, with four-by-two blocks. Its projected space is

    P0 S Q1^T-P1 S Q0^T+P0 T Q2^T-P2 T Q0^T.             (5)

Put a=rank P0,b=rank Q0. If a=0, [P1 P2] is invertible and the image
has dimension 4b; similarly b=0 gives dimension 4a. Thus these cases
give zero, four or eight.

If a,b are nonzero, quotienting the output rows by im P0 maps (5) onto
a space of dimension (4-a)b. Quotienting the output columns by im Q0
gives dimension a(4-b). Except when a=b=1, one of these is at least four.
For a=b=1 both dimensions are three. Suppose the full image had dimension
three. Projection onto the first of these three-dimensional images would
then be injective.

Write P0=p*alpha, Q0=q*beta with nonzero auxiliary rows alpha,beta.
For any S,T satisfying S beta^T=T beta^T=0 the first projected image
vanishes, hence all of (5) would vanish. Let Qbar1,Qbar2 be the blocks
after quotienting by im Q0. For arbitrary nonzero row w with w beta^T=0,
alpha S can equal w while S beta^T=0. It follows that Qbar1*w^T=0;
the T equation gives Qbar2*w^T=0. Both blocks have rank at most one, so
their concatenation has rank at most two. It must have rank three because
Q has rank four and Q0 rank one. This contradiction proves dimension at
least four in the last case too.

Sections 5 and 6 prove that each two-dimensional constant-rank-two pencil
has either zero projected image or projected dimension at least three.
If the full image of Z had dimension at most two, every such pencil would
therefore be killed. Every member of Z belongs to a pencil because
dim Z>=2. The whole image is zero. Together with Sections 2 and 3 this
proves the theorem.

## 7. Consequence and remaining scope

The actual third normal tensor of the preceding biform package has matrix
space Mat2 tensor Z_D, with dim Z_D>=2 and no rank-one matrices for every
non-plane normal in its 28-dimensional boundary-compatible family.
Within that family, projected first rank at most two therefore forces
complete cancellation. The preceding projective classification now
describes all its low-first-rank survivors, rather than only its zero
survivors. They have the conic common factor and two-dimensional non-plane
normal fibers proved there.

This does not force a general 10-by10 first-boundary pair into the
28-dimensional normal family: both separate boundary obstruction matrices
can still have rank two. Nor does it prove compatibility of later
coefficients or construct the full matrix slice space. Those are distinct
unresolved steps. The exponent remains 9/4.

## Discovery, attribution and verification limits

The registered pilot checked all 423801 ordered binary RREF kernel pairs
for the skew pencil. Its image dimensions over F2 were 0,4,5,6,7,8;
the only dimension-at-most-two candidate replayed as zero over Q. The
positive rank-one control produced dimension two as required. This finite
screen suggested the gap, but none of the arbitrary-complex-subspace
proof above follows from exhaustion of that grid.

The rank cases, quotient formulas and gap deduction are local AI-assisted
work. The Kronecker theorem retains its classical external credit; its
proof is not rebuilt here. The canonical source and biform geometry retain
their earlier credits. Exact small controls verify sharpness and essential
hypotheses; they do not formalize this written proof or independently
review it. No historical novelty is claimed.
