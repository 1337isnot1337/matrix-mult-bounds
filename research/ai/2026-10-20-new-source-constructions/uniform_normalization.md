# An explicit diagonal-orbit normalization in every degree

October 21, 2026. AI-derived written argument, unreviewed. This is a target
normalization theorem. No source degeneration or exponent improvement is
proved.

Let `m>=2` and `D=m-1`. Write the canonical target as

\[
 T_m=\sum_{u=0}^{D}\sum_{a=0}^{u}\sum_{c=0}^{D-u}
 X_{a+c}Y_{u,a}Z_{u,c}.
\]

Here `Y_(u,a)` denotes the earlier coordinate `(a,u-a)`, and `Z_(u,c)`
denotes `(c,D-u-c)`. Consider a tensor on this exact support whose
coefficients `t_(u,a,c)` are all nonzero. Its coefficients belong to the
diagonal orbit of `T_m` exactly when

\[
t_{u,a,c}=\alpha_{a+c}\beta_{u,a}\gamma_{u,c}
\tag{1}
\]

for nonzero row scalars. Everything below works over an arbitrary field.

## 1. A uniform set of independent coefficients

Select these support positions:

1. Every axis entry, meaning `a=0` or `c=0`, in every sector `u`.
2. The additional entries `(u,a,c)=(1,1,c)` for `1<=c<=m-2`.

There are `m` axis entries per sector, hence `m^2` in total, and `m-2`
additional entries. All the selected values can be assigned independently
and arbitrarily in the multiplicative group of the field.

To prove this, set the scalar gauges

\[
\alpha_0=\alpha_1=1,\qquad \beta_{u,0}=1\quad(0\le u\le D).
\tag{2}
\]

Recover the other shared scalars recursively from the sector `u=1`:

\[
\alpha_{c+1}
 =\alpha_c\,
 \frac{t_{1,1,c}\,t_{1,0,0}}
      {t_{1,0,c}\,t_{1,1,0}},
 \qquad 1\le c\le D-1.
\tag{3}
\]

Then set, in every sector,

\[
\gamma_{u,c}=\frac{t_{u,0,c}}{\alpha_c},\qquad
\beta_{u,a}=\frac{t_{u,a,0}}{\alpha_a\,t_{u,0,0}}.
\tag{4}
\]

Equations (3) and (4) are Laurent monomials in the selected coefficients.
They reproduce every axis entry immediately. Substituting (3) verifies each
additional selected entry. Thus arbitrary nonzero selected coefficients
give unique row scalars with gauges (2), without taking any roots.

## 2. Complete equations for the remaining coefficients

For each unselected position require

\[
t_{u,a,c}
 =\frac{\alpha_{a+c}}{\alpha_a\alpha_c}
  \frac{t_{u,a,0}t_{u,0,c}}{t_{u,0,0}},
\tag{5}
\]

where the `alpha` values are the explicit expressions (3). These are
necessary: substitute (1) into (3), or use the uniqueness of the gauge
normalization. They are sufficient because (4) then reproduces every
coefficient. Clearing the monomial denominators produces binomial
equations, with the nonzero conditions retained.

Every equation has a distinct unselected coefficient appearing to exponent
one and otherwise uses only selected coefficients. The equations therefore
give an exact graph over a torus of dimension `m^2+m-2`; they do not introduce
additional components on the stated open set. Their number is

\[
\binom{m+2}{3}-(m^2+m-2)
 =\frac{(m-3)(m-2)(m+2)}6.
\tag{6}
\]

The two nontrivial relations for `m=4` are the quartic relations in the
package's main README after changing the support ordering. At `m=2,3`,
every assignment of nonzero support coefficients is diagonally equivalent
to the unit target.

For a bound on equation size, put `l=min(a,c)` and `h=max(a,c)`, and define

\[
r_s=\frac{t_{1,1,s}t_{1,0,0}}{t_{1,0,s}t_{1,1,0}}.
\]

For any unselected entry, `a,c>=1` and

\[
\frac{\alpha_{a+c}}{\alpha_a\alpha_c}
 =\frac{\prod_{s=h}^{a+c-1}r_s}{\prod_{s=1}^{l-1}r_s}.
\]

After cancellation, (5) has binomial degree at most `2l+2`, hence at most
`2 floor((m-1)/2)+2`. Further cancellations can decrease the degree. This
degree refers to target coefficients; substituting source-map coefficients
can increase it.

## 3. Integer incidence interpretation

The support incidence matrix has one row per target term and one column
per row scalar. Select the rows listed in Section 1. Delete columns
`alpha_0`, `alpha_1`, and `beta_(u,0)` for every `u`, as in (2). The remaining
square matrix has size `m^2+m-2`.

The monomial map represented by this square integer matrix has the
Laurent-monomial inverse (3)--(4). At the level of integer exponent vectors,
the inverse is an integer matrix. Therefore the selected determinant is
`+1` or `-1`. This proves saturation uniformly in `m`, independently of the
finite checks. In particular, the full incidence matrix has rank
`m^2+m-2` and its diagonal stabilizer has dimension

\[
(m+2\,m(m+1)/2)-(m^2+m-2)=m+2.
\]

The relation vectors from (5) form an integer basis of the incidence
kernel: their unselected-coordinate submatrix is the identity, and the
selected square minor is unimodular. Thus the equations describe the orbit
over every field without an algebraic-closure hypothesis.

## 4. Relation to the source construction problem

For a polynomial flag model with nonzero leading row coefficients, divide
each row by its leading coefficient. This makes the maps monic and replaces
unit target coefficients by coefficients in precisely this diagonal orbit.
Conversely, (3)--(4) provide exact row scalings restoring the unit target.
The zero coefficients, polynomial degrees, and parameter weights are
preserved. Thus the method removes the monic-leading-coefficient restriction
for every such target, within any fixed flag model to which it is applied.

This does not supply polynomials satisfying the required zero pattern or
the orbit equations. A large number of variables relative to equations
does not establish their solvability.

## 5. Finite implementation controls

`general_target_orbit.py` constructs the incidence matrix, selected minor,
and relation vectors independently of the source ansatz. The recorded exact
controls cover `m=2,...,7`; the regression suite additionally reconstructs
random diagonal orbits over `F3` and `F4` for `m=2,...,8` and rejects a
modified unselected coefficient. The all-degree argument is Sections 1--3,
not extrapolation from these finite computations.

The canonical target and its earlier `m+2` stabilizer count were already
present in the repository. The contribution here is the explicit uniform
coefficient selection, Laurent inverse, complete orbit equations, and their
use to remove a restriction of the monic flag search. No historical priority
is claimed.
