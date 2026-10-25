# A third universal maximal quadratic three-plane

Over every field, V(t,x,y)=[[x,0,0],[y,t,x],[0,0,y]] has coefficient
determinant txy and exact full source rank fourteen whenever txy is nonzero.
An integer left kernel and literal minor t^2*x^4*y^8 certify the result.

Its intrinsic singular section has a unique common kernel line outside the
evaluation conic. This distinguishes it from the previous chain plane;
common-kernel dimensions distinguish it from the first universal plane.
It is inclusion maximal over every field. Characteristic two therefore
has at least three inequivalent attaining three-spaces. The odd-characteristic
global maximum remains four.

Claim `AI-QUADRATIC-NONEVALUATION-THREE-001` is **proof-written-unreviewed**.
See [proof.md](proof.md) and [sources.json](sources.json). This does not
classify all attainers or improve the matrix-multiplication exponent.

From the repository root:

```sh
python research/ai/2026-10-25-quadratic-nonevaluation-three/verify.py
python -m unittest discover -s tests -p 'test_quadratic_nonevaluation_three.py' -v
```

The report is `results/quadratic-nonevaluation-three-2026-10-25/certificate.json`.
