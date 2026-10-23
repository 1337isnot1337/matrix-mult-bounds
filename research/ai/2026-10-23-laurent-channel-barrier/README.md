# Laurent cancellation cannot evade a common channel-rank deficit

The [proof](proof.md) extends the ordinary channel obstructions in
PR157, PR173 and PR179 to formal Laurent degenerations. It permits
arbitrary pole orders, arbitrary first-leg mixing, and arbitrary maps
on an auxiliary tensor. The source and auxiliary contributions can have
poles that cancel only in their sum.

If the good source contractions have common generic channel rank below
the target middle width, the auxiliary tensor must have first flattening
rank at least the dimension of the good contraction subspace. A primitive
vector in the auxiliary kernel makes the source contraction regular
before its rank equations are specialized.

For the stated paired maps and near-full target M(l,h,r), this gives

    border_rank(R) >= (l*r - n^2 + g_B*g_C)_+,
    g_B = (r-m+1-2D-m*e_B)_+,
    g_C = (l-m+1-2D-m*e_C)_+.

The [border-rank follow-up](rank_margin.md) sharpens the auxiliary tensor
cost when the good contraction subspace is nonzero. If its dimension is
d>=1 and its generic channel rank is at most rho<h, then

    border_rank(R) >= d+h-rho-1.

The first-flattening lower bound remains d. In the paired application,
one may use `d=(l*r-n^2+g_B*g_C)_+` and `rho=a*b`, provided d>=1.
For d=0 this argument supplies no additional bound. At fixed h the extra
term is constant, so the asymptotic conclusion below is unchanged.

Here l,r<=n; m is the source width; h>=2 is the target width; D is the
stencil half-width; and e_B,e_C count exceptional source columns.
The precise common window/profile hypothesis is in the proof. Ranks
must be bounded over K((t)), not only in the leading coefficient.

At fixed m,h, outer ratios tending to one, and sublinear bandwidth and
exception counts, the bound is n^2-o(n^2). This excludes subquadratic
repair within this formal map class. Full generic channel rank and
general nonlocal maps remain open. No multiplication target is built,
and the matrix multiplication exponent is unchanged.

## Exact controls

```sh
python -S research/ai/2026-10-23-laurent-channel-barrier/verify.py --output results/laurent-channel-barrier-2026-10-23/verification.json
python -m unittest discover -s tests -p test_laurent_channel_barrier.py -v
```

The standard-library verifier compares literal native-source expansions
with the separate channel factorization in five finite cases. Every
Laurent coefficient, including poles, is retained in those identities.
It also computes complete residual flattening ranks at nonzero parameter
values over F3 and F101. These are exact finite controls, not a proof of
the general formal statement.

A separate exact example has a moving two-dimensional contraction
subspace and genuine source/auxiliary pole cancellation. Its auxiliary
first flattening has rank two. Removing one auxiliary direction causes
the required channel-rank condition to fail. Another control exhibits
the invalid raw-constant-coefficient shortcut explicitly.

The refinement has six additional controls:

```sh
python -S research/ai/2026-10-23-laurent-channel-barrier/rank_margin.py --output results/laurent-channel-barrier-2026-10-23/rank-margin-controls.json
python -m unittest discover -s tests -p test_laurent_rank_margin.py -v
```

They verify a full rank-one channel encoding, sharp one-dimensional
examples whose source and auxiliary poles cancel, and the strict
parameter-order choice needed for auxiliary border approximations.
The paired control separates a first-flattening lower bound 16 from a
border-rank lower bound 18. The
[original validation receipt](../../../results/laurent-channel-barrier-2026-10-23/VALIDATION.md)
records 904 passed tests and all five archive replays at the preceding
proof tree. The follow-up receipt states its own coverage.

All three claims remain written and unreviewed. The generating session's
proof checks are not independent mathematical review or a proof assistant
build. Prior ordinary factorizations retain credit and are pinned in
[sources.json](sources.json); they are not runtime dependencies. The
standard substitution method, rank-one-curve description of border rank,
and exact preceding-file dependencies are attributed in
[rank-margin-sources.json](rank-margin-sources.json).
