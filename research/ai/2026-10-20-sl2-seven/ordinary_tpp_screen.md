# Ordinary TPP is excluded; weighted degeneration is still open

Blasiak, Cohn, Grochow, Pratt and Umans,
[*Matrix Multiplication via Matrix Groups*, ITCS 2023](https://drops.dagstuhl.de/storage/00lipics/lipics-vol251-itcs2023/LIPIcs.ITCS.2023.19/LIPIcs.ITCS.2023.19.pdf),
Theorem 3.2, bound an ordinary triple-product-property triple by

    |S|*|T|*|U| <= |G| + sqrt(|G|^3/n(G)),

where n(G) is the smallest irreducible degree greater than one. The theorem
and its Fourier proof were inspected in the proceedings version, pages 5--6.
It is external prior work, not a new theorem of this repository.

Our exact degree calculation gives n(SL(2,7))=3. The target volume 4352
violates the bound, since

    3*(4352-336)^2 = 48,384,768 > 37,933,056 = 336^3.

Thus an ordinary TPP triple of the selected sizes is impossible. Any accepted
coordinate-potential construction must genuinely delete unwanted group terms.

This theorem does not state an exclusion of weighted degenerations. Its
Fourier estimate uses unweighted indicators and positive semidefinite
autocorrelations. Opposite vertex weights do not give those autocorrelations.
Also, passing to tensor powers does not retain this finite-volume barrier:
n(G^N)=3, so its N-th-root upper bound tends to |G|^(3/2), above our target.
We therefore retain the weighted construction question as open. No smaller
matrix-multiplication exponent follows from this screen.
