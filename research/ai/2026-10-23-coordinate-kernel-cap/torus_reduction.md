# Transfer the coordinate certificate to arbitrary complex kernels

October 23, 2026. Owner-directed Codex continuation. Written and
unreviewed. The torus specialization argument is elementary and no
historical priority, independent review or exponent gain is claimed.

## 1. A general compression principle

Let T be in A tensor B tensor C over C. Suppose diagonal one-parameter
groups D_A(s),D_B(s),D_C(s), with integer weights, preserve T:

    (D_A(s) tensor D_B(s) tensor D_C(s)) T = T.

Assume all weights on B are distinct, and all weights on C are distinct.
For arbitrary subspaces K_B,K_C, let rho(K_B,K_C) be the first flattening
rank of T projected to A tensor (B/K_B) tensor (C/K_C). There exist
coordinate subspaces K_B^0,K_C^0 of the same respective dimensions with

    rho(K_B^0,K_C^0) <= rho(K_B,K_C).                    (1)

Thus an upper bound for the compression-kernel dimension proved for
every coordinate pair transfers to every complex pair of those kernel
dimensions. The direction of (1) is essential.

Proof. Move the kernels by D_B(s),D_C(s). For s nonzero, source symmetry
identifies the projected tensor with the original projected tensor after
the invertible first-leg action D_A(s). Thus rho is unchanged.

Take the limits of these two moving subspaces as s tends to zero. These
limits exist with the same dimensions: form their maximal minors,
which are Laurent polynomials, remove the common smallest power and
take the first nonzero Plucker coordinates. Equivalently, use a regular
saturated basis over C[[s]] as in the pinned lattice argument. For every
constant z nonzero, D_B(z) sends the limiting B-plane to itself, because
it sends the family at s to the same family at zs. The same holds on C.
An invariant subspace for a diagonal group with distinct weights is a
coordinate subspace, by its one-dimensional weight-space decomposition.
The two limits are therefore K_B^0,K_C^0 as stated.

Near each limiting subspace choose a nonzero constant maximal minor.
The associated quotient chart supplies regular quotient matrices whose
constant maps have exactly those limiting kernels and the same ranks.
All generic projected first-flattening minors of size rho+1 vanish,
and their regular specializations still vanish. Hence limiting rank
cannot exceed rho, proving (1). This argument uses no target tensor,
does not replace a fixed-dimension kernel by a smaller matrix limit,
and allows the two kernel limits to be taken simultaneously.

## 2. The literal A4 source has the required simple weights

With canonical source coordinates A_(i,k,z), B_(j,p,L), C_(H,q,r), use

    w_A=i-16k+256z,
    w_B=j+16p-256L,
    w_C=-H+16q+256r.

Each of the three112-element coordinate sets has distinct weights.
For every original source coefficient, k=p+q, L=r+z and H=i+j, so

    w_A+w_B+w_C=0.

This is a literal diagonal source automorphism. The verifier checks
distinctness and all4096 coefficient identities. Every pair of legs
therefore satisfies the simple-weight hypothesis, after the usual
canonical identification of the cyclic source legs.

## 3. A universal low-defect compression cap

Take any two complex constant maps with source kernel dimensions d,e
satisfying

    d+e<=24,   d<24,   e<24.                            (2)

The coordinate proof and its8008-subset certificate give kernel dimension
at most9 for every coordinate pair with these dimensions. Indeed total
defect is below32, so a nonzero coordinate hidden space uses one coherent
endpoint; ten hidden cells would require25 deletions, or24 on one side.
Neither possibility meets (2). By (1), every complex pair also hides
at most9 source first coordinates in the linear-space sense. Thus its
projected first rank is at least103.

The constant maps' kernels need not be coordinate. We use coordinate
limits only to bound the compression rank; no target construction is
asserted to survive that specialization. The target is tested separately
by the existing saturated support condition on the original maps.

## 4. The complete high-total-rank A4 pair frontier

All sixteen mixed pairs left by the prior dense regular-leg screen have
defects satisfying (2). Their target support ceiling is102 or101, below
the universal lower bound103. They are therefore excluded for arbitrary
complex limiting kernels, with arbitrary higher regular jets and an
arbitrary Laurent third map. Combining with the prior dense long/long
result gives:

    Any two regular target-leg maps have rank sum<=192. (3)

There is a presentation-independent leading-rank formulation. For any
Laurent presentation let r_A,r_B,r_C be the ranks of each map's first
nonzero coefficient after individual scalar balancing. Any selected two
maps can be balanced to be regular, compensating their two scalar powers
on the third map. The full tensor identity is unchanged. Apply (3) to
each selected pair to obtain

    r_A+r_B<=192,  r_A+r_C<=192,  r_B+r_C<=192.          (4)

Here r_A<=100 and r_B,r_C<=110 in the selected target labeling. In
particular their total is at most288. If r_A=100, both balanced long
leading ranks are at most92. These are necessary leading-rank conditions,
not a construction or a proof that the remaining rank triples occur.

## 5. Evidence and limits

The coordinate graph certificate remains a finite exhaustive result.
The arbitrary-kernel extension is the written specialization proof
above, supported by the exact source weight check. A small noncoordinate
quotient control exhibits the required rank-drop direction under an
explicit source-torus limit; it does not formalize all Grassmannians.
The prior source, low-rank locus, saturation theorem and dense regular-leg
screen keep their byte pins and credit. Lower balanced-rank triples and
the target construction remain open to this argument. The exponent
remains9/4; there is no independent review or formalization.
