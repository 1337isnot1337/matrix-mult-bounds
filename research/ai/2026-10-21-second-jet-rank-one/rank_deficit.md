# Effective first-jet rank sums: 24, or 20 after a mixed departure

Written proof, unreviewed. These constraints apply to arbitrary compatible
first jets at the canonical flags. They use the new identity H_actual=0
and the exact matrix blocks, rather than a finite sample of subspaces.

Pass to the effective spaces E_B/G,E_C/G, each dimension16, and write
them as boundary dimension12 plus mixed dimension4. Let W_B,W_C be the
outside-leading first-row spans in these quotients, of dimensions r_B,r_C.
A necessary condition for the matrix target is

    r_B+r_C <=24.                                      (1)

If either span has a nonzero mixed projection, the stronger condition is

    r_B+r_C <=20.                                      (2)

Both spans may contain graphs between boundary and mixed coordinates;
no direct-sum assumption on them is made.

For a fixed nonzero mixed covector v, the matrix block from the opposite
boundary factor has rank6 times rank X(v), with

    X(v)=[[v3,v1],[v2,v0]].

Its boundary kernel has dimension at most6, and is zero when rank X(v)=2.
Because H_actual vanishes, every pure-boundary vector in one W space
must lie in this kernel for every mixed projection on the other side.
No cancellation from the mixed-by-mixed block is possible for a vector
whose mixed part is zero.

If both mixed projections are nonzero, each pure-boundary intersection
has dimension at most6. Each mixed projection has dimension at most4.
Thus r_B,r_C<=10, proving (2).

Suppose only W_B has a nonzero mixed projection U_B. Then W_C is pure
boundary. If U_B contains a rank-two X(v), W_C=0 and the sum is at most16.
Otherwise X(U_B) is a linear rank-at-most-one space in Mat2. It has
dimension at most2 by the elementary common-factor argument. Hence
r_B<=12+2=14, while r_C<=6, again proving (2). The other case is symmetric.

If both mixed projections are zero, r_B,r_C<=12 directly. Together these
cases prove (1). Thus at least8 of the32 available effective directions
must be lost in the two first derivatives, or at least12 if any mixed
component occurs. These inequalities and H_actual=0 are necessary only;
none supplies a formal higher-order lift or an exponent improvement.
