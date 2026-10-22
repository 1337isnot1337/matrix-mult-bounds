# Blockwise modular bounds for S5 central sources

October 21, 2026. Claim `AI-S5-BLOCK-FILTRATION-001` is a written,
AI-derived proof with exact finite certificates. It has no independent
mathematical review or formalization. No smaller exponent is established.

## Result

Put G_r=S5 x C2^r. The injective group-coordinate/potential construction
cannot realize either M(20,20,20) or M(19,20,21) from G_2. Both targets
pass the maintained general complex rank-locus and every full-space Koszul
test. The new exclusions concern the coordinate/potential construction
class; they do not exclude arbitrary complex degenerations.

More generally, put

    kappa = 3/2^(2/3),       kappa^3 = 27/4,
    P(t) = 17+9t+9t^2+18t^3+9t^4+9t^5+17t^6,
    C_r(t) = kappa^r * (P(t)/t^2 + 16*kappa),   0<t<1.      (1)

For every integer r>=0, every n>=1 and every finite rectangular direct
sum obtained by a coordinate/potential degeneration from G_r^n,

    direct_sum_i M(a_i,b_i,c_i),

the following necessary inequality holds:

    sum_i (a_i*b_i*c_i)^(2/3) <= C_r(t)^n.                 (2)

All maps and strict potential inequalities are in the maintained model.
In particular their coefficients are zero or one and their weights are
integers. The bound does not transfer an arbitrary characteristic-zero
cancellation identity to characteristic two.

At t=4/5, P(t)/t^2=785437/10000. The integer comparison

    (189/100)^3 > 27/4

certifies kappa<189/100. Hence

    C_1(4/5) < 205601193/1000000,
    C_2(4/5) < 38858625477/100000000 < 389.                (3)

A single matrix target therefore requires (abc)^2 < 389^3 in G_2.
For M20 this fails since its square marginal dimension is400. For the
other new target, the exact comparison is

    (19*20*21)^2 > (38858625477/100000000)^3.

The same bound constrains all source powers and joint rectangular targets
as in(2). It does not exclude M19, or the proposed M(13,14,14) in G_1.
No construction of either surviving target is provided.

## Exact central blocks

Reuse the previous [binary S5 radical certificate](../2026-10-21-s5-split/README.md),
with its explicit even-vertex and even-cycle representations. Its full
independent replay checks 28,800 representation products and 24,360
group-algebra products. The augmentation and the two representations
give a surjection onto F2 plus two Mat4(F2) blocks. Their kernel J is
nilpotent, and the certified power dimensions are

    dim J^0,...,dim J^7 = 120,87,62,53,35,26,17,0.

Consequently J is the radical. This is the prior finite result, not a new
module construction.

Enumerate S5 by lexicographic permutations, with the identity at index 0.
A binary integer records its support in this ordered group basis. The new
central idempotent is

    e = 0x191199262266918919666640189918.

Direct multiplication verifies e^2=e and e*g=g*e for every group element.
Thus A=F2[S5] splits as the algebra direct sum A(1+e) plus Ae. The exact
binary ranks of the projected prior power bases are

| Block | Dimensions of its projected J^k, k=0,...,7 |
| --- | --- |
| A(1+e) | 88,71,62,53,35,26,17,0 |
| Ae | 32,16,0,0,0,0,0,0 |

Because e is central, these projected flags are multiplicative:
(eJ^i)(eJ^j)=eJ^(i+j), and likewise for1+e. The new rank calculations
give layer counts P(t) in the first block and16+16t in the second. They
do not require an imported modular character table, a block classification,
or an identification of the 32-dimensional algebra with a matrix algebra
over the dual numbers.

The certificate generator finds a central element having identity image
on the first four-dimensional representation and zero image on the other
two simple factors. Three squarings give its eighth
power, an idempotent because J^7=0 and characteristic two gives
(x^2-x)^8=x^16-x^8=0. The verifier needs only the exported idempotent and
recomputes its centrality, product, and all projected ranks.

## Counting separately on each block

Here is the counting argument, including the direct-sum step. It uses the
standard modular slice method of
[Petrov, arXiv:1606.03256v4](https://arxiv.org/html/1606.03256v4)
and [Sawin, EJC25(4), P4.23(2018)](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v25i4p23/pdf/).
It makes no additivity or submultiplicativity assumption about slice rank.

For a block with a multiplicative flag I^0,...,I^(D+1)=0, choose a basis
adapted to that flag. Give a basis vector degree d when it represents a
layer I^d/I^(d+1). A nonzero coefficient of the cyclic group-algebra
trilinear form tau(xyz) can only have d_x+d_y+d_z<=D. Indeed, the product
lies in I^(d_x+d_y+d_z), so larger total degree gives zero before applying
the trace tau. This remains true for any field extension of F2.

Choose any t in(0,1) and attach positive weight t^(d-D/3) to that vector.
The product of the three weights at a nonzero coefficient is at least1.
The sum of the basis weights is

    B(t) = (sum_d layer_d*t^d)/t^(D/3).

In a tensor product, multiply these weights over the factors. Every
nonzero coefficient still has triple weight product at least1. At least
one of its three leg weights is at least1. Slice on such a leg. There
are at most the sum of all weights many basis vectors of weight at
least1. Thus the slice rank is bounded by three times the weight sum.

For an algebra direct sum, use the separately weighted bases together.
Every nonzero coefficient belongs to one block; its weight condition is
unchanged. The weight sums add. In a tensor product they multiply.
Consequently the nth tensor power has slice rank at most

    3*(sum_blocks B_block)^n,

including different choices of t and different D for different blocks.
This is precisely the information lost by applying one radical polynomial
with a common top degree to the whole S5 algebra.

The 88-dimensional block has D=6 and gives P(t)/t^2. The 32-dimensional
block has D=1, and t=1/2 gives 16*kappa. A central F2[C2] factor has
layer polynomial1+t and D=1; its same parameter gives kappa. This proves
the explicit source bound

    slice_rank(T_(G_r)^m) <= 3*C_r(t)^m,   m>=1.          (4)

The cyclic form tau(xyz) is equivalent to the group multiplication
tensor, using the nondegenerate pairing tau(xy). The central splitting
is orthogonal for that pairing, so no contribution between different
blocks has been discarded.

## Field transfer and the target lower bound

The coordinate/potential maps have the same coefficient-one leading
terms over the algebraic closure of F2. The earlier
[modular Heisenberg proof](../2026-10-20-heisenberg-seven/modular_proof.md#why-this-modular-bound-applies-and-cyclic-symmetrization)
records the exact field-transfer, cyclic symmetrization, proper
Grassmannian proof of closed bounded-slice-rank loci, and tight-support
entropy argument used here. These arguments do not use a Heisenberg
hypothesis: only the explicit source-power bound changes from that proof.

For one rectangular target of volume V, multiply its degeneration with
the two cyclic rotations. The target becomes M(V,V,V). The matrix
support is tight and has uniform marginals, so its asymptotic subrank
is at least V^2 over every field. This is the credited external
combinatorial theorem, not a claim that every complex identity survives
modular reduction. Combining this lower bound with(4) gives
V^(2/3)<=C_r(t)^n.

For a direct sum, use block probabilities proportional to V_i^(2/3)
in the same three-copy tight-support argument. Its marginal entropy
is3*log(sum_i V_i^(2/3)). Formula(4), with m=3nk and k tending to
infinity, then gives(2). All quantifiers in the stated conclusion follow.

## Finite frontier and reproduction

The comparison imports the existing exact complex rank-locus proof and
full-space Koszul formula with their original attribution. The sorted
integer formats have minimum side at least2 and maximum leg dimension
at most the source dimension; every strict 9/4 degree gate is decided
by the maintained rational root intervals.

| Source | All formats | Strict degree gate | After rank locus | After full Koszul | Extra coordinate exclusions |
| --- | ---: | ---: | ---: | ---: | ---: |
| G_1, dimension 240 | 1766 | 32 | 7 | 6 | 0 |
| G_2, dimension 480 | 5396 | 132 | 73 | 45 | 2 |

The two additional exclusions are exactly(20,20,20) and(19,20,21),
up to permutation. This table does not retire any of the 43 other
general-test survivors in G_2. The bound in(2), rather than a finite
enumeration, covers source powers and rectangular direct sums.

From the repository root:

```sh
python research/ai/2026-10-21-s5-block-filtration/blocks.py --verify results/s5-block-filtration-2026-10-21/certificate.json
python research/ai/2026-10-21-s5-block-filtration/frontier.py --output results/local/s5-block-frontier.json
python -m unittest discover -s tests -p test_s5_block_filtration.py -v
```

All acceptance computations use the maintained dependencies and exact
integers/rationals. The separately named discovery scripts use optional
NumPy/SciPy numerical optimization. Their Peirce, alternate-source and
support pilots supplied no target construction and are not needed for
this proof or its accepted bound. No optimality of the filtration is
claimed. All general arguments remain written and unreviewed.
