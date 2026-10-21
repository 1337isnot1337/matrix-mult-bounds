# Audit of the smallest claimed Sun certificate

## Status and precise question

**The proposed global degeneration is unverified in this repository. This
audit proves neither a smaller exponent nor the nonexistence of the proposed
global degeneration.** It verifies several finite components, finds a
repairable normalization error, and excludes a particular packetwise reading
of the chart substitution.

The external source is Zhi-Wei Sun, *Tensor Degenerations for Matrix
Multiplication*, [arXiv:2610.13971v1](https://arxiv.org/html/2610.13971v1),
specifically Definition 2.4, Sections 5–8, and Appendices A.3–A.7. All references
below concern this exact version, inspected on 2026-10-21. The source's theorem
statements are external claims, distinct from the calculations in this package.

One of the smallest matrix-size certificates claimed to improve the
repository's 9/4 baseline is Theorem 1.3(a):

\[
\mathsf M_{32}\unlhd
\mathsf D_{16}\boxtimes
\bigl(14\mathcal C_3\oplus6\mathcal C_2\oplus7\mathcal W
      \oplus5\mathsf D_4\bigr).
\]

Its one-row source has dimensions `(128,128,128)` and border-rank budget 128.
The full source has dimensions `(2048,2048,2048)`, while the target has
dimensions `(1024,1024,1024)`. A valid degeneration with the stated source
budget would imply the exponent bound `log_32(2048)=11/5`. The missing step is
an independently reconstructed, complete three-factor Laurent map whose
coefficient tensor is exactly the stated target.

## Reproduction

From the repository root:

```sh
python research/ai/2026-10-21-sun-audit/verify.py --output research/ai/2026-10-21-sun-audit/audit.json
python -m unittest discover -s tests -p test_sun_audit.py -v
```

The checker uses only the Python standard library. Scalar arithmetic and
matrix elimination use exact rational numbers; binary characters use integer
parity. The report includes all 64 coefficients of the small diagnostic
tensor and the complete 24-by-16 Koszul matrix with a determinant-one minor.

| Component | Exact coverage | Result |
|---|---:|---|
| Literal scalar table in Section 5 | 354 source support occurrences | 50 retained coefficients have the wrong normalization |
| Explicit local normalization repair | The same 354 occurrences | All agree with the claimed support mask |
| Proposition 5.1, normalized scalar formula | All 256 chart pairs | All agree |
| Side-colour decomposition of the support twists | All 12 supports | All agree |
| Equation (5.2), chart representatives | All 128 defects, all 256 possible chart pairs per defect | Exactly the stated two representatives |
| Generic packet chart pullback | 12 packets, all 64 central coefficients each | Exactly `M2/16` on the displayed restriction |
| First Koszul matrix of `M2` | Full 24-by-16 integer matrix | Rank 16; a recorded 16-by-16 minor has determinant 1 |
| Five-empty-module base pairings | Four rational matrix identities and 15 zero sums | All agree |
| Five-empty-module character action | All 256 character pairs | All agree |

Passing these checks does not establish the source-to-target global map.

## 1. A literal normalization mismatch that has a local repair

For the big Coppersmith–Winograd tensor, use the paper's support notation

\[
A_i=x_0y_i z_i,\qquad B_i=x_i y_0z_i,\qquad
C_i=x_i y_i z_0.
\]

Section 5 sets `x0=1/128`, `y0=z0=1`, and assigns nonzero satellite scalars the
value 1. For example, a retained `B1` has literal coefficient
`x1*y0*z1=1`, although the text says every retained support has coefficient
`1/128`. Across the 32 packets, exactly 50 of 128 retained support occurrences
have this discrepancy. The other 226 occurrences vanish as intended.

Dividing every X-side satellite scalar by 128, while retaining the stated
centre and infinity scalars, repairs all 354 coefficient comparisons. Thus
this mismatch alone is not an obstruction to the claimed theorem. The
Proposition 5.1 check in this package uses the displayed normalized formula,
equivalently the repaired local scalar table.

## 2. The finite Walsh identity checks

Write `H4=F2^4`, encoded by integers 0 through 15, and let

\[
B_0=(9,4,8,6),\qquad B_1=(8,6,4,9)
\]

denote their basis images. With the literal packet masks and support twists,
the checker evaluates

\[
\sum_{p}\frac1{128}
(-1)^{\chi_p\cdot(\rho+B_{\lambda_p}\beta)}
\sum_{m\in\mathcal R_p}(-1)^{\Theta(m)\cdot\beta}.
\]

Its only nonzero values are 1 at `(rho,beta)=(0,0)` and `(3,15)`, exactly as
in Proposition 5.1. This establishes the scalar identity. A scalar identity
in shared chart variables does not, by itself, specify a tensor restriction
on three independent coordinate spaces.

## 3. An exact obstruction to the packetwise chart interpretation

This section concerns the following specific interpretation: take each
packet's scalar summand in Proposition 5.1, substitute the chosen linear chart
section from Equation (5.2), and require that summand to be the coefficient
tensor produced by the corresponding individual source packet. That
interpretation is impossible even after the scalar normalization is repaired.

For a defect `d=(dH,d1,d2,d3)`, a legal section is

\[
\beta=d_1e_1+d_2e_2+d_3e_3,
\qquad \rho=d_H+B_0\beta.
\]

Here bit positions start at zero in the implementation, so the numerical
value of `beta` is `d1+2*d2+4*d3`. The first three columns of `B0+B1` are
`1,2,12`, exactly the prescribed map from the three central defects.

Each generic layer-one packet has the eight retained twists

\[
\{3,0,5,9,6,10,12,15\}.
\]

Restricted to the first three bits of beta, these are all eight characters of
`F2^3`. Its scalar chart summand therefore pulls back to

\[
\frac1{128}(-1)^{\chi\cdot d_H}
(-1)^{\chi\cdot(B_0+B_1)\beta}
\sum_{m\in\mathcal R_p}(-1)^{\Theta(m)\cdot\beta}
=\frac1{16}(-1)^{\chi\cdot d_H}
\mathbf1_{d_1=d_2=d_3=0}.
\]

Now fix the three noncentral labels to `q=1`, `r=2`, and `s=3`.
They are all nonzero and sum to zero in `H4`. In particular, none of the
coordinates in this restriction is the deleted zero coordinate of the
punctured dense target. Write the remaining three pairs as

\[
u=(1,\epsilon,a),\quad v=(2,\delta,b),\quad w=(3,\phi,c).
\]

The central defects are

\[
d_1=b+a+\epsilon,\quad d_2=\phi+\epsilon+\delta,
\quad d_3=c+a+\epsilon+\delta.
\]

The coordinate changes

\[
X_{\epsilon,a}\mapsto x_{a,a+\epsilon},\quad
Y_{\delta,b}\mapsto y_{b,b+\delta},\quad
Z_{\phi,c}\mapsto z_{c,c+\phi}
\]

turn their zero fibre into

\[
\sum_{a,b,c\in\mathbb F_2}x_{ab}y_{bc}z_{ca}=\mathsf M_2.
\]

Consequently the proposed individual packet pullback contains `M2/16` as an
ordinary restriction. All 64 coefficients are checked for each of the 12
generic packets.

### The lower bound needed for this obstruction is elementary

For a tensor in `A⊗B⊗C` with `dim A=4`, the first Koszul map is

\[
K_1(T):A\otimes B^*\longrightarrow\Lambda^2 A\otimes C,
\qquad
a\otimes\beta\longmapsto\sum_i(a\wedge a_i)\otimes\beta(b_i)c_i.
\]

For one simple tensor its rank is at most 3. Rank subadditivity and the
vanishing of minors imply that a tensor of border rank at most 5 has
`rank K1≤15`. The checker constructs the complete Koszul matrix of `M2`.
It has rank 16; the rows

```text
5,7,0,2,9,11,17,19,4,6,12,14,8,10,16,18
```

give a 16-by-16 minor of determinant 1 in the recorded row and column order.
Thus `border_rank(M2)≥6`, which already exceeds the source budget 5 of one
`CW3`. This also excludes a single compressed `D4` packet. No assumption
about the stronger optimal border rank of `M2` is needed.

### Why the support phases are not immediately sidewise

Let the three side colours be `thetaX(i)`, `thetaY(j)`, and `thetaZ(k)`.
The checked identity

\[
\Theta(i,j,k)=\theta_X(i)+\theta_Y(j)+\theta_Z(k)
\]

factors a character when the same beta is an external fixed parameter.
After beta is replaced by `betaX(u)+betaY(v)+betaZ(w)`, its expansion also
contains terms pairing one side's colour with another side's target
coordinate. Merely assigning each source colour its own side character
does not supply those terms.

For a concrete incidence, `A1` and `A3` share `x0` but their total twists
differ by 3. The X contribution to beta can be 5, and the resulting relative
character is `(-1)^(3·5)=-1`. The same `x0` image cannot receive two different
coefficients according to which support occurrence uses it. The Koszul
argument above strengthens this incidence diagnostic to an obstruction to
*any* three sidewise maps realizing the specified individual packet tensor.

### Scope: the global claim remains unresolved

Section 8 explicitly asks that packet, endpoint, row, and character records
remain separate until the physical decoder. It may therefore intend a more
general composition that does not produce the scalar chart pullback one
packet at a time. This audit has not reconstructed such a composition and
does not prove that no such composition exists. The common-twist average,
the use of outer rows, and the endpoint contributions must be accounted for
inside the same three maps. A proof that only counts terminal matrix cycles
does not perform that check.

The exact missing deliverable is a rule assigning to every original source
basis coordinate a Laurent polynomial linear form on its own target factor,
followed by verification of all target and off-target tensor coefficients.

## 4. The five-empty-module identities also check

The literal rational matrices `B`, `D`, `c`, and `J10` in Section 6.5 satisfy
the four displayed pairings. Every row has the stated zero sum over its last
five columns. With the packet characters `xi=(0,3,4,9,12)` and the repeated
diagonal character matrix `Sigma_delta`, the actions

\[
M_\delta=B\Sigma_\delta J_{10}D^{\mathsf T}
\]

satisfy all 256 equations `M_delta M_epsilon = M_(delta+epsilon)`.
These exact finite checks explain why a failure of the global map cannot be
inferred from these particular local identities.

## 5. Full-space Koszul tests cannot reject the proposed full source

This is a separate, general limitation of the necessary tests, derived during
this audit. It is a written proof, not a numerical experiment and not a
verification of the proposed degeneration.

For a `CWq` block of dimension `d=q+2`, normalize its invertible first slice
to the identity. The other slices can be written

\[
N_i=E_{0i}+E_{i,d-1},\qquad Z=E_{0,d-1},
\]

with `Ni Nj=delta_ij Z`, `Ni Z=Z Ni=Z^2=0`. The normalized slices commute.
The analogous `W` block has the identity and one square-zero slice, while
the diagonal blocks give commuting diagonal slices. The Koszul differential
therefore squares to zero. Contraction by the dual of the unit slice gives
a homotopy `dh+hd=I`, so the complex is exact. Its degree-p rank is

\[
d\binom{d-1}{p}.
\]

Padding the first factor to dimension `N` and applying the exterior-product
decomposition gives `d binom(N-1,p)`. The direct-sum blocks occupy disjoint
second and third factors, so their ranks add. For the full claimed source,
`N=2048`, this yields on each of its three legs

\[
\operatorname{rank}K_p(S)=2048\binom{2047}{p}.
\]

For `M32` padded to the same first-factor dimension, the domain and codomain
bounds alone give

\[
\operatorname{rank}K_p(\mathsf M_{32})
\le1024\min\left\{\binom{2048}{p},\binom{2048}{p+1}\right\}.
\]

The ratio to the source rank is at most `1024/(2048-p)<1` for `p≤1023`, and
at most `1024/(p+1)<1` for `p≥1024`. Thus every full-space Koszul test on all
three legs necessarily passes. This does not weaken the smaller packetwise
obstruction: that obstruction concerns a different source and target, where
the exact rank comparison goes in the opposite direction.
