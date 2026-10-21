# A central four-point matching is impossible

Status: written, unreviewed. This concerns the canonical group-coordinate
pair maps with strict integer vertex potentials, not arbitrary complex maps.

Let H be a central subgroup isomorphic to C2^2 in a finite group G, and let
pi:G->Q=G/H. Suppose vertex sets S,T,U have injective pair maps and strict
potentials producing their matrix tensor. There cannot be four distinct
q_i in Q and a,b,c in Q such that all twelve fibers

    S over q_i*a, T over q_i*b, U over q_i*c

are nonempty. No assumption that the original vertex sets are sections is
needed; select just one point in each indicated fiber.

Choose lifts alpha,beta,gamma of a,b,c and put X=alpha^-1*beta,
Y=beta^-1*gamma, Z=gamma^-1*alpha. The four selected matched first-leg
labels s_i^-1*t_i lie in XH, the second in YH and the third in ZH.
All labels in each leg are distinct by pair injectivity. Since H has four
elements, each leg uses the entire indicated coset. Moreover XYZ=1 and H
is central, so the group tensor restricted to these three cosets is, after
coordinate permutations, precisely the group tensor of H.

Restrict the target input spaces to the four units (s_i,t_i), (t_i,u_i),
(u_i,s_i). The resulting target is the diagonal tensor D4: a target term
remains exactly when its three indices are equal. The original coordinate
and potential maps restrict to a monomial degeneration from T_H to D4.
All intended coefficients are one; all extras have positive integer
parameter exponents. The same degeneration therefore exists over the
algebraic closure K of F2. This transfer would not hold for arbitrary
complex maps with unrestricted coefficients.

In K[H], write x=g-1 and y=h-1 for independent involutions. The basis
1,x,y,xy has x^2=y^2=0 and the augmentation ideal I=(x,y) has I^3=0.
In the trilinear form lambda(abc), where lambda is the identity coefficient,
every nonzero basis term has at least one input equal to1. Partition terms
according to the first such leg. This is a sum of three slices, so the
slice rank of T_H is at most3. The finite control verifies all27 cube
products in I and all64 transformed tensor coefficients.

The slice rank of D4 is4. To see the lower bound over the infinite field K,
suppose a slice decomposition used r1,r2,r3 slices on its three legs with
r1+r2+r3<4. Choose a first-leg functional annihilating the r1 slice vectors
and having at least4-r1 nonzero coordinates. Such a vector exists: the
annihilator has dimension at least4-r1 and a generic vector is nonzero on
every coordinate not identically zero there. The contracted diagonal
matrix has rank at least4-r1, whereas the remaining slices give rank at
most r2+r3, a contradiction.

Slice rank does not increase under restriction or degeneration over an
algebraically closed field. The latter follows from closedness of bounded
slice-rank loci: fix dimensions r1,r2,r3 and project the closed tensor
incidence condition from the proper product of three Grassmannians. The
finite union over slice allocations is closed. Thus T_H cannot degenerate
to D4, proving the claim.

The zero-cube slice method is external and standard; see
[Sawin2018, Lemma10](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v25i4p23/pdf/).
The maintained Heisenberg modular note also records the closed-locus and
field-transfer arguments with their credits. The central-quotient matching
application and finite controls here are local work, without independent
mathematical review or any matrix exponent improvement.

The control uses projected points0,40,49,102 in S5. Its three four-point
lifts into S5 x C2^2 have all three pair maps injective and violate none of
the existing commuting-trade conditions. Nevertheless a five-row Farkas
circuit with all weights one rejects strict potentials. This confirms that
the new cut removes a case surviving those earlier necessary tests.
