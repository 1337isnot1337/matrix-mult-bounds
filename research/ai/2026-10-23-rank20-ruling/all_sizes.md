# The first nonminimum source locus at every square size

October23,2026. Owner-directed OpenAI Codex continuation. Written and
unreviewed over C, without independent review or formalization.

## 1. General statement

Let a>=2 and let A_a be the canonical cyclic product of three C(a,a),
with N=a^2(2a-1). Its minimum nonzero slice rank is a^2. The entire
nonzero source locus of rank at most a^2+a consists of

    F=g tensor h,

where h is a coherent scalar-Hankel-rank-one factor and the biform
g in S_(a-1)(x) tensor S_(a-1)(z) has a divisor of degree a-2 in x or
in z. Every vector subspace in that source locus has dimension at most
2a, and the bound is attained. Zero is included when discussing subspaces.
All forms and divisors are homogeneous binary forms over C, including
repeated roots and roots at infinity.

This specializes at a=4 to the rank20 classification and dimension-eight
bound in [the A4 proof](proof.md). It is not a finite-source-grid claim.

## 2. Factor classification

The prior polynomial-rank-locus theorem applies because a^2+a<2a^2.
It gives F=g tensor h and fixes one h on any linear source space.
The source rank is rank R(g). Remove the common x divisor of g's
coefficient forms, leaving primitive x-degree d, 0<=d<=a-1. The prior
coefficient-map kernel formula is

    rank R(g)=a^2+sum_(j=1)^(a-1) min(a,mu_j),
    mu_j>=0,                  sum_j mu_j=a*d.          (1)

Its hypotheses and Grothendieck splitting dependency over P^1(C) are
exactly those of the pinned earlier gap proof, with b=a.

If d<=1, g has an x divisor of degree at least a-2. Since C is
algebraically closed, any larger common binary divisor has a divisor
of the required degree. If d>=2 and rank R(g)<=a^2+a, equation(1)
forces one mu_j=a*d and all other a-2 degrees zero. If every degree
were below a, the truncated sum would be a*d>=2a. If one is at least
a, its truncated contribution is a, leaving no other positive degree.

Thus the a-by-(2a-1) multiplication matrix has at least a-2 constant
kernel vectors. If U in S_(a-1)(z) is the span of its biform coefficient
polynomials, its constant row span is S_(a-1)U and has dimension at most

    (2a-1)-(a-2)=a+1.

Leading-degree multiplication gives dim(S_(a-1)U)>=dim U+a-1, so dim U<=2.
Dimension one would make g separable, contrary to primitive d>=2. For
independent P,Q in U, put s=degree gcd(P,Q). Their degree-(2a-2) common
multiples have dimension s+1, giving

    dim(P S_(a-1)+Q S_(a-1))=2a-s-1<=a+1.

Hence s>=a-2, and independence forces s<=a-2. Thus the z coefficients
share a divisor of degree a-2. Restoring the x common factor keeps it.
This proves one containment. Conversely an x divisor of degree a-2
leaves d<=1 in (1), making rank at most a^2+a. Transposition proves
the same for a z divisor. The two families therefore give the full locus.

## 3. The sharp linear-space bound

The two divisor families are projectively closed images of

    P(S_(a-2)) times P(S_1 tensor S_(a-1)).

A linear space is irreducible, so a space in their union lies in one.
Assume it lies in the x-divisor family. If all its elements are separable,
the two-factor rank-one bound gives dimension at most a<=2a. Otherwise
choose a nonseparable f_0=h v with exact common x divisor h of degree
a-2 and primitive vector-valued linear form v with a components.

The generic-pencil lemma from the A4 proof is unchanged for vector-valued
forms of degree a-1: rational-function independence makes their wedge
nonzero, so roots of a generic common divisor lie in one fixed finite
projective set. The generic multiplicity is the minimum of the two
vanishing orders. Therefore any element rationally independent of f_0
shares the full divisor h. If none exists, every element is q v with
q in S_(a-2), giving dimension at most a-1. If an independent g_1 exists,
adding it to any dependent element shows that element is also divisible
by h. The whole space is then inside

    h (S_1(x) tensor S_(a-1)(z)),

of vector dimension 2a. The symmetric case is identical. This dimension
is attained by the whole displayed fixed-divisor space, with a fixed
coherent middle factor. This also covers a=2, where h has degree zero.

## 4. A uniform Laurent obstruction

Take a target Xi(X)=X tensor I_n on Mat_m(C), with R=mn<=N and k=N-R.
Suppose m>2a. By the shared-correction criterion, no formal degeneration
to this target can have a regular long map C of leading rank c when

    n+k+N-c<=a^2+a,       a^2>N-c+k.                   (2)

Both other maps and the original identity lift may have arbitrary finite
poles. Equivalently the sufficient integer lower bound on c is

    max(N+n+k-a^2-a, N+k-a^2+1),

provided it does not exceed R. The two long legs are symmetric. Scalar
balancing gives the same necessary bound on each long leading rank in
any remaining candidate.

For A4 to M(10,10,11), this bound is105. At a=5, the bounds are216 for
M(13,13,17),212 for M(14,14,16), and210 for M(15,15,15). These are scoped
singular-long-map exclusions, not constructed matrix products or accepted
exponent improvements. No optimality of these thresholds is asserted.

The source formulas and external splitting theorem retain their prior
credit. The all-size factor and linear-space arguments are local extensions.
Finite selected-size controls support the calculations without proving or
formalizing these universal statements. All new assertions are unreviewed.
