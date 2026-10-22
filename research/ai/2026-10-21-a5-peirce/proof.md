# A characteristic-two slice-rank barrier for the central-cover targets

October 21, 2026. Written and unreviewed. The coefficient witness and its
integer inequalities replay exactly; this is not independent mathematical
review or formalization. The result limits an asymptotic obstruction method.
The selected matrix targets remain unconstructed and omega remains 9/4.

For a field F and a finite group G, let T_G be the trilinear group tensor

    T_G = sum(g*h*k = 1) x_g y_h z_k.

This is group-algebra multiplication after the invertible identification
of its output with the identity-coefficient pairing. Define

    s_F(G) = liminf(n -> infinity) slice_rank_F(T_G^tensor(n))^(1/n).

We do not assume that slice rank is submultiplicative or that this liminf
is a limit.

## 1. Result and exact scope

For every field F of characteristic two, the certificate and argument below
give

    s_F(A5 x C2) > 517/5 = 103.4,
    s_F(SL(2,F5)) > 517/5,
    s_F(SL(2,F5) x C2) > 976613/5000 > 195.

Here F5 specifies the matrix entries defining the abstract finite group;
the group-algebra coefficient field F has characteristic two.
The explicit double-cover projection in the certificate identifies
PSL(2,F5) with A5, so the first source is the project's split cover.

Consequently, an eventual source-power estimate

    slice_rank_F(T_G^tensor(n)) <= exp(o(n)) * C^n

cannot have C below these lower bounds. The same restriction applies if
the estimate is asserted along an unbounded subsequence of n. In
particular, this form of characteristic-two asymptotic source-cost bound
cannot cross the M10 threshold 100 in either order 120 source. For the
order 240 source it cannot cross the cyclically symmetrized
M(13,13,15) threshold: (13*13*15)^(2/3) < 195.

This does not exclude finite-power slice tests, restrictions that use
additional information about a proposed map, another characteristic,
or the target constructions themselves. A source-capacity lower bound
does not construct a matrix-multiplication target.

The comparison threshold uses the credited cyclic symmetrization from
the prior modular packages. A coordinate/potential certificate from one
copy of T_G transfers
to characteristic two because its retained coefficients are one and its
maps use integer parameter powers. Tensoring a proposed M(a,b,c) map
with its two cyclic rotations gives the square target M(abc,abc,abc).
Its tight uniform support has asymptotic subrank (abc)^2. The strict
exponential-cost comparison seeks C<(abc)^(2/3).
For M10 the threshold is 100. This is the particular comparison limited
by the present lower barrier.

## 2. The exact A5 coefficient witness

Work first over F4=F2[w]/(w^2+w+1). Enumerate A5 as the even permutations
of five letters, in lexicographic order. An algebra vector is encoded by
two 60-bit planes: the low plane is its coefficient of1 and the high plane
its coefficient of w. All 60 basis vectors in `tight-certificate.json`
are supplied explicitly.

The independent verifier uses coordinate arrays and polynomial reduction
over F2, rather than the discovery program's bit-plane convolution.
It checks the basis has rank 60 over F4, reconstructs every group product
and all 216,000 coefficients

    lambda(e_a*e_b*e_c),  lambda = coefficient of the identity.

The certificate supplies integer diagonal weights in each of the three
legs. Every nonzero source coefficient has nonnegative total weight.
Thus scaling by the corresponding powers of a parameter has a genuine
limit. The verifier checks all coefficients, including every potential
negative-power term; a sampled support or a radical-dimension prediction
is not used for acceptance.

There are 326 nonzero source coefficients in this basis. Exactly 277
remain at exponent zero. They form

    U = L direct_sum M4,

where L has 44 coordinates per leg and 213 nonzero coefficients. The M4
block has 16 coordinates per leg and exactly its 64 matrix-triangle terms,
all with coefficient1. The verifier checks this full identity. It does
not infer a matrix block from its dimensions alone.

The discovery route split idempotents over F4, then replaced the two
degree-two loop vectors (v1,v2) by

    (v1+w*v2, v1+(w+1)*v2).

That route helped find the witness. Acceptance needs only the saved basis,
group arithmetic and full coefficient check; no unverified radical pilot,
numerical optimizer or idempotent classification is a premise.
The Laurent family is defined over F4; its limit and slice-rank closedness
are interpreted over an algebraic closure, as in section 6.

## 3. Tight support and the external entropy theorem

The certificate contains three integer weight arrays, one per leg of U.
Each is injective on all 60 labels, and their sum is zero on every one
of the 277 nonzero terms. These finite identities certify tight support.
The generator found the integer arrays in a rational kernel; the verifier
checks the arrays directly and does not trust that kernel calculation.

Let W have support {(1,0,0),(0,1,0),(0,0,1)}, with all coefficients one.
Tight weights for W are (0,1), (0,1), (-1,0). If u is a leg's U weight
and v its W weight, the product weight 2u+v is injective on all 120 labels.
The verifier checks this and all 831 product-support equations explicitly.

We import Strassen's tight-support entropy lower bound, stated in
[Christandl--Vrana--Zuiddam, arXiv:1609.07476v2, Theorem 1.1.31](https://arxiv.org/abs/1609.07476v2).
For the field-independent application, use the hypergraph formulation in
[Arunachalam--Vrana--Zuiddam, EJC27(3), P3.12 (2020), section 1.4.3, equation (11)](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v27i3p12/pdf/)
together with section 1.4.1, equation (6). It gives an asymptotic induced
matching lower bound from the minimum marginal entropy of any probability
distribution on a tight support. Coordinate deletion and rescaling of
the surviving nonzero coefficients give the same tensor-subrank lower
bound over every field. This imported theorem is not a local discovery.

## 4. A rational entropy certificate

On U put mass 2/3 uniformly on L's 213 terms and mass 1/3 uniformly on the
64 matrix terms. Multiply this distribution by the uniform distribution
on W's three terms. With common denominator

    D = 122688,

each of the 639 L-times-W terms has integer weight 128, and each of the 192
matrix-times-W terms has weight 213. They sum to D. The verifier constructs
all three 120-entry marginal count vectors, checks that they coincide and
compares them with the saved vectors.

Write their common counts as m_i. In natural logarithms the marginal
entropy is

    H = log D - (1/D)*sum_i m_i*log m_i.

The accepted numerical comparison is the integer inequality

    (5D)^D > 517^D * product_i m_i^(m_i).

It proves E=exp(H)>517/5 with no floating acceptance. The two compared
integers have 2,358,869 and2,358,813 bits. For context only, floating
evaluation gives E approximately 103.432913357; the proof uses the integer
comparison. The external theorem therefore gives asymptotic subrank at
least E for U tensor W.

For a further W factor, use the product distribution. Its marginal
entropy adds the binary entropy of1/3. Put kappa=(27/4)^(1/3). Exact integer
comparisons give

    kappa > 1889/1000,
    E*kappa > (517/5)*(1889/1000) = 976613/5000 > 195,
    2535^2 < 195^3.

This argument uses the tight tensor with two W factors and its product
distribution. It does not assume multiplicativity of slice rank.

## 5. Every central double cover has the required limit

Let 1 -> {1,z} -> G -> Q ->1 be a central double cover and work in
characteristic two. Choose representatives r_q with r_1=1 and set

    u_q = r_q,       v_q = r_q*(1+z).

This is a basis of the group algebra. Since z is central and
(1+z)^2=0, every trace coefficient with two or three v factors vanishes.
A coefficient with exactly one v is1 precisely when the three quotient
indices multiply to1, independently of the extension cocycle: the lifted
product is either1 or z, and either product times(1+z) has identity
coefficient one. Coefficients with no v may be zero or one.

Give u weight1 and v weight-2 on every leg. The nonzero no-v terms have
exponent3, and the one-v terms have exponent zero. There are no poles.
The limit is exactly T_Q tensor W. This also applies to the split cover.

The certificate's map from all 120 determinant-one matrices over F5 to the
60 permutations is checked on all 14,400 products. Its kernel is precisely
{I,-I}; both centrality and order two are checked. It therefore supplies
the claimed A5 quotient for SL(2,F5), without relying on a character table.
Tensoring this limit with the C2 limit supplies the additional W factor
for SL(2,F5) x C2.

## 6. Passing to slice-rank lower bounds

Extend the coefficient field to an algebraic closure K; extension can
only decrease slice rank. Bounded slice-rank loci over K are closed.
For completeness, for each r1+r2+r3<=r, take the product of Grassmannians
of subspaces E_i of dimensions r_i. The condition

    T belongs to E1 tensor V2 tensor V3
              + V1 tensor E2 tensor V3
              + V1 tensor V2 tensor E3

is closed in the tensor/Grassmannian incidence space. Projection is proper
because the Grassmannians are projective. The finite union over the
dimension triples is closed, proving the assertion. This is the same
closedness argument credited in the earlier modular packages.

Apply closedness to every tensor power of each explicit limit. The
central-cover limit followed by the A5 basis limit gives

    slice_rank_K(T_G^tensor(n)) >= slice_rank_K((U tensor W)^tensor(n))
                              >= subrank_K((U tensor W)^tensor(n)).

The entropy lower bound and n-th roots prove the two order 120 statements.
The limit to U tensor W tensor W proves the order 240 statement in the
same way. All tensor powers, not a sampled range, are covered by the
explicit limits and imported entropy theorem.

Finite-power tests remain logically distinct. Slice rank is not generally
submultiplicative, so this asymptotic lower bound is not promoted to a
claim about every finite-power threshold. Nor does it decide any of the
missing complex target maps.
