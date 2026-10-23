# Owned question and checkpoint

Scope: biforms with arbitrary coefficients but z-degree at most one, for the literal original cyclic-source coefficient matrix R_(a,b). This is different from the diagonal-polynomial Toeplitz question in PR207 and the two-monomial and general biform projects in PR171 and PR186.

Resolved October 23, 2026 (written, unreviewed): if f=u(x)+z*v(x) is nonzero and d is the largest degree of its coprime primitive coefficient pair (or zero for a missing coefficient), rank R_(a,b)(f)=ab+min(b,ad), over every field. The exact rank spectrum and independent finite controls are in proof.md and verify.py.

Next precise problem: analyze arbitrary f=u(x)+z*v(x)+z^2*w(x) by the left-kernel recurrence
    u*lambda_r+v*lambda_(r+1)+w*lambda_(r+2)=0
for r=0,...,a-1, with lambda_L of degree <b. Determine whether primitive-degree and resultant data suffice to determine its kernel dimension; if not, construct an exact counterexample with identical coarse invariants but different ranks. Avoid claiming a tensor target from any single slice. The existing diagonal f(xz) question remains owned by PR207.

To claim an improved exponent one still needs a complete source-to-target degeneration and exact asymptotic character implication.
