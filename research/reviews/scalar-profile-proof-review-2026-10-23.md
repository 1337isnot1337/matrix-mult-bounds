# Scalar profile proof review

**Reviewed claim:** `AI-SCALAR-001`, Section 2 of
[`research_note.md`](../ai/2026-10-20/research_note.md).

**Source pin:** repository commit `1c04903c215f396150605c0778024e856ec0b0d4`;
the reviewed note blob is `356dd1a605e5b1e8293fb9a9a7c306517225663d`.
The note is unchanged from the earlier main commit `dcd209a`.

**Conclusion:** I found no gap in the all-integer proof that `P_*` is the
pointwise minimum among positive functions satisfying S1-S3. The argument
uses only those three assumptions for the lower bound. The separate rank-upper
and replication sections establish compatibility of this candidate with those
additional constraints. This audit does not construct a tensor character,
establish an exponent improvement, or count as independent human review or
Lean formalization. The claim remains proof-written and unreviewed.

## Review of admissibility

For fixed `a`, the formula is

\[
P_*(a,b)=h_a\left(b+\frac{a-1}{2}\right) \quad (b\ge a),
\]

and is affine in `b` on this range. The only concavity check at the join is
the second difference centered at `b=a`. Substitution of
`h_a=(3a-2)h_{a-1}/(3a-3)` gives

\[
P_*(a,a)-P_*(a,a-1)=h_a,
\]

so the left and right first differences agree. For `2\le b<a`, direct
substitution of the recurrence gives the stated slack
`2 h_b (a-b)/(3b(3b-2))`, which is nonnegative. The boundary value and
symmetry follow directly from the definition.

For shifted tripling with `b\ge a`, the shifted index is still on the affine
branch and the identity is exact. For `b<a`, the shifted index
`3b+a-1` is at least `a`, and the tripling inequality reduces to

\[
F_b(a):=h_a\frac{a+2b-1}{2a+b-1}\ge h_b.
\]

At `a=b` equality holds. The exact ratio comparison in (7) has positive
denominators and numerator `2(a-b)(a-b+1)`, so `F_b(a)` is nondecreasing
for integer `a\ge b`. This proves the remaining case, including `b=1`.

## Review of the pointwise lower bound

Fix `a` and write `\Delta_{a,b}=P(a,b+1)-P(a,b)`. S2 says these increments
are nonincreasing. If any increment were negative, every later increment
would be bounded above by that same negative number and `P(a,b)` would
eventually become negative. Positivity therefore makes every increment
nonnegative. They have a finite limit `\ell_a\ge0`; the Cesaro mean of the
increments, together with `P(a,1)=a` from symmetry and S1, gives
`P(a,b)/b\to\ell_a`.

Iterating S3 uses integer indices `b_{j+1}=3b_j+a-1`, with
\[
b_j=3^j\left(b+\frac{a-1}{2}\right)-\frac{a-1}{2}.
\]
Thus `b_j\to\infty`, and dividing `P(a,b_j)\ge3^jP(a,b)` by `b_j`
proves
\[
\ell_a\ge\frac{P(a,b)}{b+(a-1)/2}.
\]
Taking `b=a` yields `\ell_a\ge K_a`, for
`K_a=2P(a,a)/(3a-1)`.

Symmetry gives the exact diagonal difference
\[
P(a,a)-P(a-1,a-1)=\Delta_{a,a-1}+\Delta_{a-1,a-1}.
\]
Each increment is at least its limiting slope. Substituting the definitions
of `K_a` and `K_{a-1}` and rearranging gives
\[
K_a\ge\frac{3a-2}{3a-3}K_{a-1}.
\]
Since `K_1=1`, induction gives `K_a\ge h_a`. For `b\ge a`, summing the
increments from the diagonal now yields
\[
P(a,b)\ge P(a,a)+(b-a)\ell_a
\ge h_a\left(\frac{3a-1}{2}+b-a\right)=P_*(a,b).
\]
Symmetry covers `b<a`. No limit interchange beyond the elementary Cesaro
limit is used, and no assumption about `P` outside positive integer pairs is
needed.

## Scope and follow-up

The proof of minimality does not use S4. The separate cubic induction proves
`h_a^3\le(3a-1)/2`, which combines with the two factors of `P_*` for
`b\ge a` to give `P_*(a,b)^3\le(a+b-1)^4`; symmetry handles the other half.
The replication argument also checks the candidate against the stated
scaling condition. These are compatibility statements for the scalar model,
not evidence that an actual character attains the model.

This is a first-party Codex audit. An independent human proof review and any
Lean formalization remain outstanding.

## Reproduction record

The repository replay completed with Python 3.14.8 and SymPy 1.14.0. Its
durable [validation record](../../results/scalar-profile-review-2026-10-23/validation.json)
confirms all 10 archived file hashes and exact payload matches for the five
replays: 73,856 scalar grid checks, 353,664 filtration inequalities, 12,976
binary candidates, 209,692 ternary candidates, and 20,000 seeded random
candidates. These finite checks are consistency evidence only; they do not
replace the all-integer argument above.
