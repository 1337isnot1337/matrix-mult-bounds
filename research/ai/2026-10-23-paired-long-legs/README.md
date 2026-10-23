# Paired-source long-leg Koszul maps

The [written proof](proof.md) shows that, over every field and for every
a>=2, both long-leg Koszul maps of P_a, with the short leg as input,
are injective for 0<=p<=a(a-1). Their rank in this interval is
a^2 binom(a(2a-1),p). The proof combines a complete symmetric Hankel
calculation with an explicit quotient bundle on the projective line.

This closes those degrees as a source of additional target exclusions.
For the 28 short-leg survivors through a16, a new long-leg exclusion
would require p>=183,211,241 at a14,15,16. No higher-degree comparison
or target construction is supplied. The exponent remains unimproved.

Exact controls replay the literal source and its long-leg symmetry, the
Hankel ranks in all degrees through a6, and finite paired injectivity
examples. At a2,p3, ten independent integer kernel vectors and a modular
rank70 lower bound certify the exact complex rank70, beyond the proved
interval. This prevents treating full column rank in every degree as a
consequence of the theorem.

Run from the repository root:

```sh
python research/ai/2026-10-23-paired-long-legs/verify.py --verify results/paired-long-legs-2026-10-23/certificate.json
python -m unittest discover -s tests -p 'test_paired_long_legs.py' -v
```

The verifier uses the standard library. The all-size proof is written and
unreviewed, with no formalization. Finite coefficient checks do not prove
the universal argument. Source conventions, original frontier and basic
line-bundle fact are credited in sources.json and the proof.
