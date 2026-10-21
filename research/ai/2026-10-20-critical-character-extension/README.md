# Oriented endpoint rigidity and quantitative spectral stability

October 21, 2026. AI-derived research by Codex at the owner's request.
Written arguments, not independently reviewed or formally verified.
**No exponent below 9/4 is proved in this note.**

## Scope

The existing local rigidity theorem determines the geometric mean of six
oriented convolution profiles at a hypothetical character attaining 9/4.
This note determines all six profiles separately, proves quantitative
stability estimates for near-extremal dot-product parameters and offsets,
and isolates an exact higher-difference obstruction to the endpoint shape.
The higher-difference inequality that would turn that obstruction into a
matrix multiplication improvement remains an open tensor premise.

All tensor-theoretic inputs in Sections 1--4 below are from Przemyslaw
Uznanski, [*Rectangular matrix multiplication from polynomial products*,
arXiv:2610.10494v2](https://arxiv.org/html/2610.10494v2), Lemmas 4.1 and 5.1,
Proposition 5.2 and Appendix G. The analytic deductions below do not add a
tensor degeneration. The previous local result is
[the symmetrized homogeneous rigidity note](../2026-10-20-concavity-equivalence/homogeneous_rigidity.md).

## 1. Notation and cited inputs

Fix a tensor character lambda. Write its dot-product parameters as

$$p_i=\log_2\lambda(B_i(2))\in[0,1],\qquad
S=p_1+p_2+p_3,\qquad \delta=\frac94-S.$$

For distinct input legs i,j and the remaining output leg k, put

$$g_{ij}(x,y)=\lim_{N\to\infty}
\frac{\lambda(C_{ij}(\lceil Nx\rceil,\lceil Ny\rceil))}{N}.$$

Uznanski's Lemma 4.1 proves existence, positivity, continuity, homogeneity
of degree one, and the input interchange relation

$$g_{ij}(x,y)=g_{ji}(y,x).$$

When p_i is positive, define

$$Q_{ij}(s)=g_{ij}(1,s)^{1/p_i}.$$

Lemma 5.1 provides a common asymptotic slope L_i>0 for Q_ij and Q_ik and
offsets c_ij,c_ik such that

$$c_{ij},c_{ik}\ge0,\qquad c_{ij}+c_{ik}\le1,$$

$$Q_{ij}(s+h)\ge Q_{ij}(s)+L_i h,\qquad
L_i s\le Q_{ij}(s)\le L_i(s+c_{ij})\quad(s,h>0). \tag{1}$$

Each Q_ij is concave. The pairwise consequence proved in Appendix G is

$$\sqrt{c_{ij}c_{ji}}\ge r_{ij},\qquad
r_{ij}=\left(\sqrt{p_ip_j}-\sqrt{(1-p_i)(1-p_j)}\right)_+. \tag{2}$$

The angular constraint, valid also when a parameter vanishes, is

$$\theta_i=\arccos\sqrt{p_i},\qquad
\theta_1+\theta_2+\theta_3\ge\frac\pi2. \tag{3}$$

The square objective is S. Thus an actual uniform improvement is a proof
that S is at most 9/4 minus a fixed positive number for every character.

## 2. An exact decomposition of the endpoint deficit

This section assumes all p_i>0 so that the six offsets above are available.
Define

$$\sigma=3-\sum_{i\ne j}c_{ij},\qquad
E=\sum_{i<j}(\sqrt{c_{ij}}-\sqrt{c_{ji}})^2.$$

The following identity has only nonnegative terms on the right:

$$\boxed{
4\delta=\sigma+E
+2\sum_{i<j}\left(\sqrt{c_{ij}c_{ji}}-r_{ij}\right)
+2\sum_{i<j}\left(r_{ij}-(p_i+p_j-1)\right).
} \tag{4}$$

To check the identity, use

$$\sigma+E=3-2\sum_{i<j}\sqrt{c_{ij}c_{ji}},\qquad
\sum_{i<j}(p_i+p_j-1)=2S-3.$$

Nonnegativity of sigma follows by summing the three row constraints.
Nonnegativity of the third term is (2). To check the final term, first
consider p_i+p_j<=1, where it is immediate. Otherwise theta_i+theta_j<pi/2
and

$$p_i+p_j-1
=\cos(\theta_i+\theta_j)\cos(\theta_i-\theta_j)
\le\cos(\theta_i+\theta_j)=r_{ij}.$$

In particular,

$$\boxed{\sigma+E\le4\delta.} \tag{5}$$

This proves the square bound S<=9/4 directly from the offset inequalities.
It also says that a near-extremal character must nearly saturate every row
constraint and must have nearly reciprocal opposite offsets. A constant
number of finite errors cannot be hidden in a near-extremal solution.

### Equality

If delta=0, then S=9/4 and each pair has p_i+p_j>=5/4>1. The last summands
in (4) vanish only if cos(theta_i-theta_j)=1. Thus all p_i agree and equal
3/4. Next sigma=E=0 says the offset matrix is symmetric with every row sum
one. On three vertices this uniquely forces

$$\boxed{p_1=p_2=p_3=\frac34,\qquad c_{ij}=\frac12\quad(i\ne j).} \tag{6}$$

There is no differentiability assumption in this argument.

## 3. Two parameter localization bounds

These estimates use only (3) and are valid on the whole closed angular
region, including zero parameters.

### 3.1 A sharp one-coordinate bound

For each i,

$$\boxed{\left(\sqrt{1-p_i}-\frac12\right)^2\le\delta.} \tag{7}$$

Fix theta_i and put alpha=pi/2-theta_i. Since theta_j+theta_k>=alpha,
monotonicity of cosine squared lets us decrease their sum to alpha when
maximizing p_j+p_k. At that sum,

$$\cos^2u+\cos^2(\alpha-u)
=1+\cos\alpha\cos(2u-\alpha)
\le1+\cos\alpha=1+\sin\theta_i.$$

Consequently

$$S\le p_i+1+\sqrt{1-p_i}
=\frac94-\left(\sqrt{1-p_i}-\frac12\right)^2.$$

Equality is attained on the angular boundary when the other two angles
are equal, so (7) is sharp as a bound depending only on p_i.

For 0<=delta<=1/4, squaring the nonnegative endpoints gives the useful box

$$\boxed{\frac34-\delta-\sqrt\delta
\le p_i\le
\frac34-\delta+\sqrt\delta.} \tag{8}$$

For example, a putative character with S>=2.249 has every parameter in
the rational interval [717/1000,781/1000]. A character with S>=2.2499 has
every parameter in [7399/10000,7599/10000]. These are search regions, not
certificates excluding any character.

### 3.2 A sharp global squared-distance bound

Every point of the angular region satisfies

$$\boxed{\sum_{i=1}^3\left(p_i-\frac34\right)^2
\le\frac{11}{4}\left(\frac94-S\right).} \tag{9}$$

The constant 11/4 is optimal globally: equality holds at each of the three
flattening vertices (0,1,1) and at (3/4,3/4,3/4). These are all equality
cases.

**Proof.** Rearranging (9), it is equivalent to

$$\sum_i\left(p_i^2+\frac54p_i\right)\le\frac92. \tag{10}$$

The left side is strictly increasing in every p_i. Its maximum on (3)
therefore lies on the boundary sum(theta_i)=pi/2. Set q_i=sin^2(theta_i)
and r=sqrt(q_1q_2q_3). The elementary complementary-angle identity gives

$$q_1+q_2+q_3+2r=1.$$

Writing e_2=q_1q_2+q_2q_3+q_3q_1, the left side of (10) becomes

$$\frac92+\frac52r+4r^2-2e_2.$$

It remains to prove

$$J=e_2-\frac54r-2r^2\ge0 \tag{11}$$

on the larger compact set q_i>=0, sum(q_i)+2sqrt(q_1q_2q_3)=1.
On its boundary r=0 and J=e_2>=0. At an interior minimum, write
G=sum(q_i)+2r. Since every partial derivative of G is positive, Lagrange
multipliers apply. Let s_1=sum(q_i) and A=5/4+4r. Multiplying
partial_i J=mu partial_i G by q_i gives

$$q_i(s_1-q_i)-\frac A2r=\mu(q_i+r).$$

Thus all three q_i are roots of the same quadratic

$$q_i^2-(s_1-\mu)q_i+(A/2+\mu)r=0.$$

At least two q_i are equal. Put q_1=q_2=u and q_3=z^2. The constraint
factors as (z+1)(z+2u-1)=0, hence z=1-2u and 0<=u<=1/2. Direct expansion
then gives

$$\boxed{J=\frac u4(4u-1)^2(3-2u)\ge0.} \tag{12}$$

Every minimum is nonnegative, proving (11). Equality in the interior
requires u=1/4, hence all q_i=1/4. On the boundary equality requires two
q_i to vanish and the third to equal one. Strict monotonicity used in
reducing to the angular boundary excludes additional equality cases.

## 4. Rigidity of each oriented limiting profile

Suppose an actual character attains S=9/4. Then all six oriented profiles
have one common positive amplitude K and satisfy

$$\boxed{
g_{ij}(x,y)^{4/3}
=K\min(x,y)^{1/3}
\left(\max(x,y)+\frac{\min(x,y)}2\right)
\quad(i\ne j).
} \tag{13}$$

This determines each orientation separately; it does not merely determine
their geometric mean. It does not prove that a character satisfying (13)
exists, and it does not determine the finite-size profile.

**Proof.** By (6), set d=4/3 and Q_ij(s)=g_ij(1,s)^d. For a pair i,j,
input interchange and homogeneity give

$$Q_{ji}(s)=s^dQ_{ij}(1/s). \tag{14}$$

In particular v=Q_ij(1)=Q_ji(1)>0. Finite concavity supplies finite
one-sided derivatives at one. Write

$$a=Q'_{ij,+}(1),\qquad b=Q'_{ji,-}(1).$$

Expanding (14) as s tends to one from below proves

$$a+b=dv.$$

The increment lower bounds (1) give a>=L_i and b>=L_j. The affine upper
bounds with offsets 1/2 give v<=(3/2)min(L_i,L_j). Therefore

$$L_i+L_j\le dv\le2\min(L_i,L_j)\le L_i+L_j.$$

Every inequality is an equality. Thus L_i=L_j=L, v=3L/2, and a=L.
Concavity bounds Q_ij above by its right tangent for s>=1; the increment
bound bounds it below by the same line. Consequently

$$Q_{ij}(s)=L(s+1/2)\quad(s\ge1).$$

Repeating this for every ordered pair proves that all three slopes agree.
Equation (14) gives Q_ij(s)=L s^(1/3)(1+s/2) for 0<s<=1. Homogeneity
finishes the proof with K=L.

## 5. A concrete higher-difference obstruction

Normalize the critical powered profile by its amplitude:

$$q(s)=\begin{cases}s^{1/3}(1+s/2),&0<s\le1,\\
s+1/2,&s\ge1.
\end{cases} \tag{15}$$

It is C^2, with q(1)=3/2, q'(1)=1 and q''(1)=0. Its third derivatives
have a jump:

$$q'''(1-)=\frac29,\qquad q'''(1+)=0.$$

The unpowered profile g(s)=(K q(s))^(3/4) has

$$\frac{g'''(1-)}{g(1)}=\frac{13}{72},\qquad
\frac{g'''(1+)}{g(1)}=\frac5{72}.$$

Thus C^3 regularity of every actual oriented limiting profile would exclude
the endpoint. **No such regularity theorem has been proved here.**
Concavity supplies only one-sided first derivatives and cannot supply it.

One can replace this regularity target with a single finite inequality.
For the fifth forward difference, the exact radical expression

$$D=\Delta_{1/20}^5q(4/5)
=\sum_{k=0}^5(-1)^{5-k}\binom5k
q\left(\frac45+\frac k{20}\right)$$

satisfies

$$-\frac{306600}{10^{11}}<D<-\frac{306599}{10^{11}}<0. \tag{16}$$

Its approximate value is -0.000003065993116. The interval in (16) is
certified with rational arithmetic by the included verifier; it is not a
floating-point sign claim. Multiplication by any K>0 preserves the sign.

A universal nonnegativity theorem for this fifth difference of the powered
oriented profile would therefore contradict (13). For a smooth function,
a nonnegative fifth derivative implies this finite difference by five
applications of the fundamental theorem of calculus. Functions whose
derivative is completely monotone satisfy the required sign. These are
potential sources of a new premise, **not established tensor constraints**.

In particular, the already completed scalar concavity and tripling theory
admits (15) and cannot establish that fifth-difference inequality. Claiming
the sign as a consequence of ordinary concavity would be false.

Two follow-up calculations narrow this construction question. The
[quantum-character calculation](quantum_profiles.md) proves all the
alternating derivative signs on that actual family and, by a cited edge
classification, proves the fifth-difference test for every character with
one dot-product exponent equal to one. The
[matched-stencil obstruction](stencil_obstruction.md) proves that the
literal positive and negative block sums from (16) cannot degenerate to
one another at any finite scale, even with independent shared-input bases.
For the canonical common basis, all quantum characters nevertheless order
these block sums in the proposed direction. These facts leave the
interior-character and asymptotic-construction questions open.

## 6. Reproduction and limits

Run the standard-library verifier from this directory:

```sh
python verify.py
```

It checks the exact factorization (12), the derivatives at the diagonal,
the rational box examples, the endpoint equality examples in (9), and the
strict rational interval for (16). The full global inequalities and
rigidity theorem rest on the written proofs above. Finite checks do not
verify a universal theorem about tensor characters.

The next mathematical step must supply a new tensor inequality that rejects
the common oriented profile (13), or another restriction on actual
characters beyond the cited inputs. Neither a numerical optimizer nor the
new stability formulas alone supplies that step.
