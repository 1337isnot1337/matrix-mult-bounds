# Full first-leg response of the saved eleven-channel module

Research calculation, October 21, 2026. This note concerns the **particular
saved rational maps** in [the eleven-channel witness](../../../results/anisotropic-constructions-2026-10-20/crossed-module11-witness.json)
and [their matched full-source lift](parity_balancing_cross_module_lifts.md).
Their full first-leg response in $A(8,8)$ has rank exactly $256$.
Consequently they cannot be held fixed while extending that rectangular
core to $M_{27}$ or $M_{27}\oplus M_7$ by ordinary maps. Other module maps,
mixed-copy constructions, and arbitrary degenerations remain open.

## 1. The full response

Write the source coordinates as $F(i,k,s)$, with $0\le i,s<8$ and
$0\le k<15$. The source coefficients are

\[
 X(i,p+q,s)Y(p,r+s,j)Z(r,i+j,q).
\]

The saved lift puts the two non-first maps at

\[
 Y_{u\alpha,(L,j)}\mapsto F(2p,e+2L,j),\qquad
 Z_{i\beta,(a,H)}\mapsto F(e+2a,H,t),
\]

where $p,t,e$ are binary, $0\le L<5$, $0\le a<4$,
$0\le j<8$, and $0\le H<9$. Its target is $M(4,4,22)$.
Fix both maps and let the full $960$-dimensional first source space vary.
Denote the resulting linear map by $\Psi$.

The only active first middle coordinates are $k=2p+t$, hence $k=0,1,2,3$.
These four choices act in disjoint output blocks, indexed by $(p,t)$.
Each output block has $44$ rows and $44$ columns. Each corresponding
source block has $64$ coordinates $(i,s)$, so

\[
 \operatorname{rank}\Psi\le4\cdot64=256.
 \tag{1}
\]

All four blocks have identical coefficient matrices. Reorder a target
row within a block as $(e_Y,y)$ with $0\le y<22$, and a target column
as $(e_Z,z)$ with $0\le z<22$. Their coefficient on $F(i,k,s)$ is zero
unless $e_Y\equiv e_Z+s\pmod2$. Otherwise put
$h=(e_Z+s-e_Y)/2$; the coefficient is

\[
 \sum_{\substack{0\le a<4,\ 0\le j<8\\
                  0\le a+h<5,\ i+j<9}}
 Y_{y,\,8(a+h)+j}\,Z_{z,\,9a+i+j}.
 \tag{2}
\]

The verifier rebuilds a specified $64\times64$ minor of this response
directly from the saved rational maps. After clearing their common
denominator $2860\cdot8=22880$, its determinant is nonzero modulo
the prime $65521$. This proves the rational rank lower bound $64$ in
each block. The disjoint supports and (1) therefore give

\[
 \operatorname{rank}\Psi=256,\qquad\dim\ker\Psi=704.
 \tag{3}
\]

## 2. Exact scope of the extension obstruction

Embed the rectangular core in a prospective square matrix tensor using
four row vertices, four column vertices, and its $22$ middle vertices.
Only the $16$ first-leg units joining the chosen row and column vertices
have nonzero contractions with the fixed other two core spaces.
Every remaining first-leg unit of the square target must lie in
$\ker\Psi$. Every first-leg unit from a different direct-sum component
must also lie there.

For a concise target with common leg dimension $D$, the images of those
$D-16$ first-leg units must be independent. Equation (3) requires

\[
 D-16\le704,\qquad D\le720.
 \tag{4}
\]

The dimensions $27^2=729$ and $27^2+7^2=778$ both violate (4).
Equivalently, the corresponding first response would have needed rank
at most $247$ or $198$, respectively. This argument retains the saved
other-leg maps exactly. It does not prohibit replacing them with maps
whose response has smaller rank, or using a singular construction.

## 3. Replay and next construction requirement

The minor certificate contains $64$ output column indices. The replay
uses only Python integers and independently checks the four-block
support decomposition:

```bash
python -S research/ai/2026-10-20-anisotropic-constructions/crossed_module_response.py
```

The matrix entries are regenerated, rather than accepted from stored
rank metadata. The separate [four-factor flattening proof](parity_balancing_crossed_flattening.md)
also excludes reaching the larger square target when the original
sixteen first images stay fixed, even if the other maps change.
A useful replacement must therefore change the first map as well.
The [exact corner extension](parity_structure_cross_module_corner.md)
does so and lowers the response rank to 186, but supplies only a
twelve-channel rectangular core. These are assembly conditions;
the square-target maps remain missing.
