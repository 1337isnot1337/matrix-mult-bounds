# Boundary-spanning first growth is excluded at every order

AI-assisted research, October 21, 2026. Written proof, unreviewed.
**No matrix-multiplication exponent improvement is established.**

The [proof](proof.md) excludes the matrix target for the canonical
four-row quantum flags whenever both first new-row spans give the full
boundary quotients of dimension12. The first-growth orders may be
different and delayed. All higher coefficients and the Laurent first-leg
map are unrestricted. A formal induction confines the regular leg maps
to moving spaces of dimension56, below the target's concise dimension110.

The new ingredient is a forced third-order block. Its joint matrix
supports have dimensions at most12, and a matrix-target argument forces
its first rank to be at most2. Exact triangular determinants c*L^8 instead
prove that every nonzero block has first rank at least8. It must vanish,
leaving only the four common polynomial-plane directions needed for the
induction. The rank-eight lower bound has a sharp rational control.

The same support estimate also forces first rank at most2 for the
corrected projected third coefficient of every admissible ordinary
first-extension pair at these flags, restricted to the64-dimensional
source block K_inf. This is a general necessary condition;
the lower bound8 is proved here only for the full boundary frames.

For ordinary first derivatives this improves the necessary total effective
row rank from24 to23, using the previous mixed-component bound20.
Other first subspaces and leading flags remain open. The complete second
jets of PR49 remain valid finite-order witnesses, but cannot lift to this
matrix target under the boundary-spanning hypothesis.

```sh
python research/ai/2026-10-21-third-boundary-trap/verify.py --output-dir /tmp/third-boundary-trap
python -m unittest discover -s tests -p test_third_boundary_trap.py -v
```

Use root requirements.txt. Verification consists of exact source
contractions, rational kernels and independent nonzero minors, all fixed
radical identities, repeated determinant identities, and a sharp small
target-support control. The all-order assertion comes from the written
formal induction, not from a finite jet cutoff.

Canonical extension data, the moving polynomial boundary and the original
induction are credited to PR45/46. The repeated-minor strategy is credited
to PR48; this package supplies its new third-order tensor and certificate.
The generating Codex session performed the checks. No independent review
or formal proof verification is claimed.
