# Ordinary restrictions from an EPR factor and one convolution

October 21, 2026. AI-derived written argument and exact finite replay, unreviewed.

This note concerns **ordinary linear restrictions**, not singular tensor degenerations. It does not prove an exponent improvement. The latter distinction matters: several smaller targets remain compatible with the arbitrary-degeneration tests but fail the ordinary tests below.

## 1. Polynomial model and slice bound

Let E(k;c,d)=Q(k,1;c,d)=EPR_k tensor C(c,d), and put h=c+d-1. Its dimensions are (kc,h,kd). Write its contraction on the two input legs as

    (f_1,...,f_k),(g_1,...,g_k) -> sum_a f_a(z)g_a(z),

where the f_a and g_a are homogeneous binary forms of degrees c-1 and d-1. The output is a binary form of degree h-1. This is exactly the coefficient tensor in the main note.

If the nonzero tuple f has homogeneous greatest common divisor of degree e, then its slice rank is at least

    min(2d,h-e).                                           (1)

Indeed, divide the common gcd from all f_a. Two generic linear combinations of the residual forms have no common zero on the projective line. If their degree is D=c-1-e, their degree-(d-1) multiple spaces each have dimension d and intersect in dimension max(d-D,0). Their sum has dimension min(2d,d+D), proving (1). The case D=0 has rank d directly. An arbitrary field may first be extended to its algebraic closure; coefficient ranks do not change.

In particular, every nonzero first slice has rank at least d. Suppose there is an ordinary restriction

    E(k;c,d) -> M(l,m,r).

Concision of the target makes all three side maps have full target rank. A rank-one first-leg functional of M(l,m,r) gives a matrix slice of rank m. Its lift has source rank at most

    R_X = m + (h-lm) + (kd-mr).                            (2)

The two extra summands are exactly the dimensions removed by the other two quotient maps. Thus

    m(l+r-1) <= h+(k-1)d                                  (3)

is necessary. Applying the same argument to the other input gives

    l(m+r-1) <= h+(k-1)c.                                 (4)

If R_X<2d, (1) also forces the lifted tuple's gcd degree to satisfy

    e >= h-R_X = m(l+r-1)-kd.                              (5)

The analogous statement on the third leg uses c and d interchanged and l and m interchanged. The program does not claim a gcd bound from (1) when R_X>=2d.

## 2. Which parameter can carry the common factor?

The first input map is an injection

    L: K^l tensor K^r -> K^k tensor Sym^(c-1)(K^2).

For a decomposable input u tensor v, its k form coordinates F_a(u,v,z) have parameter bidegree (1,1). Suppose their generic gcd has z-degree e' at least the lower bound e from (5). Gauss's lemma gives a common polynomial factor over K[u,v,z]. Since the F_a are multihomogeneous, this factor can be chosen multihomogeneous. Its parameter bidegree is one of (0,0), (1,0), (0,1), (1,1).

The following are necessary conditions for each case. They are not sufficient construction criteria.

| Common factor's parameters | Name in the program | Necessary conditions |
| --- | --- | --- |
| Neither u nor v | fixed | lr <= k(c-e) |
| Both u and v | full_bilinear | lr <= c |
| u only | outer | max(e,l-1) <= e' <= c-ceil(r/k) |
| v only | shared | max(e,r-1) <= e' <= min(c-ceil(l/k),h-lm) |

For a fixed common factor the whole image lies in k copies of a polynomial space of dimension at most c-e. For a factor of full parameter bidegree, the residual tuple is independent of u,v, so the whole image has dimension at most e'+1<=c.

In the outer case write F_a=H(u,z)G_a(v,z). Injectivity forces u->H to be injective, so e'+1>=l. It also forces the residual v map to be injective into k(c-e') coefficients, so r<=k(c-e'). The shared case is symmetric at this stage. Its further condition e'<=h-lm follows by fixing a nonzero shared index: every output form then has the same factor of degree e', and its image must still span the lm-dimensional target high leg.

Consequently, if all four types fail their necessary dimension conditions, no ordinary restriction exists. Every polynomial-space dimension used here includes homogeneous degree drops at infinity; there is no affine-degree exception.

## 3. Product-space obstruction after the factor split

Assume that on both inputs the only surviving factor types are outer or shared, that

    2lm>h,  r>k.                                         (6)

Then no ordinary restriction exists.

Let V be the projection from the h-dimensional polynomial output space onto the lm-dimensional target high leg. Thus dim ker V=h-lm<lm. Use standard target basis indices i=1,...,l, j=1,...,m and s=1,...,r. A correct restriction must satisfy

    V(sum_a F_(i,s,a) G_(j,t,a)) = delta_(s,t) E_(i,j).    (7)

### Both factors are outer

Write F_(i,s,a)=H_i A_(s,a) and G_(j,t,a)=H'_j B_(t,a), and set

    W=span{H_i H'_j},  q_(s,t)=sum_a A_(s,a)B_(t,a).

For a fixed diagonal s=t, equation (7) shows that W has dimension exactly lm and q_(s,s) is nonzero. For s!=t, a nonzero q_(s,t) would multiply W injectively into ker V. That is impossible because its dimension would be lm>dim ker V. Hence all off-diagonal q_(s,t) vanish.

The same argument applied to q_(s,s)-q_(t,t) shows that all diagonal polynomials coincide. Over K(z), the matrix Q=(q_(s,t)) is therefore a nonzero scalar multiple of I_r. But Q is the product of an r-by-k and k-by-r matrix, so its rank is at most k, contradicting r>k.

### At least one factor is shared

For example, write F_(i,s,a)=H_s A_(i,a). If the other factor is outer, fix t and put

    W_t=span{H'_j sum_a A_(i,a)B_(t,a)}.

The diagonal case s=t in (7) makes dim W_t=lm. For any s!=t, multiplication by the nonzero H_s is injective and takes the same W_t into ker V, a contradiction. If both factors are shared, the identical argument uses the common space spanned by sum_a A_(i,a)B_(j,a). The remaining mixed orientation is symmetric. This proves the obstruction under (6).

The argument depends on polynomial factorization of **fixed linear maps**. It has not been extended to singular degenerations; the note makes no such claim.

## 4. Exact finite coverage

The preserved program enumerates

    k,c,d>=2, c<=d, max(kc,c+d-1,kd)<=100.

There are 2867 source triples. Every positive matrix shape satisfying all three dimension bounds is considered. The improvement test uses only the three finite profile costs already recorded in the main package. Since P(k,1)=k, a target of volume V=lmr would require kP(c,d)>=V. For a recorded cost sP(c,d)<=C^(1/t), a strict endpoint improvement is certified by the integer comparison

    (sV)^3 > k^3 C^4.

This is a candidate-selection inequality, not an established improvement.

There are 10418 improving shapes in this stated finite search. Their exclusion counts are:

| First recorded obstruction | Target shapes |
| --- | ---: |
| One of the two input-leg universal Koszul upper bounds | 9756 |
| Minimum-slice inequality | 386 |
| Common-factor parameter dimensions | 171 |
| Product-space obstruction above | 105 |
| Remaining ordinary restrictions | 0 |

For each fixed source and outer shape (l,r), the program tests the smallest improving middle size m. An exclusion of that shape excludes every larger middle size by further ordinary restriction. Each record states the whole covered interval and its exact witness. This is why the number of records can be smaller than the number of covered target shapes.

The Koszul records individually exclude arbitrary degeneration. The complete finite conclusion is only about ordinary restriction, because the other witnesses use stronger hypotheses.

```sh
python research/ai/2026-10-20-unequal-paired/edge_ordinary.py --output /tmp/edge-ordinary-frontier.json
python research/ai/2026-10-20-unequal-paired/edge_ordinary.py --mode controls --output /tmp/edge-positive-controls.json
python -m unittest discover -s tests -p test_unequal_paired.py -v
```

The independent positive controls expand the integer coefficients of the actual restriction

    EPR_k tensor C((l-1)m+1,m) -> M(l,m,k).

It retains first-input polynomial indices i*m and all second-input indices j, so their sums are the distinct output indices i*m+j. The EPR index is the shared matrix index. The archive checks all 27 choices l,m,k in {2,3,4}, then verifies that neither the Koszul nor the ordinary screens reject these actual maps. This checks the tensor orientation using coefficients rather than only agreement between two formulas.

The cohomological rank upper bound and matrix Euler formula are the written arguments in this repository. The common-factor suggestion came from the coordinating agent's polynomial-gcd lane; this note supplies the parameter split, the output-kernel argument, and the finite replay. No independent mathematical review or formalization is claimed.
