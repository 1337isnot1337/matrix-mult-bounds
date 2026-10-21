# The central multiplicity tensor cannot degenerate to M2

**AI-CYCLIC-CENTRAL-POLYSTABILITY-048.** Written proof, unreviewed. Over C,
the degree-(6,6,6) multiplicity tensor B in the recoupling of A_4 is
SL_4^3-polystable. It cannot degenerate to M(2,2,2), even under arbitrary
singular changes of all three legs. This strengthens the ordinary-map
obstruction in claim 045; the earlier determinant certificate by itself
does not give this stronger conclusion.

There is no exponent improvement. This removes one possible matrix-factor
shortcut inside the recoupling; it does not exclude other values for B,
larger joint extractions or the general H1100/H106 constructions.

## 1. Exact cyclic symmetry and a smooth cubic surface

Take the rational multiplicity coefficients from `grouped-a4.json.gz`,
selecting the block with **degrees** (6,6,6), not label indices (6,6,6).
Its label indices are (3,3,3) and its multiplicity dimensions are (4,4,4).
Set

    T[i,j,k] = (-1)^i B[i,j,k],  0<=i,j,k<4.

Direct coefficient comparison gives T[i,j,k]=T[j,k,i]. Thus T is cyclically
symmetric and is isomorphic to B. Its symmetric projection is represented
by the cubic sum T[i,j,k] x_i x_j x_k. Clearing denominators and content
gives the following nonzero scalar multiple:

    f = -36400*x0^2*x1 + 3400*x0^2*x3
        +17280*x0*x1*x2 -1080*x0*x2*x3
        +11250*x1^3 -3375*x1^2*x3 -4374*x1*x2^2
        +450*x1*x3^2 +729*x2^2*x3 -75*x3^3.

The projective cubic f=0 is smooth. For each of the four charts x_i=1,
the saved certificate supplies four rational polynomials u_j such that

    sum_j u_j * primitive((partial f / partial x_j)|_(x_i=1)) = 1.

The multipliers have degree at most three; the four identities use
19, 18, 23 and 20 nonzero multiplier terms. `central_polystability.py`
reconstructs f from B, reconstructs all four primitive gradient systems,
and verifies these identities exactly. They exclude a simultaneous zero
of the gradient in every projective chart. Euler's identity for this
homogeneous cubic then gives smoothness over C. This certificate does not
depend on treating a numerical solver result as exact, or on trusting a
stored declaration that a Groebner basis equals one.

## 2. From the cubic to polystability of the full tensor

A smooth cubic surface is stable for SL_4: its cubic-form orbit is closed
and its stabilizer is finite. This is a classical external theorem; we use
Definition 6.2 and Proposition 6.5(a) of Arnaud Beauville,
[*Moduli of cubic surfaces and Hodge theory*](https://bremy.perso.math.cnrs.fr/smf_sec_18_13.pdf),
where the smooth-cubic case and its invariant-theory context are given.

We first apply the diagonal group SL_4 to V^{tensor 3}. Symmetrization is
an equivariant linear projection, and the image of T is the stable form f,
up to a nonzero scalar. This implies that the diagonal orbit of T is closed.
Here is the needed argument. If that orbit were not closed, the
Hilbert--Mumford criterion would give a nontrivial one-parameter subgroup,
after an orbit change, for which T has a finite limit outside its orbit.
Projecting gives a finite limit of the corresponding form in the orbit
of f, since that form orbit is closed. The one-parameter subgroup fixes
this limiting form. Its stabilizer is conjugate to the finite stabilizer
of f, a contradiction. The stabilizer of T is also a subgroup of that of
its symmetric projection and hence finite.

The closed diagonal orbit contains a point R of minimum Euclidean norm.
It is still cyclically symmetric, because applying the same linear map to
all legs preserves that symmetry. Therefore its three reduced density
matrices are equal, say rho_X=rho_Y=rho_Z=rho. Differentiating the squared
norm under exp(tH)^{tensor 3}, for every traceless Hermitian H, gives

    0 = 2*||R||^2 tr(H*(rho_X+rho_Y+rho_Z))
      = 6*||R||^2 tr(H*rho).

Thus rho is scalar, and normalization gives rho=I_4/4. By the tensor
Kempf--Ness criterion, R and hence B have closed SL_4^3 orbit. We use
Theorem 5.2 of van den Berg et al.,
[*Computing moment polytopes*, arXiv:2510.08336v1](https://arxiv.org/abs/2510.08336v1),
for precisely this uniform-marginal-to-polystability implication.
The passage from the cyclic tensor and its stable cubic to full
polystability is the argument supplied here; no historical priority is
claimed for this general observation.

## 3. Excluding the matrix factor

M(2,2,2) is polystable, in particular semistable, in the same 4-by-4-by-4
format. Proposition 5.3 of the moment-polytope paper, attributing the result
to Burgisser--Ikenmeyer, states that every boundary point of a polystable
tensor's GL orbit is unstable. Consequently a degeneration B -> M2
would force an ordinary isomorphism.

Claim 045 already excludes that isomorphism. Its exact slice-determinant
specialization has primitive polynomial

    192*x^4 + 352*x^2 - 765,

and the saved Bezout identity with its derivative proves squarefreeness.
The slice determinant of M2 is a quadratic square, and that property is
preserved by invertible leg changes. A nonzero squarefree quartic cannot
be the specialization of a square. The finite determinant calculation
and the full polystability argument together exclude the degeneration.

## Reproduction, provenance and scope

Run from the repository root with the existing dependencies:

```sh
python research/ai/2026-10-20-cyclic-recoupling/central_polystability.py
python -m unittest discover -s tests -p test_cyclic_polystability.py -v
```

The cubic and all four rational polynomial identities are stored in
`results/cyclic-recoupling-2026-10-20/central-cubic-smoothness.json`.
The optional discovery script reconstructs the identities by solving exact
linear coefficient equations; acceptance simply checks the saved identities.
The sources, versions, hashes and inspection scope are recorded in
`../2026-10-20-cyclic-mixed-map/sources.json`.

This is local AI-derived application of external geometric invariant
theory to the exact recoupling block. The proof is unreviewed and not
formalized. The scalar factor accompanying B has not been shown to
cancel in a degeneration; the conclusion concerns B itself. It also
does not rule out extracting smaller rectangular targets or obtaining
useful asymptotic value by a different route.
