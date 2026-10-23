# Full-source coordinate construction search

This optional discovery program leaves all three SL(2,F8) vertex families
free in the full504-element group. Its selected target is M(18,18,25).
It uses every minimal subgroup-averaging cut from PR175, rather than the
excluded fixed-full-D18 frame. PR84's local packet assembly is separate.

The three pair maps are enforced by mutually exclusive inverse-paired
left-difference variables. Each candidate is independently checked by
`pair_map`. Every proposed potential is accepted only after complete
integer group-support replay. A rejected candidate needs an exact
positive-integer Farkas circuit before it can supply a blocking clause.
A timeout or solver-reported UNSAT without a checked proof is not a
nonexistence certificate.

Independent right translations normalize an identity in each vertex set:
(S,T,U)->(Sa,Tb,Uc) changes pair labels by a^-1 X b, b^-1 Y c, c^-1 Z a,
which preserves all group-support equations and the same vertex weights.
Simultaneous conjugation also preserves them. Thus one nonidentity first-
set point may lie among the eight canonical nonidentity class representatives.
The complete conjugate-subgroup cut family respects both normalizations.

The saved M(18,1,1) control has18 intended coefficients and no extra
supported terms. It is only a control, not an improving target.

Run optional discovery in an environment with PySAT, NumPy and SciPy:

```sh
python research/ai/2026-10-23-sl2-f8-native-all-cuts/native_search.py --control --seconds 10 --max-models 1 --output results/local/f8-native-control.json
python research/ai/2026-10-23-sl2-f8-native-all-cuts/native_search.py --seconds 600 --max-models 100 --output results/local/f8-native-pilot.json
```

Replay exact evidence without the optional solver dependencies:

```sh
python research/ai/2026-10-23-sl2-f8-native-all-cuts/native_search.py --verify results/sl2-f8-native-all-cuts-2026-10-23/control.json
python -m unittest discover -s tests -p test_sl2_f8_native_all_cuts.py -v
```

The new full-source pilot is still running at this checkpoint. No result
or sourcewide exclusion is claimed. Source, subgroup-catalog and existing
lazy-LP/Farkas machinery retain their credits and byte pins in sources.json.
No exponent improvement is established.
