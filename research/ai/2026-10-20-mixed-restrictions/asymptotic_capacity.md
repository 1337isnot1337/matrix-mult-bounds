# A quantitative overhead barrier for coordinate inputs

AI-derived written proof, 2026-10-20. Unreviewed and not formalized. This
excludes an enlarged construction ansatz, not the general tensor-degeneration
premise or any matrix exponent. The target and the fixed-shared catalecticant
method come from the concurrent Koszul worker (`6bdab15`); the repetition
argument and its quantitative combination here are local derived work.

## Statement

Consider unbounded m and N=m(m+1)/2. For arbitrary positive integers k_m,
suppose C(A_m,B_m) degenerates to T_(m,k_m)=T_m tensor B_X(k_m)
by coordinate injections with arbitrary nonzero constant scalar coefficients
on both inputs, an arbitrary
constant output matrix, and diagonal integer weights on target coordinates.
Assume m<=A_m and limsup A_m/m<=5/4. Then

    liminf B_m/(k_m N) >= kappa = 3/2-sqrt(3)/4
                         = 1.0669872981... .            (1)

This allows arbitrary input-coordinate permutations, unused source input
coordinates, and output-coordinate collisions. In particular it includes
A=m+1. It excludes a construction within this class at the concurrent
criterion rho_c=9/(7*cuberoot(2))=1.0204721048.... General constant input
mixing, coefficient cancellation between several source pairs, and general
Laurent matrices are not covered.

## 1. A long arithmetic run

Use the active output sets S_(u,c) and the disjointness proof in
[collision_capacity.md](collision_capacity.md). They apply also to input
injections. The excess satisfies

    E=sum_(copy,u,c)(|S_(copy,u,c)|-1) <= A+B-1-kN.       (2)

Write d_p=x_(p+1)-x_p, a word of length n=m-1, and let L be the length of its
longest constant run. Each of the k copies has repetition lower bound R(d),
so E>=kR(d).
For a window length l>L, no window is constant. Two identical such windows
cannot start at consecutive positions, since that would make their letters
all equal. Among v=n-l+1 starts, any one window therefore occurs at most
ceil(v/2) times. Summing their deficits gives

    E/k >= sum_(v=1)^(n-L) floor(v/2)
        = floor((n-L)^2/4).                              (3)

Consequently x has an arithmetic run of length ell=L+1 with

    ell > m-2sqrt(E/k+1).                                (4)

Suppose for contradiction that a subsequence has B/(kN)<=rho for some
1<=rho<kappa. Equations (2)-(4) and A=O(m) imply

    liminf ell/m >= s=1-sqrt(2(rho-1)).                  (5)

Here 2s>3-sqrt(3)>5/4. All x indices lie in [0,A-1]. An arithmetic run
with integer step of absolute value at least two would have
2(ell-1)<=A-1, contradicting (5) and limsup A/m<=5/4. Its step is nonzero
by injection. Thus, eventually, that run has step +1 or -1.

## 2. A projected catalecticant bound

Project the target shared leg to this consecutive target-degree interval
p0,...,p0+ell-1. The corresponding source X indices are also consecutive,
possibly reversed. After an output shift/reflection, the source is
C(ell,B), embedded in the larger output space.

The target's wanted coefficients all have weight zero. Its u=2 sector gives

    wX(c+1)-wX(c)=wY(0,1)-wY(1,0)

for every 0<=c<m-1. Thus wX is an arithmetic progression. On the projected
leg its diagonal action is a polynomial-variable scaling, compatible with
the catalecticant. Write c_p for the nonzero constant scalar of that selected
first-input coordinate. Apply diag(c_p^(-1)) to the projected tensor family;
the first-input coefficients become one, and the limiting target is rescaled
on that leg. These constant diagonal maps commute with its parameter weights.

Put h=ell-1-q and apply

    X_(p0+r+s) -> U_r tensor V_s, 0<=r<=q, 0<=s<=h.

The concurrent source argument gives flattening rank B+q. Arbitrary maps
and weights on the other two legs cannot increase this rank, including
in the parameter limit. For target sector u, v=m+1-u, its matrix entry is
one when p0+r+s=a+c. Rows and columns group into disjoint all-ones blocks
indexed by r-a=c-s-p0. Its rank is therefore

    |[-u+1,q] intersect [-h-p0,v-1-p0]|.

For the unrescaled target, summing over all sectors in one copy gives the
exact rank

    (ell+p0)(m-p0) - [h(h+1)+q(q+1)]/2.                 (6)

The constant diagonal target rescaling replaces the entries in every
nonempty all-ones block by nonzero numbers. Each such block still has rank
at least one, and different groups have disjoint row and column spaces.
Thus (6) remains a lower bound with arbitrary nonzero first-input scalars.
This is the same nonzero-group argument used for leading-coefficient
rescalings in concurrent `71c821a`. Second-input scalars can be absorbed
into its arbitrary other-leg map.

One can also obtain (6) by summing the allowed u for each value r-a.
Since 0<=p0<=m-ell, the first term is at least ell*m. Choose
q=floor((ell-1)/2). Then the bracket divided by two is floor(ell^2/4), so

    B >= k*(ell*m-floor(ell^2/4))-floor((ell-1)/2).       (7)

Equation (6) is checked against independent explicit integer matrices in
`quantitative_capacity.py`. The universal argument is the block calculation.

## 3. Solving the contradiction

The k copies have disjoint matrix row and column spaces, so their ranks
add in (7). Divide (7) by kN. The function 2z-z^2/2 increases for 0<=z<=1.
Using (5) and B/(kN)<=rho gives

    rho >= 2s-s^2/2
          = 5/2-rho-sqrt(2(rho-1)),

or 2rho+sqrt(2rho-2)>=5/2. Its left side is strictly increasing for rho>=1;
equality occurs at rho=kappa. This contradicts rho<kappa and proves (1).

The comparison with the required overhead can be certified without decimals:
sqrt(3)<26/15 since 675<676, so kappa>16/15. Also

    (9*15)^3 < 2*(7*16)^3,

so rho_c<16/15. Thus the two admissible overhead ranges are disjoint.

If an enlarged-short-input variant seeks endpoint cost
rho*sigma^(1/3)<rho_c with A/m approaching sigma>=1, then rho>=1 forces
sigma<rho_c^3=729/686<5/4. It also forces rho<rho_c. Consequently (1)
excludes that variant in this same coordinate-input class.

## Boundaries

No unrestricted change of basis has been eliminated. With general constant
input matrices a target input pair may receive several source contributions;
they can cancel, invalidating the disjoint-active-set step. Parameter-dependent
nondiagonal input maps are also outside this proof. Closing this ansatz does not disprove the conditional
construction or improve omega.

The concurrent result `8e0a766` excludes arbitrary shared maps with regular
invertible limit, while allowing arbitrary other-leg Laurent maps. That is
complementary: the shared diagonal weights here can be singular, but the
constant input maps are restricted to coordinate injections. Neither result
closes the genuinely singular, nondiagonal shared-map problem.
