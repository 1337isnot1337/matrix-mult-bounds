# The remaining source-rank gap is a first-cohomology group

Written and unreviewed, October 23, 2026. Adopt the notation and bundle
map of the explicitly pinned PR169 proof: a>=2, D=a-1, h=2a-1,
N=ah, Q=O(1)^(Dh), and

    phi_p: F_p = wedge^p B tensor F^a tensor O(D)
                -> G_p = wedge^(p+1) B tensor F^a tensor O(2D).

Its global section map is the literal paired-source K_p with short
input. Let R_p(D), I_p and T_p be its kernel, image and cokernel bundles.
The local splitting by the rank-h subbundle proves these are bundles
of constant rank; no global splitting is assumed.

The source rank satisfies the exact identity

    rank K_p = N*binom(N,p+1) - h^0(T_p) - h^1(R_p(D)).       (1)

Indeed H^1(F_p)=0. The explicit line-bundle filtration of R_p(D)
gives H^2(R_p(D))=0, so the exact sequence with F_p gives H^1(I_p)=0.
The other exact sequence then gives a surjection H^0(G_p)->H^0(T_p).
Its kernel is H^0(I_p), whose quotient by the image of H^0(F_p) is
H^1(R_p(D)). This proves (1).

## An explicit cokernel Euler bound

As in PR169, let J_k be the h-dimensional-first-leg symmetric Hankel
map. Its cokernel is nonzero only at -1<=k<=a-2, with dimension

    c_k = a*(binom(h,k+1)-binom(h,k)).

At k=-1 the domain is zero and the output dimension is a. The
S-degree filtration on T_p has line-bundle quotients of degree

    d_k = p+D-a*k

with multiplicity c_k*binom(Dh,p-k). The output S-degree is k+1:
its O(-D(k+1)) factor, the O(2D) twist and the Q exterior degree
p-k give exactly d_k. Thus

    E(a,p) := chi(T_p)
      = sum_(k=-1)^(a-2) c_k*binom(Dh,p-k)*(p+D-a*k+1).

Since h^0(T_p)>=max(E(a,p),0), (1) proves the all-field upper bound

    rank K_p <= N*binom(N,p+1)-max(E(a,p),0).                (2)

Intersect it with the domain dimension and the independent fixed-short-
input upper bound. This does not assume that all extension maps have
maximal rank or that a finite modular rank equals the complex rank.

## The exact missing term in the intermediate interval

For p>=a(a-1)+1, every nonzero d_k is positive: its smallest possible
value, at k=a-2, is at least 2a. Therefore H^1(T_p)=0 and h^0(T_p)=E(a,p).
Throughout the intermediate interval left open by PR169,

    rank K_p = N*binom(N,p+1)-E(a,p)-h^1(R_p(D)).           (3)

The remaining unknown is the actual H^1 of the kernel bundle, including
its extension maps. For a target rank r_target, exclusion by this
Koszul map is equivalent to

    h^1(R_p(D)) > N*binom(N,p+1)-E(a,p)-r_target.

The reverse weak inequality certifies that this particular map cannot
exclude that target. Neither inequality is proved here for every
intermediate comparison of the saved 28-target frontier.

Finite literal coefficient ranks modulo2 match (2) at (a,p)=(2,3),
(3,10),(3,11), proving exact complex ranks 70,18819,6660 at those
three cases. In general (2) is only an upper bound. At a3,p7 the
cokernel bound capped by the domain is 57915, while the fixed-input
kernels already prove a strictly smaller upper bound 57870.

The all-size statement is written, unreviewed and not formalized. It
uses PR169's explicit filtration and the same Stacks line-bundle facts.
The exact cohomology sequence, Euler expression and finite controls are
owner-directed Codex continuation. No historical priority, independent
review, matrix target or exponent improvement is claimed.
