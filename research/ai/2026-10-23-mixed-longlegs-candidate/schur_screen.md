# Complete Schur-component screen for the tensor-power contractions

2026-10-23. Companion to [source_b_koszul.md](source_b_koszul.md).
Written and checked in the same generating session; no external review,
formalization, target construction, or exponent improvement is claimed.

## Natural component ranks

Work over C. The simultaneous contraction map Dq is equivariant for the
symmetric group Sq acting on its q second-leg positions, with the matching
permutation of its q output summands. This action commutes with every
global general linear change on the three tensor legs.

For a partition lambda of q, the central idempotent of C[Sq] projects to
the lambda-isotypic subspace. Restricting Dq to this fixed subspace gives
another matrix whose coefficients are linear in the tensor. Its rank is
therefore invariant under basis changes and cannot increase in a degeneration.
By the ordinary isotypic decomposition, this rank is f_lambda times a
well-defined multiplicity-space rank, where f_lambda is the dimension of
the corresponding irreducible Sq representation.

For a canonical Full-only source of parameters(a,N,c), the preceding note
identifies the Dq kernel, equivariantly for Sq, as

\[
H^0(O(a-1-q))\otimes(C^{N-c})^{\otimes q}.
\]

Consequently the kernel multiplicity of lambda is

\[
\max(a-q,0)\dim S_\lambda(C^{N-c}),
\]

and the multiplicity-space rank is

\[
a\dim S_\lambda(C^N)
-\max(a-q,0)\dim S_\lambda(C^{N-c}).
\]

This is a finite useful family: all components are injective for q>=a.
At a=5, only the partitions of1,2,3,4 need to be checked. The exterior
components are the second-leg Koszul ranks already computed independently
by pr_audit.

## Exact target computation

The target is precisely the canonical(5,100,140) mixture in the preceding
note. The separate first identifications are fixed as stated there.

The Dq kernel splits by ordered second-leg block labels. A permutation
has trace zero on a summand unless those labels are constant along each
cycle. For fixed labels, the verifier computes a rational row reduction
of the literal small coefficient matrix. The free input coordinates give
a basis of its kernel. The trace of a permutation on that basis is the
sum of the appropriate permuted free-coordinate coefficients; this needs
no floating-point eigenvalue calculation.

For a given cycle type, each cycle can choose one block of a given type.
The factor for that choice is the number of copies of that type. Different
cycles may choose the same block; no distinctness condition is imposed.
This gives the exact whole-kernel character by summing the small traces.
Character inner products then recover every kernel multiplicity.

The implementation checks the small character tables by orthogonality.
Thirty separate Full-only controls reproduce the predicted kernel character
max(5-q,0)*(b-1)^(number of cycles). All recovered multiplicities are
nonnegative integers and sum, with their representation dimensions, to
the independent total Dq kernel dimensions.

## Results

Every component passes the necessary rank inequality.

| Partition | Source rank | Canonical target rank | Target minus source |
| --- | ---: | ---: | ---: |
| (2) | 12965 | 12730 | -235 |
| (1,1) | 12735 | 12587 | -148 |
| (3) | 607340 | 584960 | -22380 |
| (2,1) | 1180560 | 1144036 | -36524 |
| (1,1,1) | 573540 | 559238 | -14302 |
| (4) | 19186640 | 18058265 | -1128375 |
| (3,1) | 55361160 | 52392132 | -2969028 |
| (2,2) | 36195675 | 34347288 | -1848387 |
| (2,1,1) | 53225865 | 50650046 | -2575819 |
| (1,1,1,1) | 17050935 | 16315992 | -734943 |

Degree1 is the third-leg flattening and has rank140 for both tensors.
All q>=5 source components have full column rank, so the candidate passes
them automatically in the same ambient format. Thus no member of this
particular family excludes the canonical candidate.

The three exterior values12587,559238,16315992 agree with pr_audit's
separate graded-occupancy exact computation. This is agreement between two
implementations in the same session, not external independent review.

Reproduce after the preceding Dq report exists:

```sh
python research/ai/2026-10-23-mixed-longlegs-candidate/shared_output_schur.py
```

The complete small traces, cycle weights, source controls, characters, and
component dimensions are retained in
`results/mixed-longlegs-candidate-2026-10-23/shared_output_schur_controls.json`.
This closes the specified rank-screen route for this canonical candidate;
it does not establish that the tensor degeneration exists.
