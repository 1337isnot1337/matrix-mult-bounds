# Rank-four obstruction and first quotient ranks at least thirteen

Written proof, unreviewed, October 21, 2026. This strengthens the
[maximal-first-extension theorem](proof.md), using its source conventions
and formal induction. It does not establish a smaller exponent.

## 1. The two obstruction matrices

After the 220 first normal constraints, there are 228 parameters for
the leading-row normal error D. Section 2 of the preceding proof defines
two linear maps

    Psi_B(D): E_B/G -> coker{ b' -> T(K,b',G) },
    Psi_C(D): E_C/G -> coker{ c' -> T(K,G,c') }.

Each is a 200-by-16 matrix linear in D. For example its B column at b
is the class of T(K,b,D_C)-T(y,b,G). A correction b' exists precisely
when that column vanishes. The previous certificate shows that the
common kernel in D of both complete matrices consists of the four
polynomial-plane directions.

We now prove that each matrix, whenever nonzero, has rank at least four,
over C. The statement concerns every value of D, not a finite parameter
sample.

## 2. A finite certificate for all parameters

For either matrix, the frozen certificate supplies three rounds of
four-by-four triangular minors. In each selected minor all entries above
the diagonal vanish identically and the four diagonal entries are nonzero
rational multiples of one linear form L. Its determinant is therefore

    c L^4,     c in Q, c != 0.

If the matrix had rank at most three at D, every such L would vanish.
Restrict the parameters to the simultaneous kernel of these linear forms
and repeat. The exact counts on both sides are

| Round | Parameter dimension | Rank of forced linear equations | Remaining dimension |
| --- | ---: | ---: | ---: |
| 1 | 228 | 82 | 146 |
| 2 | 146 | 42 | 104 |
| 3 | 104 | 16 | 88 |

After the third restriction every entry of the obstruction matrix is
identically zero. Thus rank at most three implies rank zero, proving
the claimed minimum nonzero rank four. All nullspace restrictions are
over Q and are full kernels, so they do not discard complex solutions.
No floating-point zero or finite-field upper-rank inference is used.

`minimum_rank.py` reconstructs the coefficient matrices, checks the
triangular zero identities and repeated diagonal forms, and performs
the exact kernel restrictions. The saved report lists every minor and
linear form. The tests also replay those saved identities and kernels
without running the minor search, and reject a corrupted zero identity.

The auxiliary rank bound is sharp: normal parameter 90 in the saved
canonical coordinates gives B rank four and C rank zero. This is a
linear-obstruction control, not a completed source-jet construction.

## 3. Consequence for arbitrary first-extension subspaces

Suppose the first new rows span subspaces V_B of E_B/G and V_C of E_C/G,
each of dimension at least thirteen. In the formal induction of the
preceding proof, the next off-diagonal equations say that Psi_B(D)
annihilates V_B and Psi_C(D) annihilates V_C. A linear map with
16-dimensional domain and a kernel of dimension at least thirteen has
rank at most three. The minimum-rank certificate therefore forces

    Psi_B(D)=Psi_C(D)=0.

The old four-direction lemma now applies to D. The same plane correction
and induction confine the full output maps to moving spaces of dimension
56, contradicting the two 110-dimensional concise target legs.

Consequently any possible M(10,10,11) construction with the normalized
rank-four leading flags must have first quotient rank at most twelve
on at least one side. This includes arbitrary subspaces of the stated
dimensions, not just coordinate omissions or sampled hyperplanes.

The proof's threshold thirteen comes from the sharp auxiliary rank-four
bound. This does not assert that lower-rank jets can produce the target.
Their other coefficient equations, delayed growth, leading-rank losses,
and different leading flags remain open. The first-extension and
partial-saturation sources are credited in the package's source record.
