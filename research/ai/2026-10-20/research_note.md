# Matrix multiplication: first research pass

Date: 2026-10-20

## Status

This pass does **not** establish an exponent below 9/4. It establishes an exact
pointwise minimum for the scalar profile system used in the 9/4 proof, including
a matching example. The example also satisfies the relevant rank upper bound
at t = 3/4 and the convolution-replication inequality. Thus that scalar system
cannot, by itself, exclude t = 3/4.

An additional family of tensor-product filtration inequalities is derived below.
Finite exact checks of that family and a restricted monomial-degeneration search
found no violation of the matching profile. These finite searches do not prove
that all additional tensor inequalities are exhausted.

The proofs here have been algebraically checked and supported by exact-rational
computations. They have not been independently reviewed or formalized in Lean.
No claim of priority is made for the formulas or filtration construction.

## 1. Starting point

Write

\[
C(a,b)=\sum_{i=0}^{a-1}\sum_{j=0}^{b-1}x_i y_j z_{i+j}.
\]

For a tensor character lambda with oriented dot-product exponents p_X, p_Y,
p_Z, put t=(p_X+p_Y+p_Z)/3. The case t=0 causes no difficulty for the square
exponent, so take t>0. Extend the symmetrized profile notation to any nonzero
tensor by

\[
\mathcal P(T)=\left(\prod_{\pi\in S_3}\lambda_\pi(T)\right)^{1/(6t)},
\qquad P(a,b)=\mathcal P(C(a,b)).
\]

The starting paper [1] proves

\[
P(a,b)=P(b,a)>0,\qquad P(1,b)=b,
\tag{S1}
\]

\[
2P(a,b)\ge P(a,b-1)+P(a,b+1)\quad(b\ge2),
\tag{S2}
\]

\[
P(a,3b+a-1)\ge3P(a,b),
\tag{S3}
\]

and the separate upper bound

\[
P(a,b)\le(a+b-1)^{1/t}.
\tag{S4}
\]

Bounding t for every character bounds the square exponent by 3t, through the
spectral argument of [1]. The leaderboard [3] listed 2.25 when checked for this
pass. The finite inequalities and their mathematical consequences, rather than
the leaderboard status, are the starting assumptions here.

## 2. Exact pointwise solution of the scalar system

The product recurrence below already appears as a lower bound in Section 5 of
[1]. The additional result proved here is that its two-variable extension is
feasible and pointwise minimal for the entire scalar system.

Define the rational sequence

\[
h_1=1,\qquad h_{a+1}=\left(1+\frac1{3a}\right)h_a.
\]

For m=min(a,b), M=max(a,b), define

\[
P_*(a,b)=h_m\left(M+\frac{m-1}{2}\right).
\tag{1}
\]

### Theorem

The function P_* satisfies (S1)-(S3). Every positive function satisfying
(S1)-(S3) satisfies P(a,b) >= P_*(a,b) at every positive integer pair.
Consequently P_* is the exact pointwise minimum of this scalar system.

In addition,

\[
P_*(a,b)\le(a+b-1)^{4/3},
\tag{2}
\]

and, for every positive integer q,

\[
P_*(qa,qb)\ge q^{4/3}P_*(a,b).
\tag{3}
\]

The diagonal is

\[
P_*(a,a)=\frac{3a-1}{2}
\frac{\Gamma(a+1/3)}{\Gamma(4/3)\Gamma(a)}
\sim\frac{3}{2\Gamma(4/3)}a^{4/3}.
\tag{4}
\]

The coefficient in (4) is approximately 1.679769782583278. This stronger
prefactor than the simplified a^(4/3) estimate already follows from the
intermediate recurrence in [1]. The result proved here is its attainability and
pointwise sharpness, not discovery of that recurrence or coefficient. It does
not improve the matrix-multiplication exponent.

### 2.1 The matching function is admissible

Symmetry and P_*(1,b)=b follow directly from (1).

For fixed a and b>=a, the profile is affine in b. Its discrete second difference
is zero, including the joining point b=a. For 2<=b<a, substitution of the
recurrence for h gives the exact identity

\[
2P_*(a,b)-P_*(a,b-1)-P_*(a,b+1)
=\frac{2h_b(a-b)}{3b(3b-2)}\ge0.
\tag{5}
\]

At b=a, the joining identity is

\[
\frac{3a-3}{2}h_a=\frac{3a-2}{2}h_{a-1}\quad(a\ge2).
\]

This proves discrete concavity everywhere it is required.

For b>=a, shifted tripling is an equality:

\[
P_*(a,3b+a-1)=3P_*(a,b).
\]

For b<a, the same inequality is equivalent to

\[
h_a\frac{a+2b-1}{2a+b-1}\ge h_b.
\tag{6}
\]

For fixed b, let F_b(a) denote the expression on the left of (6). At a=b it
is h_b. The numerator of the comparison F_b(a+1)/F_b(a)>=1 is

\[
(3a+1)(a+2b)(2a+b-1)
-3a(a+2b-1)(2a+b+1)
=2(a-b)(a-b+1)\ge0.
\tag{7}
\]

All denominators are positive. Thus F_b is nondecreasing for integer a>=b,
and (6) follows. This proves (S3).

### 2.2 Every admissible profile lies above it

Let P satisfy (S1)-(S3). For fixed a, set

\[
\Delta_{a,b}=P(a,b+1)-P(a,b).
\]

Concavity makes these increments nonincreasing. They cannot be negative: a
negative increment would bound all later increments above by a negative
constant, eventually making P negative. Thus the finite limit

\[
\ell_a=\lim_{b\to\infty}\Delta_{a,b}
=\lim_{b\to\infty}\frac{P(a,b)}b
\]

exists and is nonnegative, and every increment is at least ell_a.

Iterate b -> 3b+a-1. The resulting sequence is

\[
b_j=3^j\left(b+\frac{a-1}{2}\right)-\frac{a-1}{2}.
\]

Tripling gives P(a,b_j)>=3^j P(a,b). Divide by b_j and pass to the limit:

\[
\ell_a\ge\frac{P(a,b)}{b+(a-1)/2}.
\tag{8}
\]

Put D_a=P(a,a) and K_a=2D_a/(3a-1). Equation (8) gives ell_a>=K_a.
Symmetry and the increment lower bounds imply, for a>=2,

\[
D_a-D_{a-1}
=\Delta_{a,a-1}+\Delta_{a-1,a-1}
\ge K_a+K_{a-1}.
\]

Substitute the definition of K and rearrange:

\[
K_a\ge\frac{3a-2}{3a-3}K_{a-1}.
\]

Since K_1=1, induction yields K_a>=h_a. For b>=a,

\[
\begin{aligned}
P(a,b)&\ge D_a+(b-a)\ell_a\\
&\ge\left(\frac{3a-1}{2}+b-a\right)h_a\\
&=P_*(a,b).
\end{aligned}
\]

Symmetry handles b<a. Since Section 2.1 supplies an admissible function attaining
these values, this proves exact pointwise minimality, not merely a lower bound.

### 2.3 The rank upper bound still permits t=3/4

Induction gives

\[
h_a^3\le\frac{3a-1}{2}.
\tag{9}
\]

The induction step reduces to

\[
27a^3(3a+2)-(3a+1)^3(3a-1)=6a+1>0.
\]

For b>=a, both (3a-1)/2 and b+(a-1)/2 are at most a+b-1. Therefore

\[
P_*(a,b)^3
=h_a^3\left(b+\frac{a-1}{2}\right)^3
\le(a+b-1)^4.
\]

This proves (2), which is exactly (S4) with t=3/4.

### 2.4 Replication does not exclude this example

The elementary identity

\[
\left(1+\frac1{3a}\right)^3-\left(1+\frac1a\right)
=\frac{9a+1}{27a^3}>0
\]

shows that h_a/a^(1/3) is nondecreasing. Hence h_(qa)>=q^(1/3) h_a.
Also, for b>=a,

\[
qb+\frac{qa-1}{2}
\ge q\left(b+\frac{a-1}{2}\right).
\]

Multiplying proves (3). The replication construction in [2] gives
P(qa,qb)>=q^(1/t)P(a,b) for actual character profiles. The matching example
therefore survives this additional constraint at t=3/4.

### 2.5 What the theorem rules out

The pair (P_*, t=3/4) satisfies all the scalar assumptions just stated, including
the upper bound. Consequently no logically valid consequence of only those
assumptions can force t<3/4. In particular, no improved optimization of the
original discrete-growth argument can do so.

This is a barrier for a specified scalar relaxation. It does not construct a
tensor character with t=3/4 and does not prove omega>=9/4. Tensor identities,
other spectral constraints, or a different algorithmic argument can still exclude
this scalar model.

## 3. A dimensional obstruction to shorter uniform-sector packing

A natural attempted improvement replaces the source C(a,3b+a-1) with a smaller
C(a,B), while keeping three matched sectors each isomorphic to C(a,b), sharing
an a-dimensional input leg. The two other legs may be exchanged within each
sector.

The source has total dimension B+(a+B-1)=2B+a-1 on its two nonshared legs.
The target requires

\[
3\bigl(b+(a+b-1)\bigr)=6b+3a-3
\]

independent coordinates on those legs. These are actual flattening ranks of the
concise source and matched target, so a degeneration cannot increase them. Thus

\[
2B+a-1\ge6b+3a-3,
\qquad B\ge3b+a-1.
\tag{10}
\]

The original source length meets this necessary bound exactly.

More generally, k identical sectors with source length B=kb+c(a-1), for a>1,
require c>=(k-1)/2. This argument is restricted to a single convolution source,
identical target convolutions, and the specified shared input leg. It does not
exclude unequal blocks, tensor-product sources, or auxiliary factors returned
by a degeneration.

## 4. Additional tensor-product inequalities

The following construction produces inequalities not explicitly listed in
(S1)-(S4). I have not proved that they are logically independent of that scalar
system.

Identify C(a,b) tensor C(c,d) with multiplication of bihomogeneous forms in
(u,v) and (s,w): the two input bidegrees are (a-1,c-1) and (b-1,d-1).
Filter each space by powers of D=uw-vs.

For p,q>=0, diagonal substitution (s,w)=(u,v) identifies the quotient by D with
binary forms of degree p+q. Its kernel is D times the bidegree (p-1,q-1) space
when p,q>=1: multiplication by D is injective, its image is in the kernel, and
the dimensions agree. Iterating gives associated-graded input blocks with
lengths

\[
A_i=a+c-1-2i,\quad 0\le i<\min(a,c),
\]

\[
B_j=b+d-1-2j,\quad 0\le j<\min(b,d).
\]

Multiplication preserves this filtration and sends orders i,j to orders at
least i+j. Give the two input blocks weights -i and -j and an output block of
order k weight k. Every total weight is nonnegative; the surviving blocks have
k=i+j. On the associated graded, multiplication is ordinary multiplication of
binary forms. Its (i,j,k) block is C(A_i,B_j).

Fixing k leaves matched sectors sharing the output leg. The shared-leg entropy
argument, multiplied over the six leg permutations and optimized over the same
probability vector, yields

\[
P(a,b)P(c,d)\ge
\sum_{\substack{0\le i<\min(a,c)\\0\le k-i<\min(b,d)}}
P(a+c-1-2i,\ b+d-1-2(k-i)).
\tag{11}
\]

Fixing i instead gives matched sectors sharing the first input:

\[
P(a,b)P(c,d)\ge
\sum_{j=0}^{\min(b,d)-1}P(A_i,B_j).
\tag{12}
\]

There is a symmetric inequality fixing j. The factorization of the left-hand
side is exact because the symmetrized profile is multiplicative on tensor
products. The blockwise first-leg basis changes are not required to be the
same: character invariance is applied to the individual blocks after the
shared-leg inequality.

These inequalities are derived here as an additional search family. The
filtration is a standard determinant-filtration construction, and no novelty
claim is made for it.

## 5. Completed computations

All completed experiments are reproducible with the accompanying Python files.
The reports contain actual counts and exact values, rather than asserted search
coverage. Runs that did not finish are not included in these counts.

### 5.1 Scalar-profile verification

`verify_profile.py` performs 73,856 exact-rational checks. They include symmetry,
boundary values, concavity, shifted tripling, the cubed rank upper bound, and
diagonal equality on a grid through 128. Replication is checked for a,b<=32 and
q<=8. It separately checks the symbolic identities (5), (7), and the induction
identity for (9).

Result: all checks passed. The proof in Section 2, not the finite grid, establishes
the theorem for all positive integers.

### 5.2 Tensor-product filtration

`check_product_filtration.py --max-size 12` checks (11), (12), and the symmetric
fixed-j inequalities against P_*.

There are 20,736 source quadruples 1<=a,b,c,d<=12 and 353,664 exact inequalities.
None excludes P_* on this grid. This is not a proof that these inequalities
preserve P_* for all sizes.

### 5.3 Monomial degenerations

`search_degenerations.py` assigns integer weights u_i,v_j to the two inputs of
C(a,b), and assigns the output weights

\[
w_k=-\min_{i+j=k}(u_i+v_j).
\]

Every tensor term has nonnegative weight. The zero-weight terms define a genuine
monomial degeneration. Connected components of the bipartite graph on the second
and third legs give matched sectors sharing the first leg.

The code checks whether each sector is exactly a convolution tensor up to
coordinate reindexing and axis reversal. Unrecognized sectors use a valid
single-slice dot-product lower bound, not an invented convolution value.
Every candidate is scored with exact rational arithmetic. Float ratios in the
reports are descriptive only.

Completed searches:

| Search | Scope | Cases |
|---|---|---:|
| Binary | Weights in {0,1}, min=0 in each input; 2<=a<=b, a+b<=11 | 12,976 |
| Ternary | Weights in {0,1,2}, min=0 in each input; 2<=a<=b, a+b<=10 | 209,692 |
| Random | 20,000 independently generated pairs of arrays; lengths 2 through 15; entries -8 through 8; seed 20261020 | 20,000 |
| Total | Specified candidate cases, not all possible degenerations | 242,668 |

Result: no scored candidate exceeds the matching source profile. The search
rediscovers exact equality examples, including the original three-sector pattern
for C(2,4).

Limitations: this does not exhaust arbitrary integer weights, coordinate
restrictions, arbitrary basis changes, cancellations, tensor powers, or stronger
estimates for the unrecognized sectors. A hypothetical finite violation of P_*
would be an additional constraint worth studying, not automatically a smaller
matrix-multiplication exponent: other profiles with the same growth exponent
could remain feasible.

## 6. An explicit sufficient target for a smaller exponent

A precise possible target, not an established result of this pass, is a fixed
eta>0 such that the actual spectral profiles satisfy

\[
P(a,4a-1)\ge(3+\eta)P(a,a)
\tag{13}
\]

for all sufficiently large a. The same eta must work for every relevant
character; the threshold in a may depend on the character.

Put q=2+eta. Concavity then gives

\[
\Delta_{a,a}\ge\frac{qD_a}{3a-1}.
\]

For sufficiently large a, apply the corresponding bound at a-1, use symmetry,
and obtain

\[
\frac{D_a}{D_{a-1}}\ge
\frac{1+q/(3a-4)}{1-q/(3a-1)}.
\tag{14}
\]

The denominator is positive once a is large enough. The logarithm of the right
side is 2q/(3a)+O(a^-2). Summing establishes

\[
D_a\ge c a^{2q/3}
\]

for a positive constant c depending on the profile. Together with the rank
upper bound, this forces

\[
t\le\frac{3}{2q},\qquad
\omega\le\frac9{4+2\eta}.
\tag{15}
\]

For example, eta=1/1000 would give

\[
\omega\le\frac{1500}{667}=2.24887556221889\ldots.
\]

That number is a conditional target, not a new bound. A gain at one isolated
size is insufficient. The matching profile has ratio exactly three in (13), so
proving a uniform gain must use an additional tensor property.

## 7. Reproduction

Run from this directory with Python and SymPy installed:

```sh
python verify_profile.py
python check_product_filtration.py --max-size 12
python search_degenerations.py --mode binary --max-sum 11 --output binary_search.json
python search_degenerations.py --mode ternary --max-sum 10 --output ternary_search.json
python search_degenerations.py --mode random --samples 20000 --seed 20261020 --output random_search.json
```

No network, API credentials, or private data are needed. `requirements.txt` pins
the SymPy version used for this run. The search and product-filtration scripts
use the Python standard library only.

## References

[1] OpenAI. *An Upper Bound of 9/4 for the Matrix Multiplication Exponent*.
October 2, 2026. Sections 3-5. Original publication location:

`https://raw.githubusercontent.com/openai/math/main/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/paper.pdf`

PDF mirror inspected, including page images for the determinant filtration,
three-sector construction, and discrete-growth lemma:

`https://www.emergentmind.com/openai-math-explorer/papers/216.pdf`

[2] Przemyslaw Uznanski. *Rectangular matrix multiplication from polynomial
products*. arXiv:2610.10494v2, October 11, 2026. In particular the replication
construction and rescaled profiles.

`https://arxiv.org/html/2610.10494v2`

[3] *Big O Speedrun: Matrix Multiplication*. Leaderboard checked October 20, 2026.
This source establishes the listed status, not an independent verification of
this note or of the original formalization.

`https://bigospeedrun.com/matrix-multiplication`
