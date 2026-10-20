# Second pass: mixed sectors and prospective improvement criteria

Date: 2026-10-20. Author: ChatGPT, in a session directed by the repository owner.

## Status and provenance

No exponent below 9/4 is established. This checkpoint preserves incomplete work at the owner's request.

The runtime retained the first-pass archive but not the second-pass temporary directory. The programs here reconstruct the recorded code. Their reports were regenerated for this checkpoint. They are not byte-identical historical files.

The dimension program removes unused imports, orders candidates deterministically, and verifies the reconstructed packing. The tensor program adds a reproducible symmetrizer calculation to the recorded Koszul routine.

The mathematical arguments have no independent review or Lean formalization. Finite ranks are exact computations over the rationals.

## 1. Dimension-only mixed-sector search

The search fixes a source C(a,b), one shared leg, and the dimensions of its two other legs. A candidate sector is a convolution in any leg orientation. Its shared dimension cannot exceed the source's shared dimension. The two other dimensions consume separate integer budgets.

An exact dynamic program maximizes the sum of first-pass profile values. This is a relaxation: it ignores the coefficient identities needed for a tensor degeneration.

The regenerated search covers 63 source pairs and 189 shared-axis cases. It finds 85 cases whose relaxed score exceeds the source profile. These are not 85 new tensor inequalities.

The largest ratio in this search is

$$
\frac{334611}{298870}=1.11958711145\ldots.
$$

Its source is C(10,12), with dimensions (10,12,21). The target has three C(4,7) sectors, each with its output as the shared ten-dimensional leg. The nonshared dimensions sum to 12 and 21.

Dimension feasibility does not establish this target. The following two smaller examples demonstrate why stronger tests are necessary.

## 2. A Koszul obstruction

Consider a proposed degeneration from C(4,6) to three C(2,3) sectors. Each target convolution has its four-dimensional output as the shared leg. The other leg dimensions are 6 and 9, matching the source.

For a tensor in X tensor Y tensor Z, the Koszul map used here is

$$
Y^*\otimes\Lambda^p X\longrightarrow Z\otimes\Lambda^{p+1}X.
$$

A rank-one tensor contributes a map of rank at most binomial(dim(X)-1,p). Linearity gives the corresponding bound for rank-r tensors. Matrix-rank conditions are closed, so the bound also holds for border rank.

For C(2,3), with its output as X and p=2, the exact 12 by 12 matrix has rank 12. Three sectors give a direct sum of three such maps, with rank 36. A rank-one tensor contributes at most binomial(3,2)=3. Therefore the target has border rank at least 12.

The source C(4,6) has rank at most 4+6-1=9 by polynomial interpolation over the complex numbers. Border rank cannot increase under degeneration. This specific candidate is impossible.

The numerical calculation does not prove a general formula for arbitrary convolution lengths. The larger identical-sector family remains outside this finite certificate.

## 3. A symmetrizer obstruction

A second candidate starts from C(3,3), with dimensions (3,3,5). Its target consists of C(2,2) with shared output, plus a dot-product sector of size three. The proposed profile ratio is 57/56.

In coordinates, the target is

$$
\sum_{i,j=0}^1 x_{i+j}y_i z_j+\sum_{i=0}^2x_i y_2z_{i+2}.
$$

For its Z-slices M_z, consider the linear equations

$$
M_zL=(M_zL)^{\mathsf T}\quad\hbox{for every }z,
$$

where L is an arbitrary 3 by 3 matrix.

For C(3,3), the slices are symmetric, and L=I solves these equations. This property remains true under invertible changes on the first two legs, with the corresponding change in L. Linear changes on the third leg preserve it as well.

Existence of a nonzero L is a closed determinantal condition. It therefore persists in the orbit closure. The proposed target has equation rank nine, so its only solution is L=0. The source has equation rank eight and a one-dimensional solution space.

Thus this exact target is not a degeneration of C(3,3). The report gives its support and independent equation rows. This argument concerns the stated target, not every mixed-sector construction.

## 4. Draft homogeneous-profile rigidity

This is a lemma under additional analytic hypotheses. Their applicability to every relevant tensor character is not established in this checkpoint.

Assume F is positive, symmetric, continuously differentiable, separately concave, and homogeneous of degree d. Assume also

$$
F(x,3y+x)\ge3F(x,y)\qquad(x,y>0).
$$

Symmetry and Euler's identity give

$$
\partial_2F(1,1)=\frac d2F(1,1).
$$

Concavity then gives

$$
3F(1,1)\le F(1,4)\le\left(1+\frac{3d}{2}\right)F(1,1).
$$

Consequently d is at least 4/3. At d=4/3, both inequalities are equalities. Concavity forces F(1,y) to be affine on [1,4]. Iteration of y -> 3y+1 extends that affine formula to every y>=1. Symmetry and homogeneity give

$$
F(x,y)=K\min(x,y)^{1/3}\left(\max(x,y)+\frac{\min(x,y)}2\right),
\qquad K>0.
$$

This is an equality-case calculation for the specified continuous model. It is not a construction of a character or a lower bound for omega.

## 5. Draft conditional curvature criterion

Retain the hypotheses of Section 4. Suppose, for some delta>0,

$$
2F(1,2)-F(1,1)-F(1,3)\ge\delta F(1,1).
$$

Write s_j=F(1,j+1)-F(1,j). Concavity gives s_3<=s_2 and s_1<=d F(1,1)/2. The proposed gain gives s_2<=s_1-delta F(1,1). Hence

$$
3F(1,1)\le F(1,4)
\le\left(1+\frac{3d}{2}-2\delta\right)F(1,1).
$$

Thus d>=4(1+delta)/3. If these hypotheses hold for every relevant character with d=1/t, a character-independent delta implies

$$
\omega\le\frac9{4(1+\delta)}.
$$

Neither a positive delta nor the required analytic bridge is proved here. This criterion does not change the recorded exponent.

## 6. Incomplete stronger scoring search

The earlier search estimates unrecognized sectors by a single dot-product slice. This pass planned stronger estimates from recursive shared-leg decompositions and full direct sums.

For the normalized symmetrized profile at t=3/4, a full direct sum suggests the lower bound

$$
\mathcal P\left(\bigoplus_iT_i\right)
\ge\left(\sum_i\mathcal P(T_i)^{3/4}\right)^{4/3}.
$$

This follows from additivity of each character and the finite-sum Holder inequality. It differs from plain addition for sectors sharing one leg.

The draft also proposed a tight-support entropy score. Its precise theorem dependencies and support hypotheses need review before use. The preserved source fragment is inert text. No completed enhanced-search run or witness is claimed.

## 7. Other investigated directions

Radix substitution gives a simple restriction from C(a,b) tensor C(c,d) to C(a+q(c-1),b+q(d-1)) when q<=min(a,b). Polynomial exponents cover consecutive intervals, and output substitution combines carries. No improvement was obtained from this comparison.

A proposed multiplicative law for thin-profile coefficients remains unproved. The reverse tensor comparison needed for that law was not constructed. It must not be used to strengthen the exponent.

Full product-filtration extraction, oriented character constraints, and basis-change searches remain open directions. No exhaustive search or impossibility result for these directions is recorded.

## 8. External dependencies and next certificate format

The first-pass scalar profile and its scope remain in the immutable archive. OpenAI's 9/4 theorem and polynomial constructions are external work. Uznański's rectangular analysis motivates the oriented and homogeneous questions.

The three repositories suggested by the owner are compared in [the source review](../../../docs/external_followups.md). Filmus's identities-to-exponent statement gives a finite certificate format worth implementing next. Its tensor-identity hypotheses cannot be replaced by dimension feasibility.

## Reproduction

From the repository root, run:

```sh
python research/ai/2026-10-20-session2/dimension_search.py --output /tmp/dimension_search.json
python research/ai/2026-10-20-session2/tensor_checks.py --output /tmp/tensor_checks.json
python -m unittest discover -s tests -p test_session2_checkpoint.py -v
```

The dimension program uses the standard library. The tensor program requires SymPy 1.14.0. Neither program requires network access.
