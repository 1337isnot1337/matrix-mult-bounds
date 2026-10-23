# A copywise dimension obstruction

Date: 2026-10-23. Owner-directed AI deduction supplied by the coordinating
agent. Written and unreviewed.

The source has ten Full(5,10) blocks, each with nonshared dimensions (10,14).
Suppose a proposed construction assigned each complete target block to one
source copy and used separate B and C subspaces inside that source copy.
This includes coordinate partitions and more general copy-preserving block
allocations on both nonshared legs.

Since the total target B and C dimensions exactly exhaust the source
dimensions, every copy would have to accommodate its assigned target blocks
with total dimensions exactly (10,14). Let x,y,z,w,v count, respectively,
Full(5,2), Full(5,3), O(3,3), O(4,2), and Mid(5,2) in one copy. These
nonnegative integers must satisfy

\[
2x+3y+3z+4w+6v=10,\qquad
6x+7y+3z+2w+2v=14.
\tag{1}
\]

Subtracting the equations gives

\[
w=2(x+y-v-1).
\tag{2}
\]

If w>=2, then x+y>=v+2. The first equation in (1) would have left side at
least 2(x+y)+4w+6v>=12+8v>10, impossible. Equation (2) makes w even, so
w=0 and x+y=v+1. Substitution into the B equation leaves

\[
2+y+3z+8v=10.
\tag{3}
\]

If v=0, then y<=1 while y+3z=8, which is impossible modulo three.
If v=1, equation (3) forces y=z=0, and then x=2. Values v>=2 are
impossible. Thus the only dimension-compatible allocation to one source
copy is

\[
(x,y,z,w,v)=(2,0,0,0,1).
\tag{4}
\]

Ten copies of (4) cannot equal the frozen target counts (7,10,4,2,6).
Consequently no assignment of whole target blocks to separate source copies
can realize the candidate, even before tensor coefficients are considered.

This is a construction limitation for the stated allocation class. It does
not obstruct arbitrary degeneration maps. Such maps may mix source copies
on the long legs, and that possibility remains part of the open question.
The exact finite control enumerates all 576 tuples permitted by the B
dimension bounds and recovers only (4).

