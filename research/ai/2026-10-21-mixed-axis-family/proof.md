# Uniform reduction on a mixed-row axis

Written proof, unreviewed, October 21, 2026. Claim
`AI-MIXED-AXIS-REDUCTION-091`. Work over C at the canonical leading flags,
with rank-one partners u=(a,-a,-1,1), v=(a,1,a,1), the full B seven-frame,
and any C five-space V containing m+t*d0. Here a is arbitrary, t is
nonzero, and d0 is the first boundary vector of the maximal C frame.

The necessary normal equations have a complete32-dimensional kernel.
After removing the four common-plane directions, every target-admissible
normal lies in an explicitly certified10-dimensional linear family. This
holds for every complex a and nonzero complex t. The remaining family is
not eliminated here; this is not a full axis exclusion or an exponent gain.

## 1. The actual mixed row and a complete normal kernel

Adopt the full-B normal kernel of dimension88, the virtual C correction,
and the sixteen adapted low-rank source slices from claim088. Their
correction errors factor through Psi and vanish on the actual first
space V contained in ker Psi. The target rank gap forces the sixteen
adapted slices to vanish on V as well.

Shear the C basis by U with U[0,6]=t and all other off-diagonal entries
zero. The new e6 is the actual row m+t*d0 in V. Apply this basis change
to Psi and every C factor of the virtual tensor. No pure-row containment
is assumed in the original coordinates.

The last columns of Psi and the sixteen vanishing slices give312 linear
equations in88 variables. The saved kernel K has32 columns, an identity
free-coordinate block, and satisfies the complete polynomial identity
M*K=0. Its entries are Laurent polynomials in t with polynomial a
coefficients. The verifier reconstructs M from the maintained source and
checks a56-by56 minor with determinant exactly t^18. Thus K is a complete
kernel at every a and t!=0; there are no omitted exceptional a values.

The four common-plane normals lie in K and annihilate both the full
obstruction and the virtual third tensor. A constant complement in the
32 free coordinates leaves28 quotient parameters d. The verifier checks
the plane embedding and reconstructs this complement exactly.

## 2. A selected row subspace and its projection

Stack Psi and the sixteen necessary vanishing slices into Z(d). Its rows
annihilate V, its mixed column is zero, and rank Z(d)<=2. Retain the56
specified rows S(d) from its joint coefficient matrix. Only inclusion
Row(S(d)) in Row(Z(d)) is needed; this proof does not assume that the
selected rows span the whole obstruction at every parameter value.

Denote the six boundary columns of S by (E0,O0,E1,O1,E2,O2), and define

    Q(d) = t^3*(O0-a^3*E0, O1-a^3*E1, O2-a^3*E2).

The factor t^3 is nonzero and clears Laurent denominators. Ten explicit
polynomial row combinations N give W(d)=N^T*S(d), with

    W_odd=a^3*W_even,  W_mixed=0.

The coefficient matrix of W_even has rank18 for every a and t!=0, so
W=0 has a complete10-dimensional kernel in the28 quotient parameters.
Completeness is certified by18 unit pivots and two elementary column
additions over Q[a,t,t^-1]. Every pivot is a nonzero rational multiple
of a power of t; no expression depending nontrivially on a is inverted.

## 3. The projection has minimum nonzero rank two

The projection satisfies the uniform implication

    rank Q(d)<=1  implies  d=0.                       (1)

For each saved triangular two-minor, both diagonal entries are Laurent
units times the same linear form L(d), and the upper off-diagonal entry
is zero. Its determinant is a Laurent unit times L(d)^2. If rank Q<=1,
then L(d)=0 over C. The verifier checks the original diagonal identities,
the triangular zero, and every coefficient of the forms.

The first28 saved forms have a complete kernel of dimension4. Its
reduction uses24 Laurent-unit pivots and two elementary column additions.
After substituting that kernel, four further square minors force all
four parameters to zero. Hence the two rounds have dimensions

    28 -> 4 -> 0.

The Gaussian certificates are replayed as invertible row and column
operations. Column additions have Laurent polynomial coefficients and
determinant one. Row normalizations divide only by nonzero rational
multiples of t powers. Final residual rows are checked to be identically
zero, and the reconstructed complete kernels are checked against the
original matrices. Consequently (1) holds at every complex a, including
a=0 and a^3=-1, with only the stated exclusion t=0.

## 4. The remaining necessary family

For fixed a,t,d, the column projection sends Row(S(d)) onto Row(Q(d));
its kernel contains Row(W(d)). Thus

    rank S(d) >= rank Q(d)+rank W(d).

If d is nonzero, (1) gives rank Q(d)>=2. Since rank S(d)<=rank Z(d)<=2,
we must have W(d)=0. This also holds for d=0. Every target-admissible
normal therefore lies in the complete10-dimensional kernel certified
in Section2, plus the four plane directions removed in Section1.

At t=0 the earlier pure-row theorem applies. The present statement is a
uniform necessary reduction on the nonzero axis. It does not show that
every vector in the remaining family is target-admissible, and it does
not exclude the axis by itself. General two-coordinate graph charts,
other partner strata, smaller first spaces and other flags remain open.

## 5. Limits of the discovery calculations

A direct rational row reduction introduced factors such as t-2*a^3.
Those factors were artifacts of that kernel representation: the accepted
Laurent-unit certificate covers their zero sets too. A later attempt to
construct a global terminal row basis stalled; it supplies no closure.
Direct uniform triangular cubic cuts also stalled on the selected rows.

At a=t=1, a separate exact incidence calculation finds rank-two
projection controls inside the remaining family. Thus the hoped-for
stronger assertion that Q has minimum nonzero rank three there would be
false. The complete obstruction still excludes the fixed graph through
claim090. The full obstruction, or further target conditions, is required
to close this axis. None of these local calculations constructs a matrix
multiplication algorithm.
