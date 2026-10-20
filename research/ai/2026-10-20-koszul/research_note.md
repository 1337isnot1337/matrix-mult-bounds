# Koszul ranks and the mixed-sector frontier

Date: 2026-10-20. AI-derived work by Codex, directed by the repository owner.
Starting revision: `e0d7ed5c9d614adaca7fb93a7b3f04e899cf5cac`.

## Status and question

This investigates R3: which dimension-feasible shared-leg convolution packings
can actually be degenerations? It also supplies an exact obstruction for the
unfinished stronger search. **No smaller matrix-multiplication exponent is
established.** The proofs below are written and unreviewed, not Lean-formalized.
The first two research archives are unchanged.

The main result is a formula for every Koszul flattening of an arbitrarily
oriented convolution, including an embedding in a larger shared space. Applied
to the prior search, it rejects all 85 saved candidate packings. This covers
those specific packings, not every packing in the 189 source/orientation cases.
In particular, replacing a rejected optimum by a different packing is allowed.

Koszul flattenings and their semicontinuity are standard tools, already used in
the second-pass archive. Polynomial evaluation/interpolation and the convolution
rank are external baseline facts from OpenAI, Section 4, at revision
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`. The formulas here are rederived
self-containedly; no claim of historical priority is made.

## 1. Definition and the degeneration test

For $T\in X\otimes Y\otimes Z$, $\dim X=H$, define

$$K_p(T):Y^*\otimes\Lambda^pX\longrightarrow Z\otimes\Lambda^{p+1}X,
\quad \beta\otimes\xi\longmapsto
\sum_\ell\beta(y_\ell)z_\ell\otimes(x_\ell\wedge\xi),$$

where $T=\sum_\ell x_\ell\otimes y_\ell\otimes z_\ell$.
Its matrix entries are linear in $T$. Rank is invariant under invertible changes
of basis and cannot increase in an orbit closure, because bounded-rank matrices
are cut out by minors. This also handles restrictions in the fixed ambient
spaces: singular substitutions are limits of invertible ones. Smaller target
spaces are padded with zero coordinates before comparing.

If $T=\sum_iT_i$ has pairwise disjoint $Y_i$ and $Z_i$, the map is a direct sum
on those two factors, despite the common $X$. Thus

$$\operatorname{rank}K_p(T)=\sum_i\operatorname{rank}K_p(T_i).$$

Each block may use a different injective identification of its shared space in
$X$. Its individual rank is unchanged: every such identification extends to an
invertible ambient map. The test therefore does not assume common block bases.

## 2. Shared output: maximal-rank formula

Let the output of $C(a,b)$ be $X$, of dimension $m=a+b-1$, and let $Y,Z$ have
dimensions $a,b$. Then for $0\le p<m$,

$$\boxed{\operatorname{rank}K_p(C(a,b))
=\min\left\{a\binom mp,\ b\binom m{p+1}\right\}.} \tag{1}$$

Choose $m$ distinct complex numbers $\alpha_i$. Evaluation and interpolation
express the tensor as $\sum_{i=1}^m e_i\otimes v_i\otimes w_i$, where the
$e_i$ form a basis, $v_i=(1,\alpha_i,\ldots,\alpha_i^{a-1})$ and
$w_i=(1,\alpha_i,\ldots,\alpha_i^{b-1})$. Every $a$ of the $v_i$ and every
$b$ of the $w_i$ are independent by the Vandermonde determinant.

Write a kernel vector as $\sum_{|S|=p}\beta_S\otimes e_S$. For every set $U$
of size $p+1$, its image coefficient is

$$\sum_{i\in U}\pm\beta_{U\setminus\{i\}}(v_i)w_i=0.$$

When $p\le b-1$, the $w_i$ in each equation are independent. Hence, for fixed
$S$, $\beta_S(v_i)=0$ for every $i\notin S$. There are $m-p\ge a$ such
vectors, so $\beta_S=0$. The map is injective. For $p\ge b-1$, transpose the
map, exchange $a,b$, and use the exterior pairing to replace $p$ by $m-1-p$.
The just-proved injectivity gives surjectivity. At $p=b-1$ both dimensions equal
$m\binom{m-1}{b-1}$, proving (1) throughout.

Consequently, $k$ copies of $C(a,b)$ sharing their full output space and having
disjoint inputs have border rank exactly $km$. The Koszul lower bound at
$p=b-1$ is $km$, since a rank-one tensor has Koszul rank
$\binom{m-1}{p}$. Concatenated interpolation decompositions give rank at most
$km$. The conclusion allows arbitrary invertible identifications of the shared
outputs. The same proof gives additivity for blocks of the same ordered input
dimensions; it is not an unrestricted border-rank additivity theorem.

For the previous optimum, three $C(4,7)$ blocks need border rank at least $30$.
Their proposed source $C(10,12)$ has rank $21$. That candidate is impossible.

## 3. Shared input: the exact kernel dimension

Now $X$ is the $a$-dimensional first input, $Y$ is the $b$-dimensional second
input, and $Z$ is the $(a+b-1)$-dimensional output. For $0\le p<a$,

$$\boxed{\operatorname{rank}K_p(C(a,b))
=b\binom ap-\binom{a-1}{p-1}\max\{b-a+p,0\}.} \tag{2}$$

Binomial coefficients with lower index outside its usual range are zero.
Here is a proof including the vector-bundle calculation behind the kernel.
Identify coefficient vectors of length $b$ with homogeneous binary forms of
degree $b-1$. The map wedges such a vector-valued form with

$$x(s,t)=(s^{a-1},s^{a-2}t,\ldots,t^{a-1}).$$

On $\mathbb P^1$, this nowhere-zero vector defines an inclusion
$L=\mathcal O(-(a-1))\hookrightarrow\mathcal O^a$. Let $Q$ be its quotient.
The dual evaluation map $\mathcal O^a\to\mathcal O(a-1)$ has kernel
$\mathcal O(-1)^{a-1}$: its columns are the adjacent syzygies
$t e_i-s e_{i+1}$, which are independent at every point $[s:t]$ and annihilate
$x(s,t)$. Taking duals gives $Q\cong\mathcal O(1)^{a-1}$.

Fiberwise, the kernel of wedging with $x$ on $\Lambda^p\mathcal O^a$ is
$L\otimes\Lambda^{p-1}Q$. Twisting by $\mathcal O(b-1)$ gives

$$\ker K_p\text{ as a sheaf}
\cong\mathcal O(b-a+p-1)^{\binom{a-1}{p-1}}.$$

Taking global sections preserves kernels. Since degree-$d$ homogeneous binary
forms have dimension $\max\{d+1,0\}$, the actual coefficient-map kernel has
dimension $\binom{a-1}{p-1}\max\{b-a+p,0\}$. Subtract this from the domain
dimension to get (2). The case $p=0$ is injective directly; $a=1$ is included.

Swapping $Y$ and $Z$ replaces $p$ by $a-1-p$ and preserves the rank. This
accounts for every leg orientation, including repeated dimensions.

## 4. Padding the shared space

If the concise shared dimension is $h\le H$, write $X=U\oplus W$ with
$\dim U=h$, $\dim W=H-h$. Decompose exterior powers by their $W$-degree.
Wedging with the tensor preserves that degree, so

$$\boxed{K_p^{(H)}\text{ has rank }
\sum_{q=0}^{H-h}\binom{H-h}{q}\operatorname{rank}K_{p-q}^{(h)}.} \tag{3}$$

Together, (1)-(3) compute source and target ranks with integers alone. No
numerical rank thresholds or unproved maximal-rank guesses enter the audit.

## 5. Exact audit and scope

`koszul.py` reads the unchanged second-pass compressed report, pins its SHA-256,
and records every source rank, block rank, target sum and obstructing exterior
degree. All 85 saved candidates have a target rank strictly exceeding the source
rank. The test includes mixed input/output blocks and smaller shared dimensions.

For example, the $C(3,3)$ candidate with $C(2,2)$ and a size-three dot-product
block has source rank $8$ and target rank $9$ at $p=1$. This recovers its earlier
symmetrizer rejection with a single Koszul test.

The finite replay confirms that the formulas reject the saved packings.
Independent exact matrices on a small grid test the formulas against coefficient
linear algebra. The written proof, not that finite grid, supports all sizes.

```sh
python research/ai/2026-10-20-koszul/koszul.py \
  --output results/koszul-2026-10-20/candidate_audit.json
python -m unittest discover -s tests -p test_koszul.py -v
```

## 6. An all-size family that these necessary tests do not exclude

The preceding rejection must not be extrapolated to all mixed-sector packings.
For every integer $k\ge1$, consider source $C(4,10k)$, with dimensions
$(4,10k,10k+3)$ and the four-dimensional input as shared leg. The proposed
target has $k$ blocks of each of these ordered nonshared dimensions:

$$ (1,4),\quad(4,1),\quad(2,3),\quad(3,2).$$

Each block is a convolution with its **output** identified with the common
four-dimensional leg. The other two legs are disjoint across all $4k$ blocks.
Each of their total dimensions is $10k$, so all three ordinary flattening
dimensions fit. Arbitrary invertible identifications of the shared outputs give
the same shared-leg Koszul ranks.

In increasing exterior degrees $p=0,1,2,3$, formulas (1)-(2) give

$$\operatorname{rank}K_p(\mathrm{source})
  =(10k,30k+3,30k+6,10k+3),$$
$$\operatorname{rank}K_p(\mathrm{target})
  =(10k,30k,30k,10k).$$

Thus **every shared-leg Koszul inequality passes for every k**, with slack
$(0,3,6,3)$. This is a proof of a limitation of this screening family, not proof
of the proposed degeneration. Section 7 also certifies the full-space Koszul
tests on the other two legs for the canonical common coefficient basis.

Its matching-profile scores are

$$P_*(4,10k)=\frac{1400k+210}{81},\qquad
\sum_iP_*(T_i)=k\left(2\cdot4+2\cdot\frac{14}3\right)=\frac{52k}3.$$

The target-minus-source surplus is exactly

$$\boxed{\frac{4k-210}{81}},$$

which is positive precisely for integers $k\ge53$. At $k=53$ the source is
$C(4,530)$, the target has 212 blocks, and the scores are $74410/81$ and
$74412/81$. The ratio is $37206/37205$. As $k\to\infty$, the ratio tends to
$351/350$.

This family was obtained analytically by balancing the interior Koszul ranks
of output-oriented dot-product and $C(2,3)$ blocks. It is not one of the 85
archived optima. The report `mixed_family.json` checks the displayed formulas
at $k=1,52,53,54,100$; the proof above supplies the all-k assertion.

**Remaining construction question:** does $C(4,10k)$ degenerate to such a target
for any $k\ge53$, allowing independent shared-output basis choices? No such
degeneration is constructed here, and no impossibility theorem is claimed.
Section 8 excludes the coordinate-selection and diagonal-weight ansatz; a
successful construction would have to use more general changes of basis.
Any construction would refute the pointwise scalar model $P_*$, because the
shared-leg inequality gives the sum of block profiles. A finite refutation
alone would not lower the exponent: the asymptotic growth implication must
still be proved. Even constructions for every k in this fixed-shared-dimension
family would first improve a thin-profile coefficient, not automatically the
diagonal growth exponent.

```sh
python research/ai/2026-10-20-koszul/mixed_family.py \
  --output results/koszul-2026-10-20/mixed_family.json
```

## 7. A target certificate and survival of all three full-leg Koszul families

Use the same coefficient basis of binary cubics for the shared outputs. The
four-block tensor for $k=1$ is

$$T=\sum_{a+b+c+d=3}X_{a+c}Y_{a,b}Z_{c,d},$$

where each input has the ten monomials of total degree at most three. It is the
degree-three part of the product of two such polynomials. Splitting by input
degrees gives precisely the four blocks in Section 6. The target for general
k is $T\otimes B_X(k)$.

**Explicit certificate.** Evaluate polynomials of total degree at most three
at the ten integer nodes $(s,t)$ with $s,t\ge0$ and $s+t\le3$. Their evaluation
matrix $V$ is invertible. For example, the falling-factorial basis indexed by
the same lower set makes the matrix triangular with nonzero factorial diagonal.
Let $w_{x,h}$ be the coefficient of $s^xt^{3-x}$ in the h-th interpolation basis
polynomial, equivalently the corresponding entry of $V^{-1}$.

The following sum has ten rank-one terms for every nonzero epsilon:

$$\sum_{h=1}^{10}\epsilon^{-3}
 \left(\sum_{x=0}^3w_{x,h}X_x\right)
 F(\epsilon s_h,\epsilon t_h)G(\epsilon s_h,\epsilon t_h). \tag{4}$$

For an input monomial product of total degree d, its contribution has power
$\epsilon^{d-3}$. Interpolation reproduces degrees at most three, so all
coefficients with $d<3$ vanish, and the degree-three coefficients are exactly
the required ones. Degrees above three vanish in the limit. Thus (4) is a
border-rank-ten certificate for T, with polynomial error of degree at most
three after cancellation. Its Y-flattening has rank ten: each Y row has a
nonempty support disjoint from every other row. Therefore

$$\underline R(T)=10,\qquad
\underline R(T\otimes B_X(k))=10k.$$

The second equality follows from concatenating k copies of (4) for the upper
bound and the $10k$-dimensional input flattening for the lower bound. It does
not invoke general additivity of border rank. `fatpoint.py` exports the ten
nodes, all rational weights and the exact leading tensor, checking all 400
coefficient positions, including 60 negative-power cancellations and 80
constant-coefficient comparisons.

**Other-leg Koszul tests.** Write $B=10k$. Along the B-dimensional source input,
formula (2) is full column rank $4\binom Bp$ for $p\le B-4$, so no target in
the same spaces can exceed it. For $p\ge B-3$, it is
$(p+4)\binom{B-1}p$. The target's border rank B bounds its Koszul rank by
$B\binom{B-1}p$, strictly smaller. Along the $(B+3)$-dimensional source output,
formula (1) is maximal matrix rank in every degree; padding the target by three
zero output coordinates cannot exceed that rank. Section 6 handled the remaining
four-dimensional leg.

Hence the canonical target passes **all full-space Koszul flattenings on all
three legs**, as well as the ordinary flattenings and border-rank comparison.
This does not cover projected Koszul tests, other Young flattenings, or other
orbit-closure equations. Certificate (4) starts from a diagonal tensor of rank
ten, not from $C(4,10k)$; it does not supply the missing source degeneration.

## 8. Why coordinate selection and diagonal weights cannot realize it

Here the allowed maps retain subsets of the source monomial coordinates,
rescale them, and apply integer weights; each target block must be recognized
by coordinate reindexing. Arbitrary linear combinations of coordinates are
outside this obstruction.

A block with nonshared sizes $(u,v)$, $u+v=5$, and shared output size four has
a full $u\times v$ rectangle of terms. In $C(4,B)$ a supported pair obeys
$0\le z-y\le3$. If its retained Y and Z coordinates have widths $w_Y,w_Z$,
then $w_Y+w_Z\le3$, while their cardinalities give
$w_Y+w_Z\ge(u-1)+(v-1)=3$. Thus both coordinate sets are intervals, and if its
Y interval starts at b, its Z interval is $[b+u-1,b+3]$.

One surviving $C(2,3)$ rectangle forces the four X weights to be affine in
their index: subtracting its zero-weight equations gives
$w_X(1)-w_X(0)=w_X(2)-w_X(1)=w_X(3)-w_X(2)$. The affine part can be absorbed
into Y and Z weights using $x=z-y$. In the resulting weights every block has
a constant Y weight $c_i$ and a constant Z weight $-c_i$. Every cross term
from block i's Y interval to block j's Z interval has weight $c_i-c_j$.
If cross terms exist in both directions, neither can be retained, so both
$c_i-c_j>0$ and $c_j-c_i>0$ would be required. This is impossible.

Order the blocks by their disjoint Y intervals. Take adjacent blocks of widths
$u,u'\le3$. If they have no unused Y coordinate between them, the source has
cross terms in both directions: the first Y interval reaches the next Z
interval since $u'\le3$, and the next Y interval reaches the first Z interval
since $u\le3$. If their Z intervals overlap, the target is already invalid.
Therefore each adjacency between two blocks of Y width at most three requires
at least one unused Y coordinate.

There are $3k$ such blocks and only k width-four blocks. The small blocks form
at most $k+1$ runs, leaving at least $3k-(k+1)=2k-1$ small-small adjacencies.
Their occupied Y coordinates total $10k$. Consequently any degeneration in
this ansatz requires

$$\boxed{B\ge10k+(2k-1)=12k-1>10k.} \tag{5}$$

This eliminates the candidate family from the monomial search class at every
k. It does not eliminate arbitrary basis changes. The construction problem in
Section 6 is deliberately left at that sharper boundary.

## Sources

- OpenAI, *An Upper Bound of 9/4 for the Matrix Multiplication Exponent*,
  [pinned manuscript](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/paper.pdf),
  Section 4: definition and interpolation rank of $C(a,b)$.
- [Second-pass local note](../2026-10-20-session2/research_note.md), Sections 1-3:
  the dimension relaxation, finite Koszul check, and symmetrizer example.
- [First-pass local note](../2026-10-20/research_note.md), Section 2: the scalar
  profile used only to score candidates, not to certify their existence.
