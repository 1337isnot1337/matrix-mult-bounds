# Heisenberg source, finite coset class, and search normalization

AI-derived written proof, unreviewed. No target degeneration or smaller
exponent is constructed. This source differs from the SL(2,5), SL(2,7) and
affine-group lanes already maintained in the repository.
The elementary representation calculation rederives the standard finite
Heisenberg decomposition; no historical novelty is claimed.

The later [normal-coset incidence argument](normal_coset_closure.md)
excludes the entire single-target coordinate-potential source-cost route
at p=5. The source calculation below remains valid, while its conditional
target premise is excluded within that construction class.

## Source decomposition

For an odd prime p, write H_p={(a,b,c):a,b,c in F_p}, with product

    (a,b,c)(x,y,z)=(a+x,b+y,c+z+a*y).

Its center is {(0,0,c)}. Put x=(1,0,0), y=(0,1,0), z=(0,0,1).
Then x^p=y^p=z^p=1, z is central and [x,y]=z. Every element is uniquely
y^b x^a z^c, which also proves the displayed multiplication law and order p^3.

Let zeta be a primitive p-th complex root. There are p^2 linear characters
chi_(r,s)(a,b,c)=zeta^(r*a+s*b). For each nonzero k in F_p define

    (rho_k(a,b,c) f)(t)=zeta^(k*(c+b*t)) f(t+a).

Composing two such operators gives phase
c+c'+a*b'+(b+b')*t, so this is a representation of the stated group.
Its shift and diagonal phase operators generate every matrix unit: Fourier
polynomials in the diagonal isolate each basis vector, and powers of the
shift move it to every other basis vector. Thus rho_k is irreducible.
Distinct k have different central characters. Its character is zero except
at (0,0,c), where it is p*zeta^(k*c).

Equivalently, the central Fourier idempotents
e_k=(1/p) sum_c zeta^(-k*c) z^c split C[H_p] into p pieces of dimension p^2.
The k=0 piece is C[F_p^2], hence splits into p^2 scalars. For k!=0 the
shift/phase images of its p^2 group basis elements span M_p, so that piece
is M_p. This gives the complete decomposition without importing a character
table. The squared degrees sum to p^3.

At p=5 the degrees are twenty-five ones and four fives. The existing exact
root-interval gate gives

    sum d_i^(2247/1000) < (10^3)^(749/1000),

with source upper numerator 1738146170409 and target lower numerator
1766037820686 over 10^10. The credited group-algebra spectral conversion
therefore gives omega<2247/1000 if a degeneration to M(10,10,10) exists.
That premise is unconstructed. The existing necessary rank-locus screen
does not exclude it.

## Exact finite two-coset family

Choose a noncentral cyclic subgroup L of order five and an element g outside
its normalizer. Let S=L union gL. There are thirty such L and twenty allowed
left cosets gL for each L, giving 600 distinct sets of size ten. Their
projected supports in H_5/Z are unions of two parallel lines. Each has
eighteen nonidentity right quotients: four in L, four in gLg^-1, and five
in each of gL and Lg^-1. These sets are disjoint when g is outside N(L).

The standard first set is S0={(a,b,0):a in F5,b in {0,1}}. For any L,g
as above, choose a generator l of L. Its projected direction and that of g
are independent. The map

    (a,b,c) -> g^b l^a [l,g]^c

is a group automorphism: the presentation relations hold, its projected
map is invertible and [l,g] generates the center. It sends S0 to L union gL.
Hence common automorphisms normalize the first set of any triple in this
family to S0 while preserving the family and vertex-potential feasibility.

The finite enumeration finds ninety possible other sets whose right
quotients avoid those of S0. Among their 4095 unordered pairs (with
repetition), exactly 400 have disjoint quotient sets and therefore all
three cyclic pair maps injective. Every one of those 400 triples has two
opposite extra potential rows. The saved positive integer circuits reject
strict potentials. No linear-programming failure is accepted as evidence.

Exchanging the other two sets reverses each group relation after reversing
its three endpoint pairs; negating all potentials preserves strictness.
This covers the ordered cases as well. Together with the common
automorphisms, the finite certificate therefore excludes the entire stated
two-left-coset family. It does not classify arbitrary central colors above
the same projected lines, other projected supports, or arbitrary tensor
degenerations. The separate colored-line pilot returned untraced UNSAT;
that solver report is not a proof of a larger exclusion.

## Necessary conditions for the broader search

For any central coset subset S0 of a selected set, the map
(s,t,u) -> s*t^-1*u on S0 times T times U is injective. Indeed, translate
S0 into the center. A nontrivial collision gives right quotients
c*qT*qU=1 with c central. Then qT and qU commute, so the reversed quotient
relation also holds. The two strict potential rows are opposites,
contradicting positivity. Pair-map injectivity handles collisions with an
unchanged endpoint. Consequently |S0|*|T|*|U|<=|H_p|.

For the size-ten target at p=5, 2*10*10>125, so all three selected sets
are center-free and have ten distinct projected points in F5^2.

Each of the six one-dimensional quotient directions gives an abelian
normal subgroup of order 25. By the maintained abelian-coset theorem, the
product of the three largest affine-line intersections in that direction
is at most 25. All three maxima are at least two. The allowed sorted
maxima are precisely (2,2,2), (2,2,3), (2,2,4), (2,2,5), (2,3,3), (2,3,4).
In particular some leg has maximum two in each direction. With ten points
on five parallel lines, maximum two means every line contains exactly two.

Six directions covered by three legs force one leg to be balanced in two
different directions. Leg permutation and a common group automorphism
place it first and send those directions to horizontal and vertical.
Independent right translations then put identity in every set; they
preserve directional balance. This justifies the first projection's row
and column sums of two in general_search.py. The search still accepts
only a complete integer group-potential witness. Its absence, or any
untraced solver refutation, is not a nonexistence theorem.
