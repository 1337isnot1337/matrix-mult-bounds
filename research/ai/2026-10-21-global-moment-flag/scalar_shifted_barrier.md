# A 3/2 cost barrier for scalar shifted blocks

Date: 2026-10-21.

This is a scoped obstruction, not an exponent improvement. It applies to
the exact scalar shifted-block ansatz in C(m+1,B), even when the matched
convolution sectors have independent invertible shared identifications.
It does not apply to free input/output flags or arbitrary Laurent maps.

## Hypotheses

Work over any field, using coefficient-dual (equivalently divided-power) contraction throughout; ordinary derivatives with factorial coefficients are not intended. Let N=m(m+1)/2, B=N+delta, and m>=3. For p=0,...,m-1
let g_p be a homogeneous binary form of degree B-p-1. Its input block is

    g_p S_p,

where S_d is the space of binary forms of degree d. For q=0,...,m-1 let
S_q^vee be an inverse form of degree B+m+q-1; output rows are its consecutive
shifts. Assume the full negative shifted moments vanish:

    g_p contraction S_q^vee = 0
    whenever p+q<m-1 and p+q>0.

For each r, the matched inverse form

    nu_r = g_r contraction S_(m-1-r)^vee

has degree 2m-1 and admits an invertible m-by-m shared Hankel matrix.
In particular its catalecticant on S_(m-1) is injective. The shared
identification may differ with r. The exceptional p=q=0 negative
condition is deliberately not assumed.

Then, for every integer 0<=k<=m-2,

    delta >= k(m-2-k)-2.

Consequently,

    B >= N + floor((m-2)^2/4)-2,
    liminf B/N >= 3/2

along any unbounded family satisfying these hypotheses.

## Proof

Fix k. Consider the relation space

    R_k = { (a_0,...,a_(m-1)) :
              a_p in S_(p+k+1), sum_p a_p g_p = 0 }.

All products have degree B+k. Dimension counting gives

    dim R_k >= sum_(p=0)^(m-1)(p+k+2) - (B+k+1)
             = (m-1)(k+1)-delta.                         (1)

Filter R_k by the largest index r for which a_r can be nonzero.
For r<=m-2, contract the relation with S_(m-1-r)^vee. Every earlier
g_p contraction vanishes, because p+(m-1-r)<m-1 and this sum is positive.
Therefore the last-coefficient map injects the r-th filtered quotient
into

    Ann(nu_r)_(r+k+1).                                  (2)

There is no p=q=0 exception in this step, because m-1-r>=1.

A binary inverse form of degree 2m-1 whose degree-(m-1) catalecticant is
injective has no annihilator in any smaller degree. Transposing
catalecticants then gives, for 0<=d<=2m-1,

    dim Ann(nu_r)_d = max(2d-2m+1,0).                    (3)

For completeness, multiplication by a nonzero polynomial injects each
lower degree into degree m-1, so a lower annihilator would contradict
middle injectivity. The catalecticant in degree d is transpose to the
one in degree 2m-1-d. These two facts prove (3) without a
complete-intersection classification.

Summing (3) for r=0,...,m-2 with d=r+k+1 gives

    sum_r max(2r+2k-2m+3,0) = 1+3+...+(2k-1) = k^2.    (4)

For the last index r=m-1 ignore all equations and bound the quotient
by the dimension of a_(m-1), namely m+k+1. Thus

    dim R_k <= k^2+m+k+1.                               (5)

Combining (1) and (5) proves delta>=k(m-2-k)-2. Maximizing the integer
quadratic proves the stated bound.

## Controls and limits

The companion verifier checks 828 literal catalecticant ranks over F_2
and F_101 and 189 exact odd-sum identities. The forms used for the
rank controls have one nonzero coefficient at index m-1, so the
middle catalecticants have integral unit antidiagonals.

The obstruction does not require canonical shared alignment. It does
require scalar polynomial input factors and consecutive shifted output
moments, including all negative shifted moments stated above. An
arbitrary completion with independently chosen output rows need not
satisfy those full inverse-form identities. Free-flag constructions
therefore remain outside the theorem.

Finite examples at m=4,5,6,7 are consistent with this asymptotic
obstruction. The theorem rules out using this ansatz alone to obtain
B=N+O(m) for unbounded m.

