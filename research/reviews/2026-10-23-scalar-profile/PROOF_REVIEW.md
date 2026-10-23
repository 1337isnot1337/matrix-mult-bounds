# Internal proof audit: the scalar matching profile

Review target: `dcd209a82e3bf97a64f8e747dd29f3a3242d8e0b`,
`research/ai/2026-10-20/research_note.md`, section 2. The reviewed source blob
is `356dd1a605e5b1e8293fb9a9a7c306517225663d`.

Reviewer: OpenAI Codex under repository-owner direction. This is an internal
consistency audit, not independent mathematical review or formalization.

## Conclusion and scope

No gap was found in the all-integer proof that the displayed profile is the
pointwise minimum among positive symmetric profiles satisfying S1-S3. The
review checked the limiting-slope argument, diagonal recurrence, profile join,
shifted tripling, rank upper bound, and replication inequality. The claim
`AI-SCALAR-001` therefore remains `proof-written-unreviewed`; this audit does
not supply independent review. The result is only about the stated scalar
relaxation. It neither realizes the profile as a tensor character nor improves
the matrix-multiplication exponent.

## Audit of pointwise minimality

For each first coordinate `r`, write
`Delta_(r,s)=P(r,s+1)-P(r,s)`. S2 says that these increments are
nonincreasing from `Delta_(r,1)` onward. If one were negative, all later
increments would be no larger, forcing `P(r,b)` eventually below zero.
Positivity rules this out. Thus `Delta_(r,s)` decreases to a finite
nonnegative limit `ell_r`; Cesaro averaging gives `P(r,b)/b -> ell_r`.

Iterating S3 gives `b_j=3^j(b+(a-1)/2)-(a-1)/2` and
`P(a,b_j)>=3^j P(a,b)`. Each `b_j` is an integer by the recurrence
`b_(j+1)=3*b_j+a-1`. Dividing by `b_j` and taking the limit yields
`ell_a>=P(a,b)/(b+(a-1)/2)`. In particular, with
`D_a=P(a,a)` and `K_a=2*D_a/(3*a-1)`, we have `ell_a>=K_a`.

Symmetry gives the exact diagonal split
`D_a-D_(a-1)=Delta_(a,a-1)+Delta_(a-1,a-1)`, so this difference is at
least `K_a+K_(a-1)`. Substituting the definitions of `K` gives
`K_a >= ((3*a-2)/(3*a-3))*K_(a-1)`. Since `K_1=1`, induction yields
`K_a>=h_a`, with exactly the recurrence already attributed to the external
9/4 proof. Also `ell_a>=h_a`. For `b>=a`, summing increments from `a` to
`b-1` now gives
`P(a,b)>=h_a*((3*a-1)/2+b-a)=P_*(a,b)`; symmetry handles `b<a`.

## Audit that the lower profile is feasible

Symmetry and the edge value follow from its definition. For `2<=b<a`, the
second difference is exactly
`2*h_b*(a-b)/(3*b*(3*b-2))`, which is nonnegative. For `a>=2` at `b=a`,
the recurrence gives `P_*(a,a-1)=((3*a-3)/2)*h_a`; together with the affine values
`P_*(a,a)=((3*a-1)/2)*h_a` and
`P_*(a,a+1)=((3*a+1)/2)*h_a`, this makes the second difference at the join
zero. Above the join the profile is affine in `b`.

For shifted tripling and `b>=a`, the inequality is equality. For `b<a`, it
reduces to monotonicity in integer `a>=b` of
`F_b(a)=h_a*(a+2*b-1)/(2*a+b-1)`. The difference
`F_b(a+1)-F_b(a)`, after clearing its positive denominator, has numerator
`2*(a-b)*(a-b+1)` after factoring out `h_a>0`. Thus this sequence is
nondecreasing and S3 follows. The endpoint `a=b` is included with equality.

For the rank upper bound, induction reduces `h_a^3<=(3*a-1)/2` to the exact
positive gap `27*a^3*(3*a+2)-(3*a+1)^3*(3*a-1)=6*a+1`. Sorting so `a<=b`,
both `(3*a-1)/2` and `b+(a-1)/2` are at most `a+b-1`, proving
`P_*(a,b)^3<=(a+b-1)^4`.

For replication, the identity
`(1+1/(3*a))^3-(1+1/a)=(9*a+1)/(27*a^3)>0` makes
`h_a/a^(1/3)` nondecreasing. Thus `h_(q*a)>=q^(1/3)*h_a`; the affine factor
in `P_*` scales by at least `q`. Symmetry covers both orderings of `a,b`,
giving `P_*(q*a,q*b)>=q^(4/3)*P_*(a,b)`.

## Reproduction and limits

The archived checker was copied to `/tmp/mmb-scalar-audit-20261023` before
execution because `verify_profile.py` writes its report beside itself. With
Python 3.14.8 and the pinned SymPy 1.14.0, the unmodified checker passed
73,856 exact grid assertions (maximum coordinate 128) and four symbolic
identities. The finite grid supports the algebraic review but is not its proof.
No repository archive file was changed.

The full [archive replay record](../../../results/scalar-profile-review-2026-10-23/validation.json)
also confirms all 10 archived hashes and exact payload matches for the five
replays: 73,856 scalar grid checks, 353,664 filtration inequalities, 12,976
binary candidates, 209,692 ternary candidates, and 20,000 seeded random
candidates. This broader finite replay is consistency evidence only.

This audit does not independently check the source paper's tensor-character
lemmas, the spectral implication from `t` to the square exponent, or any claim
outside section 2. It does not review priority; the repository's existing
attribution notes remain authoritative for that question.
