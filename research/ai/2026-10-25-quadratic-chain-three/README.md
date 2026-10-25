# A second universal maximal quadratic three-plane

Over every field, N(t,x,y)=[[t,x,0],[0,t,x],[0,y,0]] has coefficient
determinant -txy and full source rank fourteen whenever txy is nonzero.
Its integer source kernel and minor -t^2*x^7*y^5 are exact certificates.

This three-plane is inclusion maximal and inequivalent to the previous
universal three-plane. The intrinsic singular section has common-kernel
dimensions (right,left)=(1,0), versus (1,1) for the earlier example.
In characteristic two this gives at least two inequivalent attainers.
Outside characteristic two the global maximum remains four.

Claim `AI-QUADRATIC-CHAIN-THREE-001` is **proof-written-unreviewed**.
See [proof.md](proof.md) and [sources.json](sources.json). This is not a
complete characteristic-two classification or an exponent improvement.

From the repository root:

```sh
python research/ai/2026-10-25-quadratic-chain-three/verify.py
python -m unittest discover -s tests -p 'test_quadratic_chain_three.py' -v
```

The saved report is `results/quadratic-chain-three-2026-10-25/certificate.json`.
