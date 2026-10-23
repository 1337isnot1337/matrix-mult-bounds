# Finite covers for the two nonsplit central-cover targets

October 21, 2026. Claim `AI-NONSPLIT-FINITE-COVERS-001` is a written,
AI-derived proof with exact finite certificates. No independent
mathematical review, Lean formalization or exponent improvement is claimed.

## 1. Statement and scope

Write G=SL(2,F5), H=G x C2, and T for the coefficient-of-identity group
trace tensor. The F5 in G defines the abstract finite group; the tensor
coefficient field below is F4=F2[w]/(w^2+w+1). The explicit certificates give

    SR_F4(T_G) <= 98 < 100 = SR_F4(M10),                (1)
    SR_F4(T_H^tensor(3)) <= 6155844
                         < 6426225 = 2535^2.           (2)

Consequently no characteristic-two degeneration from G realizes M10.
Every single rectangular target M(a,b,c) degenerating from H in
characteristic two satisfies abc<=2481. In particular M(13,13,15), whose
volume is 2535, is excluded. Coefficient-one injective-coordinate/strict
integer-potential constructions over C reduce to characteristic two, so
these same one-copy construction classes are excluded over C.

Arbitrary complex degenerations and constructions from arbitrary higher
source powers are outside the statement. Slice rank is not assumed
submultiplicative. The preceding split-cover result separately excludes
its M10 target; together the finite results close the three selected
central-cover coordinate/potential targets, not the general exponent
problem.

## 2. Independent check of the actual nonsplit source

The certificate lists 120 F4 vectors in the actual group basis, ordered
by the identity matrix followed by the other determinant-one two-by-two
matrices over F5 in lexicographic order. A hexadecimal vector has its
coefficient-one bit plane in bits 0..119 and its coefficient-w bit plane
in bits 120..239. The verifier regenerates the group from determinant
one, using matrix multiplication modulo five. It computes basis rank
120 over F4 and all 120^3=1728000 original trace coefficients.

There are exactly 1577 nonzero coefficients. The first 88 basis vectors
and the last 32 give a full tensor direct sum P+B: every nonzero term
lies entirely in one component. No algebra classification is needed for
this assertion; it is checked directly on the full tensor.

The saved degrees have one-leg generating polynomials

    P(t)=9+8t+10t^2+8t^3+18t^4+8t^5+10t^6+8t^7+9t^8,
    B(t)=16(1+t).                                     (3)

Every nonzero P term has total degree at most eight, and every nonzero B
term has total degree at most one. Both assertions are checked against
all original coefficients. No upper bound is transferred backward from
the degeneration G to its split central cover.

Discovery lifted the preceding A5 F4 idempotents through the square-zero
central augmentation ideal and lifted each vector into its Peirce
corner. Integer coordinate covers were found by a bounded numerical
mixed-integer optimizer. Acceptance does not trust those constructions,
the optimizer's dual bounds, a radical pilot, or an unverified support:
it uses only the explicit vectors, coordinate sets and integer degrees,
reconstructed in separate dense-field arithmetic without NumPy.

## 3. A one-copy cover of G

A coordinate cover chooses sets S_X,S_Y,S_Z such that every nonzero
coefficient has at least one index in its corresponding set. Assigning
each term to the first covering coordinate in a fixed order yields a
slice decomposition with at most |S_X|+|S_Y|+|S_Z| slices.

For P the certificate selects the same 22 coordinates in each leg,
giving 66 slices. For B it selects 16 coordinates in the first leg,
none in the second, and 16 in the third, giving 32. Concatenating gives
98 slices for the original tensor T_G. The verifier checks every
nonzero coefficient against these sets; it does not accept numerical
rounding as evidence of a cover.

For comparison the full H tensor has a saved one-copy cover of 172
slices, covering all 6308 nonzero terms. This does not beat the selected
target's one-copy slice rank 169. Equation (2) uses a different finite
cube argument, not an extrapolation of that 172-slice cover.

## 4. An independently counted cube cover for H

In the extra C2 factor use (1,epsilon), epsilon=1+z. Its full group trace
has support 000,001,010,100, since epsilon^2=0 and the identity-coefficient
trace takes value one on both 1 and epsilon. In particular the 000 term
is retained. The verifier checks all eight central triples.

Expand T_H^tensor(3) into eight direct-sum block words. A word with j P
positions has binomial(3,j) copies up to position permutation. Choose
positive integer weights s,a,b: scale P's saved degrees by s, B's saved
degrees by a, and the extra C2 epsilon-degree by b. The maximum total
degree in a nonzero triple is

    D_j=8sj+a(3-j)+3b.                                (4)

The one-leg degree polynomial for that word is

    P(t^s)^j [16(1+t^a)]^(3-j) (1+t^b)^3.             (5)

Choose cutoffs (c1,c2,c3) summing to D_j-2. A term avoiding every leg's
coordinates of degree at most its cutoff would have total degree at
least D_j+1. Therefore these coordinate sets cover every nonzero term.
Adding the three cumulative counts bounds the word's slice rank.

The exact certificate uses:

| j | Words | (s,a,b) | D_j | Cutoffs | Slices per word |
| ---: | ---: | --- | ---: | --- | ---: |
| 0 | 1 | (1,1,1) | 6 | (1,1,2) | 147456 |
| 1 | 3 | (1,3,2) | 20 | (6,6,6) | 384768 |
| 2 | 3 | (1,3,3) | 28 | (8,9,9) | 898096 |
| 3 | 1 | (1,1,3) | 33 | (10,10,11) | 2159796 |

Their sum, with word multiplicities, is 6155844. Different words may
use different weights because their slice decompositions are concatenated
after the full direct-sum expansion.

The producer multiplies integer polynomials. The verifier instead groups
the explicit basis coordinates by component, saved degree and central
bit. There are 22 classes. It counts all 22^3=10648 class triples with
their integer multiplicities, checks their total 240^3=13824000, and
checks every block-word degree distribution separately. It also checks
every possible degree triple of total at most D_j against the saved
cutoffs. No floating optimizer or asymptotic estimate is an acceptance
premise.

## 5. Target lower bounds and field transfer

The finite identity SR(M_m)=m^2 holds over every field. The direct proof
is in the [preceding finite split-cover note](../2026-10-21-central-cover-finite-slices/proof.md),
section 4. It imports the bounded-rank matrix-space dimension theorem
over arbitrary fields from [de Seguins Pazzis, arXiv:1507.05375v2,
Theorem 1.1](https://arxiv.org/pdf/1507.05375v2), with Flanders and Meshulam
credited for that theorem and its field generalization. A slice
decomposition with p,q,r slices gives a matrix subspace U of dimension
at least m^2-p whose matrices all have rank at most floor((q+r)/m).
The external dimension inequality contradicts p+q+r<m^2. The case when
the characteristic divides m is included; the trace pairing on all
matrices is still nondegenerate.

Over an algebraic closure bounded slice-rank loci are closed: project the
closed slice-subspace incidence from a finite union of products of
Grassmannians. This is proper. Together with monotonicity under linear
maps, it proves that degenerations cannot increase slice rank. Extending
any alleged characteristic-two degeneration to an algebraic closure
also makes the F4 certificates available there.

For G, equation (1) immediately excludes M10. For H use cyclic symmetry
of the group trace. A degeneration to M(a,b,c), with its two cyclic
permutations, would give a degeneration from T_H^tensor(3) to
M(abc,abc,abc). Thus

    (abc)^2 <= 6155844,
    2481^2=6155361 <= 6155844 < 6160324=2482^2.         (6)

Hence abc<=2481, which excludes the selected volume 13*13*15=2535.
The strict target gap is 6426225-6155844=270381.

In the maintained complex coordinate/potential class, input variables
map injectively to group coordinates times integer Laurent monomials.
All intended coefficients are one with exponent zero; every unintended
term has positive exponent. The same family works in characteristic two
without division or cancellation. It would give precisely the forbidden
degeneration. This proves the stated complex construction-class
exclusions and does not extend them to arbitrary input mixing.

## 6. Relation to the earlier method barrier

The tight-limit certificate proves asymptotic lower source costs above
103.4 for G and above 195.3226 for H in characteristic two. Its proof
explicitly leaves finite-power tests open. The one-copy and cube upper
bounds here therefore do not contradict it. Slice rank is not
submultiplicative, so neither 98 nor the cube root of 6155844 is asserted
as an eventual exponential source cost. These are finite certificates
for the actual full nonsplit sources.
