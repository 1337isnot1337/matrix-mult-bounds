# Scalar monomial corrections to the group construction

Status: written, unreviewed. No improving witness has been constructed.

For coordinate vertex sets S,T,U with injective pair maps, use the usual
group-coordinate contraction. Give its first target variable (s,t) the
factor epsilon^(a_s-b_t), its second (tt,u) the factor
epsilon^(b_tt-c_u), and its third (uu,ss) the factor
epsilon^(c_uu-a_ss). Every intended matrix term has weight zero and
coefficient one. Every other supported monomial has weight

    a_s-a_ss+b_tt-b_t+c_uu-c_u.

Let R be a set of r such extra monomials, with every extra outside R
having positive integer weight. Add r independent scalar tensors. Map one
to the negative of each listed monomial with its stated epsilon factor.
Each scalar tensor produces exactly that one monomial. This cancels the
terms in R identically, including any Laurent poles, while leaving the
intended terms unchanged. Every surviving extra tends to zero. Thus

    C[G] direct-sum D_r degenerates to M(|S|,|T|,|U|).

Negative powers in these maps do not represent division gates in the final
algorithm. Multiplying out a fixed Laurent offset makes the coefficient
extraction polynomial. Under the kth tensor power its degree is O(k), so
interpolation costs a polynomial factor in k. This is the standard
approximate-algorithm/interpolation argument; see Bini--Lotti--Romani,
*Approximate Solutions for the Bilinear Form Computational Problem*,
[SIAM J. Comput.9(1980)](https://epubs.siam.org/doi/10.1137/0209053).
This cancellation construction and argument are not claimed as historically
new. The maintained verifier checks the complete coefficient support.

If the complex irreducible degrees of G are d_i, the source has matrix
blocks d_i plus r scalar blocks. Tensor-power block algorithms and
interpolation give asymptotic rank at most sum d_i^omega+r. Cyclically
symmetrizing the rectangular target gives a square target of side
V=|S||T||U| after three copies. Consequently

    V^(omega/3) <= sum d_i^omega+r.

This is the usual matrix block/asymptotic-rank comparison, with the
classical approximate-rank framework credited also to
[Schonhage1981](https://epubs.siam.org/doi/abs/10.1137/0210032).
When every d_i and1 are less than V^(1/3), the ratio of the right side to
V^(t/3) is strictly decreasing in t. A strict comparison at t=tau therefore
forces omega<tau. The implication includes tensor powers, cyclic
symmetrization, interpolation and arbitrary complex constants; it has the
usual all-size exact division-free asymptotic meaning. It is conditional
on an actual verified correction witness.

For G=S5 x C2 squared and target M(18,18,20), the complex degrees are four
copies of1,1,4,4,5,5,6. An exact integer-root comparison allows r=8 at
tau=22499/10000. The required improving correction witness is missing.

The finite C3-squared control has target M2. It has exactly eight intended
terms and two opposite extra terms. Its integer potentials give those
extras weights1 and-1. One auxiliary scalar cancels the negative term,
leaving only a positive-weight error. This tests the actual Laurent
cancellation step, without passing an improving source-cost comparison.

Disjoint exact Farkas circuits give a separate limited obstruction. Each
circuit must lose at least one of its extra inequalities before all
remaining weights can be positive. If their monomial supports are
disjoint, r circuits need at least r individually cancelled monomials.
Pair injectivity ensures that every extra differs in both indices in each
vertex family, so its potential row specifies that monomial uniquely.
This lower bound concerns individual monomial cancellation. A general
rank-one tensor can cancel several monomials, and is not excluded by it.

## Arbitrary low-rank Laurent corrections

There is a stronger necessary condition for the same fixed coordinate
group maps. The auxiliary maps may now be arbitrary Laurent maps from
D_r, rather than individual monomial cancellations. Their tensor has
every flattening rank at most r for each nonzero epsilon. Call an extra
term bad if its group-component exponent is nonpositive.

If bad extras occupy q distinct third-leg matrix coordinates, then r>=q.
Choose one such extra for each third coordinate. Use its pair of first-
and second-leg variables as a row of a flattening of the auxiliary tensor;
use the selected third coordinates as its columns. The selected rows are
distinct, because their group products are the inverses of distinct
third-leg labels, which are injective.

Every extra differs on the two middle vertex indices. Indeed, equality
there would telescope the first two group labels, and injectivity of the
third pair map would make the term intended. Thus each selected row has
zero target coefficient in every column. The group component is zero off
the selected diagonal, since the third labels are distinct. Its diagonal
entry is epsilon^w_i, with w_i<=0. Therefore the auxiliary diagonal must
be -epsilon^w_i+o(1), while every off-diagonal auxiliary entry is o(1).

Multiply row i by epsilon^(-w_i). This factor has nonnegative exponent,
so all off-diagonal entries still tend to zero and the diagonal tends to
-1. The normalized auxiliary matrix tends to -I_q. Matrix rank is closed
under limits, giving q<=r. The same argument applies cyclically to either
other leg. This proof uses the actual coordinate support and fixed integer
vertex weights; it does not assume the auxiliary summands are monomials.

Consequently q exact Farkas circuits supported on pairwise disjoint sets
of third-leg coordinates require auxiliary rank at least q. Every vertex
potential makes some extra nonpositive in each positive dependence; those
bad extras belong to distinct third coordinates. A packet of nine such
circuits for the first trade-free model excludes every rank-eight Laurent
correction to its fixed group-coordinate maps, for any integer vertex
potentials. Different vertex sets, mixed group-coordinate maps, and larger
auxiliary rank remain open. The C3-squared control attains the one-circuit
rank-one boundary, so the diagonal argument is sharp in that small case.
