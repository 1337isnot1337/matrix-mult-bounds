# Second-pass review of the scalar sharpness proof

Review date: October 23, 2026. Source: [the October 20 research note](../2026-10-20/research_note.md).

## Scope and result

I reviewed Sections 2.1–2.4 of `research/ai/2026-10-20/research_note.md` at
source commit `fe602e418743f37a7cfa54d788b64aaf8a9d6095`. The reviewed file's
SHA-256 is recorded in the package manifest. I find no gap in the stated
all-positive-integer scalar argument. This is an analytic second-pass review
by Codex, not independent human review or Lean formalization; the original
claim status remains `proof-written-unreviewed`.

The proof is conditional on the displayed scalar assumptions (S1)–(S3). It
does not construct a tensor character with profile `P_*`, prove
`omega >= 9/4`, or improve the exponent.

## Lower bound audit

For fixed `a`, put `Delta_b=P(a,b+1)-P(a,b)`. From (S2), the sequence
`Delta_b` is nonincreasing. If some `Delta_k<0`, then every later increment
is at most `Delta_k`, forcing `P(a,n)` eventually negative. Positivity rules
this out, so all increments are nonnegative. Therefore they have a finite
limit `ell_a >= 0`; the Cesaro identity for `P(a,n)` gives
`ell_a=lim_{n->infinity} P(a,n)/n`, and every increment is at least `ell_a`.

Iterating (S3) sends `b` to

```
b_j = 3^j * (b+(a-1)/2) - (a-1)/2.
```

These are positive integers, including when `a` is even, and
`P(a,b_j) >= 3^j P(a,b)`. Dividing by `b_j` and using the full slope limit
gives

```
ell_a >= P(a,b)/(b+(a-1)/2).
```

At `b=a`, this yields `ell_a >= K_a`, where
`K_a=2P(a,a)/(3a-1)`. Symmetry gives the exact decomposition

```
P(a,a)-P(a-1,a-1)
 = Delta_{a,a-1} + Delta_{a-1,a-1}
 >= K_a+K_{a-1}.
```

Substitution of the two diagonal values and rearrangement yields
`K_a >= ((3a-2)/(3a-3))*K_(a-1)`. Since `K_1=1`, induction gives
`K_a>=h_a` for the stated recurrence. For `b>=a`, summing increments from
the diagonal gives

```
P(a,b) >= P(a,a)+(b-a)*ell_a
        >= h_a * (b+(a-1)/2) = P_*(a,b).
```

Symmetry handles `b<a`. The limit step is valid because the proof first
establishes a full limit, not only a subsequential slope.

## Matching profile audit

Symmetry, positivity, and `P_*(1,b)=b` follow from the definition and
`h_1=1`. For `b>=a+1`, the profile is affine in `b`. At the joining index
`b=a`, the second difference is

```
((3a-3)/2)*h_a - ((3a-2)/2)*h_(a-1) = 0,
```

by the recurrence. For `2<=b<a`, direct substitution gives the nonnegative
second difference

```
2*h_b*(a-b)/(3*b*(3*b-2)).
```

Thus the join and every required concavity index are covered, including the
small cases `a=1` and `a=2`.

For shifted tripling, `3b+a-1>=a`, so its profile value is
`3*h_a*(b+(a-1)/2)`. This is equality when `b>=a`. For `b<a`, the remaining
comparison is
`h_a*(a+2b-1)/(2a+b-1) >= h_b`. The ratio at `a=b` is `h_b`; its step ratio
has positive denominator and numerator difference
`2*(a-b)*(a-b+1) >= 0`. This proves the inequality on the full integer
range.

For the rank envelope, induction from `h_1=1` uses

```
27*a^3*(3*a+2) - (3*a+1)^3*(3*a-1) = 6*a+1 > 0
```

to show `h_a^3 <= (3a-1)/2`. When `b>=a`, both factors
`(3a-1)/2` and `b+(a-1)/2` are bounded by `a+b-1`; symmetry handles the
other half. The replication argument follows from

```
(1+1/(3a))^3-(1+1/a)=(9a+1)/(27a^3)>0
```

and `qb+(qa-1)/2 >= q*(b+(a-1)/2)`.

## Attribution and evidence boundary

The product recurrence originates in the cited OpenAI manuscript; the local
proof does not claim otherwise. The exact least-profile formula and
pointwise-minimality proof also appear in Rohan Arun's earlier pinned
repository revision (`0b09d3616da31d8750366747d7821d70ae6d1b90`,
`proof.tex`, Section 4), documented in [`docs/external_followups.md`](../../../docs/external_followups.md).
The local October 20 derivation is therefore not a priority claim. This review
checks its algebra and scope; it does not establish historical priority.

The existing exact-rational verifier is only a finite sanity check. The
general conclusion above rests on the all-integer argument, not on a grid or
test count.
