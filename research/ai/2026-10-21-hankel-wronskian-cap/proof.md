# A Wronskian proof of the bounded-Hankel-space cap

October21,2026. AI-assisted written proof, unreviewed. This is a uniform
characteristic-zero proof of a rank-space bound, not a matrix multiplication
construction or an improved exponent. No historical novelty, independent
mathematical review, or formalization is claimed.

**Theorem.** Let F be any field of characteristic zero. For positive a,b
and0<=r<min(a,b), put d=a+b-2. If L is a linear space of sequences
h=(h_0,...,h_d) whose a-by-b Hankel matrices

    H(h)_(i,j)=h_(i+j)

all have rank at most r, then dim L<=r. The bound is sharp.

The proof applies over C(x,z) and its algebraic closure. It does not require
an exhaustive coordinate-subspace certificate or a hypothesis about reduced
support. Both the strict rank bound r<min(a,b) and characteristic zero
are used. The r=0 case is immediate; assume r>=1 below.

## 1. Initial zero moments force a tail

Suppose h_0=...=h_(r-1)=0 and h is nonzero. Let k be its first nonzero
coordinate. If r<=k<=d-r, choose integers i_0,j_0 with

    0<=i_0<=a-r-1,  0<=j_0<=b-r-1,  i_0+j_0=k-r.

They exist because0<=k-r<=a+b-2r-2. One explicit choice is

    i_0=max(0,k-b+1),   j_0=k-r-i_0.

The consecutive(r+1)-by-(r+1) submatrix with those initial row and column
indices has entries h_(k-r+i+j). All entries with i+j<r vanish, and all
entries with i+j=r equal h_k. Its determinant is

    (-1)^(r(r+1)/2) * h_k^(r+1),

which is nonzero. This contradicts the rank bound. Therefore k>=d-r+1:

    h_0=...=h_(d-r)=0.                                     (1)

The allowable interval is nonempty because a,b>=r+1 imply d>=2r.

## 2. A binomial shear moves the high-order zero

For any lambda in F define the invertible upper-triangular moment change

    h'_k=sum_(j=k)^d binom(d-k,j-k) lambda^(j-k) h_j.

Let S_a have entry binom(a-1-p,i-p)*lambda^(i-p) for i>=p, and zero
otherwise; define S_b similarly. The binomial convolution identity gives

    H(h')=S_a H(h) S_b^T.                                  (2)

Indeed, the coefficient of h_l in entry(p,q) on the right is lambda to
power l-p-q times

    sum_(i+j=l) binom(a-1-p,i-p) binom(b-1-q,j-q)
      =binom(d-p-q,l-p-q).

Both triangular matrices have diagonal one, so this preserves rank for
every lambda. No classification of group representations is needed.

Associate to a moment sequence the polynomial

    f_h(t)=sum_k (-1)^k binom(d,k) h_k t^k.

This is a linear isomorphism from F^(d+1) to the polynomials of degree
at most d, since the binomial coefficients are nonzero in characteristic
zero. Expanding the preceding shear and using
binom(d,k)binom(d-k,j-k)=binom(d,j)binom(j,k) gives

    f_(h')(t)=f_h(t-lambda).                                (3)

Suppose dim L>=r+1 and choose a subspace L_0 of dimension exactly r+1.
For every lambda, r homogeneous linear conditions on the transformed
L_0, namely h'_0=...=h'_(r-1)=0, have a nonzero solution. Section1
forces h'_0=...=h'_(d-r)=0. Hence f_(h')(t) is divisible by t^(d-r+1).
Equation(3) shows that the corresponding nonzero f_h in f(L_0) has a
root of multiplicity at least d-r+1 at t=-lambda.

Thus **at every point of F, this fixed(r+1)-dimensional polynomial
space contains a nonzero polynomial vanishing to order at least r+1**,
because d>=2r. The next step rules this out.

## 3. A nonzero Wronskian supplies the contradiction

Choose a basis f_0(t),...,f_r(t) of f(L_0). These polynomials have
degree at most d and are linearly independent over F.
At every finite t_0 in F, the preceding conclusion gives a nontrivial
linear combination vanishing to order at least r+1 at t_0. Hence the
jet-evaluation matrix

    (f_i^(j)(t_0))_(0<=j,i<=r)

is singular. Its determinant, the Wronskian, vanishes at every t_0 in
the infinite field F, and is therefore the zero polynomial.

For completeness, this is impossible in characteristic zero. Change the
basis by Gaussian elimination so that its nonzero leading degrees are
distinct, n_0<...<n_r, with leading coefficients c_i. The Wronskian's
highest coefficient is

    product_i c_i * product_(i<j)(n_j-n_i),

at degree sum_i n_i-r(r+1)/2. Indeed its coefficient matrix consists of
the falling-factorial polynomials in the n_i, which are monic in their
successive degrees0,...,r; their determinant is the Vandermonde. The
coefficient is nonzero in characteristic zero. The exponent is nonnegative
because n_i>=i. This contradiction proves dim L<=r.

Sharpness is supplied by the r-dimensional space supported on h_0,...,
h_(r-1): every such Hankel matrix is supported in its first r rows and
columns and has rank at most r.

## 4. A uniform rational witness generator

The proof is constructive for a supplied rational basis of dimension r+1.
The Wronskian has degree at most D=(r+1)(d-r): after degree elimination,
the largest possible degree sum is d+(d-1)+...+(d-r). The determinant
of the first r+1 sheared moment coordinates differs from the Wronskian
at -lambda by the nonzero factors(-1)^k*d(d-1)...(d-k+1).

Among the D+1 integer shears lambda=0,...,D, at least one therefore
makes that coordinate map invertible. Solve for a basis combination h
whose sheared coordinates are h'_0=...=h'_(r-1)=0,h'_r=1. Its leading
(r+1)-by-(r+1) Hankel minor is nonzero. Clear rational denominators and
extract a nonzero original Hankel minor if an integer witness is desired.
This requires no exhaustive search over coordinate supports. The exported
certificate includes the basis combination, integer moment vector, shear,
and a nonzero original minor, all replayable by exact arithmetic.

The generator in this package accepts rational bases. Its implementation
is not a claim about a numerical algorithm on arbitrary complex input,
or about the complexity exponent of matrix multiplication.

## 5. Attribution and limits

The repository already proved selected cap formats by a torus degeneration
and explicit coordinate-minor certificates. Those proofs and their artifacts
remain valid and unchanged. The concurrent rectangular integration PR76 uses
these caps in its higher-ruling and projection-saturation arguments; those
arguments retain their credits. The present note supplies an all-size proof
in characteristic zero, not a priority claim for the dimension inequality.

A related classical result over finite fields is Roy Meshulam, *Spaces of
Hankel matrices over finite fields*, Linear Algebra and its Applications218
(1995),73--76, DOI10.1016/0024-3795(93)00158-V. Its published abstract and
author's bibliography were inspected. Its finite-field theorem is not used
as an unstated characteristic-zero lemma here; the proof above is complete.

The Wronskian step itself does not extend automatically to positive
characteristic:1 and t^p are linearly independent with zero Wronskian in
characteristic p. This is a limit of this proof, not a claim that Meshulam's
finite-field inequality fails. The theorem also does not give the image cap
r for a whole Segre image: the earlier exact rank-seven, dimension-eight
Segre control remains a counterexample to that stronger assertion.

No ordinary rank-lift inequality in the applications is imposed on arbitrary
singular tensor degenerations. The exponent remains9/4.
