# Nonsplit cube covers with several degrees

October 23, 2026. `EXP-NONSPLIT-VECTOR-COVERS-001` is a finite experiment.
There is no improvement of the saved cube bound 6155844, no certified
optimality of the coordinate-cover class, and no exponent improvement.

The question was whether retaining several degrees, rather than replacing
them with a weighted scalar degree, improves the fixed-basis finite cube
cover for SL(2,F5) x C2. This continues the source certificates in PR102;
it does not duplicate their construction or change their proof status.

Separate dense replay checks the rank-120 F4 basis and all 1728000 source
coefficients. It finds precisely the 95 principal degree triples
`(d1,d2,d3)` with nonnegative entries and even sum at most eight. It also
checks that the saved 22-coordinate principal cover is the same on each
leg and meets every principal term. The source bytes are SHA-256 pinned
to commit `6cd7f3a1fc90820c135505b882a614cb62a025d5`.

For a cube word with j principal factors, `cover_model.py` retains the
principal degree p, matrix-central degree b and extra-central degree e.
The one-leg class multiplicities are the coefficients of

    P(u)^j [16(1+v)]^(3-j) (1+w)^3,
    P(u) = 9+8u+10u^2+8u^3+18u^4+8u^5+10u^6+8u^7+9u^8.

A cover is valid if it meets every class triple with principal total at
most 8j, matrix-central total at most 3-j and extra-central total at most
three. The parity variant additionally requires the principal total to
be even. Tensor products preserve this condition. Checking this safe
superset of source support gives a finite slice decomposition. No
submultiplicativity of slice rank is used.

| j | Classes per leg | Triples without parity | Triples with parity | Best saved cost per word |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 16 | 400 | 400 | 147456 |
| 1 | 108 | 33000 | 19000 | 384768 |
| 2 | 136 | 77520 | 42000 | 898096 |
| 3 | 100 | 58500 | 30940 | 2159796 |

The seven numerical runs used 120 seconds per block without parity and
180 seconds per block with parity (j=1,2,3). All returned covers replay
with exact integer arithmetic at the preceding costs. Some solver runs
reported numerical optimality; two controls reached their time limit.
Neither status is an independently checked optimality proof. Summing the
four costs with binomial word multiplicities still gives 6155844.

The second experiment adds q=0 on the 22 selected principal coordinates
and q=1 elsewhere. Every source term has total q at most two. The exact
bounded search uses principal degree `s*p+v*q`, matrix degree `a*b`, and
extra-central degree `h*e`. It enumerates primitive integer weights with
0<=s,v<=6, s+v>0 when j>0, and 1<=a,h<=6 when their factors occur.
Absent factors have weight zero. It checks every integer cutoff triple
of sum `j*(8s+2v)+(3-j)*a+3h-2`, modulo leg permutation. A cutoff may be
-1, giving an empty slice set. All 3372 weight vectors were evaluated
exactly; none improves the saved bound. This excludes improvement only
inside that explicit finite weight census, not beyond it.

Run offline acceptance from the repository root:

```sh
python research/ai/2026-10-23-nonsplit-vector-covers/verify.py --output results/local/nonsplit-vector-verification.json
python -m unittest discover -s tests -p test_nonsplit_vector_covers.py -v
```

The verifier uses only the standard library. It imports the pinned source
verifier, reconstructs the original group tensor, checks parity and cover
membership, replays all seven proposed class covers, and recomputes the
complete bounded weight census. Numerical discovery additionally needs
NumPy/SciPy; these are optional and are not acceptance dependencies:

```sh
python research/ai/2026-10-23-nonsplit-vector-covers/discover.py --principal-factors 2 --seconds 180 --even-principal --output results/local/vector-discovery.json
python research/ai/2026-10-23-nonsplit-vector-covers/weighted_discovery.py --source-certificate results/sl2-finite-slices-2026-10-21/cover-certificate.json --limit 6 --output results/local/vector-weights.json
```

These outcomes do not justify repeating the same weight grid. A further
attempt needs additional basis information, another basis, a different
source power, or a different construction mechanism. All original source
and finite-characteristic limitations remain in force. There is no
independent mathematical review or formalization.
