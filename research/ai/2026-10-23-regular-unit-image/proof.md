# Laurent regularity from a partial regular unit image

October 23, 2026. Written, unreviewed, owner-directed Codex work over C.
No independent mathematical review, formalization or exponent improvement.

## 1. General setting and result

Let O=C[[t]], K=C((t)). Let M:A -> Mat_N(C) be a linear slice map of a
tensor. Its minimum nonzero first-leg slice rank is at least mu_A; its
minimum nonzero row-leg contraction rank is at least mu_B. A row-leg
contraction is the map A -> C^N, f |-> lambda M(f) for nonzero lambda.
These assumptions are invariant under invertible changes on all three
source legs.

Let Xi:E -> Mat_R(C) be an injective target slice map, with dim E=D,
minimum nonzero matrix rank at least nu, and Xi(x_unit)=I_R for a fixed
x_unit. Suppose Laurent maps F:E -> A, B of size R by N and C of size
N by R satisfy the complete tensor identity

    B(t) M(F(t)(x)) C(t) = Xi(x) + O(t) for every x in E.       (1)

Assume C is regular and C(0) has rank R. Assume u=F(x_unit) is regular;
write S=M(u). Choose an integer r with 1<=r<=R such that

    rank(S(0) C(0)) >= r.

Put e=R-r, k=N-R and q=N-r=k+e. If

    mu_A > 3q,       nu-2e > q,       D > dim A-mu_B+q,        (2)

then B and F are regular. Moreover B(0) has full row rank, and their
constant terms together with C(0) give an ordinary restriction to Xi.

The conclusion is a regularity theorem under the stated rank margins.
If Xi has a nonzero slice of rank less than mu_A-2k, such a degeneration
is impossible. The low-rank target slice is a separate hypothesis for
this final exclusion, not a consequence of the lower bound nu.

The theorem does not require S(0) to be invertible. It does not assume
a chosen leading source flag or bound any Laurent pole order.

## 2. Select the unit columns before changing source frames

The unit equation in (1) is

    G(t)=B(t) S(t) C(t)=I_R+O(t).

Thus G is regular invertible. Replace B by G^(-1)B. This preserves the
target constant tensor and all regularity conclusions, and makes BSC=I_R
exactly. In what follows B denotes this normalized map.

Choose a constant R-by-r full-column-rank matrix H such that S(0)C(0)H
has rank r. Both C H and S C H are regular full-column-rank matrices at
zero. Independently complete them to regular invertible N-by-N frames
Q_C and Q_B whose first r columns are respectively C H and S C H.
This uses a nonzero constant minor; no Laurent inverse of S is taken.

For any constant left inverse P of H, so P H=I_r, use the compressed
target slice map

    Xi_P(x)=P Xi(x) H.

Deleting e dimensions on each side loses at most 2e in rank. Every
nonzero Xi_P(x) has rank at least nu-2e. By (2) this is positive, so
Xi_P is injective and its parameter dimension remains D.

In these independent source frames set

    M_t(f)=Q_B^(-1) M(f) Q_C,
    B_P=P B Q_B,           C_H=Q_C^(-1) C H=[I_r;0].

The source M_t is regular and its limiting tensor retains both source
rank minima. Since BSC=I_R,

    B_P=[I_r,L_P(t)],
    B_P M_t(F(x)) C_H = Xi_P(x)+O(t).                    (3)

The frames do not depend on P. A constant source-row shear removes the
constant coefficient of L_P if needed. It is regular invertible and
does not change either source rank minimum. A full invertible source
unit, or a conjugation preserving such a unit, is unnecessary here.

## 3. Why every compressed long map is regular

We give the normalized argument, retaining its all-order quantifiers.
It extends the credited normalized lemma in the earlier
[regular-unit proof](../2026-10-21-cyclic-slice-determinants/unital_chart.md).

Suppose L_P has a nonzero principal part. If F has a pole of order h>0,
choose x with nonzero leading coefficient f=F_-h(x). Write M_t(F(x)) in
blocks with row/column sizes (r,q), denoted X11,X12,X21,X22. Equation (3)
says X11+L_P X21 is regular. All X blocks have pole order at most h,
so t^h L_P X21 is regular with constant coefficient -X11,-h.

The product L_P X21 has inner dimension q. Every regularized leading
coefficient of that product has rank at most q: its (q+1)-minors vanish
over K and still vanish after specialization of the regularized matrix.
Adding the bottom q rows and last q columns gives

    rank M_0(f) <= q+q+q=3q,

contrary to mu_A>3q. This excludes every first-map pole.

Now F is regular. If F_0(x)=0, then X11(0)=0 and L_P X21 is regular
with constant coefficient Xi_P(x). The same product-rank fact gives
rank Xi_P(x)<=q. The inequality nu-2e>q forces x=0. Hence F_0 is
injective.

Let L_-s be the leading nonzero negative coefficient of L_P. The t^-s
equation in (3) gives L_-s X21,0(F_0(x))=0 for every x. A nonzero row
of L_-s is a nonzero covector lambda on the bottom q source rows.
The map f |-> lambda X21,0(f) is a nonzero source-row contraction
followed by deleting the last q columns. Its rank is at least mu_B-q.
Thus its kernel has dimension at most dim A-mu_B+q. It contains the
injective D-dimensional image of F_0, contradicting (2).

Consequently L_P, and hence P B, is regular for every constant left
inverse P of H. Notice the logical order: the temporary assumption of
a compressed pole supplies regularity and injectivity of F for the
dimension contradiction. We have not assumed either globally in advance.

## 4. Recover the whole long map and then the first map

Choose constant target coordinates in which H=[I_r;0]. Every left
inverse is P_Z=[I_r,Z], where Z is an arbitrary r-by-e constant matrix.
In the same target coordinates write B=[B_top;B_bottom]. Then

    P_Z B=B_top+Z B_bottom.

P_0 B is regular. For each bottom row j, take Z with the sole nonzero
entry Z_(1,j)=1. The first row of (P_Z-P_0)B is that bottom row.
Thus e+1 left inverses suffice to recover every row of B as a regular
linear combination. This also covers e=0 with P=I_R. Reversing constant
target coordinates and multiplying by G recovers the original regular B.

Because u and C are regular, taking the unit equation at zero now gives

    B(0) S(0) C(0)=I_R.

In particular B(0) has rank R. This would already contradict a unit
image of rank strictly less than R, but also handles its full-rank case.

If F had a pole, its highest negative coefficient f on some x would
satisfy B(0) M(f) C(0)=0. Two full-rank maps with source defect k lose
at most 2k matrix rank, so rank M(f)<=2k<mu_A. This is impossible.
Hence F is regular, and (1) specializes to an ordinary restriction.
Any nonzero target slice lifts to a nonzero source slice and therefore
has rank at least mu_A-2k. This proves the final exclusion assertion.

## 5. The A4 consequence

Use the canonical cyclic source A4 and target M(10,10,11), with first
target slices Xi(X)=X tensor I_11. The previously written elementary
[minimum-rank theorem](../2026-10-20-koszul/cyclic_finite_target.md),
Sections 2-3, gives

    dim A=N=112, R=110, D=100, mu_A=mu_B=16, nu=11.

Assume one long map C is regular with full-rank limit and the lift of
the target I_10 is regular. If rank(S(0) C(0))>=109, take r=109. Then

    e=1, q=3, 16>9, 11-2=9>3, 100>112-16+3=99.

The theorem makes all maps regular. But the ordinary source-rank lower
bound is 16-2*(112-110)=12, whereas a target rank-one X gives slice rank
11. Contradiction. The assertion holds with the two long legs exchanged.

In particular a regular unit slice of corank at most one is excluded,
because rank(S(0) C(0))>=110-corank S(0)>=109. Some unit slices of
higher corank also meet the image-rank hypothesis; no generic alignment
assumption is required. This strictly extends the older invertible-unit
chart. A remaining degeneration with a regular full-rank C and a regular
unit lift must have rank(S(0) C(0))<=108.

Taking r=108 gives q=4 and only 100>100 in the last required strict
inequality, which fails. This argument makes no exclusion at that
boundary. It also leaves singular long-leg limits and polar unit lifts
open. The full matrix target and exponent below 9/4 remain unconstructed.

## 6. Evidence and attribution

The canonical source, its all-size rank minimum, the ordinary A4
exclusion, and the normalized Laurent rank lemma are prior repository
work, pinned in sources.json and credited above. This continuation adds
independent row/column frame completions for a partial unit image, target
compression, finite left-inverse recovery, and the weaker A4 hypothesis.
Only elementary linear algebra and formal Laurent coefficients are used.
No additional external theorem is imported.

The verifier checks source pins and explicit exact matrix controls for
the rank budgets, the recovery identities, singular-unit examples and
the strict numerical margins. Those finite controls do not verify all
formal series or constitute independent review of this written proof.
