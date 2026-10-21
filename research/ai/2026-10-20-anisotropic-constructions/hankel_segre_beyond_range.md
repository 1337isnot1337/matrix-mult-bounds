# A Segre counterexample outside the fixed-scheme range

October 21, 2026. This note records an exact limitation of the
[Hankel symbol dimension argument](hankel_symbol_dimension.md).
It does not change the proved frontier or establish a new exponent.

The proved argument requires

\[
3r\le m=a+b-1,\qquad r<\min(a,b).
\]

Under these hypotheses a linear map from a matrix space that sends
every rank-one matrix into the Hankel-rank-at-most-r locus has image
dimension at most r. The condition cannot be dropped altogether.
There are Segre images of larger dimension outside this range.

## 1. A four-dimensional image of two-by-two matrices

For a=b=4 and r=3, associate to a two-by-two matrix the sequence

\[
\begin{pmatrix} A&B\\ C&D\end{pmatrix}
\longmapsto h=(0,A,B,0,C,D,0).
\]

Its four-by-four Hankel matrix is

\[
H(h)=
\begin{pmatrix}
0&A&B&0\\
A&B&0&C\\
B&0&C&D\\
0&C&D&0
\end{pmatrix},
\qquad
\det H(h)=(AD-BC)^2.
\tag{1}
\]

Consequently every rank-one two-by-two matrix maps to a Hankel
matrix of rank at most three. The linear image has dimension four.
For example, (A,B,C,D)=(1,2,3,6) gives rank exactly three.

Thus the conclusion “image dimension at most r” is false for these
parameters, even for a square matrix domain. Here 3r=9>m=7.
The source slice rank estimate includes additional polynomial
multiplication factors; this example alone does not give a tensor
restriction or disprove any claimed full-slice estimate.

## 2. A family with varying recurrence

Take integers

\[
r<\min(a,b),\qquad
2r+1\le m=a+b-1<3r.
\]

Put

\[
\ell=m-2r,\qquad k=3r-m=r-\ell.
\]

For a two-by-k matrix T define a length-m sequence by

\[
h_{\ell+j}=T_{0j},\qquad
h_{\ell+r+j}=T_{1j},\qquad 0\le j<k,
\tag{2}
\]

with all other coordinates zero. The two sets of positions are
disjoint and lie in the sequence range, so this map has image
dimension 2k.

On rank-one matrices T=uv^T, equation (2) becomes

\[
h=\sum_{j=0}^{k-1}
v_j\bigl(u_0\delta_{\ell+j}+u_1\delta_{\ell+r+j}\bigr).
\]

These sequences satisfy the polynomial recurrence

\[
u_0h_{s+r}=u_1h_s,
\qquad 0\le s\le m-r-1.
\tag{3}
\]

Indeed, the nonzero first block ends at r-1, and the second block
starts at m-r, one position after the largest index s in (3).
The two blocks match after shifting by r. No later nonzero block
is present within the sequence range.

For u_0 nonzero, each Hankel column numbered at least r is
u_1/u_0 times the column r positions earlier. Hence the a-by-b
Hankel matrix has rank at most r. All its (r+1)-minors are
polynomials in u and v, so their vanishing extends to u_0=0.
The upper bound is attained: take u_0=u_1=1 and only v_(k-1)=1.
The leading r-by-r Hankel minor is the reverse identity matrix.

The image dimension exceeds r exactly when

\[
2k>r\quad\Longleftrightarrow\quad m<\frac52r.
\tag{4}
\]

The smallest square-domain example is r=3,m=7,k=2, which gives
(1). At m=3r-1 this family has image dimension two. It then
exhibits varying annihilating schemes without violating the
dimension-r conclusion. In particular, it does not settle whether
some stronger dimension theorem holds at the currently relevant
A(7,8),r=5 boundary m=14.

## 3. Exact controls and scope

The accompanying standard-library script expands all 24 terms of
the determinant in (1), using exact polynomial arithmetic. It also
checks (3) as a formal polynomial identity for every parameter
format with 2<=r<=8 and 2r+1<=a+b-1<3r, with a<=b and r<a.
For each format it checks the rank-r reverse-identity specialization
and a specialization at u_0=0 using rational row reduction.

```sh
python research/ai/2026-10-20-anisotropic-constructions/hankel_segre_beyond_range.py --output results/anisotropic-constructions-2026-10-20/hankel-segre-beyond-range.json
python -m unittest discover -s tests -p 'test_hankel_segre_beyond_range.py'
```

This is an elementary counterexample to an unrestricted extension
of one proof step. It neither weakens the proved 3r<=m theorem nor
adds an exclusion beyond its stated hypotheses. The saved frontier
continues to use that proved range. The calculations and proof
were checked within this generating session; no external review or
formal verification is claimed.
