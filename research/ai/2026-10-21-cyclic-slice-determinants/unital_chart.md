# A low-pole obstruction with a regular invertible unit lift

October 21, 2026. Claim `AI-CYCLIC-UNITAL-LOW-POLES-003` is a written,
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
3. B(t) is Laurent with pole order at most five.

All other first-leg coefficients may have arbitrary finite Laurent poles.
Every higher regular coefficient of all maps is allowed. The asserted
tensor identity is M(10,10,11)+O(t), so every unwanted negative and constant
coefficient must vanish.

No such degeneration exists. The result also holds after exchanging the
two long legs. It does not assume a canonical source leading flag or a
particular invertible source unit.

In an exact unit normalization described below, the stronger necessary
condition is that the images of the negative long-map coefficients span
at least 11 dimensions. Thus a fixed principal image of dimension at most 10
is excluded at every Laurent order. The order-six conclusion follows
because each negative coefficient has only two free columns.

The hypotheses are material. A construction can escape by making the
regular long-leg limit lose rank, by having a singular or polar source
lift of every chosen target unit, or by using the larger principal image
and higher Laurent order. None of those cases is excluded here.

## Source and target rank data

Use the maintained [cyclic source matrix](../2026-10-20-koszul/cyclic_finite_target.md).
For A_a, every nonzero slice on every leg has rank at least a^2, with
equality at a coordinate slice. The original proof exhibits a triangular
a^2-by-a^2 minor: select a nonzero middle coefficient, then the largest
nonzero two short indices; every diagonal entry is that nonzero scalar.
It works over every field. Leg symmetry gives the other two minima.

Thus A4 has source dimensions 112 and minimum slice ranks 16 on its first
and row legs. The target first-leg slice matrix is X tensor I11, for a
10-by10 matrix X. Every nonzero such slice has rank at least 11, and the
target first-leg parameter space has dimension 100.

The [unimodular slice](proof.md) supplies a concrete invertible source unit.
It does not prove that every degeneration has a regular invertible lift
of a target unit. The present statement assumes that property explicitly.

## Normalized rank lemma

Let M_t:A -> Mat_N be a regular formal family of linear slice maps. At
t=0 assume minimum nonzero first-leg slice rank at least mu_A and minimum
nonzero row-leg contraction rank at least mu_B. Put R=N-k and set

    C=[I_R;0],        B(t)=[I_R,L(t)],       L_0=0.       (1)

Let F(t):E -> A be any Laurent linear map such that

    B(t) M_t(F(t)(x)) C = Xi(x)+O(t),     x in E.        (2)

Assume Xi is concise on E, with dim E=D, and every nonzero Xi(x) has
rank at least nu. Suppose the principal part of L is nonempty, and let

    V=span of the images of all negative coefficients of L,
    d=dim V.

If

    d<nu,             mu_A>d+2k-1,                     (3)

then F(t) is regular and

    D <= dim A-mu_B+k.                                 (4)

The source family is allowed to vary regularly. This is needed for the
regular changes of source frame used later; the two rank hypotheses are
imposed on its limiting tensor only.

### First poles cannot survive

Let L_-s be the nonzero leading negative coefficient, of rank h>=1.
Suppose F has a pole of order r>0 and choose x such that f=F_-r(x) is
nonzero. Write

    M_0(f) = [ X11 X12 ],
             [ X21 X22 ]

in the(R,k) row and column decomposition. The coefficient at t^(-s-r)
in(2) is L_-s X21=0. Therefore rank X21<=k-h.

At t^-r the unmultiplied top block is exactly X11. Every other term
contains a negative coefficient of L as its left factor. Positive-order
source coefficients cannot create another unmultiplied block at this
order, since F has no coefficient below-r. Consequently X11 has image
in V and rank at most d.

The first R columns of M_0(f) have rank at most d+k-h. The remaining
k columns add at most k. Hence

    rank M_0(f) <= d+2k-h <= d+2k-1 < mu_A,

contradicting the source minimum. Thus F is regular.

### The constant first map must be injective

Now the coefficient at t^-s in(2) gives

    L_-s X21,0(F_0(x))=0.

Choose any nonzero row covector lambda in the row space of L_-s. The
image of F_0 lies in the kernel of

    A -> row vectors of length R,
    f |-> lambda X21,0(f).                             (5)

This is a nonzero source row contraction, followed by deleting k columns.
Its rank is at least mu_B-k. The kernel has dimension at most
dim A-mu_B+k.

If F_0(x)=0, every constant target contribution in(2) has image in V:
it must come from a negative coefficient of L times higher regular
coefficients of the source and first map. Such a matrix has rank at
most d<nu. Target conciseness then forces x=0. Thus F_0 is injective,
and its image lies in the kernel of(5). This proves(4).

## Regular frame and unit normalization

Start with the actual source tensor and maps in the A4 statement. Let
x_unit=I10 and u(t)=F(t)(x_unit).

Complete the regular nonzero vector u(t) to a regular invertible source
first-leg frame. In these coordinates its lift is a fixed vector a_unit;
the source becomes a regular family. Its unit matrix
S(t)=M_t(a_unit) is regular invertible by hypothesis2. Replace source
matrices by S(t)^(-1)M_t and replace B(t) by B(t)S(t). The source unit
is now exactly I_N. All these source changes are regular invertible at
zero, so the limiting minimum slice ranks stay16. The long-map pole
order does not increase.

The target unit contraction is now

    G(t)=B(t)C(t)=I_R+O(t).

It is regular invertible. Multiplying the target row map by G(t)^(-1)
makes the unit contraction exactly I_R, preserves the target limit, and
does not increase its pole order.

Because C(0) has full column rank, complete C(t) to a regular invertible
N-byN source frame Q(t). Conjugate the unit-normalized source matrices
by Q(t), replace B by BQ, and replace C by Q^(-1)C. The latter is the
fixed inclusion in(1); the unit remains I_N. The other map must have
the form[I_R,L(t)]. A constant shear preserving that inclusion removes
L_0, with a further constant source conjugation. This yields(1)-(2).

Regular invertible source changes preserve the rank minima at zero.
They can introduce arbitrary higher regular source coefficients, which
the normalized lemma already allows. In particular no constant-source
assumption is used incorrectly after this normalization.

If the original long map has pole order at most p, so does L. Each
negative coefficient is an R-byk matrix. Therefore

    d<=kp.                                            (6)

## Substitute the A4 dimensions

Here N=dim A=112, R=110, k=2, D=100, mu_A=mu_B=16 and nu=11.
For 1<=p<=5, equations(3) follow from

    d<=2p<=10<11,
    16>10+4-1=13.

But(4) would say 100<=112-16+2=98, a contradiction. More generally,
any nonempty principal part with d<=10 gives the same contradiction,
regardless of its largest pole order.

If there is no pole, both long maps are regular of full rank at zero
after unit normalization. A first-map pole would force a nonzero source
slice to be killed by the two codimension-two projections, whose total
rank loss is at most four. This contradicts the source minimum16, so
the first map is regular too. Every nonzero limiting target slice then
has rank at least 16-4=12. The actual target has slices of rank 11. This
is the already maintained ordinary-map obstruction, and handles p=0.

The symmetric statement follows by exchanging the two long tensor legs.
The conclusion is a necessary complexity bound inside the stated unit
chart, not a construction at order six and not a global A4 exclusion.

## Verification status and attribution

The proof uses the existing full-source minimum-rank theorem and elementary
rank loss under projection, formal Laurent coefficients, and regular frame
completion. Those standard facts are not claimed as new. The normalization
and this low-pole application are local work without independent review.
The integer source and target dimensions can be checked separately, and
explicit block matrices show the leading-rank bound d+2k-h is sharp as a
linear-algebra estimate. Such finite controls do not formalize the proof.
