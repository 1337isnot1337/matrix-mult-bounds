# An explicit invertible quadratic two-plane

October 25, 2026. Claim `AI-QUADRATIC-INVERTIBLE-TWO-PLANE-002` is written and
unreviewed. This supplies a lower bound two over fields containing
i with i^2=-1 and characteristic not two, leaving the proven upper bound four
unmatched. It is not a dimension-four sharpness construction. Same-session
algebra and exact replay are corroboration, not independent review or
formalization. Exact source and discovery pins are in [sources.json](sources.json).

Use the monomial coefficient matrix

    M(x,y)=[[0,x+i*y,x-y],[-x-i*y,-2*x,x-i*y],[x+y,-x+i*y,0]].

Its two coefficient vectors are independent: the middle coefficient is -2x,
so a vanishing linear combination first forces x=0, then y=0. Also
det M=4*x^3. The source is exactly the full 15-by-15 R_(3,3) convention in
[the companion proof](proof.md). A direct symbolic check
of the pinned invariant gives Delta(M)=0. There is also an elementary
normal-form derivation: with the determinant package's P, M=P*N*P^t, where

    N=xI+cross(v),  v=(x,y,i*y),  v^t v=x^2,
    cross(v)=[[0,-i*y,y],[i*y,0,-x],[-y,x,0]].

Since cross(v)^2=v*v^t-x^2 I,

    N^t N=2*x^2 I-v*v^t.

Over the generic field (x nonzero), v spans the eigenline of eigenvalue x^2
and its orthogonal plane has eigenvalue2*x^2. Their inverse eigenvalues
satisfy 1/x^2=1/(2*x^2)+1/(2*x^2), so Delta0=0. Polynomial extension gives
Delta=0 on the full two-space, hence det R=0 in every odd characteristic.
This argument uses square roots for P only in an algebraic closure; M itself
is defined over K if i is in K.

At (x,y)=(1,0), M=[[0,1,1],[-1,-2,1],[1,-1,0]] has integer entries.
Delete row (j,L)=(0,1) and column (H,r)=(1,0) from its literal source;
the resulting 14-by-14 integer minor has determinant **16**. Both pair
orders are lexicographic, so these are zero-based indices 1 and 3.
The retained exact certificate exports the matrix and computes its determinant
directly. This minor stays nonzero in every odd characteristic. Since the
source determinant is already identically zero, its rank at this basepoint
is exactly fourteen in every odd characteristic. Thus this is a
two-dimensional geometric rank-at-most14 family containing invertible
coefficient points and rank14 source points. No claim about every source
rank away from x=0 is needed.

Discovery checks also found integral Smith diagonal (1 repeated12,4,4,0)
and the leading
14-by-14 literal minor

  16*x^8*(x+i*y)^2
    *(x*(1-2i)-i*y)*(x*(1-2i)+i*y)
    *(x*(2-i)-y)*(x*(2-i)+y).

This particular leading minor is not a uniform basepoint certificate in
characteristic five; the different minor16 above is the acceptance certificate.
Do not infer rational-ground-field two-space existence from this K(i)
construction. Sharp dimensions three/four and the
upper bound in characteristic two remain open. The companion argument closes
the characteristic-three upper bound at four. No exponent improvement follows.
