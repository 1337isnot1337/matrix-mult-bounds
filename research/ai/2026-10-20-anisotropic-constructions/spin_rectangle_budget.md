# Three exact response budgets for a rectangular extension

October 21, 2026. This package determines the three response ranks of the
published rational restriction

\[
 A(8,8)\longrightarrow M(3,3,28).
\]

They are \((192,236,216)\). All three necessary preimage tests pass for a
possible extension to \(M(27,28,28)\), with dimension allowances
\((21,24,72)\). The larger tensor is not constructed. This package does
not establish a smaller matrix multiplication exponent.

The maps come from [the fourteen-channel spin construction](spin_module14.md)
and its two-sector lift. The earlier [assembly certificate](parity_balancing_spin_assembly.md)
already gave first response rank 192 and analyzed the 27-channel section.
Here the second and third response ranks use all 28 channels.

The concurrent [ordinary rectangular frontier at main 48bd72d](https://github.com/1337isnot1337/matrix-mult-bounds/blob/48bd72d9/research/ai/2026-10-21-rectangular-ordinary-frontier/proof.md)
also identifies \(M(27,28,28)\) as the sole balanced size-eight survivor
of its stated ordinary necessary tests. This note does not claim priority
for identifying that target. Its additional evidence concerns the three
response spaces of one particular exact retained core.

## 1. Source convention and exact response maps

Every leg of \(A(8,8)\) has dimension \(960=8\cdot15\cdot8\), with
coordinate

\[
 F(i,k,s)=(15i+k)8+s.
\]

The original source has coefficient one at

\[
 X(i,p+q,s)Y(p,r+s,j)Z(r,i+j,q),
 \qquad 0\le i,p,r,j,q,s<8,
 \tag{1}
\]

and zero elsewhere. The saved core maps have respectively 9, 84 and 84
rows. They realize \(M(3,3,28)\), whose nonzero coefficients are

\[
 (X_{3I+J},Y_{28J+\alpha},Z_{28I+\alpha}),
 \qquad I,J<3,\quad\alpha<28.
 \tag{2}
\]

Fix the other two saved maps and contract (1) with an arbitrary source
functional on leg \(i\). This gives a linear response map \(R_i\).
Multiplying its entries by the fixed positive map denominators does
not change its rank or kernel over \(\mathbb Q\).

The complete response supports and rational ranks are:

| Free leg | Possible source coordinates | Support size | Exact rank | Kernel inside the support |
| --- | --- | ---: | ---: | ---: |
| X | \(i,s<8,\ k<3\) | 192 | 192 | 0 |
| Y | \(p<3,\ L<10,\ j<8\) | 240 | 236 | 4 |
| Z | \(r<8,\ H<9,\ q<3\) | 216 | 216 | 0 |

These support assertions are checked directly on the actual response
coefficients. The verifier also checks a nonsingular square minor of
each stated rank modulo the prime 65521. Such a minor is nonzero over
\(\mathbb Q\). Four saved integer Y-kernel vectors vanish under the
full rational response and are independent modulo the same prime.
They give the matching upper bound 236. Support gives the matching
upper bounds on X and Z. Thus the full source kernels have dimensions
768, 724 and 744.

The acceptance replay contracts all \(8^6=262144\) original source terms.
It checks all 63,504 target coefficients against (2), including every
unwanted coefficient. Exactly 252 target coefficients are one.

## 2. The three preimage tests

Let a fixed exact core be \(M(p,q,r)\), inside a proposed larger
\(M(a,b,c)\). Denote the retained leg dimensions by

\[
 (c_X,c_Y,c_Z)=(pq,qr,rp),
\]

and the required full leg dimensions by

\[
 (D_X,D_Y,D_Z)=(ab,bc,ca).
\]

The response of every target leg vector against the two retained other
legs lies in the corresponding core response space. That space has
dimension \(c_i\) and is contained in \(\operatorname{im}R_i\), because
the existing core is exact. Rank-nullity therefore gives

\[
 \dim R_i^{-1}(\text{core response})=960-\rho_i+c_i,
 \qquad \rho_i=\operatorname{rank}R_i.
 \tag{3}
\]

Conciseness of the full matrix tensor requires independent images of
all \(D_i\) target directions. Any ordinary extension that retains the
specified other-leg rows must consequently satisfy

\[
 D_i\le960-\rho_i+c_i,
 \qquad\text{equivalently}\qquad
 \rho_i-c_i\le960-D_i.
 \tag{4}
\]

For the original core and the proposed rectangle, all quantities are:

| Leg | Retained dimension \(c_i\) | Response rank \(\rho_i\) | Preimage dimension | Required dimension \(D_i\) | Additional rows | Remaining allowance |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| X | 9 | 192 | 777 | 756 | 747 | 21 |
| Y | 84 | 236 | 808 | 784 | 700 | 24 |
| Z | 84 | 216 | 828 | 756 | 672 | 72 |

These are necessary tests, not existence statements. New rows must
also satisfy all mixed and new-new tensor coefficients simultaneously.
The response ranks change when retained maps change.

The retained dimension must also change when the core grows. For
example, completing one new second vertex gives \(M(3,4,28)\), with
12 first directions. Its first response rank is allowed to reach

\[
 960-756+12=216.
 \tag{5}
\]

Starting from rank 192, this permits raw growth of 24. The invariant
quantity in (4) is the response rank minus the retained dimension;
holding that dimension at nine after adding a complete vertex would
impose an incorrect stronger bound.

## 3. Existing source-rank tests and the conditional exponent

The [Hankel-symbol dimension theorem](hankel_symbol_dimension.md) applies
for \(1\le r<8\) and \(3r\le15\), hence \(r=1,\ldots,5\). Its rectangular
consequence is used without strengthening its hypotheses. For each
leg, if \(D_i>64r\), a rank-one target slice lifted to the source must
satisfy

\[
 n_i+(960-D_j)+(960-D_k)\ge64(r+1),
 \tag{6}
\]

where the rank-one target slice ranks are \((n_X,n_Y,n_Z)=(28,27,28)\).
The three left sides are 408, 435 and 408. All fifteen tests pass;
the largest right side is 384. No assertion for \(r=6\) is used here.
These ordinary-map tests do not establish or exclude arbitrary singular
degenerations.

The [existing finite spectral criterion](../2026-10-20-koszul/cyclic_finite_target.md),
also stated in the concurrent rectangular frontier, says that a construction of the full rectangle
would imply

\[
 \omega\le\frac{9\log46}{\log(216\cdot27\cdot28\cdot28)}.
 \tag{7}
\]

The exact integer comparison

\[
 (216\cdot21168)^{2247}>46^{9000}
 \tag{8}
\]

certifies that this conditional upper bound is strictly below
\(2247/1000=2.247\). The missing premise is an actual restriction or
degeneration to \(M(27,28,28)\). Neither (4), (6), nor (8) supplies it.

## 4. Reconstruction, files and reproducibility

This package was reconstructed after a local executor snapshot loss,
using the unchanged published maps and the earlier published assembly
kernel. The regenerated witnesses are independently checked against
the original source. They do not rely on a saved numerical rank.

- [Standard-library acceptance verifier](spin_rectangle_budget.py).
- [Standard-library witness generator](spin_rectangle_budget_generate.py).
- [Exact response certificate](../../../results/anisotropic-constructions-2026-10-20/spin-rectangle-budget-certificate.json).
- [Recorded replay](../../../results/anisotropic-constructions-2026-10-20/spin-rectangle-budget-report.json).
- [Maintained tests](../../../tests/test_spin_rectangle_budget.py).

Run from the repository root:

```sh
python -S research/ai/2026-10-20-anisotropic-constructions/spin_rectangle_budget_generate.py
python -S research/ai/2026-10-20-anisotropic-constructions/spin_rectangle_budget.py
python -S -m unittest discover -s tests -p test_spin_rectangle_budget.py -v
```

The proof and implementation are AI-derived work from this generating
session. Checks by another agent in the same session are not external
independent mathematical review. No formal proof is claimed.
