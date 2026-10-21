# A low-rank spanning certificate freezes the second partial space

AI-assisted research, October 21, 2026. Written proofs are unreviewed.
**No exponent improvement is established.**

The canonical four-row quantum flags have a twelve-dimensional leading
first-slice space. PR45 classifies their compatible changed first jets
and bounds the second partial space by37. The new
[spanning proof](rank_one.md) sharpens that conclusion to equality:

    W2=W1=W0, with dimension12.

Twenty-six explicit rank-two slices span the entire25-dimensional canonical
bilinear second-jet image. Each has a complete rational factorization and
a nonzero2-by2 minor; a25-by25 minor certifies their span. The full second
coefficient differs from this image only by an old matrix cross of rank
at most8. A matrix-target slice has rank at least11. Since2+8<11, every
second residue in the target must vanish. This includes both second
matrix derivatives and the first-row correction.

Consequently the actual bilinear tensor of the two new-row first jets
must vanish. Exact [matrix blocks](boundary_spanning.md) yield further
restrictions: the sum of the effective first-row ranks is at most24,
or at most20 if either has a mixed component. In the boundary-spanning
family, neither first derivative can contain a mixed component. These
[rank-sum constraints](rank_deficit.md) hold for subspaces with arbitrary
graphs between boundary and mixed coordinates.

The theorem allows ungraded derivatives, arbitrary higher jets and an
arbitrary Laurent first-leg map. It requires the stated final rank-four
leading flags and the target with leg dimensions100,110,110. Growth from
order three onward, other leading flags and projections reducing the
leading images remain open. The result supplies no tensor construction,
tensor-power ceiling or exponent improvement.

```sh
python research/ai/2026-10-21-second-jet-rank-one/verify.py --output /tmp/second-jet-certificates.json
python -m unittest discover -s tests -p test_second_jet_rank_one.py -v
```

The verifier uses root requirements.txt. It replays the canonical extension
basis and completeness ranks with their original credit, checks all root
normalizations over Q(zeta_6), reconstructs the full integer tensor,
certifies the new matrix-block identities and all low-rank spanning
factorizations. Tests separately reconstruct every one of40,000 tensor
coefficients from a fixed-index formula. These checks support written
proofs; generation and replay are by the same Codex session, with no
independent mathematical review claimed.
