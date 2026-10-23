# Sharp common-divisor caps for unequal cyclic sources

October 23, 2026. Owner-directed Codex work, written and unreviewed.
No independent review, formalization, historical priority or exponent gain.

## 1. Statement

Work over C. Let `2<=a<=b`, let `d>=1` divide both `a,b`, and write
`p=a/d`, `r=b/d`. Put `m=a+b-1` and `N=abm`. In the canonical cyclic
source `A(a,b)`, every first-leg parameter `F` gives an `N` by `N` matrix

```
M(F)_((j,u,L),(H,v,t)) = F_(H-j,u+v,L-t),
```

where `j,v<b`, `u,t<a`, and `H,L<m`; source coordinates have
`i<a`, `k<m`, `s<b`. All indices are nonnegative and an out-of-range
coefficient is zero. For every integer `q` in the interval

```
a(b+d-1) <= q < a(b+d),
```

the maximum dimension of a complex linear space `V` such that
`rank M(F)<=q` for every `F in V` is exactly `bd`.

There is no coordinate, homogeneity or fixed-middle-factor assumption
on `V`. All source sizes and common divisors are quantified. The endpoint
`d=a`, when `a` divides `b`, is included. At `a=b,d<a` this recovers the
balanced theorem of PR148, whose argument and attribution are retained.

Examples are `(a,b,d)=(4,6,2)`, with cap 12 at ceilings 28--31;
`(6,9,3)`, with cap 27 at ceilings 66--71; and `(4,8,4)`, with cap 32
at ceilings 44--47. These are source-space statements, not matrix-target
constructions.

## 2. Coordinate specialization and middle extremes

Use weights `w(i,k,s)=i+a*k+a*m*s`. They are distinct integers from
zero through `N-1`. The diagonal action with multiplier `z^w` factors
on each source matrix entry into the row multiplier
`z^(-j+a*u+a*m*L)` and column multiplier `z^(H+a*v-a*m*t)`.
For nonzero `z` it therefore preserves matrix rank.

Choose a reduced row-echelon basis for `V` in increasing weight order.
Divide each transformed basis vector by its pivot multiplier. Every
entry is polynomial in `z` and the value at zero is the pivot coordinate.
The distinct pivots preserve dimension. For every fixed linear
combination, its `(q+1)`-minors vanish for every nonzero complex `z`,
and hence at zero. Thus `V` specializes to a coordinate space of the
same dimension lying in the same rank ceiling. This reconstructs PR148's
torus method in the unequal source convention.

A coordinate at middle index `k` has rank `ab h_k`, where `h_k` counts
the pairs `u+v=k` with `u<a,v<b`. Since `a>=2`, exactly the two endpoint
indices `k=0,m-1` have `h_k=1`; every other one has `h_k>=2`.
Also `d<=a<=b`, so `q<a(b+d)<=2ab`. Only the endpoints can occur.
A sum of one nonzero coordinate from each endpoint has rank `2ab`,
because both its row and column blocks are disjoint. Therefore a
bounded-rank coordinate space is entirely at one endpoint.

At either endpoint, discard zero rows and columns to get the biform
matrix

```
R_(a,b)(g)_((j,L),(H,t)) = g_(H-j,L-t),
```

with `j<b,t<a,H,L<m`. It suffices to bound its coordinate subspaces.

## 3. A rectangular partition into bd forbidden-pair classes

For a grid point `(i,s)`, retain the residues
`rho=i mod d`, `sigma=s mod d`. Write `I=(i-rho)/d`,
`J=(s-sigma)/d`, so `0<=I<p` and `0<=J<r`. Label the point by

```
(rho, sigma, (J-I) mod r).
```

There are exactly `d^2*r=bd` labels. Each class has exactly `p` points:
for every `I`, the unique `J` is `(I+label) mod r`. For two distinct
members, both original coordinates differ. Indeed their first quotients
differ by an integer with absolute value less than `p<=r`, so their
second quotients cannot be equal modulo `r`. Both differences are
nonzero multiples of `d`. Unlike an orbit of simultaneous translation
on a rectangle, these classes never repeat a row before a column.

Suppose `p>=2` and take two points in a class. Remove their common
coordinatewise monomial factor. This translates output row and column
indices without truncating them: every original product index lies in
the full range through `a+b-2`. The resulting binomial is either

```
1+x^(alpha*d) z^(beta*d)   or   x^(alpha*d)+z^(beta*d),
```

where `1<=alpha<p`, `1<=beta<r`. Split the matrix by the residues of
`j,H` and of `L,t` modulo `d`. Each of the `d^2` nonzero blocks is
`R_(p,r)` of the reduced binomial, with possible extra zero rows or
columns. In each residue, the input `j` has exactly `r` indices and
the input `t` exactly `p`. All output indices through `p+r-2` occur;
any extra index `p+r-1` carries only zero entries.

The existing complex biform lemma in
`../2026-10-20-anisotropic-constructions/slice_rank_gap.md`, section 1,
states that a nonseparable `p` by `r` biform with `2<=p<=r` has rank
at least `pr+p`. Our two coefficients are in distinct rows and columns,
so the binomial is nonseparable. The pair consequently has rank at least

```
d^2(pr+p) = ab+ad = a(b+d).
```

Such a pair cannot lie in the coordinate space. There is at most one
coordinate per label, giving dimension at most `bd`.

If `p=1`, every class is a singleton, and the same bound is just the
number `ab=bd` of all coordinates at one middle endpoint. The biform
gap is not applied with a forbidden parameter `p=1`. This covers `d=a`.

## 4. Attainment and strict endpoints

At `k=0`, take the full strip `0<=i<d`, `0<=s<b`. It has dimension
`bd`. Its only possibly nonzero columns have `v=0`, `0<=H<=b+d-2`
and `0<=t<a`. There are `a(b+d-1)` such columns. Every linear
combination has rank at most that number. The strip attains the upper
dimension bound for every ceiling in the stated interval.

The upper endpoint is strict: the pair exclusion uses rank at least
`a(b+d)`. No cap is claimed there or for non-common-divisor widths.
The statement concerns the dimension of a bounded-rank linear space;
it does not assert that every nonzero element of the attaining strip
has the largest allowed matrix rank.

## 5. Regular-long-leg consequence

Let `Xi(X)=X tensor I_n` for `X in Mat_h(C)`, put `R=hn<=N`,
and let `k=N-R`. A complete Laurent degeneration of this source to
that target cannot have a regular long map `C` of limiting rank `R-c`
if

```
h > bd,       n+2k+c < a(b+d),       ab > 3k+c.       (*)
```

The other maps can have arbitrary finite poles. This extends PR148's
stated balanced corollary by replacing its source minimum, rank threshold
and dimension cap with `ab`, `a(b+d)` and `bd`.

For completeness, balance the first map `F` against the opposite long
map `B` so that `F` is regular and `F_0` is nonzero. Write
`Y_X=M(F(X))C`, `D=Y_I`, and normalize `B` by the regular inverse of
`BD=I_R+O(z)` to obtain `BD=I_R` exactly. Then `Z_X=BY_X` is regular
with constant term `Xi(X)`. The correction
`W_X=Y_X-D Z_X=(I_N-DB)Y_X` is regular and has generic rank at most
`k`, since the projection has image `ker B`. Its rank at zero is also
at most `k`, even if the projection itself has poles.

Thus `M(F_0(X))C_0=D_0 Xi(X)+W_X(0)`. For rank-one `X`, the lifted
source slice has rank at most `n+2k+c`: the target term has rank at
most `n`, the correction at most `k`, and multiplication by `C_0`
loses at most `k+c` additional ranks. The source minimum is `ab`,
because a nonzero source slice has a nonzero biform block, whose rank
is at least `ab` by the same existing lemma. If the lift is nonzero,
then `rank(D_0 Xi(X))>=ab-2k-c>k`.

Choose `u` with some nonzero `F_0(uv^T)`; one exists because rank-one
matrices span all parameters. For that `u` and every nonzero `v`,
`D_0((uv^T) tensor I_n)` has the same image as `D_0(u tensor I_n)`.
A nonzero `v` with zero lift would force its rank to be at most `k`,
contradicting the previous strict inequality. Therefore the entire
`h`-dimensional ruling injects into the bounded-rank source space.
The cap `bd<h` is a contradiction. This proves (*).

For `A(4,6)`, `h=14,n=15,N=216,k=6,d=2`, the conditions exclude
`c<=4`, that is, a regular long limit of rank at least 206. This is
only an illustration of the corollary, not a claim of a new complete
frontier or a target that improves the exponent.

## 6. Provenance and verification scope

The canonical unequal source and complex biform gap are existing main
results. Their original credits and written-unreviewed status remain.
The biform gap imports Grothendieck's splitting theorem as documented
in that source. PR148's balanced divisor partition, PR129's torus and
ruling method, and PR113's unit-kernel correction retain their credit.
The current contribution is the rectangular class partition, its sharp
common-divisor application, endpoint `d=a`, and corresponding unequal
source substitution in the reconstructed Laurent argument.

The all-size statement follows from the proof, not from a finite census.
Exact controls separately check the partition, literal residue identities,
rank minors, attaining strip supports and boundary examples. They do not
constitute independent mathematical review or formalization. No exponent
improvement is established.
