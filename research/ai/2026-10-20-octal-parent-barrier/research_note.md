# Orbit-hole obstruction for the fixed cubic F8 parent

Date: October 20, 2026. Claim: AI-GROUP-PARENT-ORBIT-007.
Status: written proof, unreviewed; exact finite checks. No exponent improvement.

## Statement and scope

Let F be F8 with polynomial t^3+t+1, using binary integer labels 0,...,7.
In G = F^3 semidirect F*, with multiplication
(a,v)(b,w) = (ab,v+aw), consider the three 56-point sets

```
S(a,x) = (a,(x,a^2,0)),
T(a,x) = (a,(0,x,a^2)),
U(a,x) = (a,(a^2,0,x)),       a != 0, x in F.
```

Take arbitrary vertex subsets S',T',U'. Suppose their three pair maps
s^-1 t, t^-1 u, u^-1 s are used to extract one matrix multiplication tensor
by strict coordinate potentials. Then

```
|S'| |T'| |U'| <= 92,928.
```

Consequently, this construction cannot pass the usual source degree-sum
gate at any positive exponent at most 9/4. This includes unequal subset
sizes and the previously searched shape (48,48,48).

This statement concerns vertex deletion in this particular parent and the
stated potentials. General changes of basis, other parents, simultaneous
direct-sum targets, and joint extractions from tensor powers are outside its
scope. It is not a lower bound on the matrix multiplication exponent.
The volume bound is a necessary-condition bound; its attainment is not proved.

## 1. A four-row strict-inequality circuit

Use the following eight parent vertices, with (a,x) denoting the scalar and
free coordinate in the relevant family:

```
s0=(1,1), s1=(3,3);
t0=(3,6), t1=(5,7);
u0=(3,0), u1=(3,3), u2=(5,0), u3=(5,1).
```

The four six-tuples (s,t,tt,u,uu,ss) are

```
(0,0,1,1,0,1), (0,0,1,0,1,1),
(1,1,0,2,3,0), (1,1,0,3,2,0).
```

For each tuple the group identity

```
(s^-1 t)(tt^-1 u)(uu^-1 ss) = 1
```

holds, and the term is unintended: (s,t,u) differs from (ss,tt,uu).
Write p,q,r for the three vertex potentials. Each such term requires

```
p(s)-p(ss) + q(tt)-q(t) + r(uu)-r(u) > 0.
```

The first two rows sum to 2[p(s0)-p(s1)+q(t1)-q(t0)]; the last two sum
to its negative. Thus the four required positive quantities sum to zero.
Any vertex subset containing these eight vertices is impossible.

These rows were extracted from the earlier exact sparse-circuit experiment
in [the F8 source campaign](../2026-10-20-group-potentials/octal_research.md).
The present checker rebuilds them explicitly rather than trusting that report.

## 2. An orbit of certified forbidden sets

For lambda in F*, independent shifts c_S,c_T,c_U in F, and a cyclic
permutation of the families, transform a parent position by

```
(a,x) in family f -> (lambda*a, lambda^2*(x+a*c_f)) in the permuted family.
```

For the stated seed, every transformed four-row circuit is valid. This is a
finite assertion: `parent_barrier.py` independently checks all
7*8^3*3 = 10,752 choices, all 43,008 group identities, and every positive
zero dependence using exact arithmetic. Cyclic permutation rotates each
six-tuple by two positions per family step. No assertion about an arbitrary
parent or arbitrary circuit is needed.

Fix lambda and the family permutation. In each family, vary its own shift
over all eight values. If no family hits every translate of its own seed
piece with a deleted vertex, choose one unhit shift independently in each
family. The resulting whole forbidden circuit survives, a contradiction.
Therefore at least one family must hit all eight translates of its piece.

A hole in a scalar fiber of a two-point piece hits exactly one shift: its
two points have different nonzero scalars and each affine shift map is a
bijection. Hence that piece needs at least eight holes in its two scalar
fibers to hit all shifts. The four-point U piece has two different points
in each of two scalar fibers; each hole hits exactly two shifts. It needs
at least four holes in those fibers. These are necessary conditions only.
Multiplication by lambda^2 preserves these incidence counts.

## 3. A seven-cycle hole inequality

The scalar g=3 has order seven, and g^2=5. Index the scalar fibers by g^i,
with i in Z/7. For family F let h_F(i) be its deleted-vertex count in that
fiber; 0 <= h_F(i) <= 8. Its total number of holes is H_F.
Define

```
P_F(i) = 1[h_F(i)+h_F(i+1) >= 8],
Q_F(i) = 1[h_F(i)+h_F(i+1) >= 4].
```

The seed S piece uses scalars {1,g}; the T and U pieces use {g,g^2}.
For lambda=g^i and the three cyclic family placements, Section 2 gives

```
P_S(i)   or P_T(i+1) or Q_U(i+1),
P_T(i)   or P_U(i+1) or Q_S(i+1),
P_U(i)   or P_S(i+1) or Q_T(i+1).
```

Summing their 21 necessary inequalities gives

```
21 <= sum_F [2 sum_i P_F(i) + sum_i Q_F(i)].                 (1)
```

There is already a short exclusion of every shape whose three sizes are
at least 45. If H<=11, at most two cycle edges can have mass at least 8,
since the sum of all seven edge masses is 2H<=22.

- With two such edges, they must meet; disjoint edges would require 16
  holes. Every other edge is disjoint from at least one of the two and
  has mass at most H-8<=3. Thus there are exactly two Q edges and the
  score 2 sum P + sum Q is six.
- With one P edge, every Q edge must meet it. A seven-cycle has at most
  three edges meeting a fixed edge, so the score is at most five.
- With no P edge, sum Q <= floor(2H/4)<=5.

Thus each family with at most 11 holes contributes at most six. Three such
families contradict (1), because 18<21. At least one family has size <=44.

## 4. Exact rectangular volume bound

For each H=0,...,56, let f(H) be the maximum of

```
sum_i (2*1[h_i+h_(i+1)>=8] + 1[h_i+h_(i+1)>=4])
```

over h in {0,...,8}^7 with sum h=H. Then (1) implies
f(H_S)+f(H_T)+f(H_U)>=21.

An exact max-plus dynamic program computes all 57 values. Fix the first
coordinate h0. After a prefix, store its total, last coordinate, and largest
internal-edge score. Appending b adds
2*1[last+b>=8]+1[last+b>=4]. Prefixes with equal total and last coordinate
have identical future options, so discarding every smaller score is exact.
After seven coordinates add the closing-edge score. Maximize over h0.

The resulting values for H=0,...,27 are

```
0,0,0,0,2,2,2,2,6,6,6,6,8,8,8,8,
12,12,12,12,14,14,15,15,18,18,19,19.
```

For every H>=28 the value is 21. The checker supplies a realizing cycle
for each maximum. A separate exhaustive loop over all 9^7=4,782,969
vectors, without state compression, confirms the entire table.

Finally enumerate all 57^3=185,193 hole-total triples satisfying the
necessary score condition. The largest possible volume under that
relaxation is

```
(56-8)(56-12)(56-12) = 48*44*44 = 92,928.
```

This finite maximum establishes the claimed bound; it does not construct
a target of that shape. Every maximum and comparison uses integers.

## 5. Failure of the source degree-sum gate

The [existing source certificate](../2026-10-20-group-potentials/octal_source_certificate.py)
uses seven degree-one irreducibles and 73 degree-seven irreducibles for G.
The scalar action on each nonzero additive dual vector is free; its 511
vectors give 73 orbits of size seven. Together with the seven characters
of the quotient C7 these irreducibles exhaust the dimension
7+73*7^2=3584. The imported algebraic bridge is the standard complex
representation theory of an abelian normal subgroup and Maschke's theorem,
as recorded in the source campaign. This note makes no new source-cost claim.

For target volume V<=92,928, the strict integer inequalities

```
92,928^3 = 802,490,261,962,752 < 5500^4 = 915,062,500,000,000,
76^4 = 33,362,176 < 7^9 = 40,353,607,
5500 < 7+73*76 = 5555
```

give V^(3/4) < 7+73*7^(9/4). Thus the target fails the degree-sum
criterion at 9/4. If V>7^3, each ratio d/V^(1/3), for d in {1,7}, is
less than one. Decreasing a positive exponent increases their power sum,
so failure persists at every smaller positive exponent. If V<=7^3, even
one degree-seven block is at least as expensive as V^(s/3) for every s>0.

An improved source multiplication algorithm might give a different gate.
This proof excludes only the stated degree-sum construction route.

## Reproduction

From the repository root, with Python 3.10 or later:

```sh
python research/ai/2026-10-20-octal-parent-barrier/parent_barrier.py \
  --exhaustive --output results/local/octal-parent-barrier.json
python -m unittest discover -s tests -p test_octal_parent_barrier.py -v
```

The committed report is `results/octal-parent-barrier-2026-10-20/certificate.json`.
No SAT solver, numerical optimizer, external service, or new dependency is
needed to reproduce it. Finite program checks support the stated finite
steps; the written implication and its scope remain unreviewed.
