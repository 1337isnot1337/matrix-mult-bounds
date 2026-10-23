# Pure polynomial incidence curves and third-order normal-class existence

October23, 2026. Owner-directed Codex work, written and unreviewed.

## 1. Exact curve on the pure cubic fiber

Use the canonical integer 112-cubed source T and coordinate conventions
of PR101 and PR107. The twelve leading first-source coordinates A0 are
index(i,j,z)=28i+7j+z with i,j in {1,2}, z in {0,3,6}. K is the remaining
100-coordinate subspace.

Specialize PR101's cubic-component polynomial witness at d=0, hence
c=-d^3=0. Its maps have the form

    B(t)=B0+t*B1+t^2*B2,   C(t)=C0+t*C1.

All entries are in Q[a,b,t]. The exported certificate has respectively
(24,8,8) and (24,8,0) nonzero coefficient entries before specializing
a,b. Literal-source verification proves

    T(-,B(t),C(t))[K,:]=0                              (1)

as an exact polynomial identity. There are only the four possible
product degrees zero through three; replay additionally checks the
identically zero degree four slot of the stored coefficient format.
Every one of the 19600 K coordinates is checked in every slot. There
is no discarded higher term or moving-source correction.

At t=0 the selected fourteen-row minors of B0 and C0 both have
determinant one. The selected twelve-row source minor has determinant
minus one. These identities hold over Q[a,b], so for every complex a,b
the corresponding formal minors in t are units. Thus B(t),C(t) have
rank fourteen and the first-source contraction has rank exactly twelve
near t=0, while (1) holds for all t. The curve is therefore an all-order
formal incidence lift on this pure fiber, with fixed kernel K.

The constant and first coefficients are checked against the credited
specialization. PR101 identifies their projective non-plane normal class
as [1:0]. This gives claim `AI-CONIC-PURE-CURVE-003`. The maps are
inherited, with credit retained; the new result is their exact pure-fiber
certification. No independently invented map or historical priority is
claimed.

## 2. Complete criterion through order three

For every affine a,b,c in C and every nonzero [lambda:mu], some
rank-twelve incidence three-jet of two fourteen-row maps has this normal
class, allowing suitable boundary velocity and higher coefficients, if
and only if

    (a-c)*(b+c)*(c*lambda^3+mu^3)=0.                   (2)

Necessity follows by truncating a three-jet to a two-jet and applying
PR101's complete order-two criterion, which allows all boundary
velocities and moving kernels.

For sufficiency, first suppose a=c or b=-c. PR101's exact linear
incidence curves realize every nonzero normal class, so in particular
they give three-jets.

Otherwise (2) forces c*lambda^3+mu^3=0. In this case lambda cannot be
zero: it would force mu=0. Put d=mu/lambda, so c=-d^3. If d is nonzero,
PR107's explicit mixed family gives a three-jet with class [1:d], with
exact unit leading minors. If d=0, the exact pure-fiber curve from
section1 gives class [1:0]. These classes are [lambda:mu]; if a chosen
nonzero representative is desired, rescale t by lambda. This exhausts
the projective normal line and proves sufficiency. This gives claim
`AI-CONIC-THIRD-CRITERION-004`.

This is an existence criterion after choosing appropriate boundary
velocity and higher coefficients. It does not assert that every fixed
first representative, every two-jet or every second coefficient extends.

## 3. Verification, attribution and limits

The verifier pins the credited source data and the literal-source
contraction implementation from PR107, specializes the old witness
without a tangent solver, checks all polynomial coefficients and the
three leading minor identities, and compares the credited first jet.
Corruption controls alter a quadratic coefficient, the first jet,
the pure coefficient ring and the polynomial degrees. These checks
support (1); the implication (2) additionally uses the explicitly
credited complete second-order theorem, mixed three-jet family and
linear incidence components.

All code, algebra and prose in this continuation were prepared with
OpenAI Codex under owner direction. No new external theorem is imported.
Independent implementations and CI are not independent mathematical
review or formalization.

The pure fiber's exact curve does not extend the mixed component to all
orders. Mixed fourth-order compatibility, other projective base charts,
the separate12-by8 problem and the full matrix-target construction
remain open. No smaller matrix-multiplication exponent is established.
