# Exact width-two monomial score barrier

Claim `AI-WIDTH-TWO-MONOMIAL-001`: written, unreviewed. This is an
all-size statement about the **specified sector score**, not about the
true value of unrecognized tensors, arbitrary degenerations, or omega.

## Question and source convention

The R6 search records only bounded integer-weight experiments. Does its
score ever exceed the matching profile on C(2,b) or C(b,2), for arbitrary
integer weights and arbitrary b>=2?

Use the coefficient-one convolution support `(i,j,i+j)`. For integer
input weights u_i,v_j, retain all terms minimizing u_i+v_j on each output
diagonal. Group terms by connected components of the bipartite graph on
the **second and third** legs; the first leg is shared. Follow exactly
the archived recognition rule: an order-preserving reindexing, optional
axis reversals and an output-axis choice may identify a convolution;
otherwise score the sector by its largest coordinate-slice size.
Convolutions receive the existing matching profile P_*. In particular,

    P_*(1,m)=m,     P_*(2,b)=(4b+2)/3  (b>=1).

The recurrence, profile, shared-leg interpretation and scoring rule are
prior work. [sources.json](sources.json) pins their exact source bytes.
The counting proof below needs no new external theorem. Swapping the
two input legs changes the sector graph and must be treated separately.

## The short shared leg: C(2,b)

Put delta=u_1-u_0 and

    s_k=sign(v_k-v_(k-1)-delta),  1<=k<b.

At output k, s_k>0 selects y_(k-1), s_k<0 selects y_k, and
s_k=0 selects both. The two exterior outputs select y_0 and y_(b-1).
Thus the graph is a path with some internal edges removed. Every
nonempty component consists of m consecutive y vertices, m-1 interior
z vertices, and e exterior z vertices, where e is 0, 1 or 2. An isolated
y vertex carries no term and is omitted. There is no isolated z vertex.

The complete sector scores are:

| Exterior endpoints e | Nonempty sizes | Recognized support or slice | Score |
| --- | --- | --- | --- |
| 2 | m>=1 | C(2,m), with z as output | (4m+2)/3 |
| 0 | m>=2 | C(2,m-1), with y as output | (4m-2)/3 |
| 1 | m>=1 | Single slice if m=1; otherwise largest slice m | m |

For e=0, reverse the x coordinate: the interior relation k=i+j becomes
j=(1-i)+(k-1), displaying the stated convolution. For e=1 and m>=2,
the format is (2,m,m), and the support has 2m-1 terms. None of its
axes has size equal to the sum of the other two minus one (including
m=2), so the archived convolution test cannot recognize it. Its two
x slices have sizes m and m-1, while all other slices have size at most
two. The score is therefore exactly m. For m=1 it is one scalar.

Let A be the number of active y vertices, M_1 the total number of y
vertices in components with e=1, and N_e the number of components with
e exterior endpoints. Counting the b+1 output vertices gives

    b+1 = A + N_2-N_0.

Summing the three rows of the table now proves the exact identity

    score = (4A+2(N_2-N_0)-M_1)/3
          = P_*(2,b) - [2(b-A)+M_1]/3.                 (1)

Consequently every integer-weight assignment has score at most
P_*(2,b). Equality holds **exactly** when every y coordinate is active
and no component has one exterior endpoint. Every unequal score loses
at least 1/3. This gap is sharp for each b>=2: take u=(0,0) and
v=(0,...,0,1), giving one e=2 component of size b-1 and one e=1 scalar.

### Complete equality-support count

Each of the 3^(b-1) sign words is realizable by integer weights: take
u=(0,0), v_0=0 and v_k=v_(k-1)+s_k. Hence this classification has no
weight-magnitude cutoff. Different words give different retained
coordinate supports; no claim of tensor-isomorphism uniqueness is made.

In an equality support, the first and last components have e=2. At any
nonzero sign the intervening z endpoint belongs to exactly one side.
The component types must therefore alternate e=2,e=0,...,e=2.
Conversely such an alternating composition, with all e=2 sizes at least
one and all e=0 sizes at least two, determines an equality support.
For r components of type e=0 there are r+1 of type e=2, with minimum
total y size 3r+1. Distributing the remaining b-3r-1 vertices among the
2r+1 ordered components proves the exact count

    E_b = sum_(0<=r<=floor((b-1)/3)) binomial(b-r-1,2r). (2)

Thus E_1=E_2=E_3=1, and E_b=2E_(b-1)-E_(b-2)+E_(b-3) for b>=4.
For example, E_4=2, E_8=21 and E_10=65. The recurrence follows from
the formal generating function z(1-z)/(1-2z+z^2-z^3).

## The short second leg: C(b,2)

Use signs of u_k-u_(k-1)-(v_1-v_0). If no internal diagonal ties,
the two y vertices belong to separate components. Each sector has one
y coordinate, so it is a dot product; there are b+1 retained terms in
total. The score is b+1, a deficit of (b-1)/3.

If at least one internal diagonal ties, both y vertices and all z
vertices belong to one component. If every diagonal ties, the original
C(b,2) is retained and equality holds. Otherwise let r<=b be its active
first-leg size and t<b-1 the number of ties. Its format is (r,2,b+1)
and its term count is b+1+t<2b. For convolution recognition, z as output
would require r=b and 2b terms; x as output would require r=b+2;
y as output would require r+b=2. All are impossible for b>=2.
The score is therefore its largest slice. The x and z slices have at
most two terms, and each y slice at most b, so the score is at most b.

Thus equality for C(b,2) occurs only for the full original support.
Every proper support loses at least (b-1)/3, sharply attained by any
tie-free sign word. The orientation difference is essential: C(2,4)
has a proper equality support, whereas C(4,2) does not.

## Consequence and limits

This closes both width-two orientations of the archived monomial score
for all sizes and all integer weights. The argument also classifies the
same support rule for real weights, without asserting that arbitrary
real powers define an algebraic one-parameter degeneration.

The theorem neither bounds stronger scores on the unrecognized (2,m,m)
components nor handles arbitrary coordinate deletions, nonmonomial
bases, cancellations, tensor powers or minimum input size at least three.
It does not construct a tensor character or improve the exponent.
The finite census checks the formulas against the frozen original
scorer; the written proof establishes the universal quantifiers.
No independent mathematical review, formalization or priority is claimed.
