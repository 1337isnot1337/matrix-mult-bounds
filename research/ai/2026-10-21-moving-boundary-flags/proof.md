# Maximal first extensions force a moving polynomial boundary

Written local proof, unreviewed, October 21, 2026. The only finite linear
lemma below has exact rational certificates. No smaller exponent follows.

## Statement and scope

Use the source, normalized leading rows G, spaces E_B,E_C, and leading
row space W0 from the [first-extension package](../2026-10-21-quantum-extension-spaces/proof.md).
Let P(t),Q(t) be regular maps to the two 110-dimensional target legs,
with the four nonzero leading rows normalized to G in the first four
output coordinates. The first-leg map may be arbitrary Laurent.

The first-extension package proves that a limit M(10,10,11) requires
each new output row of P1,Q1 to belong to E_B,E_C respectively. Their
quotients by G have dimension 16. Assume that the new rows on **each**
side span that full 16-dimensional quotient. Then the target is impossible,
with no restriction on any higher coefficient and no grading assumption.

Thus a possible construction with these leading maps must have quotient
rank at most 15 on at least one side at first order. This does not exclude
rank-deficient first extensions, different leading flags, leading-rank
losses under final projections, or arbitrary tensor degenerations. In
particular an arc whose first new rows appear only at a later order does
not satisfy the stated maximal first-order hypothesis.

## 1. The low-rank intersection constraint

Let L0 be the saturated limiting first-row space of S(t)=(1,P(t),Q(t))T.
It has dimension at most 112 and contains W0 of dimension 12. A target
first-slice space R has dimension 100 and minimum nonzero matrix rank 11.
Let C0 be the matrix space supported on the union of the first four rows
and first four columns. Every matrix in C0 has rank at most eight. Hence

    L0 intersect C0 = W0.                              (1)

Indeed the intersection contains W0; if its dimension exceeded 12 it
would meet R nontrivially by the dimension formula in L0. This would
give a nonzero target matrix of rank at most eight.

Constant changes among the 106 new output coordinates, followed by
regular row operations adding multiples of t times leading rows, put
the first new rows in the following form: sixteen rows give chosen bases
of E_B/G and E_C/G, and all remaining first new rows are zero. The
regular row operations remove their G components. These transformations
preserve the leading maps, the regular-limit problem and the maximality
hypothesis. The verifier records the exact chosen complements.

## 2. The finite normal-direction lemma

Put

    F_B = span{e_(p,j,z): p in {0,3}},
    F_C = span{e_(r,q,z): q in {0,3}},
    K = span{e_(i,s,z): z in {1,2,4,5}}.

The omitted indices run over their full source ranges. These spaces have
dimensions 56,56,64. The preceding package proves

    (K,F_B,F_C)T=0,
    annihilator of (K,-,G)T = F_B,
    annihilator of (K,G,-)T = F_C.                      (2)

Consider eight proposed leading-row variations D_B,D_C, modulo F_B,F_C.
There are 448 normal coordinates. Suppose that, for each x in K,

    D(x) = T(x,D_B,G)+T(x,G,D_C) = y_x S0               (3)

for a unique y_x supported on the twelve first indices A0. Suppose also
that for every basis row b of E_B/G there is a row b' such that

    T(x,b',G) + T(x,b,D_C) - T(y_x,b,G) = 0             (4)

for all x in K. Require the symmetric condition for each basis row of
E_C/G, with a correction c' and D_B on the other side.

Then, modulo F_B,F_C, all such variations are precisely the four linear
combinations of the following directions, indexed by j in {0,3} and
k in {1,2}:

    (D_B)_z = -e_(k,j,z),
    (D_C)_z =  e_(j,k,z),        z in {1,2,4,5}.        (5)

Here (4) is an equality of four output coordinates, so its correction
row is required to work for all x and all four coordinates simultaneously.

The complete certificate is small rational linear algebra. The four
annihilator equations for W0 turn (3) into a 256-by-448 system of rank
220. Its kernel has dimension 228. For (4), the map b' -> T(K,b',G)
has rank 56 in 256 coordinates; a basis of its 200-dimensional cokernel
eliminates b'. Sixteen rows on either side give 6400 equations on the
228 remaining parameters. Removing duplicate and zero equations leaves
564 rows of rank 224. Thus at most four dimensions remain. The four
independent explicit directions (5) satisfy every equation, proving
equality. All ranks have rational reductions and nonzero modular minors;
the explicit directions supply an independently checked kernel bound.

Boundary components of D_B,D_C make every expression in (3)-(4) zero
by (2), including y_x=0. Therefore taking normal coordinates loses no
condition on the remaining components. The code contracts all source
terms; the finite-field calculation is only a lower-rank certificate.

## 3. Moving boundary spaces

Identify each short four-dimensional space with homogeneous cubic forms
in two variables. Let U(t) be a rank-two formal plane reducing to the
span of the two endpoint monomials e0,e3. Define

    F_B(t) = U(t) tensor C^4 tensor C^7,
    F_C(t) = C^4 tensor U(t) tensor C^7.

The three products of a basis of U(t) are independent at t=0, and hence
over C[[t]]. Let K(t) be their annihilator in the reversed long-coordinate
pairing, tensored with the sixteen short first-leg coordinates. It is
a regular rank-64 direct summand reducing to K. The source formula gives

    (K(t),F_B(t),F_C(t))T = 0                          (6)

identically. This uses the products of cubic forms, not an assertion
that an arbitrary change of their basis is a source automorphism.

The directions (5) are exactly the four tangent directions of U. Write
the leading rows as

    G_z = (e0 tensor e3 - e3 tensor e0) tensor e_z.

Moving e0 and e3 independently toward e1,e2 gives (5), with the transposed
opposite variation on the other leg. A regular graph chart for U fixes
the endpoint coordinates and leaves these four formal parameters free.

## 4. Formal induction

We construct U(t) so that every row of P,Q lies in F_B(t),F_C(t). Initially
this holds modulo t, since their leading rows are G. Suppose it holds
modulo t^N, for N>=1. Extend the currently chosen U(t) arbitrarily and
project P,Q onto the corresponding boundary spaces. Write

    P = Pbar + t^N D_B + O(t^(N+1)),
    Q = Qbar + t^N D_C + O(t^(N+1)),

where Pbar,Qbar lie in the boundary spaces identically and D_B,D_C are
their normal errors at this order. For a regular basis x(t) of K(t),
(6) shows that x(t)S(t) is divisible by t^N. Its coefficient at order N
is supported on C0, so (1) forces it to belong to W0.

The off-diagonal output blocks have no contribution from a leading-row
error on the opposite side. Thus (2) forces every new-row normal error
to vanish. Only the four leading rows on each side can depart at this
order. Their remaining error satisfies (3); choose the corresponding
constant y_x on A0. The row

    [x(t)S(t) - t^N y_x S(t)] / t^(N+1)                (7)

is regular and belongs to the generic first-row space. Its constant term
therefore lies in L0. It is still supported on C0: a product of two
normal errors can contribute at this order only when N=1, and then both
errors are confined to the leading output rows. All boundary-boundary
terms vanish by (6). Equation (1) therefore forces the residue of (7)
into W0, so both off-diagonal blocks vanish.

In the block with a new B row and leading C coordinates, this vanishing
is exactly (4). The new row's coefficient at the next order supplies b'.
The first new rows of Pbar are the fixed complement rows from Section 1:
changing U at order N cannot change them at order one, since those output
rows have zero constant term. The terms from the derivative of x(t)
affect only the top-by-top block at this order. The opposite block gives
the symmetric condition. Thus the finite lemma applies.

By (5), adjust the four graph coefficients of U at order N to absorb
the remaining leading-row normal error. New rows have zero constant
term, so this adjustment does not alter their membership modulo t^(N+1).
All rows now lie in the adjusted boundary spaces modulo t^(N+1), completing
the induction. Working formally requires no convergence assumption.

The resulting formal P,Q have row rank at most 56 over C((t)). Applying
any first-leg Laurent map cannot increase either of these flattening
ranks. At a regular limit the corresponding 57-by-57 minors still vanish.
The proposed target is concise in 110 coordinates on each of these legs,
a contradiction. This proves the stated exclusion at every order.

The argument depends on the maximal first extensions only through the
finite lemma's full complement constraints. Removing that hypothesis
requires a new analysis; a numerical low residual or a smaller collection
of rows is not silently covered by this proof.
