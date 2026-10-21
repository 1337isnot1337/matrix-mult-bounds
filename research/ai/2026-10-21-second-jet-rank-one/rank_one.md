# Low-rank spanning forces no second-jet growth

Written local proof, unreviewed, October 21, 2026. No exponent improvement
or historical priority is claimed. Canonical leading maps and extension
spaces are credited to PR45, inspected at
5d4a941930a61a195342acfac50045384f5361e4. Our verifier replays the needed
premises. The new low-rank spanning argument sharpens that package's
second partial-space dimension bound from 37 to exactly 12.

The principle is general: suppose a corrected residue map takes values in
R direct_sum W0, where every nonzero R matrix has rank at least n. Suppose
W0 lies in a matrix cross of rank at most s, and its quotient modulo that
cross is represented by a local restriction of
a canonical linear matrix space spanned by matrices of rank at most r.
If r+s<n, its R component vanishes. On each spanning preimage the rank
bound proves vanishing; on the kernel the cross alone does so. Linearity
then handles every preimage. The application below has r=2,s=8,n=11.

## The leading space and the matrix target

Write S(t)=S0+tS1+t^2 S2+... for the first flattening after two regular
output maps. The source first dimension is 112. The canonical leading
output images E,F each have dimension four, and W0=rowspan S0 has
dimension 12. The target has leg dimensions 100,110,110 and first-slice
space R consisting, up to constant invertible matrix row/column maps, of
X tensor I11 for X in Mat_(10x10). Every nonzero member has rank at least11.

Every matrix in

    W1=W0+{xS1:xS0=0}

is supported in E tensor C+B tensor F and has rank at most8. Thus R and
W1 intersect trivially inside the saturated limiting space L0. Dimension
counting forces

    W1=W0,   dim L0=112,   L0=R direct_sum W0.            (1)

The canonical first-jet classification gives twenty-dimensional covector
spaces E_B,E_C containing the rows of P1,Q1 outside their leading output
images. Each contains the four leading covectors G. Put K=ker S0. The
canonical bilinear tensor

    H=(K,E_B,E_C)T

has first flattening rank25. The extension data and that rank are adopted
with their original attribution; the new spanning certificate is below.

## A complete second-jet correction

For x in K choose y(x) linearly with xS1=y(x)S0, using (1). The regular
row t^-2(x-t y(x))S(t) has residue

    Z2(x)=xS2-y(x)S1 in L0.

Let D2(x) be its R component under (1), and put W2=W0+span Z2(K).
Changing y changes Z2 only by W1=W0. Projection away from both leading
images gives exactly

    pi Z2(x)=(x,pi_B P1,pi_C Q1)T = H_actual(x).          (2)

Every other term, including P2 Q0, P0 Q2, top first-jet rows, the y(x)S1
correction and every W0 correction, belongs to the same old cross
E tensor C+B tensor F. That entire cross has matrix rank at most8.
Therefore, whenever the canonical H(x) has matrix rank at most2,

    rank D2(x) <= rank H_actual(x)+8 <=2+8=10.

As a target matrix slice D2(x) must vanish. The same conclusion holds
when H(x)=0. This accounts for the complete second coefficient and its
row correction; no term is discarded.

## Twenty-six rank-two slices span all twenty-five directions

Let L=(ell_0,...,ell_11) be the source indices (i,s,z) in the order

    i=1,2; s=0,3; z=0,3,6.

Write U_j=e_(ell_j), V_j=e_(ell_(6+j)) for j=0,...,5, and
C=e_(0,0,6). First take these ten covectors in K:

    U0,U1,U3,U5,U2-U4;
    V0,V2,V4,V5,V1-V3.

Add, for r=1,-1,2, the three covectors

    r^4 U1 + r U2 + r^3 V1 + V2 + r^2 C.

Finally add the thirteen copies obtained by reversing the two short
indices of every source coordinate. This gives26 explicit covectors.
Every resulting H matrix has rank exactly2. The report gives a nonzero
2-by-2 minor for each and verifies the full rational factorization

    M = M[:,columns] M[rows,columns]^-1 M[rows,:]

in all400 entries. The flattened26-by400 matrix has a saved nonzero
25-by25 minor. Since canonical H has first rank25, these low-rank matrices
span its entire first-slice image over Q and over C. These are exact
coefficient identities, not sampled-rank evidence.

For any x in K, express H(x) in this spanning set. Subtract the same
combination of its source covectors to obtain x0 with H(x0)=0. The
previous section gives D2=0 on every spanning covector and on x0. By
linearity it vanishes on all of K. Consequently

    W2=W1=W0,   dim W2=12,
    H_actual=0.                                        (3)

In particular all first-jet bilinear coefficients outside both leading
images must vanish. This is stronger than a rank-ten condition. It excludes
a dense open subset of the compatible first-jet space, but does not exclude
all first jets or their later higher-order lifts.

The theorem concerns final rank-four canonical leading maps. Output maps
that reduce those ranks require new premises. It permits arbitrary
ungraded first derivatives, arbitrary second and higher jets, and arbitrary
Laurent maps on the remaining leg. Growth starting at order three or later
is not excluded, and no matrix-multiplication exponent gain is established.
