"""Unit triangular elimination for the new compatible weight chamber.

Reconstructed after the execution interruption from the recorded chamber
and the predecessor's integer elimination method. This is not a solution.
"""
from collections import defaultdict
import argparse
import json
from pathlib import Path
import sympy as sp

from chamber_system import ChamberModel


def build_model(eta=(0, 301, 628, 844), beta=100):
    model = ChamberModel(list(eta), beta)
    s = model.system
    variables = defaultdict(list)
    for index, (_, _, drop) in enumerate(s.keys):
        if index not in s.constant_values:
            variables[drop].append(index)
    s.levels, s.free = [], []
    for distance in range(1, 13):
        indices = variables[distance]
        local = {index: column for column, index in enumerate(indices)}
        constraints = s.constraints[distance]
        matrix = sp.zeros(len(constraints), len(indices))
        terms = []
        for row, (p, y, z, _) in enumerate(constraints):
            lower = []
            for i in range(min(distance, s.degrees[0][p]) + 1):
                for j in range(min(distance-i, s.degrees[1][y]) + 1):
                    k = distance-i-j
                    if k > s.degrees[2][z]:
                        continue
                    triple = tuple(s.index[key] for key in ((0,p,i),(1,y,j),(2,z,k)))
                    if distance in (i,j,k):
                        for index in triple:
                            if index in local:
                                matrix[row,local[index]] += 1
                    else:
                        lower.append(triple)
            terms.append(lower)
        pivots = list(matrix.rref()[1])
        rows = list(matrix.T.rref()[1])
        free_columns = [j for j in range(len(indices)) if j not in pivots]
        minor = matrix.extract(rows, pivots)
        determinant = int(minor.det()) if pivots else 1
        if determinant not in (-1, 1):
            raise ArithmeticError('an elimination minor is not a unit')
        free_indices = [indices[j] for j in free_columns]
        s.free.extend(free_indices)
        s.levels.append({
            'level':distance, 'variables':indices, 'constraints':constraints,
            'matrix':matrix, 'terms':terms, 'pivots':pivots, 'rows':rows,
            'inverse':minor.inv() if pivots else sp.zeros(0),
            'minor_determinant':determinant, 'free_columns':free_columns,
            'free_indices':free_indices,
            'remaining_rows':[j for j in range(len(constraints)) if j not in rows],
        })
    s.free_position = {index: j for j, index in enumerate(s.free)}
    return model


def report(model):
    s = model.system
    return {
        'eta':s.eta, 'beta':s.beta, 'nonpositive_coefficients':len(model.equations),
        'eliminated_coefficients':sum(len(level['pivots']) for level in s.levels),
        'free_monic_coefficients':len(s.free), 'nonzero_target_scalars':len(model.columns),
        'remaining_equations':sum(len(level['remaining_rows']) for level in s.levels),
        'levels':[{'distance':level['level'], 'variables':len(level['variables']),
                   'equations':len(level['constraints']), 'rank':len(level['pivots']),
                   'minor_determinant':level['minor_determinant']}
                  for level in s.levels],
        'exact_solution_found':False, 'improves_omega':False,
        'provenance':'Reconstructed after interruption; counts and coefficient replay recomputed.',
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    data = report(build_model())
    text = json.dumps(data, indent=2)+'\n'
    if args.output:
        args.output.write_text(text)
    print(text, end='')
