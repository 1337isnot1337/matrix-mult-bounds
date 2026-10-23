# Every SL(2,F8) subgroup ideal and the remaining full-coset cuts

October23,2026. Claim `AI-SL2-F8-SUBGROUP-CUTS-001` is written and
unreviewed, with an exact exhaustive finite certificate. No target tensor
construction or matrix multiplication exponent improvement is claimed.

## Statement and source

Use the maintained 504-element SL(2,F8) model over
F2[t]/(t^3+t+1), with its literal multiplication table and identity0.
All group and predecessor source pins are in `sources.json`. Over C set

    e_H=(1/|H|) sum_(h in H) h,     I_H=C[G] e_H C[G].

The complete subgroup lattice has386 members and12 conjugacy classes.
Its averaging ideals have the following exact complex dimensions.

| Subgroup order | Number of subgroups | dim I_H |
| ---: | ---: | ---: |
| 1 | 1 | 504 |
| 2 | 63 | 504 |
| 3 | 28 | 504 |
| 4 | 63 | 504 |
| 6 | 84 | 455 |
| 7 | 36 | 504 |
| 8 | 9 | 308 |
| 9 | 28 | 440 |
| 14 | 36 | 308 |
| 18 | 28 | 244 |
| 56 | 9 | 65 |
| 504 | 1 | 1 |

For each of the sixteen saved SL(2,F8) coordinate/potential target formats,
the certificate supplies every inclusion-minimal forbidden complete coset
arising from this subgroup-averaging dimension test. Beyond the previous
orders8,9,18, only orders6 and14 add minimal classes. Each order14 class
has1296 distinct left cosets of its conjugate subgroups and is forbidden
on all48 target legs. Each order6 class has7056 such cosets and is forbidden
on ten of those48 legs, precisely where the product of the other target
dimensions is strictly greater than455.

For the selected M(18,18,25), the minimal class orders are

    first leg:  8,9,14;      second leg: 8,9,14;
    third leg:  8,14,18.

The respective numbers of distinct minimal forbidden cosets are
3431,3431,2647. This does not say that every coordinate candidate is
excluded. It exhausts this one necessary-condition method for these
sixteen formats in this one source.

## Exhaustive subgroup certificate

Discovery starts at the trivial subgroup. For every found subgroup H,
it generates <H,g> for each coset representative g, and continues until
no subgroup is added. It uses the earlier central-cover catalog algorithm
with its existing credit. The group is finite, so positive words in the
generators also produce their inverses.

Acceptance independently closes the saved generators by left rather than
right multiplication and checks that each saved subgroup is exactly that
closure. It then checks every possible extension <H,g>. Only one right
H-coset representative is needed, since <H,gh>=<H,g> for h in H.
Every such extension must occur in the list.

This proves completeness: any subgroup K has a finite generating list.
Starting at {1}, append those generators one at a time. Extension closure
forces each resulting subgroup, including K, into the verified list.
Thus the list is exhaustive, rather than an order histogram or a sample.
Acceptance also recomputes all conjugates and checks that the twelve
saved classes partition the subgroup list without overlap.

## Exact ideal dimensions without a character-table assumption

The ideal I_H is the span of the integer indicator vectors of all left
cosets of all conjugates of H. Indeed,

    g e_H h = gh e_(h^-1 H h),

and every left coset of a conjugate has that form, up to the fixed nonzero
normalization1/|H|. The verifier constructs those sets from the group table.

For each class, discovery proposes a rational central element z. Acceptance
checks z^2=z in the actual integer class-product algebra and checks
z sum_H h=sum_H h at every one of the504 group coefficients. Centrality
and this containment give I_H contained in z C[G]. Since multiplication
by z is idempotent over C, its rank is its trace, namely504 z_1. This is
the certified upper dimension D.

A matching lower witness selects D actual integer coset rows and D group
coordinates. The verifier performs Gaussian elimination on that square
minor modulo the prime1009 and checks that every selected row is
independent. Its integer determinant is nonzero, hence its complex rank
is D. Those rows belong to I_H, proving the lower bound and equality.
No modular rank upper bound or unverified character-table entry is used.
The rational central blocks are discovery data only.

For example, the order14 normalizer of a split order7 torus has projection
coefficients, in the maintained nine-class order,

    (44,4,-1,-1,0,-1,0,-1,0)/72.

The integer idempotent/containment identities give upper dimension
504*44/72=308, and its saved308-by308 coset minor proves equality.
The order6 class similarly has exact dimension455.

## Target cuts and their completeness

The imported, pinned subgroup-averaging proof states that if a vertex
family of an injective-pair-map, strict-vertex-potential construction
contains a complete left coset of H, the product of the two other family
sizes is at most dim I_H. It averages the feasible potentials over H and
restricts the middle target index to its trivial H-component; positivity
and the complete-coset hypothesis are essential. This is an existing
written, unreviewed lemma, whose attribution is preserved. It applies
cyclically to all three legs and to every conjugate subgroup.

For each saved format (a,b,c), the present verifier applies that lemma
with the exact D_H above and the strict comparisons D_H<bc, D_H<ca,
D_H<ab. A coset with more points than the relevant vertex family cannot
occur and is ignored.

A forbidden H-coset is redundant precisely when H contains a proper
conjugate of a forbidden subgroup K. If bK lies inside aH, then
(a^-1 b)K lies in H; its representative a^-1 b belongs to H, so K is
contained in H. Conversely K contained in H gives aK contained in aH.
Thus containment can be checked on the exhaustive subgroup classes,
without comparing all pairs of large coset lists.

Acceptance checks minimality and coverage separately. Each reported
class must be eligible and contain no smaller eligible subgroup. Every
omitted eligible class must contain a reported smaller one. Together with
the exact ideal dimensions for every subgroup, this proves completeness
for the stated averaging test. It does not claim that this test captures
all coordinate obstructions or arbitrary complex maps.

The prior order8,9,18 cuts supply567,1568,784 cosets respectively. The
new order14 cuts add1296 on every target leg. On ten legs, order6 adds7056
more. The two new classes contain no previously forbidden proper subgroup
for those comparisons. All other relevant subgroup classes are either
not forbidden or contain one of the reported minimal classes. The
orders56 and504 exceed every saved target vertex size.

## A filter control and verification limits

The certificate includes an18-element vertex set formed from one
order14 subgroup and four outside elements. It contains no coset of
any of the old order8,9,18 subgroup classes, as independently checked by
the verifier. It does contain the order14 subgroup. Thus it passes the
previous vertex-set filters for the first leg of M(18,18,25), and the new
filter rejects it. This is only a vertex-set control, not a complete
pair-injective target or a tensor degeneration.

The certificate is exhaustive finite evidence, and the general subgroup,
rank and averaging implications above are written arguments. There is
no independent mathematical review or Lean formalization. Surviving
coordinate constructions, arbitrary complex input mixing, different
sources or powers and the exponent below9/4 remain open.
