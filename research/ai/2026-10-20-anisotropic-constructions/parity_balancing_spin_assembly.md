# Exact preimages and row constraints for the spin core

October 21, 2026. This note gives a complete linear description of the
remaining first-leg freedom for the saved
$A(8,8)\to M(3,3,28)$ restriction, and explicit bases for adding rows
after deleting middle coordinate 27. It also independently replays the
reduced construction and both original-source embeddings.

The saved core is an actual rational construction. A square assembly is
still missing. The conclusions below concern the specified saved maps;
changing existing second- or third-leg rows can change these preimages.

## 1. Actual response and its exact kernel

Use the common source coordinates $F(i,k,s)$, numbered
$(15i+k)8+s$, where $i,s<8$ and $k<15$. The original source coefficients
are one at

$$
 X(i,p+q,s)Y(p,r+s,j)Z(r,i+j,q).
 \tag{1}
$$

Let $Y^0,Z^0$ be the two saved 28-channel maps in
[the full spin export](../../../results/anisotropic-constructions-2026-10-20/spin-module14-full-maps.json).
Their rows are indexed by $(J,\alpha)$ and $(I,\beta)$, with
$I,J<3$ and $\alpha,\beta<28$. Let

$$
 \Psi(f)_{J\alpha,I\beta}=T(f,Y^0_{J\alpha},Z^0_{I\beta}).
 \tag{2}
$$

All second-leg source coordinates used by $Y^0$ have first short index
$p<2$. All third-leg coordinates used by $Z^0$ have last short index
$q<2$. Thus (1) implies that $\Psi$ only depends on

$$
 S=\operatorname{span}\{F(i,k,s):i,s<8,\ k<3\},\qquad \dim S=192.
 \tag{3}
$$

The exact integer response, before dividing by $732\cdot20$, has a
nonsingular $192\times192$ minor modulo 65521. Therefore
$\Psi|_S$ is injective over $\mathbb Q$. Together with the support
upper bound, this gives

$$
 \operatorname{rank}\Psi=192,\qquad
 \ker\Psi=W=
 \operatorname{span}\{F(i,k,s):i,s<8,\ 3\le k<15\},\qquad
 \dim W=768.
 \tag{4}
$$

The kernel in (4) is the entire coordinate space shown, with no
additional vectors supported in $S$.

The certificate proves more than one particular coordinate deletion.
It includes full-rank minors using only the middle coordinates in

$$
 S_0=\{0,\ldots,6,14,\ldots,20\},\qquad
 S_1=\{7,\ldots,13,21,\ldots,27\}.
 \tag{5}
$$

These sets are disjoint. Each of the 28 possible one-coordinate
deletions leaves at least one of the two certified minors intact.
Consequently every such deletion gives the same exact kernel $W$.
This does not concern a non-coordinate section and retraction of the
middle vertex.

## 2. The entire first-leg preimage

Write $X^0_{IJ}$ for the nine saved first images. They lie in $S$ and
satisfy

$$
 \Psi(X^0_{IJ})=E_{J,I}\otimes I_{28}.
 \tag{6}
$$

After a coordinate deletion, replace $I_{28}$ by $I_{27}$. Since (4)
still holds, every preimage of the right side of (6) is exactly

$$
 X^0_{IJ}+w_{IJ},\qquad w_{IJ}\in W.
 \tag{7}
$$

The preimage of the span of the nine response matrices has dimension
$768+9=777$. Every first unit outside this rectangular core in a
prospective direct sum of full square matrix tensors must have zero
response on the retained $Y^0,Z^0$ rows. Hence its first image must lie
in $W$.

For any concise target extending these particular second- and third-leg
rows, this proves the necessary dimension bound $D\le777$. In
particular the fixed original core, after any coordinate deletion,
cannot extend to the $D=778$ target $M_{27}\oplus M_7$.
The alternative target

$$
 M_{27}\oplus M_6\oplus M_3
 \tag{8}
$$

has $D=774$ and is not excluded by this bound. This is a statement
about fixed saved rows, not an obstruction for an altered spin
construction or for the full source.

## 3. Explicit spaces for additional second- and third-leg rows

For the remainder of this note delete middle coordinate 27, and hold
the particular first rows $X^0$ fixed, with $w_{IJ}=0$ in (7).
Let $Y^{27},Z^{27}$ be the 81 retained rows on each other leg.
Every additional second-leg row in a full square extension must lie in

$$
 K_Y=\{y:T(X^0_{IJ},y,Z^{27}_{I'\alpha})=0
        \text{ for all }I,J,I'<3,\ \alpha<27\}.
 \tag{9}
$$

Likewise every additional third-leg row must lie in

$$
 K_Z=\{z:T(X^0_{IJ},Y^{27}_{J'\alpha},z)=0
        \text{ for all }I,J,J'<3,\ \alpha<27\}.
 \tag{10}
$$

These are 729 explicit homogeneous coefficient equations for each
source vector.

In (9), the first image has $k<3$ and last short index zero or two,
while the retained third map has $q<2$ and $r<8$. Formula (1) therefore
restricts the active second coordinates to

$$
 B_Y=\{F(p,L,j):p<3,\ L<10,\ j<8\},\qquad |B_Y|=240.
 \tag{11}
$$

The response matrix on these coordinates has exact rank 233. The
certificate supplies seven independent integral vectors in its kernel;
their 729 coefficients vanish over the integers. A nonsingular
$233\times233$ minor modulo 65521 gives the matching lower rank bound.
Thus a basis of $K_Y$ consists of the 720 coordinate directions
outside $B_Y$, together with those seven vectors:

$$
 \dim K_Y=720+7=727.
 \tag{12}
$$

For (10), the first short index of $X^0$ is below two and the retained
second map has $p<2$ and $j<8$. The active third coordinates lie in

$$
 B_Z=\{F(r,H,q):r<8,\ H<9,\ q<3\},\qquad |B_Z|=216.
 \tag{13}
$$

Here the exact response rank is 213. Three independent integral kernel
vectors and a nonsingular $213\times213$ modular minor certify both
inequalities. A basis of $K_Z$ consists of the 744 coordinate
directions outside $B_Z$ and these three vectors:

$$
 \dim K_Z=744+3=747.
 \tag{14}
$$

All entries of the additional vectors are stored as pairs
$(\text{original source column},\text{integer coefficient})$ in
[the certificate](../../../results/anisotropic-constructions-2026-10-20/parity_balancing_spin_assembly_certificate.json).
Their largest absolute coefficients are 8460 for $K_Y$ and 900 for
$K_Z$. The verifier proves their independence and all their zero
coefficient identities; these are exact bases, not numerically
estimated nullspaces.

The retained 81-dimensional second row space meets $K_Y$ trivially:
otherwise its response in (9) would contradict the concise
$M(3,3,27)$ identity. The corresponding assertion holds for $K_Z$.
Thus independent added vectors inside these kernels also remain
independent of the retained rows.

## 4. What remains to construct

For (8), label the rectangular core by $I,J<3$ in the 27-dimensional
block, with every middle label $\alpha<27$. The missing row counts are

| Leg | Retained rows | Additional rows | Available space with the stated core fixed |
|---|---:|---:|---:|
| First | 9 | 765 | $W$, dimension 768 |
| Second | 81 | 693 | $K_Y$, dimension 727 |
| Third | 81 | 693 | $K_Z$, dimension 747 |

The next construction must choose those independent vectors and satisfy
all the remaining tensor equations. In particular, for an added first
image $w$, an added second image $y$, and an added third image $z$, it
must impose the required matrix coefficients of

$$
 T(w,y,Z^{27}),\qquad T(w,Y^{27},z),\qquad
 T(X^0,y,z),\qquad T(w,y,z).
 \tag{15}
$$

Equations (9)--(10) only settle coefficients with one new row and the
other two rows retained. They do not imply any of (15).
For a proposed new unit in another direct-sum block, the appropriate
mixed coefficients in (15) must also be zero.

Allowing the nine particular first images to change as in (7) enlarges
the assembly family. It then changes (9)--(10) to equations with
$X^0_{IJ}+w_{IJ}$, so the specific spaces $K_Y,K_Z$ above must not be
assumed for that enlarged problem. Likewise an exact deformation of
the retained $Y$ or $Z$ rows requires a new response calculation.

## 5. Independent replay and scope

The maintained verifier independently enumerates all 512 reduced source
terms, all 32,768 original $A(4,8)$ terms, and all 262,144 original
$A(8,8)$ terms. It checks respectively 15,876, 15,876, and 63,504
target coefficients from the actual exported maps. The deletion-27
control checks all 59,049 coefficients of $M(3,3,27)$.

It then rebuilds the complete first response directly from the actual
two other maps, compares that response against the full target
contraction, verifies the two disjoint-channel minors, and rebuilds
both added-row systems from the original source. Kernel identities
are checked with integers. Rank lower bounds use only exact arithmetic
in the prime field of order 65521.

    python -S research/ai/2026-10-20-anisotropic-constructions/parity_balancing_spin_assembly.py
    python -S -m unittest discover -s tests -p test_parity_balancing_spin_assembly.py

The accepted verifier has no NumPy or SymPy dependency. The complete
results are in
[the replay report](../../../results/anisotropic-constructions-2026-10-20/parity_balancing_spin_assembly_report.json).
No full square assembly or smaller exponent is established. No
external independent review or formalization is claimed.
