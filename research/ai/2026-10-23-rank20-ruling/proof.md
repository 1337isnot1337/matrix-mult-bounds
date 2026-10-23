# The A4 rank20 locus and its largest linear spaces

October23, 2026. Owner-directed OpenAI Codex continuation over C.
Written and unreviewed; no independent mathematical review or formalization.

## 1. Adopted source formula and reduction

The source is the canonical A4 with 112-dimensional legs. Adopt the
pinned prior source results, retaining their original credit:

* Every nonzero source slice has rank at least16.
* A source slice of rank below32 is g tensor h, where g is a biform of
  bidegree(3,3) and h has scalar Hankel rank one. A vector space wholly
  below rank32 has one fixed coherent h. Its source matrix rank equals
  the rank of the biform coefficient map R(g).
* Write the homogeneous x-coefficient forms of g as degree-three binary
  forms and remove their greatest common divisor in x. Let the remaining
  primitive degree be d, with 0<=d<=3. The kernel bundle of its four-row
  multiplication matrix on P^1(C) has splitting degrees mu_1,mu_2,mu_3,
  all nonnegative, sum mu_j=4d. Then

      rank R(g)=16+sum_(j=1)^3 min(4,mu_j).              (1)

The last formula and its external Grothendieck splitting dependency are
in the earlier slice-rank-gap proof. The formula uses the full coefficient
map, including its boundary coefficients; no polynomial output is discarded.
The prior polynomial-rank-locus proof supplies the fixed-h statement.

Let S_d denote homogeneous binary forms of degree d. We prove:

> The nonzero biform locus rank R(g)<=20 is the union of forms in
> `h_x (S_1(x) tensor S_3(z))` for some h_x in S_2(x), and forms in
> `h_z (S_3(x) tensor S_1(z))` for some h_z in S_2(z).
> Every vector subspace of A4 slices of rank at most20 has dimension at
> most eight. The bound is attained.

## 2. The rank20 biform locus

If d=0 the biform is separable. If d=1, the removed x common factor has
degree two, so g lies in the first displayed family. Suppose d>=2.
By (1), sum min(4,mu_j)<=4 while sum mu_j=4d>=8. The only possibility
is one positive mu_j=4d and two zero degrees. Indeed two positive terms
would either sum to at least eight before truncation, or one would
contribute four and another at least one after truncation.

Consequently the multiplication matrix H(x), of size4 by7, has at least
two independent constant kernel vectors. Let U be the span in S_3(z)
of the z-polynomial coefficients of the primitive g as a polynomial in x.
The common constant row span of H's coefficient matrices is exactly
S_3(z) U inside S_6(z): each coefficient matrix has rows consisting of
the four z shifts of one coefficient polynomial. It has dimension at
most7-2=5.

For a nonzero subspace U of binary cubics, dim(S_3 U)>=dim U+3. One
elementary proof dehomogenizes and chooses a basis of U of distinct
leading degrees. The leading degrees from multiplying by1,z,z^2,z^3
contain at least dim U+3 distinct integers; their corresponding products
are linearly independent. A linear change of coordinates avoids no
exception: dehomogenization on either affine chart is injective for forms
of one fixed degree. Thus dim U<=2. Dimension one would make g separable
and d=0, so dim U=2.

Take independent P,Q in U, and put s=degree gcd(P,Q). The two spaces
P S_3 and Q S_3 each have dimension four. Their intersection consists
of the common multiples of degree six, namely lcm(P,Q) S_s, of dimension
s+1. Hence

    dim(S_3 U)=8-(s+1)=7-s<=5.

Independence gives s<=2, so s=2. Thus U=h_z S_1(z), proving that g has
a quadratic z divisor. Restoring the removed x common factor preserves
that divisor. This proves containment in the claimed union.

Conversely, if g has a quadratic x divisor, its primitive x-degree is
at most one. Formula (1) has sum mu_j<=4 and therefore rank R(g)<=20.
A quadratic z divisor gives the same conclusion by transposing the
biform coefficient map. Thus the classification is exact, including
separable forms and common factors with repeated roots or roots at infinity.

## 3. A generic-pencil common-factor lemma

Let f,g be vector-valued homogeneous binary cubics, independent over the
rational function field C(x). For all but finitely many scalar t, the
degree of the common divisor of the components of f+t g equals that of
all components of f and g together.

To see this, any common zero of f+t g lies among the zeros of the
nonzero wedge f wedge g. This is a finite set of projective points.
At each such point, use a local coordinate and let a,b be the minimum
vanishing orders of the components of f,g. Except for at most one scalar
t, the minimum order for f+t g is min(a,b): its first potentially nonzero
coefficient vector cannot cancel except at one t. The same argument uses
the other affine chart at infinity. Avoiding finitely many exceptional t
at finitely many points gives the assertion with multiplicities. This
argument requires rational-function independence; it is not asserted
for proportional vector-valued forms.

## 4. Maximum dimension when the quadratic divisor may vary

Let V_x be the biform cone with an x quadratic divisor, and V_z its
symmetric counterpart. They are projectively closed: V_x is the image
of P(S_2) times P(S_1 tensor S_3) under the everywhere-defined homogeneous
multiplication map; likewise for V_z. Thus a vector space W contained
in V_x union V_z is contained in one of them, since a linear space over C
is irreducible and cannot be the union of two proper closed subsets.

Assume W is contained in V_x. If all its nonzero forms are separable,
the elementary two-factor rank-one linear-space bound gives dim W<=4.
Otherwise choose a nonseparable f_0 in W. Its x common divisor h has
degree exactly two, and f_0=h v(x), where v is a primitive C^4-valued
linear form.

For any g in W independent of f_0 over C(x), every f_0+t g has a common
x divisor of degree at least two. The pencil lemma implies that the
components of f_0 and g have a common divisor of degree at least two.
It divides h, so g is divisible by this fixed h.

If no such independent g exists, every element of W is q(x) v(x), with
q in S_2. Primitivity of v removes possible rational denominators, and
the homogeneous degrees force degree two for q. Then dim W<=3.
Otherwise fix an independent g_1. For an element g dependent on f_0,
g+g_1 is independent of f_0, so both g+g_1 and g_1 are divisible by h,
and therefore so is g. Thus all W is contained in

    h (S_1(x) tensor S_3(z)),

which has vector dimension eight. The same argument holds for V_z.
Taking all eight forms in either fixed-divisor space attains the bound.
The fixed coherent factor from Section1 transfers it to A4 source slices.

## 5. The singular long-leg consequence

Apply PR125's pinned shared-correction ruling criterion, with

    N=112, R=110, m=10, n=11, k=2, mu=16.

For a regular long map with c>=105 at zero, the source rank cap is

    L=11+2+112-c<=20.

Every source linear space at that cap has dimension at most8<10, and
mu-(N-c)-k>=16-7-2=7>0. The criterion excludes the full A4 to
M(10,10,11) Laurent degeneration, allowing arbitrary finite poles in both
other maps and in the original identity lift. Transposition treats the
other long leg. Equivalently every remaining candidate has scalar-balanced
leading ranks at most104 on both long maps.

At c104 the cap is21. This proof neither classifies that larger locus
nor supplies the needed linear-space bound there. It does not claim the
threshold105 is optimal. No complete degeneration exclusion, constructed
matrix target or exponent improvement follows.

## 6. Dependency and evidence boundaries

The source definitions, the rank formula and its splitting theorem,
the fixed coherent-factor theorem and the shared-correction criterion
are prior work with exact pins and existing credit. The local additions
are the rank20 classification, the generic-pencil common-factor argument,
the sharp linear-space dimension eight and its singular-long application.
The splitting theorem is Grothendieck1957 Theorem2.1, printed p126, for
holomorphic vector bundles on P^1(C); this field and hypothesis are retained.

Exact finite controls support the polynomial and source-rank identities
but do not prove the universal classification, formalize arbitrary series
or constitute independent mathematical review. All new assertions remain
written and unreviewed.
