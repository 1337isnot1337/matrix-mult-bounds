# The whole determinant filtration: an entropy upper certificate

October 20, 2026. AI-derived work by Codex in a session directed by the
repository owner. Written proofs below are unreviewed and not Lean formalized.
No smaller matrix-multiplication exponent is proved.

## 1. Question and exact scope

The earlier local note defines the matching scalar profile

\[
h_1=1,\quad h_{r+1}=\frac{3r+1}{3r}h_r,\qquad
P_*(a,b)=h_{\min(a,b)}\left(\max(a,b)+\frac{\min(a,b)-1}{2}\right).
\]

The recurrence comes from OpenAI's external proof; the matching two-variable
profile comes from this repository's first research pass.

For the determinant filtration of \(C(a,b)\otimes C(c,d)\), put

\[
A_i=a+c-1-2i\quad(0\le i<\min(a,c)),\qquad
B_j=b+d-1-2j\quad(0\le j<\min(b,d)).
\]

Its blocks have support \((i,j,k)=(i,j,i+j)\) and values
\(f_{ij}=P_*(A_i,B_j)\). Instead of extracting only one row, column or diagonal,
consider every probability distribution \(q=(q_{ij})\) on this support. Write
\(q_X,q_Y,q_Z\) for its marginals and use natural logarithms. Define the
**optimistic entropy score** at \(t=3/4\) by

\[
E(q)=\exp\left(\frac43\min\{H(q_X),H(q_Y),H(q_Z)\}
                   +\sum_{ij}q_{ij}\log f_{ij}\right). \tag{1}
\]

This note proves upper bounds on the explicitly defined analytic expression
(1). It does **not** assert a weighted block-extraction theorem. Strassen's
tight-support subrank theorem for scalar coefficients does not, by itself,
provide the needed theorem for arbitrary tensor-valued blocks. That bridge
requires control of the retained joint types. Any proposed extraction estimate
obtained by decreasing (1), for example by an entropy-loss term, inherits these
upper bounds.

An upper bound \(E(q)\le P_*(a,b)P_*(c,d)\) means this particular score cannot
exclude the matching profile at that source. It does not show that the profile
extends to an actual tensor character. The assertions here concern one
application of this two-source filtration, not every iteration, degeneration,
orientation-dependent estimate, or auxiliary tensor.

## 2. An upper certificate for every distribution

Let \(u_i,v_j\) be positive probability vectors. If \(C>0\) satisfies

\[
f_{ij}^3\le C^3(u_iv_j)^2\quad\hbox{for every }i,j, \tag{2}
\]

then \(E(q)\le C\) for **every** probability distribution \(q\).

Indeed, relative-entropy nonnegativity gives

\[
\sum q_{ij}\log f_{ij}
 \le\log C+\frac23\sum q_{ij}(\log u_i+\log v_j)
 \le\log C-\frac23\bigl(H(q_X)+H(q_Y)\bigr).
\]

Since the minimum of the three marginal entropies is at most
\((H(q_X)+H(q_Y))/2\), substitution in (1) proves the assertion.
Zero entries of \(q\) use the convention \(0\log0=0\).
This proof actually discards the output entropy and so bounds a larger score.
The pointwise tests (2) are rational when the data are rational; no logarithm
evaluation or numerical optimization is required for acceptance.

## 3. A closed upper bound for the matching profile

Define

\[
R(x,y)=\frac{P_*(x,y)}{h_xh_y},\qquad
W(a,c)=\sum_{i=0}^{\min(a,c)-1}h_{a+c-1-2i}^{3/2}.
\]

The function \(R\) is coordinatewise nondecreasing. To see this, for \(x\le y\),
\(R(x,y)=(y+(x-1)/2)/h_y\). Increasing \(x\) while \(x<y\) plainly increases
it. For increasing \(y\), direct subtraction gives

\[
R(x,y+1)-R(x,y)
=\frac{2y-(x-1)/2}{(3y+1)h_y}>0.
\]

Symmetry handles the other half and the join.

Set \(A=a+c-1\), \(B=b+d-1\), and choose
\(u_i=h_{A_i}^{3/2}/W(a,c)\), \(v_j=h_{B_j}^{3/2}/W(b,d)\).
Monotonicity gives

\[
f_{ij}\le R(A,B)h_{A_i}h_{B_j}
=R(A,B)\bigl(W(a,c)W(b,d)\bigr)^{2/3}(u_iv_j)^{2/3}.
\]

Consequently the all-distribution certificate of Section 2 proves

\[
\boxed{E(q)\le U(a,b,c,d):=
R(a+c-1,b+d-1)\bigl(W(a,c)W(b,d)\bigr)^{2/3}.} \tag{3}
\]

This is an all-size analytic inequality. It does not yet assert
\(U(a,b,c,d)\le P_*(a,b)P_*(c,d)\) for all unequal sources.

For exact finite checking, enclose each \(h_r^{3/2}=\sqrt{h_r^3}\) between
rationals with denominator \(10^{12}\), using an integer square root. Upper
endpoints give rational upper bounds on

\[
\left(\frac{U}{P_*(a,b)P_*(c,d)}\right)^3
=\frac{R(A,B)^3W(a,c)^2W(b,d)^2}
       {\bigl(P_*(a,b)P_*(c,d)\bigr)^3}. \tag{4}
\]

If either input marginal is a singleton, its entropy is zero. We use the
stronger direct bound \(E(q)\le\max f_{ij}=P_*(A,B)\) in those cases.

## 4. All-size balanced obstruction with a uniform gap

**Theorem.** For every integer \(n\ge2\) and every distribution on the complete
filtered support of \(C(n,n)^{\otimes2}\),

\[
\boxed{E(q)\le\frac{39}{40}P_*(n,n)^2.} \tag{5}
\]

Thus even the optimistic full-support score has a uniform gap of at least
2.5 percent below the matching source profile in this balanced family.
For \(n=1\) both scores are one.

**Proof for \(n\ge23\).** Write \(D_r=P_*(r,r)=h_r(3r-1)/2\), \(M=2n-1\),
and \(S_n=\sum_{r=1}^n\sqrt{2r-1}\).
The recurrence implies that \(h_r^3/r\) is increasing, because

\[
(1+1/(3r))^3-(1+1/r)=\frac{9r+1}{27r^3}>0.
\]

Therefore \(W(n,n)\le h_M^{3/2}S_n/\sqrt M\), and (3) gives

\[
E(q)\le D_M S_n^{4/3}/M^{2/3}. \tag{6}
\]

Also \(h_r^3/(3r-1)\) is decreasing, since

\[
27r^3(3r+2)-(3r+1)^3(3r-1)=6r+1>0.
\]

For \(n\ge2\), these two facts imply

\[
\frac{h_M^3}{h_n^3}\le\frac{3M-1}{3n-1},\qquad
h_n^3\ge\frac{32}{27}n.
\]

Since \(\sqrt{2x-1}\) increases, integrating on each interval \([r,r+1]\) gives
\(S_n\le((2n+1)^{3/2}-1)/3<(2n+1)^{3/2}/3\).
Cubing (6) and substituting these bounds yields

\[
\left(\frac{E(q)}{D_n^2}\right)^3
\le\frac{(6n-4)^4(2n+1)^6}{12n(3n-1)^7(2n-1)^2}. \tag{7}
\]

The right side of (7) is at most \((39/40)^3\) for \(n\ge23\).
This final rational-function inequality is certified by expanding

\[
39^3\,12n(3n-1)^7(2n-1)^2-40^3(6n-4)^4(2n+1)^6
\]

at \(n=x+23\). Its coefficients in ascending powers of \(x\) are

```text
463473295577927475200, 1709651189933223690240,
634923381925359316992, 109073160428966591488,
11045146149507482880, 722079120865940544,
31538029592560400, 919438579999572,
17244651958668, 188764352640, 918655344
```

Every coefficient is positive. This proves the inequality for every real
\(x\ge0\), hence all integers \(n\ge23\).

**Proof for \(2\le n\le22\).** The report supplies rational probability
vectors and verifies (2) with \(C=(39/40)D_n^2\), separately for all 3,794
block positions across these 21 sizes. These are finite exact certificates,
not a numerical extrapolation. It additionally verifies the bound (4) with
rational square-root upper enclosures. Together with the tail proof, this
covers every positive integer size. \(\square\)

## 5. Finite unequal-source coverage and remaining question

The exact report covers all 20,736 source quadruples with
\(1\le a,b,c,d\le12\). Every source upper certificate passes, bounding the
entire probability simplex at that source. Of these sources, 6,095 have a
singleton input marginal and use the direct maximum-block bound.
The largest nontrivial bound in this grid occurs at \((2,2,2,2)\), with
\(U/P_*(2,2)^2\) about 0.974773. That decimal is descriptive; the report stores
the rational upper bound on its cube.

This improves the scope of the earlier finite filtration check: those checks
considered individual matched rows, columns or diagonals. This report bounds
the whole analytic entropy expression over every distribution. It does not
claim that all these expressions are independently established tensor
inequalities.

An all-size inequality
\(U(a,b,c,d)\le P_*(a,b)P_*(c,d)\) for \(a,b,c,d\ge2\), and potentially the
stronger factor \(39/40\), remains a conjecture suggested by the finite data.
The balanced proof does not establish it for unequal sources.

To improve the matrix exponent, a successful route must still force growth
beyond the feasible scalar model for every relevant character. This result
only rules out this proposed score as an escape on the stated balanced
family and on the finite unequal-source grid.

## 6. Reproduction and sources

```sh
python3 research/ai/2026-10-20-full-filtration/entropy_certificate.py \
  --max-size 12 --output results/full-filtration-2026-10-20/entropy_certificate.json
python3 -m unittest discover -s tests -p test_full_filtration_entropy.py -v
```

The certificate generator uses the standard library. Tests use the repository's
existing SymPy dependency for an independent polynomial expansion. An
exploratory floating optimizer helped choose the upper certificate; none of
its output is used as evidence for the theorem or the finite decisions.

- OpenAI, *An Upper Bound of 9/4 for the Matrix Multiplication Exponent*,
  [pinned manuscript](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/paper.pdf),
  Sections 3--5: shared-leg separation, polynomial multiplication and growth
  recurrence. The 9/4 theorem is external work.
- [First local note](../2026-10-20/research_note.md), Sections 2 and 4:
  matching profile and the determinant-filtration block family.
- [Second local note](../2026-10-20-session2/research_note.md), Section 6:
  an unfinished stronger entropy scorer. The present work does not execute or
  modify that preserved fragment.
- Christandl, Vrana and Zuiddam, *Asymptotic tensor rank of graph tensors:
  beyond matrix multiplication*, [arXiv:1609.07476v2](https://arxiv.org/pdf/1609.07476v2),
  Definition 1.1.27 and Theorem 1.1.31, printed pages 11--12: tight support and
  Strassen's scalar asymptotic-subrank formula. Inspection of those statements
  does not establish a weighted block-extraction theorem.
