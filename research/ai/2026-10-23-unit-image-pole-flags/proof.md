# Leading pole flags at the remaining regular unit images

October 23, 2026. Owner-directed Codex continuation. Written and unreviewed
over C; no independent mathematical review or exponent improvement.

## 1. Scope and result

For a>=2 use the canonical cyclic source A_a, of leg dimension N=a^2(2a-1), and
the complete Laurent identity and regular unit lift of the
[one-sided unit theorem](../2026-10-23-one-sided-unit-image/proof.md).
In particular the long column map C is regular with full rank R at zero,
u=F(x_unit) is regular, and rank(M(u(0))C(0))>=r. Set q=N-r.

Suppose F has pole order h>0, and let W=im F_-h in the original canonical
first-leg source coordinates. Then W is nonzero, F_-h(x_unit)=0, and:

1. Every nonzero f in W has source matrix rank at most 3q.
2. If a^2<=3q<a^2+a, then there is a fixed nonzero rank-one Hankel
   profile h_k and either a fixed v in C^a with
   W contained in C^a tensor h tensor v, or a fixed u in C^a with
   W contained in u tensor h tensor C^a. In particular dim W<=a.
3. If 3q<2a^2, then W is contained in Mat_a tensor h for one fixed
   rank-one Hankel profile h. In particular dim W<=a^2.

These are necessary conditions on the highest pole coefficient only.
They do not assert that lower pole coefficients use the same flag.

For A4 to M(10,10,11), image rank at least107 is already excluded.
At image rank106 every remaining degeneration in this regular-long-map,
regular-unit-lift chart must have F polar, with leading coefficient of
rank one to four in one of the two rulings in item2. Its leading map
annihilates I_10. The complete first-map principal part has rank at least
two; in particular a simple first-map pole has leading rank two to four.
At image ranks102 through105, any polar F must satisfy
the fixed-Hankel constraint in item3. None of these remaining cases is
constructed or excluded by this note.

## 2. All nonzero highest coefficients satisfy the same rank budget

Normalize B M(u) C=I_R as in the preceding proof. Choose a constant
R-by-r matrix H whose unit image has rank r. Independent regular source
frames give

    B'=[H,L],       C'H=[I_r;0],
    H X11 + L X21 = Xi(x)H+O(t),

where Xij are the (r,q)-blocks of M_t(F(x)). These frames are fixed for
every x. For f=F_-h(x) nonzero, the regularized product t^h L X21 has
constant coefficient -H X11,-h, of rank at most q. Thus X11,-h has rank
at most q. Adding q rows and q columns gives rank M_0(f)<=3q. The source
frames are invertible at zero and do not change the first-leg parameter,
so rank M(f)<=3q in the original canonical source coordinates.

This proves item1 for every vector of the linear space W, not only for
a chosen basis. Regularity of u also gives F_-h(x_unit)=0.

## 3. Use the credited source rank loci

The prior [rank-gap theorem](../2026-10-20-anisotropic-constructions/slice_rank_gap.md)
gives source rank a^2 or at least a^2+a. Its minimum-rank locus is

    f_(i,k,s)=u_i h_k v_s,       rank(h_(p+q))=1.

Thus in item2 every nonzero vector in W has this form. The prior
[full locus below twice the minimum](../2026-10-20-anisotropic-constructions/polynomial_rank_locus.md)
gives, for item3,

    f_(i,k,s)=G_(i,s) h_k,       rank(h_(p+q))=1.

These are imported written source results, with their existing attribution;
the present note does not independently reprove them. In particular the
rank-gap proof uses Grothendieck's splitting theorem for vector bundles
on P^1_C, Theorem2.1, printed page126 of the
[1957 primary article](https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG/AG-25.pdf). The
source proof applies it to the kernel subbundle of the stated surjective
polynomial multiplication map. That external dependency is retained.

## 4. The linear spaces must lie in the stated rulings

If two nonproportional decomposable tensors have a decomposable sum,
they can differ in at most one tensor factor: otherwise a flattening
along one differing factor gives two independent columns and two
independent rows and hence rank two. This also applies to the grouped
factors G and h in item3.

The rank-one Hankel profiles are the degree-(2a-2) rational normal curve
with coordinates alpha^(2a-2-k) beta^k. Two distinct projective points
cannot have their entire pencil in that curve. Their Hankel matrices
are independent rank-one symmetric matrices with independent column
vectors (since a>=2); a sum with both coefficients nonzero has rank two.
Consequently a linear family of decomposable source tensors has fixed h.

For item2 fix a nonzero u0 tensor h tensor v0 in W. Every other vector
differs in at most one short factor. If some vector varies u, no vector
can vary v: their sum would differ in both factors and have flattening
rank two. Therefore the whole W lies in one ruling. Its dimension is
at most a. In item3 fixing h alone gives the bound a^2. This proves the
claims including one-dimensional W.

## 5. Why rank106 also requires a genuine first-map pole

At a=4, R=110, r=106, take e=4, q=6 and k=2. If F were regular, the
one-sided equation above would already make F_0 injective: for nonzero x
with F_0(x)=0 its regularized correction would give

    rank(Xi(x)H)<=6,       rank(Xi(x)H)>=11-4=7.

The original full-column kernel count then forces B regular, because
100>112-16+2=98. The resulting ordinary restriction contradicts12>11.
Thus F must have a pole. Its leading image satisfies16<=3q=18<20,
so item2 applies. Moreover B must be polar: otherwise its regular unit
equation at zero would force the unit image to have full rank110.

Let E_reg be the linear subspace of constant target parameters x for
which F(x) is regular. The same argument gives injectivity of F_0 on
E_reg, even though F is polar on other parameters: if F_0(x)=0 then
rank(Xi(x)H)<=6 contradicts the target lower bound7. A nonzero leading
row of B' kills M_0(F_0(x))C'_0 for every x in E_reg. Its source kernel
has dimension at most112-16+2=98. Hence dim E_reg<=98.

The complete principal-part map

    x |-> (F_-h(x),...,F_-1(x))

has kernel E_reg and therefore rank at least100-98=2. This is not a
lower bound of two for the highest coefficient alone when h>1. If h=1,
however, it gives rank F_-1>=2; together with item2 its rank is two to
four. A higher-order pole may have a rank-one highest coefficient and
additional independent polar parameters at lower orders.

For r=102,...,105 one has q=10,...,7 and3q<32;
item3 applies whenever F has a pole. No regularity assertion for F at
those four smaller image ranks is made.

## 6. Sharpness of the remaining block budget and evidence limits

A canonical minimum-rank source slice has16 entries in distinct rows
and columns. Put six of those rows and a disjoint six of those columns
in the deleted blocks of independent source frames. The retained
106-by106 block has rank4 and the full slice still has rank16. It
therefore passes the rank106 first-pole budget. This is a block-matrix
control only; the chosen frames are not asserted to arise from a source
unit trajectory or solve the full tensor equations.

The finite controls reconstruct literal source coefficients, check two
four-dimensional rulings, exhibit ranks20 and32 outside them, and check
this block-budget survivor. They do not prove all formal identities,
classify lower poles, or construct a target. The remaining chart and
the exponent improvement remain open.
