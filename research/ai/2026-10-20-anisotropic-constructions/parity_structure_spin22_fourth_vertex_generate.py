"""Regenerate the recovered exact fourth-vertex package; standard library only."""

import json
from parity_structure_spin22_fourth_vertex import (
    DIRECTORY, WITNESS, MAPS, MINORS, lift, check, response_matrices, make_minor,
)


ENTRIES = [
    [(0,3,2),(0,11,2),(1,2,1),(1,5,-1),(1,10,1),(2,4,2),
     (3,2,1),(3,5,1),(3,10,1),(4,1,4),(5,0,2),(5,11,2),
     (6,10,-4),(7,0,2),(7,11,-2),(8,7,2),(9,1,-1),(9,6,1),
     (9,9,-1),(10,0,2),(10,8,2),(11,1,1),(11,6,1),(11,9,1)],
    [(0,1,-1),(0,2,1),(0,4,-1),(1,5,1),(2,0,1),(2,1,-1),
     (2,7,1),(2,8,-1),(2,10,1),(3,3,1),(3,4,-1),(3,11,-1),
     (4,6,1),(4,7,-1),(5,9,1),(5,10,-1),(6,0,1),(6,1,-1),
     (6,7,-1),(6,8,1),(6,10,-1),(7,3,1),(7,4,-1),(7,11,1)],
    [(0,6,2),(1,6,2),(1,7,2),(1,8,2),(1,9,2),(1,10,2),
     (2,0,1),(2,6,-1),(2,7,-1),(2,9,-1),(3,0,1),(3,1,1),
     (3,2,1),(3,3,1),(3,4,1),(3,11,-1),(4,0,2),(4,1,2),
     (4,3,2),(5,5,2)],
]


def main():
    witness = {"claim_id": "AI-SPIN-FOURTH-VERTEX-122", "source": [2,2], "target": [3,4,2],
               "source_coordinate_order": ["(i*3+k)*2+s", "(p*3+L)*2+j", "(q*2+r)*3+H"],
               "target_coordinate_order": ["4*I+J", "2*J+alpha", "2*I+alpha"],
               "new_exponent_established": False,
               "maps": {name: {"shape": [rows,12], "denominator": denominator,
                                "entries": [list(e) for e in entries]}
                        for name, rows, denominator, entries in
                        zip("XYZ", (12,8,6), (2,1,2), ENTRIES)}}
    check(witness, tiny=True)
    DIRECTORY.mkdir(parents=True, exist_ok=True)
    WITNESS.write_text(json.dumps(witness, indent=2)+"\n")
    exported = {"claim_id": "AI-SPIN-FOURTH-VERTEX-122", "new_exponent_established": False, "targets": {}}
    minors = {"prime": 65521, "targets": {}}
    for middle in (32,28):
        key = str(middle)
        exported["targets"][key] = lift(witness,4,range(middle))
        responses, _, _, _ = response_matrices(exported["targets"][key])
        minors["targets"][key] = {name: make_minor(response) for name, response in zip("XYZ", responses)}
        print(key, [len(r) for r in responses],
              [minors["targets"][key][name]["determinant_mod_prime"] for name in "XYZ"], flush=True)
    MAPS.write_text(json.dumps(exported, separators=(",", ":"))+"\n")
    MINORS.write_text(json.dumps(minors, separators=(",", ":"))+"\n")


if __name__ == "__main__":
    main()
