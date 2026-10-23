# Unequal regular frames and a unital rank upgrade

October23,2026. Written, unreviewed owner-directed Codex work. The
full-source A4 degeneration and exponent below9/4 remain open.

## 1. General unital theorem

Keep the notation and three contraction minima of the
[partial-frame theorem](../2026-10-23-partial-regular-frames/proof.md).
In particular the source is M:A -> Mat_N(C), the target slice space
Xi:E -> Mat_R(C) is concise on all three legs, dim E=D, and every
nonzero target slice has rank at least nu. In addition suppose
Xi(x_unit)=I_R. All maps F,B,C in the complete formal tensor identity
may have arbitrary finite Laurent poles.

Let H be a constant R-by-r_C injection, J a constant R-by-r_B injection,
and V,U regular N-by-r_C and N-by-r_B matrices satisfying

    C H=V,       B U=J,
    rank V(0)=r_C,       rank U(0)=r_B.                  (1)

Set q_B=N-r_B, q_C=N-r_C and e_B=R-r_B, e_C=R-r_C. If

    mu_A>2q_B+q_C,          nu-e_B-e_C>q_B,
    D>dim A-mu_B+q_C,       D>dim A-mu_C+q_C,            (2)

then all three maps are regular and give an ordinary restriction.
No regularity of the source lift of x_unit is assumed.

## 2. The rectangular normalized argument

Complete U and V independently to regular invertible source frames
Q_B,Q_C. For every constant left inverse P of J, the two compressed
long maps become

    P B Q_B=[I_(r_B),L_P],       Q_C^(-1) C H=[I_(r_C);0].

The target P Xi(x) H has rank at least nu-e_B-e_C for nonzero x, by
two-sided rank loss, and hence remains injective on E. The source
slice blocks now have row sizes(r_B,q_B), column sizes(r_C,q_C).

Suppose L_P has a pole. If F has a pole of maximal order h, equation
X11+L_P X21=target+O(t) makes t^h L_P X21 regular. Its constant
coefficient has rank at most q_B, the product's inner dimension.
The bottom q_B rows and last q_C columns then give

    rank M_0(f) <= 2q_B+q_C < mu_A

for a nonzero leading first-map coefficient f, a contradiction. Thus
F is regular under this temporary pole assumption.

If F_0(x)=0, the constant compressed target coefficient comes solely
from the regularized product L_P X21 and has rank at most q_B.
The second inequality of (2) makes F_0 injective. A nonzero row of the
leading pole coefficient of L_P annihilates F_0(E) after the source
row contraction and deletion of q_C columns. This map has rank at
least mu_B-q_C. Its kernel cannot contain an injective D-dimensional
image by the third inequality. No compressed L_P has a pole.

Varying P through the e_B+1 left inverses in the predecessor recovery
identity proves the entire B regular. In particular rank B(0)>=r_B,
since B(0)U(0)=J. A first-map pole is now impossible from the regular
compressed equation: two compressions lose at most q_B+q_C<mu_A.
The same compressed equation and target injectivity make F_0 injective.
Thus B and F are regular even though C may still have poles.

## 3. The target identity upgrades the missing row rank

Now S=M(F(x_unit)) is regular, as a consequence of the preceding step.
The unit equation is BSC=I_R+O(t). Multiplying by H gives a regular
product because C H=V is regular. Its constant term is

    B(0) S(0) V(0)=H.

Therefore rank B(0)>=r_C, irrespective of its original right-frame
dimension r_B. If C has a pole, choose a nonzero leading pole column z.
Exactly as in the predecessor column argument,

    B(0) M(F_0(x)) z=0 for every x,

but the map f |-> B(0) M(f) z has rank at least mu_C-q_C. Its kernel
has dimension at most dim A-mu_C+q_C, contradicting the fourth
inequality and injectivity of F_0. Hence C is regular.

The target is now an ordinary restriction. Its conciseness forces both
constant long maps to have rank R; its source-rank floor is
mu_A-2(N-R). All arguments cover every finite Laurent pole order.

## 4. Formulate the hypotheses using partial unit images

There is a convenient sufficient condition for (1). For constant
injections H of size R-by-r_C and K of size R-by-r_B, assume

    C H is regular of limiting rank r_C,
    S C K is regular of limiting rank r_B.              (3)

The target subspaces im H and im K need not agree or be nested. The
whole C and S may have poles. Let G=BSC=I_R+O(t). Normalize B by
G^(-1)B, which changes no target constant term or regularity question.
Then U=S C K, V=C H and J=K satisfy (1) exactly. The theorem applies.

This uses no inverse of S. After regularity is proved one may undo
the regular target normalization. The simultaneous partial frames in
(3) are hypotheses and are not constructed for arbitrary degenerations.

## 5. Complete A4 frame-budget application

For A4 to M(10,10,11), the adopted data are

    N=dim A=112, R=110, D=100,
    mu_A=mu_B=mu_C=16, nu=11.

There are exactly nine pairs(r_B,r_C) in {1,...,110}^2 satisfying (2):

    r_C=109 with r_B=107,108,109,110;
    r_C=110 with r_B=106,107,108,109,110.

The two coordinatewise minimal pairs are(107,109) and(106,110).
This is direct finite integer bookkeeping for the sufficient theorem,
not a classification of all possible degeneration frames.

At(107,109), the four strict margins are3,2,1,1. At(106,110), they are
2,1,2,2. In both cases all maps become regular, contrary to the
ordinary source floor12 and target rank11 slice. At r_C108 the two
dimension margins are zero. At(106,109) the injectivity margin is zero;
at(105,110) the first-pole and injectivity conditions fail. These cases
remain outside this theorem.

In particular, if C is entirely regular with full-rank limit and the
target-unit lift is regular, it suffices to have

    rank(S(0) C(0)) >= 106.                             (4)

Take H=I_110 and choose106 independent columns of the regular matrix
SC for K. Equation(3) and the(106,110) case prove exclusion. This
weakens PR105's rank109 condition. Every regular source unit of corank
at most four satisfies(4), since rank(S(0)C(0))>=110-corank S(0).
Some higher-corank units also satisfy(4), depending on their alignment.
The rank105 boundary is not excluded here.

The symmetric assertion follows by exchanging the two long tensor legs.
No matrix-target construction or exponent improvement is established.

## 6. Attribution and evidence

The predecessor partial-frame proof supplies finite left-inverse recovery
and the three-leg regularity strategy. The original minimum-rank source
theorem and ordinary A4 exclusion retain their credit. Unequal normalized
blocks and the target-unit rank upgrade are the local continuation.
No new external theorem is imported. Exact finite controls verify the
complete12100-pair rank-budget scan and supporting examples; they do not
formalize the all-order proof or constitute independent review.
