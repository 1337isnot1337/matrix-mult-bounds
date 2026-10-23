# One-sided unit compression strengthens Laurent regularity

October 23, 2026. Owner-directed Codex continuation over C. Written and
unreviewed; no independent review, formalization or exponent improvement.

## 1. Question and theorem

The [partial-unit-image theorem](../2026-10-23-regular-unit-image/proof.md)
excludes A4 to M(10,10,11) when a regular source unit lift has image rank
at least 109 through a regular full-rank long map. Its two-sided target
compression and compressed source kernel count leave rank 108 open.
Keeping every target row and returning to the full long map improves both
estimates. The theorem below excludes image ranks 107 and 108 as well.

Let O=C[[t]], K=C((t)), and let M:A -> Mat_N(C) be a linear slice map.
For every nonzero f in A assume rank M(f)>=mu_A. For every nonzero source
row covector lambda assume the contraction f |-> lambda M(f) has rank
at least mu_B. Let Xi:E -> Mat_R(C) be an injective linear target map,
dim E=D, with minimum nonzero matrix rank at least nu and
Xi(x_unit)=I_R for a fixed x_unit in E.

Suppose the complete formal tensor identity is

    B(t) M(F(t)(x)) C(t) = Xi(x) + O(t), for all x in E.       (1)

Here F:E -> A, B of size R by N and C of size N by R have coefficients
in K. Assume C is regular with rank C(0)=R, and u=F(x_unit) is regular.
Write S=M(u). For an integer 1<=r<=R assume rank(S(0)C(0))>=r and set

    k=N-R,       e=R-r,       q=N-r=k+e.

If

    mu_A>3q,       nu-e>q,       D>dim A-mu_B+k,              (2)

then F and B are regular, F(0) is injective, and B(0) has full row rank.
The limit of (1) is an ordinary restriction to Xi. All three inequalities
are strict. There is no bound on the finite Laurent pole orders.

Consequently (1) is impossible if Xi has a nonzero slice of rank below
mu_A-2k. This last assertion needs the additional low-rank target slice;
it does not follow from the lower bound nu alone.

## 2. Independent source frames with no target-row compression

The unit equation G=BSC=I_R+O(t) is regular invertible. Replacing B by
G^(-1)B preserves the target constant tensor and regularity conclusions,
and gives BSC=I_R exactly. Use this normalized B below.

Choose a constant R-by-r matrix H with rank(S(0)C(0)H)=r. Both CH and
SCH have full column rank at zero. Complete them independently to regular
invertible N-by-N frames Q_C and Q_B, with these as their first r columns.
Only a nonzero constant minor is needed; no inverse of S is taken.

Set

    M_t(f)=Q_B^(-1) M(f) Q_C,
    B'=B Q_B,       C'=Q_C^(-1) C.

The limiting source M_0 retains both rank minima. Exactly,

    C'H=[I_r;0],       B'=[H,L(t)].

Block the source into row and column sizes (r,q), writing Xij for the
blocks of M_t(F(x)). Multiplying (1) on the right by H gives

    H X11 + L X21 = Xi(x) H + O(t).                         (3)

There is no projection on the R target rows. In particular every nonzero
Xi(x)H has rank at least nu-e. This loses only e target columns.

## 3. First-map regularity and injectivity

If F has a pole, choose x with pole order h>0 and nonzero leading
coefficient f=F_-h(x). All Xij have pole order at most h. By (3),
t^h L X21 is regular and its constant coefficient is -H X11,-h.
This regularized product has rank at most q: all (q+1)-minors vanish over
K and remain zero after specializing its regular entries. Since H is
injective, rank X11,-h<=q. Adding the bottom q rows and last q columns
therefore gives rank M_0(f)<=3q, contradicting the first inequality (2).
Thus F is regular. The raw constant coefficient of an unregularized
Laurent product need not have rank at most q and is not used here.

Suppose F_0(x)=0 for a nonzero x. All Xij vanish at zero. Equation (3)+makes L X21 regular with constant coefficient Xi(x)H. Its rank is at
most q by the same closed-minor argument, contradicting nu-e>q. Hence
F_0 is injective. This conclusion does not yet assume B or L regular.

## 4. Use the original full long map for the final contradiction

The complete transformed identity is

    B' M_t(F(x)) C' = Xi(x)+O(t),                          (4)

and C'_0 has full rank R. If B' has a pole of order s>0, its leading
coefficient B'_-s is nonzero. Because F, M_t and C' are regular, the
t^-s coefficient of (4) is

    B'_-s M_0(F_0(x)) C'_0 = 0, for all x in E.

Take a nonzero row lambda of B'_-s. The source contraction
f |-> lambda M_0(f) has rank at least mu_B. Right multiplication by
C'_0 loses at most k=N-R dimensions, so

    dim ker(f |-> lambda M_0(f) C'_0) <= dim A-mu_B+k.

This kernel contains the injective D-dimensional image of F_0, contrary
to the last inequality (2). Therefore B' and B are regular. The defect
here is k, not q: C'_0 is the original N-by-R map, rather than C'_0 H.

At zero B_0 S_0 C_0=I_R, forcing B_0 to have rank R. Equation (1) now
specializes to an ordinary restriction. Multiplication by B_0 and C_0
loses at most 2k source slice rank, proving the final assertion of Section 1.
Reversing the normalization by G and the regular source frames preserves
all conclusions. In particular a strictly deficient S_0 C_0 is itself
incompatible with the now regular unit equation.

## 5. A4: exclude unit-image rank at least 107

For the canonical A4 source and Xi(X)=X tensor I_11 on Mat_10, the
[prior source and target calculation](../2026-10-20-koszul/cyclic_finite_target.md)
gives

    dim A=N=112, R=110, D=100, mu_A=mu_B=16, nu=11, k=2.

At r=107, e=3 and q=5. The strict margins in (2) are

    16-3*5=1,       11-3-5=3,       100-(112-16+2)=2.

The theorem applies. A rank-one X has target slice rank 11, below the
ordinary source floor 16-2*2=12. Thus there is no A4 to M(10,10,11)
formal degeneration satisfying the stated regularity hypotheses with
rank(S_0 C_0)>=107. The assertion is symmetric in the two long legs.
A regular unit slice of corank at most three is included because
rank(S_0 C_0)>=110-corank S_0. No generic alignment is assumed.

This strengthens the earlier rank-109 result; that result remains valid
with its original proof and scope. Any remaining degeneration with a
regular full-rank C and a regular identity lift must have
rank(S_0 C_0)<=106. At r=106 the first inequality would require 16>18,
so this proof makes no exclusion there. Singular long-leg limits and
polar identity lifts remain open. No matrix target or smaller exponent
is constructed.

## 6. Evidence and attribution

The canonical source, its all-size rank minimum, its ordinary A4
obstruction, normalized Laurent product argument and partial-unit source
frames retain their prior credit. Their bytes are pinned in sources.json.
This continuation keeps all target rows in (3) and uses the complete
column map in (4). Both changes use elementary matrix rank and formal
Laurent coefficients; no new external theorem is imported.

The verifier supplies exact finite sharp controls for the two different
rank losses, the three-part source rank budget, and the regularized
product rule. It checks the numerical boundary through r=106 and retains
the failed sufficient test at that boundary. These controls do not
formalize arbitrary series or provide independent mathematical review.
