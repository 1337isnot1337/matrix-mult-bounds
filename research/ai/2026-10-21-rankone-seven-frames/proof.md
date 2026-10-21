# Maximal rank-one mixed frames force a moving boundary

Written proof, unreviewed, October 21, 2026. This is a local degeneration
exclusion and a necessary first-rank bound, not an exponent improvement.

At the canonical four-row leading flags of the cyclic A4 source, suppose
both first mixed projections have rank one and both effective first spaces
have dimension seven. Allow arbitrary complex first subspaces, all their
boundary graphs, arbitrary higher regular output maps, and an arbitrary
Laurent first map. The two first-growth orders may be different positive
integers. No such maps yield M(10,10,11).

The complete first normal equations already force the four common-plane
directions. Thus the moving-boundary induction applies without a further
third-block rank calculation. In particular, for ordinary first derivatives
with both mixed projections nonzero, the necessary total effective rank
is at most thirteen, improving the preceding bound fourteen. This does
not change the exponent 9/4 or the separate global first-rank frontier.

## 1. The maximal first spaces have no remaining graph choice

Use the canonical quotient decomposition E_B/G=D_B plus M_B, with
dimensions twelve and four, and its C counterpart. The adopted both-mixed
classification says that rank-one mixed partners have coordinates

    v=(v0,v1,v2,v3),   u=J(v)=(v0,-v2,-v1,v3),
    v0*v3=v1*v2.

The pure-boundary annihilator of either partner has dimension six. For
effective dimensions seven and seven, both pure-boundary parts are these
entire annihilators.

On the chart v3 nonzero, normalize

    v=(a*b,b,a,1),       u=(a*b,-a,-b,1).                (1)

In the maintained boundary quotient bases d0,...,d11 on each side, the
six annihilator vectors and the mixed seventh vector are

    B: d_(2j+1)-b*d_(2j), j=0,...,5;   m_B(u),
    C: d_(2j+1)+a*d_(2j), j=0,...,5;   m_C(v).          (2)

Every coefficient of H on this pair is zero as a polynomial in a,b.
The displayed coordinate matrices have a fixed identity seven-by-seven
minor, so their ranks are seven for every complex a,b. The mixed-boundary
block formula identifies the first six vectors with the complete
six-dimensional annihilators, including a=0 or b=0.

The pure mixed product H(m_B(u),m_C(v)) is already zero. If two arbitrary
graph lifts add boundary terms beta and gamma, their compatibility becomes

    H(beta,m_C(v))+H(m_B(u),gamma)=0.

The two summands have disjoint source supports L and M, from the preceding
classification. Each therefore vanishes, putting beta and gamma in the
respective six-dimensional annihilators. They do not change the full
seven-dimensional spaces (2). This proves uniqueness of the maximal
spaces for each pair of projective mixed lines; no graph lift is omitted.

Source reversal (i,j,z)->(3-i,3-j,6-z) reverses the four mixed coordinates,
preserves the leading flag, and commutes with J. It carries the chart v0
nonzero to (1). When v0=v3=0, the rank-one equation leaves just the two
projective points e1 and e2. They are exchanged by the same reversal.
The verifier constructs and checks the endpoint v=e1 separately.

## 2. A constant nonzero normal minor over the whole chart

Adopt the 448 leading-row normal coordinates and the canonical first
equations of rank 220. Their solution space has dimension 228. For a
first row b, the off-diagonal correction equation on K_inf is

    T(x,b',G)+T(x,b,D_C)-T(y_x,b,G)=0,                  (3)

with the symmetric equation for c. The rank-56 correction map is eliminated
by its full 200-dimensional cokernel. Imposing (3) for all fourteen rows
in (2) gives a polynomial matrix

    M(a,b), of shape 2800 by 228.                      (4)

The coefficient construction uses all 4096 source terms through the
canonical normal and correction maps. There is no sampled-rank inference.

At a=b=0, an exact rank certificate selects 224 rows and columns. Let
F(a,b) be that fixed square submatrix and F0=F(0,0). Its rational inverse
exists. The verifier computes the complete polynomial matrix

    N(a,b)=F0^(-1) F(a,b)-I.

It has 332 nonzero polynomial entries. The directed graph with an edge
i to j for every nonzero N_ij is acyclic; the saved permutation places
every such entry strictly above the diagonal. Hence, identically,

    det F(a,b)=det F0 != 0.                            (5)

This proves rank at least 224 at every complex point of the chart,
including all exceptional values of a,b. Four constant parameter vectors,
the common polynomial-plane motions, lie in the kernel of M(a,b)
identically. They are independent, so rank is exactly 224 and they are
the entire kernel.

The endpoint v=e1 has another exact rank-224 certificate and the same
four-dimensional plane kernel. Source reversal then covers every nonzero
rank-one v. Thus the normal conclusion is uniform over all maximal
rank-one mixed first pairs and all their boundary graphs.

## 3. Delayed orders and the formal induction

For ordinary first derivatives, H_actual=0 and the first-space
classification are adopted from the no-second-growth theorem. The same
compatibility conclusion applies when the first new rows begin at orders
s_B,s_C. Before order s_B+s_C, every corrected first-kernel residue is in
the old four-row/four-column cross, of maximum matrix rank eight, and
therefore belongs to W0. At order s_B+s_C its double projection is exactly
H_actual; earlier source corrections have zero double projection at this
order. The adopted 26 rank-two spanning slices of canonical H apply
unchanged: adding the old cross gives rank at most ten, below the target's
minimum eleven. The target component vanishes on those spanning preimages
and on ker H, and then on all of K. Consequently H_actual=0 also for
these delayed unequal first orders. This justifies using Section 1 there.

Now follow the moving-boundary induction of the preceding normal and
third-boundary packages. Let U(t) be a formal plane of cubic forms reducing
to span(e0,e3), and write

    F_B(t)=U(t) tensor C^4 tensor C^7,
    F_C(t)=C^4 tensor U(t) tensor C^7.

The long annihilator of the three products of a basis of U(t) gives a
regular rank-64 first module K_inf(t), with

    T(K_inf(t),F_B(t),F_C(t))=0                        (6)

identically. This is a polynomial-product statement; arbitrary changes
of a short-coordinate basis are not assumed to be source automorphisms.

Suppose all rows belong to these moving boundaries modulo t^N. Project
onto the boundaries and take the first normal errors t^N D. At order N,
the leading-output cross and the rank-56 annihilator identities force
every new-row normal error to vanish; only the four leading rows on
each side can depart. The canonical first equations put D in the
228-dimensional normal space.

The earlier moving-boundary order argument supplies the off-diagonal
equations (3) at N+s_B and N+s_C. The reason is that new B errors before
N+s_B, and new C errors before N+s_C, are forced into their boundaries.
A double-new-output error cannot occur before N+s_B+s_C. All intermediate
residues are therefore in the old rank-eight cross and can be cancelled
in W0. Only the leading source correction y_x enters (3); higher ones
occur later. The full first frames in (2), including the mixed rows,
are in F_B(0),F_C(0), so this argument applies to them without modification.

Section 2 now makes D a common-plane motion. Absorb it into U(t) at order
N. Because new rows have zero constant coefficient, this preserves their
boundary membership at that order and their first nonzero frames. Every
row belongs to the new boundary modulo t^(N+1). Iterate formally.

Both output maps have rank at most 56 over C((t)), since they remain in
these rank-56 moving boundaries. Neither a Laurent first map nor a regular
limit can raise those output flattening ranks to 110. This proves the
claimed exclusion at every order. No terminal third-block estimate is
needed: the off-diagonal normal equations already give the plane kernel.

## 4. Consequence and remaining scope

If both ordinary first mixed projections are nonzero, the earlier
classification gives either invertible lines of effective dimensions 1,1
or rank-one lines of dimensions at most 7,7. The latter cannot attain
7,7 by this proof. Thus their total effective rank is at most thirteen.
The separate five-frame proof also excludes the invertible-line stratum.

Smaller rank-one first spaces, mixed projections on only one side, smaller
pure-boundary spaces, and different leading flags remain open. In
particular the present statement does not exclude every 7-by-6 pair.

The source, correction maps, partner classification, low-rank spanning
lemma and moving-plane induction retain their earlier source credits.
The new contribution is the uniform maximal-frame description and
constant-minor certificate, with the resulting local exclusion. Finite
checks and this generating session's written argument are not independent
review, formalization, or a matrix-multiplication exponent improvement.
