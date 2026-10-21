# Source-independent obstructions for matched convolution blocks

October 21, 2026. AI-derived by Codex. Written proofs with small exact
computational controls; not independently reviewed or formally verified.
No new exponent bound or source degeneration is claimed.

This note investigates a genuinely different source from one-variable
truncated multiplication: could a low-border-rank algebra tensor constrain
the critical convolution profile more strongly simply by packing matched
convolution blocks? The answer depends on which role the shared leg plays.

## 1. All blocks sharing an input: a dimension barrier

Put

$$F(a,b)=\min(a,b)^{1/3}\left(\max(a,b)+\frac{\min(a,b)}2\right).$$

Consider a fixed finite family of convolution blocks whose lengths grow
linearly with N. Suppose every block shares the same leg, and that shared
leg is an **input** of every block. Let the shared input length of block l
be a_l N+o(N), and its other input length be b_l N+o(N). Its two nonshared
dimensions, divided by N, are either (b_l,a_l+b_l) or (a_l+b_l,b_l).

Suppose a source tensor of border rank at most rN+o(N) degenerates to these
matched blocks. At a hypothetical critical character, the power-sum
inequality from Uznanski's Lemma 3.3 and oriented rigidity give

$$K\sum_l F(a_l,b_l)\le r^{4/3}. \tag{1}$$

Using this inequality together with only the source border rank and the
nonshared leg dimensions can never prove an amplitude bound smaller than

$$K\le(16/9)^{1/3}.$$

More precisely, every such configuration satisfies

$$\boxed{\frac{\sum_lF(a_l,b_l)}{r^{4/3}}
\le(9/16)^{1/3}.} \tag{2}$$

Thus replacing W_r by an arbitrary smoothable algebra source, while keeping
this block pattern and the same rank-only upper bound, cannot improve the
existing two-sector critical amplitude certificate.

### Proof

First, F is superadditive on the nonnegative quadrant. Indeed G=F^(3/4)
is homogeneous of degree one and concave. On a>=b it is the weighted
geometric mean

$$G(a,b)=b^{1/4}(a+b/2)^{3/4}.$$

This is concave; the other half-plane is its reflection, and the gradients
match on a=b. Restricting to any line crossing the diagonal shows global
concavity. Homogeneity and concavity give G(u+v)>=G(u)+G(v). Since 4/3>1,
raising to that power gives F(u+v)>=F(u)+F(v).

Merge all blocks with nonshared dimensions (b_l,a_l+b_l), and separately
merge those with dimensions (a_l+b_l,b_l). Write the aggregated input
lengths as (A_+,B_+) and (A_-,B_-), and put

$$A=\max(A_+,A_-),\qquad B=B_++B_-.$$

The two nonshared leg dimensions imply r>=A+B. Superadditivity,
monotonicity and concavity in the second argument give

$$\sum_lF(a_l,b_l)
\le F(A_+,B_+)+F(A_-,B_-)
\le F(A,B_+)+F(A,B_-)
\le2F(A,B/2).$$

It remains to maximize 2F(a,b)/(a+2b)^(4/3). By homogeneity put x=a/b.
For x>=1 the expression is

$$\frac{2x+1}{(x+2)^{4/3}},$$

whose derivative has the sign of 4-x. For 0<=x<=1 it is

$$\left(\frac{x}{x+2}\right)^{1/3},$$

which is increasing. The global maximum occurs at x=4 and equals
(9/16)^(1/3), proving (2). Boundary values follow by continuity.

The existing two-sector W_r construction attains this dimension optimum
asymptotically. This proof concerns all sources with this pattern, not only
monomial restrictions of W_r.

## 2. Shared outputs and mixed roles: prior local work

The dimension argument above requires the shared leg to be an input in every
block. It does not cover output-sharing blocks or mixtures of all three roles.

During this pass, the exact Koszul formulas for those cases were rederived,
then found already present in [the October 20 Koszul
note](../2026-10-20-koszul/research_note.md), Sections 2--4. The duplicate
calculation and code were removed. In particular, that prior local note
already proves

$$\underline R(C(a,b)\otimes B_{\rm output}(k))=k(a+b-1),$$

as well as the full output and input Koszul-rank formulas and the padding
rule for arbitrary shared ambient dimensions. These are prior results, not
advances from this pass. They should be used to screen mixed-role sources.

Exploratory continuous relaxations using those formulas permitted a mixed
three-role packing with an amplitude ceiling around 1.20945. No tensor
realizing the relaxed source cost was constructed. Even such a ceiling
would remain above the established critical amplitude lower bound around
1.11985, so it would not by itself exclude the endpoint. These exploratory
numbers are not used in any theorem or certificate in this note.

## References and scope

- [Uznanski, arXiv:2610.10494v2](https://arxiv.org/html/2610.10494v2),
  Lemma 3.3: the matched-sector power-sum inequality used in (1).
- [Oriented rigidity and stability](README.md), Section 4: the critical
  value K F(a,b) for every orientation.
- [Earlier two-sector amplitude bound](../2026-10-20-truncated-algebras/two_sector_bound.md):
  the attained constant (16/9)^(1/3).
- [Existing Koszul formulas](../2026-10-20-koszul/research_note.md): all
  shared-output, shared-input and ambient-padding formulas.

The retained result in Section 1 is the rank/dimension barrier for an
arbitrary source with all convolution blocks sharing an input. The argument
uses no smoothability or special algebra structure. It does not constrain
an upper bound for the source character that is stronger than its border
rank, and it does not rule out a tensor inequality with a different pattern.
