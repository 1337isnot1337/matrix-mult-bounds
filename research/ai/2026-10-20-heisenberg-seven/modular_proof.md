# A modular obstruction to coordinate Heisenberg constructions

Status: written, unreviewed application of external results. No improvement
of the matrix multiplication exponent is established.

Let H_p={(a,b,c):a,b,c in F_p}, with product
(a,b,c)(x,y,z)=(a+x,b+y,c+z+a*y), for an odd prime p. Write T_p for its
group tensor, in the cyclic form with coefficient one when xyz=1.
Its complex character degrees are p^2 copies of one and p-1 copies of p;
the maintained [source proof](../2026-10-20-heisenberg-five/source_proof.md)
derives these degrees. Thus its character-degree cost is

    C_p(tau) = p^2 + (p-1)*p^tau.

The construction class below is the maintained injective pair-map plus
strict integer potential method, applied to H_p^r for any positive integer
r. Targets may be a single rectangular matrix tensor or a finite direct sum
of rectangular matrix tensors. Arbitrary complex linear degenerations remain
outside the conclusion.

For every p in

    {3,5,7,11,13,17,19,23,29,31,37,41,43,47},

no such construction can pass the usual degree-cost comparison

    (abc)^(tau/3) > C_p(tau)^r,       2 <= tau <= 9/4.           (1)

The same exclusion holds with a finite sum of target volumes on the left.

This includes all joint powers; it does not merely classify one-copy subsets.
At p=53 the reported rational bound fails to give this obstruction. That
failure is not evidence for a construction or for optimality of the bound.

## External results and field hypotheses

The weighted augmentation filtration is Petrov's, not a new filtration:
[Petrov, arXiv:1606.03256v4](https://arxiv.org/html/1606.03256v4),
Section 7, establishes it for Heisenberg groups over their defining field.
[Sawin, EJC25(4), P4.23 (2018)](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v25i4p23/pdf/),
Lemma 10 and the filtration method culminating in Theorem 19, provide the
associated slice-rank framework for modular group algebras. We spell out
the required counting argument below to pin the constant and hypotheses.

We also use Strassen's tight-support induced-matching theorem: a tight
three-partite support with uniform marginals of size n^2 has induced
matchings of size n^(2k-o(k)) in its k-th power. A statement is
[Christandl--Vrana--Zuiddam, arXiv:1609.07476v2](https://arxiv.org/abs/1609.07476v2),
Theorem 1.1.31, together with the definition of monomial subrank.
Its use here is combinatorial: deleting coordinates of the 0/1 support
does not depend on the characteristic. The relation between induced
matchings and tensor subrank over every field is also explicit in
[Arunachalam--Vrana--Zuiddam, EJC27(3), P3.12 (2020)](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v27i3p12/pdf/),
Section 1.4.1, equation (6). That paper's Section 1.4.3, equation (11),
states the tight-support entropy theorem directly for hypergraphs, so no
transfer of a complex-coefficient identity is needed. The matrix support is tight: injective weights
on the three ordered-pair index sets are

    alpha(i,j)=A*i+B*j,
    beta(j,k)=-B*j+C*k,
    gamma(k,i)=-C*k-A*i,

where, for example, A=1, B=n, C=n^2 and indices run from zero to n-1.
Every support triple sums to zero. The uniform distribution on its n^3
triples has uniform marginals on n^2 points. Consequently the asymptotic
subrank, and hence asymptotic slice rank, of square M(n,n,n) is at least
n^2 over the algebraic closure of F_p as well as over C. This is the only
matrix slice-rank lower bound required here. It avoids assuming a
characteristic-zero invariant remains nonzero after reduction modulo p.

Slice rank does not increase under linear restriction, and its bounded
loci are Zariski closed over an algebraically closed field. For completeness,
the closed-locus assertion follows by fixing three nonnegative integers
r_1+r_2+r_3=s and projecting the incidence condition

    T in U_1 tensor B tensor C
       + A tensor U_2 tensor C + A tensor B tensor U_3

from the product of the appropriate Grassmannians. The incidence set is
closed, the Grassmannians are proper, and there are finitely many triples
(r_1,r_2,r_3). Thus a degeneration cannot increase slice rank, including
over the algebraic closure of a finite field. This agrees with the
maintained external Tao--Sawin slice-rank reference.

## Petrov's filtration and an exact upper bound

In F_p[H_p], put X=x-1, Y=y-1, Z=z-1 for x=(1,0,0), y=(0,1,0),
z=(0,0,1). The elements Z^c Y^b X^a, 0<=a,b,c<p, form a basis:
their expansion in z^k y^j x^i is a product of three invertible triangular
binomial transforms. The relations are X^p=Y^p=Z^p=0, Z central, and

    XY = YX + ZYX + Z + ZX + ZY.

Assign weights 1,1,2 to X,Y,Z. Reordering a word into the displayed
normal order never decreases weight: the five terms on the right have
weights at least two. The process terminates by reducing each X,Y
inversion (Z is central). The maximum nonzero normal-basis weight is

    D = 4(p-1).

Every word of weight greater than D is therefore zero. In the k-th tensor
power, a coefficient of the trilinear form lambda(uvw), with lambda the
identity coefficient, can be nonzero only when the three normal-basis
weights sum to at most kD. At least one of these weights is at most kD/3.
Partition the support according to one such leg, and slice at its basis
index. This bounds slice rank by three times the number N_k of k-tuples
of normal basis vectors with total weight at most kD/3.

For any fixed rational 0<t<1, put

    F_p(t) = (1+t+...+t^(p-1))^2 * (1+t^2+...+t^(2p-2)),
    B_p(t) = F_p(t) / t^(D/3),
    Q_p(t) = B_p(t)^3 = F_p(t)^3 / t^D.

Every counted tuple has t^weight >= t^(kD/3), so

    N_k <= B_p(t)^k,
    slice_rank(T_p^k) <= 3*B_p(t)^k.                         (2)

The algebra and counting remain valid after extending F_p to its algebraic
closure. The factor three disappears upon taking k-th roots.

## Why this modular bound applies, and cyclic symmetrization

A pair-map/potential certificate uses distinct group coordinates, 0/1
coordinate maps and integer powers of a parameter. All intended coefficients
are exactly one, all unintended exponents are strictly positive, and there
are no cancellation identities depending on complex coefficients. The same
certificate thus defines the same degeneration over every field. In
particular, a coordinate construction from T_p^r to M(a,b,c) over C would
also work over the algebraic closure of F_p. We do not infer this transfer
for an arbitrary degeneration defined only over C.

Let V=abc. The source tensor is cyclically symmetric even though the group
need not be commutative: xyz=1 implies yzx=1. Take the given degeneration
and its two cyclic rotations. Their tensor product gives

    T_p^(3r) degenerates to
    M(a,b,c) tensor M(b,c,a) tensor M(c,a,b) = M(V,V,V).

Taking k-th powers, applying slice-rank monotonicity and (2), and then using
the matrix asymptotic subrank lower bound gives

    V^2 <= B_p(t)^(3r) = Q_p(t)^r.                          (3)

The cyclic step is essential. Using only the smallest original leg
dimension would leave some unequal rectangles unexcluded.

For a finite direct sum S of targets M(a_i,b_i,c_i), put V_i=a_i*b_i*c_i.
Its support is also tight: choose common local weights as above with a
base larger than every dimension, and give the three legs of block i
additional offsets i*K,i*K,-2*i*K, where K separates all local ranges.
Tensor products of tight supports are tight, using a sufficiently large
integer base to concatenate their injective weights.

In S, choose block i with probability q_i and then an index triple uniformly
inside that block. The marginal entropies are H(q)+sum q_i*log(a_i*b_i),
H(q)+sum q_i*log(b_i*c_i), H(q)+sum q_i*log(c_i*a_i). The independent
product of this distribution and its two cyclic rotations on
U=S tensor rot(S) tensor rot^2(S) has, on every leg, entropy

    3*H(q) + 2*sum_i q_i*log(V_i).

Apply the combinatorial tight-support theorem and set
q_i=V_i^(2/3)/sum_j V_j^(2/3). The asymptotic subrank of U is at least
(sum_i V_i^(2/3))^3. The same three-copy source and slice-rank bound give

    sum_i V_i^(2/3) <= B_p(t)^r.                            (5)

This argument does not assume additivity of slice rank or submultiplicativity
of slice rank; neither is needed. It uses the entropy lower bound for the
specific tight target support and the explicit upper bound for source powers.

## Rational certificate for the degree gate

For each listed prime the report gives a rational t and an explicit rational
lower bound L_p <= C_p(9/4), together with the strict integer comparison

    Q_p(t)^3 < L_p^8.                                      (4)

The root floor used in L_p is checked by its two defining fourth-power
inequalities. No floating-point acceptance or optimum computation is used.
By (3) and (4),

    V^(3/4) <= Q_p(t)^(3r/8) < L_p^r <= C_p(9/4)^r,

so (1) fails at tau=9/4. It also fails for smaller tau in the stated
interval: the finite l_tau norm of the fixed positive character-degree
list decreases as tau increases. A gate passing at a smaller tau would
therefore also pass at 9/4, a contradiction.

For direct sums and 2<=tau<=9/4, set x_i=V_i^(2/3). Since tau/2>=1,

    sum_i V_i^(tau/3) = sum_i x_i^(tau/2)
                         <= (sum_i x_i)^(tau/2)
                         <= B_p(t)^(r*tau/2).

The same decreasing l_tau norm gives
C_p(tau)^(2/tau)>=C_p(9/4)^(8/9)>B_p(t), by (4).
The multi-target degree gate therefore also fails. This statement concerns
the coordinate construction and this ordinary degree-cost comparison; it
does not assert a bound against arbitrary complex maps or other analyses.

## Reproduction and scope

`modular_bound.py` reproduces all rational certificates and checks the PBW
change of basis and every right-generator product at p=3,5,7 using actual
group-algebra multiplication over F_p. The controls cover 495 basis vectors
and 1,485 generator products. They test the finite implementation; the
all-power conclusion uses the written argument and imported theorems.

The earlier two H_7 searches each ended at their 600-second limit with no
model. They are retained as bounded discovery history, not used as proof.
The preliminary characteristic-p pilot used a weaker minimum-leg comparison;
its unproved hypotheses are superseded by this note and the volume argument.
No general complex source is excluded, and no new matrix multiplication
upper bound is supplied.
