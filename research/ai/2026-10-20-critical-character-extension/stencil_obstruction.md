# The fifth-difference blocks are incomparable at every finite scale

October 21, 2026. AI-derived proof and exact calculations, unreviewed.
This is an obstruction to one proposed construction. It does not improve
the matrix multiplication exponent or disprove a universal inequality for
limiting character profiles.

## 1. The literal matched-block comparison

The [endpoint note](README.md), Section 5, gives a strictly negative fifth
forward difference for the hypothetical critical powered profile at
\(s=4/5\), with step \(h=1/20\). Its positive and negative coefficients
suggest comparing two matched sums of convolution tensors.

Fix any integer \(n\ge1\), and put \(a=20n\). Let \(C(a,b)\) denote
polynomial convolution with the first input of dimension \(a\), the second
input of dimension \(b\), and output dimension \(a+b-1\). Define

\[
T_+(n)=5C(a,17n)\boxplus10C(a,19n)\boxplus C(a,21n),
\]

\[
T_-(n)=C(a,16n)\boxplus10C(a,18n)\boxplus5C(a,20n).
\tag{1}
\]

Here \(\boxplus\) means that all first inputs are identified with one
common \(a\)-dimensional space, while the second inputs and outputs are
disjoint across blocks. Repeated blocks have independent second-input
and output spaces. Each first-input identification can use an arbitrary
invertible map, independently for every block on either side.

Each side has 16 blocks. The three dimensions on both sides are exactly

\[
\left(20n,\ 296n,\ 616n-16\right).
\tag{2}
\]

**Proposition.** Neither \(T_+(n)\) degenerates to \(T_-(n)\), nor
\(T_-(n)\) degenerates to \(T_+(n)\), for any \(n\ge1\) and any of the
independent first-input identifications just described. The degenerations
in this statement allow arbitrary changes of basis on all three legs,
not only blockwise or diagonal substitutions.

## 2. Exact Koszul witnesses

We use the shared-input Koszul formula established in the earlier local
[Koszul note](../2026-10-20-koszul/research_note.md), Section 3:

\[
R_p(a,b):=\operatorname{rank}K_p(C(a,b))
=b\binom ap-\binom{a-1}{p-1}(b-a+p)_+,
\qquad 0\le p<a.
\tag{3}
\]

The binomial coefficient with lower index \(-1\) is zero. That note gives
a proof from the kernel bundle
\(\mathcal O(b-a+p-1)^{\binom{a-1}{p-1}}\) on \(\mathbb P^1\).
We import this formula, rather than assume that a shared-input Koszul map
always has maximal rank.

Koszul rank is invariant under invertible substitutions and cannot
increase under degeneration. It adds over matched blocks: the Koszul map
is a direct sum on the two nonshared factors. Its rank is unchanged by
each block's independent invertible first-input identification. These
facts apply to the entire tensors in (1), without preserving their block
structure during a putative degeneration.

Let \(D_p=\operatorname{rank}K_p(T_+)-\operatorname{rank}K_p(T_-)\).
Formula (3) and the fifth-difference coefficients give

\[
D_p=
\sum_{k=0}^{5}(-1)^{5-k}\binom5kR_p(a,(16+k)n)
=-\binom{20n-1}{p-1}\Phi_n(p),
\tag{4}
\]

where

\[
\Phi_n(p)=\sum_{k=0}^{5}(-1)^{5-k}\binom5k
\bigl(p+(k-4)n\bigr)_+.
\tag{5}
\]

The affine term in (3) cancels because a fifth forward difference
annihilates linear functions. Two exterior degrees suffice:

\[
\Phi_n(n)=-5n+2n=-3n,
\qquad
\Phi_n(2n)=10n-10n+3n=3n.
\]

Thus

\[
\boxed{D_n=3n\binom{20n-1}{n-1}>0,\qquad
D_{2n}=-3n\binom{20n-1}{2n-1}<0.}
\tag{6}
\]

At \(p=2n\), the source \(T_+\) has smaller rank than the proposed
target \(T_-\), which excludes the first direction. At \(p=n\), the
source \(T_-\) has smaller rank than \(T_+\), which excludes the reverse.
Both degrees lie in the allowed range \(0\le p<20n\), proving the
proposition for every positive integer scale.

For completeness, all exterior degrees can be read from the piecewise
linear formula

\[
\Phi_n(p)=
\begin{cases}
n-4p,&0\le p\le n,\\
6p-9n,&n\le p\le2n,\\
11n-4p,&2n\le p\le3n,\\
p-4n,&3n\le p\le4n,\\
0,&p\ge4n.
\end{cases}
\tag{7}
\]

The rank difference at \(p=0\) is zero because the binomial prefactor
in (4) is zero. All expressions agree at the shared endpoints.

## 3. Consequence and limits

This rules out obtaining the fifth-difference relation from a literal
finite degeneration between these two matched sums. Increasing the scale
does not remove the obstruction, and allowing arbitrary first-input bases
does not remove it either.

The proposition does **not** disprove the desired profile inequality
\(\Delta_h^5Q(s)\ge0\). A character on a matched sum is generally known
only to dominate a power sum of its block values. Equality with that
power sum has not been established for arbitrary characters. Thus a
relation between the block values and a relation between the matched
tensors are distinct assertions in the first place.

The proposition concerns degeneration at each finite scale. Section 4
also excludes full independent replication and a shared-input dot-product
auxiliary tensor. These results do not exclude asymptotic restrictions
of tensor powers, comparison after adding other tensors, multiplication
by other auxiliary tensors, or a different tensor construction proving
the profile inequality.

## 4. Independent replication does not remove the obstruction

There is a stronger finite consequence. For every positive integer q,
neither q full independent copies of T_+(n) degenerate to q full
independent copies of T_-(n), nor conversely. This q-copy operation
identifies no input spaces across the copies.

Define the shared-input Koszul rank polynomial and its difference by

\[
\mathcal K_T(t)=\sum_{p=0}^{20n-1}\operatorname{rank}K_p(T)t^p,
\qquad D_n(t)=\mathcal K_{T_+}(t)-\mathcal K_{T_-}(t).
\]

We first prove the two signs

\[
\boxed{D_n(1/19)>0,\qquad D_n(1/9)<0\quad(n\ge1).}
\tag{8}
\]

By (4), if P=1+Binomial(20n-1,t/(1+t)), then

\[
D_n(t)=-t(1+t)^{20n-1}\,\mathbb E\Phi_n(P).
\tag{9}
\]

Including P=20n in this expression causes no problem, since
\(\Phi_n(p)=0\) for \(p\ge4n\). Formula (7) shows that Phi_n is
6-Lipschitz on the nonnegative real line. At t=1/19, its value at n and
the second moment of P-n give

\[
\mathbb E\Phi_n(P)
\le-3n+6\sqrt{\frac{19n}{20}+\frac{171}{200}}<0
\qquad(n\ge5).
\tag{10}
\]

At t=1/9, center instead at 2n to obtain

\[
\mathbb E\Phi_n(P)
\ge3n-6\sqrt{\frac{9n}{5}+\frac{18}{25}}>0
\qquad(n\ge8).
\tag{11}
\]

Both bounds use \(\mathbb E|P-c|\le\sqrt{\mathbb E(P-c)^2}\).
The displayed strict inequalities follow by squaring their positive
sides; the resulting quadratic inequalities are increasing from n=5
and n=8 respectively. Together they prove (8) for n>=8.

Here are integer certificates for the remaining seven scales. Put
\(S_d(n)=d^{4n-1}D_n(1/d)\); since the degree of D_n is at most 4n-1,
these are integers computable directly from (4).

| n | S_19(n) | S_9(n) |
|---:|---:|---:|
| 1 | 171 | -99 |
| 2 | 263148689 | -24792051 |
| 3 | 245470502231930 | -3038048120670 |
| 4 | 162696452587579494790 | -283929472530121710 |
| 5 | 90326924459049957577553040 | -22965165863895412216160 |
| 6 | 45244265658998166692802035517275 | -1700055817867419873663046725 |
| 7 | 21223899599229850460334061619210389340 | -118625644051316468742842160169860 |

This proves (8) at every positive integer scale.

Now take q full independent copies of a tensor T with shared-leg
dimension a. In the ambient direct sum of the q shared spaces, each
copy has a complementary zero space of dimension (q-1)a. Decomposing
exterior powers by degree in that zero space gives

\[
\mathcal K_{q\odot T}(t)=q(1+t)^{(q-1)a}\mathcal K_T(t).
\tag{12}
\]

This is the same exterior-padding formula as Section 4 of the cited
Koszul note. The difference for q copies of T_+ and T_- is therefore
\(q(1+t)^{(q-1)20n}D_n(t)\). It still has both signs in (8).
If either finite degeneration existed, all its coefficient rank
differences would have the same weak sign. Evaluation at positive t
would preserve that sign, a contradiction. This proves the stated
incomparability after any full independent replication.

Multiplication by a dot-product tensor on the two nonshared legs,
\(B_X(r)\), merely repeats every matched block r times without changing
the shared dimension. It multiplies each Koszul rank by r. Consequently
the same conclusion holds after simultaneous multiplication by
\(\langle q\rangle\otimes B_X(r)\) for any q,r>=1. This does not treat
arbitrary auxiliary tensors.

## 5. Reproducible controls

`stencil_obstruction.py` computes every shared-input Koszul rank on both
sides for all \(1\le n\le32\), checks the dimensions, verifies (4) and
the full piecewise formula (7), and separately checks the two closed-form
witnesses (6). It also recomputes the fourteen integer certificates for
(8) and checks the moment bounds. It uses integer arithmetic and no
matrix-rank tolerances. The exterior-padding identity is proved in the
cited note and in (12), rather than inferred from finite checks.
The finite checks verify the formulas' specialization and implementation;
the all-scale assertion follows from the proof above and the imported
Koszul formula.

```sh
python research/ai/2026-10-20-critical-character-extension/stencil_obstruction.py
```
