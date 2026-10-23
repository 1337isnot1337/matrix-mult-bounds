# All independent coordinate compressions of the A4 limit

The [finite proof](proof.md), claim `AI-A4-INDEPENDENT-COORDINATE-004`,
extends the earlier principal-coordinate result to independently chosen
input and output deletions. All 142,884 two-row / two-column deletions
of the reduced 46-dimensional outer space have image dimension at least
40 over C. Two exact integer kernel witnesses attain 40.

The established bottom-left kernel reduction then bounds every full
112-dimensional independent coordinate compression by a loss of at
most six directions. The full target requires a loss of at least nine,
so this entire coordinate class is excluded. The separate
[universal compression theorem](../2026-10-23-a4-compression-algebra/proof.md)
now also excludes arbitrary constant flags in this fixed family, with
outer image dimension at least 38. This finite package retains its
sharper coordinate bound and exact equality witnesses. Moving
compressions and different singular paths remain open.

From the repository root:

```sh
python research/ai/2026-10-23-a4-coordinate-compressions/verify.py
python -m unittest discover -s tests -p 'test_a4_coordinate_compressions.py' -v
```

The complete census is recomputed by acceptance; the small retained
certificate contains its histogram and the two exact six-dimensional
kernel witnesses. The verifier imports only the pinned literal-source
reconstruction, rebuilds E directly, and performs its own modular
elimination. It does not import the census discovery program.

The [validation receipt](../../../results/a4-coordinate-compressions-2026-10-23/validation.json)
records four focused tests, including a complete fresh acceptance of all
142,884 pairs and both sharpness witnesses, plus 18 repository checks.
It pins the exact checked files and identifies the earlier full-suite
checkpoint separately; no duplicate full-suite run is claimed.

This is a written, unreviewed, finite computer-assisted result. It
does not construct target maps or improve the matrix exponent.
