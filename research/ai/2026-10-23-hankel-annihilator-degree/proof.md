# Exact inner ranks from the degree of the supporting scheme

October 23, 2026. Owner-directed Codex continuation; written and unreviewed.
This is a pointwise constraint on cyclic-source slices. It does not
construct matrix tensors or establish a smaller exponent.

Use A(a,b), d=a+b-2 and the polynomial symbol H_F(x,z) of the preceding
[kernel-descent note](../2026-10-23-hankel-equality/proof.md). Assume its
rational-function rank r satisfies 1<=r<min(a,b). Let q(U,V) be its
degree-r homogeneous supporting form over C(x,z), up to a rational unit.

For q regarded over C(z)(x), clear x denominators and remove the gcd of
its coefficients in C(z)[x]. Let epsilon_x be the x-degree of this
primitive form. Define epsilon_z similarly over C(x)[z]. These degrees
do not depend on the original rational scalar multiplying q.

## 1. Exact coefficient-map ranks

Let rho be the rank over C(x) of the full coefficient map H_F on b
polynomials in z of degree below a. Let sigma be the rank over C(z) of
the full coefficient map H_F^T on a polynomials in x of degree below b.
Then

    rho   = ar + (b-r) min(epsilon_z,a),
    sigma = br + (a-r) min(epsilon_x,b).                    (1)

Proof: work over L=C(x), and choose q primitive over L[z]. The scalar
Hankel kernel description gives the rational right kernel
q S_(b-1-r) over L(z). Gauss's lemma shows that its polynomial vectors
are exactly q times binary forms of degree b-1-r with coefficients
in L[z]. Indeed q is primitive as a polynomial in U,V over the UFD
L[z], so divisibility over its fraction field descends to that UFD.

If such a multiplier is nonzero, its z-degree adds to epsilon_z under
multiplication by q. The product's leading z coefficient cannot vanish,
because it is a product of two nonzero binary forms over a field.
Thus input coefficient vectors of degree below a in the kernel are
parametrized by b-r coefficient polynomials of degree below a-epsilon_z.
Their dimension is (b-r) max(a-epsilon_z,0). Subtract from the ab input
dimensions to get rho. Applying the same argument to the left kernel
over C(z)[x] gives sigma. No pencil index theorem or bundle splitting
result is needed for these coefficient-map identities.

## 2. A wider constant-scheme strip

The maintained outer injections rank M_F>=b rho and rank M_F>=a sigma
now give

    rank M_F >= ab r + max(
        b(b-r) min(epsilon_z,a),
        a(a-r) min(epsilon_x,b)).                          (2)

In particular, put

    Delta = min(a(a-r), b(b-r)).

If rank M_F<ab r+Delta, both degrees vanish. Then the projective form q
is defined over C(x) and over C(z), hence over C by the preceding
kernel-descent argument. All coefficient sequences of F therefore share
one constant length-r supporting scheme.

This strengthens the earlier min(a,b)-wide strip when the symbol rank
is farther below both format sizes. It remains a pointwise conclusion.
It does not identify the schemes at two different matrix parameters.
At the A9 equality rank r=8, Delta=9, so this continuation does not
strengthen that particular width or close its outstanding family problem.

## 3. Exact full ranks with one fixed short factor

If f_k(x,z)=h_k(x)v(z) for one nonzero polynomial v of degree below b,
with deg h_k<a, the full source matrix is a Kronecker product after
regrouping its rows and columns:

    M_F = (h_(p+q,H-j))_((j,p),(H,q)) tensor (v_(L-r))_(L,r).

The second factor is full polynomial multiplication by v on polynomials
of degree below a; it has rank a. The first factor is the transpose of
the inner x coefficient map, with rank sigma. Consequently

    rank M_F = a sigma = ab r+a(a-r) min(epsilon_x,b).       (3)

Here epsilon_z=0, since multiplying the symbol by v(z) does not change
its projective supporting form. Thus the bound (2) is exact throughout
this fixed-short-factor chart, not just in the particular sharpness family.
The symmetric statement for f_k=u(x)h_k(z) is rank M_F=b rho. This
calculation does not presume that every slice with a one-variable
supporting form has the displayed common factor.

## 4. Sharpness in every balanced deficient rank at least two

Fix a=b=n and 2<=r<n. Set

    f_k = x^(k/r) if r divides k, and f_k=0 otherwise,
    0<=k<=2n-2.

The degrees satisfy floor((2n-2)/r)<=n-1. The supporting form is
q=V^r-x U^r, of x-degree one and z-degree zero. The first r moments and
the recurrence show rank H_F<=r, while its leading r-by-r minor is a
nonzero signed power of x, so rank H_F=r.

As these f_k are independent of z, the full source matrix splits into
n copies of the full x coefficient map with input degree below n.
Equation (1) gives each copy rank nr+(n-r). Consequently

    rank M_F = n^2 r+n(n-r) = ab r+Delta.                  (4)

There is no constant degree-r annihilator: the coefficient of x is the
sequence supported at k=r, whose recurrence shifts force all r+1
annihilator coefficients to vanish. Thus the strict boundary in section 2
is sharp for each balanced n and each 2<=r<n. The rank-one case is not
included in this sharpness statement; the earlier polynomial rank-one
classification already makes its supporting point constant.

The subfamily r=n-1 is exactly the sharpness family from the preceding
note, retained with its credit. The current extension supplies the exact
inner-rank formulas and the larger widths for r<n-1. Exact finite controls
also test higher primitive degrees and variation in both variables. The
general statements rest on the written proof, not those controls.

## Dependencies and status

The scalar Hankel homogeneous kernel description and full-output source
coefficient injections are prior repository work, pinned in sources.json.
The preceding kernel-descent proof supplies the field-intersection step.
Gauss's lemma and degree additivity in polynomial rings supply the new
kernel count. No new external theorem is imported. No independent
mathematical review, formalization, historical novelty or exponent
improvement is claimed.
