# Invertible mixed lines cannot acquire further output rows

Written proof, unreviewed, October 21, 2026. This excludes a local
degeneration stratum; it does not improve the matrix-multiplication exponent.

Use the canonical A4 source, with all three source legs of dimension 112,
and the four leading rows

    G_z=e_(0,3,z)-e_(3,0,z), z=1,2,4,5.

Let P(t),Q(t) be regular maps to the two 110-dimensional output legs of
M(10,10,11). The remaining map may be Laurent. Suppose the first effective
new-row space on each side is a line with invertible mixed component.
Their first orders s_B,s_C may be different positive integers. All higher
coefficients and all remaining output rows are arbitrary.

**Claim.** Such a target is impossible. Under the target hypothesis,
regular output-row changes force P(t) and Q(t) to have rank at most five
over C((t)). In particular this closes the ordinary invertible-line
stratum of the both-mixed classification, including arbitrary boundary
graphs. No assumption that a normal direction integrates to a moving
polynomial plane is needed.

## 1. The rank gap for a five-row, five-column cross

Write S(t)=(1,P(t),Q(t))T and let L0 be the saturated limiting first-row
space of S. The canonical leading space W0 has dimension twelve and is
supported on the first four rows and columns. The target first-slice
space R is equivalent to Mat10 tensor I11, has dimension 100, and every
nonzero member has matrix rank at least eleven.

Let C5 denote matrices supported on the first five rows or first five
columns. Each has rank at most ten. In particular R intersects C5 only
in zero. Since W0 is contained in C5 and dim L0 is at most 112,

    L0=R direct-sum W0,       L0 intersect C5=W0.          (1)

Here R is the actual target space in the chosen output coordinates;
only its invariant minimum matrix rank is used. Every leading coefficient
of a regular Laurent first-row combination belongs to L0. Consequently,
if successive coefficients of such a combination lie in C5, they can
be cancelled successively by the twelve source rows A0 spanning W0.
This is the same saturation argument used in the preceding boundary
proofs, with a larger cross whose rank bound is still below eleven.

## 2. Normalize the first new lines and identify their annihilators

Choose one distinguished fifth row on each side, with leading terms
t^s_B b and t^s_C c. After regular row changes, all other new rows have
orders strictly greater than s_B and s_C, respectively. The first four
rows still have leading coefficients G. Denote the least orders of the
remaining rows by N_B>s_B and N_C>s_C, using infinity if they all vanish.

All coefficients of S below order N_B+N_C are in C5, since a matrix
entry outside this cross uses a remaining row on both sides. Starting
with any x in the 100-dimensional leading first kernel K, use (1) to
cancel its successive coefficients in W0. This produces source rows

    x(t)=x-sum_(j>=1) t^j y_j,       y_j in span A0,      (2)

to any order below N_B+N_C. There is no constant correction because
x annihilates S(0).

The fifth-row/leading-column coefficient at order s_B and the exchanged
coefficient at order s_C give

    b in E_B=ann T(K,-,G),   c in E_C=ann T(K,G,-).

Their fifth-row/fifth-column coefficient first occurs at s_B+s_C,
which is below N_B+N_C. No term with y_j, j>=1, can contribute at that
first order. Since W0 has no fifth-row/fifth-column entry, it follows that

    T(K,b,c)=0.                                          (3)

Adopt the complete both-mixed classification, including boundary graphs.
For any compatible pair whose two mixed lines are invertible, its
effective first spaces have dimensions one and one. This implies the
stronger annihilator identities

    ann T(K,-,span(G,c))=span(G,b),
    ann T(K,span(G,b),-)=span(G,c).                       (4)

Indeed a vector h in the first annihilator lies in E_B, and the pair
span(b,h) modulo G, span(c) modulo G still satisfies H_actual=0.
Both mixed projections are nonzero and the C projection is invertible.
The classification forces the B quotient to have dimension one, hence
h belongs to span(G,b). The reverse inclusion follows from (3) and
the extension equations. The other identity is symmetric. This argument
covers every compatible invertible graph pair, rather than just the
displayed rational seed. The verifier independently checks rank 107 for
both 500-by-112 annihilator matrices of that seed.

## 3. Eliminate every remaining row, at every order

Consider a remaining B row with first coefficient t^N_B h. If no B row
is nonzero there is nothing to eliminate on this side. By (2), corrected
source coefficients through order N_B+s_C can be cancelled in W0:

    N_B+s_C < N_B+N_C.

At order N_B in that B row and the first four C columns, the coefficient
is exactly T(x,h,G). At order N_B+s_C in that row and the fifth C column,
it is exactly T(x,h,c). Earlier source corrections cannot affect either
entry at its first possible order. Both entries lie outside the support
of W0, so they must vanish for every x in K. Equation (4) therefore gives

    h=sum a_i G_i+a_5 b.

Subtract from this remaining row t^N_B sum a_i times the first four
actual P rows and a_5 t^(N_B-s_B) times its actual fifth row. These are
regular operations, congruent to the identity modulo t, and raise the
row's order. They use the full current rows, with all their higher terms;
no assumption about the leading rows' later deformations is made.

The exchanged argument applies through order N_C+s_B<N_C+N_B and
eliminates the first coefficient of every remaining C row. Perform both
sets of eliminations and repeat. The inequalities remain strict. For
each power of t, only finitely many elimination steps affect that power,
so the output-row changes converge in C[[t]] and remain invertible with
identity constant term. In the resulting maps only the five distinguished
rows on each side remain. Both generic output ranks are at most five.

If only one side still has remaining rows, the same proof applies with
the other N equal to infinity. Thus the induction has no simultaneous
growth assumption and also covers arbitrarily late, unequal growth.

Matrix flattening rank at most five is closed under limits, even after
an arbitrary Laurent map on the first leg. It is incompatible with the
target's concise output dimensions 110 and 110. This proves the claim.

## 4. Relation to the finite lifting work

The preceding package's 40-dimensional normal filter and sixteen
quadratic conditions remain valid finite calculations. A retained control
with uncorrected first rank thirteen can be corrected through order three:
the first particular second correction had a cubic residual, but allowing
its homogeneous freedom cancels that residual. The saved five-output
curve and a separate Fraction contraction replay certify all four
coefficients through degree three. They do not certify an all-order lift.

Neither this finite lift nor nonzero normal directions can bypass the
output-row obstruction above. The next open construction strata include
the rank-one mixed partner lines with smaller boundary spans, first
spaces with a mixed projection on only one side, smaller pure-boundary
spaces, and other leading flags. The rank-one seven-by-seven control is
not excluded by this five-frame argument: its enlarged cross no longer
has rank below eleven.

## Attribution and scope

Canonical source and extension data are adopted from the first-extension
package. The saturated-limit argument and arbitrary Laurent first maps
are adopted from the moving-boundary and third-boundary proofs. The
both-mixed package supplies the all-parameter graph classification used
in (4). The new argument uses the enlarged rank-ten cross and those
annihilators to eliminate every additional output row, including delayed
unequal orders. Exact finite certificates and the written proof are from
this generating session; no independent review or formalization is claimed.
