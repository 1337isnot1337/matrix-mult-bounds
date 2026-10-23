# Elementary arbitrary-biform rank gap

The [written proof](proof.md) gives an elementary alternative to the
existing vector-bundle proof of the crossed biform block gap. For
2<=a<=b over characteristic zero, a nonzero biform f has matrix rank ab
if it is separable, and at least ab+a otherwise.

The proof preserves the literal crossed coefficient matrix under affine
translation. At a suitable point of a mixed irreducible factor of
multiplicity e, simultaneous scaling limits to a power of a mixed linear
form. Explicit binomial minors prove the exact formula

    rank R((alpha*x+beta*z)^e)=a(b+e),  1<=e<a, alpha*beta != 0.

Consequently such a repeated mixed factor forces rank R(f)>=ab+ae.
The [linear-factor-power corollary](linear_factor_powers.md) gives exact
rank a(b+e) whenever the remaining mixed part is h^e with h irreducible
and linear in x, allowing arbitrary admissible univariate factors.
The nonintersecting-path argument proving the integer minors is classical
and retains Lindstrom/Gessel-Viennot attribution; its required special
case is fully reproduced. No vector-bundle theorem is imported here.

The existing source lemma and all applications retain their original
credit and ledger entries. This alternative proof is registered
separately. No historical priority, independent mathematical review,
formalization, target construction or exponent improvement is claimed.
The power formula is not asserted in positive characteristic: the
characteristic-two a=b=3,e=2 control has rank14 rather than15.

```sh
python research/ai/2026-10-23-elementary-biform-gap/verify.py
python -m unittest discover -s tests -p 'test_elementary_biform_gap.py' -v
```

Acceptance replays45 power cases at a=2,...,6 and b=a,a+1,a+2,
with all525 positive integer block minors,45 active-column upper covers,
20 affine/scaling identities and two local byte pins. The tests use
separate symbolic polynomial extraction, determinant and rank backends,
including arbitrary symbolic coefficients in the affine identity,
repeated mixed-factor limits, separable sharpness and corrupted evidence.
These are finite controls for the written all-size proof.
