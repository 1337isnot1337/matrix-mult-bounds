# An auxiliary corner with vanishing mixed responses

## Status and purpose

Claim ID: **AI-SPIN-SCALAR-CORNER-125**.

This note constructs an exact auxiliary tensor M(1,1,9) in A(8,8).
Its three full response ranks are (15,9,9). All six mixed response
maps vanish against explicitly stated, much larger coordinate spaces.
Consequently it can cancel nine copies of a shared-first-factor scalar
error without creating cross terms. The required reduced-source map
with that scalar error has **not** been constructed.

The corner identity, mixed-response argument, and conditional completion
below are local work from this owner-directed research session. The
source convention and the response-space method are adopted from the
[existing assembly package](parity_balancing_spin_assembly.md); no
priority is claimed for these definitions or elementary coordinate
separation. A second agent independently rebuilt all original source terms, the
three ranks, six mixed responses, and the residue lift; its separate
`spin_scalar_corner_audit.py` imports no verification helper. The written
proof has no external independent review.
No exponent below 9/4 follows from this package.

## 1. Source and core ambient spaces

Every leg of A(8,8) has coordinates F(i,k,s), with
0 <= i,s < 8 and 0 <= k < 15, flattened as (15i+k)8+s.
The tensor is

\[
 T=\sum_{i,p,q,r,j,s=0}^{7}
 X(i,p+q,s)Y(p,r+s,j)Z(r,i+j,q).
 \tag{1}
\]

Thus there are 262,144 original unit source terms and 960 coordinates
on each leg. The order of the third coordinate is (r,H,q) in this
note; implementations using (q,r,H) must apply the corresponding
permutation.

Allow arbitrary retained maps supported on the following ambient spaces:

| Leg | Allowed original coordinates | Dimension |
| --- | --- | ---: |
| X | F(i,k,s), k <= 2 | 192 |
| Y | F(p,L,j), p <= 1 and j <= 5 | 180 |
| Z | F(r,H,q), r <= 5 and q <= 1 | 180 |

The unrestricted coordinates in this table range over their entire
original intervals. These are support hypotheses on the core maps,
not assumptions about a matrix tensor already being present.

## 2. A twelve-channel corner

Let the twelve labels alpha=(p,r,j) range lexicographically over

\[
 \{5,6,7\}\times\{6,7\}\times\{6,7\}.
\]

Take one first row and twelve rows on the other two legs:

\[
 x_*=F(7,12,7),\qquad
 y_\alpha=F(p,7+r,j),\qquad
 z_\alpha=F(r,7+j,12-p).
 \tag{2}
\]

These denote coefficient rows: the listed source coordinate is sent
to the corresponding target variable, and other coordinates are zero.
For a term of (1) using x_*, the equations for the outer and long
coordinates force the Y and Z labels to be equal. Conversely each
equal pair contributes exactly once. Therefore

\[
 T(x_*,y_\alpha,z_\beta)=\delta_{\alpha,\beta}.
 \tag{3}
\]

This is M(1,1,12). Selecting the same nine labels on both other legs
gives M(1,1,9).

### All mixed responses vanish

A full response leaves one entire original source leg free and
contracts the other two legs. In particular, vanishing of a full
mixed response is stronger than testing it only on the retained third
map. The six cases follow directly from (1):

| Free leg | Fixed core leg | Fixed corner leg | Impossible source condition |
| --- | --- | --- | --- |
| X | Y | Z | H >= 13 and j <= 5 force i=H-j >= 8 |
| X | Z | Y | L >= 13 and r <= 5 force s=L-r >= 8 |
| Y | X | Z | k <= 2 and q >= 5 force p=k-q < 0 |
| Y | Z | X | k=12 and q <= 1 force p=k-q >= 11 |
| Z | X | Y | k <= 2 and p >= 5 force q=k-p < 0 |
| Z | Y | X | k=12 and p <= 1 force q=k-p >= 11 |

There is no contribution even before cancellation. By linearity this
holds for every choice of core maps in the stated ambient spaces and
every linear combination of the corner rows. When core and corner
rows are added, the full tensor and each response matrix are sums of
their pure core and pure corner contributions.

## 3. Exact response cost and nine-channel choice

For a Y label alpha=(p,r,j) and Z label beta=(P,R,J), the only possible
free first coordinate is

\[
 (i,k,s)=(7+J-j,\;12+p-P,\;7+r-R).
 \tag{4}
\]

It contributes precisely when i and s lie in [0,7]. Each output pair
(alpha,beta) occurs in exactly one response column. Hence different
nonzero columns have disjoint supports, all entries are one, and
choosing one output pair from each column gives an identity minor.
The first response rank is exactly the number of distinct coordinates
in (4). There are twenty for all twelve channels. On the other legs,
the fixed first row pairs each retained channel with its unique source
coordinate, giving ranks twelve and twelve.

The exported nine-channel selection has zero-based label indices

\[
 (0,1,3,4,5,6,7,8,11).
 \tag{5}
\]

Its first response support is

\[
\begin{split}
 &(6,10,7),(6,11,6),(6,11,7),(6,12,6),(6,12,7),(6,13,7),\\
 &(7,10,6),(7,10,7),(7,11,6),(7,11,7),(7,12,6),(7,12,7),\\
 &(7,13,6),(7,13,7),(7,14,7).
\end{split}
\]

Thus its exact response ranks are (15,9,9). The certificate exports
all integer maps and all identity-minor pivots, and reconstructs the
responses from the complete original source rather than relying on
formula (4) alone.

An exhaustive scan of the 220 common nine-label subsets has histogram:

| First response rank | Number of subsets |
| ---: | ---: |
| 15 | 10 |
| 16 | 16 |
| 17 | 38 |
| 18 | 78 |
| 19 | 40 |
| 20 | 38 |

Selection (5) is the first lexicographic minimizer. This optimality
statement concerns these 220 coordinate selections only. It says
nothing about arbitrary linear nine-channel subspaces or other
auxiliary constructions.

## 4. Conditional completion of a reduced-source map

Consider the reduced tensor of format (27,16,16)

\[
 R=\sum_{\substack{0\leq i,s<3\\0\leq p,q,r,j<2}}
 X(i,p+q,s)Y(p,r+s,j)Z(r,i+j,q).
 \tag{6}
\]

The coordinate orders are (3i+k)3+s on X, (4p+L)2+j on Y,
and (4r+H)2+q on Z. There are 144 distinct unit terms.
For residues e,f in {0,1,2}, embed its coordinates into (1) by

\[
\begin{aligned}
 X(i,k,s)&\mapsto F(3i,k,3s),\\
 Y(p,L,j)&\mapsto F(p,e+3L,f+3j),\\
 Z(r,H,q)&\mapsto F(e+3r,f+3H,q).
\end{aligned}
 \tag{7}
\]

All indices are in range and in the ambient spaces of Section1.
The equations for the original long coordinates, reduced modulo3,
force matching residue pairs on Y and Z. After this match, division
by3 recovers (6). Thus (7) embeds nine copies of R with a common first
factor. The full-source replay checks all 559,872 coefficients of
format (27,144,144); exactly 1,296 coefficients are one.

**Conditional proposition.** Suppose there are three linear maps
from R to target variables of M(4,4,3) such that their output is

\[
 M(4,4,3)+a(X)b(Y)c(Z),
 \tag{8}
\]

where a, b, c are single linear forms. The maps and forms may be over
Q or C. Then the source A(8,8) has a restriction to M(4,4,27).
If the nine-copy lifted core has response ranks (r_X,r_Y,r_Z), the
completed maps have response ranks at most

\[
 (r_X+15,\;r_Y+9,\;r_Z+9).
 \tag{9}
\]

Indeed, use (7) on the maps of (8). Number the nine residue pairs by
nu=3e+f and use matrix channel 3nu+alpha for 0 <= alpha < 3.
The result is M(4,4,27) plus

\[
 a(X)\sum_{\nu=0}^{8}b_\nu(Y)c_\nu(Z).
\]

Identify the nine corner channels with these residue pairs. Send its
first variable to -a(X), and its other variables to b_nu(Y) and
c_nu(Z). The corner cancels the displayed error. Section2 excludes
every mixed term regardless of the chosen linear forms. The response
matrices also have no mixed terms, and postcomposition cannot raise
the rank of the auxiliary responses. Subadditivity of matrix rank
gives (9).

All first core response coordinates have k=p+q <= 2, so r_X <= 192
and the completed first response is at most207. This bound concerns
the partial matrix module M(4,4,27). It does not establish the remaining
matrix-unit equations or every leg's budget for a larger rectangle.
In particular, adding the auxiliary rank bounds can exhaust an
extension budget that the pure core would satisfy. Actual completed
response ranks must be checked in any such use; overlap of response
images must not be assumed.

The same cancellation holds over the Laurent-function field when
(8) holds there. It can also be used coefficientwise in a limit
construction with an explicitly controlled remaining error. Such a
limit still requires its own complete coefficient and overhead proof.
This package supplies neither the missing maps of (8) nor a larger
matrix tensor or exponent implication.

## 5. Reproduction and acceptance scope

From the repository root, with Python3.10 or later and no third-party
dependencies:

```sh
python -S research/ai/2026-10-20-anisotropic-constructions/spin_scalar_corner.py
python -S -m unittest discover -s tests -p test_spin_scalar_corner.py -v
```

The saved certificate contains the integer coordinate maps, full
response supports and unit-minor witnesses, the complete finite
selection scan, six zero mixed-response checks, and the nine-copy
reduced-source replay. An omitted sparse entry is zero. Equality of
the reconstructed sparse coefficient dictionary with the complete
target accounts for every zero as well as every nonzero coefficient.

The tests include a perturbation adding F(5,12,6) to the first Y row.
That perturbation preserves the small M(1,1,9) identity but creates
a mixed response against the core ambient Z space. The mixed-response
gate rejects it. A separate changed tensor coefficient and a changed
rank witness are rejected as well. These controls distinguish the
actual compatibility requirement from the small corner identity alone.
