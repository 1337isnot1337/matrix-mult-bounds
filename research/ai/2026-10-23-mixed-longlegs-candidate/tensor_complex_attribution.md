# Attribution of the output-leg rank calculation

The relevant primary source is Christine Berkesch Zamaere, Daniel Erman,
Manoj Kummini, and Steven V Sam, *Tensor complexes: Multilinear free
resolutions constructed from higher tensors*, JEMS 15 (2013), 2257–2295,
[DOI 10.4171/JEMS/421](https://doi.org/10.4171/JEMS/421).
The inspected [publisher PDF](https://ems.press/content/serial-article-files/31930?nt=1)
contains Definition 5.1, Theorem 5.3, and Proposition 8.1. A fixed preprint
version is [arXiv:1101.4604v5](https://arxiv.org/abs/1101.4604v5).

Their tensor complexes resolve modules supported where the contraction
kernel meets the Segre variety. The following is our explicit
specialization, over the complex numbers.

For dimensions (a,N,M), M>=N+a-1, and a-1<=p<=M-N, use their format
M×(a,N) and weight

\[
w=(0,p-a,p+1).
\]

The excluded intervals are disjoint and contained in [0,M]:

\[
[p-a+1,p-1],\qquad[p+2,p+N].
\]

Up to one common determinant twist, the adjacent terms are

\[
\Lambda^{p+1}C^*\otimes A^*
\longrightarrow\Lambda^pC^*\otimes B,
\]

with differential (K_C^p)*. A zero-free tensor lies outside the stated
support. Localizing there gives a bounded exact free complex; successive
splittings preserve exactness after specialization. Its rank calculation
gives

\[
\begin{aligned}
\dim\ker K_C^p
&=\sum_{\ell=0}^{p-a}(-1)^{p-a-\ell}
\binom M\ell\binom{p-\ell-1}{a-1}
\binom{N+p-\ell}{N-1}\\
&=\sum_{j=a+1}^{p+1}(-1)^{j-a-1}
\binom{N+j-1}{j}\binom M{p+1-j}\binom{j-2}{a-1}.
\end{aligned}
\]

The reindexing is j=p+1-ell. Thus
[source_c_koszul.md](source_c_koszul.md) is a local self-contained
specialization and derivation of standard tensor-complex machinery.
It also supplies the endpoint ranges, padding identity, and application.
No historical novelty for the rank formula is claimed. Source details
are in [tensor_complex_sources.json](tensor_complex_sources.json).
