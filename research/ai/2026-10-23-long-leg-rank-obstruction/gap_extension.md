# The source rank gap excludes long leading rank at least 106

October 23, 2026. Written and unreviewed. A second agent checked the
argument in the same generating session; this is not external independent
review or formalization. This is an obstruction for a specified Laurent
chart. No smaller exponent or degeneration is constructed.

Claim `AI-A4-GAP-LONG-106-003`.

## Statement and dependencies

Over the complex Laurent field, there is no complete degeneration

    A4 -> M(10,10,11)

whose 112-by-110 long map C is regular and has rank at least 106 at zero.
The other long map and the first map may have arbitrary finite Laurent
poles. The statement is symmetric in the two long legs.

The residual argument is the one independently derived in this session
and concurrently recorded in PR113, head
08ac3e983e270cf3df4e26d960ceb16415f7ef31. The new continuation uses the
previous source note
`research/ai/2026-10-20-anisotropic-constructions/slice_rank_gap.md`:
every nonzero A4 slice has rank 16 or at least 20, and the rank-16 locus is

    u tensor h(alpha,beta) tensor v,
    h(alpha,beta)_k=alpha^(6-k) beta^k,  0<=k<=6,

with u,v nonzero vectors in C^4. That source proof uses the splitting
theorem for vector bundles on P^1. Its existing provenance and proof
status must be retained if this continuation is packaged.

## 1. The regular kernel residual

Let E=Mat_10 and Xi(X)=X tensor I_11. Write the full Laurent identity as

    B(t) M(F(t)X) C(t) = Xi(X)+O(t),

where B has size 110-by-112, C has size 112-by-110, and M is the linear
A4 slice map with values in the 112-by-112 matrices.

Multiply F by a scalar power of t and B by the inverse scalar so that
F is regular and F0 is nonzero. This does not change C. Choose an
invertible V in Mat_10 with F0(V) nonzero. Such a V exists since a nonzero
linear map cannot vanish on the dense open set of invertible matrices.

Put S=M(F(V)), H=Xi(V)^(-1), and G=B S C H. The full Laurent identity
implies G=I+O(t). Replace B by G^(-1) B and set D=S C H. Then D is regular,
B D=I exactly, and the normalized target family T_X=B M(F(X)) C is regular
with T_X(0)=Xi(X). The matrix

    W_X=M(F(X)) C-D T_X

is regular and satisfies B W_X=0. Since B has full row rank 110 over the
Laurent field, its kernel has dimension two. Thus rank W_X<=2 over that
field, and the same bound holds at zero by specializing the 3-by-3 minors.
Consequently

    M(F0(X)) C0 = D0 Xi(X)+W_X(0),
    rank W_X(0)<=2.                                      (1)

Set r=rank C0 and d=112-r. For rank-one X, the rank of Xi(X) is 11, so

    rank M(F0(X)) <= rank(M(F0(X)) C0)+d
                  <=11+2+d.

When r>=106, we have d<=6 and this upper bound is at most 19. The source
rank gap therefore implies that F0(X) is zero or belongs to the rank-16
minimum-slice cone for every rank-one X.

## 2. Every target ruling fixes the coherent middle direction

We use the following elementary observation. A linear subspace contained
in the affine cone

    {u tensor h(alpha,beta) tensor v}

has a fixed middle line whenever it is nonzero. To prove it, suppose
two nonzero members have distinct middle lines. Regard their outer
factors as vectors w=u tensor v. A sum of two pure tensors across the
middle/outer split can be pure only if their outer vectors are
proportional. Every vector in their two-dimensional span would then
require the projective line joining the two coherent middle vectors to
lie on the degree-six rational normal curve. That curve contains no
projective line. Indeed, a projective change of the two binary variables
sends the two distinct points to alpha=0 and beta=0; the sum of the two
endpoint monomials has two nonzero endpoint coefficients and zero
intermediate coefficients, and is not a sixth power. This contradiction
proves the observation.

For each nonzero a in C^10, the space

    F0(a tensor C^10)

is linear and all its nonzero elements are minimum slices. If the space
is nonzero, the observation fixes a middle line h_a. Take any two such
a,a'. There is a b outside the union of the two proper linear kernels of
F0(a tensor -) and F0(a' tensor -). The nonzero vectors F0(a tensor b) and
F0(a' tensor b) lie in the single linear subspace

    F0(C^10 tensor b),

so their middle lines coincide. It follows that all nonzero a-rulings
have the same middle line h0. Since pure target tensors span E,

    F0(X)=Psi(X) tensor h0

after reordering the three source factors, where Psi:Mat_10 -> Mat_4 is
linear and sends rank-one matrices to rank-at-most-one matrices.

## 3. An elementary classification of the required preservers

Let Psi:A tensor B -> U tensor Z be linear and send every pure input to
a pure output or zero. Then either its whole image is in a fixed-factor
linear space, or

    Psi(a tensor b)=f(a) tensor g(b),                  (2)

or

    Psi(a tensor b)=f(b) tensor g(a),                  (3)

for linear maps of the displayed types. A fixed-factor space means
u0 tensor Z or U tensor z0. The statement includes maps with zero images.

Here is a direct proof over C. A sum of two nonzero pure tensors is pure
exactly when their first factors or their second factors are dependent.
If every pair of nonzero pure outputs shares one factor, all outputs
share the same factor: fix u1 tensor z1; every other output shares u1 or
z1. If an output u2 tensor z1 has u2 independent of u1, every output
sharing u1 but not z1 would be incompatible with it. Hence all outputs
share z1. If no such output exists, they all share u1. As pure inputs
span the domain, this gives the fixed-factor case.

Otherwise choose inputs a1 tensor b1 and a2 tensor b2 with outputs
u1 tensor z1 and u2 tensor z2, where u1,u2 and z1,z2 are independent.
Then a1,a2 and b1,b2 must also be independent. The cross outputs
Psi(a1 tensor b2) and Psi(a2 tensor b1) must each lie in one of the two
crossed lines u1 tensor z2 and u2 tensor z1, or be zero. This follows by
comparing each cross output to the two diagonal outputs along its two
input rulings.

Apply the rank-one condition to

    Psi((a1+s a2) tensor (b1+t b2)).

Its 2-by-2 determinant in these output bases shows that both cross
outputs are nonzero, they occupy opposite crossed lines, and their two
coefficients multiply to one. Rescaling u2,z2 and, when necessary,
exchanging the output factors reduces to

    Psi(ai tensor bj)=ui tensor zj,  i,j in {1,2}.    (4)

For an arbitrary a, the image of A tensor b1 is a linear space of pure
tensors containing u1 tensor z1 and u2 tensor z1. Hence it is in
U tensor z1. Similarly the image of A tensor b2 is in U tensor z2. Write

    Psi(a tensor b1)=f1(a) tensor z1,
    Psi(a tensor b2)=f2(a) tensor z2.

The maps f1,f2 are linear, agree on a1,a2, and have pointwise dependent
values because Psi(a tensor (b1+b2)) is pure. Polarizing
f1(a) wedge f2(a)=0 against ai gives

    (f1(a)-f2(a)) wedge ui=0,  i=1,2.

As u1,u2 are independent, f1=f2=:f. The same argument in the other
direction gives a linear g with

    Psi(a1 tensor b)=u1 tensor g(b),
    Psi(a2 tensor b)=u2 tensor g(b).

If f(a) and g(b) are nonzero, the a-ruling and b-ruling descriptions
give Psi(a tensor b)=c f(a) tensor g(b). Choose i for which ui and f(a)
are independent. Comparing the a+ai ruling with the sum of the a and ai
outputs forces c=1. If f(a)=0, the a+ai ruling has the two independent
outputs ui tensor z1 and ui tensor z2, so all of it lies in ui tensor Z.
Subtracting Psi(ai tensor b)=ui tensor g(b) therefore puts
Psi(a tensor b) in ui tensor Z for both i=1 and i=2. Their intersection
is zero. The case g(b)=0 is analogous. This proves (2), and undoing
the possible output-factor exchange gives (3).

For A=B=C^10 and U=Z=C^4, the two factored cases are, in matrix notation,

    Psi(X)=P X Q^T   or   Psi(X)=P X^T Q^T,

where P,Q have size 4-by-10. The classification is supplied here rather
than imported as an external linear-preserver theorem. No priority for
the classification itself is claimed.

## 4. Such a preserver always has an invertible matrix in its kernel

In a fixed-factor case, rank Psi<=4, so dim ker Psi>=96. A singular
linear subspace of Mat_10 has dimension at most 90; the elementary
block proof is already supplied in the corank-one note. Therefore
ker Psi contains an invertible X.

In the case Psi(X)=P X Q^T, put p=rank P<=4 and q=rank Q<=4. Since

    dim im Q^T=q <=10-p=dim ker P,

there is an invertible linear map X:C^10 -> C^10 carrying im Q^T into
ker P. Construct it by choosing an injection of a basis of im Q^T into
ker P and extending both selected lists to bases of C^10. Then
P X Q^T=0. The transpose case follows by transposing this invertible
matrix. Thus ker F0 contains an invertible matrix in every case.

## 5. Contradiction with the residual

Recall that V was chosen invertible with F0(V) nonzero. Every nonzero
source slice has rank at least 16, so

    rank D0=rank(M(F0(V)) C0 H)>=16-d>=10.

For an invertible X in ker F0, equation (1) instead gives

    D0 Xi(X)=-W_X(0),

whose right side has rank at most two. Since Xi(X) is invertible, this
forces rank D0<=2, a contradiction.

## Scope and next boundary

The argument excludes every regular long-map leading rank at least 106
for this target, allowing arbitrary finite Laurent poles in the other
maps. It does not make basis-dependent leading ranks invariant under
arbitrary singular changes of basis. It does not settle the full
degeneration problem.

At leading rank 105, d=7 and the rank-one residual bound becomes 20.
The prior gap permits rank 20, so the minimum-locus preserver reduction
no longer follows. This is the first rank left open by this argument.

