# A moving multiple-support family with full ambient linear span

October21,2026. Written proof, unreviewed. Source slices, not a target tensor.

Assume a>=3 and b>=a+1. Choose distinct finite points lambda_0,...,lambda_(a-2).
Use a double point at lambda_0 and a-2 simple points. Choose

    G_1(x,z)=xz A(z)C(x),
    G_0(x,z)=A(z)C(x)+x C(x)B(z)+z A(z)D(x),

where deg A<=b-2, deg C<=a-2, deg B<b and deg D<a. At each simple point
choose a separable biform H_h(x,z)=u_h(x)v_h(z), with deg u_h<a, deg v_h<b.
Define, for0<=k<a+b-1,

    f_k = lambda_0^k G_0 + k lambda_0^(k-1) G_1
                     + sum_(h=1)^(a-2) lambda_h^k H_h.          (1)

The derivative term is zero for k=0, including when lambda_0=0.

Every slice in this family has source rank at most a^2*b+1. When A,C and
all simple factors are nonzero, the generic source rank is exactly a^2*b+1,
scalar-symbol rank a, and crossed rank a+1. Its image closure, allowing the
points to move, has dimension

    a(a+b)-3.                                                 (2)

For A(8,10), this gives a141-dimensional family of generic rank641 slices.
Unlike the previous fixed-support family, its linear span is the full1360-
dimensional source leg. It still supplies no1056-dimensional linear target-leg
map or compatible three-leg tensor restriction.

## Exact separation of the long support

For the p window of length a, use the confluent Vandermonde columns

    (lambda_0^p), (p lambda_0^(p-1)), (lambda_h^p) for h>=1.

They are independent because the total scheme length is a. The corresponding
q window has length b>=a and also has full column rank. The identity

    (p+q)lambda^(p+q-1)
      =p lambda^(p-1)lambda^q+lambda^p q lambda^(q-1)

therefore transforms the whole block Hankel source matrix to a direct sum:

    [[R(G_0),R(G_1)],[R(G_1),0]],   R(H_1),...,R(H_(a-2)),       (3)

where R is the original biform coefficient block. The full-rank left and
right transformations preserve rank; no source coefficients are discarded.
The same separation applies to the crossed coefficient matrix and scalar
symbol, using the respective coefficient blocks.

## Rank of the double-point block

The local scalar2-by2 block has the exact factorization U(z)V(x), with

    U = [[A,zA,B],[0,0,zA]],
    V = [[C,0],[D,xC],[xC,0]].

The two primitive kernel pencils are c=e_1-z e_0 and d=e_2-x e_0, with
pairing d^T c=xz. The coefficient factors have rank3 when A C is nonzero.
The state-factor calculation from the pairing note now uses three states,
while the outer polynomial shift lengths remain a and b. Its two kernel
sizes are b(a-1) and a(b-1), and their pairing has rank(a-1)(b-1). Thus

    rank(local source block)
       =3ab-b(a-1)-a(b-1)+(a-1)(b-1)=2ab+1.

Its crossed rank is3 and scalar-symbol rank2. Each nonzero separable H_h
contributes source rank ab, crossed rank1 and scalar-symbol rank1. Equation(3)
therefore gives total ranks a^2*b+1, a+1 and a. Polynomial continuation gives
the source-rank upper bound at boundary specializations as well.

## Dimension and full span

The local pair (G_0,G_1) has dimension2(a+b)-4. This follows from the same
two-parameter truncated-unit gauge and matching differential lower bound
as the convolution family with two local states. Each simple residue has
rank-one coefficient dimension a+b-1. For fixed distinct support points,
Hermite interpolation makes the residue-to-sequence map injective. Thus
the fixed-support image dimension is

    2(a+b)-4+(a-2)(a+b-1)=a(a+b-1)-2.

On the open set with nonzero top jet and simple residues, the minimal scalar
recurrence has degree a and is recovered from the available2a moments. Its
roots and their multiplicities recover this support scheme, up to finite
permutation of the simple points. Moving the a-1 support points therefore
adds a-1 dimensions, proving(2). The stated b>=a+1 guarantees2a moments.

For linear span, specialize all residues except one simple residue to zero.
Allow its biform to be a monomial x^i z^s and its support point to vary.
Separable monomials span all ab biform coordinates; a+b-1 distinct support
values give an invertible Vandermonde in the long coordinate. Hence the
family's linear span is all ab(a+b-1) source coordinates. This uses boundary
members of the polynomial family and does not claim that its image is a
linear space.

## What remains missing

The full-span result removes the earlier622-coordinate obstruction for this
broader family. The141-dimensional image is nevertheless nonlinear. Neither
its dimension nor its span constructs the needed injective linear map from
the1056-dimensional target parameter leg. Every rank-one and rank-two target
parameter must have the appropriate source lift, and the other two target
leg maps must satisfy the complete tensor identity. None is supplied here.
The numerical Laurent searches are separate and remain uncertified.

The finite verifier checks the confluent support identity, coefficient ranks,
small complete source matrices and the full-span Vandermonde certificate.
This argument has no historical-priority or independent-review claim.

Later scoped obstruction: `multiple_support_linearity.md` shows that this
explicit distinct-support family cannot itself contain the generic rank-two
image of the required injective linear target-leg map. The construction and
full-span statement remain valid; arbitrary confluent closure strata and
other critical source components are not excluded by that proof.
