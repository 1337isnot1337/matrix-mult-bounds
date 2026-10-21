# A finite parent search in the order-240 group

This is an exact finite exclusion of the explicitly generated section class.
It is not a classification of arbitrary ten-point sets, a general group-algebra
degeneration obstruction, or an exponent improvement.

Let G=SL(2,5) times C2 and Z be its four-element center. The order-48
normalization subgroup has exactly five conjugates. Sort their element lists
and select the first three, H0,H1,H2. The unique order-three subgroup in
Hi intersect H(i+1) is Ki; indices are taken modulo three. All these facts
are checked from the group table.

For leg i, partition Hi into the four right cosets of Ki Z. Pick a section
closure consisting of one left Ki orbit in each coset. Its central choices
are four elements of Z; normalize the first to identity. This leaves 4^3=64
closures. Partition each closure by left K(i-1) cosets. The maximum size of a
subset selecting at most one point from each such coset is the number of
occupied cosets. Those numbers are 7,9,10 with multiplicities 8,24,32.

Retain the closures with ten occupied cosets, choose exactly one point in
each, and quotient by independent right translation: for every chosen pivot
p compute the sorted set S p^-1 and take the lexicographically least one.
There are exactly ten canonical sections for each leg. The generator checks
that each has size ten, has no nonidentity quotient in the incoming Ki,
and has exactly the outgoing Ki as its quotient intersection with Ki Z.

All 10^3 ordered triples have injective cyclic pair maps. Every triple
nevertheless has extra group support terms whose potential rows admit a
positive integer dependence summing to zero. Such rows cannot all have
strictly positive weight. The saved circuits therefore reject all 1,000
triples in this generated class. The independent verifier recomputes the
section lists, checks each triple occurs exactly once, checks every selected
extra term by group multiplication, and sums the integer rows. It uses no
SAT solver or floating point. A negative-weight tamper control is rejected.

Discovery used the pinned optional SciPy LP routine solely to find the
circuits. The certificate stream is the accepted evidence. The related
ordinary direct-product searches, with and without projected capacities,
each ended at the 600-second limit without a pair-injective candidate; those
timeouts exclude nothing.

Reproduce the exact finite acceptance from the repository root:

```sh
python research/ai/2026-10-20-sl2-five-c2/verify_structured.py \
  results/sl2-five-c2-2026-10-20/structured-ten.json
python -m unittest discover -s tests -p test_sl2_five_c2.py -v
```

Reproduce the discovery with optional NumPy, SciPy, and python-sat installed:

```sh
python research/ai/2026-10-20-sl2-five-c2/structured_sections.py \
  --output results/local/structured-ten.json
```

The next direct search fixes one thirteen-point central projection avoiding
all involution differences. Its point list is saved separately. The pilot's
larger-size solver negatives have no proof trace and are not accepted as
independence-number bounds. A related SL(2,3) times C2 pilot for (6,6,7)
also returned untraced UNSAT; no nonexistence theorem is claimed from it.
