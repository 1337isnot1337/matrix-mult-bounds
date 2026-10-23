# Partial regular frames force Laurent regularity

October 23, 2026. Written, unreviewed owner-directed Codex work. This
extends the partial-unit-image argument of PR105. It does not construct
a matrix target, exclude all degenerations or improve the exponent.

## 1. A unit-free regular-frame theorem

Work over O=C[[t]] and K=C((t)). Let M:A -> Mat_N(C) be the slice map
of a tensor. Suppose its minimum nonzero contraction ranks on the first,
row and column legs are at least mu_A, mu_B and mu_C respectively. For
the row leg this means the rank of f |-> lambda M(f), for every nonzero
row covector lambda; for the column leg it means the rank of
f |-> M(f) z, for every nonzero column vector z.

Let Xi:E -> Mat_R(C) be a concise tensor on all three legs, with
dim E=D and minimum nonzero matrix-slice rank at least nu. Suppose
arbitrary finite Laurent maps F,B,C satisfy

    B(t) M(F(t)(x)) C(t)=Xi(x)+O(t),       x in E.          (1)

Choose r with 1<=r<=R and put e=R-r, q=N-r. Assume there exist constant
R-by-r injections H,J and regular N-by-r matrices V,U such that

    C(t) H=V(t),       B(t) U(t)=J,                      (2)
    rank V(0)=rank U(0)=r.

Neither whole long map is assumed regular. No regular unit lift or
target identity is assumed. The two partial frames U,V are allowed to
vary regularly with t; their source subspaces need not agree.

If

    mu_A>3q,       nu-2e>q,
    D>dim A-mu_B+q,       D>dim A-mu_C+q,                (3)

then F,B,C are all regular. Their constant terms give an ordinary
restriction to Xi, with B(0),C(0) both of full target rank R.

## 2. Recover B through every left inverse of J

Complete V and U independently to regular invertible source frames
Q_C,Q_B. Let P be any constant left inverse of J. In these frames

    C_H=Q_C^(-1) C H=[I_r;0],
    B_P=P B Q_B=[I_r,L_P],
    M_t(f)=Q_B^(-1) M(f) Q_C.

The transformed source is a regular family whose limiting contraction
minima are unchanged. The compressed target Xi_P(x)=P Xi(x) H has
minimum nonzero matrix rank at least nu-2e and is injective on E.
The rank bound uses the rank-r maps P and H and does not require H=J.

Thus

    [I_r,L_P] M_t(F(x)) [I_r;0]=Xi_P(x)+O(t).             (4)

The normalized pole argument of the
[partial-unit-image proof](../2026-10-23-regular-unit-image/proof.md),
Section 3, applies verbatim: a pole of L_P first forces F regular by
the 3q rank bound, then makes F_0 injective by nu-2e>q, and finally
puts its D-dimensional image in a kernel of dimension at most
dim A-mu_B+q. The first three inequalities of (3) contradict that.
Consequently P B is regular for every constant left inverse P of J.

In target row coordinates with J=[I_r;0], take P_Z=[I_r,Z]. The
predecessor's finite recovery identity, using Z=0 and one elementary
Z for each of the e missing rows, proves B regular. Exactly e+1 such
projections suffice. This step uses no regularity of the unselected
columns of C or any source-unit slice.

## 3. Regularity and injectivity of the first map

Fix one such left inverse P. Equation B_P=[I_r,L_P] and regularity of
Q_B imply that (P B)(0) has rank r. V(0) also has rank r.

If F has a pole of maximal order h>0, take x with nonzero leading
coefficient f. The t^-h equation of P times (1) times H is

    (P B)(0) M(f) V(0)=0.

Two rank-r source compressions lose at most 2q in matrix rank. Hence
rank M(f)<=2q<mu_A, a contradiction. F is regular.

If F_0(x)=0, the same compressed equation at zero gives Xi_P(x)=0.
Its positive minimum rank makes Xi_P injective, so x=0. Therefore
F_0:E -> A is injective. This conclusion does not require C itself
to be regular: C H=V is the regular matrix in this argument.

## 4. Eliminate the remaining long-map poles

Suppose C has a pole of maximal order s>0, and choose a nonzero column
z of its leading coefficient C_-s. Since B and F are now regular, the
t^-s equation in (1) gives, for every x in E,

    B(0) M(F_0(x)) z=0.                                  (5)

The column contraction A -> C^N, f |-> M(f) z, has rank at least mu_C.
The map B(0) has rank at least r because B(0)U(0)=J. Projecting through
B(0) loses at most N-r=q dimensions. Therefore

    rank(f |-> B(0) M(f) z) >= mu_C-q.

Its kernel has dimension at most dim A-mu_C+q. By (5) it contains the
injective D-dimensional image F_0(E), contradicting the fourth strict
inequality in (3). Thus C is regular.

All maps are regular, so (1) specializes to an ordinary restriction.
Conciseness of the target row and column legs forces B(0),C(0) to have
rank R. In particular its minimum nonzero matrix-slice rank is at least
mu_A-2(N-R). A target slice below that floor rules out (1).

## 5. The weaker unit-image hypothesis and A4

Suppose the target has a unit x_unit with Xi(x_unit)=I_R. Write
S=M(F(x_unit)), allowing poles in the unit lift. Suppose a constant
R-by-r injection H has the following two properties:

    C H is regular with rank-r limit,
    S C H is regular with rank-r limit.                  (6)

The full unit equation gives G=BSC=I_R+O(t), regular invertible.
Replace B by G^(-1)B; this preserves the limiting target and regularity
questions and makes BSC=I_R exactly. Then V=C H, U=S C H and J=H
satisfy (2). This normalization does not alter U or V. No inverse of S
is taken and neither S nor the unselected columns of C need be regular.

For A4 to M(10,10,11), choose r=109. The known source data are

    N=dim A=112, R=110, D=100,
    mu_A=mu_B=mu_C=16, nu=11, e=1, q=3.

The four strict margins in (3) are 7,6,1,1. Thus (6) forces all maps
regular, contradicting the ordinary source-rank floor12 and the target's
rank11 slice. There is no such degeneration. This includes the entire
previous regular-unit-image chart, but also permits polar coefficients
of C and of the unit slice away from the selected partial frames.
The assertion is symmetric in the two long tensor legs.

More generally the unit-free theorem excludes this A4 target whenever
there are partial frames of size109 as in (2), even if they are unrelated
to any target-unit image. Those frames are hypotheses, not constructed
from arbitrary Laurent maps here.

At r=108 both dimension margins become zero, and this theorem gives no
exclusion. Without suitable partial frames, general Laurent degenerations
remain open. No exponent improvement follows from an obstruction alone.

## 6. Attribution and evidence boundary

The previous partial-unit-image proof supplies the normalized Laurent
argument and finite projection recovery. The original cyclic minimum
rank and ordinary obstruction retain their credit. The additional
column-contraction step and partial-frame formulation are local Codex
continuations. All three source contraction minima come from the
previous all-size theorem and cyclic source leg symmetry.

Exact finite controls and source pins accompany this proof. They verify
matrix identities, strict margins and escape cases; they do not establish
the all-order quantifiers or independent mathematical review. No additional
external theorem is imported.
