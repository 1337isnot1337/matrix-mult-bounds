# Exact ranks for biforms with one polynomial top coefficient

October 23, 2026. Owner-directed AI-assisted research. Claim AI-TOP-COEFFICIENT-BIFORM-RANK-001 is proof-written-unreviewed: this file provides a written proof and finite exact controls, not an independent mathematical review, a tensor target, or an exponent improvement.

## Statement and coefficient convention

Let K be any field, a >= 2, b >= 2, 1 <= e < b, and m = a+b-1. Consider

    f(x,z) = c_0 + c_1*z + ... + c_(e-1)*z^(e-1) + w(x)*z^e,

where c_s belongs to K, c_0 is nonzero, and w(x) is a nonzero polynomial of degree d < a. The coefficients below the highest z-power are constants; only the highest coefficient may depend on x.

Define the literal cyclic-source coefficient matrix with rows (j,L), 0<=j<b and 0<=L<m; columns (H,r), 0<=H<m and 0<=r<a; and entry

    R[(j,L),(H,r)] = coefficient of x^(H-j)*z^(L-r) in f.

Out-of-range coefficients are zero. This is the full, untruncated source matrix used in the main-branch slice-rank discussion and PR #209.

**Theorem.** Put q_j = floor((a+j)/e) for 0<=j<e. Then, over every field and every permitted choice of coefficients,

    rank_K R_(a,b)(f) = a*b + sum_(j=0)^(e-1) min(b, d*q_j).       (1)

For d=0 the formula gives rank ab. Since sum_j q_j=a, when b>=d*ceil(a/e) the rank is exactly ab+ad. All statements hold without characteristic exceptions.

For the genuinely three-term family f=1+z+(1+x^d)*z^2 with 1<=d<a and b>=3, (1) gives

    rank = ab + min(b, d*floor(a/2)) + min(b, d*ceil(a/2)).

For example, a=3,b=7,d=2 gives rank 27 and a=4,b=5,d=3 gives rank 30. These are neither binomial source slices nor diagonal polynomials f(xz). They do not construct compatible maps on three tensor legs.

## Proof over an arbitrary field

Only row groups L=0,...,a+e-1 can be nonzero, totaling (a+e)b active rows. Describe a linear dependence among those rows by polynomials

    lambda_L(x) = sum_(j=0)^(b-1) lambda_(j,L)*x^j,
    0<=L<=a+e-1,

all of degree <b. Contracting against a column (H,r) reads the coefficient of x^H in

    c_0*lambda_r + sum_(s=1)^(e-1) c_s*lambda_(r+s)
                 + w(x)*lambda_(r+e).                           (2)

Each expression in (2) has degree at most (a-1)+(b-1)=m-1. Because the literal matrix contains every H=0,...,m-1, the row dependence vanishes exactly when (2) vanishes as a complete polynomial identity for every r=0,...,a-1. In particular no highest-degree coefficient is dropped.

The nonzero constant c_0 makes this a polynomial recurrence that can be solved backwards:

    lambda_r = -(1/c_0)*(sum_(s=1)^(e-1) c_s*lambda_(r+s)
                                + w*lambda_(r+e)),              (3)

for r=a-1,...,0. Thus the e terminal polynomials lambda_a,...,lambda_(a+e-1) are freely chosen from K[x]. For j=0,...,e-1, define V_j by choosing terminal lambda_(a+j)=1 and all other terminal polynomials zero. These V_j form a free K[x]-basis of the complete polynomial solution module.

Assume d>0. Each entry V_j(i) expands as a sum of paths from index i to terminal index a+j: a step of size s<e contributes the constant factor -c_s/c_0, while a step of size e contributes the polynomial factor -w/c_0. There can be at most q_j=floor((a+j)/e) size-e steps. Consequently every coordinate of V_j has degree at most delta_j=d*q_j.

Write a+j=e*q_j+r_j with 0<=r_j<e. At coordinate i=r_j, the path with q_j size-e steps is the unique path attaining that number of polynomial steps: it consists entirely of size-e steps. Its leading coefficient is

    (-lc(w)/c_0)^(q_j),                                    (4)

which is nonzero. Every other path has fewer polynomial steps, so has degree strictly below delta_j. For every coordinate i>r_j, a path with q_j size-e steps would require a total step length at least e*q_j > a+j-i. Such a path cannot occur, so the degree-delta_j coefficient is zero. If q_j=0, the same statements hold because r_j=a+j is a free terminal coordinate, with V_j(r_j)=1 and V_j(i)=0 for all i>r_j.

The residues r_j form a permutation of 0,...,e-1. Restrict the leading coefficient vector of each V_j at degree delta_j to the first e row-group coordinates. After ordering the columns by r_j, these vectors form a triangular e-by-e matrix with nonzero diagonal (4), because the entries with i>r_j vanish. Therefore the degree-delta_j leading coefficient vectors of all V_j are linearly independent over K, even in positive characteristic.

For any polynomials P_j, not all zero, linear independence prevents cancellation at the largest weighted degree:

    deg(sum_j P_j*V_j) = max_(j:P_j != 0)(deg(P_j)+delta_j),  (5)

where degree of a polynomial vector means the maximum of its coordinate degrees. Thus all coordinates of the sum have degree <b if and only if each P_j separately satisfies deg(P_j)<b-delta_j. The active-row kernel therefore has dimension

    sum_(j=0)^(e-1) max(0,b-d*q_j).                        (6)

If d=0, all recurrence coefficients are constants and all V_j are constant vectors. Their terminal coordinates form the identity, so they remain independent and (5)-(6) hold with delta_j=0.

Subtracting (6) from the (a+e)b active rows gives

    (a+e)b - sum_j max(0,b-d*q_j)
    = ab + sum_j min(b,d*q_j),

proving (1). Write a=e*k+r, 0<=r<e. Exactly r of the q_j equal k+1 and the rest equal k; hence sum_j q_j=e*k+r=a. This proves the corollary. QED.

## Reproduction and scope

The standard-library verifier builds the entire bm-by-am source matrix and determines its rank by exact modular Gaussian elimination, without using the recurrence. Completed controls: 900 exhaustive GF(2) cases across 27 shapes; 1,836 exhaustive GF(3) cases; 216 fixed-seed GF(5), GF(7), GF(101) cases; and 420 degree witnesses. All 3,372 agree with (1). The independently implemented coefficient-lookup matrix and exact SymPy rational elimination agree in 24 QQ cases. These are same-session software controls, not independent mathematical review.

From the repository root:

    python -I research/ai/2026-10-23-top-coefficient-biforms/verify.py --receipt results/local/top-coefficient-biforms.json
    python -I research/ai/2026-10-23-top-coefficient-biforms/verify_charzero.py
    python -m unittest discover -s tests -p test_top_coefficient_biforms.py -v

The literal source indexing and preceding affine-z classification are credited to the pinned main source and PR #209. PR #171 covers binomials, #186 the general gap and another special family, and #207 the diagonal f(xz) Toeplitz family. No unmerged proof is imported. This theorem concerns one free polynomial coefficient; it does not claim a classification of arbitrary quadratic-in-z coefficients or a matrix multiplication exponent below 9/4.

The next open bottleneck is the two-nonconstant-coefficient polynomial recurrence for arbitrary u(x)+z*v(x)+z^2*w(x). With a nonconstant coefficient at lambda_r, the backwards solution (3) may cease to exist in K[x]; the minimal polynomial indices must then be determined. A three-leg tensor target, auxiliary costs, and a full asymptotic argument are also still missing.
