# Fourth-order family and a rational tenth-order conic jet

October 23, 2026. Owner-directed OpenAI Codex work. Both claims below
are written and unreviewed.

## Source and incidence equations

Use the canonical integer tensor of PR101 and PR107. Put
`index(u,v,z)=28u+7v+z`. Its 4096 coefficient-one terms are

    (index(i,s,6-p-q), index(p,j,6-r-s), index(r,q,6-i-j)),
    i,j,p,q,r,s in {0,1,2,3}.

Let A0 contain the twelve first coordinates `index(i,j,z)` with
`i,j in {1,2}` and `z in {0,3,6}`. Let K contain the other 100 coordinates.
For 14-by-112 maps B(t), C(t), flatten the contraction into a 112-by-196
matrix F(t), and set W(t)=F(t)[A0,:]. A jet of order n consists of maps
B_0,...,B_n, C_0,...,C_n and 100-by-12 matrices Y_1,...,Y_n such that

    F_k = sum_{i+j=k} T(-,B_i,C_j),
    F_0[K,:] = 0,
    F_k[K,:] = sum_{i=1}^k Y_i W_{k-i},  1 <= k <= n.       (1)

The leading ranks must be `rank(B_0)=rank(C_0)=14` and `rank(W_0)=12`.
Those ranks provide unit minors over the truncated polynomial ring.
Equation (1) then makes every other source row a combination of the
twelve rows W(t), so the incidence flattening has rank exactly twelve.
This is a local incidence construction, not the full matrix target.

## A fourth-order family on every mixed cubic parameter

**Claim AI-CONIC-MIXED-FOURTH-JET-001.** For every complex a,b,d with
d nonzero and c=-d^3, the explicit PR107 mixed-family coefficients through
order two extend to an incidence jet of order four. The coefficients lie
in Q[a,b,d,d^-1], with d-pole order at most three. The prescribed first
normal class [1:d] is retained.

The witness is
`results/conic-higher-jets-2026-10-23/mixed-fourth-family.json`.
It retains PR107's B_i,C_i for i=0,1,2. Define

    Delta = (a+d^3)*(b-d^3).

For r=0,1,2,5, let E_r have entries one at (2r,1) and (2r+1,2), and
zero elsewhere; row and column indices start at zero. Let N_B1,N_C1
be the credited middle-one normal pair. Add to PR107's third coefficient

    delta B3 = u0*E_0 + u1*E_1 + u2*E_2 + u3*E_5 + v*N_B1,
    delta C3 = v*N_C1,
    v  = Delta^2/(9*d),
    u0 = -Delta^2*(3*a*b^2-6*a*b*d^3+3*a*d^6
                  +4*b^2*d^3-8*b*d^6+3*d^9)/(3*d^3),
    u1 = -Delta^2*(b+d^3)*(a*b-a*d^3+2*b*d^3-d^6)/3,
    u2 = Delta^2*(b-d^3)*(3*a*b-2*a*d^3+4*b*d^3-2*d^6)/(3*d^3),
    u3 = b*Delta^2*(2*a*b-2*a*d^3+3*b*d^3-2*d^6)/3.

The exported fourth coefficients have 58 nonzero B entries and 48
nonzero C entries. Y1=Y2=0, and Y3,Y4 each have 16 nonzero entries.
The short formula and the complete sparse witness are checked separately.

The acceptance program `verify_symbolic.py` contracts the literal source.
It imports the dictionary arithmetic in `verify.py`, not the tangent
solver or predecessor cohomology operator. Exact rational-function
normalization checks all 19,600 entries of (1) at each order 1 through 4.
The arithmetic parser accepts only rational arithmetic in a,b,d and
checks the denominator of every coefficient. Every denominator is a
nonzero rational constant times a power of d of exponent at most three.
The chosen leading minor determinants are exactly 1,1,-1.

Consequently all coefficient identities specialize at every complex
a,b,d with d nonzero, and the leading ranks never drop in that chart.
This proves the stated family. The proof has no additional generic
parameter condition. The d=0 fiber remains outside the construction.

The exact discovery system allowed all seventy tangent fields at order
three. Its symbolic augmented system has 652 distinct rows and 71
columns, with rank 50. These discovery dimensions are not premises for
the positive result; the exported coefficient identities suffice.

## A tenth-order jet at one rational point

**Claim AI-CONIC-RATIONAL-TENTH-JET-002.** At a=1,b=2,d=1,c=-1,
PR107's mixed-family coefficients through order two extend to an
incidence jet of order ten over Q.

The witness is
`results/conic-higher-jets-2026-10-23/rational-ten-jet.json`.
It contains eleven B maps, eleven C maps, and ten source-row corrections.
The point has a-c=2 and b+c=1, so it lies outside the two previously
integrable linear components. The first coefficient contains 128
nonzero entries outside the boundary planes.

The separate acceptance program `verify.py` uses only the Python
standard library and rational arithmetic. It rebuilds all 4096 source
terms, checks the leading ranks, compares coefficients through order
two with the credited PR107 specialization, and checks every entry of
(1) through order ten. The resulting equations hold over Q[t]/(t^11)
and remain valid over C after extension of scalars. They establish the
finite jet claim.

This witness uses a different choice of the fourth coefficient from
the universal fourth-order witness. Both are accepted by their own
coefficient identities; they are not claimed to be successive
truncations of one common family.

Discovery continued through orders four to ten. At each step it allowed
the preceding coefficient to change by all seventy tangent fields while
fixing earlier coefficients. The selected rational augmented system
had 379 rows, 71 columns and rank 50 at every completed step. The last
uncorrected order-eleven Schur coefficient has 680 nonzero entries.
Neither those ranks nor that residual count proves an all-order claim
or an obstruction to order eleven.

## Scope and next question

Both results concern rank-twelve incidence of two fourteen-row maps of
the canonical 112-cubed source. They do not construct the full
M(10,10,11) target, prove an all-order formal curve, or improve omega.
The symbolic statement covers order four; order ten is established
only at the specified rational point. The d=0 cubic fiber remains open.

The next question is whether a finite algebraic parameterization explains
these compatible jets. All retained maps have paired rows separated by
one source coefficient. This suggests a smaller polynomial-matrix
incidence problem, but no reduction or all-order parameterization is
claimed in this package.

PR101 retains credit for the source, conic base, normal fields and tangent
operators. PR107 retains credit for the mixed third-order family and
its acceptance design. This package adds the displayed third correction,
fourth coefficients and rational continuation through order ten. The
verifiers were prepared in the same generating session; separate source
replay is not independent mathematical review or formalization.
