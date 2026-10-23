# Complete coordinate recognition in an additive support

Question R6 asks whether stronger block recognition can improve the monomial
search. Here is the exact boundary for recognizing an entire sector as a
convolution by coordinate permutations. This is a written, unreviewed proof,
not a claim about arbitrary linear changes of basis.

Let S be a nonempty finite set of distinct integer triples (x,y,z), all
satisfying x+y=z. Every coordinate value under discussion occurs in S.
The coefficient of every supported triple is one. Fix an output axis o;
write r,s for the other two axis cardinalities and m for its cardinality.

**Theorem.** S is the support of C(r,s), with output axis o, after independent
coordinate permutations if and only if

    m = r+s-1,             |S| = r*s.

In that case sorting the axes, and reversing a subtracted input axis when
necessary, already supplies such permutations. Consequently the archived
search's sorted-index/reversal recognizer has no missed whole convolution
sectors that arbitrary coordinate permutations could recover.

Proof. Necessity follows from the dimensions and number of supported entries
of C(r,s). For sufficiency, rewrite the original equation as a sum equation
with the chosen output: z=x+y, x=(-y)+z, or y=(-x)+z. Each input pair can
occur at most once, because it determines the output value. The cardinality
|S|=r*s therefore implies that every pair occurs. Let the two transformed
input sets in increasing order be A_0<...<A_(r-1) and B_0<...<B_(s-1).
Their sumset is exactly the output coordinate set, of size r+s-1.

Any monotone lattice path from (0,0) to (r-1,s-1), taking unit steps right
or up, encounters r+s-1 strictly increasing sums A_i+B_j. It therefore
enumerates the entire output set in increasing order. Every vertex (i,j)
lies on such a path and occurs at step i+j. Its output coordinate thus has
sorted index i+j. This is the desired convolution support, including the
cases r=1 or s=1. Negating an input set reverses its sorted order, proving
the stated restricted form of the permutations. All coefficients stay one,
so the support identification is also an exact tensor identification over
any field. QED.

If r,s>=2, this also forces both transformed input sets to be arithmetic
progressions with the same positive step. Indeed, the two grid vertices
(i+1,j) and (i,j+1) have the same index in the sorted sumset, hence
A_(i+1)-A_i=B_(j+1)-B_j for every valid i,j. The output progression has
that step as well. Singleton inputs are excluded from this corollary;
their other coordinates may have arbitrary gaps.

The integer ordering is a property of the coordinate labels, not an ordering
of the coefficient field. The same proof works for real additive labels.
It does not apply to arbitrary nonadditive supports, repeated triples with
multiplicity, or arbitrary coefficients. Recognizing a proper restriction,
a sum of blocks obtained by another degeneration, or a tensor after general
linear input mixing is a separate problem. The slice fallback on a sector
that fails the theorem can still underestimate that sector's character value.

## Ordered finite searches

The search forms components on the y and z axes, sharing x. Swapping x and
y changes which axis is shared and can change the sum of component scores,
even though the source profile P_*(a,b) is symmetric. Thus restricting to
a<=b is a specified finite scope, not a symmetry reduction for this score.
For q integer weights 0,...,q-1, normalized by minimum zero independently on
each input, the complete ordered census with a,b>=2 and a+b<=M contains

    sum_(a=2)^(M-2) sum_(b=2)^(M-a)
        (q^a-(q-1)^a) (q^b-(q-1)^b)

candidates. The acceptance script checks this count independently of the
candidate loop and compares exact Fraction scores. No exhaustive finite
alphabet search proves a statement about all weights or arbitrary bases.

## Attribution

The original support degeneration, component partition, profile and
sorted-index recognizer are archived owner-directed AI work in
`research/ai/2026-10-20/search_degenerations.py`, pinned in `sources.json`.
PR118 independently maintains exact ranking and support certificates and
preserves the distinguished first input. This package does not depend on
that unmerged PR. The lattice-path completeness proof and ordered census
are the present owner-directed Codex continuation. No historical priority,
independent review, formalization or exponent improvement is claimed.
