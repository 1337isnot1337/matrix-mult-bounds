# Both nonzero mixed projections must be lines

Written proof, unreviewed, October 21, 2026. No smaller exponent is proved.

At the canonical rank-four leading flags, let W_B,W_C be the effective
first-extension spaces in E_B/G,E_C/G. If both have nonzero mixed
projections, then each mixed projection is a line. There are only two
possibilities:

* Both mixed matrices have rank one, with partner vectors related by
  `(v0,v1,v2,v3) -> (v0,-v2,-v1,v3)`. Then dim W_B,dim W_C are at most 7.
* Both mixed matrices are invertible. Then dim W_B=dim W_C=1.

In particular the first-rank sum is at most **14** when both mixed
projections are nonzero. This improves the earlier necessary bound 16
in the mixed-pencil note. Exact compatible 7-by-7 first spaces attain
14 at the level of the first-space equations. They do not give a matrix
target, and the target's exponent remains unchanged.

## 1. The pair equation, including arbitrary boundary graphs

Adopt the canonical extension spaces from the first-extension package
and H_actual=0 from the concurrent no-second-growth theorem. The
effective extensions split as boundary dimension 12 plus mixed dimension 4.
Write H for the source tensor restricted to its 100-dimensional leading
first kernel K and these effective factors.

The boundary-by-boundary block is zero. The two mixed-boundary blocks
have disjoint twelve-dimensional coordinate supports L,M on K. In the
fixed mixed basis use

    X(v)=[[v3,v1],[v2,v0]].

Each block is a six-fold copy of this matrix action, after fixed
invertible coordinate changes. The maintained verifier reconstructs the
blocks and checks all 32 matrix-unit multiplication identities. This
also rechecks the coordinate convention for both sides of the adopted
mixed-block theorem.

Let u,v be nonzero mixed components of rows in W_B,W_C. Their boundary
components may be arbitrary and need not define direct-sum subspaces.
Nevertheless H_actual=0 necessarily implies

    H(u,v) belongs to H(D_B,v)+H(u,D_C),              (1)

where D_B,D_C denote the effective boundary factors. This is because
the only other terms in the product of two graph lifts are exactly the
two terms on the right; the boundary-by-boundary term vanishes.

There is a source coordinate c=e_(0,0,6), outside L and M, on which (1)
forces

    h_c(u,v)=u0*v3+u1*v1+u2*v2+u3*v0=0.             (2)

Write F_L(v) for the 12-by-12 matrix action on L, normalized by its
value at v=(1,0,0,1), and F_M(u) for the action on M. For rank-one v,
the adjugate identity gives a necessary condition

    ((v0+v3)I-F_L(v)) H(u,v)|_L = 0.                (3)

For rank-one u, the corresponding necessary condition is

    ((u0+u3)I-F_M(u)) H(u,v)|_M = 0.                (4)

The representation identities justify these adjugate formulas, including
rank-one nilpotent matrices. The reasoning uses image membership, not
an inverse of the singular mixed matrix.

## 2. A rank-one component has a unique partner line

Suppose v is nonzero and rank one. We prove that (1) forces

    u proportional to J(v):=(v0,-v2,-v1,v3).          (5)

First take v3 nonzero. By scaling, write v=(a*b,b,a,1), using det X(v)=0.
Two exact source-coefficient consequences of (2)-(3) are

    u2+b*u3=0,    u0+b*u1=0.

They hold uniformly for all a,b, including zero. Thus write

    u=(-b*x,x,-b*y,y).

This already has det X(u)=0. We may therefore apply (4). Two of its
exact coefficients give

    x*(x+a*y)=0,    y*(x+a*y)=0.

Since u is nonzero, x and y are not both zero; hence x=-a*y. Substituting
gives u=y*(a*b,-a,-b,1)=y*J(v), proving (5) on this entire chart.

The source automorphism (i,j,z)->(3-i,3-j,6-z) preserves the leading
flag and reverses the four mixed coordinates. It commutes with J, so
the chart v0 nonzero follows from the preceding one. If v0=v3=0,
rank one implies v1*v2=0, leaving the two coordinate points e1,e2.
For v=e1, (2)-(3) give u1=u3=0. Write u=(x,0,y,0); a coefficient of
(4) is x^2, so x=0 and u is proportional to e2, as required by (5).
Reversal covers v=e2. These charts exhaust all nonzero complex
rank-one v. The coefficient identities and reversal are replayed
exactly by `verify.py`, rather than inferred from samples.

Interchanging output legs and transposing both short indices is also
a source automorphism, preserving the mixed coordinate ordering. Hence
the same partner statement holds with u and v exchanged. Equivalently,
J is an involution.

## 3. The complete mixed projections are one-dimensional

Let U_B,U_C be the nonzero mixed projections of W_B,W_C. Every pair
u in U_B,v in U_C satisfies the necessary graph equation (1), regardless
of the choice of lifts.

Every complex linear subspace of Mat2 of dimension at least two contains
a nonzero rank-one matrix. Indeed restrict the homogeneous determinant
to a projective line: either it vanishes identically or its degree-two
homogeneous polynomial has a complex zero.

If U_C had dimension at least two, choose a rank-one nonzero v in it.
Equation (5) would force U_B to be the rank-one line spanned by J(v).
Applying the partner statement in reverse to that line would force
U_C to be the line spanned by v, a contradiction. The same argument
excludes dim U_B>=2. Thus both are lines. If one line has rank one,
(5) forces the other to have rank one; otherwise both are invertible.

The pure-boundary part of W_B must annihilate the mixed line on C.
The adopted block formula gives this annihilator dimension six in
the rank-one case, and zero in the invertible case. The same holds
on the other side. Adding the one mixed dimension gives the claimed
bounds 7,7 or exactly 1,1. Arbitrary graph lifts are included throughout.

## 4. Exact compatible controls and the next gap

`seven-seven-seed.json` gives full six-dimensional pure-boundary
annihilators and corrected mixed partner lifts, with both effective
dimensions seven. `invertible-lines-seed.json` supplies a distinct
compatible pair of invertible mixed lines. The verifier checks their
quotient ranks, mixed projections, mixed matrix ranks, and all source
coefficients of H on the first kernel.

Set P(t)=P0+tP1 and Q(t)=Q0+tQ1 using either seed, with zero leading-row
derivatives. All three coefficients satisfy pi_K(1,P(t),Q(t))T=0
exactly. This is a polynomial identity for every t, not merely a sampled
or truncated numerical fit. The first flattening has generic rank twelve,
since only the twelve leading first coordinates remain and the leading
rank is twelve. It cannot contain the 100-dimensional target slice space.

The normal equations for the displayed 7-by-7 control have only the four
common-plane dimensions; the invertible-line control leaves 72 normal
directions. These exact dimensions guide the next lifting investigation.
They do not assert that all 72 directions admit complete second or later
coefficients. The open construction question is whether a smaller or
delayed first space, particularly the invertible-line stratum, can escape
the known boundary traps and produce the required target.

## Attribution and scope

The source, extension decomposition and normal equations come from the
earlier canonical and moving-boundary packages. The concurrent second-jet
work supplies H_actual=0 and the full mixed-boundary matrix blocks.
The mixed-pencil package supplied the earlier rank-sum bound 16 for the
case treated here. The new contribution is the all-parameter partner
identity with boundary graphs allowed, its line classification, and
the exact compatible controls. This is AI-derived written research with
no independent review, formalization, or exponent improvement.
