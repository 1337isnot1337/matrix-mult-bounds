# An obstruction to equivariant cyclic matrix constructions

October 20, 2026. AI-derived written proof, unreviewed;
AI-CYCLIC-EQUIVARIANT-050. **No exponent improvement is established.**
All statements are over C. The source A_a, its invariant normalization
and its rational Clebsch-Gordan basis are those of the maintained
[cyclic recoupling package](../2026-10-20-cyclic-recoupling/README.md).

The question is whether preserving the diagonal SL2 action can reduce a
general matrix degeneration search to a small coefficient system. The
answer is negative for the cases below. This does not say that a general
degeneration can be replaced by an equivariant one.

## 1. The construction class

Write V_d=Sym^d(C^2), D=a-1 and H=4D. Under the diagonal SL2 subgroup
of the three convolution factors, each source leg is

    S = V_D tensor V_D tensor V_(2D).

The Clebsch-Gordan rule gives multiplicities 1,2,...,a,...,2,1 at
degrees 0,2,...,4D. In particular V_0 and V_H occur once each.

For the first result, the target is M_n with n=2a-1, and its vertex
space carries V_(2D). Each target leg V_(2D) tensor V_(2D) has one copy
of every even-degree representation from 0 through H. Allow arbitrary,
independent SL2-intertwining maps on the three tensor legs. Their entries
may depend on a degeneration parameter. Equivalently, consider the
closure of tensors obtained by such intertwining maps.

**Theorem.** A_a cannot degenerate to this M_(2a-1) by these maps,
for any a>=2. The maps may vary within every multiplicity space, and
need not be cyclically identical.

## 2. Five coefficients prove the theorem

Use monomials e_i=x^(d-i)y^i on V_d, and the same CG normalization as
`cg_blocks.equivariant_basis`. Projection to V_H is ordinary polynomial
multiplication. Projection to V_0 first multiplies the two short factors
and then applies the invariant pairing. On e_i tensor e_s tensor e_k it is

    L0(i,s,k) = (-1)^(i+s) / ((2D+1) binom(2D,i+s))

when i+s+k=2D, and zero otherwise. The pairing is normalized to send
the invariant vector sum_l (-1)^l binom(2D,l) e_l tensor e_(2D-l) to 1.
Multiplication annihilates all lower short-factor summands, so this is
the unique singlet projection with the chosen normalization.

Put n=2D+1 and B=binom(2D,D). Define the positive rational number

    Q_D = sum [ product_(v in {i,j,p,q,r,s}) binom(D,v) ]
                / [binom(2D,i+s) binom(2D,j+p) binom(2D,q+r)],

where 0<=i,j,p,s<=D, q=i+s-p, r=j+p-s, and only terms with
0<=q,r<=D are included. The all-zero tuple contributes 1, so Q_D>=1.

Select five coefficient positions after projection. The first column
gives their representation degrees and the second their monomial indices:

| Degrees | Indices | A_a coefficient | M_n coefficient |
| --- | --- | --- | --- |
| (0,0,0) | (0,0,0) | Q_D/n^3 | 1/n^2 |
| (0,H,H) | (0,0,H) | 1/(n B) | 1/n |
| (H,0,H) | (0,0,H) | 1/(n B) | 1/n |
| (H,H,0) | (0,H,0) | 1/(n B) | 1/n |
| (H,H,H) | (0,2D,H) | (-1)^D | 1 |

Here is a direct coefficient calculation, independent of a numerical
fit. The invariant source has terms at

    (i,s,2D-p-q), (j,p,2D-r-s), (q,r,2D-i-j)

with coefficient (-1)^(i+j+p+q+r+s) times the six short binomial
coefficients. Applying three singlet projections forces the two
independent equations defining q,r in Q_D. All signs cancel, giving
Q_D/n^3. For (0,H,H), the selected top-leg indices force
(i,j,p,q,r,s)=(0,0,0,D,D,D); the resulting coefficient is 1/(nB).
The other two positions give the same value. For (H,H,H), they force
(i,j,p,q,r,s)=(0,0,D,D,D,0), with coefficient (-1)^D.

The invariant target is obtained from the ordinary matrix tensor by
reversing and scaling the second coordinate on every leg. Its terms are

    (i,2D-j), (j,2D-k), (k,2D-i)

with coefficient (-1)^(i+j+k) binom(2D,i) binom(2D,j) binom(2D,k).
Three singlet projections force i=j=k and give n terms of size n^-3.
The other four selected coefficients each have one contributing tuple,
giving the displayed target column. These changes of basis are invertible.

Divide each selected output coefficient by its nonzero source
coefficient, and call the results b000,b0HH,bH0H,bHH0,bHHH. Since the
source representations V0 and VH occur just once, every equivariant
image satisfies the polynomial identity

    b0HH bH0H bHH0 - b000 bHHH^2 = 0.                 (1)

Indeed, if the six map scalars are x0,xH,y0,yH,z0,zH, both products
are x0*y0*z0*(xH*yH*zH)^2. This polynomial vanishes on the closure
as well, even when the scalars have poles in the degeneration parameter.

For the target the left side is

    B^3 - n/Q_D > 0.

To see strictness, Q_D>=1 and B>=2D, whereas (2D)^3>2D+1=n for
D>=1. Thus (1) fails, proving the theorem. For a=2,3,4 its exact
values are 36/5, 4950/23 and 4135600/517. A Gröbner-basis discovery
calculation first found inconsistency in the larger 15-equation a=2
system; the proof above needs only these five coefficients and no
Gröbner-basis assertion.

## 3. Allow reducible vertex representations

More generally choose three nonzero SL2 vertex representations U,V,W
of dimensions l,h,n. The matrix legs carry U tensor V*, V tensor W*,
and W tensor U*. Keep the source action in Section 1 and require all
three maps to intertwine it with these chosen target actions.

A concise limiting matrix tensor requires a surjective leg map at
generic parameter values: some full flattening minor is nonzero in
the limit and therefore is not identically zero. Complete reducibility
then requires every target-leg irreducible multiplicity to be at most
its source multiplicity. This is a necessary test, not a construction.

The center -I acts trivially on S. Thus U,V,W must each have a pure
central parity, and that parity must be the same for all three. For
example, if one vertex dimension is odd, all vertex summands must have
even highest weight, hence odd dimension. Mixtures of parities cannot
occur: their pairwise tensor products would contain a negative central
eigenspace, absent in the source.

`verify.py` enumerates the unordered partitions of each vertex dimension
into irreducible dimensions with this common parity. For each pair it
uses V_(i-1) tensor V_(j-1)=V_(i+j-2)+...+V_(abs(i-j)).

| Source and target | Representation triples checked | Surviving triples |
| --- | ---: | ---: |
| A2 to M(3,3,3) | 8 | 1 |
| A4 to M(10,10,11) | 1200 | 0 |
| A5 to M(13,13,17) | 12312 | 0 |

For A2 the sole survivor is U=V=W=V2. Section 2 excludes it. Thus
no choice of matrix-vertex SL2 representations of dimension three
rescues this equivariant A2 to M3 ansatz. For H1100 at a=4 the
multiplicity test alone excludes the ansatz. It likewise excludes the
listed a=5 target, already excluded for constant general maps by
AI-CYCLIC-MINIMUM-RANK-LOCUS-043.

These results concern this diagonal action and matrix-vertex target
actions. They do not forbid symmetry-breaking maps, different subgroup
choices, or arbitrary degenerations. No theorem is used or asserted
that would replace a general degeneration by an equivariant one.

## 4. Reproduction and status

```sh
python research/ai/2026-10-20-cyclic-equivariant/verify.py
python -m unittest discover -s tests -p test_cyclic_equivariant.py -v
```

The saved report checks the formulas exactly for a=2,...,12. At a=2,3,4
it separately compares all five source coefficients against the retained
full recoupling tensor, and builds and inverts a target CG basis to check
all five target coefficients. The representation enumeration records
the first violating leg and multiplicity, with exhaustive counts. The
natural A_a to M_a vertex representations pass as positive controls for
a=2,...,8. These finite checks support, but do not replace, Section 2's
all-size argument. The CG rule and invariant binary-form pairings are
standard; no historical priority or independent review is claimed.

The follow-up [Cartan character frontier](torus.md) relaxes SL2 equivariance
to the diagonal torus and leaves one necessary H1100 character triple. Its
completed numerical pilots do not construct the degeneration.
