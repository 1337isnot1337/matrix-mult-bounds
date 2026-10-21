"""Exact triangular elimination for the specified monic polynomial flag ansatz.

No assertion that fixing every pivot to one is lossless. All elimination
denominators are nonzero rational constants, not unknown expressions.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
import json
from pathlib import Path
import sympy as sp


class System:
    def __init__(self):
        self.m, self.B, self.eta, self.beta = 4, 10, [0, 201, 403, 607], 100
        self.points = [(a, d-a) for d in range(4) for a in range(d+1)]
        wy = [self.eta[a+b]-100*a for a,b in self.points]
        wz = [-self.eta[3-c-d]-100*c for c,d in self.points]
        ry = {v:i for i,v in enumerate(sorted(wy))}
        rz = {v:i for i,v in enumerate(sorted(wz))}
        self.degrees = [[3-p for p in range(4)], [9-ry[w] for w in wy],
                        [12-rz[w] for w in wz]]
        self.keys = []; self.index = {}; self.variables = defaultdict(list)
        self.constant_values = {}
        for leg, degrees in enumerate(self.degrees):
            for row, degree in enumerate(degrees):
                for drop in range(degree+1):
                    key = (leg, row, drop)
                    index = len(self.keys)
                    self.index[key] = index; self.keys.append(key)
                    if drop == 0:
                        self.constant_values[index] = Fraction(1)
                    elif key == (0, 2, 1):
                        self.constant_values[index] = Fraction(0)
                    else:
                        self.variables[drop].append(index)
        self.constraints = defaultdict(list)
        for p in range(4):
            for y, (a,b) in enumerate(self.points):
                for z, (c,d) in enumerate(self.points):
                    if 100*p+wy[y]+wz[z] > 0: continue
                    wanted = int(p == a+c and a+b+c+d == 3)
                    delta = self.degrees[0][p]+self.degrees[1][y]-(12-self.degrees[2][z])
                    if delta < 0:
                        if wanted: raise ArithmeticError('target identically absent')
                    else:
                        self.constraints[delta].append((p,y,z,wanted))
        self.levels = []; self.free = []
        for level in range(1, 13):
            variables = self.variables[level]
            local = {index:column for column,index in enumerate(variables)}
            constraints = self.constraints[level]
            matrix = sp.zeros(len(constraints), len(variables))
            terms = []
            for row, (p,y,z,_) in enumerate(constraints):
                row_terms = []
                for i in range(min(level, self.degrees[0][p])+1):
                    for j in range(min(level-i, self.degrees[1][y])+1):
                        k = level-i-j
                        if k > self.degrees[2][z]: continue
                        indices = [self.index[(leg,coordinate,drop)]
                                   for leg,coordinate,drop in [(0,p,i),(1,y,j),(2,z,k)]]
                        if level in [i,j,k]:
                            for index in indices:
                                if index in local: matrix[row,local[index]] += 1
                        else:
                            row_terms.append(tuple(indices))
                terms.append(row_terms)
            pivots = list(matrix.rref()[1])
            rows = list(matrix.T.rref()[1])
            free_columns = [j for j in range(len(variables)) if j not in pivots]
            free_indices = [variables[j] for j in free_columns]
            self.free.extend(free_indices)
            inverse = matrix.extract(rows, pivots).inv() if pivots else sp.zeros(0)
            self.levels.append({'level':level, 'variables':variables,
                                'constraints':constraints, 'matrix':matrix, 'terms':terms,
                                'pivots':pivots, 'rows':rows, 'inverse':inverse,
                                'free_columns':free_columns, 'free_indices':free_indices,
                                'remaining_rows':[j for j in range(len(constraints)) if j not in rows]})
        self.free_position = {index:i for i,index in enumerate(self.free)}

    def evaluate_exact(self, free):
        if len(free) != len(self.free): raise ValueError('wrong parameter count')
        values = [Fraction(0)]*len(self.keys)
        for index,value in self.constant_values.items(): values[index] = value
        for index,value in zip(self.free, free): values[index] = Fraction(value)
        residuals = []
        for level in self.levels:
            lower = [sum((values[a]*values[b]*values[c] for a,b,c in terms), Fraction(0))
                     for terms in level['terms']]
            matrix = level['matrix']
            rhs = [Fraction(constraint[3])-value for constraint,value in zip(level['constraints'],lower)]
            for row in range(len(rhs)):
                rhs[row] -= sum((Fraction(matrix[row,column])*values[level['variables'][column]]
                                 for column in level['free_columns']), Fraction(0))
            for j,column in enumerate(level['pivots']):
                values[level['variables'][column]] = sum(
                    (Fraction(level['inverse'][j,k])*rhs[row] for k,row in enumerate(level['rows'])), Fraction(0))
            for row in level['remaining_rows']:
                residuals.append(sum((Fraction(matrix[row,j])*values[index]
                                      for j,index in enumerate(level['variables'])), Fraction(0))
                                 +lower[row]-level['constraints'][row][3])
        return residuals, values

    def matrices(self, values):
        matrices = [sp.zeros(4), sp.zeros(10, 10), sp.zeros(10, 13)]
        for (leg,row,drop),value in zip(self.keys, values):
            degree = self.degrees[leg][row]
            column = degree-drop if leg < 2 else 12-degree+drop
            matrices[leg][row,column] = sp.Rational(value)
        return matrices

    def summary(self):
        return {'m':4, 'B':10, 'eta':self.eta, 'beta':100,
                'all_pivots_one':True, 'ansatz_is_lossless':False,
                'initial_complex_variables':sum(map(len,self.variables.values())),
                'retained_complex_parameters':len(self.free),
                'polynomial_conditions':sum(len(level['remaining_rows']) for level in self.levels),
                'levels':[{'distance':s['level'], 'variables':len(s['variables']),
                           'equations':len(s['constraints']), 'eliminated':len(s['pivots']),
                           'free':len(s['free_columns']), 'conditions':len(s['remaining_rows'])}
                          for s in self.levels],
                'free_coordinates':[list(self.keys[index]) for index in self.free],
                'coefficient_denominators_depend_on_parameters':False,
                'exact_solution_found':False, 'improves_omega':False}


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    text = json.dumps(System().summary(), indent=2)+'\n'
    if args.output: args.output.write_text(text)
    print(text, end='')
