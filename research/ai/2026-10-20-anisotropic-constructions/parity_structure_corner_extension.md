# Exact corner splits and a scalar supplied by A(2,3)

October 21, 2026. Monomial ordinary restrictions, verified coefficient
by coefficient. No improved matrix multiplication exponent is claimed.

## General split

Let all six integers below be positive, with s,c<=a and t,d<=b. If

\[
s+t+c+d\le a+b+1,
\tag{1}
\]

then there is an exact monomial restriction

\[
A(a,b)\longrightarrow A(s,t)\oplus A(c,d).
\tag{2}
\]

Put the first block in the low-degree corner: retain its usual short
indices in [0,s) and [0,t), and its long indices in [0,s+t-1). Put the
second block in the opposite corner, shifting its first short index
by alpha=a-c, its second short index by beta=b-d, and every long index
by alpha+beta. The two long intervals are

\[
[0,s+t-2],\qquad [a+b-c-d,a+b-2].
\]

They are disjoint, in increasing order, by (1). The all-first-block
and all-second-block terms give the two indicated sources exactly.

A mixed coefficient with one second-block row and two first-block
rows vanishes at the edge of the second-block long index. That long
index is at least a+b-c-d, while the two first-block short indices sum
to at most s+t-2. For a coefficient with two second-block rows and
one first-block row, use the edge at the first-block long index: the
two second-block short indices sum to at least a+b-c-d, exceeding
the first-block long range. These cover every mixed cyclic placement.
No disjointness of the short coordinate ranges is required.

## The A(2,3) scalar extension

The smallest useful instance is

\[
A(2,3)\longrightarrow A(2,2)\oplus\langle1\rangle.
\tag{3}
\]

Keep the standard A(2,2) coordinates, with both short indices below
two and long index below three. Append the three coordinate selectors

\[
X(1,3,2),\qquad Y(2,1,3),\qquad Z(3,2,1).
\]

Their coefficient is one. The disjoint-interval argument proves that
all coefficients mixing one of them with the A(2,2) block vanish.
The exact image has 64+1=65 terms in format 13 by 13 by 13.

This supplies the additional scalar used in
`parity_balancing_spin1.md`, whose separately verified construction
takes A(2,2) plus one scalar to M3. The present file verifies (3);
that other construction is not assumed in its coefficient replay.

Other checked instances are

\[
\begin{aligned}
A(3,3)&\longrightarrow A(2,2)\oplus A(1,2),\\
A(4,5)&\longrightarrow A(3,3)\oplus A(2,2),\\
A(5,6)&\longrightarrow A(4,4)\oplus A(2,2).
\end{aligned}
\]

Here A(1,2) is M2 after transposing the second target leg's two matrix
indices. Thus the first line also supplies A(2,2) plus M2. More
generally, (2) gives A(a,b) to A(a-1,b-1) plus M2 whenever a,b>=2,
by taking the second block to be A(1,2).

## Files and verification

`parity_structure_corner_extension.py` constructs the selector maps
for (2) and checks the complete source image in all four examples.
`parity_structure_corner_extension_certificate.json` records the
formats, degree intervals, and coefficient counts.

`parity_structure_corner_extension_a23_maps.npz` exports the maps for
(3). Its A,B,C arrays have shape (13,24), all entries are zero or one,
and x,y,z are aliases. Rows 0 through 11 use the standard lexicographic
A(2,2) order; row 12 is the scalar. This order allows direct composition
with a map whose input is A(2,2) followed by one scalar.

Run from the repository root:

```
python research/ai/2026-10-20-anisotropic-constructions/parity_structure_corner_extension.py
```

All maps in this file are ordinary coordinate restrictions. Their
existence does not prove any unconstructed larger matrix target.
