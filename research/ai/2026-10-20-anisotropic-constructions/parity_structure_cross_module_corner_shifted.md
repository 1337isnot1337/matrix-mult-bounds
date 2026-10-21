# Translating the corner reduces the response to 164

The [changed-core twelve-channel construction](parity_structure_cross_module_corner.md)
admits two integer offsets $0\le h_i,h_s\le4$. Replace only its added
corner maps by

\[
\begin{aligned}
E_{I,J}&\mapsto F(h_i+I,14,h_s+J),\\
E_{J,*}&\mapsto F(7,7+h_s+J,7),\\
E_{*,I}&\mapsto F(7,7+h_i+I,7).
\end{aligned}
\]

The first displayed term is added to the unchanged canonical first
map, as in the original construction. All indices lie in $A(8,8)$.
The old/new mixed terms still have long indices 7, 8, or 9 and hence
vanish against that first map. Two new maps force exactly the shifted
first coordinate. Thus the complete restriction to $M(4,4,12)$ persists.

The old/old response remains supported on 128 coordinates. The
old/new mixed response now has $i\in\{h_i,\ldots,7\}$, $s=1$ at
$k=7,9$. The new/old mixed response has $i\in\{0,1\}$,
$s\in\{h_s+1,\ldots,7\}$ at $k=7,8$. The new/new response has the
sixteen shifted coordinates at $k=14$.

For $(h_i,h_s)=(4,4)$ the mixed sets at $k=7$ are disjoint. The exact
support counts are 32 at each of $k=0,1,2,3$, followed by 10, 6, 4, and
16 at $k=7,8,9,14$. Their sum is **164**. The complete response has
rank 164 modulo 65521, which proves that this support bound is attained
over the rationals. Its kernel therefore has dimension 796.

The first-core four-factor flattening still has rank $360+121=481$.
The corner convolution output intervals are translated, each retaining
eleven independent rows. The exact verifier also checks the 481
distinct, pairwise disjoint indicator-row patterns in the actual
flattening, without assuming the formula.

The stored maps pass the complete integer replay of all 262,144 source
terms and all 36,864 target coefficients. There are exactly 192 desired
unit coefficients and no others. The original response-186 package is
retained unchanged; this file describes a separate actual export.

The fixed-other-map dimension test now gives $D\le960-164+16=812$.
Both that test and the fixed-first-core flattening test permit the
proposed $M_{27}\oplus M_7$ extension. They do not construct it. No
smaller exponent is established.

```bash
python -S research/ai/2026-10-20-anisotropic-constructions/parity_structure_cross_module_corner_shifted.py
```
