# Ordinary restrictions detected by low-rank slice spans

October21,2026. AI-SEMISIMPLE-LOW-SLICES-024. Written, unreviewed.
Work over C. The first argument concerns ordinary restrictions. A separate
determinant-factor argument below covers square-block border targets.
No historical priority is claimed.

Let S be the direct sum of square multiplication tensors M(d_i,d_i,d_i).
Put N=sum_i d_i^2. Suppose an ordinary linear restriction produces a
concise rectangular direct sum T=direct_sum_j M(a_j,b_j,c_j), whose first
leg has dimension M=sum_j a_j*b_j. Write k=N-M>=0. Then for every r>=0,

    sum_{i:d_i<=r} d_i*max(d_i-k,0)
       <= sum_{j:c_j<=r} a_j*b_j.                         (1)

The same inequality holds after each cyclic permutation of the target
formats, with the corresponding input dimension and codimension k.

To prove this, write the first restriction as a map from the target slice
parameter space into the source parameter space. Target conciseness makes
it injective. Its image E has codimension k in direct_sum_i Mat(d_i).
The maps on the two other tensor legs compress source slice matrices and
cannot increase their ranks.

Fix a source block i and one of its columns. Matrices supported in that
single column form a d_i-dimensional linear subspace C_ij. Every nonzero
matrix in it has matrix rank one, so its source multiplication slice has
rank d_i. The intersection E intersect C_ij has dimension at least d_i-k.
The C_ij for all columns and all blocks are in direct sum. For d_i<=r,
their intersections therefore give at least the left side of(1) independent
parameters whose individual slices have rank at most r. Their images are
independent target parameters, all in the linear span of its rank<=r locus.

In T, the slice for an a_j-by-b_j parameter X_j has matrix rank
c_j*rank(X_j); different blocks add their ranks. Every rank<=r target
parameter consequently vanishes on all blocks with c_j>r. Conversely,
rank-one matrix units span every block with c_j<=r. The linear span of the
rank<=r parameter locus has exactly the right-side dimension. This proves(1).

This proof needs no classification of matrix spaces or reflexive closures.
It applies to arbitrary ordinary linear maps, including maps that mix the
source's simple components.

## The SL(2,F8) joint target needs a singular degeneration

Take source degrees(1,7,7,7,7,8,9,9,9) and target

    2*M(8,9,9) + 2*M(9,8,9) + 2*M(9,9,8) + M7.

Each target leg has dimension499, so k=504-499=5. At r=7 the left side of(1)
is4*7*(7-5)=56. Only the M7 component contributes on the right, giving49.
Thus no ordinary complex linear restriction realizes this joint target.
This strengthens the earlier group-basis/diagonal exclusion in claim023
for ordinary maps. That claim's coordinate argument still covers the
stated singular diagonal family. The conditional2.24 implication of022
remains conditional on a genuinely singular general degeneration.

## A smaller near-full semisimple trade

The simpler proposed trade

    4*M7  ->  2*M9 + M4 + M3 + M2                         (2)

has source dimension196 and target dimension191. It passes every full-space
Koszul power and every all-rank-locus dimension budget, using the existing
exact formulas. Nevertheless(1) excludes ordinary restrictions: at r=7,
the two sides are56 and16+9+4=29. This is a strict additional ordinary
obstruction for candidates that those other necessary tests leave open.
The determinant argument below also excludes singular degenerations of(2).

If a general complex degeneration in(2) existed, it would imply
omega<=56/25=2.24, via the same credited Schonhage asymptotic sum inequality
and Bini border conversion used in claim022. For completeness, divide the
target-minus-source comparison by9^s and define

    G(s)=2+(4/9)^s+(1/3)^s+(2/9)^s-4*(7/9)^s.

The exact integer intervals at tau=56/25, scale10^10, give source upper
3126652392424 and target lower3132493487575, margin5841095151>0.
For2<=s<=9/4, G'(s)>0: log(9/7)>1/4 follows from
log(x)>2*(x-1)/(x+1) at x>1; log(9/4)<1, log3<3/2, and log(9/2)<2 follow
from log(3/2)<1/2 and log2<1. Bound(7/9)^s>(7/9)^3 and each other power
by its value at2. This gives

    G'(s) > (7/9)^3-(4/9)^2-(3/2)*(1/3)^2-2*(2/9)^2
          = 11/1458 > 0.

Together with the external omega<=9/4 theorem, G(tau)>0 contradicts the
asymptotic sum inequality if omega>=tau. Thus the missing degeneration
would imply the stated upper bound, with arbitrary fixed positive slack
in exact division-free arithmetic circuits over C. This is a conditional
implication, not a finite algorithm or an exponent improvement.

## What the ordinary argument alone says about limits

The span dimension of a low-rank locus can drop at a singular limit. For
example, the quadratic equation x*(x-t*y)=0 in a two-dimensional vector
space defines two lines spanning the whole plane for t!=0, but its reduced
zero set at t=0 is one line. Flat scheme multiplicities preserve information
that the span of reduced points discards. Likewise, independent source
slice directions may coalesce while tensors degenerate. No closedness
argument for that span construction is supplied here. It must not be used
by itself to reject border degenerations. The separate factor argument
below does establish the same inequality for square-block targets with
nonzero generic slice determinant. It does not cover the larger rectangular
packet target, whose generic slice matrices are singular.

The exact verifier records both examples and all rank budgets. A separate
rational control builds the five global linear constraints on four Mat7
blocks, computes every single-column kernel, and checks56 independent
rank-seven slices. This illustrates the elementary proof without assuming
a map to either excluded target.

## A closed determinant-factor obstruction for square targets

AI-SEMISIMPLE-DETERMINANT-026. Written, unreviewed. Suppose the target is a
direct sum of square tensors M(b_j,b_j,b_j), of leg dimension
M=sum_j b_j^2. Set k=N-M. In this case(1) is necessary even for a general
complex border degeneration. The proof uses determinant factors rather
than closedness of spans of reduced rank loci.

First consider the symbolic source slice matrix. After fixed row and
column permutations it is the block diagonal matrix consisting, for each
i, of d_i identical copies of the generic d_i-by-d_i matrix X_i.
Every M-by-M minor is divisible by

    P(X)=product_i det(X_i)^max(d_i-k,0).                  (3)

Indeed a nonzero minor of a block diagonal matrix selects equally many
rows and columns from each copy. Removing k rows and k columns can affect
at most k copies of any given X_i; at least d_i-k full copies remain.
Their determinants give the stated powers. Zero minors satisfy(3) as well.
This is a direct determinantal-divisor calculation, not an inference from
the dimension of a reduced variety.

For any linear maps on all three tensor legs, the Cauchy--Binet expansion
therefore gives the polynomial identity

    det(T_epsilon(z))
       = product_i P_i,epsilon(z)^max(d_i-k,0) * R_epsilon(z),

where P_i,epsilon is homogeneous of degree d_i, obtained by substituting
the first input map into det(X_i). If the left side is nonzero, all factors
with positive exponent are nonzero. Its degree is M.

Now let these mapped tensors tend to the square-block target. Its slice
determinant is the nonzero polynomial

    Q(z)=product_j det(Z_j)^b_j.                          (4)

Consequently the mapped determinant is nonzero generically. Normalize each
nonzero homogeneous factor projectively. The multiplication morphism from
the product of the relevant projective spaces of forms is proper: those
spaces are projective, and polynomial multiplication never gives zero in
the integral polynomial ring. Its image is closed. Thus the factorization
persists at Q, with nonzero limiting factors P_i of degree d_i and the
same exponents max(d_i-k,0). This also follows by taking convergent
subsequences of the normalized complex coefficient vectors.

Each determinant det(Z_j) is an irreducible homogeneous polynomial of
degree b_j, in the disjoint target block variables. Unique factorization
implies that P_i can involve only target determinant factors whose degrees
are at most d_i. All P_i with d_i<=r must therefore fit inside the factors
of(4) having b_j<=r. Comparing total degrees gives exactly(1), now for
border degenerations of square-block targets.

In particular4*M7 cannot border-degenerate to2*M9+M4+M3+M2: at r=7 the
required factor degree is56, whereas the available degree in determinants
of degree at most seven is29. This closes the smaller numerical candidate
despite its passing all Koszul and rank-locus dimension tests. Its2.24 gate
remains a valid conditional calculation with a premise now proved false.

This does not prove an exponent lower bound. The test concerns one fixed
finite source and target; enlarging the source, taking powers, changing
the target or using rectangular direct sums can evade it. The original
499-dimensional rectangular packet target has generic slice rank481, so
its full slice determinant vanishes and the nonzero-target step above is
unavailable. Only the ordinary span exclusion is established for it here.
