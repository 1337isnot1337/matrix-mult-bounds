# Cyclic finite-state slices have a divisibility obstruction

October21,2026. Written proof, unreviewed. Restricted slice ansatz only.

Let a source slice admit a finite-state representation of dimension n,

    F_(i,k,s) = U_i A^k V_s,   0<=k<a+b-1,

where A is an n-by-n complex matrix, U_i are rows and V_s are columns.
Assume n<=b, the minimal polynomial of A has degree n, and the family
(U_i,A) is observable. Here observable means that stacking all U_i A^q,
0<=q<n, gives column rank n. Then

    rank(M_F) is divisible by b.                     (1)

The distinct finite atom ansatz is a special case. This extension also
allows repeated eigenvalues when each eigenvalue has exactly one Jordan
block. It does not cover general noncyclic state matrices or representations
requiring support at infinity.

## Proof

Use the original source indices and factor through (h,j,r) as in the
distinct-atom note, now setting

    P[(j,p,L),(h,j',r)] = [j=j'] (A^p V_(L-r))_h,
    Q[(h,j,r),(H,q,r')] = [r=r'] (U_(H-j) A^q)_h.

Then P Q equals M_F coefficient by coefficient. P is b identical diagonal
blocks, so its rank is divisible by b. We prove Q has full row rank.

Set u(x)=sum_i U_i x^i. A cyclic matrix has one Jordan block for each
eigenvalue. A covector is observable for A precisely when it is nonzero
on the eigenvector of every block: the successive powers then detect all
vectors of each Jordan chain, and different eigenvalues separate by
polynomial projectors. Collective observability of the U_i therefore
makes u(x) nonzero on every such eigenvector over C(x). Consequently

    u(x), u(x)A, ..., u(x)A^(n-1)

are independent rows over C(x).

A row relation in Q, for fixed r, is represented by a vector z(x) of n
polynomials of degree<b. It gives u(x)A^q z(x)=0 for all0<=q<b.
Since b>=n, the preceding invertible observability matrix forces z(x)=0.
Thus Q has full row rank. Multiplication by Q preserves the rank of P,
proving (1).

## Applying the crossed-rank bound

Suppose additionally the crossed coefficient flattening has rank n and
the scalar symbol has rank r. The maintained quantitative inequality gives

    rank(M_F) >= (ab-1)*r+n.

Combining it with (1) gives the stronger necessary bound

    rank(M_F) >= b*ceil(((ab-1)*r+n)/b).              (2)

For a=8,b=10,n=9,r=8 this is650, exceeding the remaining ordinary
candidate's rank-two slice ceiling641. Thus a crossed-rank9 slice with
full scalar rank8 at that ceiling cannot have a cyclic finite-state
realization of dimension9. This conclusion assumes the representation;
no theorem here asserts that every bounded-rank Hankel slice has one.
Crossed rank8, noncyclic states and boundary support remain open.

## Why cyclicity cannot be removed

The known sequence f_0=1, f_(a-1)=xz has a dimension-(a+1) realization
A=J_a direct_sum J_1, with both blocks nilpotent. In the J_a block choose
U_1=e_0^T and V_1=e_(a-1); in J_1 choose U_0=V_0=1, and set all other
entries to zero. Its state matrix is noncyclic. Its crossed rank is a+1
and its source slice rank is a^2*b+1, including641 for A(8,10).
This preserves the existing counterexample rather than rounding its rank.

An elementary cyclic sharp example instead has f_0=1 and f_a=z. Use
A=J_(a+1), U_0=e_0^T, V_0=e_0, V_1=e_a. Its crossed rank is a+1,
its scalar symbol rank is a, and its source slice rank is a^2*b+b.
Finite exact support-cover and modular-rank certificates verify these
examples. The written general argument is not independently reviewed,
formalized, or a new matrix multiplication exponent.
