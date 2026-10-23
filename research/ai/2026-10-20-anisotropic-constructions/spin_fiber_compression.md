# An ordinary weighted spin-compression obstruction at every power

Written local proof, unreviewed, October 21, 2026. Claim
AI-SPIN-FIBER-COMPRESSION-118. This excludes a specified compression family.
It supplies no smaller matrix multiplication exponent. Arbitrary source
maps remain open. The subsequent [linear-identity proof](spin_fiber_closure.md)
also excludes Laurent limits within this same fixed compression family.

## 1. Every individual raw-column weight is allowed

Write the source coordinates as F(i,m,s). In A(d,d), the first and last
indices range from 0 to d-1 and the middle from 0 to 2d-2. The full source is

    sum_(i,j,p,q,r,s=0)^(d-1)
        F_X(i,p+q,s) F_Y(p,r+s,j) F_Z(r,i+j,q).

Use the fixed rational spin map from the existing exact scalar witness.
For a matrix with row-major entries (a,b,c,d,e,f,g,h,i), its twelve source
coordinates, in lexicographic (first,middle,last) order, are

    (e+i, 2d-h/2, b/2, a, c, -b/2,
     h/2, g, i, -h/2, b/2-2f, a+e).

Its integral numerator J has denominator 2. Consider the k-fold tensor
power of this map. A raw column has k triples (i_b,m_b,s_b), with binary
short digits and middle digits in {0,1,2}. Its prescribed compressed
coordinate in A(2^k,2^k) is

    (sum_b 2^b i_b, sum_b 2^b m_b, sum_b 2^b s_b).

Give every raw column an arbitrary scalar weight before adding columns
in a fiber. This includes singleton fibers, all dependence on short and
middle digits, and independent weights on the three legs. No normalization
is imposed on a fiber's weights. There are 3*12^k independent variables.

Number them, with leg=0,1,2, by

    I=sum_b 2^b i_b, S=sum_b 2^b s_b,
    mu=sum_b 3^(k-1-b) m_b,
    variable=leg*12^k+(I*3^k+mu)*2^k+S+1.

The trit string encoding mu is distinct from the radix-two middle sum.
Target matrix rows are numbered 3^k*row+column. Each map has denominator
2^k, so each tensor coefficient has numerator scale 2^(3k).

## 2. Five complete source contractions at two bits

At k=2, the following selected coefficients are necessary for M9.
Each residual has been divided by the stated integer factor.

| Target rows | Divisor | Normalized residual f_j |
| --- | ---: | --- |
| (0,5,45) | 64 | w20 w173 w328 - 1 |
| (0,7,63) | 64 | w20 w165 w364 - 1 |
| (1,5,63) | 32 | w19 w173 w364 |
| (1,9,0) | 64 | w19 w152 w308 + w95 w228 w384 - 1 |
| (1,9,30) | 64 | w95 w228 w384 |

The first two equations force w173 and w364 to be nonzero. The third
therefore forces w19=0. The fourth then requires w95 w228 w384=1, while
the fifth requires that product to be zero.

An integer polynomial certificate, avoiding division by unknown weights,
makes the contradiction explicit:

    1 = (w20^2 w152 w165 w308 w328) f3
        - (w19 w20 w152 w173 w308 w328) f2
        - (w19 w152 w308) f1 - f4 + f5.

The verifier expands this identity and checks all five source contractions.
It does not infer nonexistence from an optimizer or assume nonzero weights.

## 3. Induction to all k>=2

Suppose a selected coefficient has been lifted to power k. Set d=2^k and
n=3^k. Append the high matrix-unit digits X:E00, Y:E02, Z:E20. Their
matrix-multiplication coefficient is one.

In J, the Y row E02 has only source column (0,2,0), with coefficient 2;
Z row E20 has only (1,0,1), also with coefficient 2. X row E00 has two
columns (0,1,1) and (1,2,1), each with coefficient 2.

The lower X row in all five equations is 0 or 1, and stays so at every
lift. Every local column appearing in E00 or E01 has middle digit at
least one. Its lower middle sum is therefore at least d-1.

The second high X column would give full middle at least 3d-1. But the
high Y first digit is zero, so p<d, while q<2d. The source equality
middle_X=p+q would require middle_X<=3d-2. This excludes the entire
second high-X branch for every possible choice of raw weights.

Only the high columns X:(0,1,1), Y:(0,2,0), Z:(1,0,1) contribute.
For these columns the three source equalities are precisely the old ones:

    middle_X+d = p+(q+d),
    middle_Y+2d = (r+d)+(s+d),
    middle_Z = i+j.

Thus the new numerator is exactly eight times the old numerator, after
an injective renaming of raw-column variables. The desired numerator also
scales by eight. The renaming is injective since the appended high columns
are fixed and every lower digit can be recovered. It identifies no distinct
unknown weights. The five equations and the polynomial identity for one
therefore lift to all k>=2.

The finite direct controls at k=2,3,4 verify the arithmetic and variable
renaming; the preceding induction supplies the all-power conclusion.

## 4. Verification, recovery, and scope

Run:

~~~sh
python -S research/ai/2026-10-20-anisotropic-constructions/spin_fiber_compression.py
python -S -m unittest discover -s tests -p 'test_spin_fiber_compression.py' -v
~~~

The certificate stores all fifteen selected residuals at powers two through
four and the integer identity. The tests separately enumerate all 4096
terms of A(4,4), in contrast to solving for the third source coordinate in
the verifier. Altering the saved coefficient must fail replay.

The source, tests, and certificate were reconstructed after an execution
environment rollback, from the retained equations and proof. The original
and reconstructed checks both pass; the committed receipt identifies the
reconstructed bytes. A separate agent audited the all-power proof in this
generating session. This is not external independent mathematical review.

The local spin map and radix fibers are fixed. The weights may be arbitrary
field elements. The argument also excludes an exact identity with weights
in a characteristic-zero extension field, such as rational functions.
This polynomial-identity argument alone does not exclude a limiting
degeneration whose residuals tend to zero:
pole weights can multiply those residuals in the displayed polynomial
identity. The separate linear-identity proof in claim124 closes those
limits in this same family. Arbitrary source maps, altered local maps,
and additional output maps remain open. No historical priority or
exponent gain is claimed.
