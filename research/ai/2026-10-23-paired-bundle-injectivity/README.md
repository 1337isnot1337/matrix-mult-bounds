# Paired-source long-leg Koszul maps

The [written proof](proof.md) shows that, over every field and for every
a>=2, both long-leg Koszul maps of P_a, with the short leg as input,
are injective for 0<=p<=a(a-1). Their rank in this interval is
a^2 binom(a(2a-1),p). The proof combines a complete symmetric Hankel
calculation with an explicit quotient bundle on the projective line.
It also proves full row rank for a(2a-1)-a<=p<=a(2a-1), and gives
an explicit all-degree upper bound on the kernel dimension.

This closes those degrees as a source of additional target exclusions.
For the 28 short-leg survivors through a16, a new long-leg exclusion
would require p in [183,363], [211,419], [241,479] at a14,15,16.
The all-degree formula bounds source rank from below; it is not itself
a degeneration obstruction. No intermediate-degree target comparison
or target construction is supplied. The exponent remains unimproved.

Exact controls replay the literal source and its long-leg symmetry,
40 Hankel ranks through a6,18 paired full-column cases and7 full-row
cases. At a2,p3, ten independent integer kernel vectors and a modular
rank70 lower bound certify the exact complex rank70, beyond the proved
interval. This prevents treating full column rank in every degree as a
consequence of the theorem.
The kernel dimension10 also differs from the associated-graded section
sum12, so the latter is retained as a bound.

Run from the repository root:

```sh
python research/ai/2026-10-23-paired-bundle-injectivity/verify.py --verify results/paired-bundle-injectivity-2026-10-23/certificate.json
python -m unittest discover -s tests -p 'test_paired_bundle_injectivity.py' -v
```

The verifier uses the standard library. The all-size proof is written and
unreviewed, with no formalization. Finite coefficient checks do not prove
the universal argument. Source conventions, original frontier and basic
line-bundle fact are credited in sources.json and the proof.
