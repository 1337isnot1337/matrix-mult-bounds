# Characteristic-two attainers with a common evaluation kernel

October 25, 2026. Claim `AI-CHAR2-EVALUATION-KERNEL-ATTAINERS-001` is
**proof-written-unreviewed**. Exact algebra and separate same-session auditing
corroborate this argument, not independent review or formalization.

## Statement and scope

Let k be algebraically closed of characteristic two. Let W be a
three-dimensional linear coefficient family for the complete quadratic
source, with geometric source rank at most fourteen and D=detM not
identically zero. Write e=M11 and U=W intersect {e=0}. Suppose U has a
common nonzero right kernel vector u on the evaluation conic
u1^2=u0*u2, or the corresponding common left kernel. Then W is equivalent,
by permitted binary changes and optional transpose, to exactly one of

    N(t,x,y)=[[t,x,0],[0,t,x],[0,y,0]],
    P(x,y,z)=[[x,x,0],[0,y,0],[0,z,z]].

These two forms are inequivalent by the pinned section-kernel invariant.
Thus this evaluation-kernel part of the characteristic-two attainer locus
has exactly two geometric orbits. The pinned packages supply the converse
and exact source rank fourteen at coefficient-invertible points.

The two normalized-chart classifications below work over every field K
of characteristic two if the displayed first-column normalization is
already available over K. For an arbitrary ground field, the theorem
classifies after extension to its algebraic closure. We do not claim that
the required first-column normalization descends over nonclosed K, nor
classify its possible ground-field forms. Families without a common
evaluation kernel in U are outside the theorem. No full characteristic-two
classification or matrix-multiplication exponent improvement follows.

## 1. Source, integral form and the two charts

Use the complete source with lexicographic pair orders

    R(M)[(j,L),(H,r)]=M[H-j,L-r],
    0<=j,r<=2, 0<=L,H<=4,

and out-of-range entries zero. Geometric vanishing means detR is the zero
polynomial on W, not merely zero at rational points. The pinned integral
lemma gives the unique linear form ell=T4/D and identities

    T4=D*ell, D=e*(A2+e*ell+ell^2), A2=bh+df

for M=[[a,b,c],[d,e,f],[g,h,i]]. In particular e is a nonzero linear form
and dimU=2. The integer quartic T4 is reduced modulo two before use;
its exact formula and source provenance are pinned.

Permitted binary changes are M -> A(g) M A(h)^t, where

    A([[alpha,beta],[gamma,delta]])=
      [[alpha^2,alpha*gamma,gamma^2],
       [0,alpha*delta+beta*gamma,0],
       [beta^2,beta*delta,delta^2]].

They preserve source rank and scale e by det(g)det(h); transposition is
also permitted. Over k, normalize a common evaluation kernel to e0. For
u=(1,r,r^2), h=[[1,0],[r,1]] has A(h)^(-t)u=e0; the remaining endpoint
is handled by swapping variables. The first column of W is then e*v for
a fixed nonzero v, since D is nonzero. Ordinary binary quadratics over k
have two nonzero orbits: squares, represented by e0, and products of two
distinct linear forms, represented by eta=(0,1,0).

Choose g with A(g)v=c*w, c!=0, w=e0 or eta. A further right change
diag(s,1) gives first column s^2*c*e*w and e'=det(g)*s*e. Choosing
s=det(g)/c gives first column e'*w. Set t=e'. We obtain exactly two charts:

    square:       [[t,b,c],[0,t,f],[0,h,i]],
    nonsingular:  [[0,b,c],[t,t,f],[0,h,i]].

All entries b,c,f,h,i,ell are linear forms on W. We now work over any K
where a displayed chart is defined; no roots are extracted in Sections2-3.
A bar denotes restriction to U={t=0}. Algebra takes place in polynomial
domains K[W] and K[U], including when K is finite.

## 2. Square first-column chart

Here D=t(ti+fh). The integral identities, after canceling the nonzero
polynomial t, become

    Q=ti+fh+bh+t*ell+ell^2=0,
    C=t*i^2+bhi+c*h^2+(ti+fh)*ell=0.                 (S)

### 2.1. The restriction h-bar cannot vanish

If h-bar=0, then Q|U gives ell-bar=0. Write h=rho*t, ell=mu*t and
sigma=mu+mu^2. Dividing Q by t yields

    i+rho*(f+b)+sigma*t=0.

If rho=0 then i=sigma*t, D=sigma*t^3, and C/t=sigma*mu^2*t^2.
Since D!=0, sigma!=0; hence mu=0 and sigma=0, a contradiction.

If rho!=0, the full second equation divided by t is

    C/t=i^2+rho*b*i+rho^2*c*t+mu*t*(i+rho*f)=0.

Its restriction to U is i-bar*(i-bar+rho*b-bar)=0. Both branches are
necessary; the mixed term rho*b*i cannot be dropped.
If i-bar=0, write i=I*t and f=b+kap*t. If i-bar=rho*b-bar, write
i=rho*b+I*t and f=kap*t. In either branch kap=(I+sigma)/rho and

    C/t=t*[rho*(I+mu)*b+rho^2*c+(I^2+mu*I+mu*rho*kap)*t].

Every matrix entry now depends only on t,b,c, so dimension three makes
these forms independent. The coefficient rho^2 of c is nonzero, a
contradiction. Thus h-bar is nonzero.

### 2.2. All remaining square families are shears of N

On U, Q says h-bar*(f-bar+b-bar)=ell-bar^2. Primality of the nonzero
linear form h-bar makes ell-bar=lambda*h-bar and
f-bar+b-bar=lambda^2*h-bar for some lambda in K. Extend to W as

    ell=lambda*h+mu*t,
    f=b+lambda^2*h+kap*t.

Equation Q forces

    i=alpha*h+beta*t, alpha=kap+lambda, beta=mu+mu^2.

Substitution into C gives exactly

    h^2*[c+kap*b+lambda^3*h+(alpha^2+lambda^2*(mu+1))*t]
      +mu^2*b*h*t+lambda*mu^2*h*t^2+beta*mu^2*t^3=0.

Complete the independent forms t,h to coordinates t,h,z. If B and C0 are
the z coefficients of b and c, comparing z gives
C0+kap*B=0 and mu^2*B=0. If mu!=0, both B and C0 vanish, so every entry
would depend only on t,h, contradicting dimension three. Therefore mu=0.
The equation reduces to

    ell=lambda*h,
    f=b+lambda^2*h+(alpha+lambda)*t,
    i=alpha*h,
    c=(alpha+lambda)*b+lambda^3*h+(alpha^2+lambda^2)*t.       (S0)

The forms t,b,h are independent. The determinant is
D=t*h*(b+lambda*t+lambda^2*h), not the zero polynomial.

These are precisely permitted shear images of N. Take

    g=[[1,0],[lambda,1]], q=[[1,alpha],[0,1]].

Direct multiplication A(g)N(t,x,y)A(q)^t gives (S0) with
h=y and b=x+lambda*t+lambda^2*y. Both binary determinants are one and
this coordinate substitution is invertible. Thus the square chart has
one orbit, represented by N, over any field where it is normalized.

## 3. Nonsingular first-column chart

Here D=t(bi+ch). The integral equations become

    Q=bi+ch+bh+t*(f+ell)+ell^2=0,
    C=bfh+ct*(i+h)+(bi+ch)*ell=0.                  (T)

### 3.1. The restriction ell-bar must vanish

On U, combining C+ell*Q gives

    b-bar*h-bar*(f-bar+ell-bar)=ell-bar^3.

If ell-bar!=0, both b-bar and h-bar are nonzero and divide ell-bar^3.
Thus b-bar=beta*ell-bar, h-bar=eta*ell-bar with beta*eta!=0, and
f-bar=(1+1/(beta*eta))*ell-bar. Equation Q|U gives
beta*i-bar+eta*c-bar+(beta*eta+1)*ell-bar=0. All restricted entries are
then determined by c-bar,ell-bar; dimension two makes these independent.
Take coordinates x=ell,y=c,t on W and write

    b=beta*x+B*t, h=eta*x+H*t,
    f=(1+1/(beta*eta))*x+F*t,
    i=(eta/beta)*y+(eta+1/beta)*x+I*t.

The t*y coefficient in Q forces H=B*eta/beta. Hence bi+ch has no y term.
But the coefficient of t*y^2 in C is then eta/beta, from ct(i+h), and
cannot be canceled by either remaining term. This contradiction proves
ell-bar=0, so ell=L*t for a scalar L in K.

### 3.2. Neither b-bar nor h-bar can vanish

Suppose b-bar=0 and h-bar!=0. Equation Q|U gives c-bar=0, so b=B*t,c=C0*t.
Equation Q/t gives

    f=B*i+(C0+B)*h+L*(1+L)*t.

Thus h-bar,i-bar must be independent. Equation (C/t)|U is B*f-bar*h-bar=0.
If B!=0, it forces f-bar=0 and then makes i-bar proportional to h-bar,
a contradiction. Hence B=0. Now D=C0*t^2*h!=0 requires C0!=0, while
full C forces i=(L+1)*h. Every entry then depends on t,h, another
contradiction. The case h-bar=0,b-bar!=0 is equivalent: the permitted
left change A([[0,1],[1,0]]) swaps rows0,2, exchanges b,h and c,i,
and changes ell to ell+t. Direct substitution preserves (T).

If b-bar=h-bar=0, write b=B*t,h=H*t. Equation Q gives
f=B*i+H*c+(BH+L+L^2)*t. Hence c-bar,i-bar are independent, but
(C/t)|U=c-bar*i-bar=0, impossible. This exhausts the vanishing cases.

### 3.3. All remaining nonsingular families are shears of P

Since b-bar,h-bar are nonzero, C|U=0 forces f-bar=0. Put f=F*t,
j=i+h, a=F+L and S=F+L+L^2. The two equations become

    b*j+c*h+S*t^2=0,
    c*j+a*b*h+L*S*t^2=0.

On U, multiplying and subtracting gives
h-bar*(c-bar^2+a*b-bar^2)=0. Thus c-bar^2=a*b-bar^2. Comparing a nonzero
coefficient of b-bar shows c-bar=r*b-bar for a scalar r in K with r^2=a;
no root is adjoined. The first equation then gives j-bar=r*h-bar.
Every restricted entry is determined by b-bar,h-bar, so these are independent.
Write c=r*b+C0*t and j=r*h+J*t. The first full equation, divided by t,
is J*b+C0*h+S*t=0. Independence forces J=C0=S=0. Therefore
r^2=L^2, so r=L and F=L+L^2. The family is exactly

    M_L(t,b,h)=[[0,b,L*b],[t,t,L*(1+L)*t],[0,h,(L+1)*h]],
    D=t*b*h.

Right multiplication by A([[1,L],[0,1]])^t sends M_L to M_0. Also

    M_0(t,b,h)=P(b,t,h) A([[1,0],[1,1]])^t.

Both are permitted determinant-one changes. Thus this chart has exactly
one orbit, represented by P, over any field where it is normalized.

## 4. Exhaustion, converse and evidence

Section1 gives the two charts over k. Sections2-3 exhaust every branch
without assuming U contains a rank-two matrix. The pinned source
certificates for N and P prove the converse. Their intrinsic section
common-kernel dimensions are respectively (right,left)=(1,0) and (1,1).
Permitted changes preserve these dimensions and transpose swaps them, so
the two orbits remain distinct even after allowing transposition.

The proof deliberately stops at the evaluation-kernel locus. It does not
exclude other singular pencils U, prove that every attainer has such a
kernel, or descend arbitrary first-column normalizations to the ground
field. The exact checker verifies the chart equations, both repaired
h-bar=0 branches, the remaining coefficient obstructions and the explicit
shears. It does not computationally certify the geometric exhaustion.

During same-session auditing, an initial h-bar=0 argument omitted rho*b*i
from C/t. Retaining it requires the two branches treated in Section2.1;
both are now checked. An initial audit also questioned whether reversing
rows0,2 was permitted; its explicit binary matrix above resolves that
question. Neither discarded argument is a premise. Exact source and
discovery pins retain these corrections. No independent review,
historical-priority claim, compatible tensor map or exponent gain.
