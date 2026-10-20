# A finite convolution-profile target for an exponent improvement

October 20, 2026. AI-derived conditional argument, unreviewed. **The new
profile lower bound stated below is unproved. No exponent below 9/4 has
been established.** This is an alternative research target to constructing
an unbounded family of fat-point degenerations.

## 1. A finite upper bound already available

Use the symmetrized character profile P and t from the preceding notes.
OpenAI's shifted tripling construction gives

    P(a,4a-1) >= 3 P(a,a).

The concurrent two-sector construction at `f6f307c`, preserved in
[`two_sector_bound.md`](../2026-10-20-truncated-algebras/two_sector_bound.md),
gives 2P(u,v)<=(u+2v-1)^(1/t). Apply it to (u,v)=(4a-1,a), and use
symmetry. These two existing constructions imply the finite inequality

    6 P(a,a) <= (6a-2)^(1/t).                         (1)

No scaling limit, interchange of limits, or new degeneration is used in
(1). At a hypothetical endpoint character t=3/4 it reads

    P(a,a) <= U_a := (6a-2)^(4/3)/6.                 (2)

The matching lower profile is D_a=P_*(a,a)=(3a-1)h_a/2, where
h_1=1 and h_(a+1)=(1+1/(3a))h_a. Its exact finite ceiling ratio satisfies

    (U_a/D_a)^3 = (6a-2)^4/(6 D_a)^3.               (3)

For a=4, D_4=770/81, and U_4/D_4 is approximately 1.080786599.
These are descriptive decimals; (3) is rational. The ratios approach
Gamma(4/3)*(16/9)^(1/3), approximately 1.081767640, consistently with the
previous amplitude interval. The finite inequality is slightly stronger
than that limiting ceiling at small a.

## 2. An exactly checkable conditional 2.249 criterion

Here is a sufficient finite premise:

> For every actual tensor character with t>=749/1000,
> P(4,4)>= (13/12) P_*(4,4) = 5005/486.             (H4)

**(H4) is not proved.** It is a universal character inequality to seek,
not a value inferred from a finite sample or from numerical fitting.

If it held, (1) would give, for each character in that range,

    (5005/81)^t <= 22,
    3t <= 3 log(22)/log(5005/81) < 2249/1000.        (4)

The final strict comparison has the exact integer certificate

    5005^2249 > 22^3000 * 81^2249.                   (5)

Characters with t<749/1000 already have 3t<2247/1000. Thus every character
would have 3t<2249/1000, with the common explicit bound in (4) and the
low-t bound. OpenAI's detecting-character argument would then imply

    omega <= 2249/1000 = 2.249.

The real bound in (4) is about 2.248715827. The rational number 2.249 is
chosen because (5) is a short exact certificate. Neither is an achieved
exponent bound: the finite universal premise (H4) is the missing step.

A strict finite inequality above U_a at every endpoint character would
also exclude the endpoint, using the compactness argument already recorded
in `homogeneous_rigidity.md`. The near-endpoint premise (H4) instead gives
the explicit bound without requiring that compactness argument.

## 3. A dimension screen for one way to seek such a lower bound

A natural attempt is to extract independent matrix products from powers of
the fully symmetrized tensor

    S_a = tensor_product_(pi in S3) C(a,a)^pi.

Let V_a=a^2*(2a-1). Every leg of S_a has dimension V_a^2, and
lambda(S_a)=P(a,a)^(6t). At an endpoint character all three dot-product
parameters equal 3/4. This follows from Uznański v2, Proposition 5.2:
put theta_i=arccos(sqrt(p_i)). Their sum is at least pi/2. Decreasing
angles to sum pi/2 can only increase sum p_i; on that boundary,

    sum cos(theta_i)^2 = 2+2 product sin(theta_i) <= 9/4.

The last step follows from strict concavity of log(sin(theta)) and has
equality only when all theta_i=pi/6. Zero-angle boundary cases give at most
two. Therefore sum p_i=9/4 forces p_i=3/4 for every i.

Suppose S_a^n degenerates to a direct sum of matrix products with shapes
(l_j,m_j,r_j), with no extra source tensor. Write
A_j=l_j*m_j, B_j=m_j*r_j, C_j=r_j*l_j for their leg dimensions. Conciseness
and flattening rank give sum A_j,sum B_j,sum C_j <= V_a^(2n). At the
endpoint, the character of the target is

    sum_j (A_j B_j C_j)^(3/8) <= V_a^(9n/4).         (6)

For the inequality, apply Holder with three exponents equal to three,
then use sum x_j^(9/8)<=(sum x_j)^(9/8) on each leg. Since the source
character is P(a,a)^(9n/2), the numerical lower bound for P(a,a) obtained
from any such extraction is at most

    sqrt(V_a),                                      (7)

independently of the tensor-power exponent n. This is a limitation on this
specific lower-bound method, not an upper bound on the actual P(a,a).

For a=1,2,3, exact integer comparisons give

    V_a^3 <= (6a-2)^8/6^6,

so (7) cannot exceed the finite endpoint ceiling (2). In particular,
increasing the power of the a=2 or a=3 symmetrized convolution and looking
only for direct sums of matrix products cannot supply the needed strict
inequality. At a=3 the failure is close: sqrt(45) is about 6.7082 and
U_3 is about 6.7196.

The first diagonal not excluded by this dimension screen is a=4:
sqrt(112) is about 10.5830, greater than the proposed 5005/486, about
10.2984. This does not construct a matrix-product extraction. General
non-matrix targets, different auxiliary tensors, and other spectral
inequalities are outside the screen.

## 4. A concrete finite tensor target

The dimension screen suggests the following single finite construction:

> S_4 = tensor_product_(pi in S3) C(4,4)^pi
> degenerates to the 106-by-106 matrix multiplication tensor.       (H106)

**No such degeneration is known here.** This is a selected research target,
not a consequence of dimension counting. The source has dimension 12544 in
each leg and border rank at most 7^6=117649. The target has dimension 106^2=11236 in
each leg, so this basic dimension test passes. Higher tensor obstructions
and an actual construction remain to be investigated.

If (H106) held, every character would satisfy

    P(4,4)^(6t) = lambda(S_4)
                >= lambda(M_106) = 106^(3t),

and hence P(4,4)>=sqrt(106). Combining this with (1) gives

    3t <= 3 log(22)/log(6 sqrt(106)) < 2249/1000.

The exact strict certificate is

    3816^2249 > 22^6000,    where 3816=36*106.        (8)

This implication uses all characters directly; it does not require the
near-endpoint premise (H4). The two sufficient premises are distinct:
sqrt(106) is slightly smaller than 5005/486, but still gives the rational
bound 2.249. Its descriptive real bound is about 2.248860082.

Among square targets from 105 through 112, 106 is the first that makes this
comparison strictly beat 9/4: the exact endpoint test is

    (36*n)^3 > 22^8.

It fails for n=105 and passes for n=106. Targets above 112 fail the source
leg-dimension test. This finite target does not require a separate all-size
family once its actual degeneration is supplied; tensor-character detection
and the existing convolution inequalities provide that implication.

## 5. Coordinate maps with diagonal weights cannot supply this target

There is a stronger obstruction for a specific class. Embed C(a,a) as a
coordinate restriction of the group tensor of Z/(2a-1): label its inputs
by i,j and its output by -k. Since 0<=i+j<=2a-2, the group condition
i+j-k=0 is exactly the original convolution condition. Consequently S_a^q
is a coordinate restriction of the tensor of the abelian group

    G=(Z/(2a-1))^(6q), with |G|=(2a-1)^(6q).         (9)

Suppose coordinate injections, arbitrary nonzero scalar coefficients, and
diagonal weights extract a matrix product of shape (l,m,r). The intended
group labels satisfy alpha_(i,j)+beta_(j,k)+gamma_(k,i)=0. Subtracting
intended equations at fixed reference vertices shows

    alpha_(i,j)=u_i+v_j,
    beta_(j,k)=-v_j+w_k,
    gamma_(k,i)=-w_k-u_i.

The same factorization holds for the real or integer weights, since every
intended term has weight zero. Any collision
u_i+v_j+w_k=u_i'+v_j'+w_k' with unequal triples creates two unintended
source terms, one with each sign of the corresponding potential difference.
Both coefficients are nonzero, so both would need strictly positive weight,
which is impossible. Thus the map from the l*m*r triples into G is injective:

    l*m*r <= |G|.                                    (10)

This is the concurrent group worker's abelian opposite-relation argument,
Section 4.1 of `2026-10-20-group-potentials/research_note.md`, introduced at
`dcfc1ef1f80558c8e7b6c3f8c1f02e4dced94226`. The label factorization above
makes its applicability to arbitrary coordinate injections explicit. The
argument is adopted with attribution, not counted as a new group theorem.

For S_4 itself, (10) bounds every square matrix target by n<=49, because
49^3=7^6. Hence it excludes (H106) in this coordinate-and-weight class.
General constant linear combinations can cancel extra terms and are not
covered by this proof.

More strongly, even independent sums of differently shaped matrix products
from arbitrary powers cannot force a profile value above the finite ceiling
at a=4 by this method. At an endpoint character, each summand has value

    (l*m*r)^(3/4)
    <= |G|^(1/12) * (A B C)^(1/3),

where A=l*m, B=m*r, C=r*l. Sum over blocks and use Holder together with the
source leg dimension V_a^(2q). This gives

    lambda(target) <= (V_a^2 * sqrt(2a-1))^q.

Therefore the largest profile lower bound obtainable from such an extraction
is at most

    B_a := (a^8*(2a-1)^5)^(1/9).                     (11)

At a=4 this is about 10.107956, less than U_4, about 10.274144. The exact
comparison is

    6^9 * 4^8 * 7^5 < 22^12.                         (12)

This closes the entire coordinate-injection and diagonal-weight
matrix-extraction route at a=4, not merely one finite search or one tensor
power. It does not bound P(4,4) itself and does not exclude arbitrary
linear or Laurent maps. At a=5 the bound (11) is slightly above the ceiling,
so this same calculation does not close every larger diagonal.

## 6. Validation and next task

`finite_amplitude.py` records the exact rational ceilings, the integer
certificate (5), and the small dimension comparisons. No gamma or floating
logarithm is used to accept a bound. The all-character premise remains
unproved, and the written implications have no independent review.

The next question is whether (H106) can be constructed with non-coordinate
maps, or a stronger tensor obstruction excludes it; (H4) remains a more
general finite spectral target. Section 5 means an unchanged coordinate
or vertex-potential search at a=4 cannot answer that question positively.
The previous full determinant-filtration entropy score already
passes the matching profile with a gap; repeating that score is not a way
to establish (H4). Any proposed extraction must retain its actual tensor
identity and orientation costs.

External inputs are OpenAI's October 2 proof at revision
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` (tripling and detection), and
Uznański, arXiv:2610.10494v2, Proposition 5.2 (the angular constraint).
The two-sector source construction and the existing scalar profile are
credited above. No priority claim is made for combining their inequalities.
