# Former ordinary target, now excluded

October 21, 2026. The later `two_ruling_cap.md` excludes this ordinary
restriction. General singular degenerations are not excluded. The earlier
necessary tests and conditional comparison below are retained as history.
No improved exponent is claimed.

The ordinary target A(8,9) -> M30 passed the earlier necessary tests.
Enumerating1<=n<=floor(sqrt(1152))=33, it is the only single square target
that passes both the exact9/4 score gate and those necessary tests. It avoids
the extra M3 block that the bundle/stratum argument has excluded. The source
has1152 coordinates per leg; the target has900. Each output kernel has dimension252.
A rank-three parameter slice therefore lifts to rank at most594, with the
full-symbol crossed-rank upper bound26. That older rank-three dimension comparison alone did not exclude it.
The newer rank-two, two-ruling argument does exclude ordinary maps.

The historical conditional comparison was

    omega <= 3 log(49)/log(180) = approximately2.2483261906.

The purely conditional rational consequence omega<2249/1000 has the exact
integer certificate 49^3000<180^2249. The missing premise is the entire tensor
restriction. M30 has27000 required nonzero coefficients; all off-target
coefficients must also vanish. Checking just the required coefficients or a
floating residual cannot certify this premise.

## A coordinate-selection ansatz cannot work

In the reversed-long-coordinate conventions, source support consists of
three integer vectors x,y,z whose coordinatewise sum is (m-1,m-1,m-1), where
m=a+b-1. The coordinate boxes in each scalar direction have lengths a,b,m
in some order.

Suppose each target matrix unit is assigned one source coordinate, with a
nonzero scalar. The desired triangles require x_(uv)+y_(vw)+z_(wu) to be
constant for every u,v,w. Taking differences forces vertex potentials

    x_(uv)=A_u+B_v, y_(vw)=-B_v+C_w, z_(wu)=-C_w-A_u+constant.

The potentials can be chosen in translates of the integer lattice. An
unwanted source triangle would correspond exactly to

    A_u+B_v+C_w=A_(u')+B_(v')+C_(w').

Thus all n^3 potential sums must be distinct for a target M_n.
For any scalar coordinate, write alpha,beta,gamma for the widths of the
three potential sets. Because all pair combinations occur, the three box
constraints imply that their pairwise sums are at most a-1,b-1,m-1, in some
order. Adding gives

    2(alpha+beta+gamma)<=a+b+m-3=2m-2.

All sums therefore lie in a translated integer interval with at most m
positions in each of the three coordinates. Hence n^3<=m^3 and n<=m.
For A(8,9), m=16, so a one-source-coordinate-per-target-variable construction
of M30 is impossible.

This argument does not cover a target variable represented by a linear
combination of source coordinates, even if that combination is sparse.
Such combinations can create cancellations and are exactly what the next
construction attempt must retain. The argument is an elementary abelian
vertex-potential counting obstruction; no historical novelty is claimed.
