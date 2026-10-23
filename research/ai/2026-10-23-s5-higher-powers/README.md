# Higher powers cannot rescue the full S5 degree-majorant cover method

The [written, unreviewed proof](proof.md) supplies an explicit matching
lower bound on coordinate covers of the prior S5 degree majorant. For
every source power n>=36, all such covers cost too much to exclude any
of PR111's eleven remaining single targets, even allowing arbitrary
nonmonotone sets and different choices on all three legs.

This is a limitation of the full degree-majorant cover method. It is not
a lower bound on the actual source's slice rank. Other support, bases,
decompositions and powers below 36 remain separate questions. No target
construction, optimal-cover theorem or smaller exponent is established.

The certificate checks 72 induction seeds, 36 per source, and two boundary
controls. A proved concatenation injection extends those exact integer
checks to every n>=36. The prior algebra/cover certificate is replayed
with its source pins and attribution intact.

From the repository root with the maintained requirements installed:

```sh
python research/ai/2026-10-23-s5-higher-powers/bounds.py --output results/s5-higher-powers-2026-10-23/certificate.json
python research/ai/2026-10-23-s5-higher-powers/verify.py --certificate results/s5-higher-powers-2026-10-23/certificate.json --output results/s5-higher-powers-2026-10-23/verification.json
python -m unittest discover -s tests -p test_s5_higher_powers.py -v
python -m unittest discover -s tests -v
python tools/replay.py
```

This continuation follows PR111. PR140's finite monotone cube census is
a separate result. The initial [question](QUESTION.md) records that scope.
