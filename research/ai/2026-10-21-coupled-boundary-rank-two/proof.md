# Simultaneous rank-two boundary obstructions force the complete boundary family

October 21, 2026. Owner-directed Codex work; written and unreviewed.
No independent review, formalization, historical priority, matrix target
or smaller exponent is claimed.

## 1. Exact normal system and statement

Adopt the complete 228-dimensional first-normal parameter space at the
canonical A4 leading flags, with the same source-row correction quotient
as the previous moving-boundary and biform packages. Their dependencies,
coefficient conventions and current bytes are pinned in sources.json.
Write the parameter as delta in C^228.

The two boundary-quotient obstruction maps are linear matrix-valued maps

    Psi_B,Psi_C: C^228 -> Mat_(200 by 12)(C).

They are the first twelve quotient columns of the previously constructed
200-by 16 complement systems, with column-major vectorization. The actual
source builder and the saved coefficient matrices are checked against
each other; no coordinate parameter sample defines these maps.

**Theorem.** The following are equivalent:

    rank Psi_B(delta)<=2 and rank Psi_C(delta)<=2;
    Psi_B(delta)=0 and Psi_C(delta)=0.                      (1)

The common solution space is 28-dimensional and is exactly the previously
identified complete boundary-compatible normal family. Each individual
matrix space contains nonzero rank-two matrices: explicit controls have
rank pairs(2, 4) and(4, 2). The simultaneous hypothesis is essential.

## 2. The universal cubic-minor certificate

Rank at most two forces every three-by-three minor to vanish. The report
exports 232 particular minors of the two actual obstruction matrices.
At each stage their three diagonal entries are nonzero rational multiples
of the same linear form ell in the current normal parameters, and every
entry above the diagonal is identically zero. Thus the exact determinant
identity is

    det minor = c * ell^3,  c in Q nonzero.                (2)

Equation(2) and the rank assumption force ell=0 over C. Collect the
forms from both sides together and pass to their complete linear kernel.
The four successive stages are:

| Current normal dimension | Minors on each side | Rank of all forced forms | Remaining dimension |
| ---: | ---: | ---: | ---: |
|228|82|132|96|
|96|20|40|56|
|56|12|24|32|
|32|2|4|28|

Every stage exports its kernel matrix, the selected row/column positions,
the exact linear forms and each nonzero determinant ratio c. Independent
replay checks all diagonal identities, triangular zeros, kernel products,
full kernel ranks and dimensions. There is no variable denominator and
no division by ell; ell is forced to be zero, including all exceptional
complex parameter values.

On the final 28-dimensional parameter space, **both complete coefficient
maps are zero matrices**. Consequently every solution of the two rank
conditions lies in their joint zero kernel. The reverse implication in
(1) is immediate. The product of the four exported kernel bases has
rank 28, so all dimensions refer to the original 228-parameter model.

These are finite polynomial identities proving an implication at every
complex parameter, not an inference from finitely many tested parameter
values. No claim is made that successful software replay constitutes
independent mathematical review or formalization of the argument.

## 3. Identification with the prior biform family

Let F be the 448-by 228 matrix mapping normal parameters to actual normal
coefficients, inherited from the complete first-normal system. Let K be
the product of the four kernel bases, of shape 228-by 28. Let N be the
earlier 448-by 28 complete boundary-compatible basis saved with the third
normal tensor. The report exports an invertible rational 28-by 28 matrix R
such that

    F K = N R.                                             (3)

All 448-by 28 coefficients of (3) and the full rank of R are checked. Thus
the newly forced family is the same normal space on which the prior
biform core was computed; equality of dimensions alone is not being used
to identify two possibly different spaces.

## 4. Necessary classification at the balanced boundary threshold

In the credited canonical first-boundary normal system, arbitrary first
spans of dimension 10 in the respective 12-dimensional boundary quotients
must be annihilated by Psi_B(delta),Psi_C(delta). Hence both obstruction
ranks are at most two. Sections1--3 put delta in the complete 28-dimensional
family without assuming its first subspaces are coordinate spaces.

For a non-plane normal there, the prior third matrix space is
Mat2 tensor Z_delta, with dim Z_delta>=2 and no rank-one matrix in
Z_delta. When the credited target source-rank gap requires projected
third first dimension at most two, the balanced-puncture gap theorem
forces that entire projected space to vanish.

The preceding projective classification therefore applies. The quotient
kernels must be products of two base lines with their auxiliary C2 spaces.
Those base lines have a common(1, 1) factor

    g=(r*x0+s*x1)(r*y0-s*y1), [r:s] in P1,

times arbitrary nonzero residual linear forms of degrees(0, 1) and(1, 0).
Every such cancellation point has a two-dimensional non-plane normal
fiber, plus the four independent common-plane directions. The exact
sixteen-case certificate and its source attribution remain in the
preceding balanced-puncture package.

This is a necessary classification in the stated normal and third-gap
model. It does not prove that every such normal prolongs to later
coefficients, straighten a non-plane motion at all orders, or construct
the full matrix slice space. In particular it is not an all-order
exclusion of the 10-by 10 case, and the separate 12-by-8 case is untouched.

## Attribution and limits

The canonical source, leading flags, complete first-normal space,
source-row correction maps, boundary quotient conventions and previous
28-dimensional basis are inherited with their original credits. The
232 coupled cubic identities and their exact joint-kernel calculation
are the local continuation. The application imports the separately
written balanced-gap theorem and complete conic classification, both
unreviewed, with their external inputs kept explicit there. No new
external theorem is needed for the cubic implication itself.

The original 228-coordinate pilot found no simultaneous nonzero rank-two
pair; that was discovery guidance only. The proof is the complete
polynomial certificate, not the pilot. No bound below 9/4 is established.
