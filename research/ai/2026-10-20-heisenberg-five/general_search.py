"""Full Heisenberg(5) color search with exact abelian-fiber necessary clauses."""
import argparse
from itertools import combinations, product
from pathlib import Path
import sys

from source import group, RESEARCH
sys.path.insert(0, str(RESEARCH/'2026-10-20-sl2-seven/imported'))
from pysat.card import CardEnc
import search


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--seconds', type=float, default=600)
    parser.add_argument('--first-projection-index', type=int)
    parser.add_argument('--central-shear', action='store_true')
    args = parser.parse_args()
    G = group()
    directions = [(1, slope) for slope in range(5)]+[(0, 1)]
    fibers = [[sorted(q for q in range(25)
                      if (a*(q % 5)-b*(q//5)) % 5 == k) for k in range(5)]
              for a, b in directions]
    original = search.build_solver

    def build(source, shape, seed, engine):
        solver, members, metadata = original(source, shape, seed, engine)
        top = metadata['variables']
        presence = []
        for f in range(3):
            row = []
            for q in range(25):
                top += 1
                variable = top
                row.append(variable)
                colors = [members[f][5*q+c] for c in range(5)]
                solver.add_clause([-variable]+colors)
                for v in colors:
                    solver.add_clause([-v, variable])
                for v, w in combinations(colors, 2):
                    solver.add_clause([-v, -w])
            card = CardEnc.equals(row, 10, top_id=top)
            solver.append_formula(card.clauses)
            top = card.nv
            presence.append(row)
        for d in range(6):
            flags = []
            for f in range(3):
                row = {}
                for threshold in (3, 4, 5):
                    top += 1
                    row[threshold] = top
                    for fiber in fibers[d]:
                        for chosen in combinations(fiber, threshold):
                            solver.add_clause([-presence[f][q] for q in chosen]+[top])
                flags.append(row)
            solver.add_clause([-flags[f][3] for f in range(3)])
            for f, h in combinations(range(3), 2):
                solver.add_clause([-flags[f][4], -flags[h][4]])
            for f in range(3):
                for h in range(3):
                    if f != h:
                        solver.add_clause([-flags[f][5], -flags[h][3]])
        # Six directions are covered by three sets; one set is balanced on
        # two directions. Leg and common group automorphisms place it first
        # and send those directions to horizontal and vertical.
        for coordinate in (0, 1):
            for k in range(5):
                row = [presence[0][q] for q in range(25)
                       if (q//5 if coordinate == 0 else q % 5) == k]
                card = CardEnc.equals(row, 2, top_id=top)
                solver.append_formula(card.clauses)
                top = card.nv
        if args.first_projection_index is not None:
            from projection_orbits import derive
            options = derive()['affine_coordinate_orbits']
            if not 0 <= args.first_projection_index < len(options):
                raise ValueError('first projection index must lie in 0..6')
            selected = options[args.first_projection_index]['representative']
            for q, variable in enumerate(presence[0]):
                solver.add_clause([variable if q in selected else -variable])
            metadata['first_projection_orbit_index'] = args.first_projection_index
            metadata['fixed_first_projection'] = selected
            if args.central_shear:
                if not {1, 5} <= set(selected):
                    raise ArithmeticError('shear anchors missing from this representative')
                solver.add_clause([members[0][5]])   # (0,1,0)
                solver.add_clause([members[0][25]])  # (1,0,0)
                metadata['central_shear_anchor_elements'] = [5, 25]
        elif args.central_shear:
            raise ValueError('central shear normalization needs a fixed projection')
        metadata.update(projected_points=25, central_colors=5,
            abelian_fiber_directions=6, first_projection_row_and_column_sums=2,
            variables_with_fiber_constraints=top,
            normalization_status='written derivation; no independent review')
        return solver, members, metadata

    search.group = lambda _p=5: G
    search.build_solver = build
    search.run([10]*3, args.seconds, 20260511, args.output, 1000, engine='cadical195')


if __name__ == '__main__':
    main()
