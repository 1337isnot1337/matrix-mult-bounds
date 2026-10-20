# Problem and conventions

## Target

The default target is exact multiplication of two $n\times n$ matrices over $\mathbb C$. The computation model uses division-free scalar addition, subtraction, and multiplication, each at cost one. Input loads and field constants are free. These conventions follow [the target page](https://bigospeedrun.com/matrix-multiplication) and [OAI26](literature.md#oai26).

The assertion $\omega\le\tau$ means that, for every fixed $\varepsilon>0$, there exists $C_\varepsilon>0$ such that every positive dimension admits a correct circuit of cost at most $C_\varepsilon n^{\tau+\varepsilon}$. The circuit can depend on $n$ and $\varepsilon$, but it must multiply every input pair. This does not assert an $O(n^\tau)$ bound without exponent slack.

A result over all fields includes the complex target. A result only over a finite field does not automatically include it. Arithmetic operation counts are not bit complexity or measured hardware runtime.

## Tensors

The matrix multiplication tensor is

$$T_n=\sum_{i,j,k=1}^n x_{ij}y_{jk}z_{ki}.$$

A rank decomposition gives a bilinear algorithm. A restriction applies independent linear maps to the three tensor legs. A degeneration retains a leading coefficient of a parameterized family after suitable substitutions. An asymptotic conversion must account for interpolation and all auxiliary factors. [BINI80, SCH81, OAI26 in the bibliography](literature.md)

The convolution tensor used here is

$$C(a,b)=\sum_{i=0}^{a-1}\sum_{j=0}^{b-1}x_i y_j z_{i+j}.$$

A full direct sum has independent coordinates on all three legs. A matched sum with a shared leg has independence on only two legs. Confusing these constructions invalidates exponent arguments.

## Spectral notation

For an actual tensor character $\lambda$, let $p_X,p_Y,p_Z$ be its oriented dot-product exponents. Set $t=(p_X+p_Y+p_Z)/3$. In this notation $t$ is a normalized spectral parameter, not the matrix multiplication exponent. The character takes value $n^{3t}$ on $T_n$. [OAI26](literature.md#oai26)

The scalar relaxation abstracts properties of a symmetrized character profile. A feasible scalar profile need not extend to a character. The explicit local profile $P_*$ has no demonstrated character realization.

## Record requirements

A new numerical upper bound needs a proof of the complete asymptotic implication in the chosen model. It must retain the field, quantifiers, input correctness, and operation costs. A finite rank improvement, a numerical fit, or a violation of $P_*$ is not sufficient by itself.

Over finite fields, equality of functions does not imply equality of formal polynomials. Contributions involving finite fields must state which notion their certificate proves. [NAVOT26 and FILMUS26](literature.md)
