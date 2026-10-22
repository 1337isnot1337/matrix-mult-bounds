# An all-order obstruction with a regular invertible unit lift

October 21, 2026. Claim `AI-CYCLIC-REGULAR-UNIT-003` is a written,
unreviewed argument. No general degeneration or smaller exponent is proved.

## A4 statement

Consider a formal complex degeneration from A4 to M(10,10,11). Write its
first map as a lift F(t) from the 100-dimensional target covector space
to the 112-dimensional source covector space. Write the two other maps
in matrix-slice notation as B(t) of size 110 by 112 and C(t) of size 112
by 110. Assume:

1. C(t) is regular at zero and C(0) has rank 110.
2. For the target first-leg identity I10, the source lift
   u(t)=F(t)(I10) is regular, and its source slice at zero is invertible.

No such degeneration exists. B(t) and all other first-leg coefficients
may have arbitrary finite Laurent poles. Every higher regular coefficient
of every map is allowed. The assertion is the complete tensor identity
M(10,10,11)+O(t), including every unwanted negative and constant coefficient.
The result also holds after exchanging the two long legs. It assumes no
canonical source leading flag or particular choice of invertible source unit.

The two hypotheses are material. A construction can escape by making
both long-leg limits singular, or by having a singular or polar source
lift of the chosen target identity. No such cases are excluded here.

## Source and target rank data

Use the maintained [cyclic source matrix](../2026-10-20-koszul/cyclic_finite_target.md).
The adopted convention and minimum-rank proof are pinned at main fd090bd4,
Sections 2-3 of that file. Here minimum slice rank means the minimum ordinary
matrix rank after contracting one tensor leg.
For A_a, every nonzero slice on every leg has rank at least a^2, with
equality at a coordinate slice. The original proof exhibits a triangular
a^2-by-a^2 minor: select a nonzero middle coefficient, then the largest
nonzero two short indices; every diagonal entry is that nonzero scalar.
It works over every field. Leg symmetry gives the other two minima.

Thus A4 has source dimensions 112 and minimum slice ranks 16 on its first
and row legs. The target first-leg slice is X tensor I11, for a 10-by10
matrix X. Every nonzero such slice has rank at least 11, a rank-one X
attains 11, and the target first-leg parameter space has dimension 100.

The [unimodular slice](proof.md) supplies a concrete invertible source unit.
It does not prove that every degeneration has a regular invertible lift
of a target identity. The present statement assumes that property.

## A rank fact for a regularized product

Let L(t) and Y(t) be matrices over the Laurent field, with inner dimension
k. Their product has rank at most k. If t^r L(t)Y(t) is regular for some
integer r, its constant coefficient also has rank at most k: all its
(k+1)-by-(k+1) minors vanish over the Laurent field, and hence vanish at
zero after regularization.

Regularity here is essential. A raw constant coefficient of a product
with remaining negative powers can have rank greater than k. The finite
controls explicitly exhibit this distinction. The argument below proves
the required regularity before applying the rank bound.

## Normalized rank lemma

Let M_t:A -> Mat_N be a regular formal family of linear slice maps. At
t=0 assume minimum nonzero first-leg slice rank at least mu_A and minimum
nonzero row-leg contraction rank at least mu_B. Put R=N-k and set

    C=[I_R;0],        B(t)=[I_R,L(t)],       L_0=0.       (1)

Let F(t):E -> A be any Laurent linear map such that

    B(t) M_t(F(t)(x)) C = Xi(x)+O(t),     x in E.        (2)

Assume Xi is concise on E, with dim E=D, and every nonzero Xi(x) has
rank at least nu. Suppose L has a nonempty principal part. If

    mu_A>3k,                  nu>k,                    (3)

then F(t) is regular and

    D <= dim A-mu_B+k.                                 (4)

The source family may vary regularly. This is needed for the source frame
changes later; the rank hypotheses concern only its limiting tensor.

### First poles cannot survive

Suppose F has a pole of order r>0. Choose x such that f=F_-r(x) is
nonzero. Write the blocks of M_t(F(t)(x)) as Xij(t), in the(R,k) row
and column decomposition. Their poles have order at most r. Equation(2)
says

    X11(t)+L(t)X21(t) is regular.

Consequently t^r L(t)X21(t) is regular and its constant coefficient is
-X11,-r. The rank fact above gives rank X11,-r<=k. The bottom k rows
of the first R columns of M_0(f) add at most k to its rank, and the last
k columns add at most k. Therefore

    rank M_0(f) <= 3k < mu_A,

contradicting the source minimum. Thus F is regular. This argument makes
no assumption on the pole order or the coefficient-image span of L.

### The constant first map must be injective

Now X11(t) and X21(t) are regular. Equation(2) implies L(t)X21(t) is
regular too. If F_0(x)=0, its constant coefficient is Xi(x), since
X11(0)=0. That coefficient has rank at most k by the rank fact. The
inequality nu>k and target conciseness then force x=0. Hence F_0 is
injective.

Let L_-s be the nonzero leading negative coefficient of L. The coefficient
at t^-s in(2) gives

    L_-s X21,0(F_0(x))=0.

Choose a nonzero covector lambda in the row space of L_-s. The image of
F_0 lies in the kernel of

    A -> row vectors of length R,
    f |-> lambda X21,0(f).                             (5)

This is a nonzero source row contraction, followed by deleting k columns.
Its rank is at least mu_B-k, so its kernel has dimension at most
dim A-mu_B+k. Injectivity of F_0 proves(4).

## Regular frame and unit normalization

Start with the actual source tensor and maps in the A4 statement. Let
x_unit=I10 and u(t)=F(t)(x_unit).

Complete the regular nonzero vector u(t) to a regular invertible source
first-leg frame. Its lift is then a fixed vector a_unit; the source
becomes a regular family. The unit matrix S(t)=M_t(a_unit) is regular
invertible by hypothesis2. Replace source matrices by S(t)^(-1)M_t and
replace B(t) by B(t)S(t). The source unit is now exactly I_N. These source
changes are regular invertible at zero, so the limiting slice minima stay 16.

The target unit contraction is now

    G(t)=B(t)C(t)=I_R+O(t).

It is regular invertible. Multiplying the target row map by G(t)^(-1)
makes this contraction exactly I_R and preserves the target limit.

Because C(0) has full column rank, complete C(t) to a regular invertible
N-byN source frame Q(t). Conjugate the normalized source matrices by
Q(t), replace B by BQ, and replace C by Q^(-1)C. Now C is the fixed
inclusion in(1) and the unit remains I_N. The other map must be[I_R,L(t)].
A constant shear preserving that inclusion removes L_0, while conjugating
the source by a constant invertible matrix. This gives(1)-(2).

All source changes are regular invertible at zero and preserve the two
rank minima there. They may introduce higher regular source coefficients;
the normalized lemma explicitly allows that variation. All transformed
maps remain Laurent with finite principal parts.

## Substitute the A4 dimensions

Here N=dim A=112, R=110, k=2, D=100, mu_A=mu_B=16 and nu=11. Equation(3)
holds because

    16>3*2=6,                 11>2.

If L has a pole, equation(4) would imply

    100 <= 112-16+2=98,

which is impossible. This excludes every finite Laurent pole order.

If L is regular, both long maps are regular of full rank at zero after
unit normalization. A first-map pole would give a nonzero source slice
killed by two codimension-two projections, whose total rank loss is at
most four. The source minimum 16 rules it out, so the first map is regular
too. Every nonzero target slice then has rank at least 16-4=12, whereas
the target has rank-11 slices. This is the already maintained ordinary-map
obstruction, and handles the case with no long-map pole.

The symmetric statement follows by exchanging the long tensor legs.
Any general A4 construction must therefore escape the regular-full-rank
long-leg plus regular-invertible-unit chart. No escape is constructed here.

## Verification status and attribution

The proof uses the existing full-source minimum-rank theorem, elementary
rank loss under projection, closed bounded matrix-rank loci, formal Laurent
coefficients and regular frame completion. Those standard facts are not
claimed as new. The frame argument and this all-order application are local
work without independent review or formalization. Finite integer block
controls check the relevant rank budgets and the distinction between a raw
constant coefficient and a regularized product. They do not formalize the
all-order proof and supply no matrix target or exponent improvement.
