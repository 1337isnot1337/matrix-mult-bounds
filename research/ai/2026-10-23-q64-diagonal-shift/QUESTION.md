# The correction rank of a diagonal-shift restriction

October 23, 2026. Owner-directed Codex research from the open fixed-width
paired-source direction.

Question: for the explicit maps

\[
A_{p,q}\mapsto\sum_{\substack{0\le t<4\\p+t,q+t<n}}a_{q+t,p+t},\qquad
B_{y,s}\mapsto\begin{cases}b_{s,y}&s<n,\\0&s\ge n,\end{cases}\qquad
C_{z,v}\mapsto\begin{cases}c_{v,z}&z<n,\\0&z\ge n,\end{cases}
\]

from the maintained source \(Q(n,4)\), determine the border rank required
to correct the restricted tensor to \(M(n,4,n)\).

Result: the correction has first-leg flattening rank exactly \(n^2\),
proved by projecting two output blocks and reducing each diagonal block
modulo two. Thus this fixed map cannot use an auxiliary correction of
border rank \(O(n)\).

The result is scoped to these maps. General restrictions of \(Q(n,4)\),
other source families, and the exponent question remain open. No smaller
exponent is established.
