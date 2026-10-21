# One Laurent leg with two regular leading maps

Written local proof, unreviewed. No historical priority or exponent improvement is claimed.

Let T be a tensor in A tensor B tensor C over a field k, with dim A=a.
Let P(t):B->B' and Q(t):C->C' have entries in R=k[[t]], with constant
maps P0,Q0 of ranks b0,c0. Let S(t) be the first-leg flattening of
(1 tensor P(t) tensor Q(t))T, an a-by-(dim B' dim C') matrix over R.
Put r=rank S(0). If H(t):A->A' has arbitrary Laurent entries and
U(t)=(H(t) tensor P(t) tensor Q(t))T is regular, then

    slice_rank U(0) <= a-r+min(b0,c0).                         (1)

The first-leg output dimension need not equal a. Both regular maps may
have arbitrary higher jets; only their constant maps occur in (1).

Proof. In K=k((t)), let L be the row span of S(t), of dimension d<=a.
Its saturated R-lattice Lambda=L intersect R^(dim B' dim C') is a free
rank-d module. Its reduction injects into the ambient residue space:
if x in Lambda lies in tR^m then x/t is again in Lambda, so
Lambda intersect tR^m=t Lambda. Thus its residue L0 has dimension d.

Every row of S(t) is in Lambda, hence L0 contains the r-dimensional row
space W0 of S(0). Moreover W0 is a subspace of im(P0) tensor im(Q0).
Choose a basis of L0 extending a basis of W0. The tensor representing
this full basis has at most d-r first-leg slices outside W0. Its W0
part has at most min(b0,c0) slices, expanding along either im(P0) or
im(Q0). Its slice rank is therefore at most d-r+min(b0,c0).

Every row of the regular matrix H(t)S(t) is also in Lambda, so its
constant row space is a subspace of L0. It is a first-leg restriction of
that basis tensor. Slice rank cannot increase under a restriction.
Using d<=a proves (1).

If r=a, a stronger statement follows: S(t) has a right inverse over R,
obtained from a unit maximal minor. Regularity of H(t)S(t) then implies
regularity of H(t) itself. In this case the limit is an ordinary
restriction, without hidden first-leg poles.

Slice-rank upper bounds are also preserved under further complex tensor
degenerations. Indeed slice rank <=s is a finite union, over sA+sB+sC=s,
of the tensors supported in

    UA tensor B tensor C + A tensor UB tensor C + A tensor B tensor UC,

for some subspaces of dimensions sA,sB,sC. This incidence condition is
closed; projection from the product of projective Grassmannians is
closed. This uses ordinary slice rank, not border rank or a claim about
slice rank of tensor powers.

## A matrix-space support condition

There is another necessary condition when U(0) is M(l,b,r0), with first
leg dimension l*r0. Here r0 is an outer matrix dimension, distinct from
the projected-source rank r above. Include every final output substitution
in the two regular maps before computing their constant ranks. Then

    r <= a-l*r0+floor(b0/b)*floor(c0/b).                   (2)

To see this, let Z be the l*r0-dimensional first-leg matrix space of the
target inside the saturated limiting space L0. Its intersection with W0
has dimension at least l*r0+r-a. The target matrices have the form
X tensor I_b. For a subspace E of such matrices, let I and J be the joint
column and row spaces of the corresponding X matrices, of dimensions
p and q. Their joint column and row spaces after tensoring I_b have
dimensions p*b and q*b. If E lies in W0, they lie in the two prescribed
leading images, so p<=floor(b0/b) and q<=floor(c0/b). Also dim E<=p*q.
Combining these inequalities gives (2).

This applies to arbitrary leading maps, not just the root families. In
particular, if either leading rank is less than b, the target matrix space
must avoid W0 and r<=a-l*r0. A construction search can test (2) before
computing higher jets. The condition does not itself supply any such jets.

# Certified root application

For the cyclic source A4, a=112. Let M(q) be the local rational matrix
in the quantum-recoupling package. For a cyclotomic polynomial Phi, put
nu=min_entries ord_Phi M. The matrix Phi^(-nu) M is regular at a
primitive root. Use its constant residue G as the prescribed initial
map on both B and C. The two full regular lifts need not equal M(q)
or each other. H(t) is completely unrestricted as a Laurent map.

Exact nonzero-row counts bound rank G from above. A nonzero modular minor
of the full projected source gives a characteristic-zero lower bound for
r. Reduction is justified by explicit nonvanishing denominators at a
root of Phi modulo the prime 786433. A nonzero residue minor is a
nonzero element of Q[zeta], and remains nonzero under every complex
embedding. Thus one certificate covers every common primitive complex
root of the stated order.

The resulting conservative bounds are:

    order Phi   rank G upper   projected rank lower   slice ceiling
      4             38               88                   62
      8             21               89                   44
     12             16               64                   64
     16             68              112                   68
     24             22               48                   86

All are below 100. Matrix multiplication M(10,10,11) restricts to square
M10, whose slice rank is 100. For this imported fact use Blasiak,
Church, Cohn, Grochow, Naslund, Sawin and Umans, arXiv:1605.06702v4,
Discrete Analysis 2017:3, Section 4.2, Remark 4.9, following Proposition 4.8. Their Theorem
4.6 states the general low-slice-rank instability criterion; the cited
paragraph applies it to square matrix multiplication.

Consequently none of these prescribed two-regular-leading-map families
can produce the size-four target, even allowing arbitrary higher jets
on the regular legs, arbitrary Laurent maps on the other leg, and a
subsequent tensor restriction or degeneration. This is not a barrier for
all root-dependent row weights, different leading flags, or joint
extraction from powers. Slice rank is not submultiplicative; no
asymptotic method ceiling follows from (1).
