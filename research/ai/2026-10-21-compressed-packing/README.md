# A compressed packing and an explicit alternative limit

October 21, 2026. AI-derived construction, written proof, and exact controls.
The construction below does not produce the full fat-point tensor and does
not improve the matrix multiplication exponent. It modifies the
[alternating-degree packing](../2026-10-20-alternating-degree-packing/README.md)
by removing all unused input positions. The resulting negative coefficient
is retained explicitly, then used to construct a different tensor.

## 1. The complete Laurent identity

Let `m=2s>=2`, `D=m-1`, and `N=m(m+1)/2`. The target under investigation is

\[
T_m=\sum_{a+b+c+d=D}X_{a+c}Y_{a,b}Z_{c,d}.
\]

For `i=0,...,s-1`, put `b_i=i(m+1)`. The low degree `p=i` has
start `b_i` and weight zero. Its paired high degree `p=D-i` has
start `b_i+i+1` and weight one. Write these starts and weights as
`s_p,h_p`. Use the identity shared map and the substitutions

\[
Y^{\rm source}_{s_p+p-a}\longmapsto
 \epsilon^{h_p}Y_{a,p-a},\qquad 0\le a\le p,
\]

\[
Z^{\rm source}_{s_p+p+c}\longmapsto
 \epsilon^{-h_p}Z_{c,D-p-c},\qquad 0\le c\le D-p.
\]

All unselected source output coordinates are zero. These maps fit in
`C(m,N)` and give the exact identity

\[
\boxed{\text{mapped source}=\epsilon^{-1}E_m^-+T_m+\epsilon E_m^+.} \tag{1}
\]

Here `E_m^+` is the sum of the unwanted high-to-low connections, and the
entire negative coefficient has the explicit form

\[
\begin{aligned}
E_m^-={}&\sum_{i=1}^{s-1}\ \sum_{\substack{0\le a,c\le i\\a+c\le i-1}}
 X_{m-i+a+c}Y_{a,i-a}Z_{c,i-c}\\
&+\sum_{i=2}^{s-1}\ \sum_{\substack{0\le a\le i,\ 0\le c<i\\a+c\ge i+1}}
 X_{a+c-i-1}Y_{a,i-a}Z_{c,i-1-c}.
\end{aligned}                                                     \tag{2}
\]

All coefficients in these formulas are one. At `m=4`,

\[
E_4^-=X_3Y_{0,1}Z_{0,1}.
\]

For `m>=4`, (1) has a nonzero negative power and is **not** a degeneration
to `T_m`. Its purpose is to make the remaining cancellation problem exact.

## 2. Proof of the identity

Within pair `i`, the low and high selected input intervals are
`[b_i,b_i+i]` and `[b_i+i+1,b_i+m]`. They form one interval of length
`m+1`. The next pair starts at `b_i+m+1`, so the selected input indices
are exactly `0,...,N-1`.

The corresponding output intervals are `[b_i+i,b_i+m-1]` and
`[b_i+m,b_i+m+i]`. Their union has length `m+1`; successive such unions
have one unused position between them. The largest selected output is
`N+s-2`, which is within the `N+m-1` source output coordinates.

A source term connects an input position `j` to an output position `k`
exactly when `0<=k-j<=D`. Connections within a matched degree block
have difference `a+c`, exponent zero, and give exactly `T_m`.
Different low blocks do not connect: the next low output begins at least
`m+2` after the current low input maximum, while the preceding low output
ends before the current input minimum. Different high blocks also do not
connect, by the corresponding gaps `m+1` and three.

Thus every unwanted term connects high input to low output, with exponent
one, or low input to high output, with exponent minus one. For low pair
`i` and high pair `j`, the source difference is

\[
(j-i)(m+1)+m-i+a+c.
\]

It can be between zero and `D` only for `j=i` or `j=i-1`.
The first case gives `a+c<=i-1`, and the second gives `a+c>=i+1`.
These are exactly the two sums in (2), proving (1).

The two sums have respectively `i(i+1)/2` and `i(i-1)/2` terms at index
`i`. Consequently

\[
\#\operatorname{supp}(E_m^-)
 =\sum_{i=1}^{s-1}i^2=\frac{s(s-1)(2s-1)}6.                       \tag{3}
\]

Its shared indices lie in `0,...,s-3` and `s+1,...,2s-1`, with an empty
interval understood as contributing nothing. The three central indices
`s-2,s-1,s`, when present, never occur in the negative coefficient.

## 3. A genuine degeneration to an alternative tensor

Let `J_m={s-2,s-1,s} intersect {0,...,m-1}`, and let `T_m^central`
retain precisely the shared coordinates in `J_m`. Define the explicit tensor

\[
U_m=T_m^{\rm central}+E_m^-.
\]

In addition to the substitutions above, send source `X_r` to `X_r` for
`r in J_m` and to `epsilon X_r` for every other shared index. Equation
(2) shows that all terms of `epsilon^-1 E_m^-` now have exponent zero.
The central terms of `T_m` have exponent zero, its other terms have
exponent one, and the former positive terms have exponent one or two.
Therefore the transformed tensor is polynomial, with constant coefficient
`U_m`, proving

\[
\boxed{C(m,N)\unrhd U_m\quad\text{for every even }m\ge2.}          \tag{4}
\]

These are integer coefficient maps, so the construction is valid over
every field. At `m=2`, the negative coefficient is empty and this is the
already-known `T_2` control. At larger sizes, `U_m` is a different tensor.
No lower bound on its character values sufficient for an exponent
improvement is established here. In particular, (4) cannot be substituted
for the full `T_m` premise of the fat-point growth criterion.

## 4. Reproduction and scope

```sh
python research/ai/2026-10-21-compressed-packing/verify_compressed.py --max-m 40 --output results/compressed-packing-2026-10-21/compressed.json
python -m unittest discover -s tests -p test_compressed_packing.py -v
```

The verifier independently enumerates every source term, compares the zero
coefficient with the fat-point definition, compares every negative term with
(2), and then verifies the complete constant coefficient in (4). Twenty
even sizes through forty cover 182,140 source terms per map family. The
report includes the full Laurent tensor at size four and the full constant
tensor of its alternative degeneration.

The prior sharp packing remains credited to its source note. The compressed
identity and alternative tensor are construction objects for further work.
Same-session AI checks and finite replays are not external mathematical
review or formalization; no smaller exponent is claimed.
