# A short cohomological formula for matrix Koszul ranks

AI-derived written proof, unreviewed, October 20, 2026. This is a second
derivation of the ranks in matrix_koszul.md, without representation theory
or an assumption on characteristic. No historical priority is claimed.
The imported facts are the cohomology of projective space, as in the
[Stacks Project, tag 01XT](https://stacks.math.columbia.edu/tag/01XT), and
the bounded double-complex construction, [tag 012X](https://stacks.math.columbia.edu/tag/012X).

For l,r>=2 put v=lr. The kernel of the first-leg power-p Koszul map of
M(l,1,r), whose domain has dimension l binom(v,p), has dimension

    k_p = sum_(j=r)^p (-1)^(j-r) binom(v,p-j)
                         binom(j+l,l-1) binom(j-1,r-1).       (1)

The rank is l binom(v,p)-k_p. Multiply by b for M(l,b,r). Formula (1)
holds over every field, for 0<=p<=v. An empty sum is zero.

## Identify the tensor in a cohomology row

Take X=P^(l-1) times P^(r-1), L=O(1,1), F=O(-l-1,0). Write
homogeneous coordinates x_1,...,x_l and y_1,...,y_r. The top cohomology
of O(-l-1) has basis

    f_i = 1/(x_1 ... x_l x_i).

Multiplication by x_k takes f_i to zero in cohomology if k!=i and to
1/(x_1 ... x_l) if k=i. Therefore the map

    H^0(L) tensor H^(l-1)(F) -> H^(l-1)(F+L)

has coefficient delta_(i,k) y_j on x_k y_j tensor f_i. It is exactly
M(l,1,r), in the same first-leg convention as matrix_koszul.md.

## The three nonzero cohomology rows

Use the complex C^k=exterior^(p+k)(A) tensor (F+kL), with differential
wedge by the universal section of A tensor L. The section has a unit
coordinate on every standard product chart; contraction there proves the
complex is locally contractible. The bounded product Čech double complex
has zero total cohomology, as in all_koszul.md. Its first page is

    E_1^(k,q)=exterior^(p+k)(A) tensor H^q(F+kL) => 0.

Here F+kL=O(k-l-1,k). Its only nonzero rows are:

- q=l+r-2, at k<=-r;
- q=l-1, at k=0,1, of dimensions l and r before exterior factors;
- q=0, at k>=l+1.

The middle row's single differential is the desired Koszul map. The top
row cannot reach the bottom row by a later differential: d_(l+r-1)
would land at k<=l-1, where that bottom row is zero. The only possible
top-to-middle later differential is

    d_r : E_r^(-r,l+r-2) -> E_r^(0,l-1).

The only middle-to-bottom later differential starts at k=1, not k=0,
because the bottom row starts at k=l+1. Thus every top-row E_2 group
except k=-r is zero (it has no later incoming or outgoing differential),
and the displayed d_r is an isomorphism onto the entire kernel in the
middle row. This remains true when l=r: its incoming and outgoing maps
on that page involve different middle-row positions.

At k=-j, j>=r, the dimension of the top cohomology of F-jL is

    h_j=binom(j+l,l-1) binom(j-1,r-1).

Euler characteristic of the finite top-row complex therefore gives

    dim ker K_p = sum_(j=r)^p (-1)^(j-r) binom(v,p-j) h_j,

which is (1). This uses only the zero positions and exact total complex;
no maximal-rank guess for an internal differential is needed. All steps
work over an arbitrary field.

## Boundary cases and comparison controls

If l=1, the map w -> sum_j e_j wedge w tensor v_j is injective for
p<r: a coefficient of w is isolated by choosing an exterior coordinate
outside its support. Thus its rank is binom(r,p) for 0<=p<r, and zero
at p=r. If r=1, the map is exterior multiplication
exterior^p(U) tensor U -> exterior^(p+1)(U), which is surjective over
every field, with rank binom(l,p+1).

For 2<=l,r<=6 and every power, (1) agrees with the complete partition
sum from the independent complex Casimir derivation. The retained sparse
coefficient controls supply additional checks. Those finite comparisons
are controls, not the proof of (1). The short alternating sum allows the
finite target search to continue without enumerating large partitions.
