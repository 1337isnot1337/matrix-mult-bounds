# A complete fourth vertex with three low source layers

## Status and contribution

Claim ID: **AI-SPIN-FOURTH-VERTEX-122**.

This package gives explicit rational maps

\[
A(2d,2d)\longrightarrow M(3,4,2d^2),\qquad d\geq1.
\tag{1}
\]

At \(d=4\), it exports both \(M(3,4,32)\) and the same-channel
section \(M(3,4,28)\) inside the original \(A(8,8)\) source.
The first response remains in the three long-coordinate layers
\(k=0,1,2\). The three full-source response ranks of the latter
maps are exactly \((192,252,252)\).

The existence of the tiny target \(A(2,2)\to M(3,4,2)\) alone is
already implicit in the known \(A(2,2)\to M(2,3,4)\) control by
cyclic rotation; see the [package's earlier control](README.md) and
`dense_als.py`. No novelty is claimed for that target alone.
The useful additional data here are the particular rational maps on
the full twelve-dimensional local first-source chart, their explicit
residue lift, and their favorable three-leg response spaces. The local
chart contains the nine first images used by the spin-one construction.
The residue lift specifies which scaled chart is used in the larger
source.

These constructions and proofs were generated in this research session.
The tiny identity and residue argument were checked by two other agents
in this generating session; there is no external independent review.
The maps do not establish a smaller matrix multiplication exponent.

## 1. Tiny rational identity

Use the tensor

\[
\sum_{i,p,r,j,q,s\in\{0,1\}}
X(i,p+q,s)Y(p,r+s,j)Z(q,r,i+j).
\tag{2}
\]

The third coordinate order is deliberately \((q,r,H)\) here.
The flat column numbers are

| leg | tiny source column | target row |
|---|---|---|
| X | \((3i+k)2+s\) | \(4I+J\) |
| Y | \((3p+L)2+j\) | \(2J+\alpha\) |
| Z | \((2q+r)3+H\) | \(2I+\alpha\) |

Here \(I<3,J<4,\alpha<2\). The complete integer entry lists are in
[the tiny witness](../../../results/anisotropic-constructions-2026-10-20/parity_structure_spin22_fourth_vertex_witness.json).
Their common denominators are \((2,1,2)\), and their numbers of
nonzero entries are \((24,24,20)\). Every omitted entry is zero.

Writing their numerator matrices as \(P_X,P_Y,P_Z\), the exact finite
identity is

\[
\sum_{i,p,r,j,q,s<2}
P_X[4I+J,(3i+p+q)2+s]\,
P_Y[2J'+\alpha,(3p+r+s)2+j]\,
P_Z[2I'+\beta,(2q+r)3+i+j]
=4\delta_{I,I'}\delta_{J,J'}\delta_{\alpha,\beta}.
\tag{3}
\]

The verifier checks all 576 coefficients in (3), using all 64 original
source terms. Exactly 24 coefficients are four; all others are zero.
Division by the three map denominators gives \(M(3,4,2)\).
This explicit finite identity is sufficient to establish the tiny map
over \(\mathbb Q\), and therefore over \(\mathbb C\).

One way to obtain the first map is to set

\[
W(F)_{(i,q),(p,s)}=F(i,p+q,s),\qquad
P=\begin{pmatrix}0&1&0&1\\1&0&0&0\\0&0&1&0\\0&-1&0&1\end{pmatrix},
\]

and use all twelve entries in the top three rows of \(P^{-1}W(F)P\).
Their coefficient map is invertible. This extends the local nine-entry
spin chart to all twelve first directions. The other two maps solve
the full source coefficient equations; their actual lists, rather
than a numerical residual, are the acceptance witness.

## 2. Residue lift for every positive integer d

Let \(n=2d\). In the full source, every leg has columns
\(F(u,k,v)\), flattened as \(((2n-1)u+k)n+v\). For each pair
\(0\leq e,f<d\), replace tiny columns as follows:

\[
\begin{aligned}
X(i,k,s)&\mapsto F(di,k,ds),\\
Y(p,L,j)&\mapsto F(p,e+dL,f+dj),\\
Z(q,r,H)&\mapsto F(e+dr,f+dH,q).
\end{aligned}
\tag{4}
\]

All indices are in range. In particular \(e+dL,f+dH\leq3d-1\)
and the full long coordinate has upper bound \(4d-2\).
Use the common middle-channel index

\[
\gamma=2(de+f)+\alpha.
\tag{5}
\]

Different residue pairs have separate Y and Z target rows, while they
share the same twelve X target rows. Consider a coefficient using
residues \((e,f)\) on Y and \((e',f')\) on Z. The original source
equations for the two long coordinates read

\[
e+dL=e'+d(r+s),\qquad f'+dH=f+d(i+j).
\tag{6}
\]

Reduction modulo \(d\) forces \(e=e'\) and \(f=f'\), since all
four residues lie between zero and \(d-1\). Then (6) reduces to the
tiny equations \(L=r+s\), \(H=i+j\). The remaining long equation
is unchanged: \(k=p+q\). Thus every equal-residue coefficient is
exactly (3), and every unequal-residue coefficient is zero. This proves
(1), including every mixed coefficient, for all positive integers d.

Deleting the same subset of middle channels from Y and Z gives the
corresponding ordinary rectangular section. The exported 28-channel
map keeps \(\gamma=0,\ldots,27\) from the 32-channel map at d=4.

## 3. Full-source response ranks and extension budgets

For fixed Y and Z maps, the first response sends an arbitrary original
source coordinate to the bilinear form obtained by contracting those
two maps. The other two responses are defined cyclically, with the
other target legs in their stated order. If a response has rank r and
the current target leg has dimension t, the preimage of that current
target leg has dimension \(N-r+t\): the existing exact target spans
t independent response directions, and the response kernel has
dimension \(N-r\).

For X, the literal Y and Z supports have \(p,q<2\); hence all first
responses have \(k=p+q<3\). There are at most \(3\cdot8^2=192\)
such original source coordinates. The actual full-source replay
computes the response supports on all three legs. Its support sizes
are matching rank upper bounds. The saved square minors supply lower
bounds over \(\mathbb Q\), because their integer determinants are
nonzero modulo the prime 65521.

| target | exact response ranks X,Y,Z | current target leg dimensions | exact preimage dimensions |
|---|---|---|---|
| M(3,4,32) | (192,288,288) | (12,128,96) | (780,800,768) |
| M(3,4,28) | (192,252,252) | (12,112,84) | (780,820,792) |

For the proposed full target \(M(27,28,28)\), the leg dimensions are
\((756,784,756)\). The 28-channel core's separate preimage dimensions
exceed these by \((24,36,36)\). This passes three necessary dimension
checks. The remaining matrix-unit compatibility equations are unsolved;
the three separate preimages do not imply a full target restriction.

The recovered certificate uses the following nonzero minor residues:

| target | X | Y | Z |
|---|---:|---:|---:|
| M(3,4,32) | 36710 | 1787 | 19143 |
| M(3,4,28) | 43245 | 58785 | 8539 |

All minors are rebuilt from the actual saved rational map numerators.
The Y minor choices were regenerated after recovery; the ranks and
maps coincide with the earlier verified construction. No claim relies
on a saved boolean or on a floating-point rank decision.

## 4. Files and exact verification

The [generator](parity_structure_spin22_fourth_vertex_generate.py)
retains the tiny integer entries and rebuilds both full maps and the
six rank certificates. It requires only the standard library.
The [verifier](parity_structure_spin22_fourth_vertex.py) checks the
actual exported maps against (4), then contracts the original sources.

```sh
python -S research/ai/2026-10-20-anisotropic-constructions/parity_structure_spin22_fourth_vertex_generate.py
python -S research/ai/2026-10-20-anisotropic-constructions/parity_structure_spin22_fourth_vertex.py
python -S -m unittest discover -s tests -p 'test_parity_structure_spin22_fourth_vertex.py' -v
```

The full 32-channel identity checks all 262,144 original source terms
and all 147,456 target coefficients. The 28-channel section checks all
262,144 original source terms and all 112,896 target coefficients.
There are respectively 384 and 336 unit target terms. The tests also
reject a nonzero-to-nonzero change in the tiny Y map and an altered
third-leg determinant certificate.

This is recovery of previously verified claim 122 after a filesystem
rollback, with fresh standard-library replay and rank certificates.
It is not additional mathematical progress beyond that construction.
