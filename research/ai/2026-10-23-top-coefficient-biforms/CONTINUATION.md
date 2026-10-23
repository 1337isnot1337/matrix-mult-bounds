# Continuation checkpoint: single polynomial top coefficient

Date: October 23, 2026. Starting main SHA bd03b9dadba03b1089595f03ff7a091ee9e7ddbc. Branch: research/top-coefficient-biforms-20261023-t2.

The owned question is the literal R_(a,b) rank formula for biforms with a nonzero constant coefficient at z^0, all lower z coefficients constant, and one arbitrary polynomial coefficient w(x) at z^e. This includes genuinely three-term nondiagnonal e=2 biforms, with arbitrary coefficients in w. The complete all-field theorem and proof are in proof.md. Claim AI-TOP-COEFFICIENT-BIFORM-RANK-001 is proof-written-unreviewed, never independently reviewed, formalized or an exponent improvement.

## Mathematical checkpoint

The active-row dependency module has e free polynomial terminal coordinates. Backward recurrence uses invertibility of the constant coefficient c_0 in K[x]. Terminal vector V_j has predictable degree d*floor((a+j)/e) because the highest-degree paths use as many z^e steps as possible. The leading polynomial coefficient vectors are triangular on the first e row groups under the residue permutation (a+j) modulo e. This yields

    rank R = ab + sum_(j=0)^(e-1) min(b,d*floor((a+j)/e))

over every field and for all a>=2, b>e>=1, nonzero polynomial w of x-degree d<a. Proof uses full coefficient columns H=0,...,a+b-2. It does not assert anything about arbitrary variable lower z coefficients.

## Exact controls

The local offline Python 3.13.5 verifier passed 3,372 literal full-source modular ranks: 900 exhaustive GF2, 1,836 exhaustive GF3, 216 seeded GF5/GF7/GF101, and 420 degree witnesses. The separately implemented coefficient-lookup QQ/SymPy 1.14.0 oracle passed 24 exact rank comparisons. Three focused unittests passed, including a deliberately wrong-rank mutation control. Fixed receipt: results/top-coefficient-biforms-2026-10-23/verification.json.

Reproduce:

    python -I research/ai/2026-10-23-top-coefficient-biforms/verify.py --receipt results/local/top-coefficient-biforms.json
    python -I research/ai/2026-10-23-top-coefficient-biforms/verify_charzero.py
    python -m unittest discover -s tests -p test_top_coefficient_biforms.py -v

The full project-wide regression, historical replay, and hosted CI have not been completed in this task run. The Pyroam isolated runner returned a connector internal error for both public cloning and a minimal shell probe; no remote shell mathematics was run. The GitHub connector was used for authenticated repository read and topic-branch writes, and all mathematical computation was performed locally. No secret or private input was submitted to Pyroam. The published verification code and pinned receipt must be checked again by hosted CI at the current branch head before merge.

## Concurrency and ownership

102 open PRs were inspected by title at approximately 17:30 UTC, including #209 (affine-z), #171 (binomial), #186 (general biform gap), #207 (diagonal polynomial Toeplitz), and #208 (geometric diagonal). Those distinct findings are credited, not imported. PR #214 then began consolidation of 132 topic branches; by the next poll many original PRs, including #209, were closed as superseded without merging. Source heads remain cited exactly in sources.json. This package adds a different constant-lower-coefficient, arbitrary-top-polynomial family and must be reconciled with the consolidation tree before integration.

## Remaining bottleneck

A general u(x)+z*v(x)+z^2*w(x) has multiple nonconstant coefficient polynomials. If the leading recurrence coefficient is not a unit in K[x], its polynomial kernel can no longer be parametrized by freely chosen terminal polynomials. Determine its column-reduced minimal indices and whether primitive degrees plus resultant data can determine them. A concrete next step is to compute and compare rational coefficient triples with identical coarse invariants and differing kernel indices, then prove an exact classification or counterexample.

The statement is about ranks of individual biform slices, not a tensor-rank bound, a compatible three-leg degeneration, or an improvement below arithmetic exponent 9/4. Neither archived 2026-10-20 research tree has been touched. Preserve claim status, external attribution and all CI/review gates.
