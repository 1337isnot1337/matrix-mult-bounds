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

## Sources

- OpenAI, *An Upper Bound of 9/4 for the Matrix Multiplication Exponent*,
  [pinned manuscript](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/paper.pdf),
  Section 4: definition and interpolation rank of $C(a,b)$.
- [Second-pass local note](../2026-10-20-session2/research_note.md), Sections 1-3:
  the dimension relaxation, finite Koszul check, and symmetrizer example.
- [First-pass local note](../2026-10-20/research_note.md), Section 2: the scalar
  profile used only to score candidates, not to certify their existence.
