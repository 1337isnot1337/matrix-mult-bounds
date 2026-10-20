"""Bounded direct-product search using pinned SAT and integer acceptance."""
import argparse
from itertools import combinations
import json
from pathlib import Path
import sys

from pysat.card import CardEnc, EncType
from source_data import group, subgroup_certificate, SEVEN

sys.path.insert(0, str(SEVEN))
sys.path.insert(0, str(SEVEN/'imported'))
from central_involution import forced_center_pair_exclusions
import search as upstream


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seconds', type=float, default=600)
    parser.add_argument('--seed', type=int, default=20261323)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    G = group()
    cert = subgroup_certificate(G)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.with_name('subgroup-certificate.json').write_text(json.dumps(cert, indent=2)+'\n')
    original_build = upstream.build_solver

    def build(source, shape, seed, engine):
        solver, members, metadata = original_build(source, shape, seed, engine)
        top = metadata['variables']
        presence = []
        for f in range(3):
            row = []
            for orbit in cert['central_orbits']:
                top += 1
                variable = top
                row.append(variable)
                solver.add_clause([-variable]+[members[f][g] for g in orbit])
                for g in orbit:
                    solver.add_clause([-members[f][g], variable])
                for g, h in combinations(orbit, 2):
                    solver.add_clause([-members[f][g], -members[f][h]])
            card = CardEnc.equals(row, shape[f], top_id=top, encoding=EncType.seqcounter)
            solver.append_formula(card.clauses)
            top = card.nv
            presence.append(row)
        H = set(cert['members'])
        fiber = [i for i, orbit in enumerate(cert['central_orbits']) if set(orbit) <= H]
        if len(fiber) != 12:
            raise ArithmeticError('wrong quotient subgroup')
        for f in range(3):
            card = CardEnc.atleast([presence[f][i] for i in fiber], (shape[f]+4)//5,
                                   top_id=top, encoding=EncType.seqcounter)
            solver.append_formula(card.clauses)
            top = card.nv
        exclusions = forced_center_pair_exclusions(source, shape)
        if len(exclusions) != 9:
            raise ArithmeticError('central pair exclusion premise not met')
        metadata['variables_after_center_and_subgroup'] = top
        metadata['central_orbits'] = 60
        metadata['central_involutions'] = 3
        metadata['center_free_orbit_constraints_justified'] = True
        metadata['identity_subgroup_lower'] = [(s+4)//5 for s in shape]
        metadata['normalization_subgroup_order'] = 48
        return solver, members, metadata

    upstream.group = lambda _p=5: G
    upstream.build_solver = build
    upstream.run([13, 13, 15], args.seconds, args.seed, args.output,
                 max_models=1000, engine='cadical195')


if __name__ == '__main__':
    main()
