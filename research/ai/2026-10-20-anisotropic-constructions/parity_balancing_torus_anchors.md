# Exact endpoint equations for the A(8,8) torus search

## Status and scope

`parity_balancing_torus_anchors.py` constructs three rational maps from the
960-coordinate legs of A(8,8) to the 778-coordinate legs of
M27 plus M7. The current maps have denominator 64 and 782 nonzero entries
per leg. Every map has row rank 778 over the rationals.

The exported seed satisfies two sets of exact identities:

1. Every coefficient containing either extreme target matrix unit, of
   weight +14 or -14, equals the corresponding M27 plus M7 coefficient.
   This includes all required zero coefficients, on all three legs.
2. Its restriction to the four M27 vertices of charges 0, 1, 13 and 14 is
   the full M4 tensor: all 4,096 coefficients agree, with 64 nonzero terms.

**The full M27 plus M7 identity is not established. This is a partial
construction and does not improve the matrix multiplication exponent.**
The finite exact checks below do not certify that the fixed boundary can
be completed. Additional equations can obstruct a partial construction.

The first version used a Hadamard factorization at charges 1 and 13.
It passed the same six extreme-slice equations, but a separate exact
pair-functional relation proved that its fixed boundary cannot be
completed. Its original bytes are retained in
`parity_balancing_torus_anchor_hadamard_seed.json`, SHA256
`f248587f5e56bb884a63ce49a74dca1125e30c1c7d78545cbd74d3604fb843cf`.
This historical file is a nonextendable positive control for the partial
equations. The default `parity_balancing_torus_anchor_seed.json` instead
uses the M4-compatible endpoint choices described below.

The endpoint M4 construction and the corrected charge-1 and charge-2
channel choices were supplied by the parent worker in
`monotone_endpoint_seeds.md`. The common physical coordinate convention,
six-slice replay and original endpoint logic were checked by a second
agent in this generating session; no external independent review or
formalization has occurred. The present checker directly replays the
corrected maps and their ranks.

## Source coordinates and trace convention

Write a source matrix as

\[
 W(F)_{(i,q),(p,s)}=F_{i,p+q,s},\qquad 0\le i,p,q,s<8.
\]

Its 960 coordinates are `F(i,k,s)`, with `0 <= k < 15`, flattened as
`(15*i+k)*8+s`. Their torus weights are `i+s-k`.
The source tensor is the cyclic matrix trace of three such matrices
after the following coordinate identifications:

| Leg | Original source column corresponding to common F(i,k,s) |
| --- | --- |
| X | `(15*i+k)*8+s` |
| Y | `(8*s+i)*15+k` |
| Z | `(8*k+s)*8+i` |

Indeed, one trace term has coefficients
`F_X(i,p+q,s) F_Y(p,r+s,j) F_Z(r,i+j,q)`, which are exactly the original
source indices `X(i,p+q,s) Y(j,p,r+s) Z(i+j,q,r)`.

The first target block has vertex-charge multiplicities

\[
 (1,1,2,2,2,2,2,3,2,2,2,2,2,1,1)
\]

at charges 0 through 14. The second block has one vertex at each charge
0 through 6. A target matrix unit has weight equal to its row charge
minus its column charge. Rows are ordered block first, then matrix row
and column. Thus M27 occupies rows 0 through 728 and M7 rows 729 through
777. The extreme M27 vertices are `L=0` and `H=26`.

## The endpoint factorization equations

Put `u=e_(7,0)` and `v=e_(0,7)` in the 64-dimensional physical space.
The unique source matrices of weights +14 and -14 are

\[
 W_+=E_{u,v}=W(F(7,0,7)),\qquad
 W_-=E_{v,u}=W(F(0,14,0)).
\]

Map `E_(H,L)` and `E_(L,H)` to these matrices with coefficient one. For
the positive extreme, the remaining equation is

\[
 \operatorname{tr}(W_+J(B)J(C))
 =e_v^T J(B)J(C)e_u
 =\sum_{t=0}^{26} B_{L,t}C_{t,H}.
\]

For vertices of charge q, the intermediate physical space has charge
`q-7` and dimension `d_q=8-|q-7|`. Choose its basis in lexicographic
physical-index order. Let `R(q)` be the list of target linear forms in
the row `e_v^T J`, and let `C(q)` be the corresponding list in `J e_u`.
The required identity is

\[
 \sum_{h=1}^{d_q}R(q)_h(B)C(q)_h(C)
 =\sum_{t:\,\mathrm{charge}(t)=q} B_{L,t}C_{t,H}.
\]

Source membership identifies some coordinates of these lists. For
`q <= 7`, the first channels of `R(14-q)` and `C(q)` are the same source
coordinate `F(0,14-q,0)`. The construction enforces this equality rather
than prescribing independent physical rows and columns.

At q=0 and q=14, use the direct endpoint terms. At q=1 and q=13, let
`t1` and `t13` denote the unique corresponding vertices and put

\[
\begin{aligned}
 R(1)&=(0,B_{L,t1}), & C(1)&=(C_{L,t13},C_{t1,H}),\\
 R(13)&=(B_{L,t13},0), & C(13)&=(C_{t13,H},0).
\end{aligned}
\]

Both products are the required ones, and the shared source channel is
the target form at `(L,t13)`. These are the actual physical channels of
the endpoint M4 construction.

For q=2, write `a1,a2` for the forms `(L,t)` at charge 12,
`b1,b2` for `(t,H)` at charge 2, `u1,u2` for `(L,t)` at charge 2,
`c1,c2` for `(t,H)` at charge 12, and `s` for `(t1,t13)`. The same
notation denotes a form on whichever leg is being evaluated. Set

\[
\begin{aligned}
 R(12)&=(b1,a1,a2), & C(2)&=(b1,s,b2),\\
 R(2)&=(u1,0,u2), & C(12)&=(0,c1,c2).
\end{aligned}
\]

The two products are `u1*b1+u2*b2` and `a1*c1+a2*c2`. The shared first
channel is `b1`; the form `s` occupies its required M4 coordinate
`F(1,13,0)` rather than the shared coordinate.

For q=3 through 6, use a shared target form in channel zero, the
required dot-product forms in the next `c_q` channels, and disjoint
extra forms in the remaining high-row and low-column channels. Their
partners are zero on these extra channels. The exact finite choices
are exported in `high_low_slack_channels`. At q=7, use two channels
`(s,s)` on the row and `(s,-s)` on the column. Their products cancel,
while three separate channels carry the required dot product.

Finally reverse both physical indices,

\[
 F(i,k,s)\longmapsto F(7-i,14-k,7-s),
\]

and reverse the target vertices within each block. This is a physical
matrix conjugation and preserves trace. It supplies the negative
extreme equations. The constructor rejects any incompatible assignment
on a shared source coordinate. All three common-order maps initially
agree, so the positive and negative identities hold cyclically on all
three legs.

## The full embedded M4

Use the four physical vertices

\[
 ((0,7),(1,7),(6,0),(7,0)).
\]

For physical vertices `s=(i_s,q_s)` and `t=(i_t,q_t)`, the exact M4
construction maps their matrix unit to
`F(i_s,q_s+i_t,q_t)` with coefficient one. The corrected endpoint
channels above agree with all its boundary coordinates. Add the two
free diagonal entries

\[
 E_{t1,t1}\mapsto F(1,8,7),\qquad
 E_{t13,t13}\mapsto F(6,6,0).
\]

These assignments give all 16 source rows of that M4 construction.
The seed's remaining row-rank completion uses other free coordinates.
The verifier independently contracts all 262,144 source terms on these
16 target rows per leg and checks the complete 16 by 16 by 16 tensor.
This embedded M4 is an exact initial control. Arbitrary later changes
to free coefficients in its target rows need not preserve it.

## A genuine affine family preserving the six extreme slices

The fixed source boundary is the union

\[
\begin{aligned}
 &F(0,7+p,s),\quad F(7,p,s),\\
 &F(i,7+q,0),\quad F(i,q,7),\qquad 0\le i,p,q,s<8.
\end{aligned}
\]

It has 238 coordinates. The four sets each have size 64; their four
row/column intersections have sizes 8, 1, 1 and 8, with no triple
intersection. The complement has 722 coordinates.

Every matrix from the complement has zero rows and columns at both
physical endpoints `u` and `v`. Consequently, **none of these 722 free
source coordinates ever occurs beside an extreme source point in any
source tensor term**. This also follows directly from
`tr(E_(u,v) K L)=0` when `K` has zero row `v`, and from the analogous
column statement. All cyclic positions and both endpoints obey the
same argument.

Therefore arbitrary, independent changes on the free columns of each
map preserve every one of the six extreme-slice identities. Restricting
changes to equal torus weights gives 94,698 complex map coefficients
in total. Conciseness holds on an open subset containing the exported
seed; it is not asserted for every free assignment. If one also wishes
to preserve the embedded M4, its free target-row coefficients require
additional constraints or a separate freeze.

## Exact replay and rank acceptance

The checker uses only Python's standard library. It checks exactly three
maps, a positive integer denominator, all integer entry ranges, torus
weights, duplicate entries, and the consistency of the optional common
coordinate copy with the three actual exported maps. It derives the
boundary and complement independently from the four formulas above.

For each actual leg and each of its 29 target weights, it performs
Gaussian elimination on the integer numerator matrix modulo 65,521.
Every block has full target row rank; their ranks sum to 778 on each
leg. A nonzero minor modulo a prime is a nonzero integer minor, so this
certifies full row rank over the rationals. Stored rank summaries are
not used for acceptance.

The tensor replay enumerates all 262,144 source terms. Each of the six
extreme slices contains 64 source terms. Integer contraction gives
exactly 27 target coefficients equal to `64**3`, and every other
coefficient is zero. It also confirms from the enumerated support that
no free column occurs beside an extreme source point.

Focused tests replay the current and historical seeds, reject a changed
corner coefficient, reject an omitted free-only target row despite
unchanged rank metadata, reject all-zero maps, and reject malformed
entry data. A positive free-coefficient perturbation verifies that the
claimed affine freedom is real.

```bash
python -S research/ai/2026-10-20-anisotropic-constructions/parity_balancing_torus_anchors.py
python -S -m unittest discover -s tests -p test_parity_balancing_torus_anchors.py -v
```

The complete sparse maps and replay report are in
`results/anisotropic-constructions-2026-10-20/parity_balancing_torus_anchor_seed.json`.
The historical Hadamard input retains its original metadata for byte
preservation; the current verifier recomputes its actual ranks as well.
