# Complete F8 coordinate-target source-cost obstruction

October 21, 2026. AI-GROUP-F8-CLOSURE-016. Written proof, unreviewed.
No matrix multiplication exponent improvement is established.

## 1. Statement

Let G=F8^2:C7, with C7 acting by multiplication by nonzero F8 scalars.
No single matrix target obtained from injective pair maps and strict
vertex potentials passes the usual complex character-degree source-cost
comparison at any positive exponent s<=9/4.

This excludes all vertex-family sizes, including unequal sides, empty
normal fibers, nonlinear four-point fibers, all directions and all offsets.
It concerns this particular group construction and source-cost comparison.
Arbitrary complex tensor degenerations, several extracted targets together,
joint tensor powers and other groups are not excluded.

The proof combines the existing exact source-degree/rank-locus frontier,
normal-coset restriction and classical Koszul bounds with new even-slice
pencils and a complete count certificate. The source degrees, rank-locus
theorem and odd-slice pencils retain their earlier credit:

- [Source and normal-fiber prerequisites](../2026-10-20-group-potentials/octal_research.md).
- [General complex rank-locus obstruction](../2026-10-20-group-potentials/rank_locus_proof.md).
- [Normal-coset theorem and four-point cap](../2026-10-20-normal-coset-koszul/research_note.md).
- [Higher odd-slice pencils and unequal frontier](../2026-10-20-f8-unequal/research_note.md).

For classical Koszul flattenings and their border-rank use, see Landsberg
and Ottaviani, [*New Lower Bounds for the Border Rank of Matrix
Multiplication*, Theory of Computing 11 (2015)](https://theoryofcomputing.org/articles/v011a011/).
The general rank inequality is not a new result of this repository.

## 2. Exact source-cost frontier

The complex irreducible degrees are seven copies of1 and nine copies of7;
the source dimension is448. For a target M(a,b,c), the usual comparison is

```
(a*b*c)^(s/3) > 7 + 9*7^s.                                  (1)
```

Ordinary flattening requires max(ab,bc,ca)<=448. Sort a<=b<=c. If a=1,
the volume is at most448, so(1) fails at9/4: its left side is less than448,
and its right side exceeds448. For a>=2 the maintained exact scan checks
all4811 sorted integer shapes with b*c<=448. Exactly59 pass(1) at9/4.
The earlier general complex rank-locus theorem leaves26 of these shapes.
Their componentwise minimal elements are

```
(16,16,26) (16,17,24) (16,18,23) (16,19,22) (16,20,21)
(17,17,23) (17,18,22) (17,19,21) (17,20,20)
(18,18,21) (18,19,20) (19,19,19).
```

Each of the26 surviving shapes contains at least one of these twelve
matrix subtargets. Restricting the vertex families preserves pair
injectivity and every strict potential inequality. Thus excluding these
twelve formats excludes every improving shape at9/4 in the stated frame.

It also suffices for every positive s<=9/4. Put v=(abc)^(1/3). If v<=7,
one degree-seven term alone prevents(1). If v>7, the normalized source
cost 7*(1/v)^s+9*(7/v)^s is strictly decreasing in s. Therefore a shape
failing(1) at9/4 cannot pass it at any smaller positive s. Shapes already
excluded as tensor degenerations remain excluded independently of s.

All twelve minimal formats have sides greater than14. Normal unique sums
therefore give the existing four-point cap on every normal fiber. Namely,
each family has a fiber containing three points; the full difference
planes of three points in two other families sum directly to a
four-dimensional subspace of F2^6. The remaining fiber can meet each of
its four cosets at most once. This applies to nonlinear four-point fibers.

## 3. Even-slice improvement for rectangular blocks

For d slices X_t of size a by b and 0<=p<d, the classical map is

```
K_p: wedge^p C^d tensor C^b -> wedge^(p+1) C^d tensor C^a,
     w tensor v |-> sum_t (e_t wedge w) tensor X_t v.
```

A decomposable tensor contributes rank at most binomial(d-1,p).
Consequently, a normal-coset matrix target must satisfy

```
sum_i c_i r_(d,p)(a_i,b_i) <= 64*binomial(d-1,p),             (2)
```

for every cyclic alignment and every ordering of the three vertex-family
counts. This follows by restricting all source legs to the abelian normal
subgroup H, whose complex multiplication tensor has rank64. The target
restriction is the direct sum of M(a_i,b_i,c_i). Choose the first-leg
projection separately on each direct-sum block; its Koszul matrix has
c_i copies of the chosen pencil. Summing these matrix ranks proves(2),
using closed rank conditions under degeneration. No additivity assertion
about tensor border rank is used.

For rectangular pencils, d=2p+1 need not give the best bound. The additional
explicit ranks, for a,b=1,...,4, are

```
d=4, p=1, rank-one divisor3:
 3  5  6  6
 4  8 12 12
 4  8 12 16
 4  8 12 16

d=6, p=2, rank-one divisor10:
10 16 19 20
14 26 35 40
15 30 45 60
15 30 45 60
```

The tables are asymmetric. Each use records its orientation; swapping
the family ordering is a global permutation of tensor legs, which
preserves border rank. No symmetry of these tables is assumed. Each
entry is the rank modulo101 of an exported integer pencil, hence a
lower bound for its rank over C. The verifier checks all32 new pencils
and the32 existing five- and seven-slice pencils. Zero rows/columns are
zero. The classical three-slice table supplies a fifth test level.

For example, the previous(16,20,21) count survivor has an alignment with
three normal blocks M(3,4,4). The six-slice3-by4 pencil is a full-rank
60-by60 matrix, giving rank3*4*60=720>640 in(2). The small matrix is also
replayed modulo103 as a control. Passing the previous odd-slice tests did
not make these counts realizable.

## 4. Complete count cover

Count arrays belong to {0,...,4}^7. For each required total, the verifier
enumerates cyclic classes and checks independent bounded-composition
coverage using coefficients of(1+x+...+x^4)^7. Short orbits are retained;
in particular the all-three array of total21 has an orbit of size one.

For each minimal format, the certificate supplies a grid for each of its
three pairs of count classes. A grid byte can prove either:

1. Pair-capacity failure at one cyclic shift: sum_i a_i*b_(i+s)>64.
2. A Koszul averaging violation at a specified level, orientation and shift:
   if W=sum_i r(a_i,b_(i+s)), the third total n satisfies n*W>7*64*divisor.

The second condition follows by averaging the third array's seven shifts.
A zero byte makes no claim about the pair. The verifier checks every
nonzero byte and builds graphs from zero bytes. It then enumerates every
triangle of these graphs. Every such triangle must have an explicit
two-byte witness specifying the Koszul level, global family permutation
and two cyclic shifts. Its exact rank must exceed the source ceiling.
Tags are checked for validity, ranges and complete byte consumption.

The complete cover verifies9539875 pair bytes. Eleven minimal formats
leave no triangles after these pair tests. The format(16,18,23) leaves90;
all90 receive checked explicit alignments. The compressed certificate is
2494175 bytes and expands to9540055 bytes. Its uncompressed SHA256 is

```
2bd87167ad5fbb21a72fac11b6b4c308afb85948d0972be7d3e2a7842798e309
```

The earlier balanced and(16,16,26) proofs remain valid. The unified cover
checks those formats again and supplies the other ten exclusions. The
compiled program only discovers tags; its output is not accepted without
the independent standard-library Python replay. Tests reject incorrect
pair tags, incorrect explicit triangle tags, corrupted pencil ranks and
coefficients, and truncated or trailing compressed streams.

Combining this finite cover with Section2 proves the stated one-source
construction barrier. It closes the previously open unequal F8 search
within this frame, while the exponent-improvement goal remains open.

## 5. Reproduction

Use the repository's maintained verification dependencies; no SAT, LP,
floating arithmetic or optional packages are needed for acceptance.

```sh
python research/ai/2026-10-21-f8-coordinate-closure/closure_certificate.py results/f8-unequal-2026-10-20/koszul-pencils.json results/f8-coordinate-closure-2026-10-21/even-pencils.json results/f8-coordinate-closure-2026-10-21/count-cover.zlib --output results/local/f8-coordinate-cover.json
python -m unittest discover -s tests -p test_f8_coordinate_closure.py -v
```

For discovery reproduction, from the repository root:

```sh
python research/ai/2026-10-21-f8-coordinate-closure/discover_pencils.py results/f8-unequal-2026-10-20/koszul-pencils.json --output results/local/f8-even-pencils.json --table-output results/local/f8-rank-tables.txt --shape-output results/local/f8-minimal-shapes.txt
c++ -O3 -std=c++17 research/ai/2026-10-21-f8-coordinate-closure/discover_cover.cpp -o /tmp/f8-discover-cover
/tmp/f8-discover-cover results/local/f8-rank-tables.txt results/local/f8-minimal-shapes.txt results/local/f8-count-cover.raw
```

The raw discovery file can be passed directly to the imported `replay`
function. The CLI accepts its zlib-compressed form. Compression is storage
only; every decompressed tag is checked mathematically. The maintained
test compares the replay receipt with the committed result.
