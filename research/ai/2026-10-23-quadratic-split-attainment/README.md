# Split and doubled quadratics attain every balanced rank over algebraically closed fields

October 23, 2026. Owner-directed Codex research. Written and unreviewed;
same-session checks are not independent mathematical review. No improved
matrix-multiplication exponent is claimed.

The [proof](proof.md) gives an exact all-field formula for the explicit
family

    q_t(x,z)=(z-x)(z-tx),      t nonzero,

in the full crossed source R_(a,b), with a,b>=3. Put epsilon=1 when
1+t+...+t^a=0 and epsilon=0 otherwise. Then

    kernel indices = (a-epsilon, a+epsilon),
    rank R_(a,b) = ab+2 min(a,b)-epsilon [a=b].

| Parameter case | When epsilon is one |
| --- | --- |
| t!=1: distinct factors | t^(a+1)=1 |
| t=1: doubled factor | Positive characteristic p divides a+1 |
| t=1 in characteristic zero | Never |

The index change from (a,a) to (a-1,a+1) lowers the rank only at
b=a. Every other integer width b>=3 has the same rank for both
index pairs.

Over every algebraically closed field and at every a>=3, these split
or doubled models attain rank a^2+2a-1. Together with the prior
containment and elementary witnesses for the other values, the exact
balanced nonzero rank set is

    {a^2, a^2+a, a^2+2a-1, a^2+2a}.

For a>3 this concerns quadratic-in-z slices with coefficient degrees
below a. It is not a full biform or cyclic-source classification.

## Why the criterion holds

The proof solves the full polynomial recurrence with first coordinates
P,Q. With S_r=1+t+...+t^(r-1), its r-th coordinate is

    lambda_r=x^(r-1)(S_r Q-t S_(r-1)xP).

The last two degree constraints force P=Q=0 when S_(a+1) is nonzero.
When it vanishes, they force P=0 and Q constant, giving exactly one
kernel direction. The finite-sum proof includes t=1 and characteristic
two without division by 1-t or by two. The previously merged index
formula then gives the rectangular rank.

The auxiliary recurrence is valid for n>=2, but the degree-two literal
source formula requires a>=3 and b>=3. At the excluded parameter
t=0 the primitive degree drops, and the rank becomes ab+min(a,b).
These boundaries are explicit in the proof and controls.

## Exact controls

[verify.py](verify.py) constructs the auxiliary recurrence and the
complete literal source independently, using exact standard-library
arithmetic. The saved
[report](../../../results/quadratic-split-attainment-2026-10-23/controls.json)
records:

- 29 field/parameter/size cases over Q, F2, F3, F5, and F4, including
  13 nonzero explicit kernel witnesses.
- 78 literal rectangular source comparisons at the available widths
  b=a-1,a,a+1, always retaining b>=3.
- Five separate source checks at the excluded parameter t=0.
- 24 additional auxiliary recurrence matrices at n=2,3, with eight
  explicit kernel witnesses. These are not source-rank claims at a=1,2.
- Distinct-factor, doubled-factor, characteristic-two, and extension-field
  cases. At a=8, the family has balanced rank80 for the sole nonzero
  F2 parameter and rank79 for an order-three parameter in F4.

The last comparison describes this explicit family only. It does not
exclude other binary biforms attaining rank79 at that size.

From the repository root:

```sh
python research/ai/2026-10-23-quadratic-split-attainment/verify.py --output /tmp/quadratic-split-attainment-controls.json
python -m unittest discover -s tests -p 'test_quadratic_split_attainment.py'
```

All nine focused tests pass, including source-pin checks, corrupted-witness
rejection, exact rational elimination, and F4 checks by binary restriction
of scalars. Finite replay corroborates the all-size proof. No algebraically closed
attainment claim is inferred from a finite field grid.

## Provenance and remaining scope

The [merged kernel-index package](../2026-10-23-quadratic-kernel-indices/README.md)
supplies the two-index rank formula and structural containment. Their
exact files and inherited external-source records are pinned in
[sources.json](sources.json). The new recurrence argument is written
directly and needs no additional external theorem or gluing convention.

Over Q, this family has a balanced defect exactly for t=-1 and odd a.
The proof does not settle general rational attainment. A previously
saved negative checked sixteen rational sign lifts of the binary
order-five support; it was preserved without rerunning it and is not
counted among this package's acceptance checks. That negative excludes
only those sixteen choices.

The results concern individual source slices. No linear source-space
bound, compatible three-leg map, tensor target, degeneration, or exponent
improvement is supplied. Review status remains written and unreviewed.
