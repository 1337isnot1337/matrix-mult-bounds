# A four-point obstruction in the elementary abelian group of order 81

Status: written, unreviewed proof. The integer certificate is
`ternary_fourier.py`. This is an exclusion for a construction class, not an
improved matrix multiplication exponent. No historical novelty is claimed.

There do not exist sets A,B,C of size four in H = F3^4 such that the map
(a,b,c) -> a+b+c is injective.

First, every four-point set has affine span of dimension two or three. If A
spans a plane V after translation, A-A=V: for each nonzero h in V, a set
avoiding differences h and -h has at most one point on each of the three
parallel h-lines, and hence size at most three. An injective triple-sum map
would then force B x C -> H/V, (b,c) -> b+c+V to be injective. Indeed any
collision of distinct pairs has difference in A-A and extends to a collision
of triple sums. This is impossible because 16>9. The same argument applies
to each of the three sets. All three therefore have affine span dimension
three.

Every such four-set is affinely equivalent to {0,e1,e2,e3}. Write A-hat(chi)
for its unnormalized Fourier sum. Over the 80 nontrivial characters, the
squared magnitudes |A-hat(chi)|^2 have this distribution:

| Squared magnitude | Multiplicity |
| --- | --- |
| 1 | 36 |
| 4 | 18 |
| 7 | 24 |
| 16 | 2 |

The same distribution holds for B and C; the placement of its values among
characters may differ. The table follows directly by counting the three
coordinates of a dual vector. If their counts, including the exponent zero
from the point 0, are n0,n1,n2, the squared magnitude is
n0^2+n1^2+n2^2-n0*n1-n0*n2-n1*n2. The certificate enumerates all 81 dual
vectors, omits the trivial one, and checks the table with integers.

For x,y,z in {1,4,7,16}, expansion around 1 gives

    xyz >= 1+(x-1)+(y-1)+(z-1)
           +9*(1[x>1]+1[y>1]+1[z>1]-1).

When at most one value exceeds 1, the last term is nonpositive or zero.
When exactly two exceed 1 their product of excesses is at least nine.
When three do, the three pairwise products alone are at least 27>=18.
Thus the inequality holds in every case. Each spectrum has sum 308, and
44 of its values exceed 1. Summing the inequality over nontrivial characters
therefore gives

    sum_(chi != 1) |A-hat|^2 |B-hat|^2 |C-hat|^2
       >= 80 + 3*(308-80) + 9*(3*44-80) = 1232.

On the other hand, injectivity means that the convolution 1_A*1_B*1_C is
zero or one at every group element, with 64 ones. Parseval in the order-81
group would require the full Fourier sum to be 81*64. The trivial character
contributes 4^6, leaving only 81*64-4^6=1088 for the nontrivial sum. The
inequality 1232>1088 is a contradiction.

An independent stronger finite inequality is also saved: assign weights
w(1)=-26, w(4)=37, w(7)=73, w(16)=100. Every one of the 64 triples satisfies
3xyz >= w(x)+w(y)+w(z). Summing yields the stronger lower bound
36*(-26)+18*37+24*73+2*100=1682. These 64 integer inequalities are checked
individually; the simpler argument above does not need this second witness.

For a coordinate-potential construction in any group G with an abelian
subgroup H isomorphic to C3^4 of index r, three chosen right-coset fibers
can be independently right-translated into H. An abelian extra relation
and its reverse have opposite potential rows, so the restricted fibers
must have an injective triple-sum map (see `research_note.md`, section 4.1).
Consequently all three original set sizes cannot exceed 3r. For index
four this excludes (16,16,16), independently of the action used to form a
semidirect product. It does not exclude arbitrary complex tensor
degenerations with the same source and target dimensions.
