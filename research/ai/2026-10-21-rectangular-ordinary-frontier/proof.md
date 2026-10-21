# The ordinary rectangular frontier for balanced cyclic sources

Finite application of existing local theorems, October21,2026. AI-assisted,
unreviewed. No new general rank-locus theorem or smaller exponent is claimed.

## 1. Imported results and the stale research question

The original cyclic-target report used the minimum source slice rank and
its equality locus. It left four ordinary A5 targets after those gates.
The later `polynomial_rank_locus.md` already excludes all four, explicitly
including rectangular blocks. Its theorem describes every source slice
below twice the minimum and its argument propagates over matrix Segre
rulings. This package adopts that existing result; it does not claim that
classification or its proof as new work.

The maintained `hankel_symbol_dimension.md` also states its rectangular
consequence. Its permitted-rank and first-boundary refinements had been
applied exhaustively to square direct sums. Here they are applied to
single rectangular blocks of balanced A_a, retaining their original
hypotheses and credited proof status.

## 2. Necessary inequalities

Let N=a^2(2a-1) and consider an ordinary restriction to M(l,h,n), with leg
dimensions lh,hn,nl. Target conciseness forces all three source maps to
be surjective. A rank-one parameter on its lh-dimensional leg has slice
rank n. Its source lift therefore has rank at most

    R=n+(N-hn)+(N-nl).                                  (1)

All following gates are applied cyclically to the three target legs.
The source is symmetric for balanced a, so sorted shapes suffice.

The minimum source slice rank a^2 requires R>=a^2. The imported polynomial
rank-locus theorem gives

    lh>a^2  implies  R>=2a^2.                           (2)

For every integer1<=r<a with3r<=2a-1, the imported Hankel symbol theorem gives

    lh>r*a^2  implies  R>=(r+1)*a^2.                    (3)

At exactly2a-1=3r-1, r>=2, the imported first-boundary theorem instead gives

    lh>max(r,4)*a^2  implies  R>=(r+1)*a^2.              (4)

These are necessary conditions for ordinary restrictions. In particular,
(2)--(4) cannot be applied to arbitrary singular degenerations. They do
not make a surviving format sufficient.

## 3. Complete finite enumeration

The source range is the eleven integers a=2,...,12. For each a, enumerate
all positive l<=h<=n with hn<=N. Since h>=l and h^2<=hn, it is enough to
loop l<=h<=floor(sqrt N), and h<=n<=floor(N/h). All three pair products
are then at most N. A format is potentially improving under the previously
established finite spectral criterion precisely when

    216*l*h*n > (6a-2)^4.                               (5)

Every comparison in the driver is an integer comparison. For every such
format it stores either an explicit violated necessary inequality or the
fact that none of these gates excludes it. The finite scan covers5139
improving shapes. It excludes4192 and leaves947 necessary-test survivors.
It proves no statement about a>12.

| a | Improving shapes | Excluded by these gates | Survivors |
|---|---:|---:|---:|
| 2 | 0 | 0 | 0 |
| 3 | 0 | 0 | 0 |
| 4 | 1 | 1 | 0 |
| 5 | 7 | 7 | 0 |
| 6 | 14 | 14 | 0 |
| 7 | 55 | 55 | 0 |
| 8 | 154 | 153 | 1 |
| 9 | 356 | 345 | 11 |
| 10 | 732 | 609 | 123 |
| 11 | 1356 | 1087 | 269 |
| 12 | 2464 | 1921 | 543 |

The first balanced source that survives is A8, with leg dimensions960.
Its sole sorted survivor is

    M(27,28,28),    leg dimensions756,784,756.            (6)

This is a different target from the existing square direct-sum survivor
M27 plus M7. Neither construction is supplied, and no implication between
the two unproved premises is asserted.

## 4. Conditional spectral implication

The finite spectral implication is imported from `cyclic_finite_target.md`.
If A_a degenerates to M(l,h,n), it gives

    omega <= 9 log(6a-2)/log(216*l*h*n).                  (7)

For(6), volume=21168 and216*volume=4572288. The exact integer check

    4572288^191 > 46^765,       4*191<9*85               (8)

certifies that the premise would imply omega<=191/85<9/4. The premise
is unproved. The scan does not establish that exponent, tensor maps,
a strict global character gain, or independent mathematical review.

## 5. Coverage and verification limits

The report retains every improving sorted format, its three leg dimensions
and the first exclusion witness when one exists. Tests separately count
all candidate intervals, replay every inequality over all target
permutations, verify the sole a8 survivor, check the conditional integer
certificate and reject a corrupted exclusion witness. The underlying
rank-locus and Hankel theorems retain their existing written, unreviewed
status and exact source pins.

The scan covers balanced cyclic sources and single rectangular blocks.
It is not an exclusion of unbalanced sources, rectangular direct sums,
tensor-power constructions or general degenerations. The small singular
A4 target therefore remains a separate construction question despite the
absence of ordinary survivors through a7.
