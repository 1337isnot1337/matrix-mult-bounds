# Optional finite weight search

The two retained logs are completed discovery runs for central ranks one
and two. Each tests 5,400 integer choices per block word: u=1..3,
v=-u..u, q1=0..4, q2=q1..4 and h=1..24. The hardcoded type counts and
support are from the freshly replayed full source. The two common-cover
bits were tested as additional weights; every selected best witness uses
q1=q2=0. There is no global optimality claim.

From the repository root:

```sh
g++ -O3 -std=c++17 research/ai/2026-10-23-s5-peirce-covers/discovery/weighted_search.cpp -o /tmp/s5-peirce-weights
/tmp/s5-peirce-weights 1
/tmp/s5-peirce-weights 2
```

The search is optional and is not part of certificate acceptance. The
maintained exporter and separate verifier replay the actual source and
check each chosen witness using exact integer arithmetic. All limitations
in the parent proof apply.
