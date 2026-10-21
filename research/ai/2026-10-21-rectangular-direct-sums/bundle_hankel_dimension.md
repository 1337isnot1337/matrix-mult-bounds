# All-rank crossed-Hankel dimension bound from bundle extensions

October 21, 2026. Written proof, unreviewed. No independent verification,
historical priority, or smaller matrix-multiplication exponent is claimed.

Let F_0,...,F_(p+q-2) be p-by-q matrices, and let H=(F_(i+j)) have q block
rows and p block columns. Thus H is a pq-by-pq matrix in an ambient vector
space of dimension N=pq(p+q-1). For every nonnegative integer R, its rank-
at-most-R locus satisfies

    dim {rank H<=R} <= min(N, R(p+q)+floor((p-q)^2/4)).       (1)

Unlike the earlier elementary boundary proof, this bound covers R greater
than min(p,q). It uses the Birkhoff-Grothendieck splitting theorem as an
external input. All parameter and integer estimates needed below are supplied.

## 1. The block matrix as a connecting homomorphism

On P1 put A=O(-q)^p and B=O(p)^q. The vector space of extensions

    0 -> A -> E -> B -> 0

is Ext^1(B,A)=Mat_(p,q) tensor H^1(O(-p-q)), of dimension N.
Identify the entry of its Cech cocycle with

    sum_(k=0)^(p+q-2) F_k z^(-k-1).

Twisting the extension by O(-1), the connecting map is

    H^0(O(p-1))^q -> H^1(O(-q-1))^p.

Using domain monomials z^j for 0<=j<p and target Laurent classes z^(-i-1)
for 0<=i<q, multiplication by the displayed cocycle gives block entry F_(i+j).
Terms outside the target Laurent range are coboundaries. Thus the connecting
map is exactly H, up to harmless basis ordering.

The splitting theorem writes E=sum_j O(e_j), with n=p+q summands and
sum e_j=deg E=0. The cohomology exact sequence gives

    rank H = pq - h^0(E(-1)) = pq - s,
    s = sum_j max(e_j,0).                              (2)

Every occurring splitting type has -q<=e_j<=p. Indeed E(q) is globally
generated: in its extension both end terms are globally generated and
H^1(O)^p=0, so sections of the quotient lift. Applying the same argument
to the dual extension shows that E^*(p) is globally generated. Therefore
there are only finitely many possible splitting types.

## 2. Dimension of a fixed middle-bundle stratum

Fix E of an occurring splitting type. Parametrize exact sequences by an
injection i:A->E with locally free quotient isomorphic to B and an
identification of that quotient with B. The injections form a constructible
subset of Hom(A,E). Each nonempty framing fiber has dimension dim Aut(B)=q^2.
Since E(q) has no negative summands,

    dim Hom(A,E) = p h^0(E(q)) = p n(q+1).

Two such framed sequences define the same extension class exactly when
related by Aut(E). This action is free: an automorphism fixing A and B
differs from the identity by a map B->A, but Hom(B,A)=0. Thus every fiber
has dimension h^0(End E). The extension-class map can be written algebraically
on local choices of splittings by the Cech cocycle construction; dimension
of fibers gives the upper bound

    dim(stratum E) <= p n(q+1)+q^2-h^0(End E)
                    = N-h^1(End E).                    (3)

The last identity follows by summing the line-bundle cohomology formulas:
h^0(End E)-h^1(End E)=n^2. No unproved assertion that every splitting type
occurs, or that a degeneration stratum is transverse, is used.

## 3. An integer bound for every splitting type

Let P,Q,Z count positive, negative and zero e_j, so n=P+Q+Z.
Both the positive-degree sum and the absolute negative-degree sum are s,
and s>=max(P,Q). The line-bundle formula gives

    h^1(End E) = sum_(i,j) max(e_i-e_j-1,0).

Discard the nonnegative contributions between degrees of the same sign.
The remaining positive/negative and nonzero/zero pairs give

    h^1(End E) >= (n+Z)s-PQ-Z(P+Q)
                 = n s + Z(s-P-Q)-PQ.

With u=min(P,Q), this is at least

    n s - PQ - Z u = n s - u(n-u)
                  >= n s - floor(n^2/4).               (4)

This also holds when s=0. Combining (2)-(4), and using rank H<=R, gives

    dim(stratum E) <= N-n(pq-R)+floor(n^2/4)
                    = nR+floor((p-q)^2/4).

The finite union over splitting types and the ambient bound N prove (1).

## 4. Consequence for the source screen

For the source A(a,b), take p=b and q=a. Suppose a rectangular target-block
parameter has rank at most k and its source lift has rank at most L.
Assume the verified projection-saturation argument excludes generic symbol
rank at most a-1 on this parameter variety. Its generic symbol rank is then a.
The quantitative crossed-rank bound gives

    rank(T_F) <= R = L-(ab-1)a.

Closedness extends this bound over the whole rank-at-most-k parameter variety.
A necessary dimension condition is therefore

    k(u+v-k) <= R(a+b)+floor((a-b)^2/4),                (5)

where u-by-v is the parameter matrix format. Concision makes the lift
injective; the crossed coefficient embedding is also injective. The lower-
symbol-rank prerequisite remains mandatory, with an exact finite Hankel-space
certificate in the implementation.

For example, a full-symbol A89 lift of rank at most578 has crossed rank at
most10. Formula (1) bounds that locus by170, so it cannot contain an injective
image of a171-dimensional rank-three parameter variety. This does not round
578 down to576 or contradict the exact rank577 counterexample.

## External inputs and scope

Birkhoff-Grothendieck and the line-bundle cohomology formulas are classical
external results. One directly inspected source is MIT's September 2020
18.721 notes, Theorem8.4.1 and the cohomology formulas immediately following
it (PDF page186):
https://math.mit.edu/classes/18.721/ag-sept16-2020.pdf .
The external input is the splitting statement and cohomology formulas, not
this rank-stratum dimension conclusion. No source text or proof is copied.

The usual classification of extensions by Ext^1 and the fiber dimension
theorem are also used. The explicit Cech identification and framed-sequence
parameter count are given to expose the relevant hypotheses. This argument
concerns ordinary complex source slices. It constructs no tensor maps,
does not apply the lifting inequality to singular degenerations, and leaves
the matrix multiplication exponent unchanged.
