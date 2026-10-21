# All mixed graphs close at the partner a=b=1

Written proof, unreviewed, October21,2026. Claim
`AI-ALL-MIXED-GRAPHS-A1-097`. The exponent remains9/4.

For the canonical A4 leading flags, let B have its full maximal seven-frame
at partner a=b=1. Let C be any five-space in its maximal seven-frame
with nonzero mixed projection. Equivalently, C contains m+sum h_j*d_j
for some arbitrary h in C^6 and an arbitrary boundary four-space.

**Result.** Only the four common-plane normals satisfy the necessary
target conditions. The adopted shifted moving-plane induction excludes
M(10,10,11) for these first spaces, arbitrary later maps, delayed unequal
growth and a Laurent first-leg map. The source torus extends the result
to a=b nonzero. Other partner ratios and leading flags remain open.

## 1. Start with two fixed families

Adopt096's uniform dichotomy. In the84-dimensional quotient of the full
88-dimensional normal system by its four planes, every necessary normal
lies in one of two constant linear families, of dimensions54 and36.
The first has zero stable boundary rows; the second has zero boundary
projection. This is uniform in all six h, not a generic specialization.

Use the original seven C columns throughout this proof. In particular,
do not replace the mixed column by zero by selecting a graph first.
The known obstruction rows annihilate the actual C five-space.

## 2. Two source operations valid for every graph

First, if a constant combination of known source rows has all six
boundary columns zero, it is a normal linear form times the mixed
covector. It must vanish on m+sum h_j*d_j, whose mixed coordinate is one.
Hence that linear form is zero for every h. The checker obtains the
complete coefficient-row kernel of the six boundary columns and takes
the complete kernel of the resulting mixed-column forms. These are
the recorded `mixed_only` reductions, with no parameter denominator.

Second, use the virtual third tensor on the64 adapted source covectors
from090/093. Subtract each slice's part in the known coefficient rowspace.
Each saved residual has either support covered by at most two B/C
vertices or joint B coefficient rank at most two. The saturated target
rank gap therefore forces its restriction to C to vanish. Add its seven
rows to the known annihilator. The checker verifies every source index,
cover or complete coefficient rank and the unitriangular source change.
These arguments are precisely the previously credited source-rank input;
no finite numerical rank supplies a uniform inference.

Saved triangular three-minors also force normal linear forms to vanish:
each determinant is a nonzero rational multiple of that form's cube.
Complete rational kernels preserve every complex solution. These three
operations give the initial dimension sequences

    stable:           54 -> 38 -> 18 -> 16,
    zero projection:  36 -> 28 -> 22 -> 16 -> 14 -> 10 -> 8 -> 6.

Each case adds twelve adapted sources, positions16--19 and24--31.
All known source covectors still annihilate C, so their full matrix of
seven columns has rank at most two throughout.

## 3. Exact cubic identities reduce both small families

The source partition splits the16-dimensional stable family into two
eight-variable blocks, with seven source rows per block. For each block,
the certificate retains115 actual three-minors f_i and five independent
linear forms L_j. Exact rational coefficient identities give

    L_j^3 = sum_i c_ji*f_i.

The checker reconstructs the minors and verifies all120 cubic monomials.
Rank at most two forces the five forms to vanish. Taking both complete
kernels reduces16 to6, with three variables in each block.

The six-dimensional zero-projection family splits into two three-variable
blocks. In each, six actual three-minors express the cube of one linear
form. Their vanishing reduces six to four dimensions. Four additional
source slices, positions20--23, and saved triangular cubic minors then
reduce4 to0. This eliminates the entire zero-projection branch.

## 4. Cover the stable remainder by four explicit linear branches

Write the three remaining variables in each stable block as(u,v,w).
Five actual three-minors per block satisfy exact rational span identities
for the two cubic forms

    (v-w)^2*(v+w),       (v-w)^2*(u-w).

Their vanishing implies either A: v=w, or B: v=-w and u=w. This elementary
case split includes every complex point. No assertion about a radical
algorithm is required. Combining the choices on both source blocks gives
four necessary linear branches, with dimensions4,3,3,2.

Apply the source operations of Section2 to each. Four more low-rank
sources and the saved mixed-column/cubic constraints give

    AA: 4 -> 0,       AB: 3 -> 2 -> 0,
    BA: 3 -> 2 -> 0,  BB: 2 -> 0.

Every source and minor is replayed. Thus all84 quotient directions are
eliminated in the exhaustive54/36 dichotomy. Only the four planes remain.

## 5. The all-order consequence and torus

Claims089--094 provide the shifted moving-boundary induction once the
necessary normal kernel consists only of the four common planes. It
allows arbitrary later coefficients, unequal delayed first orders and
a Laurent first-leg map. Its hypotheses now hold for every h and every
actual boundary four-space at a=b=1. Hence the stated saturated matrix
target is excluded without a graph genericity assumption.

The credited source torus sends a,b to a/b,1 when b is nonzero, and sends
the graph coordinates to

    (h0/b^5,h1/b^2,h2/b^2,b*h3,b*h4,b^4*h5).

The maintained checker verifies the frame covariance as in094. This
invertible transformation of all graph coefficients extends the result
to a=b nonzero. The source's total-weight18 identity retains089's credit.

This closes the specified partner locus, not every partner, source or
leading flag. It constructs no improving tensor. Exact replay and CI
do not establish independent mathematical review or formalization.
