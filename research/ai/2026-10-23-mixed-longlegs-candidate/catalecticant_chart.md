# A catalecticant obstruction to an invertible leading first map

Date: 2026-10-23. Owner-directed AI research. The coordinating agent
proposed the catalecticant test and its canonical ranks. The frontier
agent verified those ranks and supplied the universal block lower
bounds below. These are written deductions in one generating session,
not an external independent review or a complete candidate rejection.

## 1. Result and scope

Let S=10 Full(5,10) be the canonical source in the frozen candidate.
Let T be its proposed target

\[
7\,\mathrm{Full}(5,2)+10\,\mathrm{Full}(5,3)
+4\,O(3,3)+2\,O(4,2)+6\,\mathrm{Mid}(5,2),
\]

with separate B and C intervals. Each target block may have an
arbitrary independent invertible change of its first space. The source
has its common canonical first basis. Over the complex numbers, the
middle first-factor catalecticant defined below satisfies

\[
\operatorname{rank}H(S)=120,
\qquad
\operatorname{rank}H(T)\ge130.
\tag{1}
\]

The target bound is attained by its canonical identifications. It
continues to hold after any further global invertible first map.

Consequently, in any Laurent degeneration from S to any such target,
the first map cannot have an invertible leading limit after scalar
normalization. Its nonzero leading matrix must have rank at most four.
The theorem does not exclude singular leading first maps and does not
decide the candidate's full orbit-closure question.

This is a structured first-factor test. Its rank is not invariant under
arbitrary GL(5) changes of the first factor. The proof of the stated
chart obstruction uses universal lower bounds on the target, followed
by a regular inverse; it does not assert global degeneration monotonicity
of a minimum over first bases.

## 2. Literal convention

Write A with basis x_0,...,x_4 and let V have basis e_0,e_1,e_2.
Use the coefficient Hankel map

\[
h:A\longrightarrow V\otimes V,
\qquad h(x_i)=\sum_{r+s=i}e_r\otimes e_s,
\quad0\le r,s\le2.
\tag{2}
\]

This is the middle binary catalecticant in divided-power coordinates.
Equation (2) fixes every coefficient, so no implicit binomial scaling
is used. For T=sum_i x_i tensor T_i, with T_i:B* -> C, define

\[
H(T):V^*\otimes B^*\longrightarrow V\otimes C,
\qquad H(T)=(T_{r+s})_{0\le r,s\le2}.
\tag{3}
\]

Thus a block of dimensions (5,b,c) gives a 3c-by-3b matrix. Swapping
B and C transposes (3), up to the ordering of the displayed bases.
For long-factor maps P on B and Q on C, the exact matrix identity is

\[
H((I_A\otimes P\otimes Q)T)
=(I_V\otimes Q)H(T)(I_V\otimes P^{\mathsf T}).
\tag{4}
\]

In particular H rank cannot increase under maps on B and C alone,
or in their limits. No statement like (4) is used for arbitrary
first-factor maps.

## 3. The imported Segre dimension bound

We use the following standard consequence of the projective dimension
theorem. If a complex linear map L:X tensor Y -> Z has no nonzero
decomposable vector in its kernel, then

\[
\operatorname{rank}L\ge\dim X+\dim Y-1.
\tag{5}
\]

For attribution, this is the two-factor upper bound on completely
entangled subspaces in K. R. Parthasarathy, *On the maximal dimension
of a completely entangled subspace for finite level quantum systems*,
arXiv:quant-ph/0405077v1, 14 May 2004, Proposition 1.4 and Theorem 1.5,
[primary PDF](https://arxiv.org/pdf/quant-ph/0405077). The hypotheses
used here are finite-dimensional complex vector spaces and absence of
all nonzero product vectors. No positivity or orthogonality assumption
is needed for this direction.

For completeness, put x=dim X and y=dim Y. Product lines form the
Segre variety of dimension x+y-2 in projective space of dimension
xy-1. If dim ker L were at least (x-1)(y-1)+1, its projectivization
and the Segre variety would have dimensions summing to at least xy-1.
The projective dimension theorem forces an intersection, contradicting
the hypothesis. Thus dim ker L<=(x-1)(y-1), which gives (5).
The rank bound is imported; the block applications below are local
deductions.

## 4. Full and Mid blocks under every invertible first identification

The multiplication tensor Full(5,b) has no nonzero zero-product pair
under the contraction A* times B* -> C. A product of two nonzero
polynomials is nonzero. This property persists under every invertible
change of A.

Let q=(q_0,q_1,q_2) be a nonzero element of V*. For a nonzero beta in
B*, the output of H(T) on q tensor beta has r-th V component

\[
T(\alpha_r,\beta),\qquad
\alpha_r=\sum_{s=0}^2q_s x_{r+s}^*.
\]

The covector alpha_0 is nonzero. Zero-free contraction therefore makes
this component nonzero. Thus ker H(T) contains no nonzero product
vector in V* tensor B*. Applying (5) gives

\[
\operatorname{rank}H(g\cdot\mathrm{Full}(5,b))\ge b+2
\qquad(g\in\mathrm{GL}(5)).
\tag{6}
\]

The canonical rank is exactly b+2. Indeed, writing the three input
polynomials as f_0,f_1,f_2 of degree at most b-1, (3) sends them to

\[
(1,z,z^2)\bigl(f_0+zf_1+z^2f_2\bigr).
\]

The parenthesized polynomial ranges over all degrees at most b+1,
and multiplication by the nonzero vector (1,z,z^2) is injective.
This also covers b=1. Therefore the minimum over invertible first
changes is exactly b+2.

Mid(5,b) swaps the two long legs of Full(5,b). Transposition of (3)
shows that its universal minimum is also b+2. In particular the
target minima are 4 for Full(5,2), 5 for Full(5,3), and 4 for Mid(5,2).

## 5. Shared-output blocks under every invertible first identification

For q in V*, contracting (2) with q on either V factor gives

\[
L_q:A\longrightarrow V,
\qquad (L_q a)_r=\sum_{s=0}^2 q_s a_{r+s}.
\tag{7}
\]

Every nonzero q gives rank L_q=3 and dim ker L_q=2. To see this,
transpose (7): it is multiplication by the nonzero polynomial
q_0+q_1z+q_2z^2 on polynomials of degree at most two, into polynomials
of degree at most four. Polynomial multiplication is injective.

Now let O(d,e)=sum_{j,k} x_(j+k) tensor y_j tensor z_k, where d+e=6.
Fix a nonzero gamma in C*. The image in A of

\[
B^*\longrightarrow A,\qquad\beta\longmapsto O(d,e)(\beta,\gamma)
\]

has dimension d: it is multiplication of a length-d polynomial by
the fixed nonzero length-e polynomial gamma. Applying an arbitrary
g in GL(A) preserves that dimension.

If H(g O(d,e))^T annihilated q tensor gamma with both factors nonzero,
equation (7) would annihilate this entire d-dimensional image. For
d>=3 that would put a space of dimension at least three in a kernel
of dimension two, which is impossible. Thus the transpose has no
nonzero decomposable kernel in V* tensor C*. Applying (5) gives

\[
\operatorname{rank}H(g O(d,e))\ge e+2\qquad(d\ge3).
\tag{8}
\]

In particular O(3,3) has rank at least five and O(4,2) rank at least
four under every invertible first change. For completeness, when
e>=3 the original orientation gives the symmetric lower bound d+2.

The canonical ranks attain the relevant lower bounds. A row of (3)
is indexed by (r,k) and a column by (s,j); its entry is one exactly
when r+s=j+k. Equivalently r-k=j-s. Grouping rows and columns by
this common integer gives disjoint all-ones blocks. For d=e=3 there
are five nonempty groups, and for d=4,e=2 there are four. Each has
rank one. More generally the rank is
min(2,d-1)+min(2,e-1)+1=min(d,e)+2 when d+e=6.

## 6. Aggregation and the Laurent chart

Reordering V tensor direct sums makes (3) block diagonal across the
target's separate B and C intervals. The block lower bounds therefore
add, even when the first identifications differ independently:

| Target block | Multiplicity | Universal minimum | Contribution |
| --- | ---: | ---: | ---: |
| Full(5,2) | 7 | 4 | 28 |
| Full(5,3) | 10 | 5 | 50 |
| O(3,3) | 4 | 5 | 20 |
| O(4,2) | 2 | 4 | 8 |
| Mid(5,2) | 6 | 4 | 24 |
| Total | | | 130 |

The canonical source has ten blocks of rank 10+2=12, hence rank 120.
This proves (1).

Suppose Laurent matrices a(t),b(t),c(t) give a tensor series

\[
T(t)=(a(t)\otimes b(t)\otimes c(t))S\longrightarrow T.
\]

Multiply a(t) by a scalar power of t, compensating in b(t), so that
a(t) has power-series entries and a nonzero reduction a_0. Suppose
for contradiction that a_0 is invertible. Then a(t)^(-1) also has
power-series entries, and

\[
Q(t)=(I_A\otimes b(t)\otimes c(t))S
=(a(t)^{-1}\otimes I_B\otimes I_C)T(t)
\longrightarrow(a_0^{-1}\otimes I_B\otimes I_C)T.
\tag{9}
\]

The right side shows that Q(t) has a regular limit, despite possible
poles in its individual long-factor maps. Over C((t)), (4) gives
rank H(Q(t))<=120. Every minor of size 121 consequently vanishes;
its constant term vanishes as well. The limiting H matrix has rank
at most 120.

But a_0^(-1) composed with each target identification is still
invertible. The universal target lower bound gives limiting rank
at least 130, a contradiction. Thus every scalar-normalized first
map has singular nonzero leading matrix. This conclusion permits
arbitrary long-map poles, arbitrary mixing of source copies, and
arbitrary independent target first identifications. It excludes only
the invertible leading first chart.

## 7. Exact controls and unresolved scope

The standard-library verifier constructs the literal coefficient
matrices. It checks the six canonical block ranks, the candidate
totals, further Full/Mid widths and all five output shapes, selected
invertible first changes, and the transpose convention. It also
checks (7) on a finite set of nonzero quadratic coefficient vectors.
The universal assertions follow from the proof, not from those
finite samples. Separate tests check long-factor covariance directly.

The original candidate input and earlier result files are unchanged.
This additive theorem narrows the necessary form of a possible
degeneration. It supplies no singular-first-map construction, no
complete degeneration obstruction, and no matrix multiplication
exponent improvement.
