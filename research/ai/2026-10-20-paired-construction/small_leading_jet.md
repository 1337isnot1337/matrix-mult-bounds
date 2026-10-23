# A smaller leading seed and its first-jet equations

## Exact seed and scope

The k=2 member of `outer_product_injection.py` gives
Q(3,2) to M(2,4,2). Embed its B and C maps into Q(6,4) by
retaining only source inner indices 0,1 and convolution output
indices 0,1,2,3. All other columns are zero. The leading target B
and C spaces each have dimension eight. Their full source A slice
space has rank 16, with active source coordinates p,q<4.

Add one scalar source D1, and choose its leading B and C images to
duplicate the rank-one ghost slice A33:

\[
b_{s,0}=B_0(B_{0,3}),\qquad c_{s,0}=C_0(C_{3,0}).
\tag{1}
\]

The rank remains 16. Its first-leg kernel K0 has the explicit basis

\[
\{A_{p,q}:0\le p,q<6,\ p\ge4\text{ or }q\ge4\}
\cup\{e_s-A_{3,3}\}.
\tag{2}
\]

This is a 21-dimensional kernel. The full M(5,4,5) target needs
25-4=21 slice directions outside the old M(2,4,2) support, so the
saturated dimension requirement is tight: 16+21=37, the source
first-leg dimension after adding D1.

The exact first-jet calculation below excludes the monomial extension
of this fixed seed in which new target outer B/C modes have order t,
edge A rows have order t^-1, and corner A rows have order t^-2.
It does not exclude different leading maps or arbitrary higher-order
valuation patterns. No full M5 restriction or omega improvement is claimed.

## Why the scalar lead is placed in old support

If both scalar long-leg maps vanish at t=0 and their first nonzero
images lie in the new target outer modes at order t, the scalar
would contribute a rank-one new/new slice at order t^2. In the tight
dimension case, the nine-dimensional corner quotient must be exactly
Mat_3 tensor I_4. Every nonzero matrix in that quotient has rank
at least four. Thus a new-only scalar contribution cannot fill a
corner direction in this monomial chart. Placement (1) avoids that
immediate contradiction by making the scalar kernel generator a
difference with an existing source slice.

## The required first saturation

Write S_r for the coefficient of t^r in the source slice map after
the B and C maps. Let E_cross denote the 12-dimensional cross slice
space of M5, with one outer index old (0,1) and the other new
(2,3,4). For the stated monomial powers, the necessary conditions are

\[
S_1(K_0)=E_{\rm cross},\qquad
\dim\ker(S_1|_{K_0})=9,
\]

followed by a second-order map from that nine-dimensional kernel
onto the new/new corner space Mat_3 tensor I_4. These statements are
understood after projection away from the old/old support. Optional
first-order changes in old target rows do not change these cross blocks.

The first requirement already fails for the fixed seed.

## Exact zero of the aligned B edge map

Fix one new outer B row, comprising four middle coordinates, and
let B1 denote its arbitrary first-order coefficients on all 37
source B variables. For q=4 or 5 and p=3, the old C map leaves only
the two independent vectors C0(C_(3,0)) and C0(C_(3,1)). Hence

\[
S_{1,B}(A_{3,q})=
B_1(B_{0,q})\otimes C_0(C_{3,0})+
B_1(B_{0,q+1})\otimes C_0(C_{3,1}).
\]

This matrix has rank at most two. If it belongs to the prescribed
M5 edge fibre, every nonzero member has rank four. It must therefore
vanish, forcing B1(B_(0,s))=0 for s=4,5,6.

Now descend through p=2,1,0. All terms with earlier source y have
already vanished. At each step only the same two-dimensional C
fibre remains, forcing the next B1 row to vanish at s=4,5,6. Thus

\[
B_1(B_{y,s})=0\qquad(0\le y<4,\quad s=4,5,6).
\tag{3}
\]

For the final kernel generator delta=e_s-A33, these conditions give

\[
S_{1,B}(\delta)=
(B_1(e_s)-B_1(B_{0,3}))\otimes C_0(C_{3,0}).
\]

Its rank is at most one, so alignment again forces zero and

\[
B_1(e_s)=B_1(B_{0,3}).
\tag{4}
\]

Conditions (3),(4) kill the B cross image of every vector in (2).
The C argument is the transposed statement:

\[
C_1(C_{z,v})=0\quad(z=4,5,6,\ 0\le v<4),\qquad
C_1(e_s)=C_1(C_{3,0}).
\tag{5}
\]

Thus every aligned first cross jet is zero. Its possible rank is
zero rather than the required 12.

## Complete linear certificate

For one new outer B row, there are 4 times 37 = 148 unknown
coefficients. The program writes all 203 nonzero equations expressing
alignment of the 21 kernel slices with the two-dimensional MM edge
fibre. Exact rational elimination gives rank 52 and nullity 96.
The 52 independent conditions are precisely the 48 scalar zero
conditions in (3) and four scalar copy conditions in (4). Every
allowed edge coefficient is zero on the complete nullspace. The
C system gives the same ranks and the conditions (5).

The saved certificate includes the full initial maps, all 21 kernel
generators, a nonzero 16 by 16 leading-rank minor, every linear
equation, and a complete rational nullspace basis. It also checks
all 256 coefficients of the leading M(2,4,2) identity. These are
exact checks of the specified chart; they do not make a claim about
unsearched leading maps.

```bash
python research/ai/2026-10-20-paired-construction/small_leading_jet.py
python -m unittest discover -s tests -p test_small_leading_jet.py -v
```
