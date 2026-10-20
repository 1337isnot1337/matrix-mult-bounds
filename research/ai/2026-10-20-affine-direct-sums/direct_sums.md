# Extracting full direct sums from the determinant filtration

Date: 2026-10-20. AI-derived written construction and finite experiment;
unreviewed, not Lean formalized. No improvement below omega <= 9/4.
The associated-graded product and character framework are attributed in the
[companion note](research_note.md). This investigation begins after proving
that the old fixed-label family cannot exclude the matching scalar profile.
See [concurrent contributions](COORDINATION.md) for the overlap with the
other agents and the precise distinct contribution here.

## A stronger extraction

For C(a,b) tensor C(c,d), use the associated-graded blocks

    (i,j,k) = (i,j,i+j), with block C(A_i,B_j),
    A_i=a+c-1-2i, B_j=b+d-1-2j.

Fix integers r,s,u with r, s and r-s nonzero. On the support k=i+j,

    (ri+sj+u)^2
      = [(r^2-rs)i^2+2ru i+u^2]
        + [(s^2-rs)j^2+2su j] + rs k^2.                 (1)

Each bracket is a weight on just one leg. Consequently its zero set extracts
the blocks on the affine line ri+sj+u=0. Distinct points of this line have
distinct i,j,k, so these blocks form a **full direct sum**. The exclusions
r=0, s=0 and r=s are essential: each would repeat a label on one leg.

This can be implemented as one elementary degeneration of the original
product, rather than assuming a new closure property of degeneration. The
determinant filtration has nonzero blocks only for k>=i+j. Add M(k-i-j) to
the weights in (1), with M greater than the sum of the maximum absolute
values of the three bracket weights over the finite leg ranges. Every
k>i+j term then has positive weight; every k=i+j term has weight (1).
Blocks k<i+j are identically zero by multiplication preserving the filtration.

The output labels range over

    0 <= k < min(a+b-1,c+d-1).

The construction thus retains actual auxiliary spaces and uses integer
weights; it does not cancel a tensor factor. It works over the complex
numbers in the model under investigation.

## Character consequence

For any full direct sum D=direct_sum_l T_l, character additivity and
finite-sum Holder give

    P(D)^t >= sum_l P(T_l)^t.

Indeed, put x_(pi,l)=lambda_pi(T_l). Holder says
product_pi(sum_l x_(pi,l))^(1/6)
>= sum_l product_pi x_(pi,l)^(1/6), and the latter block factor equals
P(T_l)^t. Monotonicity and multiplicativity therefore imply

    [P(a,b)P(c,d)]^t
        >= sum_{ri+sj+u=0} P(A_i,B_j)^t.                 (2)

At t=3/4, this is a sum of 3/4 powers, a different constraint from the plain
fixed-label sums. For instance a=b=c=d=2 and i=j give

    P(2,2)^(3/2) >= P(3,3)^(3/4) + 1.

The matching profile survives this example. A finite violation of (2) would
exclude P_*; it would still need a universal growth argument to improve omega.

## A finite upper bound covering every matched selection of whole blocks

Rather than enumerate only affine lines, assign weight
W_ij=P_*(A_i,B_j)^(3/4) to every grid cell. Any full direct sum of whole
graded blocks with distinct i,j,k uses distinct rows and columns. Drop the
restriction that k=i+j be distinct. The resulting **larger** feasible set is
all bipartite matchings of the row and column labels.

All weights are positive, so an optimal matching uses every label on the
smaller side. A subset dynamic program computes its maximum using upper
integer bounds on W_ij. This covers unrealizable matchings as well; its
purpose is an upper bound, not a claim of a degeneration for every matching.

For a positive rational x=N/D and Q=2^96, compute

    L=floor_fourth_root(floor(N^3 Q^4 / D^3)).

Then L/Q <= x^(3/4) <= (L+1)/Q, with an exact endpoint when
L^4 D^3=N^3 Q^4. The dynamic program maximizes upper endpoints and compares
the result with a lower endpoint for [P_*(a,b)P_*(c,d)]^(3/4).
Single-row/column cases reduce to an exact rational comparison by
monotonicity; this avoids calling an interval overlap an equality proof.
No floating-point value is used for acceptance or ordering.

The recorded run exhausts all 6,561 ordered source quadruples with each
dimension from 1 through 9. None of these relaxed matching scores violates
P_*. Counts and the maximizing nontrivial witness are in
`results/affine-direct-sums-2026-10-20/full_direct_sums.json`. Those results exclude
the whole-block matching search class on this finite grid, including every
affine line extraction there. They do not prove all-size compatibility or
cover splitting a graded block, mixing bases between blocks, or tensor powers.

## Reproduction and next question

Run:

```sh
python research/ai/2026-10-20-affine-direct-sums/full_direct_sums.py --max-size 9 --output results/affine-direct-sums-2026-10-20/full_direct_sums.json
```

The program also exports a finite weight certificate for the smallest
nontrivial diagonal extraction. Tests independently multiply binary forms
in determinant-adapted bases and check all coefficients, zero forbidden
blocks, and the exact surviving support. These coefficient checks use SymPy;
the matching-bound verifier uses the Python standard library only.

The remaining potentially stronger mechanism is extracting independent
pieces *inside* graded blocks or from tensor powers whose labels are words,
rather than just selecting whole blocks from one product. A larger search
over the same fixed-label sums cannot help, and this finite result identifies
another precise class that supplies no violation on the recorded grid.
