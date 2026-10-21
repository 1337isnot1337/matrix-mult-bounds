# Exact low-coordinate freedoms of the balanced32 core

This package recovers **AI-BALANCED-SPIN-FREEDOMS-120** from the published exact construction in
`parity_balancing_spin44.md`. The earlier execution environment restored an
older filesystem snapshot; the present code and certificates recompute the
same theorem from those published maps. The positive control below is an
explicit newly reconstructed instance of the same family.

No larger matrix multiplication tensor or smaller exponent is claimed.

## Literal source spaces and exact kernels

Write the original source terms as

$$
X(i,p+q,s)Y(p,r+s,j)Z(r,i+j,q),\qquad
0\le i,p,r,j,q,s<8.
$$

The published restriction is $A(8,8)\to M(3,3,32)$. Keep its nine first
maps fixed. On the other legs use the literal coordinate spaces

$$
B_Y=\operatorname{span}\{F(p,L,j):p<2,\ L<10,\ j<8\},\qquad
B_Z=\operatorname{span}\{F(r,H,q):r<8,\ H<10,\ q<2\}.
$$

Each space has dimension 160. Contracting a free second row against the
nine first maps and all 96 third rows has rank 160 on $B_Y$. The analogous
third-row response has rank 160 on $B_Z$. Thus neither low space has a
nonzero common fiber against all 32 channels.

Retain channels $0,\ldots,26$, and delete $27,\ldots,31$. Each low response
then has rank 145. Its 15-dimensional kernel consists exactly of the 15
actual omitted rows on that leg, one for each omitted channel and each
of the three outer vertices. These are identities over $\mathbb Q$:
the verifier contracts every omitted row to zero, checks that these 15
rows are independent, and checks a nonzero 145-minor of the response.
The 160-minors establish the full-channel statements.

For the published export and this baseline deletion, the retained second
map uses 158 nonzero source coordinates and the third map uses 160. Both
ambient low spaces still have dimension 160. Dropping coordinates that
happen to be zero in a retained map would give an incorrect domain for
its possible changes. The verifier retains both complete 160-coordinate
domains and reconstructs the actual omitted rows within them. These
support counts replace a stale pre-rollback recollection of 160 and 159;
the exact response ranks and kernel theorem are unchanged.

## Coupled graphs that preserve the core

Let $r,s\in\{0,\ldots,80\}$ index arbitrary retained second and third rows.
Write $J,I\in\{0,1,2\}$ for outer labels and $d\in\{0,\ldots,4\}$ for
the omitted channel $27+d$. Every individually neutral low-coordinate
change has a unique expression

$$
Y'_r=Y_r+\sum_{J,d}A_{r,J,d}\,Y_{J,27+d},\qquad
Z'_s=Z_s+\sum_{I,d}B_{s,I,d}\,Z_{27+d,I}.
$$

Here individually neutral means that changing just that one leg preserves
the retained $M(3,3,27)$ core while the first and opposite maps remain
fixed. This definition is a restriction on the construction class.

The terms linear in either change vanish by the exact kernel identities.
The complete remaining coefficient at $(X_{I,J},Y_r,Z_s)$ is

$$
\sum_{d=0}^4 A_{r,J,d}B_{s,I,d}.
$$

Therefore the simultaneous change preserves the whole retained core if
and only if

$$
A_J B_I^{\mathsf T}=0\quad\text{for all }I,J,
\qquad A_J,B_I\in\mathbb Q^{81\times5}.
$$

Equivalently, the row spaces obtained by stacking the three $A_J$ matrices
and the three $B_I$ matrices are orthogonal in $\mathbb Q^5$. Arbitrary
outer-index mixing is allowed. This condition does not classify all
simultaneous deformations: changes whose linear and quadratic effects
cancel each other need not be individually neutral and are outside it.

## Concrete controls and replay

The positive control changes all 81 retained rows on both legs. Its second
graph uses omitted channels 0 and 1; its third graph uses 2, 3, and 4. Their outer
labels vary with each retained channel. The two graph row spaces are
orthogonal, and a separate contraction of all 262,144 original source terms
checks all 59,049 output coefficients: exactly 243 are one and every other
coefficient is zero. This verifies the actual source maps in addition to
the smaller graph identity.

The negative control uses the same omitted channel on both legs. Its
graph residual has coefficient one at $(7,1,2)$, which is outside the
target support. Complete source replay rejects it. The focused tests also
reject a response certificate with duplicate minor columns and an omitted
kernel basis with a zero vector.

The accepted verifier imports only the Python standard library. Numerical
code may discover minor indices, but acceptance recomputes their entries
from the saved rational maps and checks their ranks modulo 1,000,000,007.
The omitted-row zero identities use exact integers, and the matching
dimension bounds prove the stated ranks over $\mathbb Q$.

## Reusable interfaces

`low_domains()` returns both ordered 160-coordinate domains. `parse_full`
returns the three sparse numerator maps and their denominators.
`low_responses(maps)` contracts the actual full 32 maps; `trim_response`
retains the 27 baseline channels. `select_rows(entries, channels)` also
supports other channel selections. `omitted_rows` and `apply_graph` use
the baseline deletion 27 through31. `graph_residual(a,b)` accepts sparse
integer entries `[retained_row, omitted_outer_label, omitted_channel, value]`.
The proof permits rational graph coefficients as well.

The pre-rollback proof was checked by a second agent in this generating
session. The reconstruction is available for the same-session replay;
no external independent review or formalization is claimed.
