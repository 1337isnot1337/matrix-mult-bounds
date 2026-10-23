# Checkpoint: elementary biform proof

Base: main3008d70. PR186. Isolated worktree:
`/home/cinna/matrix-mult-elementary-biform-d83f`.

Written: arbitrary characteristic-zero biform block gap without bundle
splitting; exact mixed-linear power rank a(b+e); mixed-factor multiplicity
lower bound ab+ae. Both registered claims remain written and unreviewed.
Seven focused tests and nine metadata/archive tests pass at350f9e0.
Receipt: results/elementary-biform-gap-2026-10-23/validation.json.
All287 prior claims and23 archive files are unchanged from main.
Current-head hosted CI is a separate pending merge gate.

The corollary in linear_factor_powers.md now proves exact rank a(b+e)
for f=U(x)V(z)h^e when h is one irreducible mixed factor linear in x.
Both univariate removals preserve crossed rank by injective multiplication
on the complete output images. Three additional tests pass, covering
five nonlinear/decorated instances, singular truncated multiplication
matrices and a two-distinct-factor boundary of rank14 rather than15.

Next: record the additive validation receipt, refresh PR186, and await
current-head required CI. A broader positive-characteristic gap proof
would need a separate treatment of inseparable factors and vanishing
integer minors. Do not infer it from this characteristic-zero argument.

No full target maps or improved exponent are established.
