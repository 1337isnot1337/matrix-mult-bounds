# Finite kernel types for the paired long-leg map

This note extracts representation structure from the exact finite rank
atlases. It is a finite computation, not an all-size rank theorem.

Set `D=a-1` and let `U,V` be two-dimensional vector spaces. In divided-power
monomial bases, the coefficient condition
`x+y=z` and `q+v=j` identifies the paired tensor with the product of the two
binary-form multiplication tensors. One compatible `SL2 x SL2` convention is

```text
A = Sym^D(U) tensor Sym^D(V*)
B = Sym^D(U) tensor Sym^(2D)(V)
C = Sym^(2D)(U*) tensor Sym^D(V*).
```

Thus the Koszul map is equivariant. With the monomial of index `i` in
`Sym^d` assigned torus weight `2i-d`, its source weight at the atlas grade
`(g1,g2)=(sum(y)-x, sum(j)+q)` is

```text
w_U = 2*g1 - (p-1)*D
w_V = 2*g2 - (2*p+1)*D.
```

Each exact block contributes kernel weight multiplicity
`columns - rank_over_q`. The script `kernel_representation.py` recovers
irreducible multiplicities by taking finite differences in the two weight
coordinates. The symmetric weight tables and the direct-sum dimensions are
checked by the script.

The exact finite decompositions are:

* `(a,p)=(2,3)`: `Sym^0(U) tensor Sym^3(V)` once and
  `Sym^0(U) tensor Sym^5(V)` once, totaling dimension 10.
* `(a,p)=(3,7)`: for first-factor highest weight 0, the multiplicities of
  `Sym^(2t)(V)` for `t=0,...,10` are
  `[3,1,5,3,6,3,5,2,3,1,1]`. For first-factor highest weight 2, the
  multiplicities for `t=1,...,9` are `[2,1,2,1,2,1,2,1,1]`. Their total
  dimension is 730.

The first defects at `a=2,p=3` and `a=3,p=7` are consistent with the
conjectural boundary `p=a(a-1)+1`. The `a=4,p=5` control is only one injective
point and does not test that boundary. No all-size claim follows.

Reproduce the source atlases and decomposition with:

```text
python research/ai/2026-10-23-paired-long-legs/rank_atlas.py --a 2 --powers 3 --output results/paired-long-legs-2026-10-23/graded-rank-atlas-a2-p3.json
python research/ai/2026-10-23-paired-long-legs/rank_atlas.py --a 3 --powers 4 5 6 7 --output results/paired-long-legs-2026-10-23/graded-rank-atlas-a3.json
python research/ai/2026-10-23-paired-long-legs/kernel_representation.py --input results/paired-long-legs-2026-10-23/graded-rank-atlas-a2-p3.json results/paired-long-legs-2026-10-23/graded-rank-atlas-a3.json --output results/paired-long-legs-2026-10-23/kernel-decomposition-a2-p3-a3-p7.json
```
