# What the generalized packing rule adds to the scalar program

October 21, 2026. Source update and a written scalar deduction, checked
by another agent in the same generating session. No exponent improvement
or independent mathematical review is asserted.

## New external source

Rafael Pass, *Matrix Multiplication from Polynomial Packings: A
Constructive and Elementary Proof of omega <= 9/4*,
[arXiv:2610.28627v1](https://arxiv.org/html/2610.28627v1), submitted
October 20, 2026, gives a constructive route to the existing bound.
Lemma 2.4 has positive integer parameters a,b,c,t with
`ct >= a+2b-1`. It packs c+1 full products and one middle product,
sharing the left polynomial, into c full source products whose right
length grows from b to b+t. The subsequent construction combines
primal and dual maps and separates shared inputs.

The packing maps and constructive exponent theorem belong to that
paper. This note examines only the following scalar update suggested
by its source and target counts:

\[
cP(a,b+t)\ge(c+2)P(a,b),\qquad ct\ge a+2b-1.
\tag{1}
\]

The full tensor maps contain information beyond this scalar projection.
No equivalence of tensor constructions is claimed.

## Concavity and shifted tripling already imply the update

Fix a positive integer a. Suppose P(a,b) is positive and discretely
concave in the positive integer b, and satisfies

\[
P(a,3b+a-1)\ge3P(a,b)
\tag{2}
\]

for every positive integer b. These are the existing assumptions in
the [archived scalar analysis](../2026-10-20/research_note.md).

For positive integers b,t, set d=(a-1)/2 and

\[
B_k=3^k(b+d)-d.
\]

The number B_k is an integer: 3^k-1 is even. Iterating (2) gives
`P(a,B_k) >= 3^k P(a,b)`. Choose k with B_k >= b+t.
Discrete concavity places every intermediate integer value above
the chord from b to B_k. Consequently

\[
\begin{aligned}
P(a,b+t)
&\ge P(a,b)+\frac{t}{B_k-b}
       \bigl(P(a,B_k)-P(a,b)\bigr)\\
&\ge\left(1+\frac{t}{b+d}\right)P(a,b).
\end{aligned}
\tag{3}
\]

Here `B_k-b=(3^k-1)(b+d)`. No differentiability, real-argument
extension, or limiting slope is needed. If `ct >= a+2b-1`, then
`ct >= 2(b+d)`, so (3) implies (1) with the finite offset retained
exactly.

Conversely, choosing c=1 and t=a+2b-1 in (1) gives (2).
Thus, in the presence of discrete concavity, the entire family (1)
is equivalent to shifted tripling. Varying c and t in this scalar
rule does not strengthen the existing feasible set.

The same conclusion also follows from the slope inequality (8) in
the archived note. This is an application of that earlier argument,
not a new source of historical priority.

## Equality controls and the remaining construction question

For b>=a the existing feasible profile is

\[
P_*(a,b)=h_a\left(b+\frac{a-1}{2}\right).
\]

Whenever positive integers c,t meet `ct=a+2b-1`, it has exactly

\[
\frac{P_*(a,b+t)}{P_*(a,b)}=1+\frac2c.
\]

For example, a=b=4, c=11, t=1 gives ratio 13/11. Since
`h_4=140/81`, the two profile values are 770/81 and 910/81.
These rational values saturate the candidate update. The offset -1
does not itself produce a strict gain at the endpoint.

This conclusion concerns the scalar family (1). It does not rule out
using the external packing maps in a coupled tensor construction,
changing the source, retaining additional information, or deriving
another inequality. A successful improvement needs such additional
content; merely adding (1) to the existing concavity program cannot
remove its already certified feasible profile.
