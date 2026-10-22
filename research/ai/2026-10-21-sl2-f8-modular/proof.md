# A modular all-power bound for SL(2,F8)

October 21, 2026. `AI-SL2-F8-MODULAR-001` is a written, AI-derived proof
with exact finite certificates, without independent mathematical review or
formalization. No smaller matrix multiplication exponent is established.

## Statement

Let G=SL(2,F8), in the maintained field model F2[t]/(t^3+t+1). Put

    P(t)=61+60t+63t^2+72t^3+63t^4+60t^5+61t^6,
    B(t)=64+P(t)/t^2,           0<t<1.                    (1)

For every n>=1, a coordinate/potential degeneration from the group tensor
of G^n to a finite rectangular direct sum must satisfy

    direct_sum_i M(a_i,b_i,c_i),
    sum_i (a_i*b_i*c_i)^(2/3) <= B(t)^n.                 (2)

The construction class is the maintained injective group-coordinate maps
with coefficient-one intended terms and strict integer vertex potentials.
The argument also applies whenever a larger coefficient-one diagonal
coordinate construction transfers to characteristic two in the same way.
It does not apply to an arbitrary complex degeneration with input mixing
or characteristic-dependent cancellation.

At t=3/4 the exact source bound is

    B(3/4)=1035637/2304 < 450.                           (3)

Consequently no such construction, even across source powers, can realize
the tensor power of the joint target consisting of six cyclically balanced
M(8,9,9) packets and M7. The conditional target is the one investigated in
[PR84, pinned at aefbf5e](https://github.com/1337isnot1337/matrix-mult-bounds/blob/aefbf5ef336f42c3d4767719d383ba8d85ffe21d/research/ai/2026-10-21-sl2-f8-ideals/assembly_note.md).
Every orientation of a packet has volume 648. Since

    74^3=405224 < 648^2=419904,
    6*648^(2/3)+49 > 6*74+49=493 > 450,

its score contradicts(2). This extends the one-copy dense-coordinate
assembly obstruction to an all-power modular inequality. It supplies no
obstruction to general complex singular maps. The packet construction and
its conditional exponent comparison retain PR84's credit.

The new bound does not exclude any of the 16 single-matrix formats left by
the maintained complex rank-locus/full-Koszul comparison. In particular,
M(18,18,25) and the main exponent question remain open. This non-exclusion
is checked exactly, rather than inferred from a numerical fit.

## Explicit binary modular quotient

Use the exact 504-element matrix group from the maintained
[semisimple-source package](../2026-10-21-semisimple-koszul/proof.md).
The following representations define an F2-algebra homomorphism:

    F2[G] -> F2 + Mat2(F8) + Mat4(F8) + Mat8(F2).        (4)

The scalar representation is augmentation. The two-dimensional F8 module
is the literal natural matrix action. The four-dimensional module is the
tensor product of that action with its Frobenius-square twist. For the
last module, act on the nine points of P1(F8), and use the eight-dimensional
even augmentation subspace of its binary permutation module. Its basis is
e_i+e_infinity for the eight finite points. These are explicit module
constructions, with no modular character table assumed.

The codomain has binary dimension 1+12+48+64=125. Exact binary rank of the
504 image columns is125, so(4) fills the entire product of matrix algebras.
Every representation product is checked for every ordered group pair:
508,032 F8-matrix products and254,016 binary-matrix products. Thus its
kernel J has dimension 379. The exported power bases have dimensions

    dim J^0,...,dim J^7 = 504,379,319,256,184,121,61,0.  (5)

The next section proves that the finite replay certifies the actual powers,
including both span inclusions. In particular J is nilpotent. Since the
quotient in(4) is semisimple, J is exactly the Jacobson radical. The
standard nilpotent-kernel/semisimple-quotient argument is not claimed as a
new algebra theorem.

## Exact power replay without all quadratic generator pairs

The supplied 15 vectors l_j lie in J, and their left ideal span A*l_j
has dimension 379. The replay verifies this span by closure under three
group generators, whose actual group products reach all 504 elements.
It follows that J=sum_j A*l_j. If a saved basis spans J^k, then

    J^(k+1)=J*J^k=sum_j A*(l_j*J^k).                    (6)

The verifier explicitly forms every l_j times every basis vector of J^k
and closes their span under the same generating group actions. It checks
that the resulting rank equals the next saved basis rank and that every
next saved basis vector is in that span. Independent rank of each saved
basis proves equality. This inductively establishes(5). The replay uses
19,800 such products, as against 500,280 products using every vector in
the original J basis. The span argument, not a sample, justifies the
smaller product list.

Group-vector multiplication uses binary permutation networks. Every one
of their254,016 group-action columns is compared with the literal group
table. Each network acts F2-linearly, so these column checks establish
its action on every source vector, including every saved witness. No
untested numerical or randomized multiplication is used by acceptance.
The separate small routing controls are additional implementation checks.

## The 64-dimensional central summand

The central witness in `results/sl2-f8-modular-2026-10-21/central.json`
is reconstructed from the exact conjugacy-class sums and then raised to
its eighth power. Because J^7=0, this lifts its simple-factor idempotent.
The independent verifier instead reads the witness and checks directly:

- e^2=e and e*g=g*e for all 504 group elements;
- the span of A*e has dimension64;
- its image in(4) is exactly the identity in Mat8(F2) and zero elsewhere.

The restricted image map A*e -> Mat8(F2) is therefore an isomorphism.
Its intersection with J is zero. Hence A=A*e plus A*(1+e) as an algebra
direct sum, of dimensions 64 and 440. All positive powers of J lie in the
440-dimensional block. Subtracting their successive dimensions in(5)
gives that block's layer polynomial P in(1).

The 64-dimensional summand needs only degree zero. Its multiplication
tensor has the trivial slice upper bound 64. No separate classification
of this summand, or comparison of characteristic-zero irreducibles with
modular simples, is needed beyond the checked algebra map.

## Source powers and target entropy

The modular slice framework is external work:
[Petrov, arXiv:1606.03256v4](https://arxiv.org/html/1606.03256v4), and
[Sawin, EJC25(4), P4.23(2018)](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v25i4p23/pdf/).
The separately weighted direct-sum argument also occurs in the local
[S5 block continuation, PR93](https://github.com/1337isnot1337/matrix-mult-bounds/pull/93).
Here is the explicit source count needed for this application.

Choose a basis of the 440-dimensional block adapted to its J-power flag,
with degree d on J^d/J^(d+1). A nonzero coefficient of the cyclic form
tau(xyz) has d_x+d_y+d_z<=6, since a product of higher total degree is
zero. Give the vector positive weight t^(d-2). In the 64-dimensional block
give every vector weight1. At every nonzero coefficient the product of
the three weights is at least 1. The total weight is B(t).

In an mth tensor power, weights multiply and their total is B(t)^m.
At least one leg of a nonzero coefficient has weight at least 1. There are
at most B(t)^m such basis indices on each leg, since each contributes at
least 1 to that weight sum. Partition the support among such indices to get

    slice_rank(T_G^m) <= 3*B(t)^m.                      (7)

The cyclic form is equivalent to group multiplication by the nondegenerate
pairing tau(xy). The two central summands are orthogonal for that pairing.
Thus the weighted sum has retained the entire source tensor. This proof
uses no assumed additivity or submultiplicativity of general slice rank.

The coordinate/potential maps transfer to the algebraic closure of F2:
the intended coefficients remain one and all extra terms have strictly
positive exponent. Slice rank cannot increase under these degenerations;
the proper-Grassmannian argument for its closed bounded loci is recorded
in the maintained [modular proof](../2026-10-20-heisenberg-seven/modular_proof.md).

Finally use that proof's credited field-independent tight-support target
theorem. For a rectangular direct sum, take its product with the two cyclic
rotations, and choose target-block probabilities proportional to
(a_i*b_i*c_i)^(2/3). All three marginal entropies are
3*log(sum_i(a_i*b_i*c_i)^(2/3)). The target asymptotic subrank lower bound
and(7), after kth roots and k tending to infinity, give(2). This is the
same explicitly credited entropy bridge; no new target theorem or
characteristic-zero invariant is being asserted.

## Reproduction and limits

From the repository root:

```sh
python research/ai/2026-10-21-sl2-f8-modular/verify.py
python -m unittest discover -s tests -p test_sl2_f8_modular.py -v
```

Exact witness regeneration, in order, uses `modules.py`,
`left_generators.py`, and `central.py` in this package. These require
only the maintained root environment. They use no external execution
service or floating-point acceptance step.

The finite module, power, and block certificates support the written
all-power implication. They do not establish an optimal filtration,
construct a missing matrix target, or prove an exponent improvement.
