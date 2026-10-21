# A full-coset obstruction in every odd-prime Heisenberg group

AI-derived written proof, unreviewed. No historical novelty, independent
review, formalization or exponent improvement is asserted. The argument
concerns coordinate group constructions with strict vertex potentials.

**Proposition.** Let p be an odd prime and H_p the three-dimensional
Heisenberg group of order p^3. Suppose S_i is a nonempty union of left
cosets of one fixed noncentral cyclic subgroup L_i of order p, for each
i=1,2,3. If the three cyclic pair maps are injective and all extra terms
have strictly positive vertex weight, then

    |S_1| |S_2| |S_3| <= p^4.                              (1)

In particular no construction in this class passes the usual source
degree-sum comparison at any exponent between 2 and 9/4.

## 1. Stabilizer averaging

This step holds in every finite group. Independent right translations of
the selected vertex sets preserve the cyclic support equations: the three
group labels change to h1^-1 X h2, h2^-1 Y h3, h3^-1 Z h1, so their
product is conjugated. Potentials move with their vertices.

If S_i is a union of left L_i cosets, right multiplication by L_i permutes
S_i. Average a strictly feasible potential vector over the three finite
right actions. Every strict inequality remains strict. The resulting
potentials are constant on each chosen left coset.

Now fix one coset in each set. Any nontrivial extra relation using endpoint
pairs within these three cosets has weight zero. It follows that the three
conjugate subgroups g_i L_i g_i^-1 satisfy the ordinary triple product
property (TPP), for every independent choice of the three cosets.

## 2. Three nonparallel cyclic subgroups

Use the coordinates (v,h), where v=(a,b) and h=c-a*b/2. Multiplication is

    (v,h)(w,k)=(v+w,h+k+omega(v,w)/2),

where omega((a,b),(x,y))=a*y-b*x. Every noncentral cyclic subgroup is
{(t*v_i,t*h_i):t in F_p}, with v_i nonzero.

Assume its three projected directions are pairwise distinct. There is a
unique relation sum a_i*v_i=0 up to scale, and every a_i is nonzero.
All projected solutions to a product of the three subgroup elements being
identity have parameters t_i=lambda*a_i. The remaining central equation is

    lambda*B+lambda^2*A=0,
    B=sum a_i*h_i,
    A=omega(a_1*v_1,a_2*v_2)/2 != 0.                       (2)

For clarity, the quadratic coefficient follows by substituting
w_3=-w_1-w_2 in sum_(i<j) omega(w_i,w_j)/2; the sum is
omega(w_1,w_2)/2. Thus (2) has no nonzero solution exactly when B=0.
The three subgroups satisfy the TPP if and only if B=0.

Conjugation by (w,k) replaces h_i by h_i+omega(w,v_i). By Section 1,
B=0 must hold for every independent coset choice. Since a_i!=0, the
conjugate subgroup g_i L_i g_i^-1 is therefore constant as its coset varies.

Translate each S_i independently so that it contains identity. It remains
a union of left cosets, with L_i possibly conjugated. The identity coset
is L_i itself, so all selected representatives normalize L_i. Consequently
S_i lies in N(L_i), an abelian subgroup of order p^2 and index p.

## 3. Sizes and the parallel-direction case

Write |S_i|=p*k_i. If any k_i=1, injectivity of the pair map on the other
two sets already gives (1): multiply its |S_j||S_k|<=p^3 by |S_i|=p.

Suppose all k_i>=2. If two projected subgroup directions coincide, their
common abelian normalizer H has order p^2. Each corresponding set contains
a whole p-point left coset in a right H coset; normality of H justifies
this statement regardless of the chosen representatives. The third set
has at least ceil(p*k_i/p)=k_i>=2 points in some right H coset. The
maintained abelian-coset bound would require p*p*2<=p^2, a contradiction.
Thus the three directions must be pairwise distinct.

Section 2 now puts S_i inside its abelian normalizer H_i. Apply the same
abelian-coset bound to H_1. The first maximum fiber has size p*k_1;
the others have sizes at least k_2,k_3. Hence

    p*k_1*k_2*k_3 <= p^2,

which proves |S_1||S_2||S_3|=p^3*k_1*k_2*k_3<=p^4.

## 4. Consequence and precise scope

The explicit source degrees give sum d_i^2=p^3. For 2<=tau<=9/4,

    sum d_i^tau >= p^3 >= p^(4*tau/3)
                   >= (|S_1||S_2||S_3|)^(tau/3).

The required strict degree-sum gate cannot hold. In particular the tested
two-coset M10 family at p=5 and three-coset M33 progression at p=11 cannot
produce the desired exponent by this route. Arbitrary subsets, arbitrary
central colorings over the same projected lines, and noncoordinate tensor
degenerations are outside the proposition.

The abelian-coset bound is the existing maintained group-worker theorem,
not a new result of this note. The finite subgroup TPP problem has related
prior literature: [Murthy, arXiv:2602.15796v1, February 17, 2026](https://arxiv.org/html/2602.15796v1)
studies ordinary TPP for triples of subgroups in nilpotency class two.
That paper's subgroup scope does not itself exclude the weighted subset
constructions considered here. The present proof is an unreviewed
stabilizer-averaging application, without a priority claim.
