# Leading-defect flags for the singular A4 problem

October23,2026. Written, unreviewed owner-directed OpenAI Codex work.
No independent review, formalization, complete degeneration or exponent gain.

## 1. Balance both long maps

Suppose the complete formal identity for A4 and M(10,10,11) is

    B M(F(X)) C = X tensor I_11+O(t),   X in Mat_10(C).       (1)

Every map is Laurent with finite principal part. Let b,c be the minimum
entry valuations of B,C. Replace the three maps by

    B_hat=t^(-b)B,  C_hat=t^(-c)C,  F_hat=t^(b+c)F.

Equation (1) is unchanged. The balanced long maps are regular with
nonzero leading coefficients. Put

    r_B=rank B_hat(0),   r_C=rank C_hat(0),
    q_B=112-r_B,         q_C=112-r_C,       d=q_B+q_C.

The [one-regular-long-leg theorem](../2026-10-23-one-regular-leg/proof.md)
requires r_B,r_C<=109 in any remaining candidate. In particular q_B,q_C
are positive. If F_hat were regular, the target unit at zero would give
rank(B_hat(0) M(F_hat(I_10)(0)) C_hat(0))=110, impossible with those
leading ranks. Thus F_hat has a pole of some order h>0. Write

    L=F_hat_(-h):Mat_10(C) -> A4,       L!=0.

Its first negative coefficient equation is

    B_hat(0) M(L(X)) C_hat(0)=0 for every X.                 (2)

All statements below are necessary leading conditions. They do not
solve the subsequent Laurent coefficient equations.

## 2. Total defect and the coherent-factor bound

For any matrix Z, multiplication by B_hat(0),C_hat(0) loses at most
q_B+q_C in rank. Hence (2) implies

    rank M(L(X))<=d for every X.                            (3)

The source minimum16 forces d>=16, or equivalently

    r_B+r_C<=208.                                          (4)

If d<32, the entire nonzero linear space im L has source slice ranks
below32. The prior [polynomial-rank-locus theorem](../2026-10-20-anisotropic-constructions/polynomial_rank_locus.md),
specialized to a=b=4, gives one fixed rank-one Hankel factor h such that

    im L is contained in {F_(i,k,s)=g_(i,s) h_k}.

This is a16-dimensional vector space, so rank L<=16 for16<=d<=31.
The cited source theorem supplies this coherent-factor conclusion for
arbitrary linear spaces, not just coordinate slices or target rulings.
Its proof is elementary polynomial multiplication and is byte-pinned.

## 3. The equality case d=16 has only one leading source direction

Every nonzero member of im L now has rank exactly16. The prior complete
[minimum-rank classification](../2026-10-20-koszul/cyclic_finite_target.md),
Section4, gives F=u tensor h tensor v, with h on the degree-six rational
normal curve and u,v in C^4. The coherent-factor theorem above fixes h.

A linear subspace of decomposable tensors u tensor v either has one
fixed u or one fixed v. Indeed, the sum of u_1 tensor v_1 and u_2 tensor
v_2 is decomposable only if one pair of factors is proportional. If two
u factors are independent, their v factors coincide up to scalar, and
comparison with both tensors forces every other v factor to coincide.
Otherwise all u factors were already proportional.

Suppose im L had dimension at least two. It would therefore contain a
pencil with two independent u factors and fixed v, or the exchanged
case with two independent v factors and fixed u. We exclude both.

For each nonzero f in im L, write Z=M(f), W=im C_hat(0), and
K_B=ker B_hat(0). Equation (2) says Z(W) is contained in K_B. Since
rank Z=16=q_B+q_C, the projection bounds are equalities:

    rank Z|_W=q_B,       Z(W)=K_B,       ker Z is contained in W.

Consequently every column space of Z contains the same nonzero K_B,
and every row space contains the same nonzero annihilator W^perp.
Here perp denotes the algebraic dual annihilator; no Hermitian structure
is being assumed. Their dimensions are q_B,q_C respectively.

Apply a constant source GL2 change on the middle convolution factor
to move h to the endpoint h=(1,0,...,0). This preserves the source,
all matrix ranks and the fixed-subspace conclusions. The literal source
formula then gives, up to fixed coordinate orderings,

    row M(u tensor h tensor v)=(u S_3) tensor C^4,
    col M(u tensor h tensor v)=C^4 tensor (v S_3),             (5)

in their fixed28-dimensional coordinate supports. S_3 is the space of
one-variable polynomials of degree at most3. The factors u,v are viewed
as polynomials of degree at most3, or homogeneous cubics.

For independent u_0,u_1,

    intersection_(z in C) (u_0+z u_1) S_3 = {0}.            (6)

To prove this, divide u_0,u_1 by their polynomial gcd g. The remaining
coprime independent pair yields infinitely many pairwise coprime
nonconstant factors u_0/g+z u_1/g (at most one is constant). A fixed
nonzero polynomial cannot be divisible by all of them. Any vector in
the intersection would have exactly that divisibility, a contradiction.
All degrees are bounded by6; the homogeneous endpoint version is the
same argument. Tensoring with C^4 preserves this zero intersection.

Thus a varying-u pencil has zero common row space, contradicting the
nonzero W^perp. A varying-v pencil has zero common column space,
contradicting the nonzero K_B. Hence

    d=16 implies rank L=1.                                 (7)

The sole source direction is a minimum-rank slice u tensor h tensor v.
The scalar functional X -> L(X)/f remains unrestricted by this argument.
It is not assumed to be injective or supported at a matrix unit.

## 4. Equality requires a first-map pole of order at least ten

Still assume d=16. Apply the preceding rank-one kernel-space result
successively to the negative coefficients of F_hat. Initially L has
rank one. On its kernel, the next negative equation has all earlier
first-map coefficients zero, so its image is again a linear subspace
of the kernel in (2), and has dimension at most one. Continue down to
coefficient -1. If the pole order is h, the common kernel E_0 of all
negative first-map coefficients therefore has codimension p<=h in
Mat_10. This does not assume their images or scalar functionals coincide.

On E_0 the map F_hat is regular, so the constant equation is ordinary:

    B_hat(0) M(F_hat_0(X)) C_hat(0)=X tensor I_11, X in E_0. (8)

Thus F_hat_0 is injective on E_0. Suppose h<=9, so p<=9. Describe E_0
as the common kernel of p bilinear forms ell_j(a,b) on rank-one matrix
parameters X=a b^T. Let Z be the reduced projective incidence

    Z={([a],[b]) in P^9 x P^9: ell_j(a,b)=0 for all j}.

Every nonzero rank-one X in E_0 has source lift of rank at most
11+d=27<32 by (8). Projectivized F_hat_0 is a linear embedding on E_0,
so the credited source locus gives a regular coherent-factor map
eta:Z -> P^1. This uses the projection of the closed Segre product
P^15 times the degree-six rational normal curve, which is an isomorphism
onto its image. No source lift vanishes on Z, by injectivity.

For each nonzero a, put V_a={b:ell_j(a,b)=0 for all j}. Its dimension
is at least10-p>=1. The entire fiber P(V_a) of Z -> P^9 maps to a
linear space of source slices below32, so eta is constant on that
fiber. These fibers are nonempty projective linear spaces at every a,
including rank-drop points of the bilinear constraints.

We justify descent across those points, rather than using only generic
fibers. On an open set of maximal constraint rank, choose a rational
nonzero kernel vector b(a). It defines the rational value eta(a).
Take the reduced closure Gamma of its graph in P^9 x P^1. Every point
of Gamma lies in the closed image of (projection,eta):Z -> P^9 x P^1,
so all fibers of Gamma -> P^9 contain at most one point. Properness
makes the projection surjective, hence every fiber has one point.
It is finite by the proper-finite-fibers theorem, and birational because
it is a graph on a dense open. Since P^9 is normal, it is an isomorphism.
These two external facts are [Stacks, Tag02LS](https://stacks.math.columbia.edu/tag/02LS)
and [Tag0AB1](https://stacks.math.columbia.edu/tag/0AB1), respectively.
Thus eta descends to a regular map P^9 -> P^1 on the whole base.

Every regular map P^9 -> P^1 is constant. For completeness, the pullback
of O(1) is O(e), and its two generating sections are homogeneous
polynomials of degree e with no common projective zero. If e>0, two
hypersurfaces in P^9 have a common zero (equivalently their homogeneous
ideal has height at most two). Hence e=0 and the map is constant.
Here the usual Picard description of projective space follows by
representing Cartier divisors as sums of homogeneous prime divisors;
the polynomial ring is factorial, so their classes are their degrees.
This also explains why the argument needs the entire normal base,
not merely a rational map defined away from a rank-drop locus.

It follows that all rank-one images in E_0 share one fixed h. Let T be
the span of the rank-one matrices in E_0. Injectivity in (8) gives

    dim T<=16.                                              (9)

We now show dim T>=19 for p<=9. Both projections of Z onto P^9 are
surjective, since each system of at most9 linear equations in ten
variables has a nonzero solution. There is an irreducible component Y
of Z dominating the a-projective space: the finitely many component
images are closed and cover the irreducible base.

If b is nonconstant on Y, choose two nonproportional coordinate functions
b_s,b_t. The20 coordinate sections a_i b_s,a_i b_t have at most one
linear relation. Indeed, any relation is L(a)b_s+M(a)b_t=0 with linear
forms L,M. In a nonzero relation they are nonzero and nonproportional,
since Y dominates the a-space and b_s/b_t is nonconstant. A second
relation gives LM'-L'M=0 as a polynomial in a. The independent linear
forms L,M are coprime, so L'=cL,M'=cM with c constant. Thus the space
of relations has dimension at most one. The linear span of Y, and hence
T, has dimension at least19, contradicting (9).

Otherwise b is constant on Y, so Y=P^9 times one point [b_0]. By the
same argument applied to a component dominating the b-space, either
its span already has dimension at least19, or it is one point [a_0]
times P^9. In the latter case T contains

    (C^10 tensor b_0)+(a_0 tensor C^10),

of dimension19 as well. This proves the contradiction in every case,
including p=9, where the simpler basis-fiber dimension bound is only10.
Therefore

    d=16 implies h>=10.                                    (10)

This excludes pole orders1 through9 in the balanced first map, allowing
arbitrary higher regular coefficients in both long maps. Pole order10
is not excluded or constructed. The external inputs above are standard
algebraic geometry, not results of this repository; their exact tags,
hypotheses and access date are recorded in sources.json.

## 5. Equality leading equations are feasible

The rank-one leading bound is attainable for equation (2). Take the
literal source coordinate f_(0,0,0)=1, whose slice has16 distinct
nonzero row/column pivots. For any3<=q_B<=13, partition those pivots into
q_B killed rows and q_C=16-q_B killed columns. Coordinate long maps
of ranks112-q_B and112-q_C annihilate the entire slice, and both ranks
are at most109. Padding their target rows and columns to110 gives the
stated formats. Adding t times q_B-2 deleted row coordinates and q_C-2
deleted column coordinates makes both maps have rank110 over K.

With first lift t^(-1)f, every negative output coefficient vanishes;
the constant output is a partial permutation of rank12. This is not a
target identity, whose rank would be110. These exact controls show only
that the leading equation and bound rank L=1 are sharp at this level.
They do not provide later jets or an A4 target.

## 6. Scope and evidence

The full-source minimum, complete minimum-rank locus, coherent-factor
locus and PR113 obstruction are predecessor results, retained with exact
byte pins and their original credit. Section4 imports the two explicitly cited standard graph-descent facts.
The equality row/column-intersection argument here is elementary and
has no historical priority claim. All new proofs and finite controls are
owner-directed OpenAI Codex work, with written-unreviewed status.

Remaining candidates with d>=32 are unrestricted by the coherent-factor
bound here. For16<d<32, rank L<=16 is only necessary. At d=16, pole
orders at least10 with a single minimum-rank leading direction remain open.
Neither this flag reduction nor its exact finite controls construct or
exclude the general A4 target or improve the matrix exponent below9/4.
